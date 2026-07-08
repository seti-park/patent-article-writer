<!--
  TEMPLATE: handoff/02-compose/figures-rationale.md
  Produced by: essay-en-composer (Phase 2 Compose, Step 7)
  Schema sources: essay-en-composer/SKILL.md (figures-rationale.md output)
                  + references/figure-rendering.md (placement + caption_role + rendering)

  Phase 1 figure-rationale.md states INTENT; this file records Compose's ACTUAL
  placement decisions: where each figure landed, its rendering mode, its caption_role,
  and the caption as written. Phase 3 Edit Pass 6 checks placement/format here.

  rendering enum: image-plus-caption (header default) | caption-only-italic (body default)
  placement enum: header | body-after-section-N | body-section-N-after-X
  caption_role enum: header_composite | body_figure_in_header_composite
                     | body_figure_prose_covers_fully | body_figure_carries_unique_info

  Example content: Tesla RCM / 70ms patent (matches essay-draft.md placements).
-->

# Figures Rationale (Compose placements)

## FIG. 1 — header

- **Placement**: header
- **Rendering**: image-plus-caption
- **caption_role**: header_composite
- **Caption (as written)**: detailed header caption walking the vision sensor array (416) → vehicle control unit (414) → airbag module (430) signal path and connecting it to the vision-first thesis.
- **Decision note**: chosen as the top visual hook; the composite is the thesis anchor evidence.

## FIG. 2 — body, in §2 (architecture)

- **Placement**: body-after-section-2
- **Rendering**: caption-only-italic
- **caption_role**: body_figure_prose_covers_fully
- **Caption (as written)**: `*FIG. 2: the vision sensor array.*`
- **Decision note**: §2 prose already conveys the mechanism; figure is a visual anchor only, so the caption stays short (5-10 words).

## FIG. 4A — body, in §3 (baseline)

- **Placement**: body-section-3-after-[0024]
- **Rendering**: caption-only-italic
- **caption_role**: body_figure_carries_unique_info
- **Caption (as written)**: `*FIG. 4A: pre-impact decision timing. The vision-path decision lands ~70 ms ahead of the accelerometer baseline.*`
- **Decision note**: figure carries the timing data points; medium caption (15-30 words) per body_figure_carries_unique_info.

## FIG. 4B — NOT placed

- **Placement**: omitted from the draft
- **Decision note**: FIG. 4A's caption carries the load-bearing timing data; placing 4B would restate without adding reader value. The same-page pair was reviewed (per figure-selection.md) before dropping 4B — pair-break is intentional, not an oversight.
