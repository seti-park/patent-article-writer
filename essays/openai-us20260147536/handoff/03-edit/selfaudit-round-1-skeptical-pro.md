---
pass: self-audit-adversarial-reader
persona: skeptical domain professional (chip/hardware engineer — compute-in-memory + floating-point arithmetic)
target: handoff/03-edit/essay-final.md
patent: input/patent.md
posture: firm (verdict edition)
verdict: 2 findings (1 medium, 1 low)
---

# Self-audit — skeptical domain professional (CIM / FP arithmetic)

Read the accepted essay with expert, skeptical eyes, hunting for surviving technical
overclaim, sloppy mechanism, prior-art mis-credit, figure-caption overclaim, and both
overreach AND over-hedge. Grounding spot-checks were run against the patent and the claim
scope map. Every checked anchor resolved to the cited paragraph; the numeric walk is
faithful; the claim/description separation and registry facts are honest; no pinned value
is described as a bound (scope map lists no pins); no safe-harbor boilerplate under the firm
posture. Two findings remain.

---

## SKPRO-01 — prior-art scope: the headline "trick" is block floating point, conceded only as a data-format matter

- **check**: overreach / crediting OpenAI for an industry-standard technique (steelman completeness + placement)
- **severity**: medium
- **location**: title + section "Multiply in Floating Point, Add as Integers, Convert Once" (bolded line) vs. concession in "The Headline Features Are Described. The Circuits Are Claimed"
- **quoted span (overclaim framing)**:
  > "OpenAI's Chip Patent Does Floating-Point Math on Integer Adders" (title)
  > "**Align once, and the whole accumulation becomes integer arithmetic.** One alignment, one integer sum, one conversion back: that is the trick, and it is the part OpenAI wants to own [0011]."
- **quoted span (the concession that must carry it)**:
  > "And block-scaled arithmetic is established practice, standardized a year before this filing's priority date. A skeptic can fairly call the core a known technique, implemented."
- **why**: The essay's vivid mechanism reveal — "does floating-point math on integer adders,"
  "align once → integer arithmetic," billed as "the trick" — is the textbook definition of
  **block floating point (BFP)**: align a block of FP values to a shared (max) exponent, then
  sum the mantissas on an integer adder tree. The patent itself says so at `[0141]`: "A
  microscale (MX) format is a type of **Block Floating Point (BFP)** data format." BFP integer
  accumulation is a decades-old DSP/CIM technique, not an OpenAI insight. The essay DOES concede
  prior art — but the concession is scoped to the DATA FORMAT / "block-scaled arithmetic" and
  lands two sections after the "trick" framing. A domain reader hits "that is the trick" (with
  the align-once integer-accumulate sold as the surprising move) before any concession, and the
  essay never closes the loop that the exact mechanism it headlines IS the conceded prior art
  (BFP), the patent's `[0011]` claim being the specific **CIM circuit realization**, not the
  arithmetic idea. "the part OpenAI wants to own [0011]" is correctly claim-scoped, which
  contains the damage, so this is contained overreach, not a clean miss — hence medium, not high.
- **fix (label / narrow, NOT hedge)**: at the point of the "trick" assertion, name the method —
  e.g., make explicit that align-to-block-max-exponent + integer-adder-tree accumulation is
  block floating point (the patent's own `[0141]` label), and that what claim 1 `[0011]` seeks
  is the CIM circuit that executes it, not the arithmetic idea. This lets the affirmative core
  (dated, assigned circuit machinery) carry the beat without the reader leaving thinking OpenAI
  invented doing FP math on integer adders.

## SKPRO-02 — figure-caption overclaim: FIG. 4 is a functional/dataflow block, called "circuitry ... made literal"

- **check**: figure caption overclaims beyond what the drawing shows
- **severity**: low
- **location**: hero caption directly under the title
- **quoted span**:
  > "FIG. 4: the align-once core, drawn as circuitry. Each product's mantissa shifts onto the block's largest exponent (at most 22 here, a 5-bit integer [0199]), and the column adder tree sums the aligned mantissas as plain integers [0011], one 35-bit result per column [0145]. This is claim 1's align-then-integer-accumulate step, made literal."
- **why**: Per the patent, FIG. 4 is NOT a circuit schematic — `[0138]`: "FIG. **4** illustrates
  an exemplary **functional block** for mantissa alignment **3880** ... An example of **process
  flow and data flow** for mantissa align-ups and accumulation ... is also depicted in FIG. **4**."
  The *physical/circuit* implementation is a different figure — `[0205]`: "FIG. **38** illustrates
  an exemplary **physical implementation** of a column of computing unit **222**." (For contrast,
  the essay's FIG. 43 caption is fine — `[0217]` calls FIG. 43 "an exemplary **schematic
  diagram**.") Calling FIG. 4 "drawn as circuitry" and "made literal" overstates the drawing
  type: a functional/dataflow block diagram is not a literal circuit. The numeric content of the
  caption (Emax 22 → INT5, INT35 per column, claim-1 step) is accurate and grounded; only the
  "circuitry / made literal" characterization overreaches.
- **fix (narrow)**: retitle the drawing accurately, e.g., "the align-once core as a
  functional / dataflow block" (drop "drawn as circuitry ... made literal"), or point the
  "made literal / circuitry" language at the physical-implementation figure (FIG. 38) if that
  asset is used instead.

---

## Checks that passed (evidence-forced, for the record)

- **Numeric walk** (FP8×FP6 → Emax 22 → INT5 / INT35 → FP22): faithful. `[0199]` "the maximum
  exponent value E.sub.max of the resulting primitive product is 22, which can be represented by
  a 5-bit integer INT5(22)"; `[0145]` "1×32 dot products in INT35 and INT5 formats ... converted
  to FP22"; `[0202]` shift register "7b+22b=29b"; `[0207]` adder-tree output "in INT35 format."
  verdict: yes.
- **Mantissa-alignment mechanism** (shift to block-max exponent, integer adder tree, one
  dequant to FP22): faithful. `[0200]` "P.sub.shift_i = E.sub.max − P.sub.E_i"; `[0139]`
  "synthesizable (or custom) adder tree ... accumulates ... in the integer domain (e.g., INT35
  and INT5)." verdict: yes.
- **Claimed vs described separation**: honest. Independent claims {1, 20, 29} quoted/attributed
  correctly (claim 20 = triad + shift calc/select decode unit `[0200]`; claim 29 = triad + shift
  register; deps 3/6-9 at `[0202]`/`[0206]`). Mode decoding unit, format agility `[0130]`,
  dual-bank double-bitcell `[0012]`/`[0015]`, FP22 dequant, scan are correctly labeled as
  description/summary material, not claimed ("described, in its summary passages rather than in
  the claims it is seeking"). Matches the claim scope map. verdict: yes.
- **OCP MX prior-art concession**: honest and correctly scoped (MX v1.0 2023-09, seven named
  signatories, "not OpenAI's idea at all," "a year before this filing's priority date"). Present
  and specific; rebuttal (dated/assigned circuit machinery) carries >= the concession — not
  steelman-overweight. See SKPRO-01 for the one residual gap (method vs. format). verdict: yes
  with SKPRO-01 caveat.
- **Over-hedge / firm posture**: no safe-harbor boilerplate. Pending-application caveat "prices
  the evidence without changing what it shows"; "design statements by an applicant, not
  measurements of silicon"; Jalapeño / no-silicon guard is THIS-patent specific. Verdict firm
  ("the record is the harder document to argue with"). No granted-scope overreach ("what
  examination leaves of claims 1, 20, and 29 will fix how much ... OpenAI ends up owning").
  verdict: yes (clean, no over-hedge finding).
- **Pins vs bounds**: scope map lists no pins; example values (Emax 22, block of 32, 32×32,
  64×64 adders, 256 VMM) are presented as description examples, not claim limitations. verdict: yes.
- **Anchor grounding spot-checks** (>3 sections): `[0011]`, `[0133]`, `[0141]`, `[0145]`,
  `[0199]`, `[0200]`, `[0202]`, `[0206]`, `[0183]`, `[0154]`, `[0012]`, `[0015]`, `[0118]`,
  `[0234]`, `[0262]`, `[0289]`, `[0217]/[0218]` all resolve to the cited paragraphs. verdict: yes.
