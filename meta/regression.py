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
                       "must_contain_check_ids": ["SOURCES-002", ...],      # optional
                       "mode": "essay"|"wire",                             # optional (default essay)
                       "profile": "...",                                   # optional (ignored by gates)
                       "acceptance": "single-clean"|"double-clean"}        # optional (reserved)
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


def _run_meta_validators():
    """Run the meta-bookkeeping validators so they cannot silently rot.

    - validate_ledger.py (default, non-strict): the findings ledger conforms to
      schema (historical '?'/absent tolerated; --strict is a manual/diff tool).
    - proposals_index.py --check: the improvement-proposals README index agrees
      with each proposal file's status: frontmatter.
    Absent scripts are skipped (not a failure), so this is additive.
    """
    print("== meta validators ==")
    ok = True
    for name, args in (("validate_ledger.py", []),
                       ("proposals_index.py", ["--check"])):
        path = os.path.join(HERE, name)
        if not os.path.exists(path):
            print("  skip %s (not present)" % name)
            continue
        rc = subprocess.call([sys.executable, path] + args)
        print("  %s %s" % ("ok  " if rc == 0 else "FAIL", name))
        ok = ok and rc == 0
    return ok


def _load(path):
    with open(path, "r", encoding="utf-8") as fh:
        return fh.read()


def _fixture_dirs(root, prefix=""):
    """Yield (display_name, dir) for every directory holding an expect.json,
    recursing so grouping dirs like fixtures/handoff/ hold no expect.json of
    their own. A dir with expect.json is a leaf fixture; otherwise recurse."""
    for d in sorted(os.listdir(root)):
        full = os.path.join(root, d)
        if not os.path.isdir(full):
            continue
        name = prefix + d
        if os.path.exists(os.path.join(full, "expect.json")):
            yield name, full
        else:
            for sub in _fixture_dirs(full, name + "/"):
                yield sub


def _run_check_run_fixture(name, fdir, expect):
    """Run check_run.check() over a materialized handoff/ tree; compare the
    reported rule-id SET (not a hardcoded inventory) to expect.json.
    Handles xfail (a rule another lane may not have landed yet)."""
    import check_run
    xfail = bool(expect.get("xfail"))
    result = check_run.check(
        os.path.join(fdir, "handoff"),
        threshold=expect.get("threshold", "pass"),
        self_audit=expect.get("self_audit", "on"),
        acceptance=expect.get("acceptance", "double-clean"),
        owner_confirm=expect.get("owner_confirm", "required"),
        require_understand=expect.get("require_understand", True),
        recheck_gates=expect.get("recheck_gates", True),
    )
    seen = {f["check_id"] for f in result["findings"]}
    ok = True
    if "passed" in expect and result["passed"] != expect["passed"]:
        ok = False
        print("  %s %s: passed expected %s, got %s (%s)"
              % ("xfail" if xfail else "FAIL", name, expect["passed"],
                 result["passed"], ",".join(sorted(seen)) or "none"))
    for cid in expect.get("must_contain", []):
        if cid not in seen:
            ok = False
            print("  %s %s: expected %s not reported" % ("xfail" if xfail else "FAIL", name, cid))
    for cid in expect.get("must_not_contain", []):
        if cid in seen:
            ok = False
            print("  %s %s: %s present (must not contain)" % ("xfail" if xfail else "FAIL", name, cid))
    if ok:
        print("  ok   %s" % name)
        return True, False
    if xfail:
        print("       ^ xfail: %s" % expect.get("reason", "expected to fail until a pending rule lands"))
        return True, True   # xfail does not fail the suite
    return False, False


def _run_fixture(name, fdir=None):
    """Run gates over one fixture; compare to expect.json. Return True on pass."""
    import run_gates  # imported here so a broken edit surfaces as a clear failure

    if fdir is None:
        fdir = os.path.join(FIXTURES, name)
    expect = json.loads(_load(os.path.join(fdir, "expect.json")))
    if expect.get("kind") == "check_run":
        ok, _ = _run_check_run_fixture(name, fdir, expect)
        return ok
    draft = _load(os.path.join(fdir, "draft.md"))

    # Fixture ctx flexibility (HARNESS-03): mode/profile/acceptance may be
    # declared in expect.json; absent keys keep prior defaults (mode=essay).
    ctx = {
        "mode": expect.get("mode", "essay"),
    }
    if "profile" in expect:
        ctx["profile"] = expect["profile"]
    if "acceptance" in expect:
        ctx["acceptance"] = expect["acceptance"]
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
        all_ok = _run_meta_validators() and all_ok

    print("== fixtures ==")
    if not os.path.isdir(FIXTURES):
        print("  (no fixtures directory)")
    else:
        fixtures = list(_fixture_dirs(FIXTURES))
        if not fixtures:
            print("  (no fixtures yet)")
        for name, fdir in fixtures:
            all_ok = _run_fixture(name, fdir) and all_ok

    print("\nREGRESSION: %s" % ("PASS" if all_ok else "FAIL"))
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
