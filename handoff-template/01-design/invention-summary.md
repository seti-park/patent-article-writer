<!--
  TEMPLATE: handoff/01-design/invention-summary.md
  Produced by: thesis-architect (Phase 1 Design, Step 1)
  Schema source: thesis-architect/references/invention-summary-schema.md
                 + references/quote-anchor-conventions.md

  Fill every <placeholder>. Use <unknown> only when a cover-page field is
  genuinely absent. All Quotable spans and Quote anchor table verbatim_text
  must be EXACT patent text (post-allowed-normalization) — Phase 3 Edit Pass 3
  string-matches the essay's [xxxx] cites against these.

  Example content below uses the Tesla RCM / predictive-airbag / 70ms patent
  used throughout the pipeline docs.
-->

# Invention Summary

## Metadata

<!-- All fields required if visible on the cover page. Use <unknown> otherwise. -->
- **Patent ID**: US 2026/0125022 A1
- **Title**: Predictive Airbag Deployment using Vehicle Vision Data
- **Filing date**: 2024-10-23
- **Publication date**: 2026-04-23
- **Inventors**: Jane A. Roe, Marcus Lindgren, Priya Nair
- **Classification**: B60R 21/0134; G06V 20/58; B60R 21/01512
- **Assignee**: Tesla, Inc.

## 발명 명칭 / 기술분야

<!-- 1-3 sentences. Title 격상 from official title to essay-ready phrasing.
     기술분야 from the patent's "Technical Field" or first paragraph. -->
A restraint-control architecture that lets a vehicle's forward vision sensor
feed pre-impact predictions directly into the airbag controller's deployment
decision. Technical field: occupant-protection / restraint-control systems for
automotive safety, specifically vision-assisted predictive airbag deployment.

## 종래 문제 / 과제

<!-- Background of Invention 압축 — 1-3 paragraphs. Each problem statement cites
     a paragraph anchor. The Quotable spans below are the verbatim source Phase 2
     cites directly without re-touching patent.md. -->
Conventional airbag systems rely on accelerometer-based crash sensing, which can
only register a collision once the impact has begun. This reactive posture caps
how early the restraint-control module (RCM) can commit to deployment, leaving
little margin for occupant pre-positioning.

**Quotable spans:**
<!-- 2-5 entries. Format: `[XXXX]`: "verbatim text". 4-digit zero-padded anchors.
     Verbatim — no paraphrase, no punctuation/capitalization normalization. -->
- `[0014]`: "conventional accelerometer-based systems respond only after the collision has begun"
- `[0016]`: "the resulting latency limits the window available for pre-deployment occupant positioning"

## 청구항 분석 — 4-layer core mechanism

### Layer 1 — What (one sentence)

<!-- Single-sentence summary of the primary technical claim. -->
A vehicle vision sensor supplies pre-impact predictions to the airbag controller
so that the deployment decision is made before an accelerometer-based system would
register the crash.

### Layer 2 — How (mechanism)

<!-- 3-7 ordered steps. Each step: verb phrase + reference number labels.
     Key components must map 1:1 with the Reference number table below. -->
1. The vision sensor array (416) captures the forward scene and detects an imminent collision.
2. The vision sensor array (416) computes a pre-impact prediction signal.
3. The prediction signal is routed to the vehicle control unit (414) over the safety bus (420).
4. The vehicle control unit (414) evaluates the prediction against deployment thresholds.
5. The vehicle control unit (414) arms and triggers the airbag module (430) within the pre-impact window.

**Key components**: vehicle control unit (414), vision sensor array (416), safety bus (420), airbag module (430)

### Layer 3 — Why novel

- **Relative to prior art**: Prior systems treat optical sensing as a redundant or post-impact input; here the vision path is the primary, claim-anchored predictive trigger.
- **Industry practice contrast**: Standard automotive restraint design gates deployment on accelerometer latency; this architecture moves the decision upstream to the perception layer.

### Layer 4 — Innovation angles

<!-- 2-4 angles. Each = a distinct novelty dimension that could carry its own
     thesis. Each MUST have >=1 evidence paragraph and >=1 quote anchor ref.
     No anchor = exclude. Phase 1 Step 3 generates thesis candidates from these. -->
- **predictive-vision-path**: vision sensor as the claim-anchored predictive trigger, not a redundant input
  - Evidence paragraphs: `[0016]`, `[0017]`
  - Quote anchor refs: `q-0016-1`, `q-0017-1`
- **pre-impact-lead-time**: quantified ~70ms decision lead over accelerometer baseline
  - Evidence paragraphs: `[0024]`
  - Quote anchor refs: `q-0024-1`
- **architecture-timing**: filing predates Tesla's public safety announcement, reframing the public claim
  - Evidence paragraphs: `[0016]`
  - Quote anchor refs: `q-0016-1`

## Reference number table

<!-- Every numeric label in the patent text gets a row. Figures column lists which
     cleaned figure files (fig-NN.png / FIG. N) contain the label. -->
| Number | Label | Paragraphs | Figures |
|---|---|---|---|
| 414 | Vehicle Control Unit | `[0016]`, `[0023]`, `[0028]` | FIG. 1, FIG. 4 |
| 416 | Vision Sensor Array | `[0017]`, `[0024]` | FIG. 2 |
| 420 | Safety Bus | `[0019]` | FIG. 1 |
| 430 | Airbag Module | `[0021]`, `[0028]` | FIG. 1, FIG. 4 |

## Figure relationships

<!-- Documents paired relationships that figure-selection (Step 9) needs.
     same-page sub-figure pair / progressive sequence / standalone.
     Selecting one of a pair but not the other risks losing the visual narrative. -->
| Figure | Paired with | Relationship | Page (if known) |
|---|---|---|---|
| FIG. 1 | (standalone) | — | p. 9 |
| FIG. 4A | FIG. 4B | same-page sub-figure pair | p. 13 |
| FIG. 7A | FIG. 7B, FIG. 7C | progressive sequence (before / during / after) | pp. 15-17 |

## Quote anchor table

<!-- Comprehensive list of every quote-worthy passage. Quote ID = q-<paragraph>-<seq>.
     Significance enum (mutually exclusive):
       claim-supporting | mechanism-critical | quantitative | prior-art-contrast -->
| Quote ID | Paragraph | Verbatim text | Significance |
|---|---|---|---|
| q-0016-1 | `[0016]` | "the vision sensor providing pre-impact prediction to the airbag controller" | claim-supporting |
| q-0017-1 | `[0017]` | "the vision sensor functions as a predictive input rather than a redundant sensor" | mechanism-critical |
| q-0014-1 | `[0014]` | "conventional accelerometer-based systems respond only after the collision has begun" | prior-art-contrast |
| q-0024-1 | `[0024]` | "deployment decision is made approximately 70 milliseconds before traditional accelerometer-based systems would respond" | quantitative |

## Timeline

<!-- Examination period = publication_date - filing_date (published applications)
     or grant_date - filing_date (granted patents).
     Days relative to subject filing: negative = prior art predates (typical). -->
- **Filing date**: 2024-10-23
- **Publication date**: 2026-04-23
- **Examination period**: 547 days
- **Prior-art chronology**:
  | Citation | Filing date | Publication date | Days relative to subject filing |
  |---|---|---|---|
  | US 2022/0123456 A1 | 2021-01-15 | 2022-04-21 | -1011 |
  | DE 10 2019 207 123 A1 | 2019-05-14 | 2020-11-19 | -1988 |

## Prior-art references + differentiation

<!-- Each cited prior-art reference gets a bullet: significance + how this patent
     differentiates. Required for 4-axis-grounding Axis 4 (baseline-difference). -->
- **US 2022/0123456 A1** (cited at `[0008]`): discloses optical sensing as a secondary, post-impact confirmation channel; this patent differentiates by making the vision path the primary pre-impact trigger.
- **DE 10 2019 207 123 A1 (Bosch)** (cited at `[0011]`): accelerometer-based ECU with ~10ms deployment latency; cited as the baseline this invention is contrasted against.

## 유리한 효과 + 정량 데이터

<!-- Effects of the Invention 압축. The Quotable spans here are the DIRECT source
     for 4-axis-grounding Axis 3 (effect anchor). Quantitative metrics listed with
     paragraph anchor. -->
The architecture moves the deployment decision upstream of accelerometer latency,
yielding a measurable pre-impact lead time while keeping false-positive deployment
within bounds.

**Quotable spans:**
- `[0024]`: "deployment decision is made approximately 70 milliseconds before traditional accelerometer-based systems would respond"
- `[0029]`: "the false-positive deployment rate remains below 0.1 percent across the validation set"

| Metric | Value | Paragraph |
|---|---|---|
| Pre-impact lead time | ~70 ms | `[0024]` |
| False-positive rate | <0.1% | `[0029]` |

<!--
  REVISION NOTE convention (feedback-loop discipline):
  When a later step revises this file, append a block-quote at the end:
  > Revision note — triggered by [step N] [date]: [what changed and why]
-->
