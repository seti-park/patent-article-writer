# Q7 hook gate — 2 admitted patterns

Step 5. Q7 (hook accessibility) is a **hard gate**. Each thesis candidate must map to exactly one of the 2 admitted patterns. Otherwise reject.

v1 had 4 patterns. v2 drops `timing-anomaly` and `visual-contradiction` due to external-evidence cost — neither could be reliably anchored without expensive web research per essay, and pilot essays showed degraded hook quality when forced into those patterns.

## Q7 검증 질문

Thesis 의 entry point 가 도메인 사전지식 없는 청자에게도 작동하는가?

아래 2 패턴 중 어느 anchor 와 매핑되는가? 어느 것도 매핑 안 되면 thesis candidate 거부 (hard gate).

## Pattern 1 — `corporate-narrative-friction`

회사 또는 산업 차원의 narrative (M&A 발표, 전략 statement, 임원 발언, product launch claim) 와 patent evidence 사이의 friction 이 entry point.

**입력**: Step 2 context research 의 corporate-narrative coverage category + `invention-summary.md` §"청구항 분석" mechanism.

**Anchor format**:
```
"<corporate narrative event> vs <patent evidence> — <friction nature>"
```

**Anchor 예시**:
- "Tesla 의 '70ms 는 unprecedented' 발표 narrative vs Bosch airbag 10ms baseline — 산업 narrative friction"
- "SpaceX-xAI merger 발표 narrative 가 Tesla 를 exclusion 으로 명시 vs Tesla-SpaceX patent overlap — 회사 narrative friction"

**적용 essay 예시**: BP6 SpaceX merger 패턴, voice-canon `opening-corporate-event-spacex-xai-merger-exclusion`.

**판정 기준**: narrative event 가 specific (M&A, executive statement, product launch claim — 추상적 industry trend 아님), friction 이 binary (둘 중 하나가 부정확) 또는 measurable (수치 차이).

**Payload 조건 (attention budget)**: friction 의 **기술적 대상** — 그 아이디어가 무엇을 하고
무엇을 바꾸는지 — 가 lead ¶1 안에서 설명 가능해야 한다. Friction 이 registry 상태
(심사·거절·RCE·담보) 에만 걸려 있고 기술 내용이 ¶1 에 들어갈 수 없다면, 이 anchor 는 절차를
plot 으로 만드는 결함 훅이다 (class `procedure-overweight-lead`; doctrine
`_shared/references/reader-energy.md` §6 — status 는 술어, 발명이 주어).

## Pattern 2 — `technical-impossibility`

청자의 "이건 안 될 텐데" 의문이 entry point 가 되는 기술적 anomaly 또는 constraint.

**입력**: `invention-summary.md` §"청구항 분석 — 4-layer core mechanism" Layer 3 `why_novel` + 청자의 도메인 가정.

**Anchor format**:
```
"<청자의 reasonable objection> → patent 이 <어떻게 해결>"
```

**Anchor 예시**:
- "광자 input 으로 lithium plating 검출 — 청자의 'photon 으로 어떻게 internal short 를 보느냐' 의문이 entry"
- "Vision sensor 가 accelerometer 보다 빠르게 collision 감지 — 청자의 'optical 이 electrical 보다 어떻게 빠르냐' 의문이 entry"

**적용 essay 예시**: BP2 Photon In 패턴, voice-canon `inline-bold-thesis-anchor-photon-in-8bit-optimization`.

**판정 기준**: 청자의 의문이 reasonable (해당 domain 의 first-order 직관), patent 의 resolution 이 청구항 또는 명세서에 명시.

## 거부 사례

다음 경우 Q7 hard gate 실패 — 후보 거부.

### 사례 1: 두 패턴 어느 것도 매핑 안 됨

Thesis "Tesla improves battery yield" → 어떤 corporate narrative 와 friction 인지 명시 안 됨, 어떤 청자 의문이 entry 인지도 명시 안 됨. **거부**.

대응: 다음 중 하나로 회귀.
- Patent 의 다른 angle 에서 2 패턴 중 하나에 anchor 가능한 새 hook 찾기.
- Context research (Step 2) 재진입으로 외부 anchor 후보 추가 탐색.
- Thesis 자체 재설계 (다른 thesis_seed 로 출발).

### 사례 2: timing-anomaly 또는 visual-contradiction 만 매핑

v1 에서는 4 패턴 중 하나로 통과. v2 에서는 **거부** — 위 2 패턴 중 하나로 reframe 가능한지 점검.

대응:
- Timing-anomaly 후보를 corporate-narrative-friction 으로 reframe 가능한가? (예: "patent grant 가 발표보다 앞섬" → "발표 narrative 가 patent evidence 와 friction")
- Visual-contradiction 후보를 technical-impossibility 로 reframe 가능한가? (예: "외부 사진과 도면 contradiction" → "청자의 'X 가 보이지 않는다' 의문")
- Reframe 불가능 시 thesis 폐기.

## Spine 에 명시

선택된 hook pattern 을 `thesis-spine.md` 의 "Q7 hook pattern (hard gate)" 영역에 명시. Anchor 도 함께 기록.

```markdown
## Q7 hook pattern (hard gate)
- [x] `corporate-narrative-friction` — anchor: <narrative event + friction>
- [ ] `technical-impossibility`
```

## 왜 2 패턴만 남았는가

v1 운영 결과:

- `timing-anomaly` — external-event 검증 비용 높음. Patent 의 시점은 객관적이지만 "anomalous proximity" 판단은 industry-event coverage 가 필요. 매 essay 마다 6-10 회 web search 동원. v2 의 working-hours budget 에 fit 안 됨.
- `visual-contradiction` — 외부 사진 / product image 확보 어려움. User 가 매번 추가 자료 제공해야 함. 자동화 어려움.
- `corporate-narrative-friction` — narrative event 가 patent metadata (filing/publication) 와 동시 수집 가능. Context research 1-2 회로 충분.
- `technical-impossibility` — patent 자체에서 derive 가능. 외부 evidence 최소.

v2 는 후 두 패턴에 한정. Pilot essay 결과 voice fidelity 가 5% 이내 유지.
