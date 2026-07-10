# Cold Reader — Round 1 (casual scroller, first reaction)

Read once, phone, half-paying-attention. Honest gut reactions only.

## (a) Where I stopped / started skimming

I read the opening for real. The title ("OpenAI's Chip Patent Does Floating-Point Math on
Integer Adders") plus the first section hook pulled me in — "There is a published OpenAI
patent that designs an AI chip down to the individual memory cell" and the eleven-months
thing landed.

I started skimming here, in the second section:

> "the largest exponent any product can carry is 22, which fits in a 5-bit integer [0199]. After the shift, the adder tree sums the column and hands out a 35-bit integer plus that 5-bit exponent [0145]."

Once the numbers started stacking (FP8/FP6/FP4, mantissa, exponent, 35-bit, FP22, [0199]
[0200] anchors everywhere) my eyes glazed and I scrolled. The decimal-alignment analogy
("line up the points first, then add the digits") snapped me back for a second, but I lost it
again right after.

After that I was skim-reading — jumping headings. I slowed down again only twice: the Apple
engineer line (Jean-Didier Allegrucci, "seventeen years leading SoC engineering at Apple")
and the last two lines of the essay.

## (b) What I felt, and where

- **Curious** — at the top. "OpenAI secretly designed its own chip and it was on file before
  the announcement" is a real hook.
- **Bored / eyes-glazing** — the whole "Multiply in Floating Point, Add as Integers" section.
  Too many numbers and bit-widths back to back. Felt like reading a spec sheet.
- **Mildly lost** — the claims-vs-description section (OCP MX, the company list). I could tell
  it mattered but couldn't hold why.
- **"so what?" flicker** — middle of the essay I kept half-thinking "okay, but does the chip
  exist / work?" It does get answered near the end, but late.
- **Re-hooked / interested** — the ex-Apple engineer detail. That's the one human thing.
- **Satisfied** — the closing ("The chip story was told in 2025. The design record says the
  work started earlier") felt like a clean landing.

## (c) The one thing I'd repeat to a friend

"OpenAI had the actual design for its own AI chip on file almost a year before they announced
it — down to the individual memory cell, so 'OpenAI-designed' isn't marketing, it's literal."

The bracket-heavy, mantissa/exponent middle bit I would not repeat and could not repeat — I'd
just say "and there's some clever math trick to make it cheaper."
