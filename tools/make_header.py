#!/usr/bin/env python3
"""Branded 5:2 header builder for patent-essay publications.

The series style is fixed (see tools/header-style.md); per-essay you swap only
the title block text and the patent figure(s):

  python tools/make_header.py \
      --badge "US 12,636,684 B1 . GRANTED" \
      --title "The Deleted Dome" \
      --subtitle "Tesla's patent runs a wiper across the bare camera lens" \
      --figure input/figures/fig-1.png \
      --out runs/<essay-id>/header-branded.png \
      [--figure second.png]          # stacks figures vertically in the panel
      [--avatar cat.jpg]             # round profile stamp next to the series tag
      [--series "SETI . PATENT ESSAYIST"]

Figures are band-stripped (sheet "FIG. N" caption + corner tag removed) and
multiply-blended onto the paper background so the line art prints on the card
instead of sitting in a white box. Output: 3000x1200 PNG (exactly 5:2).
"""
import argparse

from PIL import Image, ImageChops, ImageDraw, ImageFont

# ---------------------------------------------------------------------------
# Series style constants (the brand; per-essay content arrives via CLI)
# ---------------------------------------------------------------------------
W, H = 3000, 1200
PAPER = (248, 242, 231)      # warm paper; reads as a light card in dark mode
INK = (34, 41, 51)           # near-navy text/line ink
INK_SOFT = (90, 95, 102)     # subtitle grey
ACCENT = (191, 59, 43)       # muted signal red (matches the avatar's red)
GRID = (226, 217, 196)       # dot grid, barely-there
DECOR = (180, 170, 148)      # crop marks, dashes, hatching

FONT_DIR = "/usr/share/fonts/truetype/liberation"
F_TITLE = f"{FONT_DIR}/LiberationSans-Bold.ttf"
F_MONO = f"{FONT_DIR}/LiberationMono-Regular.ttf"
F_MONO_B = f"{FONT_DIR}/LiberationMono-Bold.ttf"

MARGIN = 130
TEXT_X, TEXT_W = MARGIN, 1180           # left column
FIG_ZONE = (1460, 120, 2870, 1080)      # right panel (x0, y0, x1, y1)

# figure band-strip tuning (same approach as the run archives' composites)
THRESH = 245
PAD = 14
GAP_MIN = 35
MINOR_FRAC = 0.18


# ---------------------------------------------------------------------------
# Figure preparation
# ---------------------------------------------------------------------------
def _row_blocks(im):
    w, h = im.size
    px = im.load()
    blocks, start, gap = [], None, 0
    for y in range(h):
        has = any(px[x, y] < THRESH for x in range(0, w, 2))
        if has:
            if start is None:
                start = y
            gap = 0
        elif start is not None:
            gap += 1
            if gap >= GAP_MIN:
                blocks.append((start, y - gap))
                start, gap = None, 0
    if start is not None:
        blocks.append((start, h - 1))
    return blocks


def crop_drawing(path):
    """Tight-crop a patent sheet to its drawing, dropping the FIG.-label band
    and small corner tags (blocks much shorter than the main drawing block)."""
    im = Image.open(path).convert("L")
    bbox = im.point(lambda p: 255 if p < THRESH else 0).getbbox()
    im = im.crop(bbox)
    blocks = _row_blocks(im)
    main = max(blocks, key=lambda b: b[1] - b[0])
    keep = [b for b in blocks
            if (b[1] - b[0]) >= MINOR_FRAC * (main[1] - main[0]) or b == main]
    top, bot = min(b[0] for b in keep), max(b[1] for b in keep)
    im = im.crop((0, max(0, top - PAD), im.width, min(im.height, bot + PAD)))
    l, t, r, b = im.point(lambda p: 255 if p < THRESH else 0).getbbox()
    return im.crop((max(0, l - PAD), 0, min(im.width, r + PAD), im.height))


def paste_figures(canvas, paths):
    """Fit one figure (or a vertical stack) into FIG_ZONE, multiply-blended."""
    x0, y0, x1, y1 = FIG_ZONE
    zone_w, zone_h = x1 - x0, y1 - y0
    gap = 44
    figs = [crop_drawing(p) for p in paths]
    inv = sum(f.height / f.width for f in figs)
    col_w = min(zone_w, int((zone_h - gap * (len(figs) - 1)) / inv))
    scaled = [f.resize((col_w, int(col_w * f.height / f.width)), Image.LANCZOS)
              for f in figs]
    total_h = sum(f.height for f in scaled) + gap * (len(scaled) - 1)
    if total_h > zone_h:  # very tall single figure: fit by height instead
        k = zone_h / total_h
        scaled = [f.resize((int(f.width * k), int(f.height * k)), Image.LANCZOS)
                  for f in scaled]
        total_h = sum(f.height for f in scaled) + gap * (len(scaled) - 1)
    y = y0 + (zone_h - total_h) // 2
    for f in scaled:
        x = x0 + (zone_w - f.width) // 2
        region = canvas.crop((x, y, x + f.width, y + f.height))
        canvas.paste(ImageChops.multiply(region, f.convert("RGB")), (x, y))
        y += f.height + gap


# ---------------------------------------------------------------------------
# Decorations (dot grid, crop marks, dashed frame fragments, hatch block)
# ---------------------------------------------------------------------------
def decorate(d):
    for gx in range(90, W - 80, 58):
        for gy in range(90, H - 80, 58):
            d.ellipse((gx, gy, gx + 2, gy + 2), fill=GRID)
    for cx, cy in [(70, 70), (W - 70, 70), (70, H - 70), (W - 70, H - 70)]:
        d.line((cx - 18, cy, cx + 18, cy), fill=DECOR, width=3)
        d.line((cx, cy - 18, cx, cy + 18), fill=DECOR, width=3)
    for x in range(MARGIN, 880, 34):                     # top-left dashes
        d.line((x, 84, x + 18, 84), fill=DECOR, width=3)
    for y in range(MARGIN, 480, 34):
        d.line((84, y, 84, y + 18), fill=DECOR, width=3)
    for x in range(W - 880, W - MARGIN, 34):             # bottom-right dashes
        d.line((x, H - 84, x + 18, H - 84), fill=DECOR, width=3)
    for y in range(H - 480, H - MARGIN, 34):
        d.line((W - 84, y, W - 84, y + 18), fill=DECOR, width=3)
    hx, hy, hw, hh = MARGIN, H - 138, 200, 48            # hatch block
    for i in range(-hh, hw, 16):
        d.line((hx + i, hy + hh, hx + i + hh, hy), fill=DECOR, width=3)


# ---------------------------------------------------------------------------
# Text block
# ---------------------------------------------------------------------------
def wrap_to_width(d, text, font, max_w):
    lines, line = [], ""
    for word in text.split():
        probe = f"{line} {word}".strip()
        if d.textlength(probe, font=font) <= max_w or not line:
            line = probe
        else:
            lines.append(line)
            line = word
    if line:
        lines.append(line)
    return lines


def fit_title(d, text, max_w, max_lines=3, start=176, floor=96):
    size = start
    while size > floor:
        font = ImageFont.truetype(F_TITLE, size)
        lines = wrap_to_width(d, text, font, max_w)
        if len(lines) <= max_lines:
            return font, lines
        size -= 8
    font = ImageFont.truetype(F_TITLE, floor)
    return font, wrap_to_width(d, text, font, max_w)


def text_block(canvas, d, badge, title, subtitle, series, avatar):
    y = 240
    # badge chip
    f_badge = ImageFont.truetype(F_MONO_B, 46)
    bw = int(d.textlength(badge, font=f_badge))
    d.rounded_rectangle((TEXT_X, y, TEXT_X + bw + 56, y + 88), radius=14,
                        fill=ACCENT)
    d.text((TEXT_X + 28, y + 18), badge, font=f_badge, fill=PAPER)
    y += 88 + 52
    # title
    f_title, lines = fit_title(d, title, TEXT_W)
    line_h = int(f_title.size * 1.12)
    for ln in lines:
        d.text((TEXT_X, y), ln, font=f_title, fill=INK)
        y += line_h
    y += 34
    # subtitle
    f_sub = ImageFont.truetype(F_MONO, 46)
    for ln in wrap_to_width(d, subtitle, f_sub, TEXT_W)[:3]:
        d.text((TEXT_X, y), ln, font=f_sub, fill=INK_SOFT)
        y += 62
    # series row (above the hatch block)
    sy = H - 232
    sx = TEXT_X
    if avatar:
        av = Image.open(avatar).convert("RGB")
        side = int(min(av.size) * 0.5)
        cx, cy = int(av.width * 0.53), int(av.height * 0.46)
        box = (max(0, cx - side // 2), max(0, cy - side // 2))
        av = av.crop((box[0], box[1], box[0] + side, box[1] + side))
        dia = 116
        av = av.resize((dia, dia), Image.LANCZOS)
        mask = Image.new("L", (dia, dia), 0)
        ImageDraw.Draw(mask).ellipse((0, 0, dia, dia), fill=255)
        canvas.paste(av, (sx, sy - 36), mask)
        d.ellipse((sx - 3, sy - 39, sx + dia + 3, sy - 36 + dia + 3),
                  outline=ACCENT, width=6)
        sx += dia + 36
    f_series = ImageFont.truetype(F_MONO_B, 40)
    d.text((sx, sy), " ".join(series.upper()), font=f_series, fill=INK_SOFT)


# ---------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser(description="Branded 5:2 essay header")
    ap.add_argument("--badge", required=True)
    ap.add_argument("--title", required=True)
    ap.add_argument("--subtitle", required=True)
    ap.add_argument("--figure", action="append", required=True,
                    help="patent figure PNG; repeat to stack vertically")
    ap.add_argument("--series", default="SETI . PATENT ESSAYIST")
    ap.add_argument("--avatar", help="profile photo for the round stamp")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    canvas = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(canvas)
    decorate(d)
    paste_figures(canvas, args.figure)
    text_block(canvas, d, args.badge, args.title, args.subtitle,
               args.series, args.avatar)
    canvas.save(args.out, optimize=True)
    print(args.out, canvas.size)


if __name__ == "__main__":
    main()
