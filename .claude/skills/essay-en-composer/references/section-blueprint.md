# Section blueprint (Step 3 of compose)

Adapted from v1 essay-architect Step 4. v2 input is `handoff/01-design/thesis-spine.md` (Markdown) instead of a Blueprint YAML. Output is the section structure the composer follows in Step 4.

## Section structure

For the locked single spine in `thesis-spine.md`:

- Typical structure: 4-7 sections (lead, context, architecture/mechanism, implication, closing — adjust per essay character).
- Section ordering follows thesis arc, NOT patent document structure.
- The spine→section trace in `thesis-spine.md` is the contract — every supporting point lands somewhere; no section advances claims outside the spine.

## Lead altitude, section headers, and balance (analytical / diligence mode)

For analytical or diligence essays (investor / technical-moat reads), three structural
defaults — learned from run 045's hand-revision (see
`meta/improvement-proposals/2026-06-26-human-revision-blindspots.md`):

- **Lead altitude (hook-first).** Paragraph 1 delivers the selected energy register's hook
  beat — the discovery fact, collision, inversion, privileged view, or stakes number from the
  chosen `title-lead-candidates.md` pair — as declarative prose, NOT a deferred question.
  Verdict-insurance facts (status labels, liens, rejections) never precede the beat; they
  price it afterwards. The full two-sided call still lands by the END of the lead section —
  hook-first reorders the lead, it does not defer the call past it. Claim-then-proof holds:
  the body substantiates a call already on the table by lead's end. See
  `_shared/references/reader-energy.md`. (A narrative-magazine piece may defer; pick per
  mode.) *(checked: editorial pass-6 6A/6H + pass-7 hook check; the "rest of this essay"
  framing is gated by `META-001`; mechanical warns: `SURF-002/004`.)*
- **Section headers are claims.** Each `##` header is an assertion, so a header-only skim
  reconstructs the argument (run 045: *workflow-not-robot → disclaims-the-hard-parts →
  territory-is-not-the-moat → moat-is-filed-elsewhere*). Avoid bare-label / "What X does"
  headers. *(checked: editorial pass-6 / pass-7 header-as-claim.)*
- **Steelman beat (concede-and-return, not elaborate).** When `thesis-spine.md` adversarial
  defense names a strong pro-subject counter, allocate a beat that concedes it **compactly and
  specifically, then returns to the affirmative core** (run 045: "the workflow claim is a strong
  fence, and a fence is not an engine"). Draft the concession once and the return-to-core with
  **at least as much weight** as the concession; do **not** re-spend a caveat an earlier section
  already made, and keep the spend/procedure lexicon **out** of the beat — elaborating the
  counter primes it (the "don't think of an elephant" effect) and reads as safe-harbor. Ratio,
  not length: a long beat is fine if the core out-weighs the counter. *(checked: pass-4 / pass-7
  `steelman-absent` ↔ `steelman-overweight`; mechanical warn `SURF-007`; doctrine
  `_shared/references/reader-energy.md` §6.)*
- **No stub sections.** Keep `word_target`s balanced; a section far shorter than its siblings
  should be merged or expanded. *(gate: `STUB-001` warn.)*
- **Attention budget (payload-first, procedure priced once).** Learned from
  etched-us20240378175-r2 v5 (class `procedure-overweight-lead`; doctrine:
  `_shared/references/reader-energy.md` §6). After the hook, the lead answers *what the
  invention does and what that changes* BEFORE *what it costs / where it stands*; status
  LABELS belong to the two-sided call and are fine, but process NARRATION (fee mechanics,
  RCE explainers, who-paid-when, lien walks) is not lead material — it lives in the single
  section the spine tags `payload: pricing`, plus at most one lead clause and the closing
  recap. **Motif budget:** when the edition brief budgets a topic ("exactly ONE label
  sentence"), paraphrase echoes of the same motif (keeps-paying / expensive-to-keep-alive
  variants) draw on the SAME budget; in revision mode, re-scan the whole draft for the
  motif before declaring a budget honored. Declared signature lines are exempt.
  *(checked: pass-6 6I; mechanical warns: `SURF-005/006`.)*

## Signature lines (≤ 3, declared)

Plan up to 3 **signature lines** — the aphoristic, repeatable sentences the reader carries
out (usually the `reader_sentence` or a close sibling; often one in the lead, one at the
closing landing). Declare their EXACT strings in `handoff/02-compose/thesis-trace.md` under
`## Signature lines` (write `none` if zero). Declared lines are protected surface per
`_shared/references/reader-energy.md`: echo/count rules exempt them; factual review (pass-3/4)
still applies in full.

Each section the composer plans has:

- `section_id` — kebab-case, unique (e.g. `1-lead`, `2-architecture`, `4-closing`).
- `header` — the section's `##` title, written as a *claim* (assertion), not a label; the set
  of headers should read as the argument skeleton (see above).
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

`thesis-spine.md` 의 `closing_posture` declaration + adversarial defense's residual risk together pre-commit the closing.

Under `closing_posture: firm` (the default for verdict/investor/analysis editions):

- If residual risk = `Acceptance` (binary falsifier) → use `closing-binary-test` voice pattern.
- If residual risk = `Acknowledged` → use `closing-forward-watching-event` or `closing-binary-test` — NOT `closing-open-question`. The acknowledgement was already spent in the limits section; the closing lands the call.
- If residual risk = `none` → use `closing-aphoristic-landing` or `closing-forward-watching-event`.

Under `closing_posture: open` (explicitly declared, with a recorded reason) the `Acknowledged` →
`closing-open-question` mapping is available.

**Verdict-section drafting discipline** (enforced by `gate_hedge` + editorial 6G):

- The call leads; bounds follow ("The verdict is yes. …" — never "a qualified yes").
- Exactly ONE anti-hype guard, specific to this patent — generic patent truisms ("a patent does
  not guarantee production / a rising stock price", "only time will tell") are banned in the
  verdict section; they belong (once) in the dedicated limits section.
- Limits are referenced from the verdict ("the boundaries set out above scope the moat"), never
  re-listed.

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
