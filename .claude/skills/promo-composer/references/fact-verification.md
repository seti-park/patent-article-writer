# Fact verification: the safe-claims defense

Promo 는 essay 와 같은 hedge 강도에서 작성되므로 unverified fact 노출 시 fact-check
위험이 크다. v2 의 답은 단순하다: **promo 는 사실을 검증하지 않는다. 이미 검증된 문장을
재사용한다.**

## Why verbatim sourcing (the rationale)

The Compose↔Edit loop and the post-acceptance self-audit scrubbed specific error CLASSES
out of the essay. Live examples from the etched-us20240378175-r2 run:

- **Venue**: "pitched on stage" was unsupported; corrected to the stealth-exit thread
  (self-audit sa1A-F01/sa1B-F1, six occurrences fixed including a signature line).
- **Founder count**: exhaustive "both co-founders" corrected to "two of its co-founders"
  (self-audit round 2).
- **Date arithmetic**: "two years before" corrected to "three years before" (May 2023 →
  June 2026; caught at compose).

`essay-final.md`, `publication-package/publication.md`, and `owner-briefing.md` carry the
CORRECTED phrasings. Sourcing every promo phrase verbatim from those texts is what keeps
the dead errors dead. Writing a promo phrase from memory of the run, or from general
knowledge, is exactly how a scrubbed error resurrects: memory holds the pre-correction
version too.

## The hard rule

1. Allowed sources, the only three: `essays/<id>/essay-final.md`,
   `essays/<id>/publication-package/publication.md`, `essays/<id>/owner-briefing.md`.
2. Every factual phrase in every deliverable maps to a sentence in those sources.
3. Verbatim-consistency scope: numbers, dates, names, venue words, quantities, and **verbs
   of certainty**. An application-era essay writes "filed", "asks for", "still hasn't said
   yes"; the promo never upgrades to "patented", "owns", "granted". A company-claimed
   figure the essay labels as the company's telling stays labeled in the promo.
4. A fact not in the sources is DROPPED. No web search, no patent re-read, no
   fact-check-log or handoff mining, no memory. (v1 allowed "web search verify 또는 삭제";
   v2 deliberately removes the verify branch. Promo runs post-archive with no reviewer
   behind it, so the only safe claim is a reused claim.)
5. Dropped facts are listed on the Verification Status header's `fact_trace` line
   (`dropped facts: none` when clean).

## 검증 절차 (per deliverable, per sentence)

1. 후보 sentence 의 factual phrase 를 모두 표시한다 (숫자, 날짜, 이름, 장소, 인용,
   확실성 동사).
2. 각 phrase 를 세 source 중 하나의 문장에 매핑한다. 매핑 안 되면 그 phrase 를 고쳐
   쓰거나 문장을 버린다.
3. KR post 는 번역이므로 단어가 아니라 사실 단위로 매핑한다: 숫자/날짜/이름/특허번호는
   원문 그대로, 영어 인용은 따옴표 안에 영어 원문 유지 (번역은 따옴표 밖).
4. 아래 Sub-rules 1/2/3 을 시점 표현과 quote 압축에 적용한다.

가장 안전한 습관: essay lead 의 timing 표현과 declared signature lines 를 그대로
carry-over 하는 것. 이 문장들은 loop 와 self-audit 를 이미 통과했다.

## Sub-rule 1: 시점 관계 자율 합성 금지

Promo 가 시점 sequence 표현 (before / after / during / N days 간격) 을 쓸 때 두 가지를
모두 verify 한다.

- 두 시점이 source 문장에 명시되어 있는가
- 그 두 시점 사이의 sequence relationship 이 source 에 명시되어 있는가

둘 다 YES 면 OK. 하나라도 NO 면 그 시점 표현을 버린다 (v1 과 달리 web verify 대안
없음).

실패 사례 (Tesla dry 4680 promo, 2026-05): 초안이 *"emerged the week before Cybercab
pilot production began"* 이라고 썼다. 실제로는 patents 가 발표 after 공개. Sequence
역방향 자율 합성, 사용자 catch.

## Sub-rule 2: 평행 구조 위험 (date arithmetic)

두 시점 사이 간격을 표현할 때, 다른 시점 표현과 평행 구조 ("seven days apart + seven
days after") 를 만들고 싶은 충동을 의식적으로 차단한다. 평행성 < 정확성.

- 간격 표현은 essay 자신의 간격 문구를 그대로 가져오는 것이 1순위다 ("three years
  older").
- Essay 에 간격 문구가 없고 두 날짜가 모두 essay 에 있으면, 캘린더로 직접 계산해서
  쓴다. 계산 결과를 다시 한 번 날짜로 검산한다.
- 해결 표현 패턴: 정확한 일수 직접 (*"eight days after"*), 자연스러운 idiom (*"just
  over a week after"*), 시점 명시 + 함축 (*"emerged on April 30, just over a week after
  Q1 earnings"*).

실패 사례 (Tesla dry 4680 promo, 2026-05): *"filed seven days apart... emerged seven
days after Q1 earnings"*. 실제 간격은 8 일. 평행 구조를 위해 "seven" 으로 합성, 사용자
catch. 같은 class 가 이 파이프라인에서도 나왔다: r2 run 의 "two years" 슬립 (위 참조).

## Sub-rule 3: Quote 압축 시 anchor preservation

Essay quote 나 짧은 표현을 압축 carry-over 할 때, 그 표현이 의존하는 비교 baseline /
referent 가 promo 본문만으로 finishable 한지 verify 한다. Thread 에서는 tweet 단위로
적용한다 (각 tweet standalone).

절차: quoted phrase / 지시 표현마다 (1) implicit anchor 식별 (baseline? referent?
anaphoric reference?) (2) promo 본문이 인접 문장 안에서 그 anchor 를 제공하는지 확인
(3) NO 면 fix.

| 유형 | 손실 영역 | 자주 보이는 token |
|---|---|---|
| A. Baseline 손실 | "X 보다" 의 비교 기준 부재 | "above-average", "more efficient", "lower cost" |
| B. Referent 손실 | "that X" 의 X anchor 부재 | "that loop", "that gap", "that process" |
| C. Anaphoric 손실 | "the same / this Y" 의 which Y 부재 | "the same architecture", "this fixture" |

해결: baseline 1-2 단어 추가 (*"compared to X"*), referent 명시 (*"that scrap recycling
loop"*), 또는 지시 표현 제거 후 plain paraphrase.

실패 사례 (Tesla 368 cutting station promo, 2026-05): *"generate scrap at
'above-average' rates. The 368 patent closes that loop on the same fixture"*. baseline /
referent / fixture anchor 세 개 부재, 사용자 catch. Fix: *"above-average rates compared
to wet electrodes. The 368 patent integrates that scrap recycling into the cutting
station itself."*

## 게시 시점 cross-check

Promo 는 essay 발행 직후 또는 며칠 후 게시될 수 있다. 시점 표현 (today / this week /
last week / 어제 / 이번 주) 이 게시 시점 기준으로 정확해야 한다.

1. 게시 예정 시점 확인 (owner context, 없으면 상대 시점 표현 자체를 피한다: 날짜
   직접 표기가 항상 안전하다).
2. Essay 와 promo 의 시점 표현 정합성 점검.
3. Tweet 1 hook 과 KR post 첫 문장의 시점 표현은 별도 verify (share 시 가장 노출되는
   위치).

## Never reopen the loop

이 pass 중에 essay 자체의 사실 결함이 의심되면:

- 해당 claim 을 promo 에서 뺀다.
- Verification Status header 의 `suspected_essay_defects` line 에 적는다 (essay 위치 +
  의심 내용 한 줄).
- 거기서 끝. essay 는 편집하지 않고, 편집을 제안하지도 않는다. 후속 처리는
  human-post-accept channel (essays/<id>/revision-notes.md 경로, ledger 로 흘러간다) 의
  몫이다.
