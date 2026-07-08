---
essay_id: intel-us20250266395
patent_reference: US 2025/0266395 A1
spine_source: handoff/01-design/thesis-spine.md
draft_version: 3
mode_used: walkthrough
posture_used: measured
closing_posture: firm
---

# Intel Filed the Packaging Flow That Comes After EMIB-T

![FIG. 11: the filed method, end to end.](figures/fig-11.png)

FIG. 11: the filed method, end to end. The bridge is attached to the dies to form a multi-die assembly, the assembly goes through performance testing, and only an assembly that passes is attached to a target substrate. The test box sits before the substrate box, and that ordering is the whole story.

## The Next Flow Was Already on File

Fifteen months before Intel put EMIB-T on a conference stage, a filing from its packaging group had already written down a different way to build the same kind of chip package. In the flow Intel ships today, the little bridge die is buried in the board, and the chips land on top. The filed method bonds the bridge straight onto the chips first, then tests the whole cluster before a board ever enters the picture [0142]. The technology in the news is the bridge getting power vias. The filing is the bridge changing sides.

A bridge die is a small piece of silicon that carries the dense wiring between two bigger chips in one package. In EMIB-T, the version Intel detailed at the ECTC conference in May 2025, that bridge stays embedded in the package substrate, the board-like base the whole package is built on. New vias let power climb into it from the package bottom (Tom's Hardware; see Sources). The application in question was filed on 20 February 2024 and published in August 2025 as US 2025/0266395 A1 (Google Patents).

It takes the same powered-bridge idea and rebuilds the assembly order around it. That cuts two ways. This is the most concrete piece of after-EMIB-T assembly thinking on the public record. It is also a pending application: a set of claims Intel is asking for, not a product it has scheduled.

## The Bridge Changes Sides

Start with what the document claims as a method. In plain English: set two chips on a temporary carrier, mold them into one rigid piece, peel the carrier away, and bond a bridge across the two chips [0060], [0061]. The background names the industry's standing wish list, better "bump density, power efficiency, speed and bandwidth" [0001], but the move that matters here is about order, not materials. The bonded unit gets its own name, the multi-die bridge assembly, and the claim language as filed is worth reading in the original:

> "attaching a bridge component to a first portion of the first IC and a first portion of the second IC, to thereby create a multi-die bridge assembly"
> US 2025/0266395 A1, Example 21 [0142]

Then comes the half Intel's shipped bridge flow does not contain, the test-and-commit order:

> "testing the multi-die bridge assembly to determine whether it passes performance metrics; and attaching a substrate to the multi-die bridge assembly when the multi-die bridge assembly passes the performance metrics to thereby create a package assembly"
> US 2025/0266395 A1, Example 21 [0142]

That one step moves the dividing line: **the bridge stops being part of the board and becomes part of the chip cluster.**

In the drawings, the assembly is two dies joined by one bridge slung underneath them, a self-contained object with no substrate in sight [0030]. How the bridge is bonded to the dies is left open in the method claim itself. The filing claims hybrid bonding and solder separately, as options, and gives each its own variant sheet in FIG. 2A and 2B. Hybrid bonding is the premium route, and the apparatus claim carries it in claim text: insulating material "directly bonded" to insulating material, metal contacts bonded straight to metal contacts, with no solder in between [0122]. The description's example numbers put that contact spacing, the pitch, "in a range of 1 to 10 microns" on the bridge [0034]. A micron is a millionth of a meter, and those pitch numbers live in the description, not in any claim.

The other end of the assembly still lives in the old world, because "many substrates remain solder-attach components" [0025]. So one object bonds to chips at micron spacing on top while presenting ordinary solder interfaces below. That double life is the point.

*FIG. 1: the multi-die bridge assembly in cross-section.*

## The Test Comes While the Substrate Is Still on the Shelf

The flowchart in FIG. 11 is where the filing shows its hand. After the bridge attach, "the multi-die bridge assembly is subjected to testing to determine whether it passes performance metrics" [0061]. Only then does the expensive part arrive: "a substrate is attached to the multi-die bridge assembly after the multi-die bridge assembly passes the performance metrics" [0062]. The industry's term of art for this problem is the known-good die, learning that a chip is bad before you build anything more around it. The filing's own words are plainer: performance testing, passes, then attach.

The patent never puts a number on what that gate is worth, but industry arithmetic does. At 95 percent per die, a four-die package comes out about 81 percent good, and a twenty-die package about 35 percent (industry known-good-die figures; see Sources). The multiplication is nothing deeper than 0.95 times itself, die after die. One bad die can scrap the finished package.

That math is the industry's and this essay's, not the patent's. But it explains why a flow that grades the bonded cluster while the substrate is still on the shelf reads like an economic decision, not a manufacturing nicety. Only an assembly that has already passed its test gets to spend a substrate.

Scale sharpens it. Intel has discussed rolling out EMIB packages up to roughly 120 by 120 millimeters from 2026, carrying as many as twelve HBM memory stacks plus compute chiplets (single-outlet report; see Sources). That is exactly where the arithmetic turns brutal. Those numbers belong to the EMIB-T roadmap, not to this filing, whose drawings show a modest two dies on one bridge [0030]. The principle runs in the filing's favor, though: the more dies a package carries, the more it pays to test the cluster before committing anything else to it.

*FIG. 5A and 5B: the tested object, prepped for a substrate. The bridge's underside carries either ball-pitch solder pads (526, FIG. 5A) or hybrid-bond contacts (536, FIG. 5B), the two ways down the description draws.*

## Power Comes Up Through the Floor

Why rebuild the order at all? The background section is unusually candid about the bridge dilemma. "Passive bridge components are easier to fabricate and lower cost but cannot achieve the maximum current (Imax) that many applications require" [0024]. Active bridges answer with through-silicon vias, TSVs, vertical metal shafts running through the die so power and ground can cross it. But even there, "technical challenges, such as drilling, alignment, cavity filling and soldering remain" [0024]. Every bridge design lives between those two walls: too passive and the package starves for current, too active and the fabrication pain piles up.

Here is where the EMIB comparison earns its place, with one caution attached. The document never uses the word EMIB, and every link this essay draws to it rests on timeline and mechanism, not on anything Intel has said. In the EMIB flow Intel ships, the bridge is embedded in a cavity in the substrate first, and build-up layers are laminated over it (IEEE ECTC paper; see Sources).

The chips land last, on a board that already contains its bridge. EMIB-T, unveiled in May 2025, keeps that chips-last order and gives the embedded bridge TSVs, so power arrives from the package bottom instead of detouring around the bridge (Tom's Hardware; see Sources). This filing carries the same bottom-power idea into the inverted order.

*FIG. 7: the receiving substrate. A cavity (701) opens in the top surface; underneath, a glass layer (702) is patterned with through-glass vias (704) that run power toward the floor.*

In the cavity embodiments, the tested assembly is lowered onto a substrate whose top surface holds a cavity shaped for the bridge, and the description says what the through-bridge path is for: it "is often used to enable power to be routed into the bridge component" from "a source located at a bottom of a cavity in a substrate" [0035]. Even here the attach options stay open: solder at the cavity floor as drawn in FIG. 8, direct bonding in the FIG. 9 variant [0057], or a no-cavity version that solder-attaches the flipped assembly's die backsides instead, FIG. 10 [0058].

The claimed structure behind the power path is spare, just "at least one contact on the second surface that provides an electrical pathway to the first surface" [0123]. The payoff on offer is the one stated-effect sentence in the document: the routing "reduces the number of substrate routing layers and can improve product yield" [0035]. Note whose yield that is. The description ties it to the routing and the saved substrate layers, not to the test step.

*FIG. 8: the end state. The bridge (872) sits solder-attached at the cavity floor, the dies land across the substrate top on solder bumps (882), and one underfill (860) runs across the surface and down into the cavity.*

There is a quiet glass thread here: the bridge itself may be silicon, organic, or glass [0033]. A glass frame between the dies, drawn in FIG. 6A, is there "to provide structural stability" [0049]. And the receiving substrate can be built on a layer of glass shot through with through-glass vias, TGVs, the same vertical-power idea executed in glass [0054]. Example 17 even sizes it: "a layer of glass having a thickness in a range of 20 microns to 1.4 millimeters" [0138]. Intel announced glass-core substrates as a packaging direction in September 2023 (Intel newsroom; see Sources), and this filing is one of the places where the glass roadmap and the bridge roadmap touch. The ambition line sits at the end of the embodiments: assemblies like these may provide "the functionality conventionally associated with a monolithic system on chip (SoC)" [0059], big-chip behavior from a cluster of small ones.

## One Filing Among Hundreds, Except for One Claim

Now the objection, at full strength. Read cold, this is one filing among the hundreds Intel produces in a year. Its last four drawing sheets, beginning at FIG. 12, are generic wafer-and-device boilerplate, and its impressive numbers do not sit where the previous sections may have left the impression they do. The 1-to-10-micron pitch lives in the description's examples, and no claim carries it [0034]. The hybrid-bonding language sits in the apparatus claim, which requires the "directly bonded" stack but attaches no pitch to it [0122]. The through-via claim never says power, TSV, or cavity; it locks in only "at least one contact on the second surface that provides an electrical pathway to the first surface" [0123], and the power-from-the-floor purpose is the description talking [0035].

The dissection cuts deeper still. The glass-and-TGV claim, claim 17 as filed, hangs off the no-cavity inverted package of claim 16, not off the cavity packages described above. The parallel Example paragraph is written broader [0138]. The claim as filed is not.

No single claim contains the full architecture narrated above. And the document never mentions EMIB. The after-EMIB-T reading is this essay's synthesis of a filing date, an unveiling date, and a shared power-delivery idea. Intel has not connected the two documents.

Concede all of that, and look at what is left standing. The one thing the method claim as filed does lock is the part everything else orbits: the order of operations. Bridge to dies first, then "testing the multi-die bridge assembly", then a substrate "when the multi-die bridge assembly passes the performance metrics" [0142], with the cavity seating one dependent claim away, "placing the bridge component in the cavity" [0144]. The pitch numbers, the power path, the glass are the option space the description builds around that spine, each claimed narrowly somewhere or left deliberately open. That is what a serious packaging filing looks like: breadth around a locked core, not an absence of one. And the order plus the test gate is exactly the piece the public EMIB-T story does not have.

Price it accordingly. Every "locks" above is a lock Intel is asking for: this is a pending application, published in August 2025, eighteen months after its February 2024 filing, with no granted claim yet (Google Patents). Intel has also filed counterparts in Japan, Korea, China and Germany, which is fee money a company does not usually spend on ideas it considers dead (Google Patents).

Among the thirteen inventors is Ravindranath Mahajan, the Intel Fellow whose original silicon-bridge patents became the foundation of EMIB (IEEE EPS biography; see Sources). This came out of Intel's mainline packaging organization. That is the full weight the evidence supports: mainline provenance, international upkeep, no grant, no product.

## The Claim That Matters Is an Order of Operations

This filing is Intel's mainline packaging organization writing down the assembly flow that comes after the one it is currently selling. Bond the bridge to the chips first, test the cluster while no board is committed, then feed it power through the floor of a cavity. The claim that carries that flow is not a material and not a pitch number. It is an order of operations, filed fifteen months before EMIB-T had a name on a stage. Bond first, test before the board exists, power through the floor.

It is one pending application, and nothing in it schedules a product. The limits priced in the previous section stand as written, and none of them moves the call. What would move it is watchable and binary. If this flow is more than paper, die-first assembly and pre-substrate testing will start surfacing in Intel's packaging disclosures at venues like ECTC, or in this patent family's continued prosecution. If examination narrows the claims away from the test step, the staked-out-flow reading weakens with it. Either way, the tell will be in the documents. The paperwork moved first last time.

# Sources

## Patents
- US 2025/0266395 A1, "Multi-Die Bridge Assemblies and Methods for Three-Dimensional Packaging," Intel Corporation, priority 2024-02-20, published 2025-08-21, inventors: Jeremy D. Ecton, Minglu Liu, Mohamed R. Saber, Brandon Christian Marin, Bohan Shan, Ravindranath V. Mahajan, Benjamin T. Duong, Gang Duan, Srinivas V. Pietambaram, Suddhasattwa Nad, Kristof Darmawikarta, Zhiguo Qian, Rahul Manepalli. https://patents.google.com/patent/US20250266395A1/en

## Papers
- IEEE ECTC 2025, EMIB-T conference paper. https://ieeexplore.ieee.org/document/11038064/
- Ravindranath Mahajan biography, IEEE Electronics Packaging Society. https://eps.ieee.org/technology/9-about-cpmt/313-bio-mahajan.html

## Official statements
- Intel, "Intel Unveils Industry-Leading Glass Substrates" (September 2023). https://newsroom.intel.com/artificial-intelligence/intel-unveils-industry-leading-glass-substrates

## News & media
- Tom's Hardware, "Intel details new advanced packaging breakthroughs: EMIB-T paves the way for HBM4 and increased UCIe bandwidth" (May 2025). https://www.tomshardware.com/pc-components/cpus/intel-details-new-advanced-packaging-breakthroughs-emib-t-paves-the-way-for-hbm4-and-increased-ucie-bandwidth

## Technical specs
- IEEE ECTC, EMIB packaging technology overview. https://ieeexplore.ieee.org/document/9501629/
- Avecas, "Known-Good Die (KGD) strategies in chiplet assembly." https://avecas.in/known-good-die-kgd-strategies-chiplet-assembly/
