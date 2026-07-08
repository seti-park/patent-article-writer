#!/usr/bin/env python3
"""Section-balance (stub) gate for the patent-essay pipeline.

Flags a body section that is a *stub* relative to its siblings -- markedly shorter,
a rhythm break that usually means the section should be merged or expanded. This is
the too-short complement of gate_structure's STRUCT-001 (too-long paragraph). Run
045 compressed a section to four sentences (a stub) and then merged it; see
meta/improvement-proposals/2026-06-26-human-revision-blindspots.md (class
`section-stub-imbalance`).

DRAFT FORMAT ASSUMPTIONS:
  - '## ' headers delimit body sections; counting STOPS at the '# Sources' H1, so
    the Sources sub-group headers (## Patents, ## Official statements, ...) are not
    counted as body sections.
  - Word count per section is its body prose (the header line itself excluded).

All checks WARN (rhythm is advisory, never a blocker).

Checks:
  STUB-001 (warn): a section with word count < max(FLOOR, RATIO * sibling median),
                   when there are at least MIN_SECTIONS body sections.
"""

import argparse
import re
import sys

GATE_ID = "stub"
MIN_SECTIONS = 3          # need enough siblings for a ratio to mean anything
STUB_FLOOR_WORDS = 50     # never flag a section at/above this absolute size
STUB_RATIO = 0.35         # flag below this fraction of the sibling median

H2_RE = re.compile(r"^\s*##\s+(.*\S)\s*$")
SOURCES_H1_RE = re.compile(r"^\s*#\s+Sources\b", re.IGNORECASE)
FENCE_RE = re.compile(r"^\s*(```|~~~)")


def _body_sections(draft_text):
    """Return [(title, lineno, word_count), ...] for ## sections before # Sources."""
    sections = []
    cur_title, cur_line, cur_words = None, None, 0
    in_fence = False
    for lineno, raw in enumerate(draft_text.splitlines(), start=1):
        if FENCE_RE.match(raw):
            in_fence = not in_fence
            if cur_title is not None and not in_fence:
                pass
            continue
        if in_fence:
            if cur_title is not None:
                cur_words += len(re.findall(r"\S+", raw))
            continue
        if SOURCES_H1_RE.match(raw):
            break
        m = H2_RE.match(raw)
        if m:
            if cur_title is not None:
                sections.append((cur_title, cur_line, cur_words))
            cur_title, cur_line, cur_words = m.group(1), lineno, 0
            continue
        if cur_title is not None:
            cur_words += len(re.findall(r"\S+", raw))
    if cur_title is not None:
        sections.append((cur_title, cur_line, cur_words))
    return sections


def _median(xs):
    s = sorted(xs)
    n = len(s)
    if n == 0:
        return 0
    mid = n // 2
    return s[mid] if n % 2 else (s[mid - 1] + s[mid]) / 2.0


def check(draft_text: str, context: dict) -> dict:
    findings = []
    sections = _body_sections(draft_text)
    if len(sections) >= MIN_SECTIONS:
        med = _median([w for _t, _l, w in sections])
        threshold = max(STUB_FLOOR_WORDS, STUB_RATIO * med)
        for title, lineno, w in sections:
            if w < threshold:
                findings.append({
                    "check_id": "STUB-001",
                    "severity": "warn",
                    "message": "section %r has %d words (< %.0f; sibling median %.0f) -- stub, merge or expand"
                               % (title, w, threshold, med),
                    "location": "line %d" % lineno,
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
    p = argparse.ArgumentParser(description="Section-balance (stub) gate (%s)" % GATE_ID)
    p.add_argument("draft", help="path to the draft Markdown file")
    args = p.parse_args(argv)
    with open(args.draft, "r", encoding="utf-8") as fh:
        text = fh.read()
    result = check(text, {})
    _report(result)
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
