# X Articles posting checklist — etched-us20240378175-r2

## Title (61 chars, ≤70 budget)
Etched's First Patent Filing Asks to Delete the Memory Switch

## Cover
- Use `cover-5x2.png` (1527x610, 5:2) — FIG. 5's memory-to-column band: chips 505A/B,
  channels 510A-D, wire bundle 520, IC 215 entry. Full-figure alternative:
  `cover-letterbox.png` (1500x600).
- Cover alt text: "Patent drawing: two memory chips wired straight down into a processor
  chip, four independent channels, no switch between them."

## First-two-lines feed preview (verify after paste)
"Between an AI accelerator's math units and the memory that feeds them, chip designers
typically place a switch..." — the technology beat lands inside the preview window; the
May 2023 discovery beat follows inside the same paragraph.

## Body figure order + alt texts (paste inline where publication.md places them)
1. fig-05.png (§ cover already; if the platform repeats it in-body, keep the essay caption)
2. fig-01.png — "Patent drawing of a systolic array: weights enter from the top row, data
   flows in from the left, every crossing multiplies and adds."
3. fig-02.png — "Patent drawing: nine chips fused into one combined array in a package,
   host attached by PCIe, memory chips along the top row."
4. fig-03.png — "Patent drawing: multiple memory chips feeding each top-row chip of the
   combined array."
5. fig-06.png — "Patent drawing: auxiliary circuitry beside each local array with its own
   private memory chips."
6. fig-07.png — "Patent drawing: timeline of one array row processing attention and MLP
   stages back-to-back, with a single stall marked at Time B."

## Paste source
- `publication.md` (2,913 words incl. Sources) — one line per paragraph, captions italic.
- Keep the Sources section (patents + news lines) at the end.

## Post-publication
- Reader feedback edits go through the human-post-accept channel (revision-notes.md) so
  the ledger keeps learning.
- The docket-watch beat (§6) names the RCE record as the thing to track — a follow-up
  window opens when Etched's next office-action response lands.
