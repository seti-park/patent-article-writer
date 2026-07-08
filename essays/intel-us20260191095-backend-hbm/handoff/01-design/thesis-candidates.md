# Thesis Candidates

Single-spine default (no multi-spine override in the invocation). Three candidates generated from invention-summary.md Layer 4 angles; the orchestrator auto-selects Candidate 1 and surfaces the list for owner override. Edition brief (`input/essay-context.md`) sets the thesis DIRECTION (Phase 1 may sharpen, not soften) and `closing_posture: measured`.

## Candidate 1: Memory as a foundry-plus-packaging capability

**Statement**: Intel's "Ultra HBM" filing builds the 1T1C DRAM cell from back-end (BEOL) transistors and stacks the dies eight-high to match HBM4's footprint; because the cell now lives in the back-end, the filing quietly reframes HBM-class memory as a candidate output of a logic-plus-BEOL-plus-packaging flow, not the exclusive product of a dedicated DRAM front-end fab.

**Framing**: analytical reframe — read the one load-bearing claim word ("backend") for what it changes about WHERE such memory can be made, then price the reading against what the filing does not say.

**Evidence required**:
- Claim-anchored "1T1C backend DRAM" language
- The BEOL / thin-film-transistor mechanism (what "backend" means)
- HBM supply concentration + the DRAM-FEOL-fab baseline (external)
- The falsifiable proof-point calendar (VLSI 2026; ~2029-2030)

**Evidence available in invention-summary**:
- ✓ Claims anchor (claim 1 via `[0069]`; "backend" is claim text)
- ✓ Mechanism (`[0031]` thin-film-transistor databases; `[0027]` back-end-of-line transistors)
- ✓ Effect / goal (`[0027]`, `[0034]` match-HBM4 footprint, 0.5-5 GB)
- ✓ Baseline (external: HBM ~60% SK hynix; fact-check-log)

**Structural tension**: the market asks "is Intel getting back into memory (and is this the ZAM story)?"; the filing answers something more specific and more consequential — not "rebuild a DRAM fab," but "move the DRAM cell into the back-end so it need not come off one."

**Risks**:
- The foundry reading is an inference the claim does not state (handled by making the Claim scope map the content of §5, not a vulnerability).
- Attention could drift to spec-sheet numbers or to the pending-status paperwork (handled by the payload budget: one pricing section, tech-first lead).

**Grounding (4-axis — locked in Step 4, see thesis-spine.md)**:
- Claims anchor: 청구항 1 — "each memory die in the die stack comprises one transistor one capacitor (1T1C) backend dynamic random access memory (DRAM)" (Example 1 `[0069]`); load-bearing word = "backend"
- Problem anchor: `[0019]` "state-of-the-art approaches for high bandwidth memory (HBM) can include use of single die one-transistor one-capacitor (1T1C) memory"
- Effect anchor: `[0027]` "can be an approximately 1.5 GB die based on back-end-of-line transistors" + `[0034]` "With the goal of matching HBM4's footprint"
- Baseline-difference anchor: today's HBM is fabricated in dedicated DRAM FEOL fabs, SK hynix ~60% of HBM (industry-baseline-comparison; fact-check-log hbm-supply-concentration)

**Q7 hook pattern (hard-gated in Step 5)**:
- corporate-narrative-friction
- anchor: Intel EXITED merchant memory (NAND → SK hynix 2021; Optane $559M write-off 2022) and is now publicly pushing the ZAM "HBM killer" — vs this quieter Intel filing whose real move is architectural (put the DRAM cell in the back-end). The technical payload (relocate the cell so a non-DRAM-fab flow could carry it) fits inside ¶1.

**Adversarial defense (locked in Step 6)**:
- Strongest objection: "backend" in claim 1 does not equal "logic-foundry-makeable"; 1T1C still keeps the capacitor (relocated, not removed); incumbents are already on 3D DRAM; the filing gives no yield/cost/retention number, so the foundry-capability claim is the essay's synthesis.
- Mitigation: §5 concedes this at full strength via the Claim scope map, then returns to the one thing the claim DOES lock ("backend"), and the measured verdict reserves timing/economics to the VLSI 2026 proof points.

---

## Candidate 2: The tall custom stack built to beat HBM4's footprint

**Statement**: Intel's filing architects an 8-high-and-beyond stack of 0.5-5 GB backend-DRAM dies, wired by four TSV gutters per die and a 32 GHz UCIe base die, explicitly "with the goal of matching HBM4's footprint."

**Framing**: build-walk — narrate the datablock → sub-channel → TSV-gutter → base-die architecture as a challenger to HBM4.

**Evidence required**:
- Stack height, die capacity, TSV-gutter / UCIe architecture
- A quantified HBM4 comparison

**Evidence available in invention-summary**:
- ✓ Stack + architecture (`[0023]`, `[0033]`, `[0034]`)
- ✓ Capacity / clocks (`[0027]`, `[0034]`)
- ✗ A patent-side HBM4 comparison: the filing gives NO bandwidth, capacity-vs-HBM4, or $-per-bit number — the only "vs HBM4" figures are external (ZAM specs), which invites conflation with ZAM/HB3DM

**Structural tension**: a spec-by-spec challenger walk toward "does it beat HBM4?"

**Risks**:
- Becomes a spec-sheet essay; under-weights the strategic point (WHERE it can be made), which is the edition brief's core.
- The only concrete "beats HBM4" numbers are ZAM's, not this patent's — high conflation risk (guard: connect, do not conflate).

**Grounding (4-axis)**:
- Claims anchor: 청구항 5/10 — "a plurality of alternating sub-channels and through-silicon via (TSV) gutters" (Example 5 `[0073]`)
- Problem anchor: `[0002]` "However, improvements are needed in the field of high bandwidth memory."
- Effect anchor: `[0034]` "to have a die capacity of 0.5-5 GB" + `[0023]` "8-high and beyond"
- Baseline-difference anchor: ✗ weak — no patent-side HBM4 metric; the baseline collapses into external ZAM/HBM4 bandwidth numbers (3/4)

**Q7 hook pattern**:
- technical-impossibility (draft): reader's "how does a stack of memory dies beat a purpose-built HBM stack?"
- anchor: the stack architecture vs HBM4 footprint — but the resolution needs external numbers the patent lacks

**Adversarial defense (draft)**:
- Strongest objection: the patent quantifies nothing versus HBM4; the "beats HBM4" claim would ride ZAM's numbers, conflating two different documents.
- Mitigation: would require heavy external scaffolding, moving the load off the patent.

**Rejection reason**: Axis 4 only 3/4 anchored — the patent supplies no HBM4 comparison, so the "beat HBM4" frame leans on external ZAM figures and risks conflating this filing with ZAM/HB3DM (an explicit accuracy guard). It also under-weights the edition brief's strategic core (memory as a foundry capability). Folded into Candidate 1 as §3 (the stack + "match HBM4's footprint" is the mechanism beat that FEEDS the foundry-capability verdict), not the spine.

---

## Candidate 3: Intel's memory comeback

**Statement**: Intel, which exited memory, is coming back — the ZAM "HBM killer" and this "Ultra HBM" filing are Intel re-entering the memory business.

**Framing**: corporate-return narrative — the company's arc as the plot.

**Evidence available in invention-summary**:
- ✗ The patent never says "comeback," "product," "business re-entry," or schedules anything; it is a pending application
- ✗ Even in ZAM, Powerchip (not Intel) is reported to fab the DRAM — "Intel makes memory again" is not supported

**Structural tension**: none earned from the patent; the tension is entirely in the news cycle.

**Risks**:
- Overreach to productization from one pending filing (accuracy guard violation).
- Makes the company/paperwork the plot, not the invention (procedure-overweight; verdict frame ≠ narrative frame).
- The edition brief explicitly says the interesting move is NOT "Intel kills the DRAM fab" / "back into memory."

**Grounding (4-axis)**:
- Claims anchor: none — "comeback" is not a claim element
- Problem / Effect / Baseline: all external narrative, not patent-anchored (0/4 on patent text)

**Q7 hook pattern**: would be corporate-narrative-friction, but the "friction" resolves into status/business narration whose technical payload cannot lead ¶1 — a `procedure-overweight-lead` defect.

**Rejection reason**: 0/4 patent-axis grounding and a direct violation of the edition brief's accuracy guards (published application ≠ productization; Intel exited memory and even ZAM has Powerchip fabbing the DRAM). It is a news frame, not a patent thesis. The corporate-return material survives ONLY as the §1 hook's narrative-friction setup and the §5/close guard, never as the spine.

---

## Comparison

| Dimension | Candidate 1 | Candidate 2 | Candidate 3 |
|-----------|-------------|-------------|-------------|
| Evidence completeness | Full | Partial | None (patent-side) |
| Audience appeal | High | Medium | High (but misleading) |
| Architectural depth | High | High | Low |
| Defensive strength | High | Medium | Very low |
| 4-axis grounding | 4/4 | 3/4 (no baseline) | 0/4 |
| Q7 hook | corporate-narrative-friction | technical-impossibility (weak) | (procedure-overweight) |
| Fit to edition brief | Exact (sharpened) | Under-weights core | Violates guards |

## Recommendation

Candidate 1 — the only 4/4-anchored candidate, it rides the one load-bearing claim word ("backend") to the edition brief's strategic core (memory as a foundry-plus-packaging capability), keeps the ZAM/market facts as clearly-labeled external context, and gives the measured verdict a real falsifiable calendar (VLSI 2026). Candidate 2's stack-walk becomes §3; Candidate 3's comeback narrative is confined to the §1 hook and the §5/close guard.

## SETI selection

- **Decision**: Select Candidate 1 (auto-selected per single-spine default; surfaced for owner override)
- **Notes**: proceed to spine lock (Step 8) with Candidate 1's grounding + corporate-narrative-friction hook + claim-scope steelman. `closing_posture: measured` per owner (essay-context option A).
