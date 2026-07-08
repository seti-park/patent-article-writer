# Audience adaptation

Essay → promo 의 독자 이동. Essay 독자는 curious retail investor
(`_shared/references/reader-profile.md`: advanced high school 에서 early undergraduate
사이의 기술 이해도, 회사/주식 때문에 열어본 사람). Promo 독자는 두 층이다:

- **EN thread**: X general public. 피드를 스크롤하다 마주친 사람. 팬, tech
  enthusiast, casual scroller 혼재.
- **KR post**: 발행자 자신의 한국어 팔로워 (아래 별도 절).

Trust-driven posture 를 잃지 않고 적응한다.

## Reader profile delta (EN deliverables)

| Dimension | Essay reader (reader-profile.md) | Promo reader (X feed) |
|---|---|---|
| Patent literacy | low-medium, 용어마다 one-clause gloss 를 받음 | low, gloss 예산 자체가 없음 |
| Domain context | 회사/주식 맥락을 갖고 열어봄 | mixed, 회사를 모를 수도 있음 |
| Attention | long-form 을 의도적으로 열었음 | 피드에서 스쳐 지나가는 중 |
| Trust signal 민감도 | high (puffery 를 버림) | high (X public 은 hype 를 즉시 감지) |

## What to expand

- **Technical jargon**: essay 는 용어 1 회 gloss 후 전제한다. Promo 는 기술 용어마다
  짧은 clarification 하나. 예: essay *"The vision-sensor latency feeds the predictive
  controller within the 70ms window."* → promo *"The vision sensor, a camera rather than
  the standard accelerometer, feeds the airbag controller about 70 milliseconds before
  the impact starts."* Clarification 의 내용도 essay 본문에 있어야 한다 (새 사실 금지).
- **단위**: 첫 사용에서 풀어 쓴다 ("milliseconds", "ms" 아님).

## What to compress

- **Claim mechanics**: essay 의 4-step walkthrough → promo 는 한 문장 요약 + walkthrough
  는 essay 에 위임. *"The mechanism is a four-step path from vision to deployment,
  summing to about 70 milliseconds."*
- **Adversarial defense**: essay 는 objection 을 세우고 무너뜨린다. Promo 는
  objection-mitigation 쌍을 나열하지 않고, 이미 방어된 thesis 로 제시한다. *"The 70ms
  gap sits against Bosch's 10ms accelerometer baseline, apples to apples."*
- **Filing/legal 시점 구분**: filed / published / granted 구분이 thesis 그 자체가 아닌
  한 "the patent published on [date]" 로 접는다. 단, 확실성 동사는 essay 와 일치
  (`fact-verification.md` hard rule 3: pending 을 granted 로 접지 않는다).

## What to drop entirely

- `[dddd]` paragraph anchors, reference numerals (414, 416 류): X 독자에게 쓸모없는
  시각 잡음. 도면을 첨부하지 않는 한 번호는 모두 제거.
- Section transitions ("Recall §2's mechanism...").
- 다른 essay 로의 cross-reference (companion essay 링크는 아티클 안에서 할 일).
- Methodology asides (분석을 어떻게 했는지).
- 내부 ID (fact ID, finding_id, voice canon entry ID).

## What to preserve as-is

- 모든 숫자 값 (단위는 풀어 쓰기).
- 회사명 표기 (같은 스펠링, 같은 casing).
- 특허번호 형식 (US 2024/0378175 A1).
- Quoted statements: essay 에서 verbatim, essay 는 patent 에서 verbatim. 압축 시
  Sub-rule 3 (`fact-verification.md`).
- 확실성 동사와 evidence 라벨 ("company-claimed", "the company's telling").

## KR post 독자 (한국어 피드)

- 발행자 계정의 팔로워: 이 계정의 특허 읽기를 보러 온 사람들. 회사 맥락은 EN 독자보다
  있는 편이지만 전제하지 않는다.
- **발행자 1인칭 허용**: essay 는 3인칭 분석문이지만 KR post 는 발행자가 자기 글을
  소개하는 말이다. "정리했습니다", "읽어봤습니다" 급의 건조한 소개가 자연스럽다. 절제:
  1인칭은 소개 동사에만, 판단 과시에는 안 쓴다.
- 한국어 독자도 hype 에 똑같이 민감하다. 과장 배제, 클릭베이트 의문형 금지, 건조한
  평서문 (`_shared/references/working-dialogue-voice.md` register).
- 영어 처리: 회사명, 특허번호, 부품번호, 영어 인용구는 원문 유지. 개념어는 한국어로
  풀되 essay 의 gloss 내용을 번역한다 (새 설명 발명 금지).

## Reader-test pass

작성 후, essay 를 본 적 없는 사람으로 각 deliverable 을 읽는다. 세 질문:

1. 이 patent 가 무엇에 관한 것인가?
2. 왜 중요한가?
3. 필자의 read 는 무엇인가?

어느 답이든 essay 가 있어야만 성립하면 self-contained finishability 실패. 압축하거나
재구성한다. Thread 는 tweet 단위로 같은 테스트를 적용한다.
