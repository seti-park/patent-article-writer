---
pass: pass-7-adversarial-reader
persona: impatient-investor
round: 2 (confirm-dryness)
draft_version_reviewed: 5
reviewer_isolation: fresh instance, blind to other readers and prior rounds
verdict: DRY at medium+ (no high, no medium findings); 3 low/observational notes recorded
---

# Self-audit round 2 — persona: impatient investor (busy retail investor; wants payoff fast, distrusts hype/filler)

Reader profile: technical comprehension advanced-high-school → early-undergraduate. Read the
whole essay in one pass as this reader, then ran the pass-7 checklist evidence-forced, plus
the two round-1 edits (FIG. 4 header caption; §2 block-floating-point sentence) and grounding
spot-checks over five sections.

## Round-1 edit verification (did the reader experience improve?)

### FIG. 4 header caption (the essay's first text after the H1 title)
- **Improved: YES.** The caption now reads: *"FIG. 4: the align-once core as a functional
  block diagram [0138]. After multiplication, every product is shifted onto one shared scale,
  then an adder tree sums the aligned results as plain integers [0011]. This is claim 1's
  align-then-integer-accumulate step, drawn as data flow."* Numerals are deferred (no INT35/
  INT5/FP22 spec-sheet dump), the drawing type reads as a block/data-flow diagram, and the
  second sentence delivers the plain-English mechanism payoff. It is no longer a spec sheet.
- Cushioned by the H1 title *"OpenAI's Chip Patent Does Floating-Point Math on Integer Adders"*
  (63 chars, SURF-001 pass) which is the true first text and is a strong plain hook.
- Residual (LOW, observational — no change required): the caption opens on three back-to-back
  terms-of-art ("mantissa-alignment" alt text / "functional block diagram" / "adder-tree")
  before the plain payoff lands in sentence two. Acceptable given the title precedes it and the
  payoff is one clause away. Fix if ever touched: tighten "the align-once core as a functional
  block diagram" → "the align-once core [0138]". Not a finding.

### §2 block-floating-point sentence
- **Reads clearly with payoff: YES.** *"One alignment, one integer sum, one conversion back:
  that arithmetic is block floating point [0141], a shared-scale style older than this filing,
  so the trick itself is not OpenAI's invention. What the claim seeks to own is the
  compute-in-memory circuit that executes it inside the array [0011]."* The term "block
  floating point" is appositive-glossed in-line ("a shared-scale style older than this filing")
  and the sentence resolves its own concession ("the trick itself is not OpenAI's invention" →
  "What the claim seeks to own is the compute-in-memory circuit"). It is a signpost, not a
  deep-dive, and it earns its keep by scaffolding the §3 steelman. Not confusing, has payoff.
- Cross-persona note (LOW): the "not OpenAI's invention / the claim owns the circuit" concession
  is now previewed here in §2 and then made at full length in §3. For the investor persona this
  reads as helpful setup and self-resolves in one sentence, so no over-hedge. Flagged only so a
  skeptic-persona reviewer can weigh whether the concession is lightly double-spent. Not a
  finding at this persona.

## Pass-7 checklist (evidence-forced)

| # | Check | Verdict | Evidence | Severity |
|---|---|---|---|---|
| 1 | Hook / lead energy | PASS | ¶1 declarative: "There is a published OpenAI patent that designs an AI chip down to the individual memory cell." Two-sided call lands by §1 end: "The filing is primary evidence that 'OpenAI-designed' is literal... It is also a pending application... which prices the evidence without changing what it shows." | — |
| 2 | Header-as-claim | PASS | All six `##` headers are assertions; header-only skim reconstructs the argument (on file before news → multiply FP, add integers, convert once → headline features described / circuits claimed → result every cycle → pending at tape-out depth → literal engineering, two dates). | — |
| 3 | Steelman present + not overweight | PASS | Specific THIS-patent concession: "the format agility that leads the document's pitch is description material... block-scaled arithmetic is established practice, standardized a year before this filing's priority date. A skeptic can fairly call the core a known technique, implemented." Affirmative core carries >= attention (2 rebuttal ¶: "The claim set answers with specificity rather than breadth..." + "That is the distinction the skeptical read misses..."). Net-new beat, no spend/procedure motif. | — |
| 4 | No meta posturing | PASS (low note) | Only borderline: "The bounds priced in the previous section scope that call, and they do not reverse it." — a functional scope cross-reference (exempt under check 4), not a reader-instruction. | LOW |
| 5 | Jargon as signpost | PASS (low note) | Terms-of-art glossed in-line (activations, weights/stationary operand, primitive product, block floating point, VMM). Densest passage line 44: "the largest exponent any product can carry is 22, which fits in a 5-bit integer [0199]... hands out a 35-bit integer plus that 5-bit exponent [0145]... converts the result to FP22". Supports the stated insight ("The numbers stay small by design") and does not deep-dive past it. | LOW |
| 6 | No stub / rhythm break | PASS | No section markedly shorter than siblings; §1 is two substantial paragraphs, all others 3-6. | — |
| 7 | Thesis not over-restated | PASS | Core verdict asserted in ~2 sections (§1 ¶2 + §6 close) plus title; within ≤3. Signature close "the record is the harder document to argue with" not echoed elsewhere. | — |

## Verdict firmness / over-hedge (goal-4, symmetric)

- **Firm, not over-hedged: PASS.** §6 lands declarative: *"'OpenAI-designed' is literal
  engineering, and this filing is the primary evidence... The announcement is from October
  2025. The engineering is dated November 2024."* One patent-specific anti-hype guard (not
  boilerplate): *"nothing connects these circuits to Jalapeño... and no source shows this macro
  running in silicon."* Verdict explicitly refuses to let caveats reverse it: *"The bounds
  priced in the previous section scope that call, and they do not reverse it."* and *"which
  prices the evidence without changing what it shows."*
- **Repeatable sentence: PRESENT.** *"The chip story was told in 2025. The design record says
  the work started earlier, and the record is the harder document to argue with."* Crisp,
  portable, matches the title. An investor leaves armed.
- No safe-harbor boilerplate ("patents don't guarantee products/stock") anywhere. The pending
  and inventor-history caveats are factual/labeled, not verdict hedges.

## Grounding spot-checks (anchors vs input/patent.md; claim-scope vs Claim scope map)

Checked every `[dddd]` anchor in 5 sections (FIG. 4 header + §1; §2; §3; §4 double-buffering;
§5 tape-out-depth). All resolve to the cited paragraph:

- [0138] FIG. 4 = "exemplary functional block for mantissa alignment 3880... process flow and
  data flow" ✓ · [0011] = claim triad, verbatim quotes at lines 36-38 match ✓ · [0133] =
  "computations... directly performed within a memory array... reducing the von Neumann
  bottleneck" ✓
- [0142] input buffer / streaming operand ✓ · [0130] streaming FP8/6/4, stationary FP6/4 ✓ ·
  [0145] INT35+INT5 → FP22 dequant, scale factor fused ✓ · [0006] mode decoding / no separate
  conversion pipelines ✓ · [0139] "synthesizable (or custom) adder tree... integer domain" ✓ ·
  [0141] "MX format is a type of Block Floating Point (BFP)... shared scaling factor" ✓ ·
  [0199] Emax=22 for FP8×FP6 = INT5 ✓ · [0200] shift = Emax − exponent ✓ · [0104] "consistent
  scale... crucial for maintaining accuracy" ✓
- [0202] shift register bits = Emax + mantissa bits ✓ · [0206] logarithmic multiplexer tree ✓ ·
  [0183] adders saved (per invention-summary quote table) ✓
- [0004] matrix-vector/matrix-matrix multiplications dominate inference/training ✓ · [0147]
  "pipelined fashion, returning a VMM product... every cycle" ✓ · [0154] "256 VMM operations"
  and "100% utilization... may be possible" ✓ · [0012]/[0015] double-bitcell parallel
  write+compute / "minimize compute stalls during updates" ✓
- [0234] setup-time relations ✓ · [0262] "check timing and margin... across many processes,
  voltages and temperatures (PVTs)" ✓ · [0289] "two non-overlapping clock signals" ✓ · [0118]
  "serve both compute storage and scan-test roles" ✓

Claim-scope integrity (vs Claim scope map, all pins = none):
- Independent claims consistently framed as **sought** ("seek to protect", "seek the
  multiply-align-add triad", "the claim seeks to own", "what examination leaves of claims 1,
  20, and 29 will fix how much... OpenAI ends up owning"). No granted-scope overreach. ✓
- Description-only material correctly labeled OPEN, not claimed: format agility / mode decoding
  ("description material"), MX block format ("established practice"), double-bitcell buffering
  ("in its summary passages rather than in the claims it is seeking"), scan/test reuse. ✓
- Claim 20 (shift calculation + select decoding unit folded in) and claim 29 (shift register
  folded in) attributions match the map; dependent-claim specifics (shift-register sizing rule
  [0202], log-mux tree [0206]) correctly attributed to "The dependent claims." ✓
- No pinned value described as a bound (map lists no pins; block size 32, Emax 22, INT35/INT5,
  FP22 all presented as example/description values, not claim limits). ✓

## Conclusion

For the impatient-investor persona, draft_version 5 is **DRY at medium+ severity**: no high,
no medium findings. Round-1 edits both improved the reader experience (caption de-spec-sheeted;
block-floating-point sentence clear with payoff). Three LOW/observational notes recorded above
(caption jargon lead; §2 densest numeric paragraph; §2/§3 lightly double-spent concession);
none require a change and none authorize any hedge. Grounding solid across five sections;
claim-scope locked/open honored; verdict firm with a repeatable takeaway.
