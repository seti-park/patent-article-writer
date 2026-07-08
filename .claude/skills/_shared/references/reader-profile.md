# Reader profile — the target audience, as a first-class contract

Single source of truth for WHO the essay is written for. The composer drafts to it, pass-5
reviews against it, pass-7's "impatient investor" persona instantiates it, and the self-audit
readers simulate it. A per-run override may appear in `input/essay-context.md` (e.g. a wire
edition for analysts); absent an override, THIS profile binds.

## The reader

A curious retail investor. Technical comprehension sits **between advanced high school and
early undergraduate**: comfortable with mechanisms explained in words and one diagram, NOT
with equations, claim-language legalese, or unglossed terms of art. They opened the article
because of the company or the stock, not the technology — the investment reading is the
thread that keeps them; the technology is what they leave having understood.

They are smart and skeptical, not expert. Do not condescend; do not assume.

## Reader jobs (what a finished essay does for them)

Comprehension tier says what the reader can process; the jobs say what they came FOR. All
three are load-bearing (goal 5 traces here; surface doctrine in
`_shared/references/reader-energy.md`):

1. **Information job** — what they came to learn: what the patent actually says, and what it
   means for the company or stock that made them open the article.
2. **Feeling job** — they leave ARMED, not lectured: insider knowledge (they read the primary
   document, through you) plus a defensible take they could argue tomorrow.
3. **Social job** — a quotable, repost-safe sentence: something they can say to a friend or
   post without having to check back against the essay.

## The leaving-sentence contract

Every run's `input/essay-context.md` SHOULD carry a `reader_sentence:` field — the one
sentence the reader wants to say to someone after reading. It is the **title brief and the
lead's design target**: Phase 1 writes its title-lead candidates against it, the composer's
¶1 aims at it, and the declared signature lines are usually it or its close siblings. If the
field is absent, Phase 1 drafts one at the top of `title-lead-candidates.md` for the
orchestrator to confirm.

## Calibration rules

1. **Jargon budget.** Every term of art gets a one-clause gloss on first use ("a method
   claim — protection on performing the steps, not on the machine itself"), then is used
   freely. A term glossed is a signpost; a term deep-dived past the insight is pass-7's
   `jargon-overdepth`.
2. **Numbers land on a familiar scale.** A quantitative claim gets one comparison the reader
   already owns ("70 ms — about a third of an eye-blink") when the magnitude carries the
   point. Source values stay verbatim; the comparison is clearly the essay's.
3. **Claim language: translate, then quote.** Lead with the plain-English meaning, then give
   the verbatim claim text its blockquote. Never make the reader parse "wherein said member"
   unassisted — and never alter the verbatim quote itself (Pass 3 binds).
4. **The money thread is structural.** Every section earns its place by feeding the verdict
   the investor came for. A mechanism section that never connects back to "why this moves
   the thesis" is a pass-5 finding even if technically flawless.
5. **No prerequisite chains.** A paragraph may introduce at most one new concept that later
   paragraphs depend on. If understanding §4 requires holding three §2 definitions, the
   structure — not the reader — is wrong.
6. **Precision beats simplification when they conflict** — but the fix is a better gloss or
   a narrower sentence, never a distortion. If a simplification would misstate the claim
   scope, keep the precise statement and gloss it.

## What this profile does NOT license

- Dumbing down the verdict (6G still requires an evidence-proportionate call).
- Cutting the verbatim quote chain (anchors + quotes are the trust spine; the gloss sits
  NEXT to the quote, not instead of it).
- Hype. Accessible and firm is the register; breathless is `gate_banned`/anti-AI territory.
