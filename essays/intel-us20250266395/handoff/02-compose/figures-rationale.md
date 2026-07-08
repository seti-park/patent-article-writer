# Figures Rationale (Compose placements)

Phase 1 intent: `handoff/01-design/figure-rationale.md` + `figure-selection.md`. This file
records Compose's ACTUAL placement decisions. The figure set, roles, and positions are
locked (`figures_locked`) for the run per `_shared/references/caption-roles.md`.

## FIG. 11 — header (cover)

- **Placement**: header
- **Rendering**: image-plus-caption (`figures/fig-11.png` embedded)
- **caption_role**: header_composite
- **Caption (as written)**: "FIG. 11: the filed method, end to end. The bridge is attached to the dies to form a multi-die assembly, the assembly goes through performance testing, and only an assembly that passes is attached to a target substrate. The test box sits before the substrate box, and that ordering is the whole story."
- **Decision note**: kept as cover per Phase 1 (the only figure depicting the claimed core step). 5:2 crop check done against the cleaned asset: the strip from the "Attach bridge component" box (1108) through "Performance testing" (1110) to "Attach MD bridge components that have passed to a target substrate" (1112) spans roughly 1300 x 520 px of the sheet, which is ~2.5:1 — the inversion + test gate survive the feed crop in one line. Fallback (fig-08 header) NOT triggered. Cover caption numeral count: 1 ("11"), within the ≤6 budget (SURF-003); steps are named, not numbered.

## FIG. 1 — body, §2 (2-flip-the-flow), end of section

- **Placement**: body-after-section-2
- **Rendering**: caption-only-italic
- **caption_role**: body_figure_prose_covers_fully
- **Caption (as written)**: `*FIG. 1: the multi-die bridge assembly in cross-section.*`
- **Decision note**: short identifier caption (8 words); §2 prose carries the anatomy (two dies, bridge underneath, signal across / power through) on `[0030]`, so the figure is a visual anchor only.

## FIG. 5A + 5B — body, §3 (3-test-before-substrate), end of section

- **Placement**: body-after-section-3
- **Rendering**: caption-only-italic
- **caption_role**: body_figure_carries_unique_info
- **Caption (as written)**: `*FIG. 5A and 5B: the tested object, prepped for a substrate. The bridge's underside carries either ball-pitch solder pads (526, FIG. 5A) or hybrid-bond contacts (536, FIG. 5B), the two ways down the description draws.*` (r2-F2 fix: 526 is the ball-pitch solder pads per the invention-summary `[0048]` reference row, not solder balls; upstream drift in Phase-1 figure-rationale.md flagged for the orchestrator.)
- **Decision note**: medium caption with the figure-unique data (526 vs 536 bottom-interface variants, `[0048]`); the pair is placed as one unit per the same-sheet selection.

## FIG. 7 — body, §4 (4-power-through-the-floor), after the EMIB-baseline paragraph

- **Placement**: body-section-4-after-baseline-paragraph
- **Rendering**: caption-only-italic
- **caption_role**: body_figure_carries_unique_info
- **Caption (as written)**: `*FIG. 7: the receiving substrate. A cavity (701) opens in the top surface; underneath, a glass layer (702) is patterned with through-glass vias (704) that run power toward the floor.*`
- **Decision note**: placed so the reader sees the bottom-to-cavity path before the prose walks the power mechanism; TGV is the caption's one glossed term, per Phase 1 intent.

## FIG. 8 — body, §4, after the cavity-mechanism paragraph

- **Placement**: body-section-4-after-[0035]
- **Rendering**: caption-only-italic
- **caption_role**: body_figure_carries_unique_info
- **Caption (as written)**: `*FIG. 8: the end state. The bridge (872) sits solder-attached at the cavity floor, the dies land across the substrate top on solder bumps (882), and one underfill (860) runs across the surface and down into the cavity.*` (r1-F2 fix: 882 attaches to the solder bumps per the invention-summary `[0056]` reference row, not to the dies.)
- **Decision note**: closes the visual arc (assembly → tested object → receiving substrate → seated end state) tracking §2 → §3 → §4, per Phase 1's body-figure order.

## Family-break handling (FIG. 9 / FIG. 10, and other unselected sheets)

Phase 1's family-break is preserved: FIG. 9 and FIG. 10 are NOT rendered. Per
`phase2-handoff-notes.md` ("If citing their variants, use `[0057]`/`[0058]` prose"), §4
covers them in one prose sentence with figure-number pointers on `[0057]`/`[0058]`, which
also satisfies `gate_figure_use`'s selected-set parse of `figure-selection.md` (the gate
reads every figure number in that file, including the acknowledged-pair rows — same
resolution as the etched-us20240378175-r2 run's FIG. 4 prose mention). Same treatment:
FIG. 2A/2B (bonding-option variant sheets, one pointer in §2), FIG. 6A (glass frame, one
pointer in the §4 glass paragraph on `[0049]`), FIG. 12 (boilerplate-context pointer in
§5's steelman, where it serves the read-cold concession). FIG. 3, 4, 13, 14, 15 are
neither rendered nor mentioned.
