# Figures Rationale (Compose placements)

figures_locked: yes — the set below (5 figures, roles, positions) is locked for the run per
`_shared/references/caption-roles.md`; changes only on an explicit Phase-3 finding.

## FIG. 5 — header (cover)

- **Placement**: header
- **Rendering**: image-plus-caption
- **caption_role**: header_composite
- **Caption (as written)**: `*FIG. 5: the claimed core step as a drawing. Two memory chips (505A, 505B) sit above one IC (215), and each independent channel (510A to 510D) runs over its own wires (520) straight into a dedicated column (515A to 515D) of the chip's systolic array (220) [0044]. No switch, no crossbar, nothing between memory and math. This is the interface the application claims, as drafted, in claim 39 [0016].*`
- **Decision note**: Phase 1's cover candidate adopted unchanged. The header carries the origin-document frame before a word is read: the claim-39 core step (channels hardwired to columns, no switching element) as hardware. Caption is application-era ("the application claims, as drafted") per figure-rationale's caption note. Also referenced in §4 body prose ("FIG. 5 is the whole argument in one picture" — layout self-reference dropped round 2, r2-F2) so the header image does thesis work inside the argument, not just above it.

## FIG. 1 — body, §3 (one-big-array), after the mental-model paragraph

- **Placement**: body-section-3-after-[0021]
- **Rendering**: caption-only-italic
- **caption_role**: body_figure_prose_covers_fully
- **Caption (as written)**: `*FIG. 1: a systolic array, logically. Weights (110) come down from the top [0021], data (115) comes in from the left, and every crossing of the two is a multiply-and-add.*`
- **Decision note**: reader-education figure; §3's opening paragraph carries the full mechanism (weights fall from the top, tensor flows from the left, every cell multiplies and adds). Self-audit round 1 (sa1A-F5): identifier-only caption gave the captions-first skimmer nothing, so one compressed claim clause was added (worded to avoid a body echo; [0021] anchors the weights-from-top clause, the 115-from-left flow is figure content). Role stays prose_covers_fully — the body remains the full treatment. Placed BEFORE FIG. 2 per figure-selection's logical-before-physical pairing rule ([0028] pair).

## FIG. 2 — body, §3 (one-big-array), after the composition paragraph

- **Placement**: body-section-3-after-[0039]
- **Rendering**: caption-only-italic
- **caption_role**: body_figure_carries_unique_info
- **Caption (as written)**: `*FIG. 2: the package (201). ICs 215A to 215I, each carrying an array tile (220), join through horizontal (230) and vertical (225) chip-to-chip connections into Combined Systolic Array 250. Memory chips (210A to 210C) sit only on the top row, and the host computer (205) connects over a standard PCIe link (240).*`
- **Decision note**: carries figure-unique topology (which connections are where; memory only on the top row; host over PCIe) that the prose deliberately does not re-enumerate. Self-audit round 1 (sa1A-F3): "host (205) ... over PCIe (240)" got a minimal gloss ("host computer", "standard PCIe link") for the captions-first reader. Medium caption with the reference numerals. Placed after FIG. 1 as its physical realization.

## FIG. 6 — body, §5 (division-of-labor), after the [0051] blockquote paragraph

- **Placement**: body-section-5-after-[0051]
- **Rendering**: caption-only-italic
- **caption_role**: body_figure_carries_unique_info
- **Caption (as written)**: `*FIG. 6: division of labor. Each IC (615A to 615D) holds an array tile (220) plus an auxiliary-circuitry block (605). The local memory chips (610A to 610D) are reachable only by that auxiliary circuitry.*`
- **Decision note**: caption follows the SPECIFICATION labels (605 = auxiliary circuitry, 610 = local memory chips), correcting the figures-manifest one-liner's swap, per phase2-handoff-notes trap T7 and the invention-summary reference-number table.

## FIG. 7 — body, §5 (division-of-labor), after the pipelining paragraph

- **Placement**: body-section-5-after-[0057]
- **Rendering**: caption-only-italic
- **caption_role**: body_figure_carries_unique_info
- **Caption (as written)**: `*FIG. 7: pipelining one array row. Attention queries, keys, and values, projection, and the MLP layers follow each other through the row, and at Time A a new computation has already entered while the previous one drains. The only idle gap is the layer-normalization stall, marked at Time B [0057].*`
- **Decision note**: carries figure-unique data (the stage sequence, Time A/Time B, the single stall) grounding the ≥98% utilization claim; medium caption names the marks and the stall per figure-rationale's intent. Revised round 2 (r2-F1): the two ticks are marked instants, not interval bounds — the stage sequence spans the full time axis, Time A marks the pipelining overlap (new computation entered while the previous drains), Time B marks the layer-normalization stall, and B precedes A on the axis. Caption re-anchored accordingly; verified against fig-07.png and the reviewer's quoted [0056]/[0057] evidence.

## FIG. 3, FIG. 4 — NOT placed (intentional, Phase 1 decision honored)

- **Placement**: omitted from the draft
- **Decision note**: sizing-variant family of FIG. 2, dropped by Phase 1 for argument economy (figure-selection.md). Their one load-bearing point (more compute rows without more memory chips, weights reused down the rows) travels in §3 prose via q-0039-1 `[0039]`. Not reopened per trap T7; the omission is recorded in the draft's `[^figures-not-placed]` footnote audit.
