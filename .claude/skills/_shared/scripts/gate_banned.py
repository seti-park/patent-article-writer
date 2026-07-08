#!/usr/bin/env python3
"""Banned-terms gate for the patent-essay pipeline.

DRAFT FORMAT ASSUMPTIONS (see gate_emdash.py for the full shared list):
  - Banned terms are only flagged OUTSIDE quoted text (double quotes "..." and
    Markdown blockquote ">" lines) and outside fenced code blocks, since quotes
    are verbatim source material.

IMPORTANT: real upstream handoff formats are still TBD; this gate uses the
documented pragmatic conventions and is easily retargeted.

The banned list is loaded from a sibling file ``banned_terms.txt`` (path is a
tunable constant). See that file's header for its format:
  - '#' comment lines and blank lines are ignored
  - 're:' prefix -> regex (case-insensitive)
  - otherwise   -> case-insensitive whole-word literal

Checks:
  BANNED-001 (fail): each banned literal/regex hit outside quoted text.
"""

import argparse
import os
import re
import sys

# ---------------------------------------------------------------------------
# Tunable constants
# ---------------------------------------------------------------------------
GATE_ID = "banned"
# Path to the banned-terms data file (sibling of this script by default).
BANNED_TERMS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "banned_terms.txt")
FENCE_RE = re.compile(r"^\s*(```|~~~)")


def load_banned_terms(path=BANNED_TERMS_FILE):
    """Load (label, compiled_regex) pairs from the data file.

    Literals are compiled to whole-word, case-insensitive regexes. Regex
    entries (``re:`` prefix) are compiled case-insensitive as written.
    """
    patterns = []
    with open(path, "r", encoding="utf-8") as fh:
        for raw in fh:
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            if line.startswith("re:"):
                expr = line[3:].strip()
                patterns.append((expr, re.compile(expr, re.IGNORECASE)))
            else:
                # Whole-word / whole-phrase literal. \b at each end; internal
                # whitespace/hyphen kept literally via re.escape.
                lit = re.compile(r"\b" + re.escape(line) + r"\b", re.IGNORECASE)
                patterns.append((line, lit))
    return patterns


def _mask_quoted_spans(line):
    """Blank out double-quoted span contents (keep the quote chars)."""
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


def check(draft_text: str, context: dict) -> dict:
    context = context or {}
    # Allow caller to inject a custom terms file path or preloaded patterns.
    patterns = context.get("banned_patterns")
    if patterns is None:
        path = context.get("banned_terms_file", BANNED_TERMS_FILE)
        patterns = load_banned_terms(path)

    findings = []
    in_fence = False
    for lineno, raw in enumerate(draft_text.splitlines(), start=1):
        if FENCE_RE.match(raw):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        # Blockquote = fully quoted -> skip entirely.
        if raw.lstrip().startswith(">"):
            continue
        scan = _mask_quoted_spans(raw)
        for label, rx in patterns:
            for m in rx.finditer(scan):
                col = m.start() + 1
                findings.append({
                    "check_id": "BANNED-001",
                    "severity": "fail",
                    "message": "banned term/pattern %r matched %r" % (label, m.group(0)),
                    "location": "line %d, col %d" % (lineno, col),
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
    p = argparse.ArgumentParser(description="Banned-terms gate (%s)" % GATE_ID)
    p.add_argument("draft", help="path to the draft Markdown file")
    p.add_argument("--terms", default=BANNED_TERMS_FILE,
                   help="path to banned_terms.txt (default: sibling file)")
    args = p.parse_args(argv)
    with open(args.draft, "r", encoding="utf-8") as fh:
        text = fh.read()
    result = check(text, {"banned_terms_file": args.terms})
    _report(result)
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
