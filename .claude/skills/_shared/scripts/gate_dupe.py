#!/usr/bin/env python3
"""Verbatim phrase-duplication gate for the patent-essay pipeline.

Catches gross verbatim repetition in body prose -- a distinctive multi-word phrase
appearing 2+ times -- a common revision hazard when restructuring (a clause pasted
twice, a distinctive phrase echoed). Subtle single-word echoes (the same uncommon
noun reused, e.g. run 045's "the tell" / "the clearest tell") are below this gate's
resolution and remain an editorial-pass (judgment) catch; see
meta/improvement-proposals/2026-06-26-human-revision-blindspots.md (class
`revision-induced-duplication`).

DRAFT FORMAT ASSUMPTIONS:
  - Scans BODY PROSE only: excludes quoted text (double quotes / '>' blockquotes),
    fenced code, the '# Sources' block (and everything after it), '#' headers,
    Markdown image lines, and whole-line emphasis (italic captions / bold buttons).
  - A phrase = NGRAM consecutive lowercased word-tokens; an all-stopword n-gram is
    ignored (those repeat legitimately).

All checks WARN.

Checks:
  DUPE-001 (warn): a distinctive NGRAM-word phrase occurring 2+ times in prose.
"""

import argparse
import re
import sys
from collections import defaultdict

GATE_ID = "dupe"
NGRAM = 5  # 5-word window: catches gross verbatim repeats, skips incidental 4-word echoes
FENCE_RE = re.compile(r"^\s*(```|~~~)")
SOURCES_H1_RE = re.compile(r"^\s*#\s+Sources\b", re.IGNORECASE)
HEADER_RE = re.compile(r"^\s*#{1,6}\s+")
IMAGE_RE = re.compile(r"^\s*!\[")
EMPHASIS_LINE_RE = re.compile(r"^\s*\*{1,2}.*\*{1,2}\s*$")  # whole-line italic/bold
WORD_RE = re.compile(r"[A-Za-z][A-Za-z'-]*")

STOPWORDS = set(
    "a an the of to in on at by for and or but nor so yet as is are was were be been "
    "being it its this that these those with from into out over under than then their "
    "them they he she his her you your we our us my one not no do does did has have had "
    "will would can could may might shall should must if when where which who whom whose "
    "what how why there here also only just more most some any all".split()
)


def _mask_quoted_spans(line):
    out, in_q = [], False
    for ch in line:
        if ch == '"':
            out.append(ch)
            in_q = not in_q
        elif in_q:
            out.append(" ")
        else:
            out.append(ch)
    return "".join(out)


def _prose_tokens(draft_text):
    """Lowercased word tokens of body prose, with source spans / figures excluded."""
    toks = []
    in_fence = False
    for raw in draft_text.splitlines():
        if FENCE_RE.match(raw):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if SOURCES_H1_RE.match(raw):
            break
        if (HEADER_RE.match(raw) or IMAGE_RE.match(raw)
                or EMPHASIS_LINE_RE.match(raw) or raw.lstrip().startswith(">")):
            continue
        scan = _mask_quoted_spans(raw)
        toks.extend(m.group(0).lower() for m in WORD_RE.finditer(scan))
    return toks


def check(draft_text: str, context: dict) -> dict:
    findings = []
    toks = _prose_tokens(draft_text)
    seen = defaultdict(list)
    for i in range(len(toks) - NGRAM + 1):
        gram = tuple(toks[i:i + NGRAM])
        if all(t in STOPWORDS for t in gram):
            continue
        seen[gram].append(i)
    for gram, positions in seen.items():
        if len(positions) >= 2:
            findings.append({
                "check_id": "DUPE-001",
                "severity": "warn",
                "message": "repeated %d-word phrase %r occurs %d times in prose"
                           % (NGRAM, " ".join(gram), len(positions)),
                "location": "prose token #%d" % positions[0],
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
    p = argparse.ArgumentParser(description="Verbatim phrase-duplication gate (%s)" % GATE_ID)
    p.add_argument("draft", help="path to the draft Markdown file")
    args = p.parse_args(argv)
    with open(args.draft, "r", encoding="utf-8") as fh:
        text = fh.read()
    result = check(text, {})
    _report(result)
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
