---
proposal_id: 2026-07-06-check-run-confirmation-transition-veto
created: 2026-07-06T17:30:00Z
status: proposed  # first isolation; latent (no false-pass this run) but structural masking risk on a mandatory completeness check
lever: gate-strengthen
goal: "all"
root_cause_stage: gate
root_cause_artifact: _shared/scripts/check_run.py — _is_confirmation_transition (loose "confirmation" marker match) + the RUN-003 disposition gate that trusts it without a revision-response veto
recurrence_count: 1  # but inverse of an already-APPLIED fix (2026-07-03-check-run-confirmation-round-model); the two together bracket both failure modes of the same feature
confidence: medium-high  # reproduced deterministically; no harm this run, but the fix is small, safe, and non-regressing
triggering_findings:
  - essay_id: intel-us20260191095-backend-hbm, check_id RUN-000, pattern_tag checker-confirmation-overfire (round 1->2 real revision mislabeled as a confirmation transition; RUN-003 disposition-coverage silently skipped)
relates_to: 2026-07-03-check-run-confirmation-round-model  # APPLIED; this is the inverse failure mode of that feature
---

## Problem — the confirmation-transition model now OVER-fires (inverse of the applied fix)

The applied proposal `2026-07-03-check-run-confirmation-round-model` taught `check_run.py` to
recognize a **confirmation round** (the loop spec's second clean review of an UNCHANGED draft,
run with no revision in between) so it would stop **false-FAILing** it for lacking a
`revision-response.round-N.md`. It fixed the model **under**-firing.

This run surfaces the **inverse** hazard: the same model now **over**-fires. `check_run.py`
classified the **round 1 → 2** transition as a confirmation transition and **skipped the
RUN-003 disposition-coverage check** for round 1's findings — but round 1 → 2 was a **real
revision**. Reproduced deterministically against the live artifacts:

```
$ python .claude/skills/_shared/scripts/check_run.py --handoff handoff
[PASS] check_run
  WARN  RUN-000  round 1 -> 2 is a confirmation transition (no revision in between);
                 revision-response/disposition requirements skipped for this transition
  WARN  RUN-000  round 2 -> 3 is a confirmation transition ...
```

Round 1 → 2 was **not** a confirmation transition. `handoff/02-compose/revision-response.round-1.md`
exists and records **7/7 findings applied** (2 medium — r1-F1, r1-F2 — + 5 low). The draft was
genuinely revised (draft_version 1 → 2). Only round **2 → 3** is a real confirmation transition
(unchanged draft, independent fresh reviewer).

### Why it misfired

`_is_confirmation_transition(edit_dir, score_path, next_round)` returns True on **any one** of
three loose text signals for `next_round`. Two of them matched `next_round=2` on wording that
describes what a **clean round triggers NEXT**, not an assertion that round 2 **is** a
confirmation:

- **Signal 2** (`CONFIRMATION_PHRASE_RE`, `edit-log.round-2.md` first 40 lines) matched line 8:
  *"this is the FIRST clean round → triggers a **CONFIRMATION round** (round 3), NOT
  acceptance."*
- **Signal 3** (score-history row substring) matched the round-2 row:
  *"CLEAN (first) ... First clean → **confirmation** trigger, NOT acceptance."*

The detector cannot distinguish *"this clean round triggers a confirmation round next"* from
*"this round is itself the confirmation round."* (Note: `edit-log.round-2.md` carries **no**
`round_type: confirmation` structured marker — grep across all edit-logs finds zero — so
detection ran **entirely** on the loose signals.)

### Why it matters (the masking risk, symmetric with the over-hedge doctrine)

Across a confirmation transition, `check_run.py` deliberately **skips RUN-001 and RUN-003**
(there is no revision to trace or disposition). So mis-labeling a **real** revised transition as
a confirmation **silently drops RUN-003** for that round's medium+ findings and any failing
gate check_id. This run was harmless — the dispositions all exist, and **RUN-004 id-continuity
still ran** across the transition, so a *dropped* finding would still have been caught. But
RUN-003 checks something RUN-004 does not: that each medium+ finding has a **disposition block**
in `revision-response.round-N.md`, and that a failing gate check_id is dispositioned. A future
run where a genuinely-revised round's log or score-row merely uses the word "confirmation" (an
easy, natural phrasing — every first-clean round "triggers a confirmation round") would have its
RUN-003 disposition-coverage **silently skipped**, masking a real gap on the exact mechanical
check that defends disposition completeness.

## Proposed change (exact diff sketch) — the revision-response veto

Make the **presence of `revision-response.round-N.md`** dispositive. A confirmation transition
takes **no** revision by spec, so a revision-response for round N and a real confirmation at the
N → N+1 transition are **mutually exclusive**. If the response file exists, a real revision
happened — run the disposition checks, whatever the score-history/edit-log wording says.

This is a **call-site restructure** in `check(...)` (both `compose_dir` and `n` are in scope
there); `_is_confirmation_transition` itself is unchanged.

**File: `.claude/skills/_shared/scripts/check_run.py`** (the `if n < K:` block, ~lines 230-241):

```diff
         if n < K:
-            if _is_confirmation_transition(edit_dir, score_path, n + 1):
+            resp_path = os.path.join(compose_dir, "revision-response.round-%d.md" % n)
+            resp_exists = os.path.exists(resp_path)
+            confirmation = _is_confirmation_transition(edit_dir, score_path, n + 1)
+            # VETO: a revision-response is dispositive proof a real revision happened at
+            # this transition. A confirmation round takes no revision (loop spec), so the
+            # response file and a real confirmation transition cannot coexist. Presence of
+            # the file overrides any "confirmation" marker/wording and forces RUN-003.
+            if resp_exists:
+                if confirmation:
+                    add("RUN-000", "warn",
+                        "round %d -> %d carries BOTH a revision-response and a "
+                        "'confirmation' marker; the revision-response is dispositive "
+                        "(a confirmation round takes no revision) -- treating as a REAL "
+                        "revision and running disposition checks" % (n, n + 1), edit_dir)
+                # ... existing RUN-003 disposition + failing-gate block runs unchanged ...
+            elif confirmation:
                 add("RUN-000", "warn",
                     "round %d -> %d is a confirmation transition (no revision "
                     "in between); revision-response/disposition requirements "
                     "skipped for this transition" % (n, n + 1), edit_dir)
             else:
-                resp_path = os.path.join(compose_dir, "revision-response.round-%d.md" % n)
-                if not os.path.exists(resp_path):
-                    add("RUN-001", "fail",
-                        "revision-response.round-%d.md missing ..." % (n, n), compose_dir)
-                else:
-                    resp = _read(resp_path)
-                    ... RUN-003 disposition checks ...
+                add("RUN-001", "fail",
+                    "revision-response.round-%d.md missing (round %d was revised "
+                    "without a disposition trace)" % (n, n), compose_dir)
```

(The existing RUN-003 body — `resp = _read(resp_path)`, the per-finding disposition loop, and
the failing-gate loop — moves under the `if resp_exists:` branch unchanged. Only the branching
order changes: **check for the response first**, consult the confirmation markers only to decide
whether an **absent** response is legitimate.)

### Optional defense-in-depth (secondary, do not ship alone)

The loose markers could also be tightened to fire only on an **assertion** that the round IS a
confirmation (e.g. prefer the structured `round_type: confirmation` marker, or match the
score-history **type column** rather than a free-text substring). This is **secondary** and
carries regression risk: this run's confirmation rounds emit **no** `round_type` marker, so
tightening the markers alone — without the veto — would re-introduce the exact false RUN-001
FAIL the 2026-07-03 proposal fixed. **The veto is the whole fix; ship it alone.** Marker
tightening should only follow after editorial-review is amended to always emit
`round_type: confirmation` on confirmation rounds (a separate reference-edit).

## Why this lever

- The defect lives in the checker's control flow (`root_cause_stage: gate`); no reference or
  authoring-discipline change closes a mechanical masking hole on a mandatory completeness check.
- **Strict refinement / cannot regress a legitimate confirmation round.** A real confirmation
  round reviews an unchanged draft and therefore has **no** `revision-response.round-N.md` — so
  the veto never fires on it. Verified against this run: `revision-response.round-1.md` **exists**
  (veto fires → 1→2 correctly treated as a real revision, RUN-003 runs) while
  `revision-response.round-2.md` is **absent** (veto silent → 2→3 stays a confirmation, RUN-003
  correctly skipped). The veto flips exactly the one transition that was wrong and leaves the
  correct one untouched.
- **Brackets the feature with its applied inverse.** `2026-07-03-check-run-confirmation-round-model`
  stops false FAILs on real confirmation rounds; this stops false SKIPS on real revisions. Both
  are needed for the confirmation model to be sound in both directions.

## Regression expectation

Run `python meta/regression.py` before applying. Expected after:

- `python .claude/skills/_shared/scripts/check_run.py --handoff handoff` on this run's live
  tree: round **1→2** no longer reported as a confirmation transition (RUN-003 runs; all round-1
  dispositions present → still PASS); round **2→3** still reported as a confirmation transition
  (RUN-000 warn, RUN-003 skipped). Overall verdict unchanged: **PASS**.
- Existing check_run fixtures/tests: unchanged. A confirmation-round fixture (no
  revision-response) is untouched by the veto. Any fixture with a real, fully-dispositioned
  revision stays PASS. The veto can only **add** RUN-003 evaluations, never remove them.
- **New fixtures to ship** (both built to mirror this run's shape):
  (a) a round 1→2 transition with `revision-response.round-1.md` present **and** a "confirmation"
      mention in `score-history.md`/`edit-log.round-2.md`, all medium findings dispositioned →
      must **PASS** (veto runs RUN-003, coverage complete);
  (b) the same but with one medium finding's disposition **missing from**
      `revision-response.round-1.md` → must **FAIL RUN-003** (the gap the old heuristic masked is
      now surfaced).
- Observable next-run criterion: a run's first-clean round can say it "triggers a confirmation
  round" in its log/score-row without `check_run.py` skipping the prior round's disposition
  checks; genuine confirmation transitions (no revision-response) still skip them correctly.
