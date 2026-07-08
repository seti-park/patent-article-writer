---
proposal_id: 2026-06-11-external-fact-scope-discipline
created: 2026-06-11T16:30:00Z
status: recommended-apply
lever: reference-edit
goal: "1"
root_cause_stage: compose
root_cause_artifact: essay-en-composer/references/execution-boundary.md (external-fact scope discipline)
recurrence_count: 3
confidence: medium
triggering_findings:
  - essay_id: 2026-06-10-us12636684b1-deleted-dome, iter: 1, pattern_tag: external-fact-universalization
  - essay_id: 2026-06-10-us12636684b1-deleted-dome, iter: 2, pattern_tag: external-fact-universalization
  - essay_id: 2026-06-11-us20260158546a1-both-and-steel, iter: 1, pattern_tag: external-fact-universalization
---

## Problem

External (non-patent) facts get **universalized beyond the fact-check-log entry's literal
scope** during composition. 3 ledger records, 2 distinct instances, **2 of 2 essays**,
`medium` at first appearance both times (goal 1, accuracy):

- Run 1 (medium → low residue): "the industry sprays its covers" universalized from the
  dlhBowles nozzle facts, whose logged scope also covers spraying a bare lens; the verified
  invariant was non-contact cleaning, not cover-as-universal. Editor recommendation,
  verbatim: *"Tie external-fact prose scope to the fact-check-log entry's literal scope;
  assert a universal only when the log states one."*
- Run 2 (medium, F2): EOS maraging steel "sold for exactly this kind of work" stretched the
  logged fact (`eos-ms1-18ni300-aging`: "typical applications **include** injection-molding
  tools and inserts") into a universal fit. Fixed by naming the logged scope explicitly.

`execution-boundary.md` already locks **which** facts may be used (`facts_locked`) but says
nothing about the **scope** of prose built on them — the recurring gap is over-claiming from
an admitted fact, which no gate can see.

Record count 3 = RECUR_THRESHOLD, cross-essay 2/2 → `recommended-apply`. Confidence
`medium` (not high) because the distinct-instance count is 2; the third record is run-1's
same-instance residue (accepted title/aphorism compression).

## Proposed change (exact diff)

**File: `.claude/skills/essay-en-composer/references/execution-boundary.md`** — extend the
"Quick reference" per-sentence checklist:

```diff
 Before composing each sentence:
 - Is this a factual claim? → Cite [^fact-id] from facts_locked
 - Is the fact in facts_locked? → If no, stop. Gap detected.
+- Is it an EXTERNAL (non-patent) fact? → Prose scope must not exceed the fact-check-log
+  entry's literal scope. Assert a universal ("the industry…", "sold for exactly this…")
+  only when the log entry states one; if the log says "include"/"typical"/"can also",
+  name the logged scope explicitly instead of universalizing it. Titles and closing
+  aphorisms may compress a scoped fact only when the precise scoped statement appears in
+  nearby body prose (deliberate-compression allowance, on the record).
 - Is this transition/interpretation prose? → No citation needed, but no new facts either
```

## Why this lever

- Root cause is a compose-stage procedural gap, and `execution-boundary.md` is the artifact
  the composer is required to check sentence-by-sentence — the rule lands exactly where the
  failure happens. Both editors' fixes were applications of this same sentence.
- Not gate-promotion: scope comparison requires reading the log entry's semantics
  ("include" vs "is"); a regex would be all false positives.
- The title/aphorism allowance clause encodes run-1's iter-2 adjudication (compression
  backed by precise nearby prose was accepted as deliberate), so the rule doesn't outlaw a
  pattern the editor already sanctioned.

## Regression expectation

Documentation-only change. `python .claude/skills/_shared/scripts/test_gates.py` and
`python meta/regression.py` unchanged green (no script or fixture touched). Success
criterion: zero pass-3 external-fact scope findings in the next run; a third *distinct*
instance after applying would flip this class toward `ineffective-patch` accounting
(CASCADE_CAP watch).
