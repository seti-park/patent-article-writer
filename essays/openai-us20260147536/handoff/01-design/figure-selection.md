# Figure Selection

## Figure-enabled edition (supersedes the earlier text-only declaration)

The figures arrived after the first pass: the owner uploaded the 64 USPTO drawing sheets
(input/figures-raw/figs1-3.zip), and Phase 0 cleaned a priority set to
`input/figures/fig-NN.png` (available set in `handoff/01-design/figures-index.txt`:
1, 2, 3, 4, 6, 38, 42, 43, 45, 46; full 64-sheet catalogue in
`input/figures/figures-manifest.md`). This run is now **figure-enabled**. Four figures are
selected — the mechanism spine the essay most needs a reader to *see*: system → multiply →
align-and-accumulate core → parallel weights.

## Selected figures

| Figure | File | Thesis point (spine element / section) | caption_role |
|---|---|---|---|
| FIG. 4 | fig-04.png | **Cover / core.** The claimed align-once, integer-accumulate step made literal: per-row Shift Calculation (EMax − E) with Emax = INT5(22), 2's-complement shift, then the column **Adder Tree (426)** emitting INT35. This IS claim 1's (b)+(c). Spine Axis 1; header + §2. | header_composite |
| FIG. 1 | fig-01.png | **System overview.** 32×32 digital CIM macro (101), input buffer (102), dequantization (106) to FP22, output register (108), mode decoding (110) — the one-pass datapath the reader orients on. §2 (mechanism). | body_figure_carries_unique_info |
| FIG. 3 | fig-03.png | **The multiply unit.** One column cell (Col 0, Row 0): sign/exponent/mantissa bitcell logic that produces one primitive product before alignment. §2 (mechanism); prose covers the detail. | body_figure_prose_covers_fully |
| FIG. 43 | fig-43.png | **Parallel weights.** Double-bitcell design (4303): BC0/BC1 per column on shared bitlines with separate write-wordlines — the dual-bank structure behind double-buffered weight loads. §4 (throughput). | body_figure_carries_unique_info |

## Paired-figure relationships (acknowledged)

- FIG. 1 → FIG. 3 → FIG. 4 form the natural zoom sequence (system → column cell → the
  column's alignment/adder-tree back end). All three selected, placed in reading order in §2.
- The base double-bitcell structure (selected as FIG. 43) has scan-wired variants and an
  alignment-column-cell / compute-timing group that remain available but unselected. Those
  are named by role here, not by drawing number, so they do NOT tokenize as "selected" for
  `gate_figure_use` (the earlier text-only pass learned this the hard way). The §5 depth
  point is carried in prose (clock margins, scan chains) to keep the placed-figure count
  tight; the composer may still cross-reference an available-but-unselected drawing in prose
  where it adds reader value (that registers as a FIGUSE-002 warn, never a fail).

## Header / body assignment

- **Header (5:2 cover)**: FIG. 4 — the adder-tree/mantissa-alignment core. It is the one
  drawing that shows the thesis at a glance; the title rides above it.
- **Body §2 (mechanism)**: FIG. 1 (system datapath), then FIG. 3 (column-cell multiply),
  with the header's FIG. 4 referenced again as the align/accumulate back end.
- **Body §4 (throughput)**: FIG. 43 (double-bitcell / dual-bank).
- **Not figure-backed**: §1 lead, §3 scope-and-baseline, §5 registry/depth, §6 closing —
  prose carries these; no figure is forced where it would only decorate.

## Orphan / reference discipline (gate note)

Every selected figure (1, 3, 4, 43) MUST be referenced by "FIG. N" in the draft or
`gate_figure_use` fails FIGUSE-001 (orphan). The composer references exactly these four and
may cite any other *available* figure (2, 6, 38, 42, 45, 46) only if it adds reader value
(that would be a FIGUSE-002 warn, not a fail). Referencing a figure NOT in the available
index would fail gate_anchors FIGREF-001 — so stay within the available set.
