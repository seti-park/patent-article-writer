# Section blueprint (Step 3 of compose)

Adapted from v1 essay-architect Step 4. v2 input is `handoff/01-design/thesis-spine.md` (Markdown) instead of a Blueprint YAML. Output is the section structure the composer follows in Step 4.

## Section structure

For the locked single spine in `thesis-spine.md`:

- Typical structure: 4-7 sections (lead, context, architecture/mechanism, implication, closing — adjust per essay character).
- Section ordering follows thesis arc, NOT patent document structure.
- The spine→section trace in `thesis-spine.md` is the contract — every supporting point lands somewhere; no section advances claims outside the spine.

## Per-section fields (composer's internal plan)

Each section the composer plans has:

- `section_id` — kebab-case, unique (e.g. `1-lead`, `2-architecture`, `4-closing`).
- `word_target` — integer. Composer writes within ±20%.
- `voice_canon_reference` — list of `voice-canon-lookup` entry_ids (at least 1).
- `paragraph_anchors_used` — list of `[XXXX]` patent paragraph anchors this section will cite, drawn from `invention-summary.md` Quotable spans + Quote anchor table.
- `external_facts_used` — list of `fact-check-log.md` Fact IDs this section will cite. Empty if section is purely patent-anchored.
- `structural_note` — brief intent statement (1-2 sentences).

## Patent-fact discipline

Every patent-text claim in the essay must trace to a `[XXXX]` anchor that exists in `invention-summary.md` Quotable spans or Quote anchor table. Patent text never sourced from patent.md directly (it's not in Phase 2 Knowledge).

Every external claim (industry baseline, corporate statement, prior product date) must trace to a `fact-check-log.md` Fact ID + appear in the essay's `# Sources` block.

A section's `paragraph_anchors_used: []` and `external_facts_used: []` is valid only if the section is pure transitional/connective prose (no patent claims, no dates, no descriptions, no named-entity claims).

### Failure case — Tesla CAM essay §5 (carry-over from v1)

Closing section initially planned with `external_facts_used: []` for narrative framing. Mid-write self-catch found 3 patent ID claims in the closing chain. Three Quotable span anchors had to be added retroactively. v2 lesson: plan paragraph_anchors_used + external_facts_used at Step 3, not Step 4.

## Closing directive (last section)

For the last section, plan a `closing_directive` to pre-commit closing framing before drafting. Without it, the composer iterates the closing 3-4 times trying to land it.

Fields:

- **forward_pointer** — observable next event or future condition (e.g., "the algorithm stays until the model can be trusted without it").
- **wider_framing** — analogy, industry pattern, broader framing.
- **thesis_recap** — one-sentence thesis crystallization.
- **anti_pattern** — defensive hedging to avoid (e.g., "no 'only X can confirm' / 'we cannot say'").

### Closing directive integrates with `thesis-spine.md`

`thesis-spine.md` 의 Closing posture (from voice-canon selection) + adversarial defense's residual risk together pre-commit the closing.

- If residual risk = `Acceptance` (binary falsifier) → use `closing-binary-test` voice pattern.
- If residual risk = `Acknowledged` → use `closing-open-question` or `closing-aphoristic-landing`.
- If residual risk = `none` → use `closing-aphoristic-landing` or `closing-forward-watching-event`.

## Sources structure plan

Plan the essay's `# Sources` block upfront. v2 enum (5 categories): Patents / Papers / Official statements / News & media / Technical specs.

Fields:

- **expected_count** — total entries expected.
- **category_distribution** — per-category counts.
- **subgrouping_decision** — `flat` or `subgrouped`. Rule: 4+ entries AND 2+ categories → subgrouped. Subgrouping is all-or-nothing — if any category appears, every source must be categorized.
- **rationale** — one-line reasoning.

Example plan:
```
expected_count: 6
category_distribution:
  Patents: 3
  Papers: 2
  News & media: 1
subgrouping_decision: subgrouped
rationale: 3 categories, 6 entries → subgrouped
```

This plan guides Step 4 writing. Phase 3 Edit Pass 6 verifies the final block matches.

## Mode hint (optional)

The composer's Step 0 (mode selection) defaults to walkthrough + measured (see `references/mode-spec.md`). The section blueprint may include a mode hint based on essay characteristics:

| Essay characteristic | suggested_mode | suggested_posture |
|---|---|---|
| New domain / unprecedented thesis | walkthrough | aggressive |
| Standard domain / well-trodden thesis | walkthrough | measured (default) |
| Time-constrained / wire-style (rapid) | strict-execution | measured |
| Voice canon experimentation | pair | aggressive |
| Adversarial reader concern / strategic essay | walkthrough | conservative |
| Patent-heavy / factual density high | walkthrough | conservative |

The hint is overrideable by SETI invocation. Priority: invocation > hint > default.

## Section ordering pattern (default)

Standard arc:

1. **Lead** — news event or patent entry, thesis trigger (uses opening voice canon).
2. **Context / Architecture** — patent mechanism + industry baseline.
3. **Implication** — strategic implication of the patent evidence.
4. **Closing** — forward_pointer + wider_framing + thesis_recap (uses closing voice canon).

Adjust per essay character. Multi-spine essays (override required) may have sub-sections per thread.

## Output of Step 3 (input for Step 4)

A composer-internal plan listing each section with the fields above. The plan is not written to a separate file — it's the composer's working memory before drafting. The output of Step 4 (drafting) is `handoff/02-compose/essay-draft.md`. The plan can be traced in `handoff/02-compose/thesis-trace.md`.

## Next step

Step 4 — figure planning per `references/figure-rendering.md`. Then Step 5 — compose sections in order applying mode-spec rules from `references/mode-spec.md`.
