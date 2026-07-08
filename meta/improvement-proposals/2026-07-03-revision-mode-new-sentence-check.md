---
proposal_id: 2026-07-03-revision-mode-new-sentence-check
created: 2026-07-03T00:20:00Z
status: watch
lever: reference-edit
goal: "1"
root_cause_artifact: essay-en-composer/references/revision-mode.md
recurrence_count: 2 (within-run: SA round-2 medium on round-1-added text; SA round-3 medium on round-2-added text)
confidence: medium
triggering_findings:
  - essay_id: etched-us12361091, sa2B-F1 -> added design-around sentence -> sa3B-F1 (dependency mischaracterization in that added sentence)
---

## Problem

Each self-audit revision round's medium findings concentrated on text ADDED by the previous
revision: the round-2 steelman addition mischaracterized claims 8/9/11's dependency
structure and was itself the round-3 medium. New sentences enter the draft with less
scrutiny than original composition (which had the full spine/anchor discipline).

## Proposed change

revision-mode.md gains one mandatory step: for every NEW sentence that states claim
structure or cites an anchor, quote-check it against the claim text / span carried in the
finding being applied (the audit reports quote the patent verbatim — check against THAT,
not memory) before returning. One line in the revision-response per new sentence:
`new-sentence check: <claim/anchor> verified`.

## Amendment (2026-07-04, etched-us20240378175)

Recurrence now 4 within-run instances across 2 runs: this run's FIG. 7 caption needed THREE
touches (r2-F1 semantic re-anchor; sa2G-F1 missing [0056]; sa3G-F1 clause-boundary split) —
each fix's new text spawned the next round's finding. Two additions to the proposed check:
(1) multi-clause captions anchor EACH clause to its own paragraph at write time;
(2) formalize the fix-at-source span-request protocol that worked ad hoc twice this run
(composer BLOCKED -> Phase 1 adds q-NNNN span verbatim -> composer applies): revision-mode.md
should name it as the standard path when a fix needs an anchor outside the design bundle,
instead of relying on orchestrator improvisation.
