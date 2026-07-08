<!--
  TEMPLATE: handoff/01-design/thesis-spine.md
  Produced by: thesis-architect (Phase 1 Design, Step 8 — spine lock)
  Schema sources: thesis-architect/SKILL.md "Output" example
                  + references/4-axis-grounding.md (Output schema)
                  + references/hook-patterns.md (Q7 hard gate)
                  + references/adversarial-defense.md (Output schema)

  This is the LOCKED single spine that Phase 2 Compose executes against. Phase 2
  rejects this handoff if the Q7 hook is not declared or if Quotable spans are
  missing for the spine anchors. Example content: Tesla RCM / 70ms patent.
-->

# Thesis Spine

## Selected thesis

<!-- One-line spine = the single sentence the whole essay defends. -->
**One-line spine**:
> Tesla's RCM patent reveals an architectural decision made months before the public announcement that retroactively explains the 70-millisecond claim.

## 4-axis grounding

<!-- All 4 axes MUST be anchored. A missing axis disqualifies the candidate
     (it should never reach the locked spine). Anchors trace to invention-summary.md. -->

### Axis 1 — Claims anchor
<!-- Format: "청구항 N 의 (X) limitation — '...'". Independent claim preferred. -->
> 청구항 1 의 (b) limitation — "the vision sensor providing pre-impact prediction to the airbag controller"

### Axis 2 — Problem anchor
<!-- Format: "[XXXX] '기존 X 의 한계는 Y'". Source: §종래 문제 Quotable spans. -->
> `[0014]` "conventional accelerometer-based systems respond only after the collision has begun"

### Axis 3 — Effect anchor
<!-- Format: "[XXXX] '본 발명은 Z 효과'" or "why_novel synthesis".
     Source: §유리한 효과 Quotable spans + quantitative significance entries. -->
> `[0024]` "deployment decision is made approximately 70 milliseconds before traditional accelerometer-based systems would respond"

### Axis 4 — Baseline-difference anchor
<!-- Format: "<industry baseline> vs <claimed> (<comparison type>)".
     Source: Step 2 context research + §Prior-art differentiation. Needs an
     EXTERNAL baseline — patent novelty alone does not satisfy this axis. -->
> Bosch airbag baseline ~10ms accelerometer latency vs claimed ~70ms vision-path lead (industry-baseline-comparison)

## Q7 hook pattern (hard gate)

<!-- Exactly ONE of the 2 admitted patterns must be checked, with its anchor.
     corporate-narrative-friction | technical-impossibility.
     If neither maps, the candidate is rejected at Step 5. -->
- [x] `corporate-narrative-friction` — anchor: Tesla 公식 safety 발표가 patent publication 보다 11개월 후 → narrative friction
- [ ] `technical-impossibility`

## Adversarial defense

<!-- 3 layers. Strongest objection from the strictest reader (steelman, not weak-man).
     Mitigation must name WHERE in the essay the objection is disarmed.
     Residual risk: none | Acknowledged: <noted assumption> | Acceptance: <falsifier>. -->
**Strongest objection**: The 70ms claim could be measured against a different baseline than Bosch's 10ms accelerometer, making the comparison apples-to-oranges.

**Mitigation**: §3 explicitly cites both baselines (Bosch ~10ms accelerometer vs Tesla ~70ms vision-path) and shows both are pre-deployment-decision latencies — an apples-to-apples comparison.

**Residual risk**: Acknowledged — Bosch's ~10ms baseline assumes a 2020-era accelerometer ECU; §3 notes this and bounds the claim accordingly.

**Steelman beat**: §3 concedes at full strength that the baseline could be read as outdated, then refines with the ECU-generation bound. <!-- THIS-patent objection only; the generic "patents don't guarantee products" truism is banned as a steelman (adversarial-defense.md). -->

## Closing posture

<!-- firm is the DEFAULT for verdict/investor/analysis editions. Under firm, an
     Acknowledged residual maps to closing-forward-watching-event or
     closing-binary-test, never closing-open-question (pass-6 6B override; 6G).
     The composer copies this into the draft frontmatter for gate_hedge. -->
closing_posture: firm

## Single-spine declaration

<!-- Single-spine is the v2 default. Multi-spine requires an explicit SETI override
     per references/single-spine-default.md. -->
- [x] Single-spine (default)
- [ ] Multi-spine (override — record SETI authorization)

## Spine → section trace

<!-- The contract Phase 2 follows: every supporting point lands in exactly one
     section; no section advances claims outside the spine. Section ids are
     planned by the composer (section-blueprint.md).
     payload tags (attention budget, reader-energy.md §6 / SKILL Step 8):
       tech    = the invention and its effects (the reader's payload)
       pricing = prosecution / finance / registry treatment (at most ONE section;
                 elsewhere only one lead clause + the closing recap)
       frame   = hook, verdict, recap framing
     Verdict frame ≠ narrative frame: even when the edition contract prices the
     document by its treatment, the spine's subject stays the invention. -->
| Section | payload | Spine element carried | Primary anchors |
|---|---|---|---|
| 1-lead | frame | Hook — corporate-narrative-friction (announcement vs filing); tech beat before status beat | (framing; no patent claim) |
| 2-architecture | tech | Axis 1 claims anchor + mechanism | `[0016]`, `[0017]` |
| 3-baseline | tech | Axis 4 baseline-difference + adversarial mitigation | `[0014]`, `[0024]` |
| 4-implication | tech | Axis 3 effect anchor → strategic reframe | `[0024]`, `[0029]` |
| 5-closing | frame | Thesis recap + forward pointer | (framing) |

<!--
  > Revision note — triggered by [step N] [date]: [what changed and why]
  (Append when Step 9 figure mapping or a feedback loop revises this file.)
-->
