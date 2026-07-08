#!/usr/bin/env python3
"""Structural heuristics gate for the patent-essay pipeline.

DRAFT FORMAT ASSUMPTIONS (see gate_emdash.py for the full shared list):
  - Markdown. A "body paragraph" is a maximal run of non-blank lines that is
    neither a header, a fenced code block, nor a list (bullet/numbered) run.
  - Bold spans are **...** (asterisk) or __...__ (underscore).
  - Bullet lines start with '-', '*', '+', or 'N.' (numbered).

IMPORTANT: real upstream formats are TBD; these heuristics use the documented
pragmatic conventions and are easily retargeted. EVERY check here is WARN
severity (never a hard fail) by design — they flag style risks, not blockers.

Checks (all warn):
  STRUCT-001: a body paragraph with more than 7 sentences (8+ is a Pass 2C high).
  STRUCT-002: bold-overuse — more than MAX_BOLD_PER_100_WORDS bold spans /100 words.
  STRUCT-003: bullet-overuse — bullet lines > MAX_BULLET_FRACTION of non-blank lines.
  STRUCT-004: rule-of-three — sentences with an "A, B, and C" triad of short items.
"""

import argparse
import re
import sys

# ---------------------------------------------------------------------------
# Tunable constants
# ---------------------------------------------------------------------------
GATE_ID = "structure"
# Editorial Pass 2C flags >= 8 sentences as high; the gate warns at the same boundary.
MAX_SENTENCES_PER_PARA = 7       # STRUCT-001: warn when a paragraph exceeds the 3-7 band
MAX_BOLD_PER_100_WORDS = 2       # STRUCT-002 threshold (spans per 100 words)
MAX_BULLET_FRACTION = 0.35       # STRUCT-003 threshold (fraction of non-blank lines)

FENCE_RE = re.compile(r"^\s*(```|~~~)")
HEADER_RE = re.compile(r"^\s*#{1,6}\s+")
BULLET_RE = re.compile(r"^\s*(?:[-*+]|\d+\.)\s+")
BOLD_RE = re.compile(r"\*\*[^*]+?\*\*|__[^_]+?__")
# Sentence splitter: terminal punctuation followed by whitespace/EOL.
SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?])\s+")
# Rule-of-three: "<word>, <word>, and <word>" with short single-token items.
# Conservative: items are 1 short word (letters/hyphen), to avoid false hits.
RULE_OF_THREE_RE = re.compile(
    r"\b([A-Za-z][A-Za-z-]{1,14}),\s+([A-Za-z][A-Za-z-]{1,14}),\s+and\s+([A-Za-z][A-Za-z-]{1,14})\b")


def _count_sentences(text):
    text = text.strip()
    if not text:
        return 0
    parts = [s for s in SENTENCE_SPLIT_RE.split(text) if s.strip()]
    return len(parts) if parts else 1


def _strip_code_blocks(lines):
    """Return list of (lineno, line) with fenced code-block lines removed."""
    kept = []
    in_fence = False
    for i, raw in enumerate(lines, start=1):
        if FENCE_RE.match(raw):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        kept.append((i, raw))
    return kept


def check(draft_text: str, context: dict) -> dict:
    findings = []
    lines = draft_text.splitlines()
    kept = _strip_code_blocks(lines)

    # --- group into body paragraphs (skip headers + bullet runs) ------------
    paragraphs = []  # list of (start_lineno, text)
    buf = []
    buf_start = None
    for lineno, raw in kept:
        if not raw.strip():
            if buf:
                paragraphs.append((buf_start, " ".join(buf)))
                buf, buf_start = [], None
            continue
        if HEADER_RE.match(raw) or BULLET_RE.match(raw):
            if buf:
                paragraphs.append((buf_start, " ".join(buf)))
                buf, buf_start = [], None
            continue
        if buf_start is None:
            buf_start = lineno
        buf.append(raw.strip())
    if buf:
        paragraphs.append((buf_start, " ".join(buf)))

    # STRUCT-001: long paragraphs
    for start, text in paragraphs:
        n = _count_sentences(text)
        if n > MAX_SENTENCES_PER_PARA:
            findings.append({
                "check_id": "STRUCT-001",
                "severity": "warn",
                "message": "paragraph has %d sentences (max %d)" % (n, MAX_SENTENCES_PER_PARA),
                "location": "line %d" % start,
            })

    # STRUCT-002: bold overuse (whole document, excluding code)
    body_text = "\n".join(raw for _l, raw in kept)
    words = re.findall(r"\S+", body_text)
    n_words = len(words)
    n_bold = len(BOLD_RE.findall(body_text))
    if n_words >= 100:  # ratio only meaningful with enough text
        per_100 = n_bold * 100.0 / n_words
        if per_100 > MAX_BOLD_PER_100_WORDS:
            findings.append({
                "check_id": "STRUCT-002",
                "severity": "warn",
                "message": "bold overuse: %.1f bold spans per 100 words (max %d); %d spans / %d words"
                           % (per_100, MAX_BOLD_PER_100_WORDS, n_bold, n_words),
                "location": "(document)",
            })

    # STRUCT-003: bullet overuse
    non_blank = [(l, r) for l, r in kept if r.strip()]
    if non_blank:
        bullets = sum(1 for _l, r in non_blank if BULLET_RE.match(r))
        frac = bullets / float(len(non_blank))
        if frac > MAX_BULLET_FRACTION:
            findings.append({
                "check_id": "STRUCT-003",
                "severity": "warn",
                "message": "bullet overuse: %.0f%% of non-blank lines are bullets (max %.0f%%)"
                           % (frac * 100, MAX_BULLET_FRACTION * 100),
                "location": "(document)",
            })

    # STRUCT-004: rule-of-three triads (conservative, counted)
    triad_count = 0
    first_loc = None
    for lineno, raw in kept:
        for _m in RULE_OF_THREE_RE.finditer(raw):
            triad_count += 1
            if first_loc is None:
                first_loc = lineno
    if triad_count:
        findings.append({
            "check_id": "STRUCT-004",
            "severity": "warn",
            "message": "rule-of-three: %d 'A, B, and C' triad(s) detected" % triad_count,
            "location": "line %d (first)" % first_loc,
        })

    # All checks are warn -> the gate always "passes" (no fail severity).
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
    p = argparse.ArgumentParser(description="Structure gate (%s)" % GATE_ID)
    p.add_argument("draft", help="path to the draft Markdown file")
    args = p.parse_args(argv)
    with open(args.draft, "r", encoding="utf-8") as fh:
        text = fh.read()
    result = check(text, {})
    _report(result)
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
