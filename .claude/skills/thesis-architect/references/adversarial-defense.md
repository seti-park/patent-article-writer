# Adversarial defense (Step 6)

For each thesis candidate that survived 4-axis grounding (Step 4) and the Q7 hook gate (Step 5), surface the strongest objection and draft a mitigation. Output goes to `thesis-spine.md` §"Adversarial defense".

## 원칙

가장 strict 한 reader (편집장, 경쟁 분석가, 회의적 투자자) 의 시각에서 thesis 를 공격. Steelman 의 반대 — weak-man 회피.

**Generic-truism ban.** "특허는 양산/제품/주가 상승을 보장하지 않는다" 류의 category-level
truism 은 steelman 이 아니라 weak-man 이다 — 어떤 특허 에세이에도 똑같이 적용되므로 THIS
thesis 에 대한 objection 이 아니다. Strongest objection 은 반드시 이 특허의 청구항 텍스트,
이 baseline, 이 thesis 의 인과 구조를 특정해서 공격해야 한다. Generic truism 을 objection
으로 채택하면 mitigation 이 자동으로 generic hedge ("보장하지 않지만 지켜볼 만하다") 로
수렴하고, 결론부가 safe-harbor boilerplate 로 무너진다 (pass-6 6G / gate_hedge 가 이를
잡지만, 근본 원인은 여기서 차단). Category-level 한계는 limits section 이 1회 다루는
소재이지, adversarial defense 의 산출물이 아니다.

3 layer:

1. **Strongest objection** — 어느 reader 가 가장 강하게 제기할 challenge.
2. **Mitigation** — essay 가 어떻게 그 challenge 를 disarm 하는가. 본문의 어느 영역에서.
3. **Residual risk** — mitigation 적용 후에도 남는 weakness. 명시 (acknowledged) 또는 acceptance (post-hoc 검증 가능).

## Priority inputs

Beyond patent text itself, the following are highest-value sources for objection surfacing:

1. **Context research's layer-confusion findings** — when an informed reader can distinguish patent's contribution level from broader/narrower claims (e.g., "patent claims X at layer A, but industry's well-known result is at layer A' — informed reader expects this distinction but thesis collapses them"), this is an immediate-dismissal risk. Surface these as **Category 1 (Claim scope)** objections first.
2. **Industry baseline references** with explicit numeric data — these enable **Category 2 (Baseline)** objections.
3. **Prior-art citations within patent's own text** — these reveal what the patent acknowledges as alternative explanations (**Category 4**).

Origin: phase1-retrospective.md Insight 5-2 — context research 의 layer-confusion 발견이 informed reader 의 thesis dismissal 의 가장 강한 source. 이 priority 가 의식되지 않으면 weak-man objections 만 surface 하고 진짜 reader risk 가 catch 안 됨.

## Step-by-step

### A. Objection surfacing

각 thesis candidate 에 대해 4 카테고리 challenge 를 시도. 가장 강한 것 선정.

#### Category 1: Claim scope challenge

"Patent 의 claim scope 가 thesis 가 주장하는 mechanism 을 cover 안 한다"

Source: `invention-summary.md` §"청구항 분석" + Layer 3 `why_novel.relative_to_prior_art`.

판정: 청구항 limitation 중 thesis 가 의존하는 element 가 명시되어 있는가. Embodiment-only 인가.

#### Category 2: Baseline challenge

"Thesis 가 비교하는 baseline 이 잘못 선정되었거나 outdated 다"

Source: Step 2 context research + `references/4-axis-grounding.md` Axis 4 anchor.

판정: Industry baseline 의 정확성, 시점, attribution. Apples-to-apples 비교인가.

#### Category 3: Correlation vs causation

"Patent evidence 가 thesis 의 causal claim 을 지지하지 않는다 — correlation 만"

Source: Patent text 의 명시 인과 vs thesis 의 인과 주장.

판정: Patent 이 "X causes Y" 명시하는가, 아니면 "X is associated with Y" 인가. Thesis 가 후자를 전자로 격상하는가.

#### Category 4: Alternative explanation

"Patent evidence 가 다른 thesis 로도 설명 가능하다"

Source: `invention-summary.md` §"청구항 분석" Layer 4 `innovation_angles` — 같은 evidence 를 anchor 하는 다른 angle.

판정: 선택된 thesis 가 evidence 의 유일한 reading 인가, 가장 strong 한 reading 인가.

### B. Mitigation drafting

선정된 objection 에 대해 essay 의 어느 영역이 disarm 하는지 명시.

Format:
```
**Mitigation**: <how>. <Where in essay>.
```

예시:
- "Mitigation: §3 explicitly cites both baselines (Bosch 10ms accelerometer vs Tesla 70ms vision-path) and shows the comparison is apples-to-apples — both are pre-deployment decision latencies."
- "Mitigation: §2 quotes 청구항 1 의 (b) limitation verbatim, where the vision sensor is explicitly part of the airbag controller's decision path — not an optional accelerator."

Mitigation 이 명시 안 되면 thesis disqualification 위험. Thesis 가 weak 한 신호.

### C. Residual risk acknowledgement

Mitigation 적용 후에도 남는 weakness 명시. Residual risk 는 **결론의 강도를 낮추는 장치가
아니라 결론의 신뢰를 사는 장치**다: `Acknowledged` 는 limits section 에 1회 명시로 소비되고,
verdict 는 spine 의 `closing_posture` (verdict edition 은 firm 이 default) 를 따른다.
`Acknowledged` 라는 이유로 open-question closing 을 고르지 않는다 (pass-6 6B firm-closing
override 참조). 3 옵션:

1. **None** — patent text 가 strict, thesis 가 완전 anchored. 최선.
2. **Acknowledged** — essay 본문에서 "본 분석은 X 가정에 기반한다" 명시. Reader 가 가정을 보고 disagree 할 수 있음.
3. **Acceptance** — post-hoc 검증 가능. "다음 patent filing 또는 product launch 가 thesis 를 yes/no 로 falsify"

예시:
- "Residual risk: none — patent text quantitatively grounded."
- "Residual risk: Acknowledged — Bosch's 10ms baseline assumes 2020-era accelerometer; modern (2025+) accelerometers may be faster. Essay §4 notes this and bounds the claim accordingly."
- "Residual risk: Acceptance — thesis predicts Tesla will publish a continuation in 2026 H2 with explicit 70ms benchmark. Falsifiable."

### D. Steelman beat — carry into Compose

The strongest objection + its mitigation is not just a thesis-survival check; it is a **beat
the essay must draft.** Carry it into `phase2-handoff-notes` as a **concede-and-return**
instruction so Compose allocates a section beat that concedes the objection **once, compactly,
and specifically**, then **returns to the affirmative core** — never leaving the strongest
pro-subject counter for the reader to raise.

**Concede is not elaborate (the two-sided steelman rule).** The beat must be specific — but
specific is not the same as long. Two failure modes are symmetric:

- `steelman-absent` — the concession is missing or a generic truism (below).
- `steelman-overweight` — the concession is present, specific, and correct but **over-spends
  the reader's attention on the objection**: it elaborates the counter past the point of
  conceding it, restates a caveat an earlier section already made, or narrates spend/procedure
  inside the beat. The cost is cognitive: **elaborating an objection primes the objection**
  (the negation / framing effect — "don't think of an elephant"), so the reader leaves carrying
  the counter, not the invention the concession exists to defend.

So the carried spec sets a **ratio, not a length**: the affirmative core (what survives the
concession) carries **at least as much attention** as the concession, and the concession is
**net-new** — it may not re-spend a caveat the spine already places in an earlier section
(those are spent once, where they first land). "Lean" here means *specific-but-bounded-and-
net-new*, never brief-and-vague. A long beat is fine if the core out-weighs the counter.

The steelman beat inherits the **generic-truism ban**: it concedes the strongest
THIS-patent objection (claim scope, baseline, causal structure), never the generic
"patents don't guarantee products" truism. Editorial pass-7 check 3 judges the steelman by
both rules — a truism steelman is `steelman-absent`; a counter that out-weighs its own
rebuttal (or re-spends a prior caveat, or carries a spend/procedure motif) is
`steelman-overweight`. Symmetric with the 6G over-hedge ↔ overreach verdict defense, and with
the attention-budget doctrine (`_shared/references/reader-energy.md` §6). Mechanical warn:
`gate_surface` SURF-007.

Run 045 gap: the strongest counter — "isn't claiming the broad workflow the smart, strong
move?" — was a Category-1/4 objection (the patent's breadth read as a strength, not a weakness)
that survived to publication unrebutted, until hand-revision added "the workflow claim is a
strong fence, and a fence is not an engine." Class `steelman-absent`; checked by editorial
pass-4 / pass-7; allocated by `section-blueprint.md`'s steelman beat.

## Output schema (thesis-spine.md)

```markdown
## Adversarial defense

**Strongest objection**: <one-sentence challenge from a critical reader>

**Mitigation**: <how the essay disarms it + where in the essay>

**Residual risk**: none | Acknowledged: <what gets noted> | Acceptance: <falsifier event>

**Steelman beat**: <the section that concedes the strongest counter compactly and specifically, then returns to the affirmative core which carries >= the concession's attention; net-new (no re-spent prior caveat), no spend/procedure motif in the beat — carried into phase2-handoff-notes as a concede-and-return ratio, not a length>
```

## 실패 사례

### 사례 1: Mitigation 부재

Thesis: "Tesla CAM 공정이 industry-first 다"

Objection: "BASF 가 2019 년에 유사 공정 publish 했다 — industry-first 아니다"

Mitigation 시도: ... (essay 본문에서 다루지 않음)

**판정**: Mitigation 없음 → thesis disqualification. 후보 reframe 필요. "Tesla CAM 공정이 industry-first" → "Tesla CAM patent 가 BASF approach 를 dry-electrode 와 결합한 첫 case" (다른 angle 로 reframe + BASF 차이 명시).

### 사례 2: Mitigation 이 본문에 안 들어감

Mitigation 으로 "§3 에서 baseline 비교 명시" 라고 적었지만 essay 본문에는 baseline 비교 영역이 spine 에 없음.

**판정**: Spine→section trace 와 mitigation 의 inconsistency. Spine 에 baseline 비교 section 추가 또는 mitigation 변경 (다른 section 으로).

### 사례 3: Residual risk 누락

"Residual risk: none" 으로 명시했지만 실제로는 acknowledged 영역 (e.g., baseline 시점 가정).

**판정**: Reader 가 가정을 보지 못함 → essay 의 trustworthiness 손상. Acknowledged 로 격상 + essay 본문에 1-line 가정 명시 의무.
