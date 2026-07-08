#!/usr/bin/env python3
"""Venue ticker-convention gate for the patent-essay pipeline (X Articles).

When a stock ticker is introduced in a ticker-labeling context ("trading as AGLT",
"NASDAQ: AGLT", "ticker AGLT"), the X Articles convention is the $-prefixed cashtag
($AGLT) -- a native, linkable token. This flags a bare (un-$'d) ticker in that
context. It keys on the labeling CONTEXT, not bare uppercase tokens, so acronyms
like GXO / USPTO / PIPE are never flagged. Run 045 fixed AGLT -> $AGLT by hand
(v2.1); see meta/improvement-proposals/2026-06-26-human-revision-blindspots.md
(class `venue-ticker-convention`).

DRAFT FORMAT ASSUMPTIONS (see gate_emdash.py for the full shared list):
  - Tickers inside quoted source text are not flagged (quotes are verbatim).

All checks WARN.

Checks:
  CASH-001 (warn): a ticker in labeling context lacking the '$' cashtag prefix.
"""

import argparse
import re
import sys

GATE_ID = "cashtag"
FENCE_RE = re.compile(r"^\s*(```|~~~)")

# Labeling phrase immediately followed by a bare UPPERCASE ticker (no leading '$').
LABEL_RE = re.compile(
    r"\b(?:ticker|trading as|traded as|listed as|symbol)\b[:\s]+(?!\$)([A-Z]{2,5})\b")
EXCHANGE_RE = re.compile(
    r"\b(?:NYSE|NASDAQ|Nasdaq|AMEX|CBOE)\b\s*:\s*(?!\$)([A-Z]{2,5})\b")


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
        for rx in (LABEL_RE, EXCHANGE_RE):
            for m in rx.finditer(scan):
                tk = m.group(1)
                findings.append({
                    "check_id": "CASH-001",
                    "severity": "warn",
                    "message": "ticker %r in labeling context lacks the $ cashtag (X Articles): use $%s"
                               % (tk, tk),
                    "location": "line %d, col %d" % (lineno, m.start(1) + 1),
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
    p = argparse.ArgumentParser(description="Venue cashtag gate (%s)" % GATE_ID)
    p.add_argument("draft", help="path to the draft Markdown file")
    args = p.parse_args(argv)
    with open(args.draft, "r", encoding="utf-8") as fh:
        text = fh.read()
    result = check(text, {})
    _report(result)
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
