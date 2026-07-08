---
proposal_id: 2026-07-04-pending-application-edition
created: 2026-07-04T09:35:00Z
status: recommended apply  # edition ran end-to-end clean; codifying prevents re-derivation drift
lever: reference-edit
goal: "1 / 4a"
root_cause_artifact: thesis-architect references (claim-scope classes) + essay-context template
recurrence_count: 1 run (full pipeline, double-clean + 3-round self-audit, zero edition violations found by 7 independent reviewers/verifiers)
confidence: high
triggering_findings:
  - essay_id: etched-us20240378175 — first pending-application run; edition rules lived only in a per-run essay-context.md
---

## Problem

The pipeline's claim-scope machinery (Claim scope map, locked/open/pinned classes,
grant-era verb conventions) presumes a granted patent. This run proved a pending-application
edition works — sought-* scope classes, application-era language, prosecution-label budget,
collateral-scope discipline — but every rule was hand-authored in input/essay-context.md.
The next pending-application run would re-derive them from scratch, and drift is likely
(e.g. a run whose context brief forgets the enforceability-verb ban).

## Proposed change

1. thesis-architect/references (claim-scope conventions): add a "pending application"
   section — scope classes sought-broad/-structured/-system/-<specific> with a
   prosecution-risk note per independent; no locked class may be emitted for an A1 input.
2. essay-en-composer voice/citation references: application-era verb table (claims/seeks/
   as-drafted vs locks/fences/requires-of-competitors) + the enforceability-language ban.
3. handoff-template essay-context: an optional "Edition: pending-application" block
   carrying the label-sentence budget, the sought-scope rule, and the collateral/absence
   evidence_level discipline, so per-run briefs opt in rather than re-derive.
4. Detection guard: gate_meta (or a Phase-1 self-check) warns when input/patent.md's header
   says application/A1 but the invention-summary emits a "locked" scope class.

Evidence: this run's edit-logs (edition compliance verified as first-class content in all
4 inner rounds), selfaudit reports (zero grant-era verbs found in 3 grounding sweeps), and
score-history (double-clean + readers dry x2 rounds at cap).
