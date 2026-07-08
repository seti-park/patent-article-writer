---
proposal_id: 2026-06-24-conclusion-over-hedge-check
created: 2026-06-24T03:30:00Z
status: watch
lever: reference-edit
goal: "4a"
root_cause_stage: edit
root_cause_artifact: editorial-review/references/pass-6-lead-conclusion-format.md (no over-hedge check) + posture-lens.md (no firm-closing default for verdict editions)
recurrence_count: 1
confidence: medium
triggering_findings:
  - essay_id: us12560948b2 ad-hoc run (pre-pipeline), pattern_tag: conclusion-over-hedge, surfaced by SETI catch (not in ledger)
  - essay_id: 2026-06-24-us12560948b2-safe-stop, iter: 1, pattern_tag: conclusion-over-hedge (prevented; firm-closing posture held)
---

## Problem

The 6-pass rubric is asymmetric. Pass 3 and Pass 4 defend hard against factual and causal
**overreach** (claimed too much, correlation framed as causation, indirect evidence behind a
direct claim). No pass defends against **over-hedge**: a verdict too defensive for the evidence
the body already established. For an essay whose job is to land a call (investor, analysis, or
assessment editions), an over-hedged conclusion is a real quality failure, and the rubric cannot
currently see it.

This surfaced concretely on US 12,560,948 B2. An ad-hoc (pre-pipeline) article on the patent
passed all six deterministic gates and the measured 6-pass loop, yet closed over-defensively:

- it led with the qualifier, not the call ("The verdict is a qualified yes");
- it set the moat and its limits as equal weights ("Its limits are equally real");
- it re-listed caveats in the verdict that the dedicated limits section had already covered.

None of the six passes flagged any of that. Only a human (SETI) read caught it. When the run was
redone through the formal pipeline, the fix lived entirely upstream: `thesis-spine.md` pinned a
firm-closing posture and the composer drafted it in, so the loop passed in one round. That
confirms the gap is structural, not a one-off: absent the pinned posture, the loop would have
accepted the over-hedged close again.

`recurrence_count` is 1 documented incident (plus one prevented recurrence this run), below
RECUR_THRESHOLD=3, so this files at `watch`. It is surfaced now with the exact diff because the
defect is a structural rubric asymmetry confirmed by a real incident and a human catch, and
because verdict editions (the investor edition the system is now producing) are exactly where it
bites.

## Proposed change (exact diff)

**File 1: `editorial-review/references/pass-6-lead-conclusion-format.md`** — add a sub-check
after 6F:

```markdown
## 6G — Verdict confidence proportionate to evidence (over-hedge guard)

For essays that land a verdict or recommendation (investor / analysis / assessment editions),
check that the conclusion's confidence matches the evidence the body established. This is the
mirror of Pass 3 / Pass 4, which guard OVERREACH; 6G guards OVER-HEDGE.

Flag (over-hedge):
- the verdict leads with the qualifier instead of the call ("a qualified yes" before the "yes");
- false equivalence between the thesis and its limits ("the limits are equally real");
- caveats re-listed in the verdict that a dedicated limits section already covered (state once,
  then reference);
- stacked hedges a body with firm evidence does not warrant.

Do not invert the fix into overclaim: a firm verdict still keeps exactly one anti-hype guard and
never asserts beyond the claim scope (Pass 3 still binds).

Severity: medium under measured posture; high when `thesis-spine.md` declares a firm-closing
posture and the draft violates it.
```

**File 2: `editorial-review/references/posture-lens.md`** — add to the closing/Pass-6 row a note:

```markdown
Verdict editions (investor / analysis) default to a firmer closing. When thesis-spine declares a
firm-closing posture, an `Acknowledged` residual risk maps toward `closing-forward-watching-event`
or `closing-binary-test`, NOT `closing-open-question`; an over-hedged close is then a 6G finding.
```

**File 3: `meta/attribution-table.md`** — add a row to the main table:

```markdown
| `conclusion-over-hedge` | SETI catch / pass-6 6G | 4a | design + edit | thesis-spine closing posture + pass-6-lead-conclusion-format.md | reference-edit (or rubric-tuning: posture) |
```

## Why this lever

- No mechanical gate can judge "confidence proportionate to evidence"; it requires reading the
  body's evidence against the verdict's strength. So the check belongs in Pass 6 judgment plus a
  posture default, not a regex gate. Not gate-promotion.
- reference-edit is the cheapest lever that hits the root: the failure is a missing review lens
  (Pass 6) and a missing closing default (posture-lens). Both are documentation.
- It encodes the SETI catch as a reusable rule so the next verdict edition does not depend on a
  human noticing the over-hedge.

## Regression expectation

Documentation-only change (three Markdown files; no script, no banned list, no fixture). After
applying:

- `python .claude/skills/_shared/scripts/test_gates.py` — unchanged, all pass.
- `python meta/regression.py` — `clean-baseline` and `figure-orphan` fixtures unchanged (no gate
  reads these files).
- Observable success criterion: the next investor-edition run lands a firm, evidence-proportionate
  verdict by construction, and Pass 6 6G flags any over-hedge before a human catch is needed.
