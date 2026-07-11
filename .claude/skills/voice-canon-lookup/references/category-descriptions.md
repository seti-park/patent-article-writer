# Voice canon category descriptions

Detailed definition + applicability for each of the 14 voice canon categories. Extracted from v1 voice-profile-seti SKILL.md.

## Opening 계열 (5)

### `opening-news-event`

뉴스 이벤트 → 대중의 각도 → 정당성 인정 → 전환.

예시 entries: `opening-news-event-tesla-terafab`, `opening-news-event-cybercab-production-timeline`, `opening-news-event-cloud-cascade`, `opening-news-event-genie-hassabis-quote`, `opening-news-event-spacex-xai-merger`.

용례: 시의성 news event (M&A 발표, 임원 quote, product launch) 를 lede 로 잡고 대중적 narrative 정당성 인정 후 patent evidence 로 전환.

### `opening-reader-experience`

독자 직접 체험 → 문제 본질 → 특허 등장.

예시 entries: `opening-reader-experience-llm-date`.

용례: 독자가 직접 체험할 만한 일상적 sit (LLM 에게 오늘 날짜 묻기 등) 으로 시작 → 문제 본질을 노출 → patent 가 해법 제시.

### `opening-industry-norm-reversal`

업계 표준 절차 명시 → 시간적 권위 (예: for decades) → 다른 방식 반전 한 문장.

예시 entries: `opening-industry-norm-reversal-xray-tesla`.

용례: 업계가 수십 년간 해 온 방식 명시 → 그 권위 인정 → patent 이 그 default 를 reverse.

### `opening-corporate-event`

회사 차원 narrative event (M&A 발표, 전략 statement, 임원 발언) 를 entry point 로 잡고 patent evidence 와의 friction 으로 진입.

예시 entries: `opening-corporate-event-spacex-xai-merger-exclusion`.

용례: Q7 hook pattern `corporate-narrative-friction` 의 voice 표현. Corporate narrative 와 patent evidence 의 friction.

### `opening-visual-anomaly`

사진·도면·도해 같은 visible artifact 의 contradiction 또는 anomaly 를 entry point. 독자가 시각적 위화감을 먼저 감지하고 그 정체를 patent 가 해명.

예시 entries: `opening-visual-anomaly-cybercab-taillight-photo-pair`.

용례: visual contradiction 으로 진입. v2 의 hook pattern 에서는 dropped 됐지만, voice canon 에 archived — 다른 essay 의 visual reference 에 활용 가능.

## Closing 계열 (4)

### `closing-aphoristic-landing`

구체적 기술 → 범위 확장 → 격언조 한두 문장. essay 끝 또는 section 끝 모두 가능. 🤔 는 essay 끝일 때 주로 등장.

예시 entries: `closing-aphoristic-landing-circuit-contract`, `closing-aphoristic-landing-paintshop-rewrote`, `closing-aphoristic-landing-redundancy-steady-state`, `closing-aphoristic-landing-architecture-harder-to-read`, `closing-aphoristic-landing-xray-signal`, `closing-aphoristic-landing-learning-vs-inference-asymmetry`, `closing-aphoristic-landing-pin-replacement-materials`, `closing-aphoristic-landing-corporate-story-vs-patents`.

용례: essay 의 가장 빈번한 closing 패턴. 본문의 구체적 mechanism 을 범위 확장한 한두 문장.

### `closing-open-question`

전망 제시 → 열린 질문형 → 🤔.

예시 entries: `closing-open-question-model-weights`, `closing-open-question-etherloop-ring-extension`, `closing-open-question-tesla-yield-rate`, `closing-open-question-genie-understanding-world`, `closing-open-question-finger-cable-next-essay`, `closing-open-question-chip-swarm-satellite-mesh`.

용례: essay 끝의 열린 질문형. Reader 가 thesis 의 다음 step 을 자체적으로 생각하도록.

### `closing-forward-watching-event`

다가올 특정 시점/event (filing date, product 출시, 외부 catalyst) 를 watching point 로 제시. Thesis 의 다음 verification 시점을 독자에게 명시.

예시 entries: `closing-forward-watching-event-etherloop-next-iteration`.

용례: Thesis 가 특정 event 로 verify 가능할 때. Reader 에게 monitoring point 제시.

### `closing-binary-test`

Thesis 의 참/거짓을 가를 binary 조건 제시. 미래 시점에 yes/no 로 갈리는 명시적 falsifier. 독자가 시간을 두고 thesis 를 검증할 수 있게 한다.

예시 entries: `closing-binary-test-spacex-tesla-ecosystem-realized`.

용례: Adversarial defense 의 "Residual risk: Acceptance" 와 정합. Binary falsifier 가 essay closing 의 anchor.

## Inline 계열 (1)

### `inline-bold-thesis-anchor`

단락 본문 안에 굵은 단문 1-2 줄로 thesis 의 핵심 주장을 anchor 시키는 device. 본문 흐름에 한 박자 멈춤을 만들고 thesis 의 도장 역할. 본문 어디든 등장 가능하나 통상 section 의 turning point 직후 배치.

예시 entries: `inline-bold-thesis-anchor-photon-in-8bit-optimization`, `inline-bold-thesis-anchor-etherloop-steady-state`, `inline-bold-thesis-anchor-taillight-hidden-skin`, `inline-bold-thesis-anchor-spacex-tesla-communication-hub`.

용례: thesis 의 핵심 주장을 본문 중간에 굵은 단문으로 anchor. Section 의 turning point 직후 배치.

## Signature phrase 계열 — 한국어 (4)

### `sig-ko-hypothesis-statement`

분석의 turning point 에서 Owner 의 관점 명시.

예시 entries: `sig-ko-hypothesis-statement-spacex-tesla-convergence`.

용례: 한글 essay 또는 wire 의 turning point 에서 Owner 관점 명시 phrasing.

### `sig-ko-core-claim`

단정 회피의 hedge.

예시 entries: `sig-ko-core-claim-optimus-implementation-reading`.

용례: 한글 essay 의 단정 회피 phrasing.

### `sig-ko-next-question`

Section 전환의 명시적 anchoring.

예시 entries: `sig-ko-next-question-genie-unlabeled-videos`.

용례: 한글 essay 의 section 전환 phrasing.

### `sig-ko-interesting-pivot`

분석 중 흥미로운 관찰로의 pivot.

예시 entries: `sig-ko-interesting-pivot-spacex-no-training`.

용례: 한글 essay 의 흥미로운 관찰 pivot phrasing.

## 적용 우선순위

Essay 구조에서:

- **Lead section** → opening 계열 중 하나 (5 카테고리)
- **Body section turning points** → inline-bold-thesis-anchor
- **Closing section** → closing 계열 중 하나 (4 카테고리)
- **Korean essay sections (한글 essay)** → sig-ko-* 계열 중 적절

본 우선순위는 essay-en-composer 의 section_blueprint 가 voice_canon_reference 선정 시 사용.

## Phase A 신규 5 범주 (2026-05-23 추가)

v1 운영 중 추가된 5 범주:

- `opening-corporate-event` — corporate-narrative-friction hook pattern 의 voice 표현
- `opening-visual-anomaly` — visual-contradiction hook pattern 의 voice (v2 에서 hook pattern 은 dropped, voice canon 만 보존)
- `inline-bold-thesis-anchor` — body section turning point 의 thesis anchor device
- `closing-forward-watching-event` — verification timepoint anchor
- `closing-binary-test` — explicit falsifier anchor

v2 에서는 모두 보존. 14 categories 전체가 active.
