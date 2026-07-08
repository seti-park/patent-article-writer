<!--
  TEMPLATE: handoff/01-design/owner-briefing.md
  Produced by: thesis-architect (Phase 1 Design, Step 2b - owner briefing)
  Schema source: _shared/references/owner-briefing-schema.md

  KOREAN document for the OWNER (publisher). Written after Step 2 context research
  and before Step 3 thesis candidates: it describes the PATENT, never the essay's
  angle. Register (embedded because Phase 1 is voice-off): 건조한 평서문, 단정은
  근거 위에서만, 과장·수식어 배제, 특허 용어 원어 병기, no em dashes. 본문
  600-900 단어(어절) + 인용 블록, 5분 안에 읽히는 분량.

  Grounding: every patent-derived claim carries an inline `[dddd]` anchor.
  Sections ①-④ each END with a **근거 (verbatim):** block whose lines are
  gate-parseable Quotable-span lines; the orchestrator runs gate_quotes on this
  file against input/patent.md at the Phase-1 early gate (QUOTE-001 = fix at
  source). Quotes stay English inside the quote marks; the Korean gloss goes on
  the NEXT line, in parentheses. A 근거 line must end at its closing quote or the
  gate silently skips it. Quotes shorter than 8 characters are banned (the gate
  ignores them).

  The ① block below carries one fully-worked 근거 line (Tesla RCM example patent
  used throughout the pipeline docs); everything in <...> is a placeholder.

  Archived to essays/<essay-id>/owner-briefing.md, next to the run's patent.md
  snapshot, so anchors resolve offline.
-->

# Owner Briefing (발행자 브리핑)

- **특허 번호**: <US 2026/0125022 A1>
- **제목**: <Predictive Airbag Deployment using Vehicle Vision Data>
- **상태**: <등록·출원 구분. 등록이면 등록번호·등록일, 출원이면 공개번호·심사 상태. 예: 출원
  (공개 공보; 등록 전, 심사 계속 중)>
- **출원일**: <2024-10-23>
- **발명자**: <Jane A. Roe, Marcus Lindgren, Priya Nair>

**한 줄 요약**: <발행자가 가져갈 한국어 한 문장, 정확히 한 줄. 예: 전방 카메라의 충돌 예측
신호가 가속도계보다 먼저 에어백 전개 결정을 내리게 하는 구조를 청구한 출원이다.>

## ① 과거 기술의 과제/문제점

<명세서 background 가 지목하는 문제를 2-4문장으로. 업계 일반론이 아니라 이 문서가 명시한
문제로 한정. 모든 특허 유래 서술에 인라인 `[dddd]` 앵커. 예: 기존 에어백은 가속도계로
충돌을 감지하므로 충돌이 시작된 뒤에야 반응한다 `[0014]`.>

**근거 (verbatim):**
- `[0014]`: "conventional accelerometer-based systems respond only after the collision has begun"
  (기존 가속도계 기반 시스템은 충돌이 시작된 뒤에야 반응한다는 뜻)
<!-- ^ 완성 예시 줄. 형식: 대시, 백틱 앵커 `[dddd]`, 콜론, 곧은 큰따옴표 안에 patent.md
     원문 verbatim(8자 이상), 줄은 닫는 따옴표에서 끝남. 한국어 글로스는 다음 줄 괄호 안.
     블록당 1-3줄. 허용 정규화는 quote-anchor-conventions.md 와 동일(NBSP·bold·smart quote),
     그 외 일체 불가. 따옴표 안 번역 금지. -->

## ② 기존 기술의 해결 방향과 그 한계

<종래 기술(선행 문헌·업계 관행)이 그 문제를 어떻게 풀려 했고 어디서 막혔는지. 2-4문장,
앵커 포함.>

**근거 (verbatim):**
- `[<dddd>]`: "<exact English quote from patent.md, 8+ chars>"
  (<한국어 글로스>)

## ③ 이 특허의 독창적 해법 (핵심 청구항 중심)

<발명이 실제로 청구하는 해법. 핵심 독립항 번호 명시. invention-summary Claim scope map 의
구분을 그대로 사용: locked / open / pinned, 출원 건은 locked 없이 sought-* (청구 중, 확정
아님). 청구항이 요구하는 것과 명세서가 선호만 하는 것을 절대 섞지 않는다.>

**근거 (verbatim):**
- `[<dddd>]`: "<exact English quote>"
  (<한국어 글로스>)

## ④ 기대 효과

<명세서가 주장하는 효과로 한정. 수치는 앵커와 함께. 명세서 밖의 효과 추정 금지(⑥ (b)로
보낸다).>

**근거 (verbatim):**
- `[<dddd>]`: "<exact English quote>"
  (<한국어 글로스>)

## ⑤ 회사 프로모션 글/기술과의 연결

<Step 2 context research 와 input/essay-context.md(있으면)를 재료로. 연결할 프로모션
맥락이 없으면 "없음"이라고 명시.>

**특허가 실제로 뒷받침하는 것**
- <특허 텍스트에 앵커되는 부분만. `[dddd]`>

**회사 주장**
- <특허가 뒷받침하지 않는 회사 발언. fact-check-log 의 evidence_level 라벨을 그대로 부기.
  예: 랙 출하 일정은 회사 발표다 (company-claimed); 등록 원부상 담보 설정은 확인됐다
  (registry-verified).>

## ⑥ 아는 것/모르는 것 경계 지도

**(a) 이 런의 증거가 확립한 것**
- <특허 전문 확인, 레지스트리 사실 등 이번 런이 검증한 것.>

**(b) 증거 밖에 있는 것 - 단정 불가 리스트**
- <독자 앞에서 단정하면 안 되는 것의 명시적 목록. 예: 읽지 않은 관련 출원의 전문,
  레지스트리 스냅샷 이후의 심사 경과, 제품이 실제로 청구항을 실시하는지 여부.>

**(c) 원문 자체가 열어둔 것**
- <명세서가 대안 실시예나 "may" 표현으로 열어둔 지점. `[dddd]` 인용 가능; verbatim 인용 줄
  형식을 쓰면 그 줄도 게이트 검증 대상.>

## ⑦ 자료 지도

반박이 오면 볼 곳:

| 반박 유형 | 참고 파일 |
|---|---|
| 가장 강한 반론 (steelman) | `handoff/01-design/thesis-spine.md` §Adversarial defense |
| 문장별 검증 | 최종 라운드 `handoff/03-edit/selfaudit-round-N-grounding.md` |
| 외부 사실 | `handoff/01-design/fact-check-log.md` |
| 청구항 범위 | `handoff/01-design/invention-summary.md` §Claim scope map |
| 원문 | `essays/<essay-id>/patent.md` |

<N 은 이 런의 마지막 self-audit 라운드 번호(아카이브의 handoff/03-edit/ 에서 가장 큰 N).
경로는 고정 계약 경로: 아카이브 안에서는 essays/<essay-id>/ 기준으로 그대로 통한다.>

<!--
  REVISION NOTE convention (feedback-loop discipline):
  When a later step or a self-audit fix revises this file, append a block-quote:
  > Revision note - triggered by [step N] [date]: [what changed and why]
-->
