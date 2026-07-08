# Figures Rationale (Phase 2 Compose — actual placement decisions)

Four figures placed, matching `handoff/01-design/figure-selection.md` exactly (FIG. 1B cover +
FIG. 1A/1F/1G body). No figure added, dropped, or repositioned off-plan. All four are panels of
FIG. 1, so the figure set the gates see at integer granularity is `{1}`.

## figures_locked

| Figure | File | Placement | Rendering | caption_role (figure-rendering) | Role (caption-roles enum) | Section |
|---|---|---|---|---|---|---|
| FIG. 1B | fig-01B.png | header (cover) | image-plus-caption | header_composite | Orientation | header, primes §3 |
| FIG. 1F | fig-01F.png | body, mid-§2 after the "what backend means" paragraph | caption-only-italic | body_figure_carries_unique_info | Evidence | 2-the-move |
| FIG. 1G | fig-01G.png | body, mid-§3 after the TSV-gutter paragraph | caption-only-italic | body_figure_carries_unique_info | Mechanism | 3-the-stack |
| FIG. 1A | fig-01A.png | body, mid-§4 after the reframe paragraph | caption-only-italic | body_figure_carries_unique_info | Orientation | 4-who-can-make-it |

Set is **locked** for the run per `caption-roles.md`: list, roles, and positions do not change in
revision unless a Phase-3 finding calls for it.

## Per-figure placement decision

### FIG. 1B — header / cover (Orientation)
- **Decision**: cover, image-plus-caption, per figure-selection recommendation. It is the literal
  picture of claim 1's "memory die stack" and `[0023]` "8-high and beyond," and it carries the most
  instant feed force (a new kind of tall memory tower before a word is read). The caption walks the
  stack (111), TSVs (114), and base die (115) and links to the spine.
- **Cover-caption numeral budget**: 3 distinct reference numerals (111, 114, 115), under the ≤ 6
  SURF-003 budget. Stack height is spelled "eight-high" (no numeral token).

### FIG. 1F — §2 body (Evidence)
- **Decision**: placed right after the paragraph that glosses front-end vs back-end and the
  thin-film transistor, so the reader sees the claimed backend cell made literal at the moment the
  term lands. This is the figure that IS the proof for the load-bearing claim word "backend." Also
  the honest place the prose notes the capacitor is relocated, not removed. Medium caption names the
  TRANSISTOR tiers (151, 153) and interconnect regions (152, 154).

### FIG. 1G — §3 body (Mechanism)
- **Decision**: placed inside §3 after the TSV-gutter sentence. It carries the "match HBM4's
  footprint" internal architecture (eight sub-channels 161A-161H split by four TSV gutters 162-165)
  so the prose can stay light and move to the stakes. The "match HBM4's footprint" goal is stated in
  prose as the patent's GOAL, not a measured result (kept out of the caption).

### FIG. 1A — §4 body (Orientation)
- **Decision**: placed in §4 after the affirmative reframe paragraph. It is the only figure putting
  logic (106) and the memory stack (104) on one package, so it grounds the "one flow carries both"
  reading visually at the exact point the prose argues it. Used in §4 (not §2) per the
  phase2-handoff-notes default: fig-01A anchors the strategic reframe, not the mechanism.

## Note for the orchestrator — gate_figure_use FIGUSE-001 (pre-existing artifact, not a placement defect)

`run_gates.py` reports FIGUSE-001 orphans for figures 2, 3, 4, 5, 6, 7. This is a false positive
from the Phase-1 `figure-selection.md`, NOT a composition defect:

- All four SELECTED figures are panels of FIG. 1, so the true selected-integer set is `{1}`, which
  the draft references (via 1A/1B/1F/1G). True orphan set is empty.
- `gate_figure_use.py` extracts EVERY `FIG. N` token in `figure-selection.md` as "selected." That
  file names the non-selected figures with parseable tokens (the intro "(FIG. 2-6) ... (FIG. 7)"
  and the "Paired-figure relationships" table rows for FIG. 1C/1D, 3/4, 5/6, and the standalone
  1E/1H/2/7 row), so the gate treats 2-7 as selected and then orphans them.
- Fix belongs in Phase 1 (one-line scope): render the non-selected figures WITHOUT the `FIG. N`
  token form (for example "the packaging-variant family, figures two to six" and "the device block
  diagram, figure seven"), or scope the gate's "selected" set to the explicit selection table.
- Composition was NOT distorted to satisfy the gate: referencing figures 2-7 would violate the
  locked figure plan and add packaging-variant figures the spine deliberately excluded.
