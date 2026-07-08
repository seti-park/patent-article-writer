---
proposal_id: 2026-06-26-self-audit-origin-and-goal-acceptance
created: 2026-06-26T00:00:00Z
status: applied
applied: "2026-06-27 (branch claude/nice-ptolemy-epd4el) — Part A normalizer origin + Part B orchestrator self-audit stage (patent-essay/SKILL.md) + scoring-rubric Layer 3 + CLAUDE.md three-tier loop control. selftest + meta/regression.py + gate suite green."
lever: new-tool + reference-edit
goal: "1, 2, 3, 4a, 4b (cross-cutting: the autonomous self-check itself)"
root_cause_stage: orchestrator + meta
root_cause_artifact: patent-essay/SKILL.md (acceptance set) + meta/normalize_revision_notes.py (origin) + scoring-rubric.md
recurrence_count: 1
confidence: high
triggering_findings:
  - essay_id: 2026-06-26-us12560948b2-investor-selfaudit, pattern_tag: self-audit-channel-demonstrated (11 findings caught + resolved autonomously across two rounds after the inner loop returned pass)
---

## Problem

The inner Compose↔Edit loop can return `overall_assessment == pass` with all ten gates green, and
the draft can still carry editorial and grounding blind-spots that only a *fresh* adversarial read
catches — exactly the misses the run-045 human-revision channel was built to record. The open
question (the user's): can `/goal` drive that fresh adversarial read **autonomously**, with no
human in the loop, so the system self-corrects past its own "pass"?

This run answers it empirically: **yes.** On the loop-PASSED investor essay for US 12,560,948
(`essays/agility-us12560948/essay-final.md`), a fresh-context adversarial pass found 1 high + 6
medium + a real claim-scope grounding slip the loop's pass-3 missed; the fixes were applied
autonomously; a second blind fresh-context pair verified convergence (0 high, 0 medium of the
round-1 classes; both reviewers "publishable as-is"). The mechanical layer even backstopped the
judgment layer mid-run: `gate_dupe` caught a 5-gram echo that a round-1 fix introduced.

Two things are missing to make this a standing capability rather than a one-off:

1. The revision-delta channel has no **origin** for "the self-audit caught it" — `normalize_revision_notes.py`
   hardcodes `human-post-accept`. Self-caught findings are invisible to `pipeline-retro`'s recurrence
   scoring, or worse, mislabeled as human.
2. There is no **acceptance set** that tells `/goal` what "self-audited" means, so the autonomous
   pass depends on whoever drives it remembering to run it.

## Proposed change

### Part A — `self-post-accept` origin (APPLIED on branch `claude/nice-ptolemy-epd4el`; port to main)

`meta/normalize_revision_notes.py` gains a backward-compatible `--origin` / `--source` pair
(default unchanged: `human-post-accept` / `human-revision`) and six new CLASS_MAP rows for the
classes the autonomous pass surfaces. The selftest is extended to prove the default path is
untouched AND the new origin flips `origin` / `source` / the finding verb. Exact diff (already on
the branch, `meta/regression.py` = PASS, gate suite = PASS):

```diff
-def to_record(d, essay_id, ts):
+def to_record(d, essay_id, ts, origin="human-post-accept", source="human-revision"):
@@
-    finding = "post-accept revision%s: %r -> %r. %s" % (
+    verb = "self-audit revision" if origin == "self-post-accept" else "post-accept revision"
+    finding = "%s%s: %r -> %r. %s" % (
+        verb,
@@
-        "source": "human-revision",
-        "origin": "human-post-accept",
+        "source": source,
+        "origin": origin,
@@
-def normalize(text, essay_id, ts):
-    return [to_record(d, essay_id, ts) for d in parse_notes(text)]
+def normalize(text, essay_id, ts, origin="human-post-accept", source="human-revision"):
+    return [to_record(d, essay_id, ts, origin, source) for d in parse_notes(text)]
```
Plus the `--origin {human-post-accept,self-post-accept,inner-loop}` / `--source` argparse pair
(source auto-pairs to `self-audit` when origin is `self-post-accept`), the six CLASS_MAP rows
(`claim-scope-misattribution`, `legal-posture-language-slip`, `prosecution-record-overstatement`,
`figure-caption-scope-deferral`, `figure-cover-undervalued`, `anchor-incomplete`), and the
matching attribution-table section. NOTE: main's `normalize_revision_notes.py` and the run-045
attribution rows are AHEAD of this branch; reconcile by taking main's file and re-applying only the
`--origin`/`--source` hunk + the six rows (no conflict — additive).

### Part B — `/goal` autonomous self-audit acceptance set (reference-edit; for `patent-essay/SKILL.md` + `scoring-rubric.md`)

Add a self-audit stage the orchestrator runs AFTER the inner loop returns `pass`, gated by a
`/goal` acceptance set so it is enforced, not optional:

```
/goal the patent-essay run is self-audited: after the inner loop returns pass with all gates
green, a fresh-context adversarial pass (pass-7 personas, run in a SEPARATE context from compose
+ edit) returns NO unresolved high or medium finding, the grounding hard-gate holds
(claim-scope verified against the claims, anchors re-checked), and a second blind fresh-context
pass confirms convergence; all applied deltas are logged via the revision-delta channel with
origin: self-post-accept.
```

Why this is reliable and not just "ask the model if it's good" (the mechanisms this run used):
- **Fresh context = real voice/eval fence.** The reviewer has no commitment to the draft's choices;
  it is told to assume the draft is flawed and hunt. This is what converts a soft self-grade into a
  finding.
- **Decompose + force evidence.** Every pass-7 check is a yes/no with a quoted span or `ABSENT`,
  never a holistic rating. A claim-scope check quotes BOTH the essay span and the claim/paragraph.
- **Multi-vote + persona diversity.** Two independent reviewers (impatient-investor, IP-skeptic);
  a finding is applied on agreement, logged-and-dropped on a split. This run applied the 2 findings
  both raised and correctly declined a singleton low and a round-1 candidate that failed grounding.
- **Keep the hard-gates.** Grounding (claim-scope) and goal-2 (orphan figure) stay hard; the
  self-audit can only ADD findings, never lower the existing bar.
- **Loop until dry, bounded.** Re-audit after each apply round; stop when a fresh pass adds no
  high/medium (this run: 2 rounds). The mechanical gates re-run every round and backstop the edits.

## Evidence (this run)

| round | trigger | findings | applied |
|---|---|---|---|
| v1 | inner loop | pass, 10/10 gates 0 findings | baseline |
| v2 | round-1 fresh pair (multi-vote) | 1 high + 6 medium + 1 grounding slip | 8 |
| v2.1 | `gate_dupe` re-run | 1 self-introduced 5-gram echo (warn) | 1 |
| v2.2 | round-2 fresh pair (multi-vote) | 0 high/0 medium of round-1 classes; 2 agreed lows (1 medium per reviewer B) | 2 |
| final | gates + both reviewers | 0 gate findings; "publishable as-is" ×2 | converged |

Artifacts: `essays/agility-us12560948/essay-final-selfaudit.md` (the autonomously revised v2.2),
`revision-notes.md` (11 `## delta` blocks + the considered-not-applied log),
`revision-notes.ledger.jsonl` (the normalized records), 11 records appended to
`meta/findings-ledger.jsonl` as the first `self-post-accept` dataset.

## Why this lever

- Part A is a tool extension whose whole risk surface is covered by the selftest + `meta/regression.py`
  (both PASS); it is additive and backward-compatible.
- Part B is a reference-edit to the orchestrator's acceptance set and the rubric. It does not change
  any gate or any pass; it makes the fresh adversarial pass a required, evidence-forced stage rather
  than an optional one. The self-audit can only raise the bar.

## Regression expectation

- `python meta/normalize_revision_notes.py --selftest` → OK (default + origin-flag).
- `python meta/regression.py` → PASS (32 tests + 2 fixtures), unchanged.
- Success criterion: the next run, after the inner loop says `pass`, produces a `revision-notes.md`
  with `origin: self-post-accept` deltas and a convergence record, with no human edit in between.

## Related

- Extends `2026-06-26-human-revision-blindspots.md` (the human channel) with its autonomous twin.
- Uses the run-045 `pass-7-adversarial-reader.md` checklist as the self-audit's evidence-forced spec.
- Pairs with the standing backstop already documented in CLAUDE.md:
  `/goal the patent-essay SCORE HISTORY shows a final draft that passes all gates with overall_assessment == pass`.
