# Figures Rationale (Compose placements)

Compose's ACTUAL placement decisions for draft_version 1 (essay-draft.md). Phase 1 intent in
`handoff/01-design/figure-rationale.md`; deltas noted per figure. The set below is
**figures_locked** for this run: list, roles, and positions do not change during revision
unless a Phase-3 finding explicitly calls for it.

## FIG. 5 — header (COVER)

- **Placement**: header
- **Rendering**: image-plus-caption (`![...](figures/fig-05.png)` + italic caption line)
- **caption_role**: header_composite
- **Caption (as written, v4 — venue + pitch date corrected per self-audit sa1A-F01/sa1B-F1/sa1G-F1)**: `*FIG. 5, from Etched's first patent filing: independent memory channels (510) run through dedicated wires (520) straight into individual columns (515) of the on-chip math array, with no switch anywhere in the path. Etched pitched this as its no-layer memory philosophy in its stealth-exit thread in late June 2026. The drawing is dated May 2023.*`
- **Decision note**: carries the discovery beat (two dates, three-year gap) on the card, not
  a parts list. Numeral budget honored: 5 distinct reference-numeral tokens (510, 520, 515,
  2026, 2023 — years count under SURF-003's tokenizer), within the ≤ 6 budget; 215/220 and
  even 505 left out of the caption per figure-selection.md. FIG. 5 is also walked in §3
  prose ("FIG. 5 draws it: two memory chips (505)...") for narrative continuity — prose
  reference only, no second embed, no second caption.

## FIG. 1 — body, §2 (2-origin-array), first

- **Placement**: body-section-2-after-[0024] (after the systolic-array primer paragraph)
- **Rendering**: caption-only-italic
- **caption_role**: body_figure_prose_covers_fully
- **Caption (as written)**: `*FIG. 1: the basic systolic array, two computations sharing one grid.*`
- **Decision note**: prose carries the mechanism (weights fall [0021], tensors stream left
  to right, splittable [0024]); the figure is the picture the prose points at, so the
  caption stays short. Placed BEFORE FIG. 2 per the locked logical-before-physical order
  ([0028]).

## FIG. 2 — body, §2 (2-origin-array), second

- **Placement**: body-section-2-after-[0028] (after the host-sees-one-array blockquote paragraph)
- **Rendering**: caption-only-italic
- **caption_role**: body_figure_carries_unique_info
- **Caption (as written)**: `*FIG. 2: nine ICs (215), each holding a local array (220), fused into one combined array (250); memory chips (210) line the top row; the host (205) attaches over PCIe (240).*`
- **Decision note**: the figure carries structure the prose does not enumerate (grid
  topology, where memory sits, where the host attaches); medium caption with the reference
  numerals doing the work.

## FIG. 3 — body, §3 (3-memory-half)

- **Placement**: body-section-3-after-[0040] (after the memory-economy paragraph)
- **Rendering**: caption-only-italic
- **caption_role**: body_figure_prose_covers_fully
- **Caption (as written)**: `*FIG. 3: the square-grid variant; multiple memory chips (305) feed each top-row chip.*`
- **Decision note**: prose carries the argument (rows add compute without memory [0039],
  >1 TB/s per top-row chip [0040]); short caption. The broken FIG. 3/FIG. 4 pair is
  acknowledged in prose with a single clause ("a sibling sheet, FIG. 4, redraws the same
  design with unequal rows and columns" — "design", not "package", per r1-F10: FIG. 4 is
  package 401, a distinct embodiment of the same design) — grounded in invention-summary's
  figure relationships row for the [0041] variant pair. This keeps the intentional pair-break
  honest for the reader AND keeps the mechanical figure_use selected-set (which parses
  FIG. 4 from figure-selection.md's NOT-selected note) coherent. FIG. 4 itself is NOT
  placed (no caption, no embed) — the Phase-1 drop decision is not reopened.

## FIG. 6 — body, §4 (4-division-of-labor), first

- **Placement**: body-section-4-after-[0051] (after the sidecar/negative-limitation paragraph)
- **Rendering**: caption-only-italic
- **caption_role**: body_figure_carries_unique_info
- **Caption (as written)**: `*FIG. 6: inside each IC (615), the array tile (220) and the auxiliary circuitry (605) sit side by side; the private local memory chips (610) hang off the auxiliary circuitry, outside the combined array (650).*`
- **Decision note**: labels follow the SPEC per [0047]-[0051], not the Phase-0 manifest
  (which swaps 605/610): **605 = auxiliary circuitry (inside the ICs 615); 610 = local
  memory chips (small boxes outside)**. Manifest defect flagged in invention-summary and
  phase2-handoff-notes; caption written against the corrected labels.

## FIG. 7 — body, §4 (4-division-of-labor), second

- **Placement**: body-section-4-after-[0057] (after the pipelining/98% paragraph)
- **Rendering**: caption-only-italic
- **caption_role**: body_figure_carries_unique_info
- **Caption (as written)**: `*FIG. 7: a row's clock-by-clock schedule for one transformer layer. Description-only, no claim covers it: attention passes, pre-fed next batches, and the lone stall at layer normalization (Time B).*`
- **Decision note**: the figure carries what prose cannot (the interleaving, the stall's
  position at Time B). The description-only status is carried BOTH in the caption
  ("Description-only, no claim covers it") and in §4 prose ("none of what it shows is
  claimed anywhere"), per the phase2-handoff-notes figure trap.

## FIG. 4 — NOT placed

- **Placement**: omitted from the draft (no embed, no caption)
- **Decision note**: intentional pair-break per figure-selection.md and
  phase2-handoff-notes.md ("do not reopen"). The load-bearing memory-economy point is
  FIG. 3's; FIG. 4 adds only the unequal-grid nuance. Acknowledged in §3 prose with one
  clause (see FIG. 3 note) so the sibling's existence is honest without granting it a
  placement.
