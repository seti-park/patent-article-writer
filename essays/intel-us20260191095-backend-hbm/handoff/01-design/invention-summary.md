# Invention Summary

## Metadata

- **Patent ID**: US 2026/0191095 A1 (published application; Appl. No. 19/001921)
- **Title**: Ultra High Bandwidth Memory with Backend Transistors
- **Filing date**: 2024-12-26
- **Publication date**: 2026-07-02
- **Inventors**: Abhishek Anil Sharma (Portland, OR), Anand Iyer (Saratoga, CA), Prashant Majhi (San Jose, CA), Nitin A. Deshpande (Chandler, AZ)
- **Classification**: Int. Cl. H01L25/07; H01L21/66; H10B80/00. CPC H10W90/00; H10B80/00; H10P74/27; H10W90/297
- **Assignee**: Intel Corporation (Santa Clara, CA)

## 발명 명칭 / 기술분야

Essay-ready phrasing: a high-bandwidth-memory (HBM) design in which each memory die's DRAM cell is built from **back-end (BEOL) transistors** rather than a crystalline-silicon DRAM front-end, and the dies are stacked "8-high and beyond" over a base die, wired by through-silicon-via (TSV) gutters and a UCIe I/O bundle, "with the goal of matching HBM4's footprint." 기술분야: 3D-stacked DRAM for high bandwidth memory — backend/thin-film-transistor 1T1C DRAM, TSV/HBI die stacking, UCIe base-die I/O, and memory-on-package (MoP) form factors `[0018]`, `[0020]`, `[0034]`.

## 종래 문제 / 과제

The background is unusually short. The patent states only that HBM is a 3D-stacked SDRAM interface used across GPUs, datacenter AI ASICs, CPUs, FPGAs, and supercomputers `[0001]`, and that "improvements are needed in the field of high bandwidth memory" `[0002]`. It then frames the state of the art it is departing from: current HBM can use **single-die 1T1C memory** `[0019]` — that is, one-transistor-one-capacitor DRAM built conventionally, on one die.

The second problem site is packaging. Memory-on-package (MoP) has been used for the best DDR performance and smallest footprint, but it raises package Z-height (by 300-350 μm in some architectures), and the coreless architecture used to mitigate that "can be an extremely expensive solution" `[0044]`, `[0045]`; controlling warpage adds a stiffener and area `[0046]`.

**Quotable spans:**
- `[0002]`: "However, improvements are needed in the field of high bandwidth memory."
- `[0019]`: "state-of-the-art approaches for high bandwidth memory (HBM) can include use of single die one-transistor one-capacitor (1T1C) memory"
- `[0045]`: "the use of a coreless architecture can be an extremely expensive solution"

## 청구항 분석 — 4-layer core mechanism

### Layer 1 — What (one sentence)

Each memory die in a stack carries **1T1C backend DRAM** (a one-transistor-one-capacitor cell whose transistor is a back-end/thin-film device, not a crystalline-silicon front-end device); the dies are stacked over — or without — a base die on a package substrate, and the stack is stitched together by TSV gutters and a UCIe I/O bundle routed through the base die, "with the goal of matching HBM4's footprint."

### Layer 2 — How (mechanism)

Structure (claim 1/6/11; description `[0020]`-`[0037]`):

1. Build each memory die (105/120/140) so its DRAM is **1T1C backend DRAM** — the cell's access transistor is a back-end-of-line / thin-film transistor, giving an ~1.5 GB die "based on back-end-of-line transistors" `[0027]`; FIG. 1F labels the stacked layers "TRANSISTOR" and "GM" as thin-film-transistor databases (151/153) `[0031]`.
2. Stack N such dies "8-high and beyond," wafer-to-wafer or die-to-die, thinning the silicon to enable many-layer stacking `[0023]`, `[0031]`.
3. Separate the sub-channels (161A-H) with four TSV gutters (162-165) per die and both-sided HBI connections, so data/control drop through signal TSVs to the die below `[0033]`, `[0034]`, `[0037]`.
4. Route all I/O to the compute die through a **base die** (115/130) carrying UCIe (132), test/controller/debug (133), and spare repair channels (134-137); the base die holds 4 die-sub-channels of redundant arrays as "fungible recoverability resources" for post-assembly repair `[0027]`, `[0034]`.
5. Size each XBM die to 0.5-5 GB with N datablocks "with the goal of matching HBM4's footprint"; channels run 2 GHz, the UCIe I/O 32 GHz `[0034]`.
6. Seat the stack on the package beside the compute/logic die (106) via an interposer, or in a memory-on-package / reversed-overhang form factor to cut Z-height and cost `[0022]`, `[0039]`, `[0053]`.

**Key components**: package substrate (101), interposer (102), HBM stack (104) of memory dies (105), logic die (106), die stack (111) with databases (113) and TSVs (114), base die (115/130) with UCIe (132), memory die (120/140), thin-film-transistor databases (151/153), TSV/HBI regions (152/154), basic building block (160) with sub-channels (161A-H) and TSV gutters (162-165), channel layout (170) channels 0-7 (172-179)

### Layer 3 — Why novel

- **Relative to prior art (as the patent frames it)**: the state of the art is single-die 1T1C HBM `[0019]`; this filing puts 1T1C DRAM on a stack of dies whose transistors are **backend** devices `[0020]`, `[0027]`, and funnels I/O through a UCIe base die with built-in redundancy `[0034]`. The patent's own contrast is "single die" → stacked backend-transistor dies.
- **Industry practice contrast (external, see fact-check-log)**: conventional DRAM (and therefore today's HBM) is made in a dedicated DRAM front-end (FEOL) fab on crystalline silicon; a back-end/thin-film access transistor is a low-temperature device that stacks in metal layers. The patent never says "logic fab," "foundry," or "without a DRAM fab" — that reading is an external strategic inference, not patent text. The patent's own words are "backend transistors," "1T1C backend DRAM," "back-end-of-line transistors," "thin film transistor."

### Layer 4 — Innovation angles

- **backend-cell-relocation**: the 1T1C DRAM cell is built from back-end transistors ("backend" is in claim 1; description elaborates thin-film-transistor / back-end-of-line)
  - Evidence paragraphs: `[0018]`, `[0020]`, `[0027]`, `[0031]`; claim 1 via Example 1 `[0069]`
  - Quote anchor refs: `q-0069-1`, `q-0027-1`, `q-0031-1`
- **match-hbm4-footprint-stack**: 8-high-and-beyond stack of backend-transistor dies, 0.5-5 GB each, explicitly aimed at HBM4's footprint
  - Evidence paragraphs: `[0023]`, `[0034]`
  - Quote anchor refs: `q-0023-1`, `q-0034-1`, `q-0034-2`
- **base-die-io-and-redundancy**: UCIe I/O + BIST + redundancy funneled through a base die, with post-assembly repair from redundant arrays
  - Evidence paragraphs: `[0020]`, `[0034]`; claims 3/4/5 via Examples `[0071]`-`[0073]`
  - Quote anchor refs: `q-0020-2`, `q-0034-5`, `q-0073-1`
- **memory-on-package-formfactor**: MoP and reversed-overhang packaging variants that cut Z-height and cost (secondary theme)
  - Evidence paragraphs: `[0044]`, `[0045]`, `[0053]`
  - Quote anchor refs: `q-0045-1`, `q-0053-1`

## Claim scope map

This is a PENDING APPLICATION (published 2026-07-02, no grant). Nothing here is locked in the granted sense: every "Locks" entry is **sought-locked** — required by the claim text as filed, still subject to examination. Phase 2 must narrate scope with sought-* vocabulary ("the claim as filed requires...", "Intel is claiming...", never "Intel owns/has secured..."). The single load-bearing claim word for the thesis is **"backend"**: claim 1 requires "1T1C **backend** DRAM." The specifics that make it HBM-competitive (thin-film transistor, 8-high, UCIe, TSV gutters, match-HBM4 goal, capacities, frequencies) are description or dependent claims, NOT independent-claim requirements.

| Claim | Locks (sought — required by claim text as filed) | Leaves open (description preference only) | Pins (approximate point limitations) |
|---|---|---|---|
| 1 (indep., structure) | a package substrate; a base die coupled to the package substrate; a memory die stack coupled to the base die; **each memory die comprises 1T1C backend DRAM** (the word "backend" is in the claim text) | The channel MATERIAL is never named (no oxide / IGZO / amorphous); "thin film transistor" and "back-end-of-line" are DESCRIPTION phrasings `[0031]`, `[0027]`, not claim 1 words; 8-high (claim 2), BIST (claim 3), redundancy (claim 4), sub-channels + TSV gutters (claim 5), UCIe / HBI / "match HBM4's footprint" / capacities / 2 GHz / 32 GHz are all description `[0020]`, `[0034]` or dependent claims | none in claim 1 (the "approximately 1.5 GB die," "about 9.5 mm" values are description `[0027]`, not claim limitations) |
| 6 (indep., structure, no base die) | a package substrate; a memory die stack coupled to the package substrate; each memory die comprises 1T1C backend DRAM (a base die is NOT required in this claim) | same dependent options (claims 7-10) | none |
| 11 (indep., computing device) | a board; a memory structure coupled to the board (either the base-die variant OR the no-base-die variant); each memory die comprises 1T1C backend DRAM | processor / communication chip / battery / camera / display / compass / GPS are dependent claims 14-20 | none |
| 2 / 7 (dep.) | the memory die stack comprises **eight** memory dies | — | "eight" is an exact count sought by the dependent claim (NOT required by claim 1/6); it is a count, not an "about" pin |
| 5 / 10 (dep.) | each memory die comprises a plurality of **alternating sub-channels and TSV gutters** | gutter count (four, `[0033]`), sub-channel count, UCIe routing are description | none |
| 3 / 8 (dep.) | each memory die comprises a built-in self-test (BIST) | BIST implementation is description | none |
| 4 / 9 (dep.) | each memory die comprises redundancy | redundancy scheme (base-die 32-datablock arrays, `[0034]`) is description | none |

Map rules honored downstream: "backend" is claim text (sought-locked); "thin film transistor" / "back-end-of-line" is the description's elaboration on description anchors; the **logic-foundry / no-DRAM-fab / cost / $-per-bit / yield / channel-material** reading is EXTERNAL strategic inference, never attributed to claim or description; 1T1C **keeps a capacitor** (relocated to the back-end, not removed — contrast the 2T0C capacitor-less path, fact-check-log `imec-2t0c-igzo`); never present "approximately 1.5 GB" or the die spans as a claim pin.

## Reference number table

Load-bearing numerals are drawn from the invention figures (FIG. 1A-1H); the packaging-variant figures (FIG. 2-6) and the boilerplate device figure (FIG. 7) are grouped at coarse granularity at the end.

| Number | Label | Paragraphs | Figures |
|---|---|---|---|
| 100 | package | `[0021]`, `[0022]` | FIG. 1A |
| 101 | package substrate | `[0022]` | FIG. 1A |
| 102 | interposer | `[0022]` | FIG. 1A |
| 103 | interconnect structures | `[0022]` | FIG. 1A |
| 104 | high bandwidth memory (HBM) stack | `[0022]` | FIG. 1A |
| 105 | like memory dies (in the stack) | `[0022]` | FIG. 1A |
| 106 | logic die | `[0022]` | FIG. 1A |
| 110 | memory structure (die stack) | `[0024]`, `[0025]` | FIG. 1B |
| 111 | stack of dies | `[0025]` | FIG. 1B |
| 112 | dies | `[0025]` | FIG. 1B |
| 113 | aligned databases (DBs) | `[0025]` | FIG. 1B |
| 114 | through silicon vias (TSVs) | `[0025]` | FIG. 1B |
| 115 | base die (bottom die of stack; may be omitted) | `[0025]` | FIG. 1B |
| 120 | memory die (first die option; ~9.5 mm × ~13.5 mm; ~1.5 GB) | `[0026]`, `[0027]` | FIG. 1C |
| 121 / 122 | die spans (~9.5 mm; ~13.5 mm) | `[0027]` | FIG. 1C |
| 123 | domains (e.g., 2 GHz) | `[0027]` | FIG. 1C |
| 124 / 125 / 126 | CP slice locations | `[0027]` | FIG. 1C |
| 130 | base die | `[0027]` | FIG. 1D |
| 131 | substrate (of base die) | `[0027]` | FIG. 1D |
| 132 | Universal Chiplet Interconnect Express (UCIe) | `[0027]` | FIG. 1D |
| 133 | test / controller / debug region | `[0027]` | FIG. 1D |
| 134 / 135 / 136 / 137 | spare channels for repair | `[0027]` | FIG. 1D |
| 138 | TSV regions | `[0027]` | FIG. 1D |
| 140 | memory die (second die option; no base die) | `[0028]`, `[0029]` | FIG. 1E |
| 141 / 142 / 143 | die spans; 32 GHz domain | `[0029]` | FIG. 1E |
| 150 / 150A | die-stack cross-section; exploded view | `[0030]`, `[0031]` | FIG. 1F |
| 151 / 153 | first / second thin film transistor database | `[0031]` | FIG. 1F |
| 152 / 154 | first / second region of TSV/HBI connections | `[0031]` | FIG. 1F |
| 155 / 156 / 157 | first / second / eighth-or-ninth wafer or die | `[0031]` | FIG. 1F |
| 160 | basic memory building block (XBM datablock) | `[0032]`, `[0033]`, `[0034]` | FIG. 1G |
| 161A-161H | sub-channel 0 through sub-channel 7 | `[0033]` | FIG. 1G |
| 162 / 163 / 164 / 165 | TSV gutter 0 / 1 / 2 / 3 | `[0033]` | FIG. 1G |
| 170 | channel layout for a die | `[0036]` | FIG. 1H |
| 171 | domains of sub-channels / regions | `[0036]` | FIG. 1H |
| 172-179 | channel 0 through channel 7 | `[0036]` | FIG. 1H |
| 200 / 205 / 220 / 221 / 222 / 225 / 230 / 235 | MoP package: package substrate, memory die stacks, memory package substrate, memory dies, mold layer, die module, interposer | `[0039]`-`[0042]` | FIG. 2 |
| 300 / 305 / 320 / 322 / 328 / 329 / 330 / 338 | embedded-MoP package: package substrate, memory die stacks, memory dies, mold layer, opening, die module, pads | `[0047]`-`[0052]` | FIG. 3, FIG. 4 |
| 500 / 504 / 506 / 524 / 526 / 534 / 536 | reversed-overhang system: memory stack, die-stack structure, DRAM substrate, pre-solder, plated through holes | `[0054]`-`[0055]` | FIG. 5 |
| 600 / 620 / 630 | reversed-overhang system with flat heat spreader (630) | `[0056]`, `[0057]` | FIG. 6 |
| 700 / 702 / 704 / 706 | computing device: board, processor, communication chip (context) | `[0059]`-`[0063]` | FIG. 7 |

## Figure relationships

| Figure | Paired with | Relationship | Page (if known) | Cover candidate? | Phase map (sequences only) |
|---|---|---|---|---|---|
| FIG. 1A | (standalone) | package cross-section: logic die (106) beside HBM stack (104) on one interposer/substrate — the co-package "thesis image" | sheet 1 (fig-01A.png) | alternate (best thesis-in-one-image: logic + memory on one package; 7 numerals, over the cover caption budget of 6) | — |
| FIG. 1B | (standalone) | angled/isometric view of the 8-high die stack (111) on a base die (115) | sheet 2 (fig-01B.png) | **yes — recommended** (highest feed force; depicts the claimed die stack, "8-high and beyond"; 6 numerals fits the cover caption budget) | — |
| FIG. 1C | FIG. 1D | first exemplary die option: memory die (120) plan view + its base die (130) plan view — a same-option pair | sheets 3-4 (fig-01C.png, fig-01D.png) | | — |
| FIG. 1E | (standalone) | second exemplary die option: memory die (140), no base die | sheet 5 (fig-01E.png) | | — |
| FIG. 1F | (has exploded inset 150A) | die-stack cross-section with an exploded view of the backend "TRANSISTOR"/GM layers — the most literal picture of the claimed backend-transistor cell | sheet 6 (fig-01F.png) | alternate (most literal "backend transistor" claimed-core depiction; dense at cover scale) | — |
| FIG. 1G | (standalone) | isometric schematic of the basic building block (160): sub-channels 161A-H + TSV gutters 162-165 | sheet 7 (fig-01G.png) | | — |
| FIG. 1H | (standalone) | channel-layout schematic (170): channels 0-7 | sheet 8 (fig-01H.png) | | — |
| FIG. 2 | (standalone) | memory-on-package (MoP) cross-section: memory die stacks (220) beside a die module on a package substrate | sheet 9 (fig-02.png) | | — |
| FIG. 3 | FIG. 4 | same embodiment, two views: MoP plan view (mold layer 328, opening 329, four stacks 320) + its cross-section (stacks embedded directly on substrate 305) — a plan/section pair (cropped from one shared sheet) | sheet 10 (fig-03.png, fig-04.png) | | — |
| FIG. 5 | FIG. 6 | reversed-overhang MoP variants: without (5) and with (6) a flat heat spreader (630) — an option pair | sheets 11-12 (fig-05.png, fig-06.png) | | — |
| FIG. 7 | (standalone context) | boilerplate computing-device block diagram | sheet 13 (fig-07.png) | | — |

## Quote anchor table

| Quote ID | Paragraph | Verbatim text | Significance |
|---|---|---|---|
| q-0002-1 | `[0002]` | "However, improvements are needed in the field of high bandwidth memory." | prior-art-contrast |
| q-0018-1 | `[0018]` | "Embodiments are directed to ultra high bandwidth memory (HBM) with backend transistors." | mechanism-critical |
| q-0019-1 | `[0019]` | "state-of-the-art approaches for high bandwidth memory (HBM) can include use of single die one-transistor one-capacitor (1T1C) memory" | prior-art-contrast |
| q-0020-1 | `[0020]` | "an approach involves the use of a stack of N memory dies containing 1T1C backend DRAM, through silicon via (TSV) gutters and both-sided high bandwidth interconnect (HBI) connections" | mechanism-critical |
| q-0020-2 | `[0020]` | "high speed universal chiplet interconnect express (UCIe) connections are included to funnel out the data from and XBM construct" | mechanism-critical |
| q-0023-1 | `[0023]` | "In accordance with an embodiment of the present disclosure, a die stacking cube is 8-high and beyond." | quantitative |
| q-0023-2 | `[0023]` | "In an embodiment, die stacking is achieved wafer-to-wafer." | mechanism-critical |
| q-0027-1 | `[0027]` | "can be an approximately 1.5 GB die based on back-end-of-line transistors" | quantitative |
| q-0031-1 | `[0031]` | "a first thin film transistor database 151, a first region 152 of TSV/HBI connections, a second thin film transistor database 153" | mechanism-critical |
| q-0031-2 | `[0031]` | "thinning of the silicon can be implemented to enable many-layer stacking" | mechanism-critical |
| q-0034-1 | `[0034]` | "With the goal of matching HBM4's footprint" | mechanism-critical |
| q-0034-2 | `[0034]` | "to have a die capacity of 0.5-5 GB" | quantitative |
| q-0034-3 | `[0034]` | "The channels operate at 2 GHz and are fully synchronous." | quantitative |
| q-0034-4 | `[0034]` | "The UCIe I/O operates at 32 GHz and serializes/deserializes data and control between the memory dies and compute die." | quantitative |
| q-0034-5 | `[0034]` | "The base die has 4 die-sub-channels of redundant memory arrays (32 datablocks) to act as fungible recoverability resources for unrepairable defects in the top memory dies." | mechanism-critical |
| q-0034-6 | `[0034]` | "There are four TSV gutters in each die, one carrying data and control for sub-channels 0-1, and another for sub-channels 2-3 and so on." | mechanism-critical |
| q-0045-1 | `[0045]` | "the use of a coreless architecture can be an extremely expensive solution" | prior-art-contrast |
| q-0053-1 | `[0053]` | "a dynamic random access memory (DRAM) package is reversely mounted to a system on chip (SOC) package through an extended DRAM substrate" | mechanism-critical |
| q-0069-1 | `[0069]` | "Each memory die in the die stack includes one transistor one capacitor (1T1C) backend dynamic random access memory (DRAM)." | claim-supporting |
| q-0069-2 | `[0069]` | "A base die is coupled to the package substrate." | claim-supporting |
| q-0070-1 | `[0070]` | "wherein the memory die stack includes eight memory dies" | claim-supporting |
| q-0073-1 | `[0073]` | "wherein each memory die in the die stack includes a plurality of alternating sub-channels and through-silicon via (TSV) gutters" | claim-supporting |
| q-0074-1 | `[0074]` | "A memory die stack is coupled to the package substrate." | claim-supporting |

> Note: the numbered claims (lines 144-163 of patent.md) carry no `[dddd]` paragraph anchors. Claim text is quoted via the Example-embodiment paragraphs, which mirror the claims: claim 1 ↔ Example 1 `[0069]`, claim 2 ↔ Example 2 `[0070]`, claim 5 ↔ Example 5 `[0073]`, claim 6 ↔ Example 6 `[0074]`, claim 11 ↔ Example 11 `[0079]`. The Examples say "includes" where the claims say "comprises" (the only difference); both wordings are verbatim-present in patent.md. Phase 2 cites the Example spans (anchored), and may attribute them as "the claim language as filed" only with the Example anchor attached.

## Timeline

- **Filing date**: 2024-12-26
- **Publication date**: 2026-07-02
- **Examination period**: 553 days filing→publication (standard ~18-month publication; application PENDING, no office-action record in the provided text)
- **Prior-art chronology**: no prior-art documents are cited in the provided patent.md text (the Background `[0001]`-`[0002]` names the HBM field and a need for improvement, not references):
  | Citation | Filing date | Publication date | Days relative to subject filing |
  |---|---|---|---|
  | (none cited in provided text) | — | — | — |

## Prior-art references + differentiation

No patent or literature citations appear in the provided text. Differentiation is argued against the state of the art the patent names inside its own description, and against industry practice established externally:

- **Single-die 1T1C HBM** (named at `[0019]`): the state-of-the-art HBM the patent departs from. This filing puts 1T1C DRAM on a stack of dies whose transistors are backend devices `[0020]`, `[0027]`.
- **Coreless / stiffener MoP packaging** (described at `[0044]`-`[0046]`): raises Z-height or cost; this filing offers MoP and reversed-overhang variants to cut Z-height and eliminate the stiffener `[0044]`, `[0053]`.
- **Industry baseline (external, fact-check-log)**: conventional DRAM — and today's HBM — is fabricated in a dedicated DRAM front-end (FEOL) fab on crystalline silicon, and the HBM supply is highly concentrated (SK hynix ~60% of HBM). Back-end/thin-film access transistors are low-temperature devices; the strategic reading that this loosens the DRAM-FEOL-fab bottleneck is external inference, never patent text. Incumbents (SK hynix, Samsung, Micron) are independently pursuing 3D DRAM toward ~2030; imec's capacitor-less BEOL path is 2T0C, NOT this filing's 1T1C.

## 유리한 효과 + 정량 데이터

The specification states effects sparingly and mostly as design goals rather than measured results. It gives no cost, yield, retention, bandwidth-vs-HBM4, or $-per-bit number. The quantified claims cluster on die capacity, stack height, and clock rates, and the load-bearing qualitative claim is that each die's DRAM is "based on back-end-of-line transistors" `[0027]` and the stack is architected "with the goal of matching HBM4's footprint" `[0034]`.

**Quotable spans:**
- `[0027]`: "can be an approximately 1.5 GB die based on back-end-of-line transistors"
- `[0034]`: "With the goal of matching HBM4's footprint"
- `[0034]`: "to have a die capacity of 0.5-5 GB"
- `[0023]`: "In accordance with an embodiment of the present disclosure, a die stacking cube is 8-high and beyond."

| Metric | Value | Paragraph |
|---|---|---|
| Die capacity (first die option) | approximately 1.5 GB, based on back-end-of-line transistors | `[0027]` |
| Die capacity (XBM die, match-HBM4 goal) | 0.5-5 GB | `[0034]` |
| Stack height | 8-high and beyond (up to 96 DB per sub-channel for 8-high; 192 for 16-high) | `[0023]`, `[0034]` |
| Datablocks per die | 768 (32 rows × 24 columns) | `[0037]` |
| Channel clock | 2 GHz, fully synchronous | `[0034]` |
| UCIe I/O clock | 32 GHz (bundle at 32 GT/s) | `[0034]` |
| Read/Write block size | 1-640 B | `[0034]` |
| Base-die redundancy | 4 die-sub-channels / 32 datablocks of redundant arrays for post-assembly repair | `[0034]` |
| Cost / yield / retention / $-per-bit / bandwidth-vs-HBM4 | not stated anywhere in the patent | — |
