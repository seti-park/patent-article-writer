# Cold reader — round 2 (casual scroller, one read)

First-reaction only. Not a review.

**(a) Where did I stop / start skimming?**

I started skimming here:

> "The numbers stay small by design: for an FP8 activation times an FP6 weight, the largest exponent any product can carry is 22, which fits in a 5-bit integer [0199]. After the shift, the adder tree sums the column and hands out a 35-bit integer plus that 5-bit exponent [0145]."

That's where my thumb sped up. The decimals-by-hand analogy just before it was clicking, but then the 22 / 5-bit / 35-bit / FP22 numbers piled on and I stopped actually reading them and just slid down. I picked back up at "A Pending Application, Written at Tape-Out Depth" because the Apple-guy sentence caught my eye.

**(b) What did I feel, and where?**

- Top ("The Design Was on File Before It Was News"): curious, a little hooked — the "on file before it was news" angle is a real thing to know.
- Middle (the FP8/mantissa/adder-tree stretch): foggy, "okay I trust you," half-lost. Not bored exactly, just out of my depth and skimming.
- The bracketed [0199]-style codes everywhere: my eye kept snagging on them, felt like reading with speed bumps.
- Bottom third (the ex-Apple hire, the "scan-test" / clock-margin detail, the two dates): re-engaged, mild "huh, that's clever" — the concrete stuff landed better than the math.
- Overall closing: satisfied, "so the point is the timing." Clear enough.

**(c) The one thing I'd repeat to a friend:**

"OpenAI had the actual chip design patented almost a year before they even announced they were making their own chips — like, engineered down to the memory cell, so 'OpenAI-designed' isn't just marketing." That's the sentence I'd say out loud. The floating-point-on-integer-adders trick, which is the headline, is NOT the thing I'd repeat — I couldn't re-explain it.
