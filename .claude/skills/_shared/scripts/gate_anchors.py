#!/usr/bin/env python3
"""Citation-anchor + figure-reference gate for the patent-essay pipeline.

DRAFT FORMAT ASSUMPTIONS (see gate_emdash.py for the full shared list):
  - Citation anchors are inline tokens matching \\[(\\d{4})\\], e.g. [0123].
  - Figure refs are "Figure N" / "Fig. N" / "Fig N" (case-insensitive), N int.

IMPORTANT: real upstream handoff formats are still TBD; these scripts use the
documented pragmatic formats above and are written to be easily retargeted.

Context keys consumed:
  - invention_summary_text (str, optional): text of the invention-summary; the
    anchors found here ([dddd] tokens) form the allowed anchor set.
  - figures_index (list[int], optional): the set of valid figure numbers.

Checks:
  ANCHOR-002 (fail): any bracketed-digit anchor that is not 4-digit zero-padded
                     (e.g. [123], [12345]) -- Pass 6 6E format rule.
  ANCHOR-001 (fail): every [dddd] anchor in the draft must also appear in the
                     invention-summary anchor set.
  ANCHOR-000 (warn): emitted (and check skipped/passed) when no
                     invention_summary_text is provided.
  FIGREF-001 (fail): every figure number referenced in the draft must be in
                     figures_index.
  FIGREF-000 (warn): emitted (and check skipped) when figures_index is absent.
"""

import argparse
import re
import sys

# ---------------------------------------------------------------------------
# Tunable constants
# ---------------------------------------------------------------------------
GATE_ID = "anchors"
ANCHOR_RE = re.compile(r"\[(\d{4})\]")                 # [0123]
# Any bracketed pure-digit token, to catch malformed (non-4-digit) anchors like
# [123] or [12345]. Markdown footnote refs ([^id]) are excluded by \d-only.
ANCHOR_ANY_DIGITS_RE = re.compile(r"\[(\d+)\]")
FIGREF_RE = re.compile(r"\bfig(?:ure|\.)?\s*(\d+)[a-z]?\b", re.IGNORECASE)  # Figure 3 / Fig. 3 / Fig 3 / FIG. 3B


def _find_anchors(text):
    """Return an ordered list of (anchor_token, lineno) for each [dddd] hit."""
    hits = []
    for lineno, raw in enumerate((text or "").splitlines(), start=1):
        for m in ANCHOR_RE.finditer(raw):
            hits.append((m.group(1), lineno))
    return hits


def _anchor_set(text):
    return {m.group(1) for m in ANCHOR_RE.finditer(text or "")}


def check(draft_text: str, context: dict) -> dict:
    findings = []
    context = context or {}

    # --- ANCHOR format (4-digit zero-padded) ---------------------------------
    # Pass 6 6E: any `[XXX]` / `[XXXXX]` non-4-digit anchor is a hard fail.
    for lineno, raw in enumerate(draft_text.splitlines(), start=1):
        for m in ANCHOR_ANY_DIGITS_RE.finditer(raw):
            if len(m.group(1)) != 4:
                findings.append({
                    "check_id": "ANCHOR-002",
                    "severity": "fail",
                    "message": "malformed citation anchor [%s] (must be 4-digit "
                               "zero-padded, e.g. [0042])" % m.group(1),
                    "location": "line %d" % lineno,
                })

    # --- ANCHOR chain --------------------------------------------------------
    summary = context.get("invention_summary_text")
    if summary is None:
        findings.append({
            "check_id": "ANCHOR-000",
            "severity": "warn",
            "message": "no invention-summary provided, anchor-chain check skipped",
            "location": "(global)",
        })
    else:
        allowed = _anchor_set(summary)
        for token, lineno in _find_anchors(draft_text):
            if token not in allowed:
                findings.append({
                    "check_id": "ANCHOR-001",
                    "severity": "fail",
                    "message": "citation anchor [%s] not present in invention-summary" % token,
                    "location": "line %d" % lineno,
                })

    # --- FIGURE refs ---------------------------------------------------------
    figures_index = context.get("figures_index")
    if figures_index is None:
        findings.append({
            "check_id": "FIGREF-000",
            "severity": "warn",
            "message": "no figures_index provided, figure-ref check skipped",
            "location": "(global)",
        })
    else:
        valid = set(int(n) for n in figures_index)
        for lineno, raw in enumerate(draft_text.splitlines(), start=1):
            for m in FIGREF_RE.finditer(raw):
                num = int(m.group(1))
                if num not in valid:
                    findings.append({
                        "check_id": "FIGREF-001",
                        "severity": "fail",
                        "message": "figure reference 'Figure %d' not in figures_index" % num,
                        "location": "line %d" % lineno,
                    })

    passed = not any(f["severity"] == "fail" for f in findings)
    return {"gate": GATE_ID, "passed": passed, "findings": findings}


def _parse_figures_file(path):
    """Parse a figures file: one integer per line, or comma-separated."""
    with open(path, "r", encoding="utf-8") as fh:
        raw = fh.read()
    nums = []
    for tok in re.split(r"[,\s]+", raw.strip()):
        if tok:
            nums.append(int(tok))
    return nums


def _report(result):
    status = "PASS" if result["passed"] else "FAIL"
    print("[%s] gate=%s" % (status, result["gate"]))
    for f in result["findings"]:
        print("  %-5s %-12s %s  (%s)" % (
            f["severity"].upper(), f["check_id"], f["message"], f["location"]))
    if not result["findings"]:
        print("  (no findings)")


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description="Anchor/figure gate (%s)" % GATE_ID)
    p.add_argument("draft", help="path to the draft Markdown file")
    p.add_argument("--invention-summary", help="path to invention-summary text file")
    p.add_argument("--figures", help="path to figures file (ints, line/comma separated)")
    args = p.parse_args(argv)

    with open(args.draft, "r", encoding="utf-8") as fh:
        text = fh.read()

    ctx = {}
    if args.invention_summary:
        with open(args.invention_summary, "r", encoding="utf-8") as fh:
            ctx["invention_summary_text"] = fh.read()
    if args.figures:
        ctx["figures_index"] = _parse_figures_file(args.figures)

    result = check(text, ctx)
    _report(result)
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
