# Figure Selection

## Selected figures

| Figure | File | Thesis point (spine element / section) | caption_role |
|---|---|---|---|
| FIG. 5 | fig-05.png | Claim 39's core step — memory channels (510) hardwired to array columns (515) with no switching element (4-memory-half; Axis 1) | header_composite |
| FIG. 1 | fig-01.png | What a systolic array is — DPU grid, weights top-down, tensor left-right (3-one-big-array; reader education) | body_figure_prose_covers_fully |
| FIG. 2 | fig-02.png | The combined-array package: ICs 215A-I composed into one array 250, memory chips on the top row, host over PCIe (3-one-big-array; claims 1/15 frame) | body_figure_carries_unique_info |
| FIG. 6 | fig-06.png | Division of labor — auxiliary circuitry (605) with private local memory (610) the arrays never touch (5-division-of-labor; claims 11-13) | body_figure_carries_unique_info |
| FIG. 7 | fig-07.png | Pipelining a transformer layer through one array row — the ≥98% utilization argument (5-division-of-labor) | body_figure_carries_unique_info |

## Cover candidate

**FIG. 5 (fig-05.png)** — tagged for the 5:2 header. It is the most literal picture of the
spine's claimed core step (claim 39 / claims 7-8: channels hardwired to columns, no
switch), and its visual hierarchy is strong at header crop: two labeled memory chips
sitting directly on top of four array columns, wires and nothing else in between — the
"no middlemen" thesis as a drawing. FIG. 2 was the runner-up (visually denser, but it
depicts claim 1's combined-array frame, not the memory-side step the spine leads on).

## Not selected (with reason)

| Figure | File | Reason |
|---|---|---|
| FIG. 3 | fig-03.png | Variant-family member of FIG. 2 (square grid, multiple memory chips per top-row IC). Its one unique point — add compute rows without adding memory chips `[0039]` — is carried in prose via q-0039-1. Argument economy. |
| FIG. 4 | fig-04.png | Variant-family member of FIG. 2 (unequal rows/columns). Adds sizing flexibility only; no spine point rests on it. |

## Paired-figure relationships (acknowledged)

| Figure(s) | Relationship | Treatment in selection |
|---|---|---|
| FIG. 1 + FIG. 2 | logical/physical pair (`[0028]`: FIG. 1 is the logical view of FIG. 2's distributed array) | BOTH selected — treated as one cognitive unit in 3-one-big-array; Phase 2 should place FIG. 1 before FIG. 2 so the logical view precedes the physical one |
| FIG. 2 + FIG. 3 + FIG. 4 | variant family (sizing variants, NOT a progressive sequence) | FIG. 2 selected as the family representative; FIG. 3/4 dropped — intentional, flagged in phase2-handoff-notes.md so Phase 2 does not reopen |
| FIG. 5 | standalone (memory-interface detail) | selected; cover candidate |
| FIG. 6 | standalone (extends FIG. 2 with auxiliary circuitry) | selected |
| FIG. 7 | standalone (timeline chart) | selected |

No progressive sequences exist in this application (no phase map / keyframe duty).

## Header / body assignment

- **Header**: FIG. 5 (cover candidate — the claimed core step as a drawing)
- **Body**: FIG. 1, FIG. 2, FIG. 6, FIG. 7 (in spine-section order 3 → 3 → 5 → 5)
