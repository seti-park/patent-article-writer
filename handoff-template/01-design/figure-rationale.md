<!--
  TEMPLATE: handoff/01-design/figure-rationale.md
  Produced by: thesis-architect (Phase 1 Design, Step 9 — figure mapping)
  Schema source: thesis-architect/SKILL.md Step 9 ("per-figure purpose + intended effect")

  One block per SELECTED figure (same set as figure-selection.md). Records WHY the
  figure earns its place (purpose) and what it should do to the reader (intended
  effect). Phase 2 Compose reads this alongside figure-selection.md when planning
  placement + caption. Example content: Tesla RCM / 70ms patent.
-->

# Figure Rationale

## FIG. 1 — System architecture composite

<!-- Purpose: what the figure shows / which thesis point it grounds.
     Intended effect: what cognitive move it produces in the reader. -->
- **Purpose**: Shows the vehicle control unit (414), vision sensor array (416), safety bus (420), and airbag module (430) as one signal path, with the vision sensor feeding the RCM directly.
- **Intended effect**: Establishes up front that the vision path is the primary decision route, not a redundant add-on — primes the reader for the "optical drives deployment" thesis.

## FIG. 2 — Vision sensor array detail

- **Purpose**: Isolates the vision sensor array (416) and its pre-impact prediction output, supporting the `[0017]` "predictive input rather than a redundant sensor" claim.
- **Intended effect**: Lets prose stay light — the figure carries the mechanism so the body text can move to implication. (caption_role: body_figure_prose_covers_fully.)

## FIG. 4A — Pre-impact decision timing

- **Purpose**: Plots the deployment-decision point on the vision path against the accelerometer baseline, carrying the ~70ms lead-time data `[0024]`.
- **Intended effect**: Makes the 70ms claim visually concrete — the reader sees the lead, not just reads it. (caption_role: body_figure_carries_unique_info — medium caption with the timing data points.)

## FIG. 4B — Deployment-window detail

- **Purpose**: Companion to 4A; details the arming window inside the pre-impact interval. Paired same-page sub-figure.
- **Intended effect**: Reinforces 4A without restating it; kept short because 4A's caption carries the unique data. (caption_role: body_figure_in_header_composite.)

<!--
  > Revision note — triggered by [step N] [date]: [what changed and why]
-->
