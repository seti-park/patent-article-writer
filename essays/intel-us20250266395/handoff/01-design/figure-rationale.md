# Figure Rationale

## FIG. 11 — Method flowchart (cover / header)

- **Purpose**: Shows the claimed order of operations end to end: assemble ICs on carrier with bond film → overlay encapsulant → detach carrier → attach bridge component (creating the MD bridge assembly) → performance testing → attach the PASSED assembly to the target substrate → optional system-package assembly (`[0060]`-`[0063]`; claim 19 via `[0142]`).
- **Intended effect**: The reader sees that the test box sits BEFORE the substrate box — the whole thesis in one glance. It also inoculates against the claim-scope steelman: what the flowchart shows is exactly what the method claim locks, no more.

## FIG. 1 — Multi-die bridge assembly concept

- **Purpose**: Establishes the object: two dies (106, 110) joined by a bridge component (102), with the signal path across the bridge (arrow 125) and the optional through-bridge power path (arrow 123) drawn as cartoon arrows (`[0030]`, `[0033]`, `[0035]`).
- **Intended effect**: Gives the reader their first mental model of "bridge" cheaply, so §2's prose can spend its budget on the ORDER inversion instead of the anatomy. (caption_role: body_figure_prose_covers_fully — short identifier caption; the two arrows are explained in prose.)

## FIG. 5A + 5B — The assembly, prepped for a substrate

- **Purpose**: Shows the finished multi-die bridge assembly as a self-contained unit wearing its substrate interface on the bottom: ball-pitch solder pads on the dies (520-1/520-2) and either ball-pitch solder pads (526, 5A) or hybrid-bond contacts (536, 5B) on the bridge's underside (`[0048]`).
- **Intended effect**: Makes "test it before the substrate exists" concrete — here is the discrete thing that gets tested and then shipped toward a cavity. The 5A/5B pair also quietly carries the solder-vs-hybrid-bond option space. (caption_role: body_figure_carries_unique_info — medium caption naming the two bottom-interface variants.)

## FIG. 7 — The receiving substrate (cavity + glass core + TGVs)

- **Purpose**: Shows what the assembly lands on: a substrate with a cavity formed in its top surface (`[0055]`) over a glass layer patterned with through-glass vias (702/704, `[0054]`) and RDL dielectric layers (`[0052]`).
- **Intended effect**: Sets up "power through the floor": the reader sees a path from the bottom of the package up into the cavity before §4 says the words. Also the one place the glass-substrate tie-in gets a visual. (caption_role: body_figure_carries_unique_info — medium caption; keep TGV as the one glossed term.)

## FIG. 8 — End state: bridge seated in the cavity

- **Purpose**: The after picture: bridge component (872) solder-attached to the cavity floor, dies solder-attached across the substrate top (882), one continuous underfill running across the surface and down into the cavity (860) (`[0056]`).
- **Intended effect**: Closes the visual arc (assembly → tested → seated) and shows the geometry that makes floor-fed power sensible: the bridge's underside is now the closest thing to the package's power inlet. Prose notes the FIG. 9 hybrid-bond and FIG. 10 no-cavity variants without showing them (`[0057]`, `[0058]`). (caption_role: body_figure_carries_unique_info — medium caption.)

## Not selected (rationale)

- **FIG. 2A-4B**: bonding-variant ladders (HB vs solder, with/without via, molded). Mechanism-depth beyond the reader profile's budget; `[0025]`/`[0034]` pitch prose + FIG. 1 carry the point.
- **FIG. 9 / FIG. 10**: attach-option alternatives to FIG. 8; showing them would re-spend §4's attention on options the Claim scope map already prices as open.
- **FIG. 6A/6B**: glass frame and inverted variants; one prose paragraph each at most.
- **FIG. 12-15**: USPTO boilerplate context (wafer, transistor stack, board, device diagram); no thesis load.
