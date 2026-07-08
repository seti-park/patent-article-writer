#!/usr/bin/env python3
"""Regression guard for pipeline-retro improvement proposals.

A proposal from `pipeline-retro` (under meta/improvement-proposals/) changes a skill,
reference, gate, or canon. Before a human applies it, run this to confirm nothing regresses:

  1. the deterministic gate test suite still passes
     (_shared/scripts/test_gates.py), and
  2. every fixture under meta/fixtures/ still produces its expected gate verdict
     (and, where declared, no longer exhibits the previously-recurring defect check_id).

A proposal that breaks (1) or worsens any fixture in (2) must be rejected.

Each fixture is a directory meta/fixtures/<name>/ containing:
  - expect.json     : {"gate_pass": true|false,
                       "must_not_contain_check_ids": ["FIGUSE-001", ...],   # optional
                       "must_contain_check_ids": ["SOURCES-002", ...]}      # optional
  - draft.md        : the essay draft to run gates over
  - invention-summary.md   (optional context)
  - figures-index.txt      (optional, ints one per line)
  - figure-selection.md    (optional)
  - patent.md              (optional, verbatim-quote gate context)

Usage:
  python meta/regression.py            # run gate tests + all fixtures
  python meta/regression.py --fixtures-only
Exit code 0 iff everything passes.
"""

import argparse
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
SCRIPTS = os.path.join(REPO, ".claude", "skills", "_shared", "scripts")
FIXTURES = os.path.join(HERE, "fixtures")

sys.path.insert(0, SCRIPTS)


def _run_gate_tests():
    """Run the gate unittest suite as a subprocess. Return True on success."""
    test_path = os.path.join(SCRIPTS, "test_gates.py")
    print("== gate test suite ==")
    rc = subprocess.call([sys.executable, test_path])
    return rc == 0


def _load(path):
    with open(path, "r", encoding="utf-8") as fh:
        return fh.read()


def _run_fixture(name):
    """Run gates over one fixture; compare to expect.json. Return True on pass."""
    import run_gates  # imported here so a broken edit surfaces as a clear failure

    fdir = os.path.join(FIXTURES, name)
    expect = json.loads(_load(os.path.join(fdir, "expect.json")))
    draft = _load(os.path.join(fdir, "draft.md"))

    ctx = {"mode": "essay"}
    inv = os.path.join(fdir, "invention-summary.md")
    if os.path.exists(inv):
        ctx["invention_summary_text"] = _load(inv)
    figs = os.path.join(fdir, "figures-index.txt")
    if os.path.exists(figs):
        ctx["figures_index"] = [int(t) for t in _load(figs).split()]
    sel = os.path.join(fdir, "figure-selection.md")
    if os.path.exists(sel):
        ctx["figure_selection_text"] = _load(sel)
    pat = os.path.join(fdir, "patent.md")
    if os.path.exists(pat):
        ctx["patent_text"] = _load(pat)

    overall, results = run_gates.run_all(draft, ctx)
    seen = {f["check_id"] for r in results for f in r["findings"]}

    ok = True
    if "gate_pass" in expect and overall != expect["gate_pass"]:
        print("  FAIL %s: gate_pass expected %s, got %s" % (name, expect["gate_pass"], overall))
        ok = False
    for cid in expect.get("must_not_contain_check_ids", []):
        if cid in seen:
            print("  FAIL %s: regressed -- %s present (must not contain)" % (name, cid))
            ok = False
    for cid in expect.get("must_contain_check_ids", []):
        if cid not in seen:
            print("  FAIL %s: expected %s not detected" % (name, cid))
            ok = False
    if ok:
        print("  ok   %s" % name)
    return ok


def main(argv=None):
    p = argparse.ArgumentParser(description="pipeline-retro regression guard")
    p.add_argument("--fixtures-only", action="store_true")
    args = p.parse_args(argv)

    all_ok = True
    if not args.fixtures_only:
        all_ok = _run_gate_tests() and all_ok

    print("== fixtures ==")
    if not os.path.isdir(FIXTURES):
        print("  (no fixtures directory)")
    else:
        names = sorted(
            d for d in os.listdir(FIXTURES)
            if os.path.isdir(os.path.join(FIXTURES, d))
        )
        if not names:
            print("  (no fixtures yet)")
        for name in names:
            all_ok = _run_fixture(name) and all_ok

    print("\nREGRESSION: %s" % ("PASS" if all_ok else "FAIL"))
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
