# Figure Selection

## Selected figures

| Figure | File | Thesis point (spine element / section) | caption_role |
|---|---|---|---|
| FIG. 5 | fig-05.png | COVER — the claim-39 core step made literal: memory channels (510) hardwired by wires (520) to array columns (515), no switching element (3-memory-half; Axis 1/3) | header_composite |
| FIG. 1 | fig-01.png | Systolic-array primer: DPU grid, weights fall from the top, tensors flow left to right; two multiplications share one array (splittable) (2-origin-array) | body_figure_prose_covers_fully |
| FIG. 2 | fig-02.png | The package gestalt: nine ICs fused into one combined array (250), host (205) on PCIe (240), memory chips (210) on the top row — the logical FIG. 1 made physical per `[0028]` (2-origin-array) | body_figure_carries_unique_info |
| FIG. 3 | fig-03.png | Memory economy of the grid: multiple memory chips per top-row IC; add rows of compute without adding memory `[0039]`, `[0040]` (3-memory-half) | body_figure_prose_covers_fully |
| FIG. 6 | fig-06.png | Division of labor: auxiliary circuitry (605) beside each local array (220), with private local memory chips (610) the arrays never touch `[0051]` (4-division-of-labor) | body_figure_carries_unique_info |
| FIG. 7 | fig-07.png | Pipelining one transformer layer through a row of the combined array: batches back-to-back, the Time B layer-norm stall, 98%+ utilization; description-only status flagged (4-division-of-labor) | body_figure_carries_unique_info |

NOT selected: FIG. 4 (fig-04.png) — variant pair of FIG. 3 (unequal vs equal rows/columns,
`[0041]`). The load-bearing memory-economy point is FIG. 3's; FIG. 4 adds only the
unequal-grid nuance, which the spine does not use. Pair-break is intentional and flagged in
phase2-handoff-notes.md; do not reopen.

## Paired-figure relationships (acknowledged)

| Figure(s) | Relationship | Treatment in selection |
|---|---|---|
| FIG. 1 + FIG. 2 | logical/physical pair (`[0028]`: FIG. 1 is the logical view of FIG. 2's array 250) | BOTH selected, placed together in 2-origin-array in that order (logical first, physical second) |
| FIG. 3 + FIG. 4 | variant pair (equal vs unequal grid, `[0041]`) | FIG. 3 selected, FIG. 4 dropped — BROKEN intentionally, see phase2-handoff-notes.md |
| FIG. 5 | standalone | selected as COVER (header) |
| FIG. 6 | standalone | selected, 4-division-of-labor |
| FIG. 7 | standalone (single chart, not a sequence) | selected, 4-division-of-labor |

## Header / body assignment

- **Header (cover candidate)**: FIG. 5 — judged on both cover criteria: (a) it depicts the
  claimed core step of the locked spine (claim 39's channel-to-column hardwiring, the
  essay's central object) rather than generic context; (b) card survival: large clean
  blocks, straight wire runs, and few labels stay legible at 5:2 feed-card scale, where
  FIG. 2/3 read as dense wiring diagrams and FIG. 7 becomes an unreadable stripe chart.
  Feed rule for Phase 2: cover caption ≤ 6 distinct reference numerals (SURF-003) — FIG. 5
  needs only four numeral families (505 memory chips, 510 channels, 515 columns, 520 wires);
  leave 215/220 out of the cover caption.
- **Body**: FIG. 1, FIG. 2 (2-origin-array, in that order); FIG. 3 (3-memory-half, after the
  FIG. 5 walk); FIG. 6, FIG. 7 (4-division-of-labor).

<!--
  > Revision note — none. Selection made after invention-summary §Figure relationships was
  complete; no retroactive pair fixes were needed.
-->
