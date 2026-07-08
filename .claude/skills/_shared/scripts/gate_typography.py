#!/usr/bin/env python3
"""Typography / plain-English gate for the patent-essay pipeline.

The GOV.UK-base hygiene checks that the other gates did not yet cover. These are
the mechanically-safe subset of the govuk-style rules; the nuanced ones (number
and date style, plain-word swaps that depend on sense) stay in
`deliverable-voice-rules.md` / `anti-ai-writing.md` for editorial judgment.

DRAFT FORMAT ASSUMPTIONS (shared with the other gates; see gate_emdash.py):
  - Markdown draft.
  - "Quoted text" = inside double quotes ("...") OR a Markdown blockquote ('>').
    Everything inside is verbatim source and is EXEMPT from every check here.
  - Fenced code blocks (``` / ~~~) are EXEMPT.
  - Patent reality is respected: single acronyms and part numbers (USB, LLM,
    US1234567B2, FIG) are NOT flagged; only a *run* of >=3 all-caps words reads
    as shouting. Markdown image syntax (![alt](src)) is not read as a '!'.

Checks:
  LATIN-001  (fail): Latin abbreviation 'eg' / 'ie' / 'etc' / 'e.g.' / 'i.e.'
                     outside quotes/code. Write "for example" / "that is" /
                     "and so on".
  EXCLAIM-001(fail): exclamation mark in body prose outside quotes/code.
  EMOJI-001  (warn): emoji outside quotes/code (the canon allows a single
                     closing-question 🤔, which is exempted).
  CAPS-001   (warn): a run of >=3 consecutive ALL-CAPS words (emphasis, not an
                     acronym).
  LINK-001   (warn): non-descriptive Markdown link text ("click here", "here").
  LONGSENT-001(warn): a sentence longer than LONG_SENTENCE_WORDS words. The
                     editorial target is ~15-25 words (deliverable-voice-rules);
                     this gate only flags egregious run-ons to keep the signal
                     high.

LONGSENT-001 splitter (2026-07-03-longsent-boundary-merge proposal): sentences
are never joined across a structural boundary. The draft is first partitioned
into units at: a leading YAML frontmatter block (skipped entirely, mirroring
strip_publication.py's strip_frontmatter), blank lines, ATX headings
(`^#{1,6}\s`), standalone bold lines (`^\*\*[^*]+\*\*\s*$`), image lines
(`^!\[`), table rows (`^\|`), and bullet/numbered list lines (mirroring
strip_publication.py's `_is_structural`, which already treats all of the above
as non-prose). A standalone italic caption line (`^\*[^*].*\*\s*$`) is also a
boundary, but -- unlike the others -- becomes a unit of its own rather than
being discarded, since a caption is prose worth measuring on its own merits.
Sentence-splitting then runs WITHIN each unit only, so a heading's title, a
Sources bullet, or a footnote definition can never absorb (or be absorbed by)
a neighboring sentence. A genuinely long sentence inside a unit -- including a
caption's own sentence -- still warns.
"""

import argparse
import re
import sys

# ---------------------------------------------------------------------------
# Tunable constants
# ---------------------------------------------------------------------------
GATE_ID = "typography"
LONG_SENTENCE_WORDS = 35          # warn threshold; editorial target is ~15-25
ALLOWED_EMOJI = {"\U0001F914"}    # 🤔 — sanctioned at a closing-open-question

FENCE_RE = re.compile(r"^\s*(```|~~~)")

LATIN_PATTERNS = [
    (re.compile(r"\be\.g\.", re.I), "Latin abbreviation 'e.g.' (write 'for example')"),
    (re.compile(r"\bi\.e\.", re.I), "Latin abbreviation 'i.e.' (write 'that is')"),
    (re.compile(r"\beg\b"), "Latin abbreviation 'eg' (write 'for example')"),
    (re.compile(r"\bie\b"), "Latin abbreviation 'ie' (write 'that is')"),
    (re.compile(r"\betc\b\.?", re.I), "Latin abbreviation 'etc' (write 'and so on')"),
]
# "!" not part of a Markdown image "![".
EXCLAIM_RE = re.compile(r"!(?!\[)")
# >=3 consecutive all-caps words (>=2 letters each).
CAPS_RUN_RE = re.compile(r"\b[A-Z]{2,}(?:[ \t]+[A-Z]{2,}){2,}\b")
# Non-descriptive link text.
LINK_RE = re.compile(
    r"\[\s*(click here|click|here|this link|this|read more|learn more|link|more)\s*\]\(",
    re.I,
)
EMOJI_RE = re.compile(
    "["
    "\U0001F300-\U0001FAFF"   # symbols & pictographs, emoji, supplemental
    "\U00002600-\U000026FF"   # misc symbols
    "\U00002700-\U000027BF"   # dingbats
    "\U0001F1E6-\U0001F1FF"   # regional indicators
    "]"
)
ANCHOR_RE = re.compile(r"\[\d{4}\]")
SENTENCE_SPLIT_RE = re.compile(r'(?<=[.!?])\s+(?=[A-Z0-9"\'])')
WORD_RE = re.compile(r"[\w$%]+")

# --- LONGSENT-001 structural-boundary units (never merge across these) -----
ATX_HEADING_RE = re.compile(r"^#{1,6}\s")
BOLD_LINE_RE = re.compile(r"^\*\*[^*]+\*\*\s*$")
IMAGE_LINE_RE = re.compile(r"^!\[")
TABLE_ROW_RE = re.compile(r"^\|")
BULLET_LINE_RE = re.compile(r"^\s*(?:[-*+]|\d+\.)\s+")
# Standalone italic caption: single leading '*' (not '**bold**'), closing '*'.
CAPTION_LINE_RE = re.compile(r"^\*(?!\*).*\*\s*$")


def _mask_quoted_spans(line: str) -> str:
    """Blank out the contents of double-quoted spans (keep the quote chars).

    Same approach as gate_emdash: text inside "..." is verbatim and exempt.
    """
    out = []
    in_quote = False
    for ch in line:
        if ch == '"':
            out.append(ch)
            in_quote = not in_quote
        elif in_quote:
            out.append(" ")
        else:
            out.append(ch)
    return "".join(out)


def _strip_for_count(sentence: str) -> str:
    """Drop citation anchors and leading markdown markers before counting words."""
    s = ANCHOR_RE.sub(" ", sentence)
    s = re.sub(r"^\s{0,3}(#{1,6}\s+|[-*+]\s+|>\s+)", " ", s)
    return s


def _strip_frontmatter_lines(draft_text: str):
    """Return the draft's lines with a leading YAML frontmatter block removed.

    Same tolerant rule as strip_publication.py's strip_frontmatter: only a
    frontmatter block that is actually closed is stripped.
    """
    lines = draft_text.splitlines()
    if lines and lines[0].strip() == "---":
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                return lines[i + 1:]
    return lines


def _longsent_units(draft_text: str):
    """Partition the draft into structurally-isolated units for LONGSENT-001.

    A unit never absorbs text across a structural boundary: blank lines, ATX
    headings, standalone bold lines, image lines, table rows, and bullet/
    numbered list lines all flush the current unit and are themselves
    excluded (mirroring strip_publication.py's `_is_structural`, which
    already treats every one of these as non-prose). A standalone italic
    caption line is also a boundary, but becomes a unit of its own instead of
    being discarded, since a caption is prose worth measuring on its own
    merits. Fenced code and blockquote lines are excluded entirely, same as
    the rest of this gate. Quoted spans are masked per line, same as the
    per-line checks above.
    """
    units = []
    buf = []
    in_fence = False

    def flush():
        if buf:
            units.append(" ".join(buf))
            del buf[:]

    for raw in _strip_frontmatter_lines(draft_text):
        if FENCE_RE.match(raw):
            flush()
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if raw.lstrip().startswith(">"):
            flush()
            continue

        line = raw.strip()
        if not line:
            flush()
            continue
        if (ATX_HEADING_RE.match(line) or BOLD_LINE_RE.match(line)
                or IMAGE_LINE_RE.match(line) or TABLE_ROW_RE.match(line)
                or BULLET_LINE_RE.match(raw)):
            flush()
            continue
        if CAPTION_LINE_RE.match(line):
            flush()
            units.append(_mask_quoted_spans(line))
            continue

        buf.append(_mask_quoted_spans(line))
    flush()
    return units


def check(draft_text: str, context: dict) -> dict:
    findings = []
    in_fence = False

    for lineno, raw in enumerate(draft_text.splitlines(), start=1):
        if FENCE_RE.match(raw):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        # Blockquote lines are entirely verbatim -> exempt from every check.
        if raw.lstrip().startswith(">"):
            continue

        scan = _mask_quoted_spans(raw)

        # LATIN-001 (fail)
        for pat, msg in LATIN_PATTERNS:
            for m in pat.finditer(scan):
                findings.append({
                    "check_id": "LATIN-001", "severity": "fail",
                    "message": msg,
                    "location": "line %d, col %d" % (lineno, m.start() + 1),
                })

        # EXCLAIM-001 (fail)
        for m in EXCLAIM_RE.finditer(scan):
            findings.append({
                "check_id": "EXCLAIM-001", "severity": "fail",
                "message": "exclamation mark in body prose",
                "location": "line %d, col %d" % (lineno, m.start() + 1),
            })

        # EMOJI-001 (warn) — allow the sanctioned 🤔
        for m in EMOJI_RE.finditer(scan):
            if m.group(0) in ALLOWED_EMOJI:
                continue
            findings.append({
                "check_id": "EMOJI-001", "severity": "warn",
                "message": "emoji in analytical prose (%r)" % m.group(0),
                "location": "line %d, col %d" % (lineno, m.start() + 1),
            })

        # CAPS-001 (warn)
        for m in CAPS_RUN_RE.finditer(scan):
            findings.append({
                "check_id": "CAPS-001", "severity": "warn",
                "message": "run of ALL-CAPS words reads as emphasis/shouting",
                "location": "line %d, col %d" % (lineno, m.start() + 1),
            })

        # LINK-001 (warn)
        for m in LINK_RE.finditer(scan):
            findings.append({
                "check_id": "LINK-001", "severity": "warn",
                "message": "non-descriptive link text (say where it goes, key words first)",
                "location": "line %d, col %d" % (lineno, m.start() + 1),
            })

    # LONGSENT-001 (warn) — structural units never merge into each other;
    # sentences are split, and counted, WITHIN each unit only.
    for unit in _longsent_units(draft_text):
        for sent in SENTENCE_SPLIT_RE.split(unit):
            nwords = len(WORD_RE.findall(_strip_for_count(sent)))
            if nwords > LONG_SENTENCE_WORDS:
                findings.append({
                    "check_id": "LONGSENT-001", "severity": "warn",
                    "message": "sentence runs %d words (target ~15-25)" % nwords,
                    "location": "sentence: %s..." % sent.strip()[:50],
                })

    passed = not any(f["severity"] == "fail" for f in findings)
    return {"gate": GATE_ID, "passed": passed, "findings": findings}


def _report(result: dict) -> None:
    status = "PASS" if result["passed"] else "FAIL"
    print("[%s] gate=%s" % (status, result["gate"]))
    for f in result["findings"]:
        print("  %-5s %-12s %s  (%s)" % (
            f["severity"].upper(), f["check_id"], f["message"], f["location"]))
    if not result["findings"]:
        print("  (no findings)")


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description="Typography gate (%s)" % GATE_ID)
    p.add_argument("draft", help="path to the draft Markdown file")
    args = p.parse_args(argv)
    with open(args.draft, "r", encoding="utf-8") as fh:
        text = fh.read()
    result = check(text, {})
    _report(result)
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
