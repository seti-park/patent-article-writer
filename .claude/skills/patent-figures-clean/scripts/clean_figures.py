#!/usr/bin/env python3
"""Mechanical layer of patent-figures-clean (Layer 1 figure preprocessing).

Converts a raw patent-figure drop (zip archives, multi-page TIFFs, mixed
PNG/JPG/GIF/BMP/WEBP) into trimmed, size-capped PNGs ready for the vision
naming pass. The AGENT does the seeing (labels, panel splits, final names);
this script only moves pixels.

Requires Pillow (`pip install pillow`) — the only non-stdlib dependency in the
repo, and only for this Phase-0 skill. PDFs are NOT supported: export images
first (USPTO full-text TIFFs and Google Patents PNGs both work).

Subcommands:
  all      extract + convert + trim + resize from --src into --work/staged/,
           writing --work/manifest.json  (the normal entry point)
  crop     cut a pixel box from a staged sheet into a new file (panel splits)
  rotate   rotate a staged file by 90/180/270 degrees
  rename   apply a JSON mapping {staged-name: final-name} from --work/staged/
           into --out (default input/figures/)

Trim gotcha, preserved from the 2026-06-26 retro: PIL's Image.getbbox() trims
BLACK borders, not white — a white-background trim is a silent no-op. The fix
is ImageChops.difference against a white canvas, which is what trim() does.
"""

import argparse
import json
import os
import shutil
import sys
import zipfile

try:
    from PIL import Image, ImageChops
except ImportError:  # pragma: no cover
    sys.stderr.write(
        "Pillow is required: pip install pillow\n"
        "(the only non-stdlib dependency in this repo, used only by Phase 0)\n")
    sys.exit(2)

IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".gif", ".bmp", ".webp", ".tif", ".tiff"}
MAX_EDGE_DEFAULT = 2000
TRIM_PAD = 16  # px of white margin to keep after the trim
WHITE_THRESHOLD = 245  # >= this (0-255) counts as background white for the trim


def _extract(src_dir, work_dir):
    """Copy loose images and unzip archives from src into work/raw/."""
    raw_dir = os.path.join(work_dir, "raw")
    os.makedirs(raw_dir, exist_ok=True)
    n = 0
    for root, _dirs, files in os.walk(src_dir):
        for name in files:
            path = os.path.join(root, name)
            ext = os.path.splitext(name)[1].lower()
            if ext == ".zip":
                with zipfile.ZipFile(path) as zf:
                    for member in zf.namelist():
                        mext = os.path.splitext(member)[1].lower()
                        if mext in IMAGE_EXTS and not member.endswith("/"):
                            target = os.path.join(raw_dir, os.path.basename(member))
                            with zf.open(member) as fin, open(target, "wb") as fout:
                                shutil.copyfileobj(fin, fout)
                            n += 1
            elif ext in IMAGE_EXTS:
                shutil.copy2(path, os.path.join(raw_dir, name))
                n += 1
            elif ext == ".pdf":
                print("SKIP (pdf unsupported, export images first): %s" % name)
    return raw_dir, n


def _to_pages(path):
    """Yield (page_index, PIL.Image) — multi-page TIFFs yield one per page."""
    img = Image.open(path)
    i = 0
    while True:
        try:
            img.seek(i)
        except EOFError:
            break
        yield i, img.copy()
        i += 1
        if not getattr(img, "is_animated", False) and i == 1:
            break


def trim(img, pad=TRIM_PAD):
    """Auto-crop white margins. getbbox() trims black, not white — so diff
    against a white canvas (ImageChops.difference) and bbox THAT."""
    rgb = img.convert("RGB")
    white = Image.new("RGB", rgb.size, (255, 255, 255))
    diff = ImageChops.difference(rgb, white)
    # Threshold faint scanner noise so near-white specks don't defeat the trim.
    gray = diff.convert("L").point(lambda p: 255 if p > (255 - WHITE_THRESHOLD) else 0)
    bbox = gray.getbbox()
    if not bbox:
        return img  # blank page; leave as-is
    left = max(bbox[0] - pad, 0)
    top = max(bbox[1] - pad, 0)
    right = min(bbox[2] + pad, img.size[0])
    bottom = min(bbox[3] + pad, img.size[1])
    return img.crop((left, top, right, bottom))


def _resize_cap(img, max_edge):
    w, h = img.size
    edge = max(w, h)
    if edge <= max_edge:
        return img
    scale = max_edge / float(edge)
    return img.resize((max(1, int(w * scale)), max(1, int(h * scale))), Image.LANCZOS)


def cmd_all(args):
    work = args.work
    staged_dir = os.path.join(work, "staged")
    os.makedirs(staged_dir, exist_ok=True)
    raw_dir, n_found = _extract(args.src, work)
    manifest = []
    for name in sorted(os.listdir(raw_dir)):
        path = os.path.join(raw_dir, name)
        base = os.path.splitext(name)[0]
        try:
            for page, img in _to_pages(path):
                img = img.convert("RGB")
                img = trim(img)
                img = _resize_cap(img, args.max_edge)
                suffix = "" if page == 0 else "-p%02d" % (page + 1)
                out_name = "%s%s.png" % (base, suffix)
                out_path = os.path.join(staged_dir, out_name)
                img.save(out_path, "PNG")
                manifest.append({"src": name, "page": page, "staged": out_name,
                                 "width": img.size[0], "height": img.size[1]})
        except Exception as e:  # keep going; report per-file failures
            manifest.append({"src": name, "error": str(e)})
            print("ERROR %s: %s" % (name, e))
    with open(os.path.join(work, "manifest.json"), "w", encoding="utf-8") as fh:
        json.dump(manifest, fh, indent=2)
    ok = [m for m in manifest if "error" not in m]
    print("extracted %d source file(s); staged %d page image(s) -> %s"
          % (n_found, len(ok), staged_dir))
    return 0 if ok else 1


def cmd_crop(args):
    img = Image.open(args.file)
    box = tuple(int(v) for v in args.box.split(","))
    if len(box) != 4:
        print("--box must be left,top,right,bottom")
        return 1
    img.crop(box).save(args.out, "PNG")
    print("cropped %s %s -> %s" % (args.file, box, args.out))
    return 0


def cmd_rotate(args):
    img = Image.open(args.file)
    img.rotate(-args.degrees, expand=True).save(args.file, "PNG")
    print("rotated %s by %d degrees (clockwise)" % (args.file, args.degrees))
    return 0


def cmd_rename(args):
    with open(args.map, "r", encoding="utf-8") as fh:
        mapping = json.load(fh)
    os.makedirs(args.out, exist_ok=True)
    staged_dir = os.path.join(args.work, "staged")
    for staged, final in sorted(mapping.items()):
        src = os.path.join(staged_dir, staged)
        dst = os.path.join(args.out, final)
        shutil.copy2(src, dst)
        print("%s -> %s" % (staged, final))
    print("renamed %d file(s) into %s" % (len(mapping), args.out))
    return 0


def main(argv=None):
    p = argparse.ArgumentParser(description="patent-figures-clean mechanical layer")
    sub = p.add_subparsers(dest="cmd", required=True)

    pa = sub.add_parser("all", help="extract + convert + trim + resize + manifest")
    pa.add_argument("--src", default=os.path.join("input", "figures-raw"))
    pa.add_argument("--work", default=os.path.join("input", "figures-work"))
    pa.add_argument("--max-edge", type=int, default=MAX_EDGE_DEFAULT)
    pa.set_defaults(func=cmd_all)

    pc = sub.add_parser("crop", help="crop a pixel box out of a staged sheet")
    pc.add_argument("file")
    pc.add_argument("--box", required=True, help="left,top,right,bottom (px)")
    pc.add_argument("--out", required=True)
    pc.set_defaults(func=cmd_crop)

    pr = sub.add_parser("rotate", help="rotate a staged file clockwise")
    pr.add_argument("file")
    pr.add_argument("--degrees", type=int, choices=[90, 180, 270], required=True)
    pr.set_defaults(func=cmd_rotate)

    pn = sub.add_parser("rename", help="apply staged->final name mapping")
    pn.add_argument("--map", required=True, help="JSON {staged-name: final-name}")
    pn.add_argument("--work", default=os.path.join("input", "figures-work"))
    pn.add_argument("--out", default=os.path.join("input", "figures"))
    pn.set_defaults(func=cmd_rename)

    args = p.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
