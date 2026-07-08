<!--
  TEMPLATE: handoff/01-design/figure-selection.md
  Produced by: thesis-architect (Phase 1 Design, Step 9 — figure mapping)
  Schema source: thesis-architect/SKILL.md Step 9 + references/figure-rendering.md
                 (caption_role enum) + invention-summary.md §"Figure relationships"

  Every SELECTED figure maps to a thesis point + a caption_role. Paired-figure
  relationships (same-page sub-figure / progressive sequence) must be treated as
  one unit — pull them from invention-summary.md §"Figure relationships". If SETI
  deliberately breaks a pair, flag it in phase2-handoff-notes.md so Phase 2 does
  not reopen the decision. Example content: Tesla RCM / 70ms patent.

  caption_role enum (drives caption length in Phase 2 figure-rendering.md):
    header_composite                 — multi-panel header figure; detailed caption
    body_figure_in_header_composite  — already in header; short identifier-only
    body_figure_prose_covers_fully   — prose conveys all; short identifier-only
    body_figure_carries_unique_info  — figure-unique data; medium 15-30 word caption
-->

# Figure Selection

## Selected figures

<!-- One row per SELECTED figure. Thesis point = which spine element / section the
     figure supports (trace to thesis-spine.md spine→section). file = cleaned
     fig-NN.png asset from Layer 1 patent-figures-clean. -->
| Figure | File | Thesis point (spine element / section) | caption_role |
|---|---|---|---|
| FIG. 1 | fig-01.png | System architecture overview — vision path into RCM (2-architecture) | header_composite |
| FIG. 2 | fig-02.png | Vision sensor array as predictive input (2-architecture) | body_figure_prose_covers_fully |
| FIG. 4A | fig-04a.png | Pre-impact decision timing vs accelerometer baseline (3-baseline) | body_figure_carries_unique_info |

<!-- FIG. 4B was reviewed as the same-page pair of 4A but NOT selected: 4A's caption
     carries the load-bearing timing data and 4B would restate without adding reader
     value. Pair-break is intentional and is flagged in phase2-handoff-notes.md so
     Phase 2 does not reopen it. See the paired-figure table below. -->

## Paired-figure relationships (acknowledged)

<!-- Mirror the relevant rows of invention-summary.md §"Figure relationships".
     Confirm each pair is treated as ONE cognitive unit in the selection above.
     If a pair is intentionally split, mark "BROKEN — see phase2-handoff-notes.md". -->
| Figure(s) | Relationship | Treatment in selection |
|---|---|---|
| FIG. 4A + FIG. 4B | same-page sub-figure pair | 4A selected, 4B dropped — pair-break is intentional (flagged in phase2-handoff-notes.md) |
| FIG. 7A / 7B / 7C | progressive sequence (before / during / after) | NOT selected — sequence not load-bearing for this spine |
| FIG. 1 | standalone | selected as header composite |

## Header / body assignment

<!-- One header figure (top visual hook + thesis anchor). Remaining = body figures.
     Header default rendering = image-plus-caption; body default = caption-only-italic
     (per figure-rendering.md). -->
- **Header**: FIG. 1 (system architecture composite — anchors the vision-path thesis)
- **Body**: FIG. 2, FIG. 4A

<!--
  > Revision note — triggered by [step N] [date]: [what changed and why]
  (Append if a feedback loop revises figure selection, e.g. a paired figure was
  added retroactively after a SETI catch.)
-->
