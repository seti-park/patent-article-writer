# Invention Summary

## Metadata

- **Patent ID**: US 2025/0266395 A1 (published application; Appl. No. 18/582,203)
- **Title**: Multi-Die Bridge Assemblies and Methods for Three-Dimensional Packaging
- **Filing date**: 2024-02-20
- **Publication date**: 2025-08-21
- **Inventors**: Jeremy D. Ecton, Minglu Liu, Mohamed R. Saber, Brandon Christian Marin, Bohan Shan, Ravindranath V. Mahajan, Benjamin T. Duong, Gang Duan, Srinivas V. Pietambaram, Suddhasattwa Nad, Kristof Darmawikarta, Zhiguo Qian, Rahul Manepalli
- **Classification**: Int. Cl. H01L25/065; H01L23/00; H01L23/15; H01L23/48; H01L23/538; H01L25/00; H10B80/00. CPC incl. H01L25/0652; H01L23/15; H01L23/481; H01L23/5383-5386; H01L25/50; H10B80/00
- **Assignee**: Intel Corporation (Santa Clara, CA)

## 발명 명칭 / 기술분야

Essay-ready phrasing: a die-first bridge assembly flow for multi-chip packages. Two or more chips are bonded to a small "bridge" die FIRST (by hybrid bonding, solder, or thermal compression), the resulting multi-die bridge assembly is performance-tested BEFORE any package substrate is committed, and only a passing assembly is then attached to a substrate, typically by dropping the bridge into a cavity whose floor can feed power up through vias in the bridge. 기술분야: 3D semiconductor packaging — multi-die (chiplet) integration via bridge components, hybrid bonding interconnect (HBI), cavity substrates, and glass-core substrates with through-glass vias `[0022]`, `[0025]`.

## 종래 문제 / 과제

The background is short and cost/fabrication-centric: the industry push is toward better bump density, power efficiency, speed, and bandwidth in packaging `[0001]`, but existing die-to-die (D2D) and die-to-wafer (D2W) 3D approaches carry fabrication challenges and higher costs `[0022]`, with copper-to-copper bonding complexity called out specifically `[0023]`.

The bridge component itself is the second problem site `[0024]`: passive bridges (signal-only, one surface) are cheap but cannot carry the maximum current (Imax) many applications need; active bridges add through-silicon vias (TSVs) to route power and ground between surfaces and improve Imax, but drilling, alignment, cavity filling, and soldering remain unsolved pain points. A third, structural tension: hybrid bonding enables micron-class pitches, but most substrates are still solder-attach parts, so the two interconnect worlds must be integrated in one assembly `[0025]`.

**Quotable spans:**
- `[0001]`: "There is an ongoing push to improve bump density, power efficiency, speed and bandwidth in semiconductor packaging."
- `[0022]`: "However, many available D2D and D2 W methods and architectures face fabrication challenges and higher costs."
- `[0023]`: "One technical challenge to D2D and D2 W bonding is the complexity and high cost of copper-to-copper bonding technologies needed."
- `[0024]`: "Passive bridge components are easier to fabricate and lower cost but cannot achieve the maximum current (Imax) that many applications require."
- `[0024]`: "Active bridge components often include through silicon vias (TSVs) to route power and ground between surfaces, and thereby improve Imax; however, technical challenges, such as drilling, alignment, cavity filling and soldering remain."

## 청구항 분석 — 4-layer core mechanism

### Layer 1 — What (one sentence)

A multi-die bridge assembly is built dies-first (bridge bonded directly to two or more dies, hybrid bonding at the finest pitches), performance-tested as a unit before any substrate exists, and then attached to a substrate — in the cavity embodiments by seating the bridge in a cavity whose floor supplies power up through the bridge's TSVs/TGVs.

### Layer 2 — How (mechanism)

Method flow (FIG. 11, `[0060]`-`[0063]`; sought in claim 19, mirrored at Example 21 `[0142]`):

1. Assemble a first IC die and a second IC die on a carrier with an adhesive/bond film (1102).
2. Overlay an encapsulant/mold compound (1104) to stabilize the dies, then detach the carrier (1106).
3. Attach the bridge component (102) to a first portion of each die (1108) — by hybrid bonding at 1-10 micron pitch `[0034]`, solder bumps, TCB micro balls, or plating `[0033]` — creating the multi-die bridge assembly (100).
4. Subject the multi-die bridge assembly to performance testing (1110); only assemblies that pass proceed `[0061]`.
5. Attach the passing assembly to a substrate (1112): in cavity embodiments the bridge component (102/872/972) is placed into a cavity (701) and attached to the cavity floor by solder (FIG. 8), hybrid/direct bonding (FIG. 9), or adhesive `[0057]`, `[0062]`; a no-cavity inverted variant solder-attaches the die backsides instead (FIG. 10) `[0058]`.
6. Optionally assemble one or more package assemblies into a system package (1114) `[0063]`.

Power path: the bridge can carry TSVs/TGVs (arrow 123 / contacts 320-3) so power and ground enter from the cavity floor below, instead of detouring through extra substrate routing layers `[0035]`, `[0045]`. Substrate can carry a glass layer/core (702) with through-glass vias (704) `[0054]`.

**Key components**: multi-die bridge assembly (100), bridge component (102) — silicon, organic, or glass `[0033]`, dies IC 1/IC 2 (106/110), means for attachment (125: HBI 225-1 or solder field 225-2), through-bridge pathway (123 / contact 320-3), encapsulant (124), glass frame (628), substrate (700) with cavity (701), glass layer (702) + TGVs (704), method steps (1102-1114)

### Layer 3 — Why novel

- **Relative to prior art (as the patent frames it)**: passive bridges cannot reach the required Imax and active TSV bridges leave drilling/alignment/cavity-filling/soldering problems `[0024]`; the disclosed assemblies pair the TSV/TGV power path with an assembly order in which the bridge is bonded to the dies before the substrate — and the whole multi-die unit is tested before substrate attach `[0061]`, `[0062]`.
- **Industry practice contrast (external, see fact-check-log)**: Intel's shipped EMIB flow embeds the bridge in the substrate first and attaches the chips last (bridge is part of the board the chips land on); this filing inverts that order — the bridge becomes part of the chip cluster, and the substrate is the last, optional-to-commit component. The patent itself never uses the term "EMIB".

### Layer 4 — Innovation angles

- **assembly-order-inversion** (die-first bridge assembly; substrate last)
  - Evidence paragraphs: `[0060]`, `[0061]`, `[0062]`, `[0142]`
  - Quote anchor refs: `q-0142-1`, `q-0061-1`, `q-0062-1`
- **pre-substrate-performance-test** (test the multi-die unit before a substrate is committed)
  - Evidence paragraphs: `[0061]`, `[0062]`, `[0142]`
  - Quote anchor refs: `q-0061-2`, `q-0062-2`, `q-0142-2`
- **cavity-floor-power-delivery** (TSV/TGV bridge powered from the bottom of a substrate cavity)
  - Evidence paragraphs: `[0024]`, `[0035]`, `[0045]`, `[0123]`
  - Quote anchor refs: `q-0035-1`, `q-0035-2`, `q-0024-2`
- **hybrid-bond-meets-solder** (micron-pitch HBI integrated with solder-attach substrates in one assembly)
  - Evidence paragraphs: `[0025]`, `[0034]`, `[0122]`
  - Quote anchor refs: `q-0025-1`, `q-0034-1`, `q-0122-1`
- **glass-stack** (glass bridge option, glass frame, glass-core substrate with TGVs)
  - Evidence paragraphs: `[0033]`, `[0049]`, `[0054]`, `[0138]`
  - Quote anchor refs: `q-0033-1`, `q-0049-1`, `q-0054-1`

## Claim scope map

This is a PENDING APPLICATION (published 2025-08-21, no grant). Nothing here is locked in the granted sense: every "Locks" entry below is **sought-locked** — required by the claim text as filed, still subject to examination. Phase 2 must narrate scope with sought-* vocabulary ("the claim as filed requires...", "Intel is claiming...", never "Intel owns...").

| Claim | Locks (sought — required by claim text as filed) | Leaves open (description preference only) | Pins (approximate point limitations) |
|---|---|---|---|
| 1 (indep., assembly) | Bridge with metal contacts in two areas + at least one electrical pathway between the areas; two dies whose insulating materials are DIRECTLY BONDED to the bridge's insulating material and whose metal contacts are directly bonded to the bridge's contacts (i.e., hybrid bonding is in the claim text) | Pitch values (1-10 micron HBI, 25-55 micron solder `[0034]`) are description examples, NOT in any claim; bridge material (silicon/organic/glass `[0033]`) open; no substrate, no cavity, no TSV, no test required by claim 1 | none |
| 2 (dep. on 1) | At least one contact on the bridge's second surface providing an electrical pathway to the first surface (the through-bridge via structure) | The PURPOSE (power/ground from a cavity floor) is description only `[0035]`; claim 2 does not say "power", "TSV", or "cavity" | none |
| 11 (dep. on 8) | A glass structure between the dies, contacting the bridge's first surface (the glass frame) | Frame geometry ("glass ladder" plan view `[0049]`) open | none |
| 12 (indep.-style package on 1) | Substrate with RDL dielectric layers + cavity on top surface; assembly attached with bridge in the cavity | Attach means into the cavity open in 12 (13 = solder layer, 15 = direct bonding to cavity-floor pads) | none |
| 13 / 15 (packages on 2) | 13: layer of solder in the cavity, bridge solder-attached to it. 15: cavity floor has dielectric with metal pads, bridge DIRECT-BONDED to pads and dielectric-to-dielectric to the cavity floor | Underfill (14) optional; which power rails run through the via is unstated | none |
| 16 / 17 (package on 1, no cavity) | 16: inverted mount — die lower surfaces solder-attached to the substrate top. 17 (dep. on 16): substrate includes a layer of glass 20 microns to 1.4 millimeters thick with multiple through-glass vias | NOTE: as filed, the glass+TGV claim 17 hangs off the NO-CAVITY inverted package 16, not off the cavity packages 12-15 (Example 17 `[0138]` is written broader — "any one of Examples 12-16" — but the claim is not) | Claim 17 states an exact range (20 µm-1.4 mm), no "about"; description gives "about 20 microns to about 1.5 millimeter, +/-10%" `[0054]` — a description-level approximate range, not a claim pin |
| 18 (indep., package assembly) | Processing unit die + memory die + bridge with electrical pathways between them; substrate with cavity; bridge in the cavity | Attachment means fully open in 18 (no direct-bonding language) | none |
| 19 (indep., METHOD — the spine claim) | Order of operations: assemble two IC dies on a carrier with bond film → mold compound over them → detach carrier → attach bridge to the dies, creating the multi-die bridge assembly → TEST it against performance metrics → attach a substrate WHEN it passes | Bonding method for the bridge attach is OPEN in claim 19 (Examples 24/25 `[0145]`, `[0146]` claim hybrid bonding and solder as separate dependent options); no cavity required (that is claim 20); no TSV, no glass, no pitch numbers | none |
| 20 (dep. on 19) | Substrate has a cavity; attaching includes placing the bridge component in the cavity | Cavity-floor attach means open | none |

Map rules honored downstream: never present the 1-10 µm pitch, the power-from-cavity-floor purpose, or the glass options as required by the method claim; never call claim 17's exact range a pin or the description's "about" range a claim limit; never collapse sought-locked into granted-locked.

## Reference number table

Load-bearing numerals from the invention figures (FIGS. 1-11); the context figures (FIGS. 12-15) are grouped at the end. Multi-series numerals (102/202/302...) share one row.

| Number | Label | Paragraphs | Figures |
|---|---|---|---|
| 100 / 200 / 300 / 400 / 500 / 600 | multi-die bridge assembly | `[0030]`, `[0036]`, `[0045]`, `[0047]`, `[0048]`, `[0049]` | FIG. 1-6B |
| 102 / 202 / 302 / 402 / 502 / 602 | bridge component (silicon, organic, or glass) | `[0030]`, `[0033]` | FIG. 1-6A |
| 106 / 110 (206/210 etc.) | IC die 1 / IC die 2 (chiplets) | `[0030]`, `[0032]` | FIG. 1-6B |
| 108 / 112 | die I/O structures facing the bridge | `[0034]` | FIG. 1 |
| 120-1 / 120-2 (220/320/420/520/620) | die I/O contacts facing the substrate (bump pitch) | `[0032]` | FIG. 1-6 |
| 123 | optional through-bridge pathway arrow (TSV/TGV, power+ground) | `[0035]` | FIG. 1 |
| 124 / 424 / 624 | encapsulant / mold | `[0031]`, `[0047]`, `[0049]` | FIG. 1, 4A-4B, 6A |
| 125 | means for attachment (die-to-bridge) | `[0033]`, `[0034]` | FIG. 1 |
| 203 / 205 (303/305, 403/405) | bridge first (top) / second (bottom) surface | `[0038]`, `[0042]` | FIG. 2A-4B |
| 204 / 304 / 404 (-1, -2) | bridge hybrid-bond metal contacts, areas 1 and 2 | `[0042]`, `[0043]` | FIG. 2A, 3A, 4A |
| 208 / 212 (308/312, 408/412) | die-side hybrid bond contacts | `[0038]`, `[0041]` | FIG. 2A-4A |
| 225-1 | hybrid bonding interface (HBI) | `[0037]`, `[0043]` | FIG. 2A |
| 225-2 / 325-2 / 425-2 | solder / micro-bump field | `[0034]`, `[0044]` | FIG. 2B, 3B, 4B |
| 232 / 234 (332/334, 432/434) | solder bumps die-to-bridge | `[0044]`, `[0047]` | FIG. 2B, 3B, 4B |
| 240 / 340 / 440 / 540 / 640 | die-to-die electrical pathway through bridge | `[0042]` | FIG. 2-6 |
| 320-3 / 420-3 | contact on bridge second surface (through-via to first surface) | `[0045]`, `[0046]` | FIG. 3A-4B |
| 436 | underfill (die-to-bridge, solder embodiments) | `[0047]` | FIG. 4B |
| 520-1 / 520-2 / 526 | ball-pitch solder pads (dies; bridge bottom) | `[0048]` | FIG. 5A |
| 534 / 536 | HB contacts for bonding bridge in a cavity | `[0048]` | FIG. 5B |
| 628 | glass frame / glass structure | `[0049]` | FIG. 6A |
| 650-1 / 650-2 | solder bumps on die backsides (inverted assembly) | `[0050]` | FIG. 6B |
| 700 / 870 / 970 / 1070 | substrate | `[0052]` | FIG. 7-10 |
| 701 | cavity in substrate upper surface | `[0055]` | FIG. 7-9 |
| 702 / 802 / 902 / 1002 | layer of glass / glass core | `[0052]`, `[0054]` | FIG. 7-10 |
| 704 / 804 / 904 / 1004 | through-glass vias (TGVs) | `[0054]` | FIG. 7-10 |
| 724 / 730 (824/830 etc.) | substrate dielectric layers with RDL | `[0052]`, `[0053]` | FIG. 7-10 |
| 726 / 728 (826/828 etc.) | RDL vias and conductive traces | `[0052]` | FIG. 7-10 |
| 872 / 972 | bridge component (with TSVs/TGVs) attached in cavity | `[0056]`, `[0057]` | FIG. 8, 9 |
| 882 / 982 | solder bumps, dies to substrate top surface | `[0056]` | FIG. 8, 9 |
| 860 / 960 | underfill across substrate top and into cavity | `[0056]` | FIG. 8, 9 |
| 1020-1 / 1020-2 | solder attach of inverted assembly to cavity-less substrate | `[0058]` | FIG. 10 |
| 1100; 1102-1114 | method and method steps (assemble/mold/detach/attach bridge/test/attach substrate/system) | `[0060]`-`[0063]` | FIG. 11 |
| 1200 / 1202 | wafer / dies (context) | `[0065]` | FIG. 12 |
| 1300-series | integrated circuit detail: substrate 1302, device layer 1304, interconnect layers 1306-1310, structures 1328a/b, contacts 1336 (context) | `[0066]`-`[0084]` | FIG. 13 |
| 1400-series | microelectronic assembly: board 1402, interposer 1404, components 1420/1424/1426/1432 (context) | `[0086]`-`[0096]` | FIG. 14 |
| 1500-series | electrical device block diagram: processor 1502, memory 1504, comms 1512 etc. (context) | `[0097]`-`[0111]` | FIG. 15 |

## Figure relationships

| Figure | Paired with | Relationship | Page (if known) | Cover candidate? | Phase map (sequences only) |
|---|---|---|---|---|---|
| FIG. 1 | (standalone; concept for 2-6) | master cross-section with cartoon arrows (signal 125 / power 123) | sheet 1 (fig-01.png) | | |
| FIG. 2A | FIG. 2B | same-sheet variant pair: hybrid bond vs solder, no through-via | sheet 2 (fig-02AB.png) | | |
| FIG. 3A | FIG. 3B | same-sheet variant pair: adds through-bridge contact 320-3 | sheet 3 (fig-03AB.png) | | |
| FIG. 4A | FIG. 4B | same-sheet variant pair: mold encapsulation; 4B adds underfill | sheet 4 (fig-04AB.png) | | |
| FIG. 5A | FIG. 5B | same-sheet variant pair: assembly prepped for substrate (solder-ball bottom vs HB-in-cavity bottom) | sheet 5 (fig-05AB.png) | | |
| FIG. 6A | FIG. 6B | same-sheet pair: glass frame variant; inverted (bridge-on-top) variant | sheet 6 (fig-06AB.png) | | |
| FIG. 7 | FIG. 8, 9, 10 | progressive family: empty cavity substrate (7) → solder attach in cavity (8) → hybrid bond in cavity (9) → no-cavity inverted attach (10) | sheets 7-10 | | 7 = substrate per `[0052]`-`[0055]`; 8 = solder `[0056]`; 9 = HB `[0057]`; 10 = inverted `[0058]` (alternatives after 7, not time steps) |
| FIG. 11 | (standalone) | method flowchart incl. the performance-testing step | sheet 11 (fig-11.png) | **yes** — the only figure that depicts the claimed core step (claim 19's test-before-substrate order) | flow per `[0060]`-`[0063]` |
| FIG. 12-15 | (standalone context) | boilerplate context figures (wafer, IC stack, board assembly, device) | sheets 12-15 | | |

## Quote anchor table

| Quote ID | Paragraph | Verbatim text | Significance |
|---|---|---|---|
| q-0001-1 | `[0001]` | "There is an ongoing push to improve bump density, power efficiency, speed and bandwidth in semiconductor packaging." | prior-art-contrast |
| q-0023-1 | `[0023]` | "One technical challenge to D2D and D2 W bonding is the complexity and high cost of copper-to-copper bonding technologies needed." | prior-art-contrast |
| q-0024-1 | `[0024]` | "Passive bridge components are easier to fabricate and lower cost but cannot achieve the maximum current (Imax) that many applications require." | prior-art-contrast |
| q-0024-2 | `[0024]` | "Active bridge components often include through silicon vias (TSVs) to route power and ground between surfaces, and thereby improve Imax; however, technical challenges, such as drilling, alignment, cavity filling and soldering remain." | prior-art-contrast |
| q-0025-1 | `[0025]` | "many substrates remain solder-attach components, having solder-based interconnects for electrical communication with IC dies" | mechanism-critical |
| q-0025-2 | `[0025]` | "HBI advantageously enables "small" pitches (defined herein as a pitch less than 10 microns+/−10%, and in some cases, the pitch is less than 1 micron+/−10%)" | quantitative |
| q-0033-1 | `[0033]` | "The bridge component 102/202/302/402/502/602 may be embodied as a conventional silicon bridge, an organic bridge, a glass bridge, or some combination thereof." | mechanism-critical |
| q-0034-1 | `[0034]` | "When the means for attachment 125 is HBI, the HBI pitch on the bridge components 102 is smaller still, in a range of 1 to 10 microns." | quantitative |
| q-0035-1 | `[0035]` | "In practice, the optional cartoon arrow 123 is often used to enable power to be routed into the bridge component 102 from a source located at a bottom of a cavity in a substrate." | mechanism-critical |
| q-0035-2 | `[0035]` | "The electrical pathways or routing indicated by optional cartoon arrow 123 reduces the number of substrate routing layers and can improve product yield." | quantitative |
| q-0049-1 | `[0049]` | "The glass frame (also referred to herein as a glass structure) is to provide structural stability for the die 606 and die 610." | mechanism-critical |
| q-0054-1 | `[0054]` | "The TGVs 704 are volumes in which glass is removed and conductive materials are placed in the volumes, sufficient to enable electrical communication from an upper surface 703 to a lower surface." | mechanism-critical |
| q-0059-1 | `[0059]` | "The above embodiments may provide, in a multi-die package assembly, the functionality conventionally associated with a monolithic system on chip (SoC)." | claim-supporting |
| q-0061-1 | `[0061]` | "At 1108, a bridge component is attached to a first portion of the first IC and a first portion of the second IC, to thereby create a multi-die bridge assembly." | mechanism-critical |
| q-0061-2 | `[0061]` | "At 1110, the multi-die bridge assembly is subjected to testing to determine whether it passes performance metrics." | claim-supporting |
| q-0062-1 | `[0062]` | "At 1112, a substrate is attached to the multi-die bridge assembly after the multi-die bridge assembly passes the performance metrics." | claim-supporting |
| q-0062-2 | `[0062]` | "wherein the substrate has a cavity, the multi-die bridge assembly is attached to the substrate such that the bridge component is placed in the cavity" | claim-supporting |
| q-0122-1 | `[0122]` | "wherein the first insulating material is directly bonded to the second insulating material and some first metal contacts are directly bonded to a respective second metal contact" | claim-supporting |
| q-0123-1 | `[0123]` | "further comprising at least one contact on the second surface that provides an electrical pathway to the first surface" | claim-supporting |
| q-0138-1 | `[0138]` | "the substrate includes a layer of glass having a thickness in a range of 20 microns to 1.4 millimeters" | claim-supporting |
| q-0142-1 | `[0142]` | "attaching a bridge component to a first portion of the first IC and a first portion of the second IC, to thereby create a multi-die bridge assembly" | claim-supporting |
| q-0142-2 | `[0142]` | "testing the multi-die bridge assembly to determine whether it passes performance metrics; and attaching a substrate to the multi-die bridge assembly when the multi-die bridge assembly passes the performance metrics to thereby create a package assembly" | claim-supporting |
| q-0144-1 | `[0144]` | "wherein the substrate has a cavity and attaching the substrate to the multi-die bridge assembly includes placing the bridge component in the cavity" | claim-supporting |
| q-0030-1 | `[0030]` | "FIG. 1 is a simplified cross-sectional illustration of a multi-die bridge assembly 100 comprising a bridge component 102 and two integrated circuit dies die 106 (IC 1) and die 110 (IC 2)." | mechanism-critical |

> Note: claims carry no `[dddd]` paragraph anchors in patent.md. Claim text is quoted via the Examples paragraphs, which mirror the claims: claim 1 ↔ Example 1 `[0122]`, claim 2 ↔ Example 2 `[0123]`, claim 17 ↔ Example 17 `[0138]` (Example is written broader than the claim — see Claim scope map), claim 19 ↔ Example 21 `[0142]` (wording differs trivially: Example says "over the first IC and second IC", claim says "over the first IC die and the second IC die"), claim 20 ↔ Example 23 `[0144]`. Phase 2 quotes the Example spans, and may attribute them as "the claim language as filed" only with the Example anchor attached.

## Timeline

- **Filing date**: 2024-02-20
- **Publication date**: 2025-08-21
- **Examination period**: 548 days filing→publication (standard 18-month publication; application PENDING, no office-action record in the provided text)
- **Prior-art chronology**: no prior-art documents are cited in the provided patent.md text (the Background names problem classes, not references):
  | Citation | Filing date | Publication date | Days relative to subject filing |
  |---|---|---|---|
  | (none cited in provided text) | — | — | — |

## Prior-art references + differentiation

No patent or literature citations appear in the provided text. Differentiation is argued against practice categories inside the patent's own description:

- **Passive bridge components** (described at `[0024]`): signal-only pathways on one surface; cheap but Imax-limited. This filing's bridge optionally carries TSVs/TGVs for power/ground between surfaces (`[0035]`, claim 2 via `[0123]`).
- **Active TSV bridge components** (described at `[0024]`): improve Imax but leave drilling, alignment, cavity filling, and soldering challenges. This filing's answer is architectural: bond the bridge to the dies first (multiple attach options `[0033]`), test the unit `[0061]`, then commit a substrate `[0062]`.
- **Industry baseline (external, fact-check-log)**: Intel's shipped EMIB flow embeds the bridge in the substrate before any die attaches (chips-last); EMIB-T (announced ECTC 2025) adds TSVs to the embedded bridge for bottom-side power. This filing shares the TSV-bridge power idea but inverts the assembly order and inserts a pre-substrate test.

## 유리한 효과 + 정량 데이터

The specification states effects sparingly; the quantified ones cluster on pitch and on the through-bridge power path. The routing/yield effect is tied to the TSV/TGV pathway `[0035]`; the pre-substrate test's economic effect (only passing assemblies consume a substrate) is stated as flow order `[0061]`-`[0062]`, not quantified. The assemblies collectively aim at SoC-class functionality from disaggregated dies `[0059]`.

**Quotable spans:**
- `[0035]`: "The electrical pathways or routing indicated by optional cartoon arrow 123 reduces the number of substrate routing layers and can improve product yield."
- `[0025]`: "HBI advantageously enables "small" pitches (defined herein as a pitch less than 10 microns+/−10%, and in some cases, the pitch is less than 1 micron+/−10%)"
- `[0062]`: "At 1112, a substrate is attached to the multi-die bridge assembly after the multi-die bridge assembly passes the performance metrics."
- `[0059]`: "The above embodiments may provide, in a multi-die package assembly, the functionality conventionally associated with a monolithic system on chip (SoC)."

| Metric | Value | Paragraph |
|---|---|---|
| HBI pitch ("small" pitch definition) | < 10 µm ±10%, some cases < 1 µm ±10% | `[0025]` |
| HBI pitch on the bridge component | 1-10 µm | `[0034]` |
| Solder bump pitch, die-to-bridge | 45 ±10% to 55 ±10% µm (or 25-35 µm) | `[0034]` |
| Die-to-substrate bump pitch example | 110-86 µm (IC 1), 110-95 µm (IC 2) | `[0032]` |
| Glass layer thickness (description) | about 20 µm to about 1.5 mm, ±10% | `[0054]` |
| Glass layer thickness (claim 17 as filed / Example 17) | 20 µm to 1.4 mm | `[0138]` |
| Substrate panel X/Y lengths | 10 mm to 500 mm each | `[0054]` |
| Effect of through-bridge routing | fewer substrate routing layers; can improve product yield | `[0035]` |
