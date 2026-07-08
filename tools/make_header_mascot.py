#!/usr/bin/env python3
"""Mascot edition of the branded 5:2 header (the series' primary template).

Right side: Gyeongtae (tools/assets/gyeongtae.svg) presenting a whiteboard
that holds the essay's representative patent figure. Left side: ticker chip,
keyword title, patent-number line, series tag. Per essay only --ticker,
--title, --patent, and --figure change.

  python tools/make_header_mascot.py \
      --ticker '$TSLA' \
      --title "Print It or Keep It Hard" \
      --patent "US 2026/0158546 A1 . PENDING" \
      --figure input/figures/fig-01.png \
      --out runs/<essay-id>/header-mascot.png \
      [--subtitle "..."] [--series "SETI . PATENT ESSAYIST"]

Requires Pillow + cairosvg. Style tokens live in make_header.py and
tools/header-style.md; the mascot master asset is SVG so the same character
scales to video formats (16:9, 9:16) later.
"""
import argparse
import io
import os
import sys

from PIL import Image, ImageChops, ImageDraw, ImageFont

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from make_header import (ACCENT, DECOR, F_MONO, F_MONO_B, INK, INK_SOFT,
                         PAPER, H, W, crop_drawing, decorate, fit_title,
                         wrap_to_width)

ASSETS = {
    "comic": os.path.join(os.path.dirname(os.path.abspath(__file__)),
                          "assets", "gyeongtae-comic.svg"),
    "flat": os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         "assets", "gyeongtae.svg"),
}

TEXT_X, TEXT_W = 130, 1230
BASELINE = 1086
BOARD = (1520, 150, 2470, 880)       # outer frame
BOARD_INSET = 46                     # figure area inset from the frame
CAT_H = 850                          # rendered mascot height (svg 620x1040)


def draw_easel(canvas, d):
    x0, y0, x1, y1 = BOARD
    d.line((1500, BASELINE, 2920, BASELINE), fill=DECOR, width=4)
    # legs
    d.line((x0 + 100, y1 + 36, x0 + 28, BASELINE), fill=INK, width=12)
    d.line((x1 - 100, y1 + 36, x1 - 28, BASELINE), fill=INK, width=12)
    # board: white face pops against the paper canvas
    d.rounded_rectangle(BOARD, radius=18, fill=(255, 255, 255),
                        outline=INK, width=10)
    # marker tray + marker
    d.rounded_rectangle((x0 + 170, y1 + 4, x1 - 170, y1 + 38), radius=8,
                        fill=PAPER, outline=INK, width=6)
    d.rounded_rectangle((x0 + 220, y1 + 10, x0 + 320, y1 + 26), radius=8,
                        fill=ACCENT)


def paste_board_figure(canvas, path):
    x0 = BOARD[0] + BOARD_INSET
    y0 = BOARD[1] + BOARD_INSET
    x1 = BOARD[2] - BOARD_INSET
    y1 = BOARD[3] - BOARD_INSET
    zone_w, zone_h = x1 - x0, y1 - y0
    fig = crop_drawing(path)
    k = min(zone_w / fig.width, zone_h / fig.height)
    fig = fig.resize((int(fig.width * k), int(fig.height * k)), Image.LANCZOS)
    x = x0 + (zone_w - fig.width) // 2
    y = y0 + (zone_h - fig.height) // 2
    region = canvas.crop((x, y, x + fig.width, y + fig.height))
    canvas.paste(ImageChops.multiply(region, fig.convert("RGB")), (x, y))


def paste_mascot(canvas, style):
    import cairosvg
    k = CAT_H / 1040
    png = cairosvg.svg2png(url=ASSETS[style], output_width=int(620 * k),
                           output_height=CAT_H)
    cat = Image.open(io.BytesIO(png)).convert("RGBA")
    feet_bottom = int(926 * k)       # paw ellipse bottom in svg coords
    x = 2385                          # pointer tip lands on the board edge
    y = BASELINE - feet_bottom
    canvas.paste(cat, (x, y), cat)


def text_block(d, ticker, title, subtitle, patent, series):
    top = 230
    f_tick = ImageFont.truetype(F_MONO_B, 72)
    tw = int(d.textlength(ticker, font=f_tick))
    d.rounded_rectangle((TEXT_X, top, TEXT_X + tw + 72, top + 124), radius=18,
                        fill=ACCENT)
    d.text((TEXT_X + 36, top + 26), ticker, font=f_tick, fill=PAPER)

    # fit the whole stack above the series row (shrink title until it fits)
    sub_lines = 0
    if subtitle:
        f_sub = ImageFont.truetype(F_MONO, 46)
        sub_lines = min(2, len(wrap_to_width(d, subtitle, f_sub, TEXT_W)))
    limit = H - 300
    start = 190
    while True:
        f_title, lines = fit_title(d, title, TEXT_W, max_lines=3, start=start)
        y = top + 124 + 58 + len(lines) * int(f_title.size * 1.12) + 36
        y += sub_lines * 62 + (18 if subtitle else 0)
        if y + 52 <= limit or f_title.size <= 96:
            break
        start = f_title.size - 8

    y = top + 124 + 58
    for ln in lines:
        d.text((TEXT_X, y), ln, font=f_title, fill=INK)
        y += int(f_title.size * 1.12)
    y += 36
    if subtitle:
        f_sub = ImageFont.truetype(F_MONO, 46)
        for ln in wrap_to_width(d, subtitle, f_sub, TEXT_W)[:2]:
            d.text((TEXT_X, y), ln, font=f_sub, fill=INK_SOFT)
            y += 62
        y += 18
    f_pat = ImageFont.truetype(F_MONO, 42)
    d.text((TEXT_X, y), patent, font=f_pat, fill=INK_SOFT)
    f_series = ImageFont.truetype(F_MONO_B, 40)
    d.text((TEXT_X, H - 210), " ".join(series.upper()), font=f_series,
           fill=INK_SOFT)


def main():
    ap = argparse.ArgumentParser(description="Mascot 5:2 essay header")
    ap.add_argument("--ticker", required=True, help="e.g. $TSLA")
    ap.add_argument("--title", required=True, help="keyword/hook title")
    ap.add_argument("--patent", required=True,
                    help="e.g. 'US 12,636,684 B1 . GRANTED'")
    ap.add_argument("--figure", required=True,
                    help="patent figure PNG for the whiteboard")
    ap.add_argument("--subtitle", default="")
    ap.add_argument("--series", default="SETI . PATENT ESSAYIST")
    ap.add_argument("--style", choices=["comic", "flat"], default="comic",
                    help="mascot edition (default: comic)")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    canvas = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(canvas)
    decorate(d)
    draw_easel(canvas, d)
    paste_board_figure(canvas, args.figure)
    paste_mascot(canvas, args.style)
    d = ImageDraw.Draw(canvas)
    text_block(d, args.ticker, args.title, args.subtitle, args.patent,
               args.series)
    canvas.save(args.out, optimize=True)
    print(args.out, canvas.size)


if __name__ == "__main__":
    main()
