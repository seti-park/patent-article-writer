# Voice shift from essay to promo

Essay register is analytical restraint. Promo register is editor-curated digest. The shift is in cadence, attribution density, and emoji discipline — NOT in the underlying voice.

See `voice-profile.md` (Phase 4 Knowledge) for SETI's full voice definition. This file covers the register-specific adjustments.

## What stays the same

- **Honesty discipline** — no puffery, no "remarkable / extraordinary / unprecedented".
- **Specificity over abstraction** — concrete dates, numbers, names.
- **Banned word list** (`anti-ai-writing.md`) — applies fully.
- **Em dash forbidden** in title and body.
- **Single closing emoji 🤔** at essay/promo end (signature).
- **Hedge calibration** — universal claims at hard tier zero, "significantly" type modifiers zero.

## What shifts

### Cadence

Essay: paragraph 3-7 sentences, sentence up to 35 words but often 20-25.

Promo: paragraph 1-3 sentences, sentence cap 35 words but typically 15-25. Closing sentences 15-25 words (tighter).

The shift creates the digest feel — faster, denser per word.

### Attribution density

Essay: every patent claim cites `[XXXX]`. Every external claim cites source in `# Sources` block.

Promo: 핵심 인용만 명시 (압축 가능). The reader doesn't see a `# Sources` block — promo is self-contained.

- Patent paragraph anchors `[XXXX]`: drop unless the anchor itself is the point.
- External sources: name the source in-prose ("per Bosch's spec sheet") if essential, otherwise drop the attribution and rely on essay backup.

### Markdown weight

Essay: `## §N` section headers, inline `**bold**` thesis anchors, `*italic*` captions.

Promo:
- **No section headers** — only the ALL-CAPS title.
- **No bold** — digest restraint.
- **No italic captions** — figure captions, if used, are plain text on a separate line.

### Voice pattern selection

Essay's voice canon access is full (all 14 categories). Promo's canon access is constrained:

- Opening: `opening-news-event` is the default (declarative lede). Other opening patterns rarely fit promo's compressed lede.
- Closing: 4 closing patterns are all available, picked per `references/closing-posture.md`.
- Inline-bold-thesis-anchor: NOT used in promo (no bold).
- Korean sig-ko-* patterns: NOT used in promo (English only).

### Sentence-level register

Essay can use rhetorical questions, parenthetical asides, em-of-the-fact-of-the-matter constructions.

Promo strips these. Each sentence is a statement of fact or a clean implication. No rhetorical question except as the closing posture (and that's still understated, not "Is this not remarkable?").

## Example pair

### Essay

> Tesla's patent grant predates the May announcement by eleven months. The architectural decision was complete; the announcement was vindication packaging. **The vision-sensor path is the patent's claim 1 (b), not a press-release embellishment.** [0016]

### Promo

> Tesla's patent granted eleven months before the May announcement. The architectural decision was complete; the announcement was vindication. The vision-sensor path sits in claim 1 (b), not in press copy.

Differences:
- Essay's bold thesis anchor → promo's plain sentence (still load-bearing, but no bold).
- Essay's `[0016]` → promo drops (reader doesn't have invention-summary).
- Essay's "embellishment" → promo's "press copy" (slightly tighter, same meaning).
- Three sentences in both; same cadence, different anchor density.

## Voice consistency anchor

Both essay and promo must read like SETI wrote them. If a reader could open the promo without knowing it's promo and confuse it for "some other writer's compression of SETI's essay", the voice shift went too far.

Test: pick a sentence at random from the promo. Compare to a sentence at random from `voice-canon/opening-news-event-*.md` (one of the 5 carry-over entries). The sentence-level cadence and word choice should be siblings.
