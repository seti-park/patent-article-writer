# Figure Selection

## Selected figures

| Figure | File | Thesis point (spine element / section) | caption_role |
|---|---|---|---|
| FIG. 11 | fig-11.png | The claimed core step: method flowchart with the performance-test gate between bridge attach and substrate attach (2-flip-the-flow, 3-test-before-substrate; cover) | header_composite |
| FIG. 1 | fig-01.png | What a multi-die bridge assembly is: two dies + bridge, signal path (125) across, optional power path (123) through (2-flip-the-flow) | body_figure_prose_covers_fully |
| FIG. 5A + 5B | fig-05AB.png | The finished multi-die assembly prepped for a substrate: solder-ball bottom (5A) vs hybrid-bond-in-cavity bottom (5B) — the object that gets tested, then dropped in (3-test-before-substrate) | body_figure_carries_unique_info |
| FIG. 7 | fig-07.png | The receiving substrate: cavity in the top, glass layer with TGVs underneath — where the power comes from (4-power-through-the-floor) | body_figure_carries_unique_info |
| FIG. 8 | fig-08.png | End state: bridge seated in the cavity, dies solder-attached across the top, underfill flowing into the cavity (4-power-through-the-floor) | body_figure_carries_unique_info |

## Paired-figure relationships (acknowledged)

| Figure(s) | Relationship | Treatment in selection |
|---|---|---|
| FIG. 5A + FIG. 5B | same-sheet variant pair (one file, fig-05AB.png) | selected as ONE unit — the solder-vs-hybrid-bond bottom variants are the point |
| FIG. 7 + FIG. 8 + FIG. 9 + FIG. 10 | progressive family (empty cavity substrate → solder attach → HB attach → no-cavity inverted) | FIG. 7 and FIG. 8 selected as the before/after keyframes per the Phase map (`[0052]`-`[0056]`); FIG. 9 (HB-in-cavity variant of 8) and FIG. 10 (no-cavity inverted) NOT selected — they are attach-option alternatives, not sequence steps; prose covers them on `[0057]`, `[0058]`. Family-break is intentional and flagged in phase2-handoff-notes.md |
| FIG. 2A/2B, 3A/3B, 4A/4B | same-sheet variant pairs (HB vs solder ladders) | NOT selected — mechanism detail the prose + FIG. 1 carry; each sheet would cost more attention than it pays for this spine |
| FIG. 6A / 6B | same-sheet pair (glass frame; inverted) | NOT selected — glass-frame tie-in is one paragraph on `[0049]`; no figure needed |
| FIG. 11 | standalone flowchart | selected as header/cover |
| FIG. 12-15 | standalone boilerplate context | NOT selected |

## Header / body assignment

- **Header / cover candidate**: FIG. 11 (fig-11.png) — the only figure that depicts the claimed core step itself (claim 19's bond → test → attach-on-pass order). Judged on claimed-step fidelity first: the flowchart IS the spine. For the 5:2 crop, the strip from "attach bridge component" through "performance testing" to "attach passed MD bridge to target substrate" carries the inversion + test gate in one line; keep the cover caption under 6 numerals (name the steps, not the 11xx labels).
- **Body**: FIG. 1, FIG. 5A+5B, FIG. 7, FIG. 8 (assembly → tested object → receiving substrate → seated end state: the visual argument tracks the spine order §2 → §3 → §4).
- **Fallback**: if the flowchart crops poorly at 5:2, FIG. 8 is the visual-force alternate (dense cross-section, bridge visibly sunk in the cavity), with FIG. 11 demoted to body at `body_figure_carries_unique_info`. Surface this to the orchestrator rather than deciding silently in Phase 2.
