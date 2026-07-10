# Execution Boundary (Plan ⊥ Execute)

Referenced by tech-essay-en SKILL.md. Defines exactly what tech-essay-en can and cannot do.

## Allowed actions

| Action | Note |
|--------|------|
| Use any fact in facts_locked | Primary source of factual content |
| Cite paragraph from quote_anchor_table | If patent-reader output is accessible |
| Apply voice_canon_reference pattern | Anchor prose on referenced examples |
| Compose lead, transitions, conclusion | Interstitial prose between facts |
| Add interpretive prose between facts | Stitch facts into narrative |
| Refine caption phrasing minor | Within caption_draft intent |
| Match structural_note intent | Each section's note guides expansion |
| Word target ±20% | Some flexibility on length |

## Forbidden actions

| Action | Reason |
|--------|--------|
| Use fact NOT in facts_locked | Violates Plan ⊥ Execute. Even if Claude knows the fact, only admitted entries valid. |
| Add new section | Section structure is locked by blueprint |
| Reorder sections | Section order is locked |
| Use voice canon entry not referenced in blueprint | Voice direction is locked |
| Change figure placement | Figure placement is locked |
| Substantial caption rewrite | Caption_draft can be refined for flow, not rewritten |
| Skip a section | Sections must be composed in order |
| Combine sections | Section boundaries are locked |
| Word target violation >20% | Substantial deviation requires blueprint revision |

## If forbidden action seems necessary

This means a blueprint gap is detected. Action:

1. Stop composition
2. Identify the gap specifically: "Section 3 needs fact about <X>, but facts_locked has only <Y>"
3. Return to user with specific gap
4. User decides:
   - Revise blueprint (return to essay-architect)
   - Abandon current attempt
   - Add admission round to fill gap

Never improvise to work around a gap. This is the central discipline of the plan-execute split.

## Why this discipline

When the execute stage allows "minor" deviation, the deviation accumulates into substantive change. Facts get reframed. Quotes drift. Voice shifts.

Plan ⊥ Execute boundary means: variance is localized to plan stage. Once blueprint locks, execution is mechanical expansion.

The cost is rigidity. The benefit is family-level reproducibility — the same blueprint produces the same draft family.

## Internal reasoning vs output

tech-essay-en's internal reasoning is not bound. Claude can think about facts outside `facts_locked`. But output cannot reference them.

This distinction matters: avoid using "I know X is also true" reasoning to introduce X into the draft. Even if X is correct, X is not in `facts_locked`, so X cannot enter the output.

## Quick reference

Before composing each sentence:
- Is this a factual claim? → Cite [^fact-id] from facts_locked
- Is the fact in facts_locked? → If no, stop. Gap detected.
- Is this transition/interpretation prose? → No citation needed, but no new facts either
- Am I matching the voice_canon_reference? → If drifting, re-read canon entries

Before composing each section:
- Section_id matches blueprint? ✓
- Word_target within ±20%? ✓
- voice_canon_reference applied? ✓
- All facts_used cited? ✓
- structural_note intent fulfilled? ✓

## Failure modes

Five recurring failure modes during composition. All resolve by stopping rather than improvising.

### FM1. Blueprint gap during composition

Composition reveals need for a fact not in `facts_locked`.

→ Stop. Return the specific gap to user. Do not improvise around it. See "If forbidden action seems necessary" above.

### FM2. Voice canon constraint too rigid

Referenced canon examples don't fit the section.

→ Stop. Return to essay-architect for revision (additional or different canon reference).

### FM3. Word target unachievable

Section cannot expand without padding, or cannot fit within ±20% without omitting required content.

→ Stop. Return for blueprint revision (adjust `word_target` or restructure section).

### FM4. Annotation overhead

Inline citations make prose feel academic.

→ Place markers at end-of-clause or end-of-sentence level. Treat annotations as subtle markers. Prose flow remains natural with markers as light touches rather than mid-sentence interruptions.

### FM5. Mode mismatch with essay needs

User selected strict-execution but Blueprint coverage is incomplete. Or user selected conservative posture but a thesis-altering catch emerges.

→ Surface the mismatch. Propose mode or posture shift per `mode-spec.md` mid-pipeline shift rules. Raise `OWNER_QUESTION` (orchestrator relays via Owner checkpoint protocol); Owner decides: shift mid-pipeline, abandon attempt, or return to design for blueprint revision.
