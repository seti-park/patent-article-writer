<!--
  handoff/02-compose/figures-rationale.md
  Produced by: essay-en-composer (Phase 2 Compose, Step 7) — draft_version 1
  Records Compose's ACTUAL placement decisions for US 12,361,091 B1 (Etched).
  Phase 1 intent: handoff/01-design/figure-selection.md + figure-rationale.md.
-->

# Figures Rationale (Compose placements)

figures_locked: the six-figure set below (FIG. 7C header; FIG. 1, 7A, 7B, 9A, 6 body), their
roles, and their positions are locked for this run per caption-roles.md; they do not change
during revision unless a Phase-3 finding explicitly calls for it.

round-1 revision note: placements, roles, and the six-figure set are unchanged. Two caption
TEXTS changed under Phase-3 authority — FIG. 7C re-anchored per r1-F13 and FIG. 6 narrowed
per r1-F2 (the caption repeated the body's false "only memory in the patent" absolute).
Transcriptions below are updated to match draft_version 2.

selfaudit-round-1 revision note (post-acceptance, origin self-post-accept): placements,
roles, and the six-figure set remain unchanged. Three caption TEXTS changed —
FIG. 7C gained the figure-derived-count caveat "counted off the drawing" (sa1G-F4);
FIG. 7B gained [0139] on the criss-cross clause and [0125] beside [0123] on the union
clause (r2-F2 + sa1G-F5); FIG. 9A re-anchored [0251] → [0252], [0259] (r3-F2 = sa1G-F7).
Transcriptions below are updated to match draft_version 3; see
handoff/03-edit/revision-notes.md for the delta log.

selfaudit-round-2 revision note (post-acceptance, origin self-post-accept): placements,
roles, the six-figure set, and every caption TEXT are unchanged — no round-2 finding
touched figure content. Transcriptions below remain valid for draft_version 4.

selfaudit-round-3 revision note (post-acceptance, origin self-post-accept, FINAL round —
self-audit cap reached): placements, roles, the six-figure set, and every caption TEXT
are unchanged — no round-3 finding touched figure content (round-3 grounding verified
all 6 placed captions against the image files: 8/8 SUPPORTED). Transcriptions below
remain valid for draft_version 5.

## FIG. 7C — header (cover)

- **Placement**: header
- **Rendering**: image-plus-caption
- **caption_role**: header_composite
- **Caption (as written)**: `*FIG. 7C: the claimed core in one drawing. Eight chips stand in two columns: the first set 710a (a1, a3, a5, a7) on the right and the second set 710b (a0, a2, a4, a6) on the left [0126]. Every chip in one column is wired straight to every chip in the other, 16 channels in all, counted off the drawing, and no wire runs inside a column [0128], [0129]. Both channel families (730, 740) are overlaid here [0125].*`
- **Self-audit revision (sa1G-F4)**: the 16-channel count in the anchored clause now carries
  the same figure-derived caveat the body gives it ("counted off the drawing"), so the
  caption no longer implies the number is patent text.
- **Round-1 revision (r1-F13)**: cross-pair + no-wire-inside sentence re-anchored from
  `[0125]` (which only says 7C shows all connections in one figure) to `[0128]`, `[0129]`;
  `[0125]` moved to the overlay sentence it actually supports. Caption content itself was
  verified accurate against fig-07C.png by the round-1 review.
- **Decision note**: Phase 1's cover candidate, kept. The overlay IS claim 1's granted core;
  the caption walks columns (sets), cross-only wiring, and the family overlay, and states the
  16-channel count as read off the drawing. The "one at a time" forward pointer to 7A/7B was
  trimmed at compose time (STRUCT sentence budget); the section-4 pointer paragraph carries it
  instead. Publication-time note: artwork is roughly square; the 5:2 header crop should center
  on the mid-band where the 730/740 families interleave, keeping both column groups in frame
  (carried in # Footnotes).

## FIG. 1 — body, section 3 (wiring), after the size-problem paragraph

- **Placement**: body-section-3-after-[0036]
- **Rendering**: caption-only-italic
- **caption_role**: body_figure_prose_covers_fully
- **Caption (as written)**: `*FIG. 1: inside one tensor parallel group: processing devices built as systolic arrays.*`
- **Decision note**: placed where "processing device" vocabulary is introduced so the wiring
  discussion can move fast; prose fully covers content (claim 7's systolic-array limitation is
  in the adjacent sentence), so the caption stays short.

## FIG. 7A — body, section 4 (traffic), after the decomposition pointer paragraph

- **Placement**: body-section-4-after-[0123]
- **Rendering**: caption-only-italic
- **caption_role**: body_figure_carries_unique_info
- **Caption (as written)**: `*FIG. 7A: the first channel family (730): group 712a wired to every chip of 712c, and 712b to every chip of 712d [0138].*`
- **Decision note**: carries the group-pairing data claims 8/18 hang on; adjacent to FIG. 7B
  per figure-selection (the pair reads as one argument).

## FIG. 7B — body, section 4 (traffic), immediately after FIG. 7A

- **Placement**: body-section-4-after-[0123] (adjacent pair with 7A)
- **Rendering**: caption-only-italic
- **caption_role**: body_figure_carries_unique_info
- **Caption (as written)**: `*FIG. 7B: the second channel family (740): the criss-cross, 712a to 712d and 712b to 712c [0139]. Added to FIG. 7A's links it gives the full FIG. 7C web [0123], [0125].*`
- **Self-audit revision (r2-F2 + sa1G-F5)**: the criss-cross pairing clause now carries its
  own anchor [0139]; the union clause keeps [0123] (all connections of 7A+7B) and adds
  [0125] (7C shows them in a single figure), the paragraph that actually names FIG. 7C.
- **Decision note**: completes the decomposition; caption states the 7A+7B=7C union so the
  reader gets the "two disjoint rail systems" idea from the pictures alone. Decomposition
  framing only, no temporal language (7A/7B are NOT a sequence, per the Phase-1 trap).

## FIG. 9A — body, section 5 (workload), after the transformer-target paragraph

- **Placement**: body-section-5-after-[0252]
- **Rendering**: caption-only-italic
- **caption_role**: body_figure_prose_covers_fully
- **Caption (as written)**: `*FIG. 9A: the decoding-layer loop the description maps onto the group [0252], [0259].*`
- **Self-audit revision (r3-F2 = sa1G-F7)**: re-anchored — [0251] only establishes what the
  model is; the maps-onto-the-group fact is [0252] and the loop is [0259] (both
  Phase-1-resolvable; [0263] avoided as not in the Phase-1 anchor inventory).
- **Decision note**: prose walks the layers (normalization, self-attention, projection, MLP,
  decoding); the figure anchors the names. Caption says "the description maps", keeping the
  claim-scope line clean (workload is description-level, not a claim limitation).

## FIG. 6 — body, section 6 (boundary), after the memory-absence paragraph

- **Placement**: body-section-6-after-[0119]
- **Rendering**: caption-only-italic
- **caption_role**: body_figure_carries_unique_info
- **Caption (as written)**: `*FIG. 6: box 630, the memory that feeds the tensor parallel groups, described in one embodiment figure and never claimed [0119].*`
- **Round-1 revision (r1-F2 spillover)**: "the patent's only memory" dropped — the same
  false document-level absolute the body carried (the description also has per-chip
  memory devices at `[0133]`); the caption now states only what `[0119]` supports (feeds
  the groups, described once in this figure, never claimed).
- **Decision note**: the boundary exhibit; the caption itself names memory 630 as
  described-not-claimed, per figure-rationale intent. Text label "tensor parallel groups" used
  (not the drawing's "Tensor Parallel Device"), per the Phase-1 source-inconsistency note.

## Not placed (audit)

- **FIG. 9B**: pair-break intentional and locked by Phase 1 (equation-level restatement of 9A,
  above reader profile). Not reopened.
- **FIG. 2, FIG. 3, FIG. 4, FIG. 5, FIG. 8, FIG. 10, FIG. 11, FIG. 12, FIG. 13**: not selected
  by Phase 1 (method-flowchart family = sibling-patent territory; FIG. 2 covered by one prose
  sentence; FIG. 13 boilerplate). None referenced in the essay body; the not-placed set is
  recorded in the draft's # Footnotes for the figure-use audit.

## Gate note (for the orchestrator)

`gate_figure_use` parses every figure token in figure-selection.md as "selected", including
the tokens inside its NOT-selected rationale rows, which false-orphaned figures 2/3/8/10/13 on
the first gate run. Resolved by recording the not-placed audit (with tokens) in the draft's
# Footnotes block, which is stripped from publication.md. Flagging as a candidate
pipeline-retro item: the gate's selected-set parse vs figure-selection.md's exclusion rows.
