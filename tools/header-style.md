# Essay header style (5:2 branded template)

The publication header for every patent essay uses one fixed series template;
per essay only the **patent figure(s)** and the **text slots** change. Built by
`tools/make_header.py`. Output: 3000x1200 PNG (exactly 5:2, X Articles cover).

## Why these choices

- **Light warm-paper background** (`#F8F2E7`): X timelines are mostly viewed in
  dark mode; a light card pops against it, and patent line art is born for
  paper. (Decision: 2026-06-11, SETI.)
- **Accent red** (`#BF3B2B`): picks up the red in the profile avatar so the
  timeline avatar and the header read as one brand row.
- **Ink navy** (`#222933`) text, **mono** secondary type: patent-document /
  engineering-drawing register, matching the blueprint decorations.

## Tokens

| token | value | used for |
|---|---|---|
| PAPER | `#F8F2E7` | canvas |
| INK | `#222933` | title, crop marks |
| INK_SOFT | `#5A5F66` | subtitle, series tag |
| ACCENT | `#BF3B2B` | badge chip, avatar ring |
| GRID | `#E2D9C4` | dot grid (58 px pitch) |
| DECOR | `#B4AA94` | dashes, corner marks, hatch block |

Type: Liberation Sans Bold (title, autosized 176→96, wraps to <=3 lines);
Liberation Mono Bold 46 (badge), Mono 46 (subtitle), Mono Bold 40 letterspaced
caps (series tag).

## Layout grid (3000x1200)

- Left text column: x 130-1310. Badge chip (y 240) → title → subtitle.
- Series row at y ~968: round avatar stamp (116 px, accent ring) + series tag.
- Right figure panel: x 1460-2870, y 120-1080. One figure centered, or several
  stacked vertically with 44 px gaps.
- Decorations: corner `+` marks, dashed frame fragments (top-left,
  bottom-right), 45-degree hatch block bottom-left, full-canvas dot grid.

## Figure treatment

1. **Band-strip**: tight-crop the cleaned sheet, dropping the `FIG. N` caption
   band and corner reference tags (row-block analysis, same logic as the
   composite builders in the run archives).
2. **Multiply blend** onto the canvas: white paper of the sheet disappears,
   line art prints directly on the card (no white box).

## Per-essay slots

| slot | convention |
|---|---|
| `--badge` | patent number + status: `US 12,636,684 B1 . GRANTED` / `US 2026/0158546 A1 . PENDING` |
| `--title` | essay title's hook half (short; the colon-tail goes to the subtitle) |
| `--subtitle` | essay title's tail or one-line thesis |
| `--figure` | the essay's header figure (repeat the flag to stack 2) |
| `--avatar` | profile photo (optional; omit to drop the stamp) |
| `--series` | default `SETI . PATENT ESSAYIST` |

## Example

```
python tools/make_header.py \
  --badge "US 2026/0158546 A1 . PENDING" \
  --title "Print It or Keep It Hard" \
  --subtitle "Tesla's tool-steel filing claims both: a die alloy you can laser-print" \
  --figure input/figures/fig-01.png \
  --avatar <profile.jpg> \
  --out runs/<essay-id>/header-branded.png
```

Requires Pillow (`pip install Pillow`) and the Liberation fonts
(`/usr/share/fonts/truetype/liberation`, present in the default environment).

Relation to the older plain composites: `figure-attachment-policy.md` still
governs *promo* attachments (original sheets, no wide composite); this branded
template is the essay-article visual header only, replacing the undecorated
5:2 composites built for the first two runs.

## Mascot edition (optional) — tools/make_header_mascot.py

The franchise header. Right side: **Gyeongtae** (경태), the studio's
anthropomorphized cat analyst (round glasses after the eye markings that named
him; navy sweater vest, white shirt, accent-red tie; wooden pointer; a rolled
patent in the other paw), presenting an easel whiteboard that carries the
essay's representative figure (band-stripped, multiply-printed on the white
board face). Left side: ticker chip + keyword title + optional subtitle +
patent-number line + series tag.

Per-essay slots: `--ticker` (`$TSLA`), `--title` (keyword/hook),
`--subtitle` (optional), `--patent` (number + GRANTED/PENDING), `--figure`
(one PNG for the board), `--out`. The title autosizes and the whole left
stack reflows so it never collides with the series row.

Assets (two editions, `--style comic|flat`, **comic is the default**):
- `tools/assets/gyeongtae-comic.svg` — comic/manhwa edition: chibi
  proportions, big amber eyes, blush, open smile, cel shading + hatching,
  lens highlights, curled ringed tail. The series face.
- `tools/assets/gyeongtae.svg` — flat editorial edition (kept for
  minimal/diagrammatic contexts).
- `tools/assets/gyeongtae-comic.png`, `gyeongtae.png` — 2x transparent
  renders for quick compositing.
Both editions share rig anchors (feet bottom ~926, pointer tip ~(24,336) in
the 620x1040 viewBox), so the compositor and any future video scenes can swap
them freely. Vector masters scale loss-free to 16:9 / 9:16 for video.

Character tokens reuse the brand palette: tabby `#8C7B6B` / stripes `#6E5F52`,
ink outlines, accent-red tie and pointer tip, ear/nose pink `#E8B4A8`/`#D98E80`.
The plain figure-panel template above remains available for figure-only covers.

## Investor edition (series default for investor digests) — tools/make_header_investor.py

Left: dual ticker chips (`--tickers "$TSLA,$SPCX"`, accent-red + ink-navy),
title, patent line (append `. INVESTOR EDITION`), monochrome company logo
strip (tools/assets/logos/, simple-icons CC0, rendered ink for editorial
reference), series tag. Right: a pure patent-figure panel (band-stripped,
multiply-printed on the paper, same treatment as the base template); pass
`--figure` once or twice, and the layout auto-picks row vs column by which
gives the drawings more area (landscape pairs stack as before/after, portrait
pairs sit side by side). 2026-06-12 brand decision (SETI): the right panel
carries patent drawings, not the mascot. The brand lives in the paper
background, the type, and the tokens; the drawings are the highest-quality
asset the series owns and are fully reproducible. The mascot editions above
remain available for secondary/video uses.
