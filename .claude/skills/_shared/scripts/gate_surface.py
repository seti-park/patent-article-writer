#!/usr/bin/env python3
"""Surface / feed-context gate for the patent-essay pipeline.

The 2026-07-04 reader-first overhaul (docs/architecture/reader-first-overhaul.md,
row T9) added an energy contract that binds the SURFACE of the essay -- the
title, the cover caption, and the lead's opening sentences -- the part a reader
sees in a feed or card before ever opening the piece. These are the mechanical
half of that contract. They never touch body accuracy, and (like
gate_structure.py) every check here is WARN severity by design: a title that
reads well in isolation can still sit on a bad essay, and vice versa, so this
is a nudge, not a blocker.

DRAFT FORMAT ASSUMPTIONS (see gate_emdash.py for the full shared list): the
draft is Markdown, with an optional leading YAML frontmatter block delimited by
`---` lines; the title is the first `#` (H1) line; a cover image is a
`![alt](src)` line; a cover caption is a standalone italic `*...*` line. "Body"
begins after that structural matter (frontmatter, title, cover image, cover
caption) and after any `##` section header.

Checks (all warn):
  SURF-001: the H1 title exceeds TITLE_MAX_CHARS (markdown '#' and a trailing
            period stripped before counting) -- a feed card truncates a long
            title, so the whole hook must fit inside the limit.
  SURF-002: the first body sentence is qualifier-led (reuses gate_hedge's
            qualifier-led-verdict lexicon/detector). The lead's job is the
            hook, not a pre-hedged verdict; the call belongs at the END of the
            lead, per the hook-first lead directive (T5), not its first word.
  SURF-003: the cover caption carries more than SURF003_MAX_NUMERALS distinct
            reference-numeral tokens -- a caption dense with part numbers reads
            as a parts diagram, not an invitation, in a feed preview.
  SURF-004: a defensive-open lexicon hit (status / lien / rejection language)
            lands in the first two body sentences -- discovery must come
            before insurance; stacking disclaimers ahead of the hook is the
            report-genre failure (verdict-insurance-first) this overhaul
            targets.
  SURF-005: the lead section (the prose between the first and second `##`
            section headings) carries more than SURF005_MAX_PROC_SENTENCES
            sentence(s) naming prosecution/finance procedure (examiner, RCE,
            fee, docket, paying, ...). The lead's attention budget is for the
            invention, not a blow-by-blow of the patent office's paperwork or
            the applicant's ledger; that narration belongs later, priced once.
  SURF-006: the spend-motif lexicon (pay/paid/paying/payment/spend/spending/
            spent/fee) appears more than SURF006_MAX_SPEND_MOTIF times across
            the whole essay's body prose -- a paying/fee refrain repeated
            through the piece re-litigates the same pricing beat instead of
            stating it once and moving on.
  SURF-007: the concession/steelman section (the non-lead `##` section with
            the most CONCESSION_MARKER hits, if any section clears
            SURF007_MIN_MARKERS) carries a spend/procedure motif (the same
            SURF-006 lexicon) at or above SURF007_MIN_SPEND -- the
            "steelman-overweight" mechanical half (reader-energy.md #6 /
            meta/improvement-proposals/2026-07-06-steelman-two-sided.md): a
            concede beat that rides on paying/fee narration reads as
            safe-harbor instead of a specific, bounded objection.
"""

import argparse
import os
import re
import sys

# Allow running both as a script and as a module (mirrors run_gates.py).
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import gate_hedge  # reuse its qualifier-led-verdict lexicon for SURF-002

# ---------------------------------------------------------------------------
# Tunable constants
# ---------------------------------------------------------------------------
GATE_ID = "surface"

TITLE_MAX_CHARS = 70        # SURF-001
SURF003_MAX_NUMERALS = 6    # SURF-003
SURF005_MAX_PROC_SENTENCES = 1   # SURF-005
SURF006_MAX_SPEND_MOTIF = 4      # SURF-006
SURF007_MIN_MARKERS = 2          # SURF-007: min CONCESSION_MARKER hits to identify the beat
SURF007_MIN_SPEND = 1            # SURF-007: min spend-motif hits inside the beat to warn

HEADING_RE = re.compile(r"^#{1,6}\s+")
H1_RE = re.compile(r"^#\s+(.*)$")
SECTION_H2_RE = re.compile(r"^##\s+\S")
IMAGE_RE = re.compile(r"^!\[")
# A standalone italic line: single leading '*' (not '**bold**'), closing '*'.
CAPTION_RE = re.compile(r"^\*(?!\*).*\*\s*$")
BLOCKQUOTE_RE = re.compile(r"^>")
SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?])\s+")
NUMERAL_TOKEN_RE = re.compile(r"\b\d{3,4}[A-Za-z]?\b")

# SURF-002: identical detector gate_hedge uses for a qualifier-led verdict
# ("a qualified yes", "the cautious no", ...), applied here to the lead's
# first sentence instead of the verdict section.
QUALIFIER_LED_RE = gate_hedge.QUALIFIER_LED_RE

# SURF-004: status / insurance lexicon. Case-insensitive substring match.
DEFENSIVE_OPEN_TERMS = [
    "pending application",
    "not an asset",
    "final rejection",
    "loan collateral",
    "security interest",
    "no claim has been",
    "not a patent",
    "abandoned",
]

# SURF-005: prosecution / finance procedure-narration lexicon. Deliberately
# EXCLUDES status words ("pending", "granted", "patent office") -- the status
# label is required content; it is the blow-by-blow PROCESS of getting there
# (and paying for it) that is budgeted. Also excludes borrow/borrowing/secured
# (the lending story is a separate, legitimate beat, not prosecution
# narration). "RCE" is matched case-sensitively in its own regex so lowercase
# words like "force" never match.
PROCEDURE_TERM_RE = re.compile(
    r"\b(rejections?|rejected|request for continued examination|examiners?|"
    r"examinations?|fees?|filing fee|liens?|security interests?|collateral|"
    r"dockets?|docketed|prosecution|paid|paying|pay to|spends?|spending|spent)\b",
    re.I,
)
RCE_TERM_RE = re.compile(r"\bRCE\b")  # case-sensitive: only the all-caps acronym

# SURF-006: spend-motif lexicon (whole-essay prose count).
SPEND_MOTIF_RE = re.compile(
    r"\b(pay|pays|paid|paying|payments?|spends?|spending|spent|fees?)\b", re.I
)

# SURF-007: concession/steelman-beat marker lexicon, used to LOCATE the
# concede-the-strongest-objection section (not to judge it) -- the section
# with the most hits is the candidate concession beat.
CONCESSION_MARKER_RE = re.compile(
    r"\b(concede[sd]?|conceding|objection|read cold|the dissection|"
    r"no single claim|strongest (objection|counter)|cuts deeper|boilerplate|"
    r"one filing among|bear case|for all that|granting that)\b",
    re.I,
)


def _mask_quoted_spans(text):
    """Blank out double-quoted span contents (keep the quote chars).

    Same approach as the other gates (gate_emdash.py, gate_hedge.py): text
    inside "..." is verbatim source and exempt from these checks.
    """
    out, in_q = [], False
    for ch in text:
        if ch == '"':
            out.append(ch)
            in_q = not in_q
        elif in_q:
            out.append(" ")
        else:
            out.append(ch)
    return "".join(out)


def _strip_frontmatter(draft_text):
    """Return the draft's lines with a leading YAML frontmatter block removed."""
    lines = draft_text.splitlines()
    if lines and lines[0].strip() == "---":
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                return lines[i + 1:]
    return lines


def _title_line(draft_text):
    """Return the H1 title's text (markdown '#' stripped), or None."""
    for raw in _strip_frontmatter(draft_text):
        line = raw.strip()
        if not line:
            continue
        m = H1_RE.match(line)
        return m.group(1).strip() if m else None
    return None


def _cover_caption(draft_text):
    """First standalone italic caption line that appears before the first ## section."""
    lines = _strip_frontmatter(draft_text)
    limit = len(lines)
    for i, raw in enumerate(lines):
        if SECTION_H2_RE.match(raw.strip()):
            limit = i
            break
    for raw in lines[:limit]:
        line = raw.strip()
        if CAPTION_RE.match(line):
            return line
    return None


def _body_paragraphs(draft_text):
    """Body prose paragraphs: headers, images, captions, blockquotes excluded."""
    paragraphs = []
    buf = []
    for raw in _strip_frontmatter(draft_text):
        line = raw.strip()
        structural = (not line or HEADING_RE.match(line) or IMAGE_RE.match(line)
                      or CAPTION_RE.match(line) or BLOCKQUOTE_RE.match(line))
        if structural:
            if buf:
                paragraphs.append(" ".join(buf))
                buf = []
            continue
        buf.append(line)
    if buf:
        paragraphs.append(" ".join(buf))
    return paragraphs


def _lead_section_paragraphs(draft_text):
    """Body prose paragraphs strictly between the first and second `## ` headings.

    Same structural-line exclusion as _body_paragraphs (blank lines, headings,
    images, standalone-italic captions, blockquotes are skipped). If the draft
    has no `## ` section heading at all, returns []. If it has exactly one,
    the lead section runs to the end of the document.
    """
    lines = _strip_frontmatter(draft_text)
    h2_indices = [i for i, raw in enumerate(lines) if SECTION_H2_RE.match(raw.strip())]
    if not h2_indices:
        return []
    start = h2_indices[0] + 1
    end = h2_indices[1] if len(h2_indices) > 1 else len(lines)

    paragraphs = []
    buf = []
    for raw in lines[start:end]:
        line = raw.strip()
        structural = (not line or HEADING_RE.match(line) or IMAGE_RE.match(line)
                      or CAPTION_RE.match(line) or BLOCKQUOTE_RE.match(line))
        if structural:
            if buf:
                paragraphs.append(" ".join(buf))
                buf = []
            continue
        buf.append(line)
    if buf:
        paragraphs.append(" ".join(buf))
    return paragraphs


def _non_lead_sections(draft_text):
    """List of (header_text, paragraphs) for every `## ` section AFTER the lead.

    Mirrors _lead_section_paragraphs's own h2-boundary logic, but returns each
    subsequent section instead of only the first. If the draft has fewer than
    two `## ` headings, there is no non-lead section and [] is returned.
    """
    lines = _strip_frontmatter(draft_text)
    h2_indices = [i for i, raw in enumerate(lines) if SECTION_H2_RE.match(raw.strip())]
    if len(h2_indices) < 2:
        return []

    sections = []
    for idx, start_i in enumerate(h2_indices[1:], start=1):
        header = lines[start_i].strip().lstrip("#").strip()
        end_i = h2_indices[idx + 1] if idx + 1 < len(h2_indices) else len(lines)
        paragraphs = []
        buf = []
        for raw in lines[start_i + 1:end_i]:
            line = raw.strip()
            structural = (not line or HEADING_RE.match(line) or IMAGE_RE.match(line)
                          or CAPTION_RE.match(line) or BLOCKQUOTE_RE.match(line))
            if structural:
                if buf:
                    paragraphs.append(" ".join(buf))
                    buf = []
                continue
            buf.append(line)
        if buf:
            paragraphs.append(" ".join(buf))
        sections.append((header, paragraphs))
    return sections


def _first_body_sentences(draft_text, n):
    """First n sentences of body prose, in document order across paragraphs."""
    sentences = []
    for para in _body_paragraphs(draft_text):
        for s in SENTENCE_SPLIT_RE.split(para):
            if s.strip():
                sentences.append(s.strip())
            if len(sentences) >= n:
                return sentences
    return sentences


def check(draft_text: str, context: dict) -> dict:
    findings = []

    # SURF-001: H1 title length.
    title = _title_line(draft_text)
    if title:
        stripped = title.rstrip()
        if stripped.endswith("."):
            stripped = stripped[:-1]
        n = len(stripped)
        if n > TITLE_MAX_CHARS:
            findings.append({
                "check_id": "SURF-001",
                "severity": "warn",
                "message": "H1 title is %d characters (max %d); a feed card truncates it"
                           % (n, TITLE_MAX_CHARS),
                "location": "title line",
            })

    # SURF-002: qualifier-led first body sentence.
    first = _first_body_sentences(draft_text, 1)
    if first:
        scan = _mask_quoted_spans(first[0])
        m = QUALIFIER_LED_RE.search(scan)
        if m:
            findings.append({
                "check_id": "SURF-002",
                "severity": "warn",
                "message": "first body sentence is qualifier-led (\"%s\"); the hook "
                           "comes first, the call lands at the end of the lead"
                           % m.group(0),
                "location": "first body sentence",
            })

    # SURF-003: cover-caption reference-numeral density.
    caption = _cover_caption(draft_text)
    if caption:
        tokens = set(NUMERAL_TOKEN_RE.findall(caption))
        if len(tokens) > SURF003_MAX_NUMERALS:
            findings.append({
                "check_id": "SURF-003",
                "severity": "warn",
                "message": "cover caption carries %d distinct reference-numeral tokens "
                           "(max %d): %s" % (len(tokens), SURF003_MAX_NUMERALS,
                                             ", ".join(sorted(tokens))),
                "location": "cover caption",
            })

    # SURF-004: defensive-open lexicon in the first two body sentences.
    first_two = _first_body_sentences(draft_text, 2)
    if first_two:
        scan = _mask_quoted_spans(" ".join(first_two)).lower()
        hits = [term for term in DEFENSIVE_OPEN_TERMS if term in scan]
        if hits:
            findings.append({
                "check_id": "SURF-004",
                "severity": "warn",
                "message": "defensive-open lexicon in the first two body sentences: %s"
                           % ", ".join(hits),
                "location": "first two body sentences",
            })

    # SURF-005: procedure-narration density in the lead section.
    lead_paragraphs = _lead_section_paragraphs(draft_text)
    if lead_paragraphs:
        proc_sentence_count = 0
        for para in lead_paragraphs:
            masked = _mask_quoted_spans(para)
            for s in SENTENCE_SPLIT_RE.split(masked):
                s = s.strip()
                if not s:
                    continue
                if PROCEDURE_TERM_RE.search(s) or RCE_TERM_RE.search(s):
                    proc_sentence_count += 1
        if proc_sentence_count > SURF005_MAX_PROC_SENTENCES:
            findings.append({
                "check_id": "SURF-005",
                "severity": "warn",
                "message": "lead section carries %d procedure-narration sentences (max %d): "
                           "prosecution/finance process is pricing context, not the plot "
                           "(reader-energy.md attention budget)"
                           % (proc_sentence_count, SURF005_MAX_PROC_SENTENCES),
                "location": "lead section",
            })

    # SURF-006: spend-motif count across the whole essay's body prose.
    spend_count = 0
    for para in _body_paragraphs(draft_text):
        masked = _mask_quoted_spans(para)
        spend_count += len(SPEND_MOTIF_RE.findall(masked))
    if spend_count > SURF006_MAX_SPEND_MOTIF:
        findings.append({
            "check_id": "SURF-006",
            "severity": "warn",
            "message": "spend-motif appears %d times in prose (max %d): repeated paying/fee "
                       "language re-litigates the pricing beat (reader-energy.md attention "
                       "budget)" % (spend_count, SURF006_MAX_SPEND_MOTIF),
            "location": "(document)",
        })

    # SURF-007: spend/procedure motif inside the concession/steelman beat.
    best_header, best_marker_count, best_spend_count = None, 0, 0
    for header, paragraphs in _non_lead_sections(draft_text):
        marker_count = 0
        spend_count_section = 0
        for para in paragraphs:
            masked = _mask_quoted_spans(para)
            marker_count += len(CONCESSION_MARKER_RE.findall(masked))
            spend_count_section += len(SPEND_MOTIF_RE.findall(masked))
        if marker_count > best_marker_count:
            best_header = header
            best_marker_count = marker_count
            best_spend_count = spend_count_section
    if best_header is not None and best_marker_count >= SURF007_MIN_MARKERS:
        if best_spend_count >= SURF007_MIN_SPEND:
            findings.append({
                "check_id": "SURF-007",
                "severity": "warn",
                "message": "concession/steelman section '%s' carries a spend/procedure "
                           "motif (%d hit(s)) -- steelman-overweight mechanical half; the "
                           "concede beat reads as safe-harbor. See reader-energy.md #6."
                           % (best_header, best_spend_count),
                "location": "concession section: %s" % best_header,
            })

    passed = not any(f["severity"] == "fail" for f in findings)
    return {"gate": GATE_ID, "passed": passed, "findings": findings}


def _report(result):
    status = "PASS" if result["passed"] else "FAIL"
    print("[%s] gate=%s" % (status, result["gate"]))
    for f in result["findings"]:
        print("  %-5s %-12s %s  (%s)" % (
            f["severity"].upper(), f["check_id"], f["message"], f["location"]))
    if not result["findings"]:
        print("  (no findings)")


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description="Surface gate (%s)" % GATE_ID)
    p.add_argument("draft", help="path to the draft Markdown file")
    args = p.parse_args(argv)
    with open(args.draft, "r", encoding="utf-8") as fh:
        text = fh.read()
    result = check(text, {})
    _report(result)
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
