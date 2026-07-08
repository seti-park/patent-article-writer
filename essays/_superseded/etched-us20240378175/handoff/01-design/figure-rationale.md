# Figure Rationale

## FIG. 5 — Memory chips hardwired to array columns (HEADER / cover candidate)

- **Purpose**: Shows the spine's claim anchor as hardware: memory chips 505A/505B with
  independent channels 510A-510D wired (520) straight down into dedicated columns
  515A-515D of the array tile 220 inside IC 215 — no switch, no crossbar, nothing between
  memory and math (`[0043]`-`[0045]`; claim 39 as drafted, mirrored in `[0016]`).
- **Intended effect**: Makes "the best memory layer is no layer" a picture the reader can
  verify at a glance — two boxes of memory, four columns of compute, and only wires in
  between. Primes the verdict: this drawing is the memory-side philosophy the July 2026
  thread describes, dated May 2023. As the header image it carries the origin-document
  frame before a word is read.
- **Caption note**: caption must use application-era language ("the application claims /
  as drafted"), never "the patent locks".

## FIG. 1 — A systolic array, logically

- **Purpose**: Reader education for the default audience: the DPU grid 105, model weights
  110 entering from the top, previous tensor 115 from the left, results rippling
  diagonally (`[0020]`-`[0024]`). Also the logical view of everything that follows —
  `[0028]` says the multi-chip array of FIG. 2 presents as this one array.
- **Intended effect**: Gives the reader the one mental model the whole essay reuses
  (weights fall, data flows right, every cell multiplies-and-adds), so the multi-chip and
  memory-hardwiring figures read as variations rather than new machinery. Prose covers the
  mechanism fully; the figure carries no unique data (caption_role:
  body_figure_prose_covers_fully — short identifier caption).

## FIG. 2 — The package: many chips, one array

- **Purpose**: The claim-1/15 frame in one drawing: ICs 215A-215I each holding an array
  tile 220, stitched by horizontal (230) and vertical (225) chip-to-chip connections into
  Combined Systolic Array 250, fed by memory chips 210A-210C on the top row, talking to a
  host 205 over PCIe 240 (`[0025]`-`[0038]`).
- **Intended effect**: Shows the "splittable math arrays" idea of the company's thread as
  the origin filing drew it — the reader sees that the array boundary (dashed box 250)
  ignores chip boundaries. Carries figure-unique information (the topology: which
  connections are where, memory only on top) that prose should not re-enumerate
  (caption_role: body_figure_carries_unique_info — medium caption naming 215/220/250 and
  the top-row memory feed).
- **Pairing**: placed after FIG. 1 as its physical realization (`[0028]` logical/physical
  pair).

## FIG. 6 — Auxiliary circuitry with private memory

- **Purpose**: The claims-11-13 division of labor: each IC 615A-615D contains an
  auxiliary-circuitry block 605 beside its array tile 220, with external local memory
  chips 610A-610D reachable ONLY by the auxiliary circuitry — the systolic arrays never
  touch them (`[0047]`-`[0051]`, q-0051-1).
- **Intended effect**: Shows the transformer-shaped split of the silicon: token-history
  work (self-attention) gets its own circuit and its own memory, so the big array stays a
  pure matrix engine. Supports the "this is a transformer ASIC philosophy, in 2023" beat
  (caption_role: body_figure_carries_unique_info).
- **Correction vs manifest**: the figures-manifest one-liner labels 605 as "local memory
  chips"; per the specification and the drawing, 605A-D are the auxiliary-circuitry blocks
  and 610A-D are the local memory chips. Captions must follow the specification labels.

## FIG. 7 — Pipelining one row of the array

- **Purpose**: Timeline chart of a transformer layer's stages (attention queries/keys/
  values, projection, MLP hidden/output) flowing through one array row, including the
  swap between array and auxiliary unit (bold dashed line) and the layer-normalization
  stall at Time B (`[0053]`-`[0057]`).
- **Intended effect**: Grounds the ≥98% utilization claim (q-0057-1) — the reader sees
  that the array is fed a new computation before the previous one drains, and that the
  only white space on the chart is the layer-norm stall. Carries figure-unique data
  (caption_role: body_figure_carries_unique_info — medium caption; name Time A/Time B and
  what the stall is).

## Not selected — FIG. 3, FIG. 4 (variant family of FIG. 2)

- FIG. 3 (square grid, three memory chips per top-row IC) and FIG. 4 (2×3 unequal grid)
  repeat FIG. 2's topology at other sizes. Their one load-bearing point — more compute
  rows without more memory chips, since weights are reused down the rows `[0039]` — is
  carried in prose (q-0039-1). Selecting them would spend two figure slots restating the
  package concept. Intentional drop; flagged in phase2-handoff-notes.md.
