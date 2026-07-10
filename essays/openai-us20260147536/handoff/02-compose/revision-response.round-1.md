# Revision response — round 1

draft_version: 2  <!-- this revision applies the round-1 edit-log findings AND integrates the
                       four figures selected in the now-figure-enabled figure-selection.md -->

## r1-F1

- disposition: applied
- change: Split the dense §2 alignment paragraph at "...before the sum [0104]." into two
  paragraphs. Paragraph A now carries the adding-decimals analogy + what the bit shift does +
  the max-exponent search (3 sentences); paragraph B carries the worked FP8×FP6 example +
  INT35/INT5 output + the FP22 dequantization (3 sentences). No mechanism wording changed;
  each half now renders ~4-5 mobile lines.
- location: §2 (Multiply in Floating Point...), was ¶4, now ¶4 + ¶5

## r1-F2

- disposition: applied
- change: Split §3's densest paragraph (was 7 sentences, ~155 words) after the "64 by 64 half
  adders" sentence. Paragraph A = named-machinery specifics (4 sentences); paragraph B = the
  "MX is a data format / circuits are claimed" distinction + affirmative-core return
  (4 sentences). Also broke the ~48-word triple-clause machinery sentence into two: the first
  states the shift-calculation-and-select-decoding unit (and its claim-20 fold, see r1-F4), the
  second states the register-sizing rule and the log-mux tree. New sentence lengths ~38 and
  ~25 words.
- location: §3 (The Headline Features Are Described...), was ¶3, now ¶3 + ¶4

## r1-F3

- disposition: applied
- change: Reworded the §1 ¶2 instance from "written down to the individual memory cell" to
  "written to the bitcell", so the depth-motif no longer repeats verbatim in adjacent lead
  paragraphs. The §1 ¶1 introduction ("designs an AI chip down to the individual memory cell")
  and the §6 recap ("specified down to the individual memory cell") are preserved as the
  intended lead→closing bookend. Gate DUPE-001 now shows the phrase twice (the bookend), not
  three times.
- location: §1 ¶2

## r1-F4

- disposition: applied
- change: Made the claim-scope statement precise. The rebuilt §3 machinery sentence now states
  that the shift-calculation-and-select-decoding unit "is the one piece independent claim 20
  pulls up into itself, alongside the multiply-align-add triad" — no longer implying it is a
  dependent-claim-only addition. Register-sizing (claim 3) and the log-mux tree (claims 6-9)
  remain correctly grouped as the dependent-only specifics ("The dependent claims add the
  rest"). Consistent with the invention-summary Claim scope map (claim 20 = triad + shift-calc
  unit). No hedge added; this is a precision fix in the safe direction.
- location: §3 ¶3

## r1-F5

- disposition: applied
- change: Narrowed the categorical premise from "Concept filings do not carry clock margins and
  scan modes." to "Concept filings rarely carry clock margins and scan modes." — removes the
  absolute a skeptic could counter while keeping the contrast and the punch. The evidential
  landing ("reads like engineering rather than positioning") is untouched, so the verdict stays
  firm (jurisdiction fence: narrowed the claim, did not caveat the call).
- location: §5

## r1-F6

- disposition: applied
- change: Added "about" to the first instance of the gap figure (§1 ¶1: "on 13 October 2025,
  about eleven months later"), consistent with fact-check-log's "about eleven months" note for
  the 2024-11-22 → 2025-10-13 span. The §1 ¶2 and §6 instances inherit the now-established
  approximation, per the finding's guidance. Not a verdict hedge — a precision fix on date
  arithmetic.
- location: §1 ¶1

## Figure integration (part B — the run became figure-enabled mid-flight)

Not a finding disposition; recorded here so the round-2 reviewer knows what else moved. The
four figures selected in the now-figure-enabled `handoff/01-design/figure-selection.md`
(FIG. 4, 1, 3, 43) were integrated. Placements + captions are recorded in
`figures-rationale.md`; the §-map update is in `thesis-trace.md`.

- **FIG. 4** — header (image-plus-caption, header_composite): the mantissa-alignment /
  adder-tree core; caption walks the shift-calculation block, the two's-complement step, and
  the column adder tree (426) → INT35, tying it to claim 1's (b)+(c). Referenced again in
  §2 ¶4 as the align/accumulate back end.
- **FIG. 1** — §2, after ¶1 (caption-only-italic, medium, `body_figure_carries_unique_info`):
  the one-pass datapath (input buffer, CIM macro 101, mode decoding 110, dequantization 106 →
  FP22).
- **FIG. 3** — §2, after the [0011] claim blockquote (caption-only-italic, short,
  `body_figure_prose_covers_fully`): one column cell, where a primitive product is made.
- **FIG. 43** — §4, after the double-buffering paragraph (caption-only-italic, medium,
  `body_figure_carries_unique_info`): the double-bitcell cell (4303), dual-bank behind the
  double-buffered weight loads.

## Volunteered changes (beyond findings)

1. **Two design-permitted value-add figure cross-references (FIG. 38, FIG. 45).** `gate_figure_use`
   parses figure tokens from ALL prose in `figure-selection.md`, so the "paired-figure
   relationships" discussion of the *unselected* figures ("FIG. 45/46 (scan variants) and
   FIG. 38/42...") makes the gate read FIG. 38 and FIG. 45 as *selected*, and a draft that
   referenced only the four caption-figures orphaned them (FIGUSE-001 fail). Rather than force
   two more placed captions (against the design's tight-count intent) or edit a Phase-1
   artifact out of lane, I added two brief in-prose cross-references that are explicitly
   allowed by figure-selection.md ("may cite any other available figure ... only if it adds
   reader value") and genuinely value-adding: §2 notes FIG. 38 as the physical-layout version
   of FIG. 4's functional block; §5 notes FIG. 45 as one scan-wired double bitcell for the
   scan-test depth point [0118]. Both figures are in the available index. **Upstream flag for
   the orchestrator:** the cleaner fix is for design-architect to reword the unselected-figure
   prose in `figure-selection.md` so those tokens do not parse as selected (e.g. "sheets 45 and
   46", "sheets 38 and 42", dropping the "FIG." token); otherwise every figure-enabled
   recompose reintroduces the same orphan pressure.
2. Split the header FIG. 4 caption into three shorter sentences (was one 74-word sentence) and
   used "outputs" rather than "hands out" in it, to clear a new LONGSENT-001 warn and a new
   DUPE-001 echo with §2's "hands out a 35-bit integer". Warn-only; not required, done to keep
   the round clean.

## Gate self-check (post-revision)

`run_gates.py` OVERALL: **PASS** (0 fails). Warn-only residue: STRUCT-004 (4 content-driven
triads, pre-existing, round-1-assessed), DUPE-001 ×2 (the intended §1→§6 "down to the
individual memory cell" bookend r1-F3 preserved), LONGSENT-001 ×8 (dense but
information-bearing mechanism sentences; the one new split sentence is 38 words, an improvement
on the old 48-word original). Both declared signature lines are byte-identical and each appears
once. em-dash count 0 (all figure-integration em-dashes were converted to house-style
punctuation).
