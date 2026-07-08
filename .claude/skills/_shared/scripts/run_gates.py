#!/usr/bin/env python3
"""Aggregator for the patent-essay deterministic validation gates.

Runs all fourteen gates against a draft and aggregates the results.

DRAFT FORMAT ASSUMPTIONS: see gate_emdash.py for the full shared list (Markdown
draft; quoted text = double quotes or '>' blockquotes; [dddd] anchors; Figure N
refs; a trailing 'Sources' header section). Real upstream handoff formats are
TBD; these scripts use documented pragmatic formats and are easily retargeted.

Hard pass/fail rule:
  overall passed == no gate emits any finding of severity "fail".
  Warnings NEVER fail the run.

Usage:
  run_gates.py --draft DRAFT [--invention-summary FILE] [--figures FILE]
               [--figure-selection FILE] [--patent FILE]
               [--mode essay|wire] [--json]
"""

import argparse
import json
import os
import re
import sys

# Allow running both as a script and as a module.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import gate_emdash
import gate_anchors
import gate_quotes
import gate_sources
import gate_banned
import gate_structure
import gate_figure_use
import gate_meta
import gate_stub
import gate_cashtag
import gate_dupe
import gate_typography
import gate_hedge
import gate_surface

GATES = [
    gate_emdash,
    gate_anchors,
    gate_quotes,
    gate_sources,
    gate_banned,
    gate_structure,
    gate_figure_use,
    gate_meta,
    gate_stub,
    gate_cashtag,
    gate_dupe,
    gate_typography,
    gate_hedge,
    gate_surface,
]


def _parse_figures_file(path):
    """One integer per line, or comma/space separated."""
    with open(path, "r", encoding="utf-8") as fh:
        raw = fh.read()
    nums = []
    for tok in re.split(r"[,\s]+", raw.strip()):
        if tok:
            nums.append(int(tok))
    return nums


def build_context(args):
    ctx = {"mode": args.mode}
    if args.invention_summary:
        with open(args.invention_summary, "r", encoding="utf-8") as fh:
            ctx["invention_summary_text"] = fh.read()
    if args.figures:
        ctx["figures_index"] = _parse_figures_file(args.figures)
    if args.figure_selection:
        with open(args.figure_selection, "r", encoding="utf-8") as fh:
            ctx["figure_selection_text"] = fh.read()
    if args.patent:
        with open(args.patent, "r", encoding="utf-8") as fh:
            ctx["patent_text"] = fh.read()
    return ctx


def run_all(draft_text, context):
    """Run every gate, return (overall_passed, [per-gate result dicts])."""
    results = []
    for mod in GATES:
        results.append(mod.check(draft_text, context))
    overall = all(
        not any(f["severity"] == "fail" for f in r["findings"])
        for r in results
    )
    return overall, results


def _print_text(overall, results):
    # Summary table.
    print("=" * 64)
    print("PATENT-ESSAY VALIDATION GATES")
    print("=" * 64)
    print("%-12s %-6s %-6s %-6s" % ("GATE", "STATUS", "#FAIL", "#WARN"))
    print("-" * 64)
    for r in results:
        n_fail = sum(1 for f in r["findings"] if f["severity"] == "fail")
        n_warn = sum(1 for f in r["findings"] if f["severity"] == "warn")
        status = "PASS" if n_fail == 0 else "FAIL"
        print("%-12s %-6s %-6d %-6d" % (r["gate"], status, n_fail, n_warn))
    print("-" * 64)
    print("OVERALL: %s" % ("PASS" if overall else "FAIL"))
    print("=" * 64)

    # All findings.
    any_finding = False
    for r in results:
        for f in r["findings"]:
            any_finding = True
            print("  [%s] %-5s %-12s %s  (%s)" % (
                r["gate"], f["severity"].upper(), f["check_id"],
                f["message"], f["location"]))
    if not any_finding:
        print("  (no findings from any gate)")


def main(argv=None) -> int:
    p = argparse.ArgumentParser(
        description="Run all patent-essay validation gates against a draft.")
    p.add_argument("--draft", required=True, help="path to the draft Markdown file")
    p.add_argument("--invention-summary", help="path to invention-summary text file")
    p.add_argument("--figures", help="path to figures file (ints, line/comma separated)")
    p.add_argument("--figure-selection", help="path to figure-selection.md (orphan-figure gate)")
    p.add_argument("--patent", help="path to patent.md (verbatim-quote gate)")
    p.add_argument("--mode", choices=["essay", "wire"], default="essay",
                   help="reserved pass-through mode (default: essay)")
    p.add_argument("--json", action="store_true", help="emit JSON summary instead of text")
    args = p.parse_args(argv)

    with open(args.draft, "r", encoding="utf-8") as fh:
        draft_text = fh.read()

    context = build_context(args)
    overall, results = run_all(draft_text, context)

    if args.json:
        print(json.dumps({"passed": overall, "gates": results}, indent=2))
    else:
        _print_text(overall, results)

    return 0 if overall else 1


if __name__ == "__main__":
    sys.exit(main())
