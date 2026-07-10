# Figures Rationale (Compose placements)

## Figure-enabled edition (supersedes the earlier text-only declaration)

The run became figure-enabled mid-flight: `input/figures/` now holds the cleaned priority set
(index `1, 2, 3, 4, 6, 38, 42, 43, 45, 46`) and Phase 1 `figure-selection.md` selects four
figures — the mechanism spine the reader most needs to *see*: system → multiply →
align-and-accumulate core → parallel weights. All four are placed; captions are grounded in the
figures manifest plus `[dddd]` paragraph anchors that trace to invention-summary Quotable spans
/ Quote anchor rows. Header uses `image-plus-caption`; body figures use `caption-only-italic`
per `references/figure-rendering.md`.

## Placement table

| Figure | Placement | caption_role | Rendering | Rationale |
|---|---|---|---|---|
| FIG. 4 | Header (cover, above §1) | header_composite | image-plus-caption | The one drawing that shows the thesis at a glance: mantissa shift onto the block's largest exponent and the column adder tree summing in the integer domain → INT35. It IS claim 1's (b)+(c). Caption trimmed in round-2 (r2-F1) from ~86 to 52 words for cover-surface invitation — dropped the "(426)" reference number and the shift-arithmetic narration, kept the align-once/adder-tree core and the claim tie; anchors `[0199]` (Emax=22 → INT5), `[0011]` (adder tree, integer format), `[0145]` (INT35 out). The §2 ¶4 in-prose FIG. 4 pointer was removed in round-2 (r2-F2); FIG. 4 stays tokenized here in the header. |
| FIG. 1 | §2, after ¶1 (system datapath para) | body_figure_carries_unique_info | caption-only-italic (medium, ~28 words) | The one-pass datapath the reader orients on before the mechanism deep-dive: input buffer → CIM macro (101) → mode decoding (110) → dequantization (106) → FP22. Carries reference numbers not spelled out in prose. Anchors `[0006]` (mode decoding sets format), `[0142]`, `[0145]`. |
| FIG. 3 | §2, after the [0011] claim blockquote | body_figure_prose_covers_fully | caption-only-italic (short, ~10 words) | One column cell — the multiply that makes a single primitive product. Prose (§2 ¶3) already covers the mechanism, so the figure is a visual anchor only; short identifier caption. Anchor `[0011]`. |
| FIG. 43 | §4, after the double-buffering para | body_figure_carries_unique_info | caption-only-italic (medium, ~28 words) | The double-bitcell cell (4303): BC0/BC1 sharing bit lines with separate write-wordlines — the dual-bank structure behind double-buffered weight loads. Carries the BC0/BC1 + write-wordline detail not in prose. Anchors `[0012]` (parallel write + VMM), `[0015]` (double-buffering). |

## Value-add cross-references — REMOVED in round-2 (r2-F2)

Draft_version 2 carried two prose cross-references to available-but-unselected figures (FIG. 38
in §2 ¶4, FIG. 45 in §5). They were removed in round-2 (r2-F2): both pointed to figures the
article does not display (mild "where is that?" friction for the retail reader), and they had
existed substantially to clear a `gate_figure_use` orphan that the selection file's
paired-figure prose triggered. With the upstream `figure-selection.md` tokenization corrected
(so "FIG. 38/42" and "FIG. 45/46" no longer tokenize as selected), the orphan pressure is gone
and the pointers are no longer load-bearing. Removing them also deletes the two slightly
mechanical prose semicolon joins the round-2 reviewer noted. No `[dddd]` anchor or verbatim
quote was removed; the §5 `[0118]` scan-test quote is kept.

After the removal, the only figure tokens in the draft are FIG. 1, FIG. 3, FIG. 4, FIG. 43 —
the four selected + placed figures.

## Not figure-backed (prose carries these)

§1 lead, §3 scope-and-baseline, §5 what-the-filing-is, §6 closing take no figure — prose carries
them and a figure would only decorate. The §5 depth point is carried entirely in prose (clock
margins, scan chains, the `[0118]` scan-test quote). FIG. 2, 6, 38, 42, 45, 46 remain available
but unreferenced (no reader value beyond the four placed figures).

## Gate note

- `gate_figure_use`: PASS. Selected figures 1, 3, 4, 43 are all referenced; the draft carries
  no other figure tokens (the FIG. 38 / FIG. 45 cross-references were removed in round-2 r2-F2).
- `gate_anchors` FIGREF: PASS. Every "FIG. N" in the draft (1, 3, 4, 43) is in the available
  `figures-index.txt` set.
- **Upstream flag (resolved for this run):** the round-2 removal depends on the design-architect
  reword of the unselected-figure discussion in `figure-selection.md` so "FIG. 38/42" /
  "FIG. 45/46" no longer tokenize as selected. The orchestrator reports that correction landed
  upstream, so dropping the two cross-references does not re-trigger the FIGUSE-001 orphan.
