---
pass: self-audit-round-2
persona: skeptical domain professional (chip/hardware engineer)
draft_version: 5
verdict: DRY on all medium+ axes — round-1 fix (SKPRO-01) confirmed correct
finding_counts: {critical: 0, high: 0, medium: 0, low: 2}
---

# Self-audit round 2 — skeptical domain professional (fresh instance, blind)

Confirm-dryness pass on draft_version 5. Scope: verify the round-1 SKPRO-01 fix landed
correctly and introduced no new problem, then hunt residual technical infidelity /
overreach / over-hedge. Evidence-forced; every item returns {verdict, quoted span or
ABSENT, severity}. Jurisdiction fence honored: no recommendation adds a hedge or disclaimer.

## A. Verification of the round-1 fix (the changed spans)

### A1 — §2 block-floating-point scoping sentence
Verdict: **YES, correctly scoped. No new overreach, no new hedge.**
Span (essay §2):
> "One alignment, one integer sum, one conversion back: that arithmetic is block floating
> point [0141], a shared-scale style older than this filing, so the trick itself is not
> OpenAI's invention. What the claim seeks to own is the compute-in-memory circuit that
> executes it inside the array [0011]."

- "block floating point [0141]" — [0141] verbatim: "A microscale (MX) format is a type of
  Block Floating Point (BFP) data format... MX format employs a shared scaling factor across
  a block of elements." The patent itself names the scheme BFP at this exact paragraph, so
  [0141] is the correct (and the only) anchor for the term. GROUNDED.
- "a shared-scale style older than this filing, so the trick itself is not OpenAI's
  invention" — a concession AGAINST the subject (de-credits OpenAI for the arithmetic style).
  It is not overreach in the subject's favour, and it is not a safe-harbour hedge: it is a
  scope correction that SHARPENS the claim (format = old; circuit = claimed). BFP is a
  decades-old technique and MX (2023) predates the 2024 priority date, so "older than this
  filing" is accurate. No over-hedge.
- "What the claim seeks to own is the compute-in-memory circuit that executes it inside the
  array [0011]" — [0011] is independent-claim-1 language (CIM macro / column cell /
  functional block / adder tree). "seeks to own" matches the Claim scope map's sought-lock
  (pending, not granted) framing. "compute-in-memory circuit" is faithful: claim 1 expressly
  recites a CIM macro, so the CIM limitation is real, not invented. "inside the array" is
  patent-framed by [0133] ("computations (e.g., VMM operations) can be directly performed
  within a memory array"). GROUNDED.
- Foreshadow test: the paragraph ENDS on the affirmative (the circuit is what is claimed),
  with the concession subordinated; §3 then develops the same concession as its dedicated
  concession-first section. Consistent, not contradictory. PASS.

### A2 — FIG. 4 caption drawing-type description
Verdict: **YES, now accurate to the drawing; claims nothing beyond it.**
Span:
> "FIG. 4: the align-once core as a functional block diagram [0138]. After multiplication,
> every product is shifted onto one shared scale, then an adder tree sums the aligned results
> as plain integers [0011]. This is claim 1's align-then-integer-accumulate step, drawn as
> data flow."

- [0138] verbatim: "FIG. 4 illustrates an exemplary functional block for mantissa alignment
  3880... An example of process flow and data flow for mantissa align-ups and accumulation
  of primitive products is also depicted in FIG. 4." So both "functional block diagram" and
  "drawn as data flow" are the patent's own words. GROUNDED.
- Confirmed against the actual image (input/figures/fig-04.png): it shows labelled
  functional boxes (Shift Calculation (EMax-E) 3882, Shift>>+2's Complement 3884, Adder Tree
  426) with data-flow arrows and bus-width labels (5b, INT30, INT35, INT5(22)) for Rows
  0/1/31 — a data-flow block diagram, NOT a transistor-level circuit schematic. The earlier
  mis-description is resolved. PASS.
- "adder tree sums the aligned results as plain integers [0011]" — [0011] claim language:
  "an adder tree configured to output an accumulation value... in an integer format by adding
  the shifted mantissa bits"; [0139] independently places adder tree 426 in FIG. 4. Image
  shows INT35 output. GROUNDED.

### A3 — §4 VMM anchor moved to [0004]
Verdict: **YES, [0004] supports the claim.**
Span:
> "A VMM is the document's shorthand for vector-matrix multiplication, the operation that
> dominates AI training and inference [0004]."
- [0004]: "In such models, inference and training often involve repeated application of
  matrix-vector and matrix-matrix multiplications to transform input feature vectors,
  propagate activations through network layers, and update parameters..." Supports both
  "training and inference" and the dominance framing ("repeated application"). Reinforced by
  [0002] ("Matrix-vector multiplication is a fundamental computational operation"). "Dominates"
  is a fair lay compression, not overreach. GROUNDED.

## B. General expert re-checks

### B1 — Claimed-vs-described separation
Verdict: YES, accurate against the Claim scope map.
- §3: "independent claims 1, 20, and 29 seek the multiply-align-add triad, not the mode
  decoding unit and not the format switching [0011]." Matches scope map (mode decoding unit =
  "Leaves open / description preference only" for claim 1; claims 20/29 add shift-calc unit /
  shift register, not the mode unit). CORRECT.
- §4/§5 double-buffering: "the document describes, in its summary passages rather than in the
  claims it is seeking, memory cells built from two bitcells each" [0012]. Matches scope map
  (dual-bank scheme in Summary/Aspects only; claims 11-19 canceled). CORRECT.
- Claim 20 = "shift calculation and select decoding unit [0200]"; claim 29 = "shift register";
  claim 3 = shift register sized to "maximum exponent plus the mantissa bit count [0202]";
  claims 6-9 = "logarithmic multiplexer tree [0206]". All match the scope map. CORRECT.

### B2 — Mantissa-alignment mechanism fidelity
Verdict: YES.
> "The macro finds the largest exponent among the 32 products in a block and computes how far
> each mantissa must shift to sit on that shared scale [0199] [0200], which puts every
> contribution on a consistent footing before the sum [0104]."
- [0199]: "a maximum exponent value E.max among the P.E_i<4:0> of all the primitive
  products... can be determined." [0200]: "a shift value P.shift_i of the mantissa bits... can
  be determined by subtracting an exponent value... from the maximum exponent value E.max."
  [0104]: "This alignment can ensure that all contributions are represented on a consistent
  scale... crucial for maintaining accuracy when summing many floating-point products." All
  three anchors support their spans. GROUNDED.

### B3 — FP8×FP6 → 22 → INT5 → INT35 → FP22 walk
Verdict: YES, every step grounded.
- "largest exponent any product can carry is 22, which fits in a 5-bit integer [0199]" —
  [0199]: "the maximum exponent value E.max... is 22, which can be represented by a 5-bit
  integer INT5(22)." Image confirms "Emax INT5(22)". GROUNDED.
- "adder tree sums the column and hands out a 35-bit integer plus that 5-bit exponent [0145]"
  — [0145]: "1×32 dot products in INT35 and INT5 formats"; image output = INT35. GROUNDED.
- "converts the result to FP22... in one step [0141] [0145]" — [0145]: "converted to FP22
  format by the dequantization unit 106"; [0141] = shared block scaling factor fused at
  dequant. GROUNDED. FP8/FP6 correctly conditioned on the format combo (mode-1 example), not
  presented as universal.

### B4 — No residual place crediting OpenAI for prior art
Verdict: YES (clean). §2 "the trick itself is not OpenAI's invention"; §3 "block-scaled
arithmetic is established practice... A skeptic can fairly call the core a known technique,
implemented" and "the data layout... is not OpenAI's idea at all. It is the shape the
industry standardized as OCP MX in September 2023." No paragraph credits OpenAI with BFP/MX.

### B5 — Pinned values described as bounds
Verdict: NO violation. The Claim scope map lists NO pins (all "none"); every quantitative
value used (block size 32, INT35, FP22, exponent 22, 256 VMM ops, 64×64 adders) is presented
as a description example ("in the description's example", "the example 32-by-32 array"), never
as a claim limitation.

### B6 — Steelman present + not overweight (strongest THIS-patent objection)
Verdict: PRESENT and refined at full strength (not steelman-absent). The strongest
this-patent objection — "the align-to-shared-exponent + integer-accumulate core is just known
block floating point / standardized OCP MX, so the clever part isn't OpenAI's" — is conceded
at full strength ("A skeptic can fairly call the core a known technique, implemented") then
refined to the claimed circuit ("machinery that executes those blocks natively inside a
memory macro, and the more universal the format becomes, the more that machinery is worth").
The affirmative rebuttal carries >= the concession's attention within §3. Not steelman-absent;
not a generic patent truism.

### B7 — Verdict proportionality (overreach AND over-hedge)
Verdict: firm and evidence-proportionate. §7 asserts "'OpenAI-designed' is literal
engineering, and this filing is the primary evidence" with ONE patent-specific guard
("nothing connects these circuits to Jalapeño... no source shows this macro running in
silicon"). Pending scope handled without hedging: "what examination leaves of claims 1, 20,
and 29 will fix how much of the... engine OpenAI ends up owning." No safe-harbour boilerplate;
not softer than the body's evidence.

## C. Residual findings (low; non-blocking)

### C1 — Double-mention of the "not OpenAI's invention" concession (low)
Check: steelman-overweight / thesis-restatement.
Verdict: borderline-yes, judged acceptable. The concession "block floating point is not
OpenAI's invention" now appears in §2 (one subordinate clause, foreshadow) AND as §3's whole
concession-first beat. This primes the counter twice. Mitigating: §2's clause is subordinate
and the paragraph ends on the affirmative ("What the claim seeks to own is the compute-in-
memory circuit"), and §3 is the deliberate dedicated concession section, so the reader leaves
each beat carrying the invention, not the counter. For THIS persona the §2 addition is
net-positive (it prevents the essay from implying OpenAI invented BFP, my strongest
objection, at the exact point the "trick" is celebrated). Fix if the orchestrator elects to
act: de-elaborate — tighten §2's clause or let §3 alone carry it — NEVER add a hedge. Severity
LOW; recommend NO CHANGE.

### C2 — "shared scale" (alignment) vs "shared scale factor" (MX block) proximity (low)
Check: term precision.
Verdict: technically defensible, minor conflation risk. §2/caption use "one shared scale" /
"that shared scale [0199][0200]" for the intra-column align-to-max-exponent operation, and
"the block's shared scale factor [0141][0145]" for the MX per-block b-bit scale fused at
dequant. These are two distinct mechanisms; the essay does keep distinct wording ("scale" vs
"scale factor"), so it is not wrong, but a careful engineer could momentarily merge them. Fix
if elected: none required; at most narrow the caption phrase. Severity LOW; recommend NO
CHANGE.

## Grounding spot-check log (anchors verified against input/patent.md)
§2: [0141], [0011], [0005](quote), [0199], [0200], [0104] — all match.
§4: [0004], [0147](quote), [0154], [0012], [0015] — all match ([0015] verbatim
"minimize compute stalls during updates"; also supports FIG. 43 "share bit lines").
§5/§6: [0154](256 VMM / 100% util quotes), [0012], [0118](scan-test quote verbatim),
[0262](PVT timing), [0289](non-overlapping clocks) — all match.
FIG. 4 caption: [0138] verbatim; image inspected, drawing type confirmed.

## Bottom line
Round-1 SKPRO-01 fix is confirmed CORRECT and complete: the align-once/integer-accumulate
arithmetic is now labeled block floating point (a known style), the claim is scoped to the
compute-in-memory circuit, the FIG. 4 caption accurately names the drawing type, and §4's
VMM claim is anchored to [0004]. No new overreach, no new hedge, no new technical error, no
contradiction with §3. No medium-or-higher residuals. Two LOW observations logged for the
multi-vote; both recommend NO CHANGE (and, if actioned, de-elaborate/narrow — never hedge).
