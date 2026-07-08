# Fact Verification: Promo 의 정확성 정책

Promo 는 essay 와 같은 hedge 강도에서 작성되므로 unverified fact 노출 시 fact-check 위험이 크다. Essay 에서 verify 된 fact 만 promo 에 사용한다.

## 검증 절차

Promo 후보 sentence 별로 다음 절차 적용.

1. Essay 본문 cross-check. 모든 사실 진술이 essay v[X] FINAL 의 명시 sentence 에 매핑되는가
2. Essay 에 없는 fact 는 web search verify 또는 삭제
3. Essay 의 LLM-gen fact verification flag (essay 의 `causal-reasoning` 영역) carry-over 항목 확인

추가 3 sub-rules 를 시점 표현과 quote 압축에 적용. 일반적으로 essay §1 의 timing puzzle 표현을 그대로 promo 에 carry-over 하는 것이 가장 안전.

## Sub-rule 1: 시점 관계 자율 합성 금지

Promo 가 essay 본문에 없는 시점 sequence 표현 (before / after / during / N days 간격) 을 만들 때 다음 두 가지를 모두 verify.

- 두 시점이 essay 본문에 명시되어 있는가
- 그 두 시점 사이의 sequence relationship 이 essay 에 명시되어 있는가

둘 다 YES 면 OK. 둘 중 하나라도 NO 면 web search verify 또는 시점 표현 삭제.

### 실패 사례 1 (Tesla dry 4680 promo, 2026-05)

초안에서 *"emerged the week before Cybercab pilot production began"* 작성. 실제는 patents 가 Cybercab production 발표 after 공개됨. Sequence 역방향 자율 합성. 사용자 catch.

## Sub-rule 2: 평행 구조 위험

Promo 가 두 시점 사이 간격을 표현할 때, 다른 시점 표현과 평행 구조 (예: "seven days apart + seven days after") 만들고 싶은 충동을 의식적으로 차단. 평행성 < 정확성. 캘린더 일자 직접 계산해서 verify.

### 해결 표현 패턴

- 정확한 일수 직접: *"eight days after"*
- 자연스러운 영어 idiom: *"just over a week after"*
- 시점 명시 + 함축: *"emerged on April 30, just over a week after Q1 earnings"*

### 실패 사례 2 (Tesla dry 4680 promo, 2026-05)

*"filed seven days apart in October 2024... emerged seven days after Tesla's Q1 2026 earnings call"*. Q1 call 4/22 → patents 4/30 = 정확히 8 일. 평행 구조 만들기 위해 *"seven days after"* 로 잘못 합성. 사용자 catch.

## Sub-rule 3: Quote 압축 시 anchor preservation

Promo 가 essay quote 또는 짧은 표현을 압축 carry-over 할 때, essay 안에서 자연 anchor 되는 비교 baseline / referent 가 promo 본문만으로 finishable 한지 verify.

### 검증 절차

Promo 의 각 quoted phrase / 지시 표현에 대해 다음 점검.

1. 표현이 의존하는 implicit anchor 식별 (비교 baseline? referent? anaphoric reference?)
2. Promo 본문이 그 anchor 를 인접 sentences 안에서 제공하는가
3. NO 면 fail. Fix 적용

### Anchor 손실 3 유형

| 유형 | 손실 영역 | 자주 보이는 token |
|---|---|---|
| **A. Baseline 손실** | "X 보다" 의 Y (비교 기준) 부재 | "above-average", "more efficient", "lower cost" + comparative |
| **B. Referent 손실** | "that X" 의 어떤 X anchor 부재 | "that loop", "that gap", "that process" |
| **C. Anaphoric reference 손실** | "the same / this Y" 의 which Y 부재 | "the same architecture", "this fixture", "those modules" |

### 해결 표현 패턴

- Baseline 1-2 단어 추가 (*"compared to X"*)
- Referent 명시 (*"that scrap recycling loop"* vs *"that loop"*)
- Quote / 지시 표현 제거 → plain paraphrase

### 실패 사례 3 (Tesla 368 cutting station promo, 2026-05)

초안 §5 *"generate scrap at 'above-average' rates. The 368 patent closes that loop on the same fixture"*. *above-average compared to what?* + *that loop = recycling? production?* + *the same fixture = which?* 세 anchor 부재. 사용자 catch.

Fix: *"above-average rates **compared to wet electrodes**. The 368 patent integrates **that scrap recycling** into the cutting station itself."*

## 시점 표현 cross-check (게시 시점 검증)

Promo 가 essay 발행 직후 또는 며칠 후 게시 가능. 시점 표현 (today / this week / last week / yesterday) 이 게시 시점에 정확해야 한다.

검증 절차.

1. 게시 예정 시점 확인
2. Essay 와 promo 의 시점 표현 정합성 점검
3. 제목 hook 의 시점 표현 별도 verify (제목은 share screenshot 시 가장 노출되는 위치)
