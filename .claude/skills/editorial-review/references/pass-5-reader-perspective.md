# Pass 5 — Reader perspective + paragraph readability

Three sub-passes focused on the reader's experience moving through the essay.

## 5A — Engagement curve

For each section, judge the reader's likely engagement:

- **Lead**: hook lands within first 3 sentences. Reader knows what's at stake.
- **Mid-sections**: density doesn't accumulate without payoff. Reader gets a turning-point or new evidence layer every 3-5 paragraphs.
- **Closing**: tension resolves. Reader leaves with a single landing.

Failures:

| Failure | Description | Severity |
|---|---|---|
| Slow lead | Hook doesn't land until §1 paragraph 4+ | medium |
| Density wall | 3+ consecutive paragraphs of patent-mechanism detail without surface | high |
| Lost stake | Reader can't recall why the thesis matters by §3 | high |
| Wandering closing | Closing lands on a new claim instead of the thesis | high |

## 5B — Stake clarity

Reader should be able to answer "why does this matter?" at three points:

1. After the lead.
2. At each section boundary.
3. At the closing.

If the answer requires re-reading earlier paragraphs, stake clarity is broken.

Test: read the closing paragraph in isolation. Does it make sense without §1? If no, the lead and closing aren't bookended properly.

## 5C — Mobile rendering line count

X Articles renders on mobile. Long paragraphs become walls of text on a 6" screen.

- Target: ≤ 5 lines per paragraph on iPhone-class mobile (12-15 words per line in X Articles' typography).
- Failure: paragraph renders > 8 lines on mobile.

Detection (heuristic):
- Count words per paragraph.
- Divide by 12 (mobile line word-count).
- Flag if result > 8 lines.

Long paragraphs that are otherwise clean (no Pass 2 redundancy) may still need split for mobile.

## Severity calibration per posture

| Sub-check | aggressive | measured | conservative |
|---|---|---|---|
| 5A slow lead | medium | medium | high |
| 5A density wall | high | high | high |
| 5A lost stake | high | high | high |
| 5A wandering closing | high | high | high |
| 5B stake clarity broken | high | high | high |
| 5C paragraph > 8 mobile lines | medium | medium | high |

## Output finding template

```yaml
- pass: pass-5-reader-perspective
  location: §2, paragraphs 3-5
  severity: high
  severity_under_default_posture: high
  finding: |
    Three consecutive paragraphs describe the vision-sensor → controller pipeline
    in mechanism detail. By paragraph 5, the reader has lost track of why the
    70ms claim matters relative to industry baseline.
  recommendation: |
    Insert a 2-sentence anchor after paragraph 3 that restates the stake
    ("This is what makes the 70ms claim non-trivial — without the vision
    path, the system can't see the collision before it begins").
```

## Cross-pass interactions

- Pass 5A density wall often correlates with Pass 2 paragraph word-count earn failures.
- Pass 5B stake clarity correlates with Pass 4C thesis arc coherence.
- Pass 5C mobile rendering correlates with Pass 2C paragraph word count.

## Reader profile assumption

The binding profile is `_shared/references/reader-profile.md`: a curious retail investor,
technical comprehension between advanced high school and early undergraduate, reading for the
investment thread. A per-run override may appear in `input/essay-context.md` (e.g. an
analyst-audience wire edition); absent one, the shared profile binds.

This shapes Pass 5 judgment:

- Domain literacy: high on company narratives, LOW on patent-claim mechanics, low on
  filing-process detail. Claim mechanics need the translate-then-quote treatment and a
  one-clause gloss per term of art (profile rules 1 and 3); flag unglossed terms.
- Quantitative claims need a familiar-scale comparison when magnitude carries the point
  (profile rule 2); flag naked magnitudes the reader can't weigh.
- Filing-process detail (continuation chains, prosecution history) needs full unpacking.
- Company-narrative friction needs zero unpacking (high literacy).
- The money thread is structural (profile rule 4): a section that never feeds the verdict is
  a 5B stake-clarity finding even when technically flawless.
