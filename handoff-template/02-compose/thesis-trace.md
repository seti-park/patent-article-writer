<!--
  TEMPLATE: handoff/02-compose/thesis-trace.md
  Produced by: essay-en-composer (Phase 2 Compose, Step 7)
  Schema sources: essay-en-composer/SKILL.md (thesis-trace.md output)
                  + references/section-blueprint.md (per-section internal plan fields)

  Externalizes the composer's internal Step-3 section plan so Phase 3 Edit Pass 4
  can check thesis-section alignment against thesis-spine.md's spine→section trace.

  Per section, record:
    - spine element carried (from thesis-spine.md)
    - voice_canon_reference (voice-canon-lookup entry_ids, >=1)
    - paragraph_anchors_used ([xxxx], from invention-summary Quotable spans)
    - external_facts_used (fact-check-log.md Fact IDs; [] if purely patent-anchored)
    - word_target / word_actual (composer writes within ±20% of target)

  Plus the selected title-lead register (from title-lead-candidates.md) and a
  `## Signature lines` section: 0-3 EXACT strings (`none` if zero) — protected surface
  per _shared/references/reader-energy.md (echo/count-exempt; factual review applies).

  Example content: Tesla RCM / 70ms patent (matches essay-draft.md).
-->

# Thesis Trace

## Spine source

- **Spine**: handoff/01-design/thesis-spine.md
- **One-line spine**: Tesla's RCM patent reveals an architectural decision made months before the public announcement that retroactively explains the 70-millisecond claim.
- **Q7 hook**: corporate-narrative-friction
- **Title-lead register**: discovery (handoff/01-design/title-lead-candidates.md, recommended pick)

## Section → spine mapping

### 1-lead — "When the Announcement Arrived Late"
- **Spine element carried**: Hook (announcement vs filing friction)
- **voice_canon_reference**: `opening-corporate-event-announcement-friction`
- **paragraph_anchors_used**: [] (framing only — no patent claim)
- **external_facts_used**: `tesla-safety-announcement-2026-03`, `tesla-rcm-filing-date`
- **word_target / word_actual**: 90 / 84

### 2-architecture — "What the Patent Actually Routes"
- **Spine element carried**: Axis 1 claims anchor + mechanism
- **voice_canon_reference**: `inline-bold-thesis-anchor`, `mechanism-walkthrough`
- **paragraph_anchors_used**: `[0016]`, `[0017]`
- **external_facts_used**: []
- **word_target / word_actual**: 110 / 103

### 3-baseline — "The Baseline the Number Hides"
- **Spine element carried**: Axis 4 baseline-difference + adversarial mitigation (apples-to-apples)
- **voice_canon_reference**: `baseline-comparison`
- **paragraph_anchors_used**: `[0014]`, `[0024]`
- **external_facts_used**: `bosch-ecu-10ms-2020`
- **word_target / word_actual**: 120 / 128

### 4-implication — "What the Filing Date Reframes"
- **Spine element carried**: Axis 3 effect anchor → strategic reframe (claim bounded)
- **voice_canon_reference**: `strategic-reframe`
- **paragraph_anchors_used**: `[0029]`
- **external_facts_used**: `tesla-rcm-filing-date`
- **word_target / word_actual**: 90 / 88

### 5-closing — "What the Number Was Always Going to Confirm"
- **Spine element carried**: thesis recap + forward pointer
- **voice_canon_reference**: `closing-forward-watching-event`
- **paragraph_anchors_used**: []
- **external_facts_used**: []
- **word_target / word_actual**: 70 / 66

## Signature lines

<!-- 0-3 EXACT strings ("none" if zero). Protected surface per
     _shared/references/reader-energy.md: pass-2 / pass-7 echo and count rules exempt
     them; pass-3/4 factual review still applies in full. -->
1. "The number the presentation celebrated had already been written down."
2. "The filing decides before the crash; the baseline decides during it."

## Coverage check

<!-- Confirms every spine element lands in exactly one section and no section
     advances a claim outside the spine (the section-blueprint contract). -->
- All 4 axes carried: Axis 1 → §2, Axis 2 (problem) → §3, Axis 3 → §4, Axis 4 → §3.
- No out-of-spine claims introduced.
- Every `[xxxx]` used traces to an invention-summary Quotable span / Quote anchor.
- Every external fact used traces to a fact-check-log Fact ID and appears in # Sources.
