# `invention-summary.md` schema

The fixed Markdown structure for Phase 1 Step 1's output. Replaces v1's `patent-reader-output.yaml`. Markdown chosen for human-edit-friendly handoff (the Owner can correct extraction errors directly).

## Top-level structure

```markdown
# Invention Summary

## Metadata
## 발명 명칭 / 기술분야
## 종래 문제 / 과제                              # with Quotable spans
## 청구항 분석 — 4-layer core mechanism          # Layer 1-4
## Reference number table                        # table
## Quote anchor table                            # table
## Timeline                                      # filing/publication/exam_period/prior_art_chronology
## Prior-art references + differentiation
## 유리한 효과 + 정량 데이터                      # with Quotable spans + quantitative metrics
```

Skeleton lives in `handoff-template/01-design/invention-summary.md`. Copy and fill.

## Section-by-section spec

### Metadata

```markdown
## Metadata

- **Patent ID**: <patent number, e.g. US 2026/0125022 A1>
- **Title**: <full title>
- **Filing date**: <YYYY-MM-DD>
- **Publication date**: <YYYY-MM-DD>
- **Inventors**: <name, name, name>
- **Classification**: <CPC codes>
- **Assignee**: <company>
```

All fields required if visible on cover page. Use `<unknown>` if genuinely not on cover.

### 발명 명칭 / 기술분야

```markdown
## 발명 명칭 / 기술분야

(Patent title in essay-ready phrasing + 기술분야 short paragraph.)
```

1-3 sentences. Title 격상 from patent's official title to essay's reader-friendly phrasing. 기술분야 from the patent's "Technical Field" or first paragraph.

### 종래 문제 / 과제

```markdown
## 종래 문제 / 과제

(Background of Invention 압축 — 1-3 paragraphs. Each problem statement cites a paragraph anchor.)

**Quotable spans:**
- `[0014]`: "기존 X 의 한계는 Y"
- `[0016]`: "..."
```

**Quotable spans** = verbatim text Phase 2 Compose can cite without re-touching patent.md. Format per `references/quote-anchor-conventions.md`:
- Each entry: `` `[paragraph-id]`: "verbatim text" ``
- 2-5 entries per block
- Verbatim — no paraphrase, no normalization

### 청구항 분석 — 4-layer core mechanism

Carry-over from v1 `patent-reader.references/4-layer-core-mechanism.md`.

```markdown
## 청구항 분석 — 4-layer core mechanism

### Layer 1 — What (one sentence)

<Single-sentence summary of primary technical claim>

### Layer 2 — How (mechanism)

(3-7 ordered steps. Each step: verb phrase + reference number labels.)

1. <step 1>
2. <step 2>
3. <step 3>

**Key components**: <list of components, mapped 1:1 with reference_number_table>

### Layer 3 — Why novel

- **Relative to prior art**: <differentiation from cited prior art — often explicit in patent's Background / Summary>
- **Industry practice contrast**: <contrast with established engineering practice, may not be cited in patent>

### Layer 4 — Innovation angles

(2-4 angles. Each angle = distinct novelty dimension that could carry its own essay thesis. Phase 1 Step 3 generates thesis candidates from these.)

- **angle_id_1**: <angle name>
  - Evidence paragraphs: `[XXXX]`, `[XXXX]`
  - Quote anchor refs: `q-XXXX-1`, `q-XXXX-2`
- **angle_id_2**: <angle name>
  - Evidence paragraphs: ...
  - Quote anchor refs: ...
```

Layer 4 target: 2-4 angles. Each must have at least one evidence paragraph and one quote anchor ref. No anchor = exclude.

### Claim scope map (locked / open / pinned)

Required whenever Phase 2 will cite claim anchors. One row per independent claim
plus every dependent claim the spine relies on.

```markdown
## Claim scope map

| Claim | Locks (required by claim text) | Leaves open (description preference only) | Pins (approximate point limitations) |
|---|---|---|---|
| 1 | <orderings / conditions / ranges the claim text actually requires> | <what the description prefers but the claim does not require> | <"about X" point values, if any> |
| 5 | ... | ... | e.g. "begins at about 50° C." — a pinned onset point, NOT a floor |
```

Rules:
- **Locks** lists only what the claim text requires. Never attribute the description's
  preferred embodiment (ordering, protocol, geometry) to a claim — narrate such preferences
  as the description's, on description anchors.
- **Pins** lists approximate point limitations ("about X"). A pinned point is never a floor
  or a ceiling: do not describe it with bound vocabulary the claim does not state.
- `phase2-handoff-notes.md` trap wording must restate this map's distinctions, not collapse
  them (a trap that groups a pinned point under "floors" re-seeds the exact drift it exists
  to prevent — see run 2026-06-11-us20260158546a1, finding F1).

### Reference number table

```markdown
## Reference number table

| Number | Label | Paragraphs | Figures |
|---|---|---|---|
| 414 | Vehicle Control Unit | `[0016]`, `[0023]`, `[0028]` | FIG. 1, FIG. 4 |
| 416 | Vision Sensor Array | `[0017]`, `[0024]` | FIG. 2 |
```

Every numeric label in the patent text gets a row. `Figures` column lists which figures contain the label (cross-references the cleaned figure filenames `fig-01.png` etc.).

### Figure relationships

```markdown
## Figure relationships

| Figure | Paired with | Relationship | Page (if known) | Cover candidate? | Phase map (sequences only) |
|---|---|---|---|---|---|
| FIG. 6A | FIG. 6B | same-page sub-figure pair | p. 14 | | |
| FIG. 7A | FIG. 7B, FIG. 7C | progressive sequence (before / during / after) | pp. 15-17 | yes (most literal picture of the claimed step) | 7A p1 / 7B p2 / 7C p3, per [0046]-[0047] |
| FIG. 1 | (standalone) | — | p. 9 | | |
```

Documents paired relationships that figure-selection (thesis-architect Step 9) needs:

- **same-page sub-figure pair** — typically processed together as one cognitive unit (e.g., FIG. 6A + 6B). Selecting one but not the other risks losing the visual narrative.
- **progressive sequence** — must keep all units to preserve before/after meaning. Splitting breaks the figure's argument.
- **standalone** — independent figure, no pair constraint.
- **Cover candidate**: mark the single figure that best carries the 5:2 header. It is judged on
  visual force and on depicting the claimed core step, separately from the argument-economy
  selection. A sequence that depicts the claimed step is a strong cover candidate even if a static
  end-state figure already covers the same point in the body.
- **Phase map**: when a figure is a progressive sequence and the specification enumerates phases,
  record the phase-to-panel ranges with the enumerating paragraph anchor. Keyframes chosen for a
  cover strip map one-per-phase from this column, not from visual spacing.

Phase 1 Step 9 (figure mapping) reviews this table to ensure paired figures are treated as one unit in `figure-selection.md`. Phase 1 Step 11 (`phase2-handoff-notes.md`) flags any paired figure where the Owner chose to break the pair, so Phase 2 doesn't reopen the decision.

Origin: phase1-retrospective.md Insight 6-1 — FIG 6A 가 selection 단계에서 누락 후 Owner 의 catch 로 추가됨. Paired 관계를 reference number table 단계에서 미리 정리하면 figure-selection 의 retroactive 정정 회피.

### Quote anchor table

```markdown
## Quote anchor table

| Quote ID | Paragraph | Verbatim text | Significance |
|---|---|---|---|
| q-0016-1 | `[0016]` | "the vision sensor providing pre-impact prediction to the airbag controller" | claim-supporting |
| q-0024-1 | `[0024]` | "deployment decision is made approximately 70 milliseconds before traditional accelerometer-based systems would respond" | quantitative |
```

Quote ID format: `q-<paragraph>-<seq>`. Significance enum: `claim-supporting | mechanism-critical | quantitative | prior-art-contrast`. See `references/quote-anchor-conventions.md`.

### Timeline

```markdown
## Timeline

- **Filing date**: 2024-10-23
- **Publication date**: 2026-04-23
- **Examination period**: 547 days
- **Prior-art chronology**:
  | Citation | Filing date | Publication date | Days relative to subject filing |
  |---|---|---|---|
  | US 2022/0123456 A1 | 2021-01-15 | 2022-04-21 | -1011 |
  | US 2023/0078901 A1 | 2022-03-08 | 2023-03-15 | -594 |
```

Examination period = `publication_date - filing_date` for published applications; `grant_date - filing_date` for granted patents.

Days relative to subject filing: negative = prior art predates (typical), positive = postdates (unusual — continuation or re-examination).

### Prior-art references + differentiation

```markdown
## Prior-art references + differentiation

- **US 2022/0123456 A1** (cited at `[0008]`): <significance — why mentioned, how this patent differentiates>
- **Bosch DE 10 2019 ...** (cited at `[0011]`): <significance + differentiation>
```

Each cited prior art reference gets a bullet. Required for `references/4-axis-grounding.md` Axis 4 (baseline-difference).

### 유리한 효과 + 정량 데이터

```markdown
## 유리한 효과 + 정량 데이터

(Effects of the Invention 압축. Quantitative metrics listed with anchor.)

**Quotable spans:**
- `[0023]`: "본 발명은 약 70 밀리초의 사전 감지 능력을 제공한다"
- `[0025]`: "..."

| Metric | Value | Paragraph |
|---|---|---|
| Pre-impact lead time | ~70 ms | `[0024]` |
| False-positive rate | <0.1% | `[0029]` |
```

Effects 영역의 Quotable spans 는 Axis 3 (effect anchor) 의 직접 source.

## Verbatim discipline

`Quotable spans` 와 `Quote anchor table` 의 verbatim text 는 patent 원문과 exact match. No paraphrase, no punctuation normalization, no capitalization adjustment.

근거: Phase 3 Edit Pass 3 가 `[xxxx]` 인용을 verbatim 으로 string-match 검증. Drift 발생 시 paraphrase mutation flag.

## Edge cases

- **Patent has no clear quote-worthy passages** — emit empty `Quotable spans:` block (just the header) + empty Quote anchor table. Phase 1 Step 3 가 Layer 4 `innovation_angles` 에 더 의존하게 됨.
- **Patent contains a typo** — preserve verbatim. 의미 있는 typo 면 본 schema 의 별도 영역에 note.
- **Quote spans paragraph boundary** — separate Quote anchor entries per paragraph.
- **Equations / tables in patent body** — equation 자체는 quote anchor 아님. 주변 prose 가 anchor-worthy 면 anchor. 수치는 quantitative_data table 에.
