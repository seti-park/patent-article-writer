---
proposal_id: 2026-07-05-phase1-nonquote-label-grounding
created: 2026-07-05T19:30:00Z
status: watch
lever: reference-edit
goal: "1"
root_cause_stage: design
root_cause_artifact: thesis-architect invention-summary (Layer-2 mechanism labels) + figure-rationale.md (figure part-nouns) — non-quote descriptive labels are not verified verbatim-consistent against their cited paragraph the way gate_quotes verifies quote spans
recurrence_count: 2
confidence: medium
triggering_findings:
  - essay_id: intel-us20250266395, iter: 1, pattern_tag: phase1-nonquote-label-drift (r1-F3 "face-down" not in [0060], invention-summary Layer-2 step 1)
  - essay_id: intel-us20250266395, iter: 2, pattern_tag: phase1-nonquote-label-drift (r2-F2 "solder balls" vs [0048] "ball-pitch solder pads", figure-rationale.md)
related:
  - etched-us20240378175-r2 self-audit: document-section-mislabel ("Background" [0018]/[0043] actually in the detailed description) — a cousin non-quote-label precision miss, different artifact
---

## Problem — the grounding chain has a gap gate_quotes structurally cannot cover

The grounding chain has two halves. The **quoted** half is mechanically defended: `gate_quotes`
proves every invention-summary Quotable span / Quote-anchor row is verbatim-present in the patent.
The **non-quoted** half — the descriptive **labels** Phase 1 writes around the quotes (Layer-2
mechanism verbs, orientation words, figure part-nouns) — has **no equivalent check**, because those
labels are paraphrases, not quote spans. Two such labels drifted from their cited paragraph in
Phase 1 this run, survived every inner-loop pass that inherits the design bundle, and had to be
fixed **at source mid-loop** when Phase 3 caught them:

| # | Phase-1 artifact | Label written | Cited paragraph actually says | Caught |
|---|---|---|---|---|
| r1-F3 | `invention-summary.md` Layer-2 step 1 | "Assemble ... die **face-down** on a carrier" | [0060]: "assembling ... on a carrier with an adhesive or bond film" — no orientation | Phase-3 pass-3 (medium); grep of patent.md returns 0 hits for "face-down" |
| r2-F2 | `figure-rationale.md` | "either **solder balls** (526, 5A)" | [0048]: "ball pitch solder **pads** 526" | Phase-3 pass-3 (low); the invention-summary row had the correct noun, only figure-rationale drifted |

Both are checkable against the cited paragraph by anyone with the document; both are exactly the
kind of precision the design stage is supposed to lock. Because they are **not** quote spans,
`gate_quotes` was green throughout, and because the drift lived in the Phase-1 bundle, a naive
recompose would reintroduce it (the composer flagged both as fix-at-source, and the orchestrator
applied both upstream). Within-run recurrence = **2** (invention-summary + figure-rationale, i.e.
the class is not one careless word but a stage-level gap spanning two Phase-1 artifacts).

This is distinct from the quote-fabrication class (`gate_quotes` already owns that) and from
`paraphrase-accidental-drift` (a *compose* pass-3 class); here the drift is **born in Phase 1**,
so the owner and the fix are upstream of the composer.

## Proposed change (reference-edit — Phase-1 non-quote label discipline)

Add a **grounding-label precision** rule to the thesis-architect skill (invention-summary-schema
and the figure-rationale procedure). Proposed wording:

> **Non-quote label grounding.** Every descriptive label that names a *part*, *orientation*,
> *material*, or *action* and sits next to a `[dddd]` anchor — even when it is NOT a Quotable
> span — must be verified verbatim-consistent with that paragraph's actual wording before hand-off:
> - **Part-nouns** match the source noun ("solder **pads**" when [0048] says pads, never "solder
>   balls"; "solder **bumps**" when [0056] says bumps).
> - **No orientation/adjective the paragraph does not state** ("face-down" is barred if [0060] only
>   says "on a carrier"). If a figure implies an orientation the text does not state, label it as
>   figure-derived, not as the method step.
> - The check is the paraphrase counterpart of `gate_quotes`: it does not require verbatim quoting,
>   only that the *chosen words* do not assert more than, or differently from, the cited paragraph.

Add a one-line design-stage self-check to the thesis-architect SKILL hand-off gate:
"non-quote part/orientation/material labels spot-checked against their cited paragraph (the
non-quoted half of the grounding chain)." And add the attribution-table row:

| `phase1-nonquote-label-drift` | pass-3 / fix-at-source | 1 | design | thesis-architect invention-summary Layer-2 + figure-rationale non-quote label grounding | reference-edit |

## Why this lever (and why NOT gate-promotion)

- A **gate** cannot own this safely: the labels are free-text paraphrases, so a mechanical
  verbatim check would false-positive on every legitimate paraphrase (glosses, plain-English
  renderings). `gate_quotes` works *because* Quotable spans are declared verbatim; non-quote labels
  are not, by definition. The durable fix is a **Phase-1 discipline** (reference-edit), enforced by
  the design stage's own read, not a regex.
- The owner is **design**, not compose: both drifts originated in the Phase-1 bundle and were fixed
  at source; a compose-side rule would only catch the symptom in one draft and lose it on recompose.

## Regression expectation / promotion path

- No gate or fixture change (reference-edit only); `meta/regression.py` unaffected — run it to
  confirm no unrelated drift before a human applies.
- `watch`, not `recommended-apply`: 2 within-run instances (count 2 < RECUR_THRESHOLD 3), first
  appearance of this specific mechanism. A **second run** with a Phase-1 non-quote-label drift
  (invention-summary or figure-rationale) — or corroboration from the cousin `document-section-mislabel`
  class in etched-us20240378175-r2 collapsing into this class — promotes it to `recommended-apply`.
- Success criterion: next figure-heavy run, the design hand-off carries a non-quote-label spot-check
  note, and no part-noun / orientation label reaches Phase 3 needing a fix-at-source.
