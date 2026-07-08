# Figure Rationale

## FIG. 5 — Hardwired memory channels (COVER)

- **Purpose**: The most literal picture of the spine's claims anchor: two memory chips
  (505A/505B) whose independent channels (510A-510D) run by dedicated wires (520) straight
  into individual columns (515A-515D) of the local systolic array (220) inside the IC (215).
  No switch appears because none exists — that absence is the claim (`[0043]`-`[0045]`,
  claim 39 as drafted).
- **Intended effect**: The reader SEES "no layer between memory and math" before reading a
  word of claim language; at card scale it reads as "memory wired straight into a chip",
  which is the thread's CSM pitch drawn two years earlier. Cover caption must stay within
  6 distinct numerals and carry the discovery beat, not a parts list.

## FIG. 1 — The systolic array primer

- **Purpose**: The logical machine: a grid of DPUs (105), model weights (110) entering from
  the top, the previous tensor (115) entering from the left, and two shaded multiplications
  sharing the grid simultaneously (`[0020]`-`[0024]`).
- **Intended effect**: Gives the reader the one mental model everything else reuses (weights
  fall, data flows right, every cell multiply-accumulates), and quietly shows "splittable":
  two computations in one array (`[0024]`). Prose carries the mechanism; the figure is the
  picture the prose points at (caption_role: body_figure_prose_covers_fully).

## FIG. 2 — The package: many chips, one array

- **Purpose**: The physical version of FIG. 1 per `[0028]`: nine ICs (215A-215I) each
  holding a tile (220A-220I), fused by horizontal (230) and vertical (225) links into
  combined systolic array 250, fed by memory chips (210A-210C) on the top row, talking to a
  host (205) over PCIe (240).
- **Intended effect**: The origin-document reveal in one image: what the company later
  called a giant splittable math array is a 3×3 grid of identical chips behaving as one
  device. The figure carries structure prose should not enumerate (grid topology, where
  memory sits, where the host attaches) (caption_role: body_figure_carries_unique_info).

## FIG. 3 — Memory economy of the grid

- **Purpose**: The square-grid variant (package 301) with MULTIPLE memory chips (305A-305F)
  per top-row IC, illustrating `[0039]` (adding rows of ICs adds compute without adding
  memory, because weights are reused down the rows) and `[0040]` (multiple chips per IC for
  more than 1 TB/s per top-row IC).
- **Intended effect**: Makes the memory-side arithmetic visible: memory scales with columns,
  compute scales with rows — the design reason the memory half matters to the architecture
  bet. Prose carries the argument (caption_role: body_figure_prose_covers_fully).

## FIG. 6 — The division of labor

- **Purpose**: Four ICs (615A-615D) each split in two: auxiliary circuitry (605A-605D)
  beside the array tile (220A/220B/220D/220E), with small private local memory chips
  (610A-610D) hanging off the auxiliary circuitry OUTSIDE the combined array 650. Per
  `[0047]`-`[0051]`: self-attention work goes to the sidecar; the systolic arrays do not
  have access to the local memory chips.
- **Intended effect**: Shows the transformer-shaped commitment: the chip's floor plan
  physically separates "math that forgets" (the array) from "math that remembers"
  (auxiliary circuitry + private memory) — claims 11-13 as drafted. CAUTION: the Phase 0
  manifest line for this figure swaps 605/610; captions must use the corrected labels
  (605 = auxiliary circuitry, 610 = local memory chips) per `[0047]`-`[0051]`
  (caption_role: body_figure_carries_unique_info).

## FIG. 7 — Pipelining a transformer layer

- **Purpose**: The timing chart (`[0053]`-`[0057]`): what every DPU in one row does per
  clock, stepping through Attention Queries/Keys/Values, Projection, and the MLP layers;
  inputs for the next computation pre-fed before the previous completes (Time A), and the
  one unavoidable stall at layer normalization (Time B), with utilization still at 98% or
  greater.
- **Intended effect**: Proves the paper thought about KEEPING the giant array busy, not just
  building it — the operational maturity beat. The figure carries data prose cannot
  (the stall's visual width, the interleaving). MUST be narrated as description-only: no
  claim covers pipelining, batching, or the 98% figure
  (caption_role: body_figure_carries_unique_info).

## FIG. 4 — NOT selected

- **Purpose (if it had been kept)**: unequal rows/columns variant (package 401, array 450),
  `[0041]`-`[0042]`.
- **Why dropped**: variant pair of FIG. 3; the spine uses FIG. 3's memory-economy point, and
  the unequal-grid nuance adds no thesis value. Intentional pair-break, flagged in
  phase2-handoff-notes.md.
