# Audience adaptation

Essay (Phase 2) → Promo (Phase 4) audience shift. Essay reader is investor / tech analyst. Promo reader is X general public — potentially Tesla fan, tech enthusiast, casual scroller.

Adapt without losing the trust-driven posture.

## Reader profile delta

| Dimension | Essay reader | Promo reader |
|---|---|---|
| Patent literacy | medium-high | low |
| Domain context | strong (knows the players, the industry timeline) | mixed (some are casual fans) |
| Attention | high — opened the long-form intentionally | low — scrolling past in feed |
| Trust signal sensitivity | high (will dismiss puffery) | high (X public sniffs hype quickly) |

## What to expand

### Technical jargon

Essay uses term once + assumes understanding. Promo gets one short clarification per technical term.

Essay:
> The vision-sensor latency feeds the predictive controller within the 70ms window.

Promo:
> The vision sensor — a camera, not the standard accelerometer — feeds the airbag controller about 70 milliseconds before the impact starts.

The clarification adds ~10 words but lands the mechanism for a reader who hasn't built the model from the essay's §2.

### Reference number context

Essay relies on the reader linking reference numbers (414, 416) back to the figure. Promo drops reference numbers entirely (the X reader doesn't have the figure to cross-reference unless attached).

Essay:
> The Vehicle Control Unit (414) receives the vision sensor's pre-impact signal [0016].

Promo:
> The airbag controller receives the vision sensor's pre-impact signal.

### Filing/legal terms

Essay distinguishes filing date, publication date, grant date. Promo collapses to "the patent published on YYYY-MM-DD" unless the timing distinction IS the thesis.

## What to compress

### Claim mechanics

Essay walks the reader through the 4-step claim mechanism. Promo states the mechanism in one sentence + leaves the walkthrough to the essay.

Essay:
> The mechanism unfolds in four steps: vision capture, predictive inference, control signal generation, deployment trigger. Each step's latency contributes to the 70ms total.

Promo:
> The mechanism is a four-step path from vision to deployment, summing to about 70 milliseconds.

### Paragraph anchors

Essay uses `[0016]`, `[0024]` inline. Promo drops the anchors — the X reader has no use for them and they create visual clutter.

Essay:
> Tesla's claim of 70ms pre-impact deployment [0024] rests on the vision-sensor path [0016].

Promo:
> Tesla's claim of 70ms pre-impact deployment rests on the vision-sensor path.

If anchor preservation matters (rare — e.g., quoting an exact regulatory wording), keep the anchor on the single claim where it's essential.

### Adversarial defense detail

Essay surfaces and disarms the strongest objection (Phase 1 thesis-spine adversarial_defense). Promo doesn't enumerate the objection-mitigation pair; it presents the thesis as already-defended.

Essay:
> A critical reader might ask whether the 70ms claim survives Bosch's 10ms baseline. §3 shows the comparison is apples-to-apples — both measure pre-deployment decision latency.

Promo:
> The 70ms gap sits against Bosch's 10ms accelerometer baseline — apples to apples.

## What to drop entirely

- **Section transitions** ("Recall §2's mechanism…").
- **Cross-references** to other essays SETI has written.
- **Methodology asides** (how the analysis was done — patent reading methodology, web search methodology).
- **Quote anchor IDs** (q-0024-1 style — internal artifact).
- **Voice canon entry IDs** (`closing-aphoristic-landing-...` style — internal artifact).

## What to preserve as-is

- **Every numeric value** — but with units fully spelled or clarified ("milliseconds" not "ms" on first use).
- **Company names** — same spelling, same casing as essay.
- **Patent numbers** — same format (US 2026/0125022 A1).
- **Quoted statements** — verbatim from essay, which is verbatim from invention-summary, which is verbatim from patent.
- **Closing emoji 🤔** — signature, do not omit or substitute.

## Reader-test pass

After drafting, read the promo as if you've never seen the essay. Three questions:

1. What is the patent about?
2. Why does this matter?
3. What's SETI's reading of it?

If any answer requires the essay to make sense → promo is failing self-contained finishability. Compress or restructure.
