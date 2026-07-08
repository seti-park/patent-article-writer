---
proposal_id: 2026-07-03-external-fact-evidence-scope
created: 2026-07-03T00:20:00Z
status: watch
lever: reference-edit
goal: "1"
root_cause_artifact: essay-context template + thesis-architect fact-check-log schema
recurrence_count: 1
confidence: high (caught by this run's own grounding verifier)
triggering_findings:
  - essay_id: etched-us12361091, sa3G-F1 (medium): "LVI is nowhere in this filing or its granted siblings" asserted sibling-full-text absence on bibliographic-only evidence
---

## Problem

essay-context.md carried sibling-patent facts from a bibliographic export (WIPS) without an
evidence-level marker; downstream prose inherited them at full-text confidence. The
self-audit grounding verifier caught the absence-claim as evidence-scope overreach and the
fix narrowed the sentence to "this filing". The failure class: external facts whose
evidence level (bibliographic / abstract / full-text) is silently upgraded by fluent prose.

## Proposed change

1. essay-context template: each external fact row gains `evidence_level:
   bibliographic|abstract|full-text|company-claim`.
2. thesis-architect propagates the field into fact-check-log.md rows.
3. citation-format.md gains one rule: absence/universal claims ("X is nowhere in Y")
   require `evidence_level: full-text` for Y; otherwise scope the claim to the evidence
   ("nothing in Y's abstract/bibliography").
4. grounding-verifier prompt template names the field explicitly (it already enforces the
   concept — sa3G-F1 proves the check works; this makes it cheap and upstream).
