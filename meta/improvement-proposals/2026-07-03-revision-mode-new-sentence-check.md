---
proposal_id: 2026-07-03-revision-mode-new-sentence-check
created: 2026-07-03T00:20:00Z
status: recommended-apply
lever: reference-edit
goal: "1"
root_cause_artifact: essay-en-composer/references/revision-mode.md
recurrence_count: 9 (within-run instances across 3 runs; see amendments)
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

## Amendment (2026-07-11, tesla-us20260196678-hemmed-tabless) — PROMOTED to recommended-apply

Recurrence 4 → 9 (third consecutive run; five within-run instances here), and the
mechanism broadened beyond grounding exactly as the intel run's term-collision note
predicted. This run, **every round-2 medium was a round-1 application side-effect**, and
two self-audit mediums were revision-added text:

- r2-F1 (`revision-induced-duplication`): the r1-F9 gloss re-pasted verbatim into §5 —
  DUPE-001's five windows were all this one phrase;
- r2-F2 + r2-F3 (`revision-induced-band-break`): the r1-F8/r1-F9 gloss insertions
  (content-correct) pushed the lead paragraph over the mobile band and stretched the
  closing watch-list to a 41-word comma pile;
- SA-7 (`evidence-scope-overreach`): the steelman sentence ADDED by the r1-F4 fix
  carried three document-wide absence claims on a [0002] anchor that supports one;
- SA-9 (`garbled-sentence-grammar`): the interpolated sentence CREATED by the r1-F7 fix
  became the cold reader's read-three-times stumble.

Scope addition on apply: the new-sentence self-check re-scans added/edited sentences on
**four legs**, not one — (a) grounding/anchor scope (original), (b) duplication against
the existing draft (the gloss echo), (c) band/length re-count of the receiving paragraph
and sentence, (d) parse quality (dangling participles, interpolated appositives). One
line each in the revision-response. Cost: seconds per revision; this run spent one full
review round + two self-audit findings on exactly these four legs.
