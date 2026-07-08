#!/usr/bin/env python3
"""Run-completeness checker: did the Compose↔Edit loop actually run?

The inner loop's historical escape hatches were all "the model said so": a
round-1 `pass` graded by the same context that composed, findings applied
without verification, promotion at the cap without a trace. This script makes
the loop's SHAPE mechanically checkable. The orchestrator must run it (and it
must pass) before archiving a run; the /goal acceptance string can require it.

Artifact contract (written by the orchestrator each round N = 1..K):
  handoff/03-edit/edit-log.round-N.md          review round N (feedback-format.md;
                                               findings carry finding_id rN-F<k>)
  handoff/03-edit/gate-result.round-N.json     run_gates.py --json output for round N
  handoff/02-compose/revision-response.round-N.md   composer dispositions for round N
                                               (required for every round FOLLOWED by
                                               another round)
  handoff/03-edit/essay-final.md               promotion target (acceptance only)
  handoff/03-edit/score-history.md             must contain "CAP HIT" if promoted at cap
  handoff/03-edit/revision-notes.md            self-audit deltas (essay mode)
  handoff/01-design/owner-briefing.md          Phase-1 Korean owner briefing --
                                               one-time, not per-round (RUN-008)

Checks:
  RUN-001 (fail): round artifacts missing or non-contiguous (edit-log/gate-result
                  for rounds 1..K; revision-response for rounds 1..K-1) -- UNLESS
                  round N -> N+1 is a confirmation transition (see below), which
                  by spec takes no revision and so has no response to trace.
  RUN-002 (fail): an edit-log has no parsable overall_assessment, or a gate
                  result JSON is unreadable.
  RUN-003 (fail): a medium/high/critical finding in round N has no disposition
                  block in revision-response.round-N.md, or a failing gate
                  check_id has none (rounds followed by another round only;
                  skipped entirely across a confirmation transition).
  RUN-004 (fail): a medium+ finding_id from round N-1 is never mentioned in
                  round N's edit-log (silently dropped instead of ruled on).
                  Runs across every transition, confirmation or not.
  RUN-005 (fail): essay-final.md exists but the acceptance rule is not met:
                  the LAST TWO rounds must both be clean (assessment acceptable
                  per --threshold AND gates passed) — a round-1 pass is a
                  hypothesis, not a verdict, until a fresh review confirms it —
                  UNLESS score-history.md declares "CAP HIT" (explicit
                  ship-best-round decision, surfaced to the user).
  RUN-006 (warn): promoted via CAP HIT (informational — unresolved findings ship).
  RUN-007 (fail): --self-audit on and essay-final.md exists, but
                  revision-notes.md is missing or has neither a "## delta"
                  block nor an explicit no-findings statement.
  RUN-008 (fail): essay-final.md exists but handoff/01-design/owner-briefing.md
                  is missing or empty (whitespace-only) -- the Phase-1 Korean
                  owner briefing (owner-comprehension overhaul, U5) was never
                  produced. Unconditional: unlike RUN-007, not gated by
                  --self-audit or --threshold.
  RUN-000 (warn): informational skips (incl. a confirmation transition, below).

Confirmation-transition model (2026-07-03-check-run-confirmation-round-model
proposal + its 2026-07-04 amendment): the loop spec runs a confirmation round
N+1 with no revision in between on the first CLEAN(N). Round N -> N+1 is a
confirmation transition when edit-log.round-(N+1).md declares
`round_type: confirmation` (anywhere in the file) or contains the phrase
"confirmation round" in its first 40 lines, or score-history.md's row for
round N+1 labels it "confirmation". Across such a transition, RUN-001/RUN-003
never require a revision-response.round-N.md (there was no revision); RUN-004
id-continuity still runs against round N+1's log regardless.

Severity harvesting (`_findings_with_severity`) only counts a finding_id as
THIS round's own finding when a plain `severity:` line follows it within a
few lines. The re-review protocol's carried/verification ruling blocks use
`prior_severity:` notation to re-affirm an OLDER id's severity while ruling on
it -- that notation is a citation, not a new finding, and must not manufacture
a phantom RUN-003/RUN-004 obligation for the round that merely re-verified it
(second, compounding manifestation of the same proposal, 2026-07-04 amendment,
etched-us20240378175).

Usage:
  check_run.py [--handoff handoff] [--threshold pass|revise-recommended]
               [--self-audit on|off] [--json]
Exit code 0 iff no fail-severity finding.
"""

import argparse
import glob
import json
import os
import re
import sys

ASSESS_RE = re.compile(r"^\s*overall_assessment:\s*(\S+)", re.M)
FINDING_ID_RE = re.compile(r"^\s*-\s*finding_id:\s*(r\d+-F\d+)", re.M)
SEVERITY_RE = re.compile(r"^\s*severity:\s*(\S+)", re.M)
CAP_HIT_RE = re.compile(r"\bCAP\s+HIT\b", re.I)
DELTA_RE = re.compile(r"^##\s+delta\b", re.M | re.I)
NO_FINDINGS_RE = re.compile(r"self-audit[^\n]*no[^\n]*finding", re.I)

# Confirmation-transition signals (2026-07-03-check-run-confirmation-round-model).
ROUND_TYPE_CONFIRMATION_RE = re.compile(r"^\s*round_type:\s*confirmation", re.M | re.I)
CONFIRMATION_PHRASE_RE = re.compile(r"confirmation\s+round", re.I)
FINDING_BLOCK_LOOKAHEAD = 6  # lines searched after `finding_id:` for a plain `severity:`

ACCEPTABLE = {
    "pass": {"pass"},
    "revise-recommended": {"pass", "revise-recommended"},
}


def _read(path):
    with open(path, "r", encoding="utf-8") as fh:
        return fh.read()


def _findings_with_severity(edit_log_text):
    """Return list of (finding_id, severity) DECLARED by this round's log.

    A `finding_id:` block counts as this round's own finding only when a
    plain `severity:` line follows it within FINDING_BLOCK_LOOKAHEAD lines
    (or before the next `finding_id:` block, whichever comes first). This
    deliberately does NOT match `prior_severity:` -- the re-review protocol's
    carried/verification-ruling notation, used when a round re-affirms an
    OLDER id's severity while ruling on it. A block that only ever carries
    `prior_severity:` is a citation of a previous round's finding, not a new
    finding of this round, and is excluded entirely here (not even counted as
    "unspecified") so it cannot manufacture a phantom RUN-003/RUN-004
    obligation for the round that merely re-verified it.
    """
    lines = edit_log_text.splitlines()
    out = []
    i = 0
    while i < len(lines):
        m = re.match(r"^\s*-\s*finding_id:\s*(r\d+-F\d+)", lines[i])
        if not m:
            i += 1
            continue
        fid = m.group(1)
        limit = min(i + 1 + FINDING_BLOCK_LOOKAHEAD, len(lines))
        for j in range(i + 1, limit):
            if re.match(r"^\s*-\s*finding_id:\s*(r\d+-F\d+)", lines[j]):
                break  # next block opened first -- no plain severity: for this id
            s = re.match(r"^\s*severity:\s*(\S+)", lines[j])
            if s:
                out.append((fid, s.group(1).strip()))
                break
        i += 1
    return out


def _is_confirmation_transition(edit_dir, score_path, next_round):
    """True when round `next_round` is a confirmation round for its predecessor.

    Per the loop spec, the first CLEAN(N) is followed by a confirmation round
    N+1 that reviews the SAME draft with no revision in between -- so the N ->
    N+1 transition has no revision-response to trace and no dispositions to
    require. Detected (any one signal suffices):
      1. edit-log.round-<next_round>.md declares `round_type: confirmation`
         anywhere in the file.
      2. That file's first 40 lines contain the phrase "confirmation round"
         (case-insensitive).
      3. score-history.md's row for round `next_round` labels it "confirmation".
    """
    log_path = os.path.join(edit_dir, "edit-log.round-%d.md" % next_round)
    if os.path.exists(log_path):
        text = _read(log_path)
        if ROUND_TYPE_CONFIRMATION_RE.search(text):
            return True
        first_40 = "\n".join(text.splitlines()[:40])
        if CONFIRMATION_PHRASE_RE.search(first_40):
            return True
    if os.path.exists(score_path):
        for line in _read(score_path).splitlines():
            if re.search(r"\|\s*%d\s*\|" % next_round, line) and re.search(
                    r"confirmation", line, re.I):
                return True
    return False


def check(handoff_dir, threshold="pass", self_audit="on"):
    findings = []
    edit_dir = os.path.join(handoff_dir, "03-edit")
    compose_dir = os.path.join(handoff_dir, "02-compose")
    design_dir = os.path.join(handoff_dir, "01-design")
    score_path = os.path.join(edit_dir, "score-history.md")

    def add(check_id, severity, message, location):
        findings.append({"check_id": check_id, "severity": severity,
                         "message": message, "location": location})

    # --- discover rounds --------------------------------------------------
    logs = glob.glob(os.path.join(edit_dir, "edit-log.round-*.md"))
    rounds = sorted(int(m.group(1)) for p in logs
                    for m in [re.search(r"edit-log\.round-(\d+)\.md$", p)] if m)
    if not rounds:
        add("RUN-001", "fail",
            "no edit-log.round-N.md artifacts found — the loop left no trace",
            edit_dir)
        return _result(findings)
    K = max(rounds)
    if rounds != list(range(1, K + 1)):
        add("RUN-001", "fail",
            "rounds are non-contiguous: found %s (expected 1..%d)" % (rounds, K),
            edit_dir)

    # --- per-round artifacts + parses -------------------------------------
    assessments = {}
    gates_passed = {}
    round_findings = {}
    for n in range(1, K + 1):
        log_path = os.path.join(edit_dir, "edit-log.round-%d.md" % n)
        gate_path = os.path.join(edit_dir, "gate-result.round-%d.json" % n)
        if not os.path.exists(log_path):
            continue  # RUN-001 already covers gaps
        text = _read(log_path)
        m = ASSESS_RE.search(text)
        if not m:
            add("RUN-002", "fail",
                "edit-log.round-%d.md has no parsable overall_assessment" % n, log_path)
        else:
            assessments[n] = m.group(1).strip()
        round_findings[n] = _findings_with_severity(text)

        if not os.path.exists(gate_path):
            add("RUN-001", "fail", "gate-result.round-%d.json missing" % n, edit_dir)
        else:
            try:
                gates_passed[n] = bool(json.loads(_read(gate_path)).get("passed"))
            except (ValueError, OSError) as e:
                add("RUN-002", "fail",
                    "gate-result.round-%d.json unreadable: %s" % (n, e), gate_path)

        # response required for every round followed by another round --
        # UNLESS round n -> n+1 is a confirmation transition (spec: the
        # confirmation round takes no revision, so there is nothing to
        # disposition or trace at this transition).
        if n < K:
            if _is_confirmation_transition(edit_dir, score_path, n + 1):
                add("RUN-000", "warn",
                    "round %d -> %d is a confirmation transition (no revision "
                    "in between); revision-response/disposition requirements "
                    "skipped for this transition" % (n, n + 1), edit_dir)
            else:
                resp_path = os.path.join(compose_dir, "revision-response.round-%d.md" % n)
                if not os.path.exists(resp_path):
                    add("RUN-001", "fail",
                        "revision-response.round-%d.md missing (round %d was revised "
                        "without a disposition trace)" % (n, n), compose_dir)
                else:
                    resp = _read(resp_path)
                    for fid, sev in round_findings.get(n, []):
                        if sev in ("medium", "high", "critical", "unspecified") and fid not in resp:
                            add("RUN-003", "fail",
                                "finding %s (%s) has no disposition in "
                                "revision-response.round-%d.md" % (fid, sev, n), resp_path)
                    gate_json = gates_passed.get(n)
                    if gate_json is False:
                        try:
                            gate_data = json.loads(_read(os.path.join(
                                edit_dir, "gate-result.round-%d.json" % n)))
                            failing = {f["check_id"] for g in gate_data.get("gates", [])
                                       for f in g.get("findings", [])
                                       if f.get("severity") == "fail"}
                        except (ValueError, OSError):
                            failing = set()
                        for cid in sorted(failing):
                            if cid not in resp:
                                add("RUN-003", "fail",
                                    "failing gate %s has no disposition in "
                                    "revision-response.round-%d.md" % (cid, n), resp_path)

        # carried-id rule: every medium+ id from round n-1 must appear in round n's log
        if n > 1:
            prev = round_findings.get(n - 1, [])
            for fid, sev in prev:
                if sev in ("medium", "high", "critical", "unspecified") and fid not in text:
                    add("RUN-004", "fail",
                        "finding %s (round %d, %s) is never ruled on in round %d's "
                        "edit-log (silently dropped)" % (fid, n - 1, sev, n), log_path)

    # --- acceptance rule ----------------------------------------------------
    final_path = os.path.join(edit_dir, "essay-final.md")
    if os.path.exists(final_path):
        ok = ACCEPTABLE.get(threshold, {"pass"})

        def clean(n):
            return assessments.get(n) in ok and gates_passed.get(n) is True

        double_clean = K >= 2 and clean(K) and clean(K - 1)
        cap_hit = os.path.exists(score_path) and bool(CAP_HIT_RE.search(_read(score_path)))
        if not double_clean and not cap_hit:
            add("RUN-005", "fail",
                "essay-final.md promoted without double-clean acceptance (last two "
                "rounds clean) and without an explicit CAP HIT in score-history.md — "
                "a single self-graded pass is not acceptance (K=%d, assessments=%s, "
                "gates=%s)" % (K, assessments, gates_passed), final_path)
        elif cap_hit and not double_clean:
            add("RUN-006", "warn",
                "promoted via CAP HIT — unresolved findings ship; surface them to the user",
                score_path)

        if self_audit == "on":
            notes_path = os.path.join(edit_dir, "revision-notes.md")
            if not os.path.exists(notes_path):
                add("RUN-007", "fail",
                    "self-audit is on but revision-notes.md is missing (no evidence "
                    "the post-acceptance audit ran)", edit_dir)
            else:
                notes = _read(notes_path)
                if not DELTA_RE.search(notes) and not NO_FINDINGS_RE.search(notes):
                    add("RUN-007", "fail",
                        "revision-notes.md has neither a '## delta' block nor an "
                        "explicit 'self-audit: no unresolved findings' statement",
                        notes_path)

        # RUN-008 is unconditional -- unlike RUN-007 it is not gated by
        # --self-audit or --threshold. Every completed run must carry the
        # Phase-1 Korean owner briefing (owner-comprehension overhaul, U5).
        briefing_path = os.path.join(design_dir, "owner-briefing.md")
        if not os.path.exists(briefing_path):
            add("RUN-008", "fail",
                "owner-briefing.md missing from handoff/01-design/ (the Korean "
                "owner briefing was never produced)", briefing_path)
        elif not _read(briefing_path).strip():
            add("RUN-008", "fail",
                "owner-briefing.md in handoff/01-design/ is empty or "
                "whitespace-only (the Korean owner briefing was never produced)",
                briefing_path)
    else:
        add("RUN-000", "warn",
            "essay-final.md not present — acceptance checks skipped (run in progress?)",
            edit_dir)

    return _result(findings)


def _result(findings):
    passed = not any(f["severity"] == "fail" for f in findings)
    return {"gate": "check_run", "passed": passed, "findings": findings}


def _report(result):
    status = "PASS" if result["passed"] else "FAIL"
    print("[%s] %s" % (status, result["gate"]))
    for f in result["findings"]:
        print("  %-5s %-8s %s  (%s)" % (
            f["severity"].upper(), f["check_id"], f["message"], f["location"]))
    if not result["findings"]:
        print("  (no findings)")


def main(argv=None):
    p = argparse.ArgumentParser(description="Loop run-completeness checker")
    p.add_argument("--handoff", default="handoff", help="handoff directory (default: handoff)")
    p.add_argument("--threshold", choices=["pass", "revise-recommended"], default="pass")
    p.add_argument("--self-audit", choices=["on", "off"], default="on")
    p.add_argument("--json", action="store_true")
    args = p.parse_args(argv)

    result = check(args.handoff, args.threshold, args.self_audit)
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        _report(result)
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
