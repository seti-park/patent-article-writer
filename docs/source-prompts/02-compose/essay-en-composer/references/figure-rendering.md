# Figure rendering

Referenced by tech-essay-en SKILL.md Step 6 (Place figures). Defines role-dependent rendering for each `figures_locked` entry.

## Placement categories

Blueprint `figures_locked` entries carry a `placement` field. Three placement categories drive rendering decisions.

- **header** — essay top visual hook plus thesis anchor evidence
- **body-after-section-N** — body figure inserted after a named section
- **body-section-N-after-X** — body figure inserted mid-section after a paragraph anchor

## Default rendering by placement

| Placement | Default rendering | Output form |
|---|---|---|
| header | `image-plus-caption` | `![<caption>](<file_path>)` followed by detailed caption |
| body-after-section-N | `caption-only-italic` | `*<caption_draft>*` (italic, no image embed) |
| body-section-N-after-X | `caption-only-italic` | `*<caption_draft>*` (italic, no image embed) |

Body figure default is **caption-only-italic**. Cleaned figure asset stays in `outputs/figures/` for X Articles upload at publication time.

Rationale: mobile readability plus body flow plus publication-time asset mapping clarity. Pattern validated on the 368 Tesla cutting essay (header = composite, body = 4 italic captions only) and the 050 Tesla CAM essay (header = FIG. 5 composite, body = 5 italic captions).

Override to `image-plus-caption` for a body figure only when Blueprint explicitly specifies (figure isolation for emphasis case).

## Caption length by caption_role

Blueprint `caption_role` field per body figure drives caption length. Four roles defined.

### 1. body_figure_in_header_composite

Figure already appears inside the header composite. Body reference exists for narrative continuity.

→ **Short identifier-only** caption, approximately 5-10 words.

Example: `*FIG. 5A: the conventional reference.*`

### 2. body_figure_prose_covers_fully

Prose around the figure already conveys all analytical content. The figure serves as visual anchor only.

→ **Short identifier-only** caption, approximately 5-10 words.

Example: `*FIG. 1: the method flowchart.*`

### 3. body_figure_carries_unique_info

Figure carries data not present in surrounding prose — axes, peaks, reference numbers, gradient zones, comparison curves.

→ **Medium with figure-unique data points**, approximately 15-30 words.

Example: `*FIG. 3: TGA/DSC of the precursor mixture. Water removes at 116°C; LiOH melts at 425°C and 468°C.*`

### 4. header_composite

Header figure composed of multiple panels in a truth-table or comparison layout.

→ **Detailed caption**, walking the panel structure and the thesis anchor.

Example: a header composite of three panels (baseline, intervention, result) gets a caption that walks all three and connects to thesis.

## Caption format conventions

- Body figure captions: italic via `*...*`, no image embed
- Header figure captions: regular text after the `![](...)` embed
- Annotate caption with `[^figure-entry-id]` footnote anchor where applicable

## Validated patterns

- 368 Tesla cutting essay: header = composite image-plus-caption; body = 4 italic captions, default caption-only-italic mode
- 050 Tesla CAM essay: header = FIG. 5 composite image-plus-caption; body = 5 italic captions; one body figure in `body_figure_carries_unique_info` role got medium caption with TGA/DSC data points
