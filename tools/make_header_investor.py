#!/usr/bin/env python3
"""Investor-edition 5:2 header: dual ticker chips + company logo strip on the
left, patent figure panel on the right (band-stripped, multiply-printed on the
paper, same treatment as make_header.py). No mascot: the brand is carried by
the paper background, type, and tokens.

  python tools/make_header_investor.py \
      --title "Print It or Keep It Hard" \
      --patent "US 2026/0158546 A1 . PENDING . INVESTOR EDITION" \
      --figure input/figures/fig-02A.png --figure input/figures/fig-02B.png \
      --out runs/<essay-id>/header-investor.png

Logos: tools/assets/logos/*.svg (simple-icons, CC0), rendered monochrome ink,
editorial reference to the companies discussed.
"""
import argparse
import io
import os
import sys

from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from make_header import (ACCENT, F_MONO, F_MONO_B, INK, INK_SOFT, PAPER,
                         H, W, crop_drawing, decorate, fit_title)

LOGO_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        "assets", "logos")
NAVY_CHIP = (44, 53, 67)
TEXT_X, TEXT_W = 130, 1230
FIG_ZONE = (1460, 120, 2870, 1080)


def paste_panel(canvas, paths):
    """Figures multiply-printed in FIG_ZONE; picks row vs column layout by
    whichever gives the figures more area (landscape pairs stack, portrait
    pairs sit side by side)."""
    from PIL import ImageChops
    x0, y0, x1, y1 = FIG_ZONE
    zw, zh = x1 - x0, y1 - y0
    gap = 56
    figs = [crop_drawing(p) for p in paths]
    aspects = [f.width / f.height for f in figs]
    n = len(figs)
    h_row = min(zh, (zw - gap * (n - 1)) / sum(aspects))
    w_col = min(zw, (zh - gap * (n - 1)) / sum(1 / a for a in aspects))
    if h_row * h_row * sum(aspects) >= w_col * w_col * sum(1 / a for a in aspects):
        scaled = [f.resize((int(h_row * a), int(h_row)), Image.LANCZOS)
                  for f, a in zip(figs, aspects)]
        x = x0 + (zw - sum(f.width for f in scaled) - gap * (n - 1)) // 2
        for f in scaled:
            y = y0 + (zh - f.height) // 2
            region = canvas.crop((x, y, x + f.width, y + f.height))
            canvas.paste(ImageChops.multiply(region, f.convert("RGB")), (x, y))
            x += f.width + gap
    else:
        scaled = [f.resize((int(w_col), int(w_col / a)), Image.LANCZOS)
                  for f, a in zip(figs, aspects)]
        y = y0 + (zh - sum(f.height for f in scaled) - gap * (n - 1)) // 2
        for f in scaled:
            x = x0 + (zw - f.width) // 2
            region = canvas.crop((x, y, x + f.width, y + f.height))
            canvas.paste(ImageChops.multiply(region, f.convert("RGB")), (x, y))
            y += f.height + gap


def logo_strip(canvas, d, y):
    import cairosvg
    x = TEXT_X
    f = ImageFont.truetype(F_MONO_B, 40)
    for name, label in (("tesla", "TESLA"), ("spacex", "SPACEX")):
        png = cairosvg.svg2png(url=os.path.join(LOGO_DIR, name + ".svg"),
                               output_width=54, output_height=54)
        ic = Image.open(io.BytesIO(png)).convert("RGBA")
        tint = Image.new("RGBA", ic.size, INK + (255,))
        tint.putalpha(ic.getchannel("A"))
        canvas.paste(tint, (x, y), tint)
        d.text((x + 70, y + 8), label, font=f, fill=INK)
        x += 70 + int(d.textlength(label, font=f)) + 64


def text_block(canvas, d, tickers, title, patent, series):
    y = 225
    f_tick = ImageFont.truetype(F_MONO_B, 64)
    x = TEXT_X
    for ticker, color in zip(tickers, (ACCENT, NAVY_CHIP)):
        tw = int(d.textlength(ticker, font=f_tick))
        d.rounded_rectangle((x, y, x + tw + 64, y + 108), radius=16, fill=color)
        d.text((x + 32, y + 22), ticker, font=f_tick, fill=PAPER)
        x += tw + 64 + 24
    y += 108 + 52
    f_title, lines = fit_title(d, title, TEXT_W, max_lines=2, start=170)
    for ln in lines:
        d.text((TEXT_X, y), ln, font=f_title, fill=INK)
        y += int(f_title.size * 1.12)
    y += 30
    d.text((TEXT_X, y), patent, font=ImageFont.truetype(F_MONO, 42),
           fill=INK_SOFT)
    logo_strip(canvas, d, y + 76)
    d.text((TEXT_X, y + 170), " ".join(series.upper()),
           font=ImageFont.truetype(F_MONO_B, 40), fill=INK_SOFT)


def main():
    ap = argparse.ArgumentParser(description="Investor 5:2 essay header")
    ap.add_argument("--tickers", default="$TSLA,$SPCX")
    ap.add_argument("--title", required=True)
    ap.add_argument("--patent", required=True)
    ap.add_argument("--figure", action="append", required=True,
                    help="patent figure PNG; repeat to place side by side")
    ap.add_argument("--series", default="SETI . PATENT ESSAYIST")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    canvas = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(canvas)
    decorate(d)
    paste_panel(canvas, args.figure)
    d = ImageDraw.Draw(canvas)
    text_block(canvas, d, args.tickers.split(","), args.title, args.patent,
               args.series)
    canvas.save(args.out, optimize=True)
    print(args.out, canvas.size)


if __name__ == "__main__":
    main()
