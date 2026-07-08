# 4-axis thesis grounding (Step 4)

Each thesis candidate must anchor on all 4 axes. Any missing anchor disqualifies the candidate. Source: v1 essay-architect thesis-design.md §"4-axis grounding", carried over verbatim with multi-spine A-style deprecate language dropped (single-spine is the v2 default).

## 원칙

Thesis 는 인상적인 도면이나 특정 문구가 아니라 **청구항, 해결 과제, 발명 효과, 산업 베이스라인과의 차이** 의 4 anchor 종합으로 도출. 인상적 element 의 weight 가 위 4 anchor 보다 약하면 thesis 거부.

## Axis 1 — Claims anchor

**검증 질문**: Thesis 의 핵심 mechanism 이 청구항의 어느 element 또는 limitation 에 명시되어 있는가?

**Source 위치**: `invention-summary.md` §"청구항 분석 — 4-layer core mechanism" + `reference_number_table`. Independent claim 우선; 종속항도 가능.

**Anchor 명시 format**: `"청구항 N 의 (X) limitation — '...'"`

**실패 패턴**: Thesis 가 주장하는 mechanism 이 청구항에 명시 안 됨. 명세서의 embodiment 만 anchor 인 경우 청구항 범위 외이므로 thesis 의 strategic weight 약함.

## Axis 2 — Problem anchor

**검증 질문**: Thesis 가 가리키는 problem 이 명세서의 어느 paragraph 에서 기존 기술의 문제점으로 서술되는가?

**Source 위치**: `invention-summary.md` §"종래 문제 / 과제" Quotable spans + Quote anchor table entries with significance `mechanism-critical` or `prior-art-contrast`.

**Anchor 명시 format**: `"[XXXX] '기존 X 의 한계는 Y'"`

**실패 패턴**: Thesis 가 주장하는 problem 이 명세서 Background of the Invention 에 없거나, 명세서의 problem 보다 thesis 의 problem 이 더 큰 scope.

## Axis 3 — Effect anchor

**검증 질문**: Thesis 가 가리키는 advantage 가 명세서의 어느 paragraph 에서 발명의 유리한 효과로 서술되는가?

**Source 위치**: `invention-summary.md` §"유리한 효과 + 정량 데이터" Quotable spans + Quote anchor table entries with significance `quantitative` + Layer 3 `why_novel` synthesis.

**Anchor 명시 format**: `"[XXXX] '본 발명은 Z 효과'"`  또는  `"core_mechanism.why_novel: ..."`

**실패 패턴**: Thesis 가 주장하는 effect 가 명세서 Effects of the Invention 또는 embodiment 에 명시 없음. 추정 effect 만 의존.

## Axis 4 — Baseline-difference anchor

**검증 질문**: Thesis 가 가리키는 advantage 또는 distinctiveness 가 산업 베이스라인 또는 기존 narrative 와 어떤 차이로 구체화되는가?

**Source 위치**: Step 2 context research 결과 (industry baseline category) + `invention-summary.md` §"Prior-art references + differentiation" + Layer 3 `why_novel.industry_practice_contrast`.

**Anchor 명시 format**: `"Bosch airbag baseline 10ms vs claimed 70ms (industry-baseline-comparison)"`

**실패 패턴**: Thesis 가 "novel" 또는 "distinct" 주장하지만 산업 베이스라인 anchor 부재. Patent novelty 만으로는 baseline-difference 충족 안 됨 — 외부 baseline reference 필요.

## Disqualification rules

### Rule 1: 4-axis grounding 중 1 axis 라도 anchor 부재

→ 거부 또는 anchor 추가. Implicit assumption 으로 진행 금지.

예시 (거부): Thesis "Tesla's shift to vertical integration" 의 Effect anchor 부재 — 명세서에 "vertical integration" 효과 명시 없고 추정 effect 만. Thesis 축소 또는 anchor 확보 필요.

### Rule 2: 인상적 도면 또는 특정 문구에만 의존

→ 거부. Visual evidence weight 또는 catchy phrase weight 가 4 anchor 보다 약하면 thesis 부적합.

예시 (F4 archetype): Patent 의 FIG. 5 가 인상적 8-panel grid → thesis 가 "the eight-step process" framing. 그러나 FIG. 5 의 8 panels 가 청구항의 8 elements 와 매핑 안 됨 (panels 는 illustrative, 청구항은 3 main steps). 거부 후 "coarse particle uniformity through 3-step homogenization" 으로 재설계.

### Rule 3: 4-axis 모두 약한 anchor

→ 거부 또는 invention-summary 재추출 (Quotable spans 보강).

## Output schema (per candidate in thesis-spine.md draft)

```markdown
## Candidate <N>

**4-axis grounding**:
- Claims anchor: <청구항 + limitation>
- Problem anchor: <paragraph + quote>
- Effect anchor: <paragraph + quote 또는 why_novel synthesis>
- Baseline-difference anchor: <industry baseline + difference>
```

## 실패 사례

### 사례 1: 도면 집착 (Tesla CAM essay early draft)

초안 thesis: "The eight-panel patent figure shows Tesla's complete CAM manufacturing flow"

문제: FIG. 5 의 8 panels 가 illustrative. 청구항은 3 main steps 만 cover. 명세서의 해결 과제도 coarse particle homogenization 이지 complete flow 아님.

수정: "Tesla's CAM patent isolates 3 steps that homogenize coarse LiOH input" — 4-axis 모두 anchor 확보.

### 사례 2: Catchy phrase 의존

초안 thesis: "this is Tesla's 'just the beginning' patent" (Eggleston quote 인용)

문제: Eggleston quote 는 external context. 청구항, 해결 과제, 효과 의 patent text anchor 아님. Baseline-difference 도 부재.

수정: Eggleston quote 는 §1 lede 에만 사용. Thesis 는 patent text 의 4 anchor 로 재설계.

### 사례 3: Embodiment-only anchor

초안 thesis: "Tesla uses cobalt-free chemistry" (명세서 §5 embodiment 만 anchor)

문제: 청구항이 cobalt-free limitation 명시 없음 (embodiment 만). Patent 의 legal scope 가 cobalt 포함 가능.

수정: "Tesla discloses a cobalt-free embodiment of the manganese-rich cathode" — claim scope 정합 (embodiment 명시 + 청구항 범위 인정).
