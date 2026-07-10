# Polish notes (Phase 3.7 윤문)

- **origin**: polish
- **target**: `handoff/03-edit/essay-final.md` (synced to `handoff/02-compose/essay-draft.md`; `publication.md` re-stripped)
- **draft_version**: 5 → 6
- **jurisdiction**: surface-only. No fact, number, date, name, `[dddd]` anchor, blockquote,
  signature line, verb of certainty, stance, section order, or Sources block altered.
- **edits logged**: 5 (2 priority-targeted, 3 sweep splits)

Every edit below is a `## polish` block (before / after / why-plainer). Gate re-run and
drift verification are recorded at the bottom.

---

## polish 1 — §1 lead, "bitcell" first-use gloss (IABI-01)

**before**
> Eleven months before OpenAI announced its own chip, the math engine was already on file, written to the bitcell.

**after**
> Eleven months before OpenAI announced its own chip, the math engine was already on file, written to the bitcell, the circuit that stores a single bit.

**why-plainer**: "bitcell" is a term of art that lands cold on first use here (it is only
implicitly explained later in §4/§5). Added a one-clause appositive gloss so the general
reader is not lost. The gloss is a restatement grounded in the essay's own language — §5 calls
them "latch-level bitcell circuits" (bitcell = a circuit) and §4 has "memory cells built from
two bitcells each" (each stores one bit). Comma appositive, not an em-dash (gate_emdash stays
clean). No new factual claim about the patent; nothing else in the punchy lead sentence
changed.

---

## polish 2 — §2, split the 38-word alignment sentence (numeric-cluster neighbor)

**before**
> The macro finds the largest exponent among the 32 products in a block and computes how far each mantissa must shift to sit on that shared scale [0199] [0200], which puts every contribution on a consistent footing before the sum [0104].

**after**
> The macro finds the largest exponent among the 32 products in a block and computes how far each mantissa must shift to sit on that shared scale [0199] [0200]. That puts every contribution on a consistent footing before the sum [0104].

**why-plainer**: one 38-word run split into two shorter sentences right before the numeric
cluster the cold reader glazed on, so the reader arrives at the numbers on firmer footing.
"which puts" → ". That puts" keeps the same referent. Anchors stay with their clauses:
`[0199] [0200]` with the shift/shared-scale clause, `[0104]` with the consistent-footing
clause. (Removes a LONGSENT-001 warn.)

---

## polish 3 — §2, numeric cluster: pace the delivery + plain-language bridge (PRIORITY 1)

**before**
> The numbers stay small by design: for an FP8 activation times an FP6 weight, the largest exponent any product can carry is 22, which fits in a 5-bit integer [0199]. After the shift, the adder tree sums the column and hands out a 35-bit integer plus that 5-bit exponent [0145].

**after**
> The numbers stay small by design. What the adder tree adds up is an ordinary integer, and only a tiny exponent rides along to track the scale. For an FP8 activation times an FP6 weight, the largest exponent any product can carry is 22, which fits in a 5-bit integer [0199]. After the shift, the adder tree sums the column and hands out a 35-bit integer plus that 5-bit exponent [0145].

**why-plainer**: this is the exact spot the self-audit cold reader started skimming on BOTH
rounds — "the 22 / 5-bit / 35-bit / FP22 numbers piled on." Two changes, both surface:
(1) the colon list is split so "The numbers stay small by design" lands as its own beat and
the FP8×FP6 example starts clean; (2) a short plain-language bridge tells the non-engineer why
"small" matters and what to hold onto before the specific numbers arrive — the sum is just an
ordinary integer, with one tiny exponent riding along. The bridge is a grounded restatement,
not a new fact: the integer accumulation is claim 1's own wording ("an adder tree configured
to output an accumulation value ... in an integer format", carried at [0011]) and the "35-bit
integer plus that 5-bit exponent" it foreshadows is the very next sentence [0145]; the exponent
tracking the scale restates the dequantization step that "folds the block's shared scale factor
back in" [0141] [0145]. Every number and anchor is untouched (22, 5-bit, 35-bit, 5-bit
exponent; [0199], [0145]); the decimals-by-hand analogy in the prior paragraph keeps doing its
work.

---

## polish 4 — §4, split the 43-word double-buffer sentence

**before**
> For the replacement itself, the document describes, in its summary passages rather than in the claims it is seeking, memory cells built from two bitcells each, so the next weight matrix loads into one bank while the other bank feeds the ongoing computation [0012].

**after**
> For the replacement itself, the document describes memory cells built from two bitcells each, so the next weight matrix loads into one bank while the other bank feeds the ongoing computation [0012]. It describes this in its summary passages, not in the claims it is seeking.

**why-plainer**: a 43-word sentence with the "in its summary passages rather than in the
claims it is seeking" aside jammed into the middle. Lifting the aside into its own trailing
sentence lets the reader take the double-buffer mechanism first, then the scope note.
"rather than" → "not" is the plain equivalent. The load-bearing described-not-claimed
distinction is preserved word-for-word in meaning; anchor `[0012]` stays with the mechanism
it cites. (Removes a LONGSENT-001 warn.)

---

## polish 5 — §6, split the 36-word "One guard" caveat

**before**
> One guard belongs to this patent specifically: nothing connects these circuits to Jalapeño, the inference chip OpenAI and Broadcom unveiled in June 2026, and no source shows this macro running in silicon (see Sources, Official statements).

**after**
> One guard belongs to this patent specifically. Nothing connects these circuits to Jalapeño, the inference chip OpenAI and Broadcom unveiled in June 2026, and no source shows this macro running in silicon (see Sources, Official statements).

**why-plainer**: pure colon → period split of a 36-word caveat; the flag "One guard belongs
to this patent specifically" now stands on its own before the specifics. Zero content change.
This is the guard sentence, not the verdict call — the firm closing and signature line 2 are
untouched. (Removes a LONGSENT-001 warn; gate_hedge verdict-section checks stay clean.)

---

## Considered and deliberately NOT edited (kept as baseline warns)

- **§2, "The point of the shuffle..." (82-word LONGSENT-001)** — the count is inflated because
  the inline **bold signature line** breaks the sentence splitter; smoothing it would require
  touching the byte-protected signature line "Align once, and the whole accumulation becomes
  integer arithmetic." Left as-is.
- **§5, "One name carries press-reported history: Bloomberg..." (44-word LONGSENT-001)** — a
  fact-dense biographical sentence (June 2024, seventeen years, Apple, Rain AI). A clean
  all-under-35 split needs reordering that risks a temporal-meaning shift and could introduce a
  spend-motif token ("spent") that would wake SURF-006. Not worth the drift risk; left as-is.
- **§6, "\"OpenAI-designed\" is literal engineering..." (41-word LONGSENT-001)** — the closing
  verdict lead. Any split risks equating "this filing" with "the engine" (the filing documents
  the engine); firm-verdict sensitivity outweighs the readability gain. Left as-is.

---

## Gate re-run (zero new findings)

Command: `run_gates.py --draft essay-final.md --invention-summary ... --figures ...
--figure-selection ... --patent input/patent.md`

- **OVERALL: PASS** (0 fail), before and after.
- Warn delta: baseline 9 warns → post-polish 6 warns. LONGSENT-001 dropped from 6 to 3
  (the 38-word §2, 43-word §4, and 36-word §6 sentences I split are gone). The 6 remaining
  warns (STRUCT-004 ×1, DUPE-001 ×2, LONGSENT-001 ×3: the 82/44/41-word sentences above) are
  **byte-identical to baseline findings** — same check_id, message, and location.
- **NEW findings introduced by polish: 0** (warns included). No edit woke a gate; no revert.

## Drift verification (grounding-verifier-class, changed sentences old-vs-new)

Mechanical protected-surface diff (pre-polish vs post-polish `essay-final.md`):
- `[dddd]` anchors: 53 → 53, identical multiset. PASS
- Verbatim blockquote lines: 7 → 7, identical. PASS
- `# Sources` block: identical. PASS
- Body numeric / bit-width tokens (FP8/FP6/FP4/FP22, 22, 5-bit, 35-bit, 256, 32×32, 64, 32):
  identical multiset. PASS  (the only whole-file token delta is `draft_version` 5→6.)
- Signature lines 1 and 2: byte-present in the polished file. PASS

Semantic pass on the 5 changed passages (meaning preserved, no protected surface touched,
no stance/certainty change):
- polish 1 (bitcell gloss): MEANING-PRESERVED — appositive definition, grounded restatement.
- polish 2 (alignment split): MEANING-PRESERVED — sentence split, same referent.
- polish 3 (numeric cluster): MEANING-PRESERVED — split + grounded bridge; all numbers/anchors intact.
- polish 4 (double-buffer split): MEANING-PRESERVED — described-not-claimed scope note preserved.
- polish 5 (guard split): MEANING-PRESERVED — pure split, verdict untouched.

No `MEANING-CHANGED` and no `PROTECTED-TOUCHED` verdict. **Reverts: none.**

## Publication re-strip

`strip_publication.py handoff/02-compose/essay-draft.md -o handoff/02-compose/publication.md`
re-run after the sync; `essay-final.md` and `essay-draft.md` are byte-identical.
