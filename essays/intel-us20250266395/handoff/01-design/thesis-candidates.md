# Thesis Candidates

Single-spine default (no multi-spine override present in the invocation). Candidates generated from invention-summary Layer 4 angles; per-run framing from `input/essay-context.md` (EMIB-T news hook) taken as the entry context for all candidates.

## Candidate 1: The flow after the one in the news

**Statement**: While the market watches EMIB-T productize the powered bridge, Intel's filing stakes out the next assembly flow: bond the bridge to the dies first at micron pitch, test the whole multi-die assembly before any substrate is committed, then drop the bridge into a substrate cavity and feed it power from the cavity floor.

**Framing**: narrative-reorder — the reader arrives asking "is this the EMIB-T patent?"; the essay answers "no — it is the flow one step past EMIB-T, filed before EMIB-T was even announced."

**Evidence required**:
- The claimed assembly order + pre-substrate test (patent)
- The TSV/TGV cavity-floor power path (patent) and its EMIB-T sibling (external)
- The shipped EMIB baseline flow, bridge-in-substrate-first (external)
- Yield economics of multi-die packages (external, illustrative)

**Evidence available in invention-summary**:
- ✓ Claim 19 order-of-operations + test (`[0142]`, `[0061]`, `[0062]`)
- ✓ Through-bridge power path + purpose (`[0035]`, `[0123]`) and effect (`[0035]` routing layers/yield)
- ✓ Pitch quantification (`[0025]`, `[0034]`)
- ✓ External baselines researched and logged (emib-chips-last-flow, emib-t-ectc-2025, kgd-yield-multiplier)

**Structural tension**: the news says the bridge lives in the substrate and gets TSVs; the filing says the bridge joins the dies first and the substrate becomes the last, deferrable component — with a test gate in between.

**Risks**:
- Reader conflates "filed the next flow" with "will build the next flow" — must hold the application-not-roadmap line (one anti-hype guard in the close).
- Claim-scope stitching: the full story spans multiple claims (19+20 flow, 1 hybrid bond, 2/13/15 via+cavity, 17 glass); no single claim contains it all — must be handled openly (steelman).

**Grounding (4-axis — draft, locked in Step 4)**:
- Claims anchor: claim 19 (method as filed) — attach bridge to dies → create multi-die bridge assembly → test → attach substrate when it passes (via Example 21 `[0142]`); claim 20 cavity (`[0144]`)
- Problem anchor: `[0024]` passive bridges "cannot achieve the maximum current (Imax)"; active TSV bridges leave "drilling, alignment, cavity filling and soldering" challenges
- Effect anchor: `[0035]` "reduces the number of substrate routing layers and can improve product yield"; test-gated substrate attach `[0062]`
- Baseline-difference anchor: shipped EMIB embeds the bridge in the substrate before dies attach (emib-chips-last-flow, tier-2) vs claim 19's dies-first order; EMIB-T adds the same bottom-power idea to the OLD order (emib-t-ectc-2025)

**Q7 hook pattern (draft, hard-gated in Step 5)**:
- corporate-narrative-friction
- anchor: Intel's ECTC May-2025 EMIB-T narrative (TSV bridge, power from package bottom, 2026 fab rollout) vs this Feb-2024 filing that uses the same powered-bridge idea with the assembly order inverted and a test gate inserted — the filing predates the public EMIB-T unveiling by ~15 months and describes the flow after it. The technical object (what the flow does: bond first, test, then commit a substrate) fits in ¶1.

**Adversarial defense (draft, locked in Step 6)**:
- Strongest objection: the "next flow" story is stitched from optional branches — only method claim 19/20 locks the order+test, while hybrid bonding pitch, cavity-floor power, and glass are description preferences or separate dependent claims; no single claim combines them.
- Mitigation: the essay's claim-map section states this structure explicitly (locked order vs open options) and makes the order+test the load-bearing point — which IS singly claimed.

---

## Candidate 2: The test is the patent

**Statement**: The economically decisive move in Intel's filing is a single method step: performance-test the multi-die bridge assembly before a substrate exists, so a bad die never consumes a finished package.

**Framing**: stakes-first — lead with the yield arithmetic of 12-stack AI packages, then show the filing writes the escape hatch into the claim.

**Evidence required**:
- Test step as claim limitation (patent)
- Yield-multiplier economics (external)
- Package-size roadmap making the stakes concrete (external)

**Evidence available in invention-summary**:
- ✓ Test step (`[0061]`, `[0062]`, `[0142]`)
- ✓ External: kgd-yield-multiplier, emib-package-roadmap-120mm
- ✗ Effect anchor inside the patent for the TEST specifically — the specification never states the test's benefit; `[0035]`'s yield sentence belongs to the TSV routing, not the test. Axis 3 rests on flow order alone.

**Structural tension**: the scarier the package (12 HBM stacks, reticle-busting), the more valuable the pre-substrate gate.

**Risks**:
- Axis 3 is thin: the causal claim "test saves the package" is the essay's/industry's inference, not the patent's stated effect — one step from a Category-3 (correlation/causation) hit.
- Drops the EMIB-T hook the reader arrives with; buries the assembly-order inversion that makes the test possible.

**Grounding (4-axis — draft)**:
- Claims anchor: claim 19 testing limitation (via `[0142]`)
- Problem anchor: `[0022]` fabrication challenges and higher costs
- Effect anchor: (weak) flow order only — `[0062]` substrate attached "after the multi-die bridge assembly passes the performance metrics"; no stated benefit sentence
- Baseline-difference anchor: KGD practice tests dies, not bonded multi-die-plus-bridge units, before substrate commit (kgd-yield-multiplier)

**Q7 hook pattern (draft)**:
- corporate-narrative-friction (12-HBM-stack roadmap vs one-bad-die scrap math) — workable but the friction is generic industry math, weaker than C1's specific EMIB-T inversion

**Adversarial defense (draft)**:
- Strongest objection: the patent never says the test saves yield or money; the essay would be building its spine on an unstated effect.
- Mitigation: possible (label all economics as external), but then the spine's own effect axis is borrowed.

**Rejection reason**: Axis 3 effect anchor is not in the specification for the test itself (the only yield sentence `[0035]` belongs to the TSV routing); as a standalone spine it invites a correlation-vs-causation dismissal. FOLDED INTO Candidate 1 as the §3 economics beat, where the patent supplies the flow and the external KGD math supplies the clearly-labeled stakes.

---

## Candidate 3: Two bonding worlds, one assembly

**Statement**: Intel's filing solves the mismatch the reader would not expect to coexist: micron-pitch hybrid bonding on one face of the bridge and old-fashioned solder toward the substrate on the other, in one tested assembly.

**Framing**: technical-impossibility — "you can't hybrid-bond at 1-10 microns and still solder the thing to a normal board — can you?"

**Evidence required**:
- HBI pitch numbers + solder-substrate reality (patent)
- Claim 1 direct-bonding structure (patent)
- External baseline for how hybrid bonding is normally deployed (wafer-level, e.g. TSMC SoIC)

**Evidence available in invention-summary**:
- ✓ `[0025]` solder-attach substrates persist; `[0025]`/`[0034]` pitch numbers
- ✓ Claim 1 direct bonding (`[0122]`)
- ✗ External baseline NOT researched this run (no logged source on wafer-level-only hybrid bonding practice); Axis 4 is 3/4

**Structural tension**: fine-pitch world and solder world meet inside one component.

**Risks**:
- The "impossibility" is soft — a packaging-literate reader knows mixed interconnects exist; the naive reader needs three glosses before the hook lands.
- Loses both the EMIB-T news hook and the test step (the run's stated economic center).

**Grounding (4-axis — draft)**:
- Claims anchor: claim 1 direct-bonding limitations (via `[0122]`)
- Problem anchor: `[0023]` copper-to-copper cost/complexity
- Effect anchor: `[0025]` small pitches enabled
- Baseline-difference anchor: ✗ not externally anchored this run (3/4)

**Q7 hook pattern (draft)**:
- technical-impossibility — reader's "how do micron bonds and solder balls coexist?" — judged accessible only after significant glossing

**Adversarial defense (draft)**:
- Strongest objection: mixed-interconnect packages already exist; the coexistence is not new — the assembly order is.
- Mitigation: would require reframing back toward... Candidate 1.

**Rejection reason**: Axis 4 unanchored (3/4) this run, hook requires heavy glossing for the target reader, and its own steelman collapses it into Candidate 1. The HBI-meets-solder material survives as a supporting beat in C1's mechanism section.

---

## Candidate 4: The glass filing

**Statement**: Beneath the bridge story, this filing is Intel's glass roadmap in claim form — glass bridge, glass frame, glass-core substrate with through-glass vias.

**Framing**: insider — read the claims the glass-substrate press releases never showed you.

**Evidence available in invention-summary**:
- ✓ Glass options (`[0033]`, `[0049]`, `[0054]`, `[0138]`); external intel-glass-substrate-2023 (tier-1)
- ✗ Problem anchor: the Background never states a glass-specific problem — glass appears only as an embodiment material
- ✗ Effect anchor: no stated glass-specific advantage beyond structural stability of the frame (`[0049]`)

**Rejection reason**: 4-axis grounding fails (2/4 — no problem anchor, effect anchor thin); glass is an option layer of this filing, not its spine. Survives as a one-paragraph tie-in inside Candidate 1's power/substrate section, anchored to claim 17 via `[0138]` + intel-glass-substrate-2023.

---

## Comparison

| Dimension | Candidate 1 | Candidate 2 | Candidate 3 | Candidate 4 |
|-----------|-------------|-------------|-------------|-------------|
| Evidence completeness | Full | Partial (Axis 3 thin) | Partial (Axis 4 missing) | Weak (2/4) |
| Audience appeal | High (rides the news the reader arrived with) | High lead, weak middle | Medium | Medium |
| Architectural depth | High (order + test + power + options) | Medium | Medium | Low |
| Defensive strength | High (steelman answerable inside the claims) | Medium (causation exposure) | Low (collapses into C1) | Low |
| 4-axis grounding | 4/4 | 3/4 (weak effect) | 3/4 (no baseline) | 2/4 |
| Q7 hook | corporate-narrative-friction | corporate-narrative-friction (weaker anchor) | technical-impossibility (gloss-heavy) | (none clean) |
| Hook accessibility | High | Medium-high | Medium | Low |

## Recommendation

Candidate 1 — the only 4/4 grounding; the Q7 anchor is specific and current (ECTC 2025 EMIB-T vs this Feb-2024 filing, order inverted); and it absorbs the strongest material of Candidates 2-4 as section beats instead of losing it.

## SETI selection

- **Decision**: Auto-selected Candidate 1 per single-spine default (orchestrator may override; all rejections documented above).
- **Notes**: C2's yield economics = §3 beat (external math, labeled); C3's HBI-meets-solder = §2 mechanism support; C4's glass = §4 tie-in, one paragraph, claim 17 scope per the Claim scope map.
