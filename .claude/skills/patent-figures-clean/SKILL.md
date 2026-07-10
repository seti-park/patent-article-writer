---
name: patent-figures-clean
description: >
  Phase 0 (Layer 1) figure preprocessing for the patent-essay pipeline. Turns a
  raw figure drop — zip archives, multi-page TIFFs, or loose images under
  input/figures-raw/ — into cleaned, white-trimmed, size-capped, canonically
  named input/figures/fig-NN.png files plus a vision-verified
  figures-manifest.md and the figures-index list the gates consume. Use when
  input/figures/ is empty or stale (see "Stale figures" below) and a raw figure
  source exists, or when the user asks to clean, rename, split, or verify patent
  figures.
allowed-tools: Read, Write, Edit, Grep, Glob, Bash
context: fork
agent: figures-prep
---

# patent-figures-clean — Phase 0 (Layer 1)

Raw patent figures are hostile inputs: multi-page TIFFs, one sheet holding six panels,
filenames that say `US12345678-20260224-D00003.tif` while the pixels say "FIG. 5", scanner
margins, and 4000-px pages that waste every downstream token. This skill normalizes all of
that BEFORE Phase 1, so figure-selection reasons about figures, not file archaeology.

Division of labor: `scripts/clean_figures.py` (Pillow) moves pixels; the agent's eyes assign
names and verify. Never name a file from its source filename — read the image.

```
input/figures-raw/  (zip / tif / png / jpg, as delivered)
    → clean_figures.py all      # extract + PNG + white-trim + size-cap → input/figures-work/staged/
    → vision naming pass        # agent reads every staged image, builds the name map
    → clean_figures.py crop/rotate  # panel splits, orientation fixes (as needed)
    → clean_figures.py rename   # staged → input/figures/fig-NN.png
    → verification loop         # agent re-reads finals; label ↔ filename must agree
    → input/figures/figures-manifest.md + figures-index list
```

## Process

1. **Mechanical pass.**
   `python .claude/skills/patent-figures-clean/scripts/clean_figures.py all`
   (defaults: `--src input/figures-raw --work input/figures-work`). Requires Pillow —
   `pip install pillow` if the import fails. PDFs are skipped by design: export images first
   (USPTO full-text TIFFs and Google Patents PNGs both work).
2. **Vision naming pass.** Read EVERY staged PNG (`input/figures-work/staged/`). For each,
   record: the "FIG. N" label(s) visible, orientation, whether it is a single figure, a
   multi-panel sheet of ONE figure (e.g. FIG. 5A-5F), or a mixed sheet (panels of different
   figures), and any legibility problems.
3. **Fix geometry.** Sideways sheets: `rotate --degrees 90|180|270`. Mixed sheets: `crop
   --box l,t,r,b --out <staged-name>` per panel group (pick boxes from what you saw in
   step 2; re-Read the crop to confirm).
4. **Name map.** Write `input/figures-work/name-map.json` mapping staged → final:
   - single figure: `fig-03.png` (2-digit, zero-padded);
   - one-figure panel sheet: `fig-05AF.png` (first+last panel letters, per the repo's
     existing convention);
   - cover/derived composites keep a suffix: `fig-05-sequence.png`.
   Then `clean_figures.py rename --map input/figures-work/name-map.json`.
5. **Verification loop (mandatory).** Re-Read every file in `input/figures/`: the visible
   label must match the filename; trim must not have cut a reference numeral; text must be
   readable at the delivered size. Fix and repeat until clean — a mismatch you ship becomes
   a false FIGREF/FIGUSE verdict downstream.
6. **Emit the manifest**: `input/figures/figures-manifest.md`:

   ```markdown
   # Figures manifest — <patent id>

   patent: <identifier>

   | Figure | File | Labels seen | Description (one line) | Flags |
   |---|---|---|---|---|
   | FIG. 1 | fig-01.png | FIG. 1 | System block diagram: control unit 414 ... | |
   | FIG. 5A-5F | fig-05AF.png | FIG. 5A..5F | Kneel sequence, phases 1-2 | legibility: small numerals |
   ```

   Header line `patent: <identifier>` is **mandatory** (written by this stage;
   bootstrap and RUN-012 identity checks consume it). Plus the figures-index list
   (one integer per line — Phase 1 copies it to `handoff/01-design/figures-index.txt`
   for the gates).

## Stale figures

`input/figures/` is **stale** when either:

- `figures-manifest.md` is missing, or
- manifest header `patent:` ≠ the current `input/patent.md` identifier

Stale ⇒ bootstrap clears `input/figures/`, `input/figures-work/`, `input/figures-raw/`
before stages run. Manifest missing but `fig-*.png` present is also stale.

## Pre/post conditions

Pre: `input/figures-raw/` (or a path given in the invocation) holds the raw drop.
Post: `input/figures/fig-*.png` cleaned + verified; `figures-manifest.md` present with
`patent:` header; raw sources untouched; `input/figures-work/` left in place for audit
(gitignored).

## Out of scope

- Figure SELECTION (which figures the essay uses) — Phase 1 `thesis-architect` Step 9.
- Cover composition (5:2 header strips) — `tools/` + `tools/header-style.md`.
- PDF rasterization — export images upstream.
