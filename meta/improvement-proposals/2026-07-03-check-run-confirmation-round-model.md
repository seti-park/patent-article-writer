---
proposal_id: 2026-07-03-check-run-confirmation-round-model
created: 2026-07-03T00:20:00Z
status: applied  # 2026-07-04 reader-first overhaul; regression PASS
lever: gate-strengthen
goal: "all"
root_cause_artifact: _shared/scripts/check_run.py (round-transition model + RUN-004 id harvest)
recurrence_count: 1 (but structural: every future run that accepts via a no-revision confirmation round hits it)
confidence: high
triggering_findings:
  - essay_id: etched-us12361091, check_id RUN-001 + 10x RUN-004 false FAILs at first check_run invocation
---

## Problem

The patent-essay SKILL mandates: on the first CLEAN(N), run a confirmation round N+1 with
"no revision in between". check_run.py contradicts that spec twice:

1. RUN-001 requires `revision-response.round-N.md` for EVERY round N < K
   ("response required for every round followed by another round") — including the
   CLEAN(N) -> confirmation(N+1) transition where the spec forbids a revision.
2. RUN-004 harvests finding_ids from round N's log with `_findings_with_severity`, which
   also captures ids mentioned in round N's disposition-VERIFICATION table (severity
   `unspecified`), then demands round N+1 re-rule all of them. In etched-us12361091 this
   flagged 10 r1-F* ids that round 2 had explicitly verified as landed/closed.

This run resolved it truthfully (orchestrator-authored transition record + reviewer-appended
lifecycle table), but every compliant future run pays the same tax or fails.

## Proposed change (exact diff sketch)

**File: `.claude/skills/_shared/scripts/check_run.py`**

```diff
         if n < K:
             resp_path = os.path.join(compose_dir, "revision-response.round-%d.md" % n)
-            if not os.path.exists(resp_path):
+            confirmation = _is_confirmation_transition(edit_dir, n + 1)
+            if confirmation and not os.path.exists(resp_path):
+                pass  # spec: confirmation rounds take no revision; nothing to trace
+            elif not os.path.exists(resp_path):
                 add("RUN-001", "fail", ...)
```

`_is_confirmation_transition(edit_dir, n+1)`: True when `edit-log.round-(n+1).md` contains a
`round_type: confirmation` marker line (add the marker to editorial-review's re-review
protocol for confirmation rounds) OR score-history.md labels round n+1 "confirmation".

For RUN-004: scope `_findings_with_severity` to ids declared in a `finding_id:` YAML block
with an explicit severity field, excluding table rows / prose mentions:

```diff
-FINDING_RE = re.compile(r"(r\d+-F\d+)")            # (illustrative)
+FINDING_RE = re.compile(r"^\s*-?\s*finding_id:\s*(r\d+-F\d+)", re.M)
```

Ship with two test_gates/check_run fixtures: (a) a confirmation transition without a
revision-response (must PASS), (b) a verification-table id not re-ruled (must PASS), a
declared medium dropped (must still FAIL).

## Amendment (2026-07-04, etched-us20240378175)

Second manifestation, second run in a row: RUN-003 x10 false FAILs because the severity
regex does not recognize `prior_severity:` lines inside the carried_finding_rulings blocks
that the id-continuity rule itself forces reviewers to write. The two defects compound: the
checker demands continuity notation, then misparses that notation as new findings.
Recurrence for the artifact is now 2 runs / 2 distinct defects -> upgrade confidence; the
fix should cover BOTH: (a) confirmation-transition modeling, (b) severity parsing of
carried-ruling notation (`prior_severity:`), or scoping the id harvest to declared finding
blocks (`^\s*-?\s*finding_id:` with an adjacent `severity:` field).
