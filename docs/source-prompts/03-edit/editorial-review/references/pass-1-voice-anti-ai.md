# Pass 1 — Voice canon + anti-AI compliance

Combines v1 Pass 1 (voice canon compliance) with the banned-pattern grep from `anti-ai-writing.md`. Phase 3 voice fencing applies: this pass uses `deliverable-voice-rules.md` mechanical rules + `anti-ai-writing.md` banned-pattern list, NOT `voice-profile.md`.

## Two sub-passes

### 1A — Voice canon adherence

For each section's voice anchor (declared in essay frontmatter or referenced in `handoff/02-compose/thesis-trace.md`), verify the prose inherits cadence and structure from the canon entry.

- **Cadence**: sentence-length rhythm, paragraph-density rhythm.
- **Structure**: opening pattern (one of 5 categories), closing pattern (one of 4 categories), inline anchor placement.

Compliance is judged against the deliverable voice rules (paragraph 3-7 sentences for essay, 한 문장 한 논리 단계, 인용-해석 동반, 격언조 분포). Voice canon entry IDs declared in Phase 1 thesis-spine and Phase 2 thesis-trace.

### 1B — Anti-AI banned-pattern grep

Mechanical check against `anti-ai-writing.md` lists. These are absolute — no contextual flexibility.

#### Banned words (high severity)

```
delve, tapestry, vibrant, pivotal, crucial,
fostering, underscore, meticulous, intricate, testament,
garner, bolstered, showcase, enhance, enduring,
valuable, boasts, renowned, multifaceted,
leverage, navigate, resonate, nestled, groundbreaking,
interplay,
landscape (추상적 의미 only — 지리적 의미 OK),
additionally (sentence-initial only)
```

Grep each banned word case-insensitive. Each hit = high severity finding.

#### Banned patterns (high severity)

- **not-just-X-but-Y** — "This is not just X, but Y".
- **despite-challenges** — "Despite the challenges..." 형 도입.
- **copula avoidance** — "represents", "constitutes", "serves as" instead of is/are.
- **vague attributions** — "Many experts believe", "It is widely accepted", "Studies show".
- **puffery** — "remarkable", "extraordinary", "unprecedented".
- **section summaries** — "In summary", "To recap" at section end.
- **elegant variation** — same subject called different names in one paragraph (Tesla → the EV maker → the Austin-based company).

#### Banned formatting (medium severity)

- **Triple empty modifiers** — "advanced, sophisticated, cutting-edge".
- **Bold overuse** — 3+ bold spans per paragraph (except `inline-bold-thesis-anchor` device).
- **Bullet overuse** — prose information bullet-fragmented (bullets OK only for true parallel items).
- **Emoji** — body emoji forbidden; only 🤔 at essay end for `closing-open-question` pattern.

## Severity calibration per posture

| Pattern type | aggressive | measured (default) | conservative |
|---|---|---|---|
| Banned word | high | high | high |
| Banned pattern | high | high | high |
| Banned formatting | medium | medium | high |
| Voice canon cadence drift | medium | medium | high |
| Voice canon structural inheritance miss | high | high | high |

Banned items are non-negotiable at all postures. Structural inheritance from canon is always high.

## Output finding template

```yaml
- pass: pass-1-voice-anti-ai
  location: §3, paragraph 2, sentence 4
  severity: high
  severity_under_default_posture: high
  finding: |
    Banned word "delve" appears in "We delve into the mechanism".
  recommendation: |
    Replace with plain verb. Options: "examine", "trace", "look at".
```

## Cross-pass notes

- Cadence findings often co-occur with Pass 2 (redundancy). When both pass 1 cadence and pass 2 redundancy flag the same prose, prefer pass 2's recommendation (compression often resolves cadence drift).
- "Em dash" grep is in Pass 6 (format), not here. Pass 1 covers vocabulary + structural patterns only.
