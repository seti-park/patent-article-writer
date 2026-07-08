# Thesis Candidates

Edition frame (controlling, from input/essay-context.md): pending application — the verdict
cannot be about fence strength; it lands on what this document IS (origin filing, the
memory-side half of the architecture philosophy in writing, an asset-in-formation) and what
its treatment (portfolio collateral, continued prosecution spend) says about the company.

## Candidate 1: The memory half was written first — and it is still not an asset

**Statement**: Etched's very first patent filing put the no-switch memory half of its
architecture in claim language in May 2023, two years before the company pitched it on
stage; three years of examination later it is still a bet the company keeps paying to
convert into an asset, not the asset itself.

**Framing**: origin-document verdict — read the founding filing as the earliest written
evidence of the architecture bet, then price it honestly as an asset-in-formation.

**Evidence required**:
- Claim-39-family claim language (channels hardwired to columns, no switching element)
- The filing's origin facts (2023-05-10, both co-founders)
- The thread's CSM pillar as corporate narrative (company-claimed)
- Prosecution record (label sentence) + collateral facts (portfolio scope)

**Evidence available in invention-summary**:
- ✓ Claim anchors: claim 39 (+ 7/19/32, 15) sought scope; `[0016]` twin span
- ✓ Mechanism + effect spans: `[0043]`, `[0044]`, `[0045]`, `[0039]`
- ✓ Problem spans: `[0018]` memory premise, `[0003]`
- ✓ External facts: fact-check-log (liens, prosecution, thread, family)

**Structural tension**: the philosophy ships on stage (company-claimed) while its ownership
is still being argued at the USPTO; the oldest document in the story is also the least
settled one.

**Risks**:
- The lien facts tempt patent-specific importance claims — collateral is portfolio-blanket
  (discipline in fact-check-log).
- The CSM echo must stay an echo, not an equation: the thread's rack-scale memory product is
  not claim 39, and the essay must not claim the shipping product practices the claims.

**Grounding (4-axis — draft, locked in Step 4)**:
- Claims anchor: claim 39 (sought) — "a separate memory device comprising a plurality of channels, wherein each of the plurality of channels is hardwired to respective one or more columns in the systolic array without any switching element"; reinforced by claims 7/19/32 (HBMs hardwired to columns) and claim 15 (memory chips on the top row storing weights)
- Problem anchor: `[0018]` "it is unreasonable to expect a single chip to interface with 100s of GB of memory used to store parameters and intermediate computation values" + `[0043]` switch "typically used"
- Effect anchor: `[0045]` "This avoids having to add a switching element ... which can save space and power" + `[0039]` add compute rows without adding memory
- Baseline-difference anchor: July 2026 thread presents the no-layer memory philosophy (CSM) as shipping-hardware fact (company-claimed) and the published wiring-half analysis found the memory half absent from the GRANTED record — vs the registry: the same philosophy claim-drafted 2023-05-10 and still sought (final rejection + RCE); industry side: conventional switched HBM access ([0043]; TPU-style 128×128 per-chip arrays, fact `tpu-mxu-128x128`)

**Q7 hook pattern (draft, hard-gated in Step 5)**:
- corporate-narrative-friction
- anchor: the July 2026 stealth-exit thread ("no memory layer" CSM pillar, racks shipping, $1B+ contracts — all company-claimed) vs the USPTO record: the same idea claim-drafted 2023-05-10, final-rejected 2025-10-23, under RCE — sold as shipping while its ownership is still being argued

**Adversarial defense (draft, locked in Step 6)**:
- Strongest objection: authorship without ownership — in a crowded examiner-cited field (8 refs: multi-node ML acceleration, NN accelerators) that has already produced a final rejection, the broad claims (claim 1's any-multi-chip package, claim 39's no-switch hardwiring) are exactly the ones most likely to narrow or die, so "in writing since 2023" proves the founders wrote it early, not that Etched will own it.
- Mitigation: make the objection part of the verdict, not a rebuttal target — the essay prices the document as an asset-in-formation (roadmap, not fence) and closes on the binary the objection itself sets up: what the memory-side claims look like when prosecution ends.

---

## Candidate 2: The splittable-array origin — the thread's giant math array was on file in 2023

**Statement**: The "splittable math arrays" Etched pitched in July 2026 is this document:
many identical chips fused into one combined systolic array the host sees as a single
device, written down as the company's first filing.

**Framing**: origin-reveal — the stitching idea (one array from many chips) as the founding
architecture decision.

**Evidence required**:
- Claim 1/26 combined-array language; `[0028]` one-large-array span; `[0024]` splittable span
- Thread linkage for "splittable math arrays" (company-claimed)
- Same prosecution/collateral record for the verdict

**Evidence available in invention-summary**:
- ✓ Claim anchors: claims 1, 26 (sought); `[0013]` twin span
- ✓ Mechanism spans: `[0019]`, `[0024]`, `[0028]`, `[0038]`
- ✓ External facts: same fact-check-log set
- ✗ A distinct baseline for the WIRING story that is not already spent: the granted wiring
  patent (US 12,361,091 B1) already owns "stitching chips into one array" in the PUBLISHED
  companion essay — as a granted fence, which beats a pending echo of the same story.

**Structural tension**: weaker — the reveal ("the array idea was on file early") was
substantially delivered by the granted-trio essay; this document adds only "even earlier,
but pending".

**Risks**:
- Re-treads the published wiring-half essay with a weaker (sought, not granted) document —
  violates the brief's "pairs with, does not repeat" instruction.
- Leaves the memory-side claims (this filing's distinctive content vs the granted record) as
  a footnote.

**Grounding (4-axis — draft)**:
- Claims anchor: claim 1 (sought) — chip-to-chip connections forming "a larger, combined systolic array"
- Problem anchor: `[0003]` FLOPs limited by array size in current IC design
- Effect anchor: `[0028]` host sees one large array; `[0038]` 100×400 from four chips
- Baseline-difference anchor: thread's "splittable math arrays" line (company-claimed) vs 128×128 single-chip world (`[0018]`, `tpu-mxu-128x128`)

**Q7 hook pattern (draft)**:
- corporate-narrative-friction
- anchor: thread pitches the giant splittable array as new; the filing wrote it down in May 2023

**Adversarial defense (draft)**:
- Strongest objection: the multi-chip-array concept is the most prior-art-exposed part of the filing (the examiner's 8 references aim at exactly this), and the granted trio already gives Etched a wiring fence — so this candidate stakes the essay on the weakest, most redundant claim family.
- Mitigation: none that preserves the candidate — the objection is why the memory half, not the array half, must carry the spine.

**Rejection reason**: Redundant with the published wiring-half essay (brief: "pairs with,
does not repeat") and staked on the claim family MOST exposed in prosecution while ignoring
this filing's distinctive memory-side content. The array origin survives as one supporting
section (§2) of Candidate 1, not as the spine.

---

## Candidate 3: The ASIC that takes no instructions — the transformer division of labor in writing

**Statement**: The filing describes an AI chip with no runtime instruction stream — a preset
loop of matrix math with a sidecar (auxiliary circuitry plus private memory) for the one
transformer operation that needs to remember previous tokens.

**Framing**: technical-impossibility walkthrough — resolve the reader's "how can a chip with
no instructions run a model?" through the division of labor and the pipeline chart.

**Evidence required**:
- `[0027]` preset loop; `[0047]`-`[0051]` auxiliary circuitry + private memory; claims 11-13
- FIG. 7 pipelining semantics (`[0053]`-`[0057]`)
- A GPU-flexibility baseline for the contrast

**Evidence available in invention-summary**:
- ✓ Mechanism spans: `[0027]`, `[0047]`, `[0048]`, `[0051]`; claims 11-13 (sought)
- ✓ FIG. 7 spans: `[0053]`, `[0055]`, `[0056]`, `[0057]`
- ✗ Claim anchor for the pipelining half: FIG. 7 material is description-only (no claim);
  the claim-anchored part (11-13) is dependent-claim content
- ✗ External baseline: GPU-vs-ASIC flexibility contrast needs sources this run did not
  gather (thread claims are about memory/voltage, not instruction streams)

**Structural tension**: strong as a mechanism story, weak as an investor verdict — it
explains the machine but does not price the document, which is the edition's question.

**Risks**:
- Axis 1 is dependent-claims-only for the claimed half and absent for the pipelining half.
- The edition's question ("what is this origin document worth to an investor as an asset")
  goes unanswered; the verdict would have to bolt on the registry facts unearned.

**Grounding (4-axis — draft)**:
- Claims anchor: claims 11-13 (sought, dependent) — auxiliary circuitry, self-attention, arrays do not communicate with local memory chips
- Problem anchor: `[0047]` self-attention needs previous-token data
- Effect anchor: `[0057]` 98% or greater utilization (description-only)
- Baseline-difference anchor: ✗ not externally anchored this run (3/4)

**Q7 hook pattern (draft)**:
- technical-impossibility
- anchor: "an AI chip that takes no instructions at runtime — how does it run a whole model?" resolved by `[0027]` preset loop + `[0047]`-`[0051]` division of labor

**Adversarial defense (draft)**:
- Strongest objection: the essay's showpiece (FIG. 7 pipelining, 98% utilization) is claimed nowhere — the thesis would ride on unclaimed description while presenting itself as claim analysis.
- Mitigation: possible only by demoting FIG. 7 to illustration — which collapses the candidate into a section.

**Rejection reason**: Axis 4 unanchored (3/4) and Axis 1 split (dependent claims only;
pipelining half description-only); answers "how does it work" when the edition asks "what
is the document worth". Its best material (preset loop, division of labor, FIG. 7) survives
as §4 of Candidate 1 and as the mechanism beats of the essay.

---

## Comparison

| Dimension | Candidate 1 | Candidate 2 | Candidate 3 |
|-----------|-------------|-------------|-------------|
| Evidence completeness | Full | Full (but spent) | Partial |
| Audience appeal | High (delivers the reader_sentence) | Medium (re-run of published story) | Medium-high (mechanism-curious readers) |
| Architectural depth | High | Medium | High |
| Defensive strength | High (objection folds into verdict) | Low (objection kills it) | Medium |
| Edition fit (pending-application verdict) | Direct | Weak | Weak |
| 4-axis grounding | 4/4 | 4/4 | 2.5/4 (Axis 1 split, no Axis 4) |
| Q7 hook | corporate-narrative-friction | corporate-narrative-friction | technical-impossibility |
| Hook accessibility | High | Medium | High |

## Recommendation

Candidate 1 — the only candidate whose 4-axis grounding, Q7 hook, and adversarial defense
all survive AND that answers the edition's question; it carries the reader_sentence
verbatim, folds Candidates 2 and 3's best material into §2 and §4, and its steelman (crowded
field, shrinkable breadth) strengthens rather than undermines the asset-in-formation verdict.

## SETI selection

- **Decision**: Select Candidate 1 (auto-selected per single-spine default and the run
  instruction to pick the recommended candidate; full candidate list surfaced above for
  human override).
- **Notes**: proceed to spine lock (Step 8) with Candidate 1's grounding + hook + defense.
  Candidates 2 and 3 are demoted to sections, not discarded as material.
