#!/usr/bin/env python3
"""Meta-expression gate for the patent-essay pipeline.

Flags reader-instruction and essay-self-reference rhetorical patterns: prose that
tells the reader HOW to read ("read it the way an examiner would", "watch how the
patent handles each") or refers to the essay as an object ("everything below is
the reading that gets you there", "the rest of this essay"). The target reader
buys insight, not stage directions; these are AI-tell posturing analogous to the
banned-word list, and were stripped by hand across run 045 (v2.2). See
meta/improvement-proposals/2026-06-26-human-revision-blindspots.md (class
`meta-reader-instruction` / `essay-self-reference`).

DRAFT FORMAT ASSUMPTIONS (see gate_emdash.py for the full shared list):
  - Patterns are only flagged OUTSIDE quoted text (double quotes, '>' blockquotes)
    and fenced code, since quotes are verbatim source material.

FENCE (deliberate non-match): a *scope disclaimer* such as "this essay does not
adjudicate them" is functional, not posturing, and is NOT matched -- the FAIL
patterns target the reader-command forms, the "everything below / rest of this
essay" forms, and "this essay will/argues/shows ...", never bare "this essay".

Checks:
  META-001 (fail): unambiguous reader-instruction / essay-self-reference posturing.
  META-002 (warn): softer reader-address worth a human look.
"""

import argparse
import re
import sys

GATE_ID = "meta"
FENCE_RE = re.compile(r"^\s*(```|~~~)")

# Hard-fail: phrasings that are essentially always posturing in this deliverable.
FAIL_PATTERNS = [
    r"read (?:it|this|them|the [a-z]+) the way",
    r"as we(?:'ll| will| shall) see",
    r"the rest of this (?:essay|piece|article|read)",
    r"everything (?:below|above|that follows)",
    r"watch how (?:the|this|it|they|each)",
    r"in this (?:essay|piece|article)\b",
    r"this (?:essay|piece|article) (?:will|sets out|aims|argues|shows|is going to)",
    r"let(?:'s| us) (?:look|turn|consider|begin|start|unpack|examine|dig)",
]
# Warn: reader-address that is sometimes legitimate; surface for a human look.
WARN_PATTERNS = [
    r"\bas (?:you|the reader) (?:can see|will (?:see|notice|recall))\b",
    r"\byou might (?:think|wonder|ask|expect|assume)\b",
    r"\bnotice (?:how|that)\b",
    r"\bbear with me\b",
]

FAIL_RX = [re.compile(p, re.IGNORECASE) for p in FAIL_PATTERNS]
WARN_RX = [re.compile(p, re.IGNORECASE) for p in WARN_PATTERNS]


def _mask_quoted_spans(line):
    """Blank out double-quoted span contents (keep the quote chars)."""
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


def check(draft_text: str, context: dict) -> dict:
    findings = []
    in_fence = False
    for lineno, raw in enumerate(draft_text.splitlines(), start=1):
        if FENCE_RE.match(raw):
            in_fence = not in_fence
            continue
        if in_fence or raw.lstrip().startswith(">"):
            continue
        scan = _mask_quoted_spans(raw)
        for rx in FAIL_RX:
            for m in rx.finditer(scan):
                findings.append({
                    "check_id": "META-001",
                    "severity": "fail",
                    "message": "reader-instruction / essay-self-reference %r" % m.group(0),
                    "location": "line %d, col %d" % (lineno, m.start() + 1),
                })
        for rx in WARN_RX:
            for m in rx.finditer(scan):
                findings.append({
                    "check_id": "META-002",
                    "severity": "warn",
                    "message": "reader-address worth a look: %r" % m.group(0),
                    "location": "line %d, col %d" % (lineno, m.start() + 1),
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
    p = argparse.ArgumentParser(description="Meta-expression gate (%s)" % GATE_ID)
    p.add_argument("draft", help="path to the draft Markdown file")
    args = p.parse_args(argv)
    with open(args.draft, "r", encoding="utf-8") as fh:
        text = fh.read()
    result = check(text, {})
    _report(result)
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
