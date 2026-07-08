# Voice shift from essay to promo

Essay register 는 analytical restraint, promo register 는 editor-curated 압축에 bold selection 을 더한 것 (promo-format.md bold-selection rule). Shift 는
cadence, attribution 밀도, markdown 무게에서 일어난다. 밑에 깔린 목소리는 그대로다.

Promo 의 voice stack (v2): `_shared/references/deliverable-voice-rules.md` (hygiene 층) +
`_shared/references/anti-ai-writing.md` (AI-tell 층) + 이 파일 (register shift) +
`_shared/references/working-dialogue-voice.md` (KR post register). v1 이 참조하던
voice-profile.md 는 promo stack 에 없다: persona 가 필요한 두 지점 (opening, closing)
은 `voice-canon-lookup` 호출로 example 본문만 받아 쓴다.

## What stays the same

- Honesty discipline: no puffery ("remarkable / extraordinary / unprecedented" 0 건).
- Specificity over abstraction: 구체적 날짜, 숫자, 이름.
- Banned list (`anti-ai-writing.md` → `_shared/scripts/banned_terms.txt`) 전면 적용.
- Em dash 0 (title, body, KR post 모두).
- Hedge calibration 양방향: universal claims 0, "significantly" 류 modifier 0, safe-harbor
  boilerplate 0 (`closing-posture.md` 회피 목록).
- Emoji 규율: 팩 전체 <=1, 슬롯은 KR long post 마지막 문단 하나 (0 이 자연스러우면 0).

## What shifts (KR long post + EN thread)

### Cadence

Essay: 단락 3-7 sentences, 문장 20-25 words 대. KR long post: 단락 1-3 문장. Closing 은 15-25 words. Thread 는 tweet 당 1-3 문장. 같은
목소리가 더 빠르고 단어당 더 밀도 있게 간다.

### Attribution density

Essay: 모든 patent claim 에 `[dddd]`, 모든 external claim 에 `# Sources`. Promo: 핵심
인용만 명시, `# Sources` block 없음 (self-contained).

- `[dddd]` anchor: 전부 제거 (anchor 자체가 논점인 드문 경우만 예외).
- External source: 필수적일 때만 in-prose 로 이름 ("per Bosch's spec sheet"), 나머지는
  essay backup 에 위임.

### Markdown weight

Essay: `## §N` 헤더, single bold thesis anchor, italic 캡션. Promo: 헤더 없음 (ALL-CAPS
title 줄만), bold 0, italic 0. 도면 캡션이 필요하면 attachment metadata 의 alt-text
line 으로 (본문 밖).

### Voice pattern selection

Essay 의 canon 접근은 전 category. Promo 는 두 touchpoint 만:

- Opening: `opening-news-event` (declarative lede) 가 default 이자 사실상 유일한 fit.
- Closing: `closing-posture.md` 의 4 posture (canon 의 closing patterns 와 대응).
- Inline-bold-thesis-anchor: promo 에서 미사용 (bold 0). Bold 였던 문장은 plain 으로
  옮겨도 load-bearing 이어야 한다.
- 필요하면 `voice-canon-lookup` 을 호출해 해당 pattern 의 example 본문을 받아 cadence
  를 맞춘다. Signature lines 가 이미 cadence 를 주면 생략.

### Sentence-level register

Essay 는 rhetorical question, parenthetical aside 를 쓸 수 있다. Promo 는 걷어낸다. 각
문장은 사실 진술 또는 깨끗한 implication. 의문문은 쓰지 않는다 (closing posture 도
평서문으로 처리한다).

## Example pair

Essay:

> Tesla's patent grant predates the May announcement by eleven months. The architectural
> decision was complete; the announcement was vindication packaging. **The vision-sensor
> path is the patent's claim 1 (b), not a press-release embellishment.** [0016]

Promo:

> Tesla's patent granted eleven months before the May announcement. The architectural
> decision was complete; the announcement was vindication. The vision-sensor path sits in
> claim 1 (b), not in press copy.

차이: bold thesis anchor → plain sentence (여전히 load-bearing), `[0016]` 제거,
"embellishment" → "press copy" (더 짧게, 같은 뜻). 세 문장 그대로, cadence 유지, anchor
밀도만 다름.

## KR register (the Korean post)

KR post 는 essay 목소리를 아예 쓰지 않는다. 발행자의 working-dialogue voice
(`_shared/references/working-dialogue-voice.md`) 로 쓴다:

- 한국어 평서문, em dash 없음, plain / direct / peer-to-peer.
- 포스트 전체 2-5 문장 (dialogue 규칙의 단락 규칙을 포스트 단위로 적용).
- 과장 배제: EN deliverable 과 같은 honesty discipline 의 한국어 판. "충격적인", "반드시
  보세요", "드디어 밝혀진" 급 금지.
- 건조한 소개 동사: "정리했습니다", "읽어봤습니다", "따라가 봤습니다" 급.
- Protected terms (skill/파일명이 아니라 여기서는 특허번호, 회사명, 영어 인용구) 는
  원문 유지.

Leak 규칙은 양방향이다 (working-dialogue-voice.md 와 동일): dialogue voice 가 EN thread
로 새지 않고, essay 의 English deliverable voice 가 KR post 로 새지 않는다.

## Voice consistency anchor

Digest 와 essay 는 같은 필자가 쓴 것으로 읽혀야 한다. "다른 필자가 이 essay 를 압축한
것" 으로 읽히면 shift 가 과했다.

Test: promo 에서 문장 하나를 무작위로 뽑아 (1) essay 의 declared signature line,
(2) `voice-canon-lookup` 이 돌려준 `opening-news-event` example 문장과 나란히 놓는다.
문장 단위 cadence 와 단어 선택이 형제 관계여야 한다.
