#!/usr/bin/env python3
"""Validate meta/findings-ledger.jsonl records against the ledger schema.

Stdlib-only. Checks required keys, enum values, and the absent-origin rule
(records without origin are treated as inner-loop — tolerated, not rewritten).

Usage:
  python meta/validate_ledger.py                      # validates meta/findings-ledger.jsonl
  python meta/validate_ledger.py path/to/ledger.jsonl
  python meta/validate_ledger.py --selftest

Exit 0 if valid (or if the ledger file does not exist yet — prints a note).
Non-zero on violations.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import tempfile

REQUIRED_KEYS = (
    "essay_id",
    "run_timestamp",
    "source",
    "severity",
    "goal",
    "root_cause_stage",
    "root_cause_artifact",
    "pattern_tag",
    "finding",
    "recommendation",
    "status",
)

# origin is optional on historical records; absent => inner-loop
ORIGIN_ENUM = frozenset({
    "inner-loop",
    "self-audit",
    "human-post-accept",
    "polish",
    "self-post-accept",
    "orchestration-protocol",
})

SOURCE_ENUM = frozenset({
    "editorial",
    "gate",
    "human-revision",
    "self-audit",
    "incident",
    "retro",  # meta-loop / empty-pass / retro-authored markers
})

STATUS_ENUM = frozenset({
    "open",
    "watch",
    "proposed",
    "resolved",
    "escalated",
    "none",  # empty-pass "no findings" markers (do not contribute to recurrence)
})

SEVERITY_ENUM = frozenset({
    "critical",
    "high",
    "medium",
    "low",
    "fail",
    "warn",
    "none",
})

DEFAULT_LEDGER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "findings-ledger.jsonl")


def effective_origin(rec):
    """Absent origin is read as inner-loop (append-only; never rewrite history)."""
    o = rec.get("origin")
    if o is None or o == "":
        return "inner-loop"
    return o


def validate_record(rec, line_no):
    """Return a list of violation strings for one record."""
    errs = []
    if not isinstance(rec, dict):
        return ["line %d: record is not a JSON object" % line_no]

    for k in REQUIRED_KEYS:
        if k not in rec:
            errs.append("line %d: missing required key %r" % (line_no, k))

    origin = rec.get("origin")
    if origin is not None and origin != "":
        if origin not in ORIGIN_ENUM:
            errs.append(
                "line %d: invalid origin %r (allowed: %s)"
                % (line_no, origin, ", ".join(sorted(ORIGIN_ENUM)))
            )
    # absent origin is tolerated (= inner-loop)
    _ = effective_origin(rec)

    src = rec.get("source")
    if src is not None and src not in SOURCE_ENUM:
        errs.append(
            "line %d: invalid source %r (allowed: %s)"
            % (line_no, src, ", ".join(sorted(SOURCE_ENUM)))
        )

    st = rec.get("status")
    if st is not None and st not in STATUS_ENUM:
        errs.append(
            "line %d: invalid status %r (allowed: %s)"
            % (line_no, st, ", ".join(sorted(STATUS_ENUM)))
        )

    sev = rec.get("severity")
    if sev is not None and sev not in SEVERITY_ENUM:
        errs.append(
            "line %d: invalid severity %r (allowed: %s)"
            % (line_no, sev, ", ".join(sorted(SEVERITY_ENUM)))
        )

    # iter may be null; pass/check_id may be null — no further constraints
    return errs


def validate_ledger(path):
    """Validate a JSONL ledger file. Returns (ok: bool, messages: list[str])."""
    if not os.path.exists(path):
        return True, ["note: ledger not found at %s — nothing to validate (exit 0)" % path]

    messages = []
    errors = []
    n = 0
    with open(path, "r", encoding="utf-8") as fh:
        for i, line in enumerate(fh, 1):
            line = line.strip()
            if not line:
                continue
            n += 1
            try:
                rec = json.loads(line)
            except json.JSONDecodeError as e:
                errors.append("line %d: JSON decode error: %s" % (i, e))
                continue
            errors.extend(validate_record(rec, i))

    if errors:
        messages.extend(errors)
        messages.append("FAIL: %d violation(s) in %d record(s) at %s" % (len(errors), n, path))
        return False, messages

    messages.append("OK: %d record(s) valid in %s" % (n, path))
    return True, messages


# --- selftest samples (mirror normalize_revision_notes.py pattern) ---

_GOOD_WITH_ORIGIN = {
    "essay_id": "test-1",
    "iter": 1,
    "run_timestamp": "2026-01-01T00:00:00Z",
    "source": "editorial",
    "origin": "inner-loop",
    "pass": "pass-3",
    "check_id": None,
    "severity": "medium",
    "goal": "1",
    "root_cause_stage": "compose",
    "root_cause_artifact": "citation-format.md",
    "pattern_tag": "paraphrase-accidental-drift",
    "finding": "example",
    "recommendation": "fix it",
    "status": "open",
}

_GOOD_ABSENT_ORIGIN = {
    # historical record shape — no origin field
    "essay_id": "test-2",
    "iter": 0,
    "run_timestamp": "2026-01-01T00:00:00Z",
    "source": "gate",
    "pass": None,
    "check_id": "FIGUSE-001",
    "severity": "warn",
    "goal": "2",
    "root_cause_stage": "gate",
    "root_cause_artifact": "gate_figure_use.py",
    "pattern_tag": "figure-orphan",
    "finding": "orphan",
    "recommendation": "fix",
    "status": "watch",
}

_GOOD_ORCH = {
    "essay_id": "test-3",
    "iter": None,
    "run_timestamp": "2026-01-01T00:00:00Z",
    "source": "incident",
    "origin": "orchestration-protocol",
    "pass": None,
    "check_id": None,
    "severity": "fail",
    "goal": "all",
    "root_cause_stage": "orchestrator",
    "root_cause_artifact": "patent-essay SKILL checkpoint protocol + check_run RUN-010",
    "pattern_tag": "checkpoint-skipped",
    "finding": "confirm skipped",
    "recommendation": "enforce checkpoint",
    "status": "open",
    "finding_id": "ORCH-01",
}

_BAD_ORIGIN = dict(_GOOD_WITH_ORIGIN, origin="not-a-real-origin")
_BAD_MISSING = {"essay_id": "x", "status": "open"}  # missing most required keys


def _selftest():
    # unit: absent origin
    assert effective_origin({}) == "inner-loop"
    assert effective_origin({"origin": ""}) == "inner-loop"
    assert effective_origin({"origin": "polish"}) == "polish"

    # good records
    assert validate_record(_GOOD_WITH_ORIGIN, 1) == []
    assert validate_record(_GOOD_ABSENT_ORIGIN, 2) == []
    assert validate_record(_GOOD_ORCH, 3) == []

    # bad records
    bad_o = validate_record(_BAD_ORIGIN, 4)
    assert any("invalid origin" in e for e in bad_o), bad_o
    bad_m = validate_record(_BAD_MISSING, 5)
    assert any("missing required key" in e for e in bad_m), bad_m

    # file-level: write good JSONL, validate OK
    td = tempfile.mkdtemp(prefix="validate_ledger_")
    good_path = os.path.join(td, "good.jsonl")
    with open(good_path, "w", encoding="utf-8") as fh:
        for rec in (_GOOD_WITH_ORIGIN, _GOOD_ABSENT_ORIGIN, _GOOD_ORCH):
            fh.write(json.dumps(rec) + "\n")
    ok, msgs = validate_ledger(good_path)
    assert ok, msgs

    # file-level: bad JSONL fails
    bad_path = os.path.join(td, "bad.jsonl")
    with open(bad_path, "w", encoding="utf-8") as fh:
        fh.write(json.dumps(_BAD_ORIGIN) + "\n")
    ok2, msgs2 = validate_ledger(bad_path)
    assert not ok2, "expected failure on bad origin"
    assert any("invalid origin" in m for m in msgs2)

    # missing file: exit-ok with note
    missing = os.path.join(td, "no-such-ledger.jsonl")
    ok3, msgs3 = validate_ledger(missing)
    assert ok3 and any("note:" in m for m in msgs3)

    print(
        "selftest OK: absent-origin=inner-loop, enums, required keys, "
        "missing-file note, good/bad file-level verified"
    )
    return 0


def main(argv=None):
    p = argparse.ArgumentParser(description="Validate findings-ledger.jsonl against schema.")
    p.add_argument("path", nargs="?", default=DEFAULT_LEDGER,
                   help="path to findings-ledger.jsonl (default: meta/findings-ledger.jsonl)")
    p.add_argument("--selftest", action="store_true")
    args = p.parse_args(argv)

    if args.selftest:
        return _selftest()

    ok, messages = validate_ledger(args.path)
    for m in messages:
        print(m)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
