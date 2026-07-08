# Intel's Filing Moves the DRAM Cell Into the Back-End

*This essay was prompted by a thread from @Underfox3, which flagged this Intel filing, its Cross-Batch Memory (XBM) design, and the move to a backend DRAM cell fed over UCIe links.*

![FIG. 1B: the claimed eight-high memory stack on its base die.](figures/fig-01B.png)

*FIG. 1B: the claimed memory tower. Identical memory dies stack eight-high and beyond as one die stack (111), stitched by vertical through-silicon vias (114) and seated on a base die (115) that routes every signal in and out.*

## A Memory Architecture From the Company That Left It

Intel's newest memory filing does something quietly radical. It builds the transistor inside each DRAM cell in the chip's back-end wiring layers, the low-temperature metal stacked on top. That is not where memory is normally made: DRAM has always been etched into the crystalline-silicon front-end below. The application says to stack those dies eight high, and to size the block to the footprint of HBM4, the newest generation of the high-bandwidth memory that feeds AI accelerators. Move the cell to the back-end and you change more than a spec. You change what kind of factory can build it.

That is a strange thing to find under Intel's name. Intel sold its NAND flash business to SK hynix in 2021 and wound down its Optane memory line the year after. Three companies make the world's HBM, and Intel sells none of it. This is one published application, not a product.

But its move is precise. Intel's filing moves the DRAM cell into logic-stackable back-end layers, and if the yield numbers land, who can make HBM stops being a three-company club.

## Claim 1 Turns on a Single Word: Backend

Strip the filing to its core claim and everything hangs on one word. One line states the whole idea: "Embodiments are directed to ultra high bandwidth memory (HBM) with backend transistors" [0018]. Claim 1, as filed, then requires that each memory die in the stack carry a particular kind of cell.

> "Each memory die in the die stack includes one transistor one capacitor (1T1C) backend dynamic random access memory (DRAM)."
> US 2026/0191095 A1, [0069]

A 1T1C cell is the standard unit of DRAM: one transistor to select a bit, one capacitor to hold it. That part is ordinary. The load-bearing word is backend.

In an ordinary memory chip, that transistor is etched into the crystalline silicon at the base of the die. Engineers call that layer the front-end. The back-end is everything stacked above it: the metal wiring, laid down at low temperature. Building the access transistor up there makes it a thin-film transistor. That is a device deposited as a thin coating in the wiring, rather than carved into the silicon below. The filing's description spells this out, showing thin-film-transistor layers stacked one atop another [0031]. It puts a size on one such die, at what "can be an approximately 1.5 GB die based on back-end-of-line transistors" [0027].

*FIG. 1F: the back-end cell, made literal. An exploded view of the stack shows the tiers labeled TRANSISTOR, the thin-film transistors (151, 153) that switch each cell, separated by regions of vertical interconnect (152, 154).*

That location is the whole story, and the honest part is what the filing does not do with it. The cell is 1T1C, which means it still has a capacitor, the tiny well of charge that stores each bit and the hardest thing in DRAM to shrink. The filing carries that capacitor up into the back-end alongside the transistor. **This is still a one-capacitor cell. The back-end move relocates DRAM's hardest part. It does not remove it.**

## A Tower Built to Match HBM4's Footprint

A single back-end die does not rival HBM. A tall stack of them might, and the filing is built to stack. It describes a memory cube stacked eight high and beyond [0023]. The silicon is thinned to allow that many-layer stacking [0031]. Data drops down the stack through what the patent calls TSV gutters: columns of through-silicon vias punched straight through each die. They split the traffic into many independent sub-channels, the parallel data lanes [0073]. A memory's bandwidth comes from their combined width.

*FIG. 1G: one memory building block. Eight sub-channels (161A to 161H) are divided by four vertical TSV gutters (162 to 165), the repeating tile the filing sizes toward HBM4's footprint.*

Everything leaves that stack through a base die at the bottom, a small controller chip that routes signals in and out. The base die carries the high-speed link to the processor over UCIe, or Universal Chiplet Interconnect Express [0020]. UCIe is an industry standard for wiring one chiplet to another. The base die also holds spare memory arrays that can stand in for defective ones once the stack is bonded [0034]. That is a built-in repair budget for a part that cannot be reworked after stacking.

The target is stated outright. Intel sizes each die "to have a die capacity of 0.5-5 GB" [0034]. It designs the whole block, in the document's words, "With the goal of matching HBM4's footprint" [0034]. That is a goal on the page, not a result on a bench: the filing reports no bandwidth, no cost, no yield to show the match was made.

## A Back-End Cell Could Loosen the DRAM-Fab Bottleneck

Here the filing's own words stop, and the reading begins. Claim 1 says backend. It never says foundry, never says logic fab, never says without a DRAM fab. What follows is a reading of what that one word could mean for who gets to make this memory, and the leap is mine, not the document's.

Today, DRAM and the HBM built from it are made in dedicated front-end fabs on crystalline silicon. That is a narrow door. The world's DRAM comes from just three makers, and in HBM the supply is tighter still: SK hynix alone holds around 60% of the market, with Samsung and Micron dividing most of the rest. When AI accelerators run short of memory, that narrow supply is the reason.

A back-end transistor is what could widen that door. Because it is deposited at low temperature in the wiring, it does not need the crystalline-silicon DRAM front-end that only a dedicated DRAM fab runs. A maker that already owns logic and advanced packaging, a foundry, could in principle carry an HBM-class memory through its own line rather than buy it from one of three suppliers. That is the strategic weight of the claim word. Backend belongs to the logic-and-packaging world, not the DRAM front-end.

*FIG. 1A: logic and memory on one package. A logic die (106) sits beside the high-bandwidth-memory stack (104), the two joined on a single interposer, the silicon bridge that wires the two dies together.*

This is not a lone paper. The same direction is public: Intel and SoftBank are co-developing a stacked memory called ZAM, or HB3DM, aimed squarely at beating HBM. The link is real but partial. ZAM's public signature is its diagonal Z-angle stacking; what this filing turns on is the back-end transistor cell, organized by vertical TSV gutters. Same goal, different document, and no ground for calling them one chip.

## Read Cold, It Is One Filing That Keeps the Capacitor

Read cold, the bear case is strong, and it should be put at full strength. It is a single published application, not a granted patent and not a product. Claim 1 fixes a single word. It never names the channel material, never claims a logic-compatible process, never promises a yield. The more radical path deletes the capacitor; in imec's capacitor-less cell, two thin-film transistors replace the storage capacitor entirely, and even that remains a lab result.

The incumbents, meanwhile, are not idle. SK hynix, Samsung and Micron each run their own 3D-DRAM programs, SK hynix's aimed at around 2030. One filing with no numbers, set against three funded roadmaps, could read as noise.

All of that is true, and none of it touches the one thing the claim does settle. The cell is backend. That is the property a logic-and-packaging line can carry without owning a DRAM front-end, which makes the open question the numbers, not the direction. The incumbents being on the 3D-DRAM road is not a rebuttal. It confirms the road is real, and this filing sketches a different lane onto it.

There is even a tell in Intel's own program. In ZAM, the partner reported to actually fabricate the DRAM is Powerchip, not Intel. That is what you would expect if the aim were a design-and-packaging capability, not a return to running a memory fab.

## The Direction Is Real; the Numbers Are the Test

Here is where this leaves an investor. The direction is not in doubt. The one thing claim 1 settles is that the memory cell is built in the back-end.

The bounds set out above still hold. One of them is the ceiling on the hype: this is 1T1C, so the capacitor was relocated into the back-end rather than removed. A back-end capacitor at HBM density and yield is precisely what no one has shipped.

The test is a number, and the calendar is short. Intel and SoftBank's ZAM is due to be presented at VLSI 2026 in June. Its density, yield and cost per bit will show whether this class of tall, stacked challenger can beat HBM4. That tests the class, not this filing's cell: ZAM is not established to use a back-end-transistor cell, and the back-end cell itself has no public proof point yet. The same technology family is aimed at commercialization around 2029. Those are the figures to watch.

If a back-end die matches HBM4 on capacity and yield at a workable cost, a foundry can quote HBM-class memory as a line item. The tightest bottleneck in AI hardware would gain a fourth door. If the numbers miss, the filing waits for the process to catch up.

The cell is in the back-end. Whether that becomes a fourth path to HBM is now a question of yield, not of architecture.

# Sources

## Patents
- US 2026/0191095 A1, "Ultra High Bandwidth Memory with Backend Transistors," Intel Corporation, priority 2024-12-26, published 2026-07-02, inventors: Abhishek Anil Sharma, Anand Iyer, Prashant Majhi, Nitin A. Deshpande.

## Papers
- imec, "Disrupting the DRAM roadmap: capacitor-less IGZO-DRAM technology." https://www.imec-int.com/en/articles/disrupting-dram-roadmap-capacitor-less-igzo-dram-technology

## News & media
- "SK hynix holds 62% of HBM; Micron overtakes Samsung." Astute Group. https://www.astutegroup.com/news/general/sk-hynix-holds-62-of-hbm-micron-overtakes-samsung-2026-battle-pivots-to-hbm4/
- "Global DRAM and HBM market share." Counterpoint Research. https://counterpointresearch.com/en/insights/global-dram-and-hbm-market-share
- "SK hynix set to overtake Samsung as DRAM leader amid the AI-driven memory boom." S&P Global Market Intelligence. https://www.spglobal.com/market-intelligence/en/news-insights/research/2025/05/sk-hynix-set-to-overtake-samsung-as-dram-leader-amid-ai-driven-memory-boom
- "Intel kills Optane memory business for good." Tom's Hardware. https://www.tomshardware.com/news/intel-kills-optane-memory-business-for-good
- "Intel is co-developing Z-Angle Memory (ZAM / HB3DM) to compete with HBM." Tom's Hardware (also names Powerchip, not Intel, as ZAM's DRAM fabricator). https://www.tomshardware.com/tech-industry/artificial-intelligence/intel-is-co-developing-new-z-angle-memory-to-compete-with-hbm-used-in-ai-data-centers-vertically-stacked-memory-touts-2-to-3x-more-capacity-greater-bandwidth-and-half-the-power-consumption
- "Intel / SoftBank reportedly to unveil ZAM-based HB3DM in June; bandwidth more than double HBM4." TrendForce. https://www.trendforce.com/news/2026/04/30/news-intel-softbank-reportedly-to-unveil-zam-based-hb3dm-in-june-bandwidth-more-than-double-hbm4/
- "Intel prepares HB3DM memory stacks with Z-Angle technology." TechPowerUp. https://www.techpowerup.com/348646/intel-prepares-hbm-killer-hb3dm-memory-stacks-with-z-angle-technology
- "SK hynix reveals DRAM development roadmap through 2031, including 3D DRAM." Tom's Hardware. https://www.tomshardware.com/pc-components/dram/sk-hynix-reveals-dram-development-roadmap-through-2031-ddr6-gddr8-lpddr6-and-3d-dram-incoming
