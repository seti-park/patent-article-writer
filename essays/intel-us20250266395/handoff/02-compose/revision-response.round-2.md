# Revision response — round 2

draft_version: 3  <!-- the version this revision produced -->

## r2-F1

- disposition: applied
- change: Both splits made at the reviewer's named seams, split-only, zero content change.
  §3 KGD paragraph: broken after "One bad die can scrap the finished package." → 4 + 3
  sentences (~63 + ~52 words); declared signature line 2 ("Only an assembly that has
  already passed its test gets to spend a substrate.") remains byte-identical as the
  closing sentence of the second paragraph. §5 pricing paragraph: broken after "...ideas
  it considers dead (Google Patents)." → 3 + 3 sentences (status+counterparts /
  provenance+weight). Neighbor recount after both splits: §3 now 5 / 4 / 3 / 5 sentences;
  §5 now 6 / 4 / 4 / 3 / 3 — all paragraphs in the 3-7 band, none over the >8 mobile-line
  threshold. Figure tokens re-checked after the structural edits: all present, none
  orphaned.
- location: §3 paragraph 2; §5 paragraph 4

## r2-F2

- disposition: applied
- change: FIG. 5A/5B caption noun corrected: "solder balls (526, FIG. 5A)" →
  "ball-pitch solder pads (526, FIG. 5A)", per the invention-summary reference row
  "520-1 / 520-2 / 526 | ball-pitch solder pads (dies; bridge bottom) | [0048] | FIG. 5A"
  (the Phase-1 source Phase 2 can read; matches the reviewer's [0048] wording). Mirrored
  into figures-rationale.md's "Caption (as written)" record, same as r1-F2.
- location: §3, FIG. 5A/5B caption; handoff/02-compose/figures-rationale.md
- upstream flag (fix at source, for the orchestrator): the drift originated in
  handoff/01-design/figure-rationale.md ("either solder balls (526, 5A) or hybrid-bond
  contacts (536, 5B)") — the invention-summary row has the correct noun, but the Phase-1
  figure-rationale line should be corrected to "ball-pitch solder pads (526, 5A)" or a
  future recompose reintroduces the drift.

## r2-F3

- disposition: applied
- change: Essay-self-reference clause cut exactly as recommended: "There is a quiet glass
  thread here, and it stays one paragraph:" → "There is a quiet glass thread here:".
  Nothing else in the paragraph changed; [0033] anchor and sentence force intact.
  Paragraph recounted: sentence count unchanged (6).
- location: §4, glass paragraph, first sentence

## r2-F4

- disposition: applied
- change: Universal narrowed by cutting, not hedging: "are the generic wafer-and-device
  boilerplate every filing carries" → "are generic wafer-and-device boilerplate"
  (reviewer's simplest variant — drops the unanchored every-filing claim, keeps the
  concession's color and the FIG. 12 pointer). Sentence recounted; §5 ¶1 stays 6
  sentences, in band.
- location: §5, paragraph 1, sentence 3

## Volunteered changes (beyond findings)

- thesis-trace.md bookkeeping only: §4 word_actual 622 → 617 (r2-F3 cut) and §5
  word_actual 462 → 458 (r2-F4 cut); no spine→section mapping, anchors, or signature
  lines moved. No other prose touched.
