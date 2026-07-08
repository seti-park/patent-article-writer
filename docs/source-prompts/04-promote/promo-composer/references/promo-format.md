# Promo format

3-5 paragraph X digest. **Brief lock**: v2 supersedes v1's 6-paragraph spec. Target 280-340 words; FT/Economist editor-curated voice.

X Articles platform spec applies to essay (Phase 2). Promo's X post format is the area this file covers — distinct from X Articles.

## Digest 격 정의

FT (FirstFT, Edit), The Economist (Espresso, World in Brief) 같은 editor-curated digest 의 격. **Trust-driven** (engagement-driven 아님). 첫 sentence 에 thesis 가 압축되고, 본문은 핵심 fact 정리, 마무리는 담담한 implication 관찰.

## Essay vs Promo 비교

| 형식 | 분량 | 격 | 목적 | hedge 강도 |
|------|----|----|----|----------|
| **Essay** | 2,000-3,500w | FT/Economist prose, paragraph 3-7 sentence | 분석 backup evidence layer | 강 |
| **Promo** | 280-340w | Digest 격, 단락 1-3 sentence, 3-5 단락 | Trust-driven self-contained digest | 중 (essay backup mandatory) |

Promo 는 essay 에 의존. Promo 단독으로도 finishable 해야 하지만, 모든 fact 는 essay 본문에 backup 으로 존재한다.

## 3-5 단락 구조

### 3-paragraph version (단일 patent essay)

```
[ALL-CAPS Title]

§1 Lede (~30w)
 ↓
§2 Patent mechanism + thesis (~80w)
 ↓
§3 Closing (~25w, 담담한 observation + 🤔)
```

Total ~135w + title. Use when essay covers one patent with a tight thesis arc.

### 4-paragraph version (default — single patent + implication)

```
[ALL-CAPS Title]

§1 Lede (~30w)
 ↓
§2 Patent mechanism + thesis (~80w)
 ↓
§3 Implication (~50w)
 ↓
§4 Closing (~25w + 🤔)
```

Total ~185w. Most common for single-patent essays.

### 5-paragraph version (multi-patent or rich evidence)

```
[ALL-CAPS Title]

§1 Lede (~30w)
 ↓
§2 Patent one mechanism (~55w)
 ↓
§3 Patent two mechanism + thesis (~80w)
 ↓
§4 Implication (~50w)
 ↓
§5 Closing (~25w + 🤔)
```

Total ~240w. Use when essay covers 2+ patents needing distinct treatment.

### Paragraph signatures

- **§1 Lede** — 첫 sentence 에 thesis 압축. Specific date / number / quote 1 개 이상. Drama 없음. Voice canon `opening-news-event` 패턴 (declarative 진입).
- **§2 (or §2-§3) Patent mechanism**. Mechanism + 정량 1-2 개. Quote 인용 가능 (essay carry-over). 첫 sentence 가 무엇을 해결, 다음이 메커니즘, 정량이 claim 또는 spec [paragraph].
- **§3 or §4 Implication** — Thesis statement + external connection (product / unit cost / 시의성). Essay 의 implication section 의 압축.
- **§N Closing** — 담담한 observation 또는 forward-looking pointer. Essay closing 의 회수가 가장 강함. Defensive hedge / safe-harbor 격은 0 회 권장. Closing posture 4 taxonomy 는 `closing-posture.md` 참조.

## Title 작성

### 원칙

제목은 본문을 안 읽어도 글이 무엇인지 알 수 있어야 한다 (self-contained). Metaphor 에 의존하지 말고, patent 가 실제로 무엇을 다루는지 직설.

### 좋은 제목 패턴

Single-patent essay:
```
TESLA PATENT DETAILS [MECHANISM] BEHIND [PRODUCT/LINE]
```

Multi-patent essay:
```
TWO TESLA PATENTS DETAIL [MECHANISM 1] AND [MECHANISM 2] BEHIND ITS [PRODUCT/LINE]
```

Canon 예시:
```
TWO TESLA PATENTS DETAIL THE POWDER FLOW AND ROLLER GAP BEHIND ITS DRY 4680 LINE
```

### 회피 패턴

- "TESLA JUST PATENTED X" — 클릭베이트, SEO 격
- "TESLA REVEALS / UNVEILS" — 매체 hype 격
- 본문 없이 의미 안 통하는 echo 제목

### 판정 기준

본문 안 읽어도 무엇인지 안다. 분석가 voice. "of what?" 의문 안 떠오름.

## Lede 작성

Lede (첫 단락) 는 declarative news statement. 첫 sentence 에 thesis 압축.

### 좋은 lede 패턴

```
[Company] published [N] patent application(s) on [date] that, [optional read-together clause],
describe(s) [the underlying mechanism / system / framework] behind [related event].
```

### 판정 기준

첫 sentence 에 thesis 다 들어감. ALL-CAPS hook drama 없음. Specific date / number / quote 1 개 이상.

## 단락 + 문장 규칙

### 단락 길이

- 1-3 sentences per paragraph. Digest 격의 finishability 가 핵심.
- 4+ sentence paragraph 회피.
- 한 단락 = 한 역할 (lede / patent mechanism / thesis / implication / closing).

### 문장 길이

- Maximum 35 words per sentence. Espresso 패턴.
- §N closing 은 더 짧게 (15-25 words 권장).

## Format 규칙

- **Title**: ALL-CAPS, 12-16 단어, self-contained.
- **No markdown headers** in body. `##` 류 금지, `#` title 만.
- **Bold 회피**. Digest 격의 restrained voice.
- **Em dash**: 0 회 (PI §1 의 em dash 금지 결정 적용).
- **Colon**: 2 회 이내. Lede 또는 list 도입에만.
- **Emoji**: 1 회만 (closing 🤔).

## Hedge 정책

Promo 의 hedge 강도는 essay 와 동일 수준. Digest 격은 trust-driven 이므로 단언 강도가 essay 와 비슷하다.

| Hedge 영역 | Essay | Promo (Digest) |
|---------|-----|-----|
| Universal claims | Hard tier 0 건 | Hard tier 0 건 (essay 와 동일) |
| Modifiers | "significantly" 류 0 건 | 동일 |
| 1차 source attribution | 모든 인용 명시 | 핵심 인용만 명시 (압축 가능) |
| 시점 표현 | 정확성 필수 | 정확성 필수 + Sub-rule 1, 2 적용 |
| Industry baseline | strict | Essay 통과 fact 만 사용 |

단, promo 단독 fact-check 위험 시 essay 본문이 backup 으로 작동해야 한다. Essay 에 명시 없는 fact 는 promo 에 넣지 않는다.

## Final Checklist

- [ ] Title: ALL-CAPS, 12-16 단어, self-contained ("of what?" 의문 안 떠오름)
- [ ] Title 패턴: "X PATENT(S) DETAIL Y BEHIND Z" 또는 동등
- [ ] Lede: declarative news statement, 첫 sentence 에 thesis 압축
- [ ] 3, 4, or 5 단락 구조 (essay 복잡도에 맞춤)
- [ ] Closing: 담담한 observation + essay 회수 + 🤔
- [ ] Word count: 280-340 (본문, title 제외)
- [ ] 단락 1-3 sentences 모두 준수
- [ ] 문장 max 35 words
- [ ] 모든 fact 가 essay 에 backup
- [ ] 시점 표현 정확 (Sub-rule 1: sequence 자율 합성 금지)
- [ ] 시점 일수 정확 (Sub-rule 2: 평행 구조 위해 거짓 합성 금지)
- [ ] Quote anchor 보존 (Sub-rule 3: baseline / referent / anaphoric reference)
- [ ] Universal Claims: Hard tier 0 건
- [ ] R8 LLM-gen Fact: essay 에서 verify 된 fact 만 사용
- [ ] Em dash 0 회, colon 2 회 이내
- [ ] Bold 미사용, emoji 1 회 (🤔)

## Output 형식 (Verification Status header)

```
=== Verification Status (Promo-Composer, Digest mode) ===
✓ Voice register shift from essay → digest 적용
✓ Title: self-contained ALL-CAPS, "of what?" 의문 없음
✓ Voice 적용: §1 도입부 (declarative lede) + §N 결론부 (담담한 관찰)
✓ Essay backup 검증: 모든 fact 가 essay-final.md 에 명시
✓ 시점 표현 정확: Sub-rule 1 + Sub-rule 2 적용
✓ Quote anchor 보존: Sub-rule 3 (baseline / referent / anaphoric reference)
=== Promo 본문 ===
```

## Publication 버전 생성 (Strip pipeline)

Promo draft (위 Verification Status header 포함) 에서 publication 버전 (X 게시용 깨끗한 본문) 추출.

```bash
awk '/^=== Promo 본문 ===$/{flag=1; next} flag' promo-draft.md \
 | sed '/./,$!d' \
 > promotion-post.md
```

Pipeline 동작:

- `awk`, `=== Promo 본문 ===` 마커 이후 본문만 추출 (Verification Status header 제거)
- `sed '/./,$!d'`, 시작 부분의 leading blank lines 제거

결과: title + 3-5 paragraphs + 🤔. X 게시 시 그대로 paste 가능.

## v1 → v2 변경 사항

| 영역 | v1 (patent-promo) | v2 (promo-composer) |
|---|---|---|
| 단락 수 | 6 (Lede / Background / Patent1 / Patent2 / Implication / Closing) | 3-5 (essay 복잡도에 맞춰 가변) |
| Word target | 280-340 | 동일 |
| Wire와의 관계 | Wire 도 있었음 | Wire 폐기 — promo only |
| Korean adaptation | tech-essay-ko-pub | 폐기 — English only |
| Essay backup 위치 | tech-essay-en final | handoff/03-edit/essay-final.md |
