---
name: promo-composer
description: "Composes 3-5 paragraph promotional digests (~280-340 words, ALL-CAPS title, FT/Economist-style restrained voice) for X platform from a finalized essay (handoff/03-edit/essay-final.md). Trust-driven not engagement-driven. Audience shifts from essay's investor/analyst readership to general X public — voice register adjusts accordingly. Use when essay-final.md lands in Phase 4 Promote Project and user asks for promo, digest, X post, or share copy. NOT for: long-form essay composition (Phase 2 essay-en-composer), wire-style rapid analysis (v1 patent-wire — dropped), Korean adaptation (v1 tech-essay-ko-pub — dropped), editorial review (Phase 3 editorial-review)."
---

# promo-composer

Phase 4 Promote's composition stage. 3-5 paragraph digest for X platform.

```
handoff/03-edit/essay-final.md
    + figures/ (carried through from Layer 1 + Phase 1)
    + Phase 4 Knowledge: voice-profile, deliverable-voice-rules, anti-ai-writing, working-dialogue-voice
    → 3-5 paragraph digest
    → strip pipeline
    → handoff/04-promote/promotion-post.md (X paste-ready)
```

Voice register shifts from essay's investor/analyst frame to X's general public frame — without losing the trust-driven posture.

## When to invoke

After `handoff/03-edit/essay-final.md` lands and user asks for promo, digest, X post, or share copy. The essay is FINAL — promo never modifies the essay; it digests.

## vs essay-en-composer

- `essay-en-composer`: long-form 분석 (~2,000-3,500w), full backup evidence, investor/analyst audience.
- `promo-composer`: digest 격 (~280-340w), trust-driven, FT/Economist editor-curated style. Self-contained finishability with essay as backup evidence. General X public audience.

v1 also had `patent-wire` (rapid wire-style analysis). v2 drops wire — only essay + promo remain.

## Inputs

- `handoff/03-edit/essay-final.md` (FINAL essay — never modified by this skill).
- `figures/fig-NN.png` (carried through from Layer 1; promo may attach 1-2 figures per `references/figure-attachment-policy.md`).
- Phase 4 Project Knowledge: `voice-profile.md`, `deliverable-voice-rules.md`, `anti-ai-writing.md`, `working-dialogue-voice.md`.
- Optional: SETI's additional context (시의성 event, external mention).

## Process

1. **Audience adapt** — read essay-final, identify what survives the audience shift. See `references/audience-adaptation.md`.
2. **Voice shift** — calibrate from essay register to digest register. See `references/voice-shift-from-essay.md`.
3. **Title compose** — ALL-CAPS, 12-16 words, self-contained. See `references/promo-format.md`.
4. **Lede compose** — declarative news statement; first sentence carries thesis. See `references/promo-format.md`.
5. **3-5 paragraph build** — §1 Lede / §2 Patent mechanism + thesis / §3 Implication / [§4 optional secondary patent or supporting evidence] / §N Closing. See `references/promo-format.md`.
6. **Closing posture** — pick one of 4 closing tones (담담 observation / forward pointer / binary test / aphoristic). See `references/closing-posture.md`.
7. **Fact verification** — every claim must backup in essay-final.md. Sub-rules 1/2/3 for 시점 / sequence / quote anchor. See `references/fact-verification.md`.
8. **Figure selection** — 1-2 figures if any, per `references/figure-attachment-policy.md`. Layer 1 cleaned PNGs only.
9. **Strip pipeline** — `promo-draft.md` (with Verification Status header) → `promotion-post.md` (clean X-paste body).

## Pre/post conditions

Pre:
- `handoff/03-edit/essay-final.md` exists and is FINAL (no further essay edits expected).
- `figures/` accessible.
- Phase 4 Knowledge files loaded (especially `voice-profile.md` for voice register awareness).
- All claims the promo will make have backup in essay-final.

Post:
- `handoff/04-promote/promotion-post.md` is X paste-ready.
- 3-5 paragraphs (brief lock — v1's 6-paragraph spec is superseded).
- Title ALL-CAPS 12-16 words self-contained.
- Word count 280-340.
- Em-dash 0, bold not used, 1 emoji (🤔 at closing only).
- Every fact traces to essay-final.

## Output (short example — lede only)

```
TWO TESLA PATENTS DETAIL THE POWDER FLOW AND ROLLER GAP BEHIND ITS DRY 4680 LINE

Tesla published two patent applications on April 30, 2026 that, read together,
describe the dry electrode mechanism behind the 4680 cell line announced at
Q1 earnings.
```

Full structure + final checklist → `references/promo-format.md`.

## Out of scope

- Long-form essay (`essay-en-composer`).
- Korean adaptation (v1 `tech-essay-ko-pub` — dropped).
- Wire-style rapid analysis (v1 `patent-wire` — dropped).
- Editorial review (Phase 3 `editorial-review`).
- Modifying essay-final.md (FINAL is FINAL).
- 1차 source fact verification (handled in Phase 1 fact-check-log + Phase 3 Pass 3).

## References

- `references/promo-format.md` — 3-5 paragraph structure (adapted from v1's 6-paragraph spec), title format, lede pattern, sentence/paragraph rules, Final Checklist, strip pipeline.
- `references/closing-posture.md` — 4 closing posture taxonomy (carry-over from v1).
- `references/audience-adaptation.md` — essay audience → general public on X (NEW for v2).
- `references/voice-shift-from-essay.md` — voice register adjustment (NEW for v2).
- `references/fact-verification.md` — essay backup discipline + Sub-rules 1/2/3 (carry-over from v1).
- `references/figure-attachment-policy.md` — promo figure attachment (1-2 figures, Layer 1 cleaned default).
