---
proposal_id: 2026-07-11-selfaudit-dropped-low-recheck
created: 2026-07-11T14:35:00Z
status: watch
lever: reference-edit
goal: "1"
root_cause_stage: orchestrator
root_cause_artifact: self_audit multi-vote LOG-AND-DROP disposition (contracts/stages/self_audit.yaml + patent-essay SKILL self-audit section)
recurrence_count: 1
confidence: medium
triggering_findings:
  - essay_id: tesla-us20260196678-hemmed-tabless, finding_id: SA2-C1, pattern_tag: claim-scope-absolute (round-1 A-10 low, dropped, re-escalated medium)
  - essay_id: tesla-us20260196678-hemmed-tabless, finding_id: SA2-C2, pattern_tag: claim-scope-misattribution (round-1 A-7 low, dropped, re-escalated medium)
---

## Problem

The self-audit round-1 multi-vote LOG-AND-DROPped 13 lows. The round-2 dry-loop check
(fresh hostile persona, blind by contract) found exactly two mediums — and **both were
round-1 dropped lows re-escalated**:

- A-10 "Nothing is welded on." (low, dropped) → C-1 MEDIUM (`claim-scope-absolute`:
  [0019]/[0023] list welding; the essay quotes the welding menu two sections later —
  quotable against itself);
- A-7 "claimed ... selective coating" (low, dropped) → C-2 MEDIUM
  (`claim-scope-misattribution`, external-patent variant: log supports mechanism, not
  claim scope, for US 11,749,842 B2).

Both are claim-scope absolutes/attributions — the run's (and the ledger's) dominant
goal-1 family. Cost of the drop: one full extra self-audit round, plus a lane fallback
on the resulting micro-revision (grok invalid-output ×2 → inherit). One run's evidence,
two instances of the same mechanism → watch (hypothesis recorded, no diff mandated yet).

## Proposed change (hypothesis — to be refined on recurrence)

In the multi-vote arbitration rules: lows are still droppable, EXCEPT lows whose class
is in the claim-scope family (`claim-scope-*`, `option-embodiment-upgraded`,
`external-fact-*` on load-bearing sentences). Those get a one-shot mechanical verdict
from the already-running GPT grounding lane (claimed-vs-described check on the flagged
sentence) **before** the drop decision: SUPPORTED → drop stands; anything else → apply
with the round-1 batch. Reader isolation is untouched — round-2+ readers stay blind;
only the orchestrator's disposition step changes, and the marginal cost is a few
sentences appended to a grounding check that runs anyway.

## Why this lever

reference-edit on the self-audit arbitration contract is the only place the drop
decision lives. Not a gate: the judgment is claimed-vs-described semantics, exactly what
the grounding verifier lane already adjudicates well (this run: 3/3 genuine overreach
catches).

## Regression expectation

None mechanical (contract text only). Watch for: a future run where a dropped
claim-scope low re-escalates again → promote with the exact contract diff.
