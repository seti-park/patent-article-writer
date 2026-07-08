# Pass 2 — Redundancy + compression

Three sub-checks. All apply across all postures; severity calibration varies.

## Sub-check 2A — Claim repetition

A claim stated once is the standard. Re-stating the same claim across sections (with slightly different wording) inflates word count without adding information.

Detection:
- Identify each factual or thesis claim in the draft.
- For each, list every appearance (section + paragraph + sentence index).
- Flag any claim that appears in 3+ locations as candidate redundancy.

Acceptable repetition:
- Lead → thesis recap in closing (the closing should circle back).
- Cross-section thread bridges ("Recall §2's mechanism…") — only when the bridge genuinely re-anchors a long arc.

Unacceptable repetition:
- Same numeric value cited in 3+ places ("70 milliseconds" in §1, §2, §3) without new context.
- Same patent claim restated without new evidence layer.
- Closing that restates §1 verbatim instead of synthesizing.

## Sub-check 2B — Sentence tightening

Find sentences that can be cut by ≥ 25% without losing information.

Common culprits:
- "It is the case that …" → drop, use direct.
- "In order to" → "to".
- "There exists a relationship between X and Y" → "X relates to Y" or describe the relationship directly.
- Adverbial filler — "essentially", "fundamentally", "ultimately", "actually" (usually droppable).
- Hedge stacking — "approximately about roughly" (pick one).

## Sub-check 2C — Paragraph word-count earn

Each paragraph earns its length by carrying ≥ 1 distinct idea or transition. Paragraphs >150 words that carry 1 idea probably contain ≥ 2 ideas tangled together (split) or 1 idea inflated (compress).

Detection:
- For each paragraph > 150 words, identify the spine idea.
- If the paragraph contains ≥ 2 distinct ideas → flag for split.
- If 1 idea → flag for compression target.

Genre-specific paragraph length (from `deliverable-voice-rules.md`):
- Essay: 3-7 sentences.
- Wire: 2-4 sentences.
- Promo: 2-3 sentences.

8+ sentence paragraphs in essay: high severity flag.

## Severity calibration per posture

| Sub-check | aggressive | measured | conservative |
|---|---|---|---|
| 2A claim repetition (3+ occurrences) | medium | medium | high |
| 2A acceptable bridge | low | low | low (still flag for awareness) |
| 2B sentence ≥ 25% cuttable | medium | medium | high |
| 2C paragraph ≥ 8 sentences | high | high | high |
| 2C paragraph 150+ words single-idea | medium | medium | high |

## Output finding template

```yaml
- pass: pass-2-redundancy
  location: §2, paragraph 3 — and §4, paragraph 1
  severity: medium
  severity_under_default_posture: medium
  finding: |
    "70-millisecond claim" repeated in §2 §4 §5 with no new evidence layer.
  recommendation: |
    Cut §4's restatement (a passing reference suffices). Keep §2's primary
    statement and §5's thesis recap.
```

## Cross-pass interaction

- Compression that improves Pass 2 sometimes degrades Pass 1 cadence (clipped sentences). Reviewer notes when trade-off exists.
- Repetition that survives Pass 2 may indicate Pass 4 (logical alignment) issue — thesis trying to be made true by re-assertion. Flag for cross-pass.
