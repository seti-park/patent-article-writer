# Figure Selection

## Selected figures

| Figure | File | Thesis point (spine element / section) | caption_role |
|---|---|---|---|
| FIG. 7C | fig-07C.png | Claim 1's claimed core in one image: every cross-set pair directly wired, none within a set (3-wiring; also the 5:2 header) | header_composite |
| FIG. 7A | fig-07A.png | First communication channels 730 - one of the two channel families; the group pairing 712a↔712c / 712b↔712d that claims 8/18 hang on (4-traffic) | body_figure_carries_unique_info |
| FIG. 7B | fig-07B.png | Second communication channels 740 - the criss-cross pairing 712a↔712d / 712b↔712c; the other exclusive traffic lane (4-traffic) | body_figure_carries_unique_info |
| FIG. 1 | fig-01.png | What one tensor parallel group is made of: four processing devices, each a systolic array of processing elements (2-grant / 3-wiring; claim 7) | body_figure_prose_covers_fully |
| FIG. 6 | fig-06.png | Where memory actually sits in this patent: memory 630 is a box beside the tensor parallel groups - described, never claimed (6-boundary) | body_figure_carries_unique_info |
| FIG. 9A | fig-09A.png | The workload the wiring is shaped for: decoding layers - normalization, self-attention (QKV + attention), projection, MLP (5-workload) | body_figure_prose_covers_fully |

## Paired-figure relationships (acknowledged)

| Figure(s) | Relationship | Treatment in selection |
|---|---|---|
| FIG. 7A + 7B + 7C | decomposition pair + union of ONE fixed topology (`[0123]`: split "for case of illustration" [sic]; `[0125]`: 7C shows all connections in a single figure). NOT a temporal sequence - no phase map applies. | All three selected, treated as one unit. 7C carries claim 1 (the union); 7A/7B carry claims 8/11/18 (the channel-family split). Selecting any subset would break either the claim-1 or the claim-18 visual argument. |
| FIG. 9A + 9B | same-subject pair (block diagram + tensor-equation detail) | 9A selected, 9B dropped - pair-break is INTENTIONAL and flagged in phase2-handoff-notes.md: 9B restates 9A's flow as subscripted equations (T1×WQ=Q etc.) above the reader profile; prose covers the needed level. Phase 2 must not reopen. |
| FIG. 3 / 4 / 5, FIG. 8, FIG. 10 / 11 / 12 | method-flowchart family (FIG. 8 executes on the 7A/7B topology; 10/12 cite FIG. 8 blocks) | NOT selected - tile-movement method mechanics are sibling-patent territory per essay-context (091 = structure; deep-dive reserved for a possible part-2 on 903). The `[0061]` p=4/q=2 math and the balanced-channel result are carried in prose from invention-summary anchors instead. |
| FIG. 2, FIG. 13 | standalone | NOT selected - FIG. 2's tile split is one sentence of prose; FIG. 13 is generic computer-system boilerplate. |

## Header / body assignment

- **Header**: FIG. 7C (fig-07C.png) - the single most literal picture of the claimed core
  step (claim 1's every-cross-set-pair wiring) and the highest-visual-force sheet in the
  set (the dense two-family web). **Cover candidate: fig-07C** (tagged in
  invention-summary.md §Figure relationships). Note for Phase 2: the artwork is roughly
  square; a 5:2 header crop should center on the mid-band where the 730/740 families
  visibly interleave, keeping both column groups (710a/710b) in frame.
- **Body**: FIG. 7A, FIG. 7B (as the decomposition pair, placed adjacent in 4-traffic),
  FIG. 1 (2-grant/3-wiring), FIG. 6 (6-boundary), FIG. 9A (5-workload).

<!--
  > Revision note - none. Step 9 confirmed the Step 8 section trace without revision;
  paired-figure treatment matches invention-summary.md §Figure relationships.
-->
