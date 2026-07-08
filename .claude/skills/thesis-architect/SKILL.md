---
name: thesis-architect
description: "Produces the Phase 1 Design handoff bundle (invention-summary.md, owner-briefing.md (Korean), thesis-spine.md, title-lead-candidates.md, fact-check-log.md, figure-selection.md, figure-rationale.md) from a user-supplied patent.md plus cleaned figure assets. Performs 4-axis thesis grounding, Q7 hook-accessibility gate (2 patterns only), adversarial defense, single-spine selection, energy-register title-lead candidates. Output is Markdown, not YAML. Use when user provides patent text + cleaned figures and asks for thesis design, invention analysis, essay outline planning, or Phase 1 Design output. NOT for: prose composition (Phase 2 essay-en-composer), voice work (Phase 2 voice-canon-lookup), editorial review (Phase 3 editorial-review), promo digest (Phase 4 promo-composer)."
context: fork
agent: design-architect
---

# thesis-architect

Phase 1 Design's primary inferential stage. Reads a patent + cleaned figures and produces the `handoff/01-design/` bundle that Phase 2 Compose executes against.

```
patent.md + figures/ + context research
    → invention-summary.md   (structured patent analysis with Quotable spans)
    → owner-briefing.md      (Korean owner comprehension transfer, Step 2b)
    → thesis candidates (2-4) → 4-axis grounding → Q7 hook gate → adversarial defense
    → thesis-spine.md         (locked single-spine + 4-axis anchors + Q7 + defense)
    → title-lead-candidates.md (5 title+lead pairs, one per energy register + recommended)
    → figure-selection.md     (figure ↔ thesis-point mapping)
    → figure-rationale.md     (per-figure purpose + intended effect)
    → fact-check-log.md       (external-fact seed)
```

## When to invoke

User supplies `patent.md` and a cleaned `figures/` directory (output of Layer 1 `patent-figures-clean`) and asks for thesis design, invention analysis, essay outline planning, or Phase 1 Design output. Entry point for Phase 1 — no upstream skill within Phase 1.

## Process

1. **Invention summary extraction** — read patent.md, write `invention-summary.md` per `references/invention-summary-schema.md`. Includes `**Quotable spans:**` `[xxxx]` blocks (verbatim, no paraphrase). Phase 2 reads these directly without re-touching patent.md.
2. **Context research** — web-search for industry baseline, corporate narratives, prior product launches. Log every query to `search-log.md`. **Each significant finding classified for framing-impact (main thread / paragraph / footnote) at discovery time** — SETI quick decision before Step 3 candidate generation. Output feeds the baseline-difference axis. See `references/context-research.md`.

   **Step 2b - Owner briefing (comprehension gate).** Before any thesis work, write
   `handoff/01-design/owner-briefing.md` in KOREAN per
   `_shared/references/owner-briefing-schema.md` (header block + 한 줄 요약 + sections ①-⑦ +
   the schema's embedded register). Rationale: the publisher must understand the patent before
   the pipeline starts angling it; comprehension precedes thesis. Placement: after Step 2 so
   section ⑤ (프로모션 연결) can use the researched external context (and
   `input/essay-context.md`, if present). Sections ①-④ each end with a `**근거 (verbatim):**`
   block of Quotable-span-format lines; every span must be verbatim from patent.md (the
   orchestrator runs `gate_quotes` on the briefing at the Phase-1 early gate). Full schema →
   `handoff-template/01-design/owner-briefing.md`.
3. **Thesis candidate generation** — 2-4 candidates, single-spine default. Each candidate carries draft 4-axis grounding. Write `thesis-candidates.md` capturing each candidate's frame + 4-axis status + rejection reason (for rejected ones). See `references/thesis-candidate-presentation.md`.
4. **4-axis grounding lock** — for each candidate, fill all 4 axes (claims / problem / effect / baseline-difference). Any missing axis disqualifies the candidate. See `references/4-axis-grounding.md`.
5. **Q7 hook gate (hard)** — each surviving candidate must map to exactly one of 2 admitted hook patterns. Otherwise reject. See `references/hook-patterns.md`.
6. **Adversarial defense** — surface the strongest objection per surviving candidate, draft mitigation. Context research's **layer-confusion findings** are priority inputs for Category 1 objections. See `references/adversarial-defense.md`.
7. **Spine selection (orchestrated)**: single-spine default; the orchestrator auto-selects the recommended candidate and surfaces the pick in one line for owner override (owner authority lives at surfaced decision points). Multi-spine requires explicit override per `references/single-spine-default.md`.
8. **Spine lock** — write `thesis-spine.md` with locked candidate's 4-axis anchors, Q7 pattern, adversarial defense, spine→section trace, and a **closing posture declaration**: `closing_posture: firm` is the DEFAULT for verdict/investor/analysis editions (the essay's job is to land a call; the limits section bounds it). Only declare `closing_posture: open` when the thesis itself is a genuinely open question the essay does not adjudicate — and record why. Under `firm`, an `Acknowledged` residual risk maps to `closing-forward-watching-event` or `closing-binary-test`, never `closing-open-question` (see `editorial-review/references/posture-lens.md` and pass-6 6G). **Attention budget (hard, in the trace):** tag every spine→section trace row with `payload: tech | pricing | frame`; at most ONE section carries `payload: pricing`, and prosecution/finance beats may otherwise appear only as one lead clause and the closing recap. **Verdict frame ≠ narrative frame:** when the edition contract defines the verdict by the document's TREATMENT (collateral, continued prosecution — e.g. pending-application editions), the one-line spine's SUBJECT stays the invention and treatment stays predicate; a spine one-liner or Q7 anchor whose plot is the paperwork is a defective lock (class `procedure-overweight-lead`; doctrine `_shared/references/reader-energy.md` §6).

   **Step 8b — Title-lead candidates (energy registers).** After the spine locks, write `handoff/01-design/title-lead-candidates.md`: FIVE title + lead-paragraph pairs, one per energy register (discovery / tension / contrarian / insider / stakes — definitions in `_shared/references/reader-energy.md`), ALL riding the locked spine's facts (a register changes delivery order and polarity, never the evidence). Each pair carries: (a) a title line ≤ 70 characters; (b) a 2-4 sentence lead-¶1 sketch that opens on that register's beat, with no verdict-insurance fact (status label, lien, rejection) ahead of the beat; (c) a one-line rationale tied to the `reader_sentence` from `input/essay-context.md` — if that field is absent, draft one at the top of the file for the orchestrator to confirm. The file ends with a `recommended: <register>` line plus a one-sentence why. The orchestrator surfaces all five; the selected pair travels to Phase 2. Full schema → `handoff-template/01-design/title-lead-candidates.md`.
9. **Figure mapping** — write `figure-selection.md` and `figure-rationale.md`. Each figure maps to a thesis point + caption_role. **Paired-figure relationships** (same-page / sub-figure / before-after sequence) reviewed explicitly — pull from `invention-summary.md` §"Figure relationships". Additionally: (a) tag one **cover candidate** for the 5:2 header, judged on visual force + whether it depicts the claimed core step — do NOT drop a sequence that depicts the claimed step purely for economy; (b) for a progressive sequence whose spec enumerates phases, take keyframes one-per-phase from the §"Figure relationships" Phase map (cite the enumerating paragraph), never by visual spacing.
10. **Fact-check log seed** — write `fact-check-log.md` listing every external (non-patent) fact the spine relies on, with source URL.
11. **Phase 2 handoff notes** — write `phase2-handoff-notes.md` capturing: (a) Phase 1 의 audience reframe 결정 (if any) (b) 인용 priority 매핑 (어느 Quotable span 이 essay 의 어느 section 에 우선 사용) (c) framing decision 의 trace (rejected candidates 의 핵심 사유) (d) Phase 2 가 우회해야 할 함정 — including, for every claim the spine cites, a claim-scope trap restating the invention-summary Claim scope map (locked vs open vs pinned) in do/don't form; trap wording itself must honor the map's vocabulary (never call a pinned point a "floor", never present description-preferred ordering/protocol as claim-locked); PLUS, whenever the edition brief budgets a topic (e.g. "prosecution status: exactly ONE label sentence"), an **attention-budget trap** restating the budget as a MOTIF budget (paraphrase echoes — keeps-paying / expensive-to-keep-alive variants — count against it) and naming the single `payload: pricing` section where the material lives (e) open questions for Phase 2 (SETI 결정 대기 항목).

## Pre/post conditions

Pre:
- `patent.md` uploaded to Phase 1 Project Knowledge.
- `figures/fig-NN.png` uploaded (output of Layer 1).
- `input/essay-context.md` (optional) read for per-run overrides, incl. the `reader_sentence:` leaving-sentence — Step 8b's design target (see `_shared/references/reader-profile.md`).
- Voice fencing enforced by Phase 1 PI — NO voice-profile or voice-canon access in this phase. (`_shared/references/reader-energy.md` is required reading for Step 8b — it is energy doctrine, not voice canon.)

Post:
- `handoff/01-design/invention-summary.md` exists; every patent-text claim has a paragraph anchor; every Quotable span is verbatim.
- `handoff/01-design/owner-briefing.md` exists (Step 2b): Korean per `_shared/references/owner-briefing-schema.md`; every `근거 (verbatim)` span line is verbatim-present in patent.md (gate_quotes-checkable).
- `handoff/01-design/thesis-spine.md` exists; selected candidate has all 4 axes anchored and Q7 hook pattern declared.
- `handoff/01-design/thesis-candidates.md` exists; all generated candidates documented (selected + rejected with rationale).
- `handoff/01-design/title-lead-candidates.md` exists; five register-keyed title+lead pairs (every title ≤ 70 chars, every lead sketch beat-first), rationales tied to the `reader_sentence`, and a `recommended:` line with a one-sentence why (Step 8b).
- `handoff/01-design/search-log.md` exists; every web-search query logged with URL + date + result snippet + used-in column.
- `handoff/01-design/figure-selection.md` + `figure-rationale.md` exist with every selected figure mapped to a thesis point; paired-figure relationships acknowledged.
- `handoff/01-design/fact-check-log.md` exists (may have zero entries if thesis is entirely patent-anchored).
- `handoff/01-design/phase2-handoff-notes.md` exists; Phase 2 entry instructions documented per Step 11.

## Output (short example — thesis-spine.md excerpt)

```markdown
# Thesis Spine

## Selected thesis

**One-line spine**:
> Tesla's RCM patent reveals an architectural decision made months before the public announcement that retroactively explains the 70-millisecond claim.

## 4-axis grounding

### Axis 1 — Claims anchor
> 청구항 1 의 (b) limitation — "the vision sensor providing pre-impact prediction to the airbag controller"

### Axis 2 — Problem anchor
> `[0014]` "기존 accelerometer-based systems respond after the collision begins"

### Axis 3 — Effect anchor
> `[0024]` "deployment decision is made approximately 70 milliseconds before traditional accelerometer-based systems would respond"

### Axis 4 — Baseline-difference anchor
> Bosch airbag baseline 10ms accelerometer latency vs claimed 70ms vision-path lead

## Q7 hook pattern (hard gate)
- [x] `corporate-narrative-friction` — anchor: Tesla公式발표가 patent grant 보다 11개월 후 → narrative friction

## Adversarial defense
**Strongest objection**: 70ms claim could refer to a different baseline than Bosch's 10ms accelerometer.
**Mitigation**: §3 explicitly cites both baselines and shows the comparison is apples-to-apples.
**Residual risk**: none — patent text quantitatively grounded.

## Single-spine declaration
- [x] Single-spine (default)

## Closing posture
closing_posture: firm  # verdict edition default; carried into the draft frontmatter for gate_hedge
```

Full schema → `handoff-template/01-design/thesis-spine.md`.

## Out of scope

- Prose composition — Phase 2 `essay-en-composer`.
- Voice canon work — Phase 2 `voice-canon-lookup`.
- Editorial review — Phase 3 `editorial-review`.
- Promo digest — Phase 4 `promo-composer`.
- YAML output — Phase 1 v2 emits Markdown only (handoff is human-edit-friendly).

## Feedback loop discipline

Forward-only step ordering is the default — but feedback loops are allowed when a later step surfaces a flaw in an earlier output. Examples observed in production:

- Step 2 context research finding may force re-extraction of Layer 4 innovation_angles in Step 1 invention-summary.
- Step 9 figure-mapping may force `thesis-spine.md` figure-dependence sections to update.
- Step 5 Q7 gate rejection may force return to Step 3 candidate generation.

When step N triggers a revision of step <N output, append a `> Revision note` block-quote at the end of the affected file (5-10 lines, format: `triggered by [step N] [date]: [what changed and why]`). This preserves audit trail.

If feedback loops cascade (>2 revisions of the same file), pause and ask SETI before continuing — likely a misalignment that needs explicit decision.

## References

- `references/invention-summary-schema.md` — fixed Markdown schema for `invention-summary.md` (metadata, 4-layer core mechanism, reference number table, figure relationships, quote anchor table, timeline, prior art, quantitative data).
- `references/quote-anchor-conventions.md` — `**Quotable spans:**` `[xxxx]` block format, verbatim discipline, when to split anchors.
- `_shared/references/owner-briefing-schema.md`: Step 2b contract for the Korean owner briefing (header + 한 줄 요약 + sections ①-⑦, gate-parseable `근거 (verbatim)` span format, embedded register since Phase 1 is voice-off).
- `references/context-research.md` — Step 2 web-search-first methodology, baseline-difference axis evidence sourcing.
- `references/4-axis-grounding.md` — Step 4 detail, anchor format per axis, disqualification rules.
- `references/hook-patterns.md` — Q7 hard gate, 2 admitted patterns (corporate-narrative-friction, technical-impossibility).
- `references/adversarial-defense.md` — Step 6 procedure, objection surfacing, mitigation drafting.
- `references/single-spine-default.md` — single-spine default, multi-spine override trigger keywords.
- `references/thesis-candidate-presentation.md` — Step 3 candidate format, comparison table, SETI selection.
- `_shared/references/reader-energy.md` — Step 8b required reading: the five energy registers, discovery-first lead pattern, feed-context rules (title ≤ 70 chars, first-two-lines test); the `reader_sentence` from `input/essay-context.md` is the design target.
