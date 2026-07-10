# Vendored third-party skills

These skills are bundled (vendored) from upstream open-source projects. Each retains its
own LICENSE.

> **Absorbed, not run.** The well-researched content of both vendored skills has been
> **absorbed into `_shared/references/anti-ai-writing.md`** (the AI-vocabulary list, copula
> avoidance, transition-word fingerprint, hedging/filler, punctuation tells). They are kept
> here **for reference only** and are **NOT invoked in the runtime loop**: a generic detector
> fights the Owner's own voice and causes drift. Naturalness (north-star goal 4b) is enforced by
> the Owner's canon — `anti-ai-writing.md` (judgment, editorial Pass 1) + `gate_banned.py` /
> `gate_emdash.py` (mechanical) + voice-on drafting + strip-pipeline.

| Dir | Upstream | License | Role now | Notes |
|-----|----------|---------|----------|-------|
| `ai-check/`  | [harshaneel/humanize](https://github.com/harshaneel/humanize) (`ai-check`) | MIT | **Reference only — absorbed.** Its 9 signals (esp. transition-word + punctuation fingerprint) live in `anti-ai-writing.md` Tier 2. | Not run in the loop. |
| `humanizer/` | [blader/humanizer](https://github.com/blader/humanizer) | MIT | **Reference only — absorbed.** Its AI-vocabulary, copula-avoidance, hedging/filler lists live in `anti-ai-writing.md`. | Not run in the loop; rewrite passes fight the Owner's voice. |

## How the meta-loop keeps this current

You don't re-pull these to update behavior. The `pipeline-retro` meta-loop watches for
recurring AI tells in real essays and proposes additions to `anti-ai-writing.md` (and, when
mechanically safe, to `banned_terms.txt`). To refresh from upstream for reference, re-copy the
upstream `SKILL.md` + `LICENSE` here, then absorb any genuinely new signal into the canon by
hand — never wire these back into the runtime path.

## Alternatives considered

Other MIT-licensed scoring-capable humanizers if you ever want to swap `ai-check`:
[gregorymm/humanize-text](https://github.com/gregorymm/humanize-text) (7 categories, 1–10),
[Aboudjem/humanizer-skill](https://github.com/Aboudjem/humanizer-skill) (43 patterns, 0–100).
