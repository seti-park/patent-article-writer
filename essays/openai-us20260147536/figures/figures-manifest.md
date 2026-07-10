# Figures manifest — US 2026/0147536 A1 (OpenAI, "Alignment in Hardware Accelerators")

Source: `input/figures-raw/` (figs1.zip / figs2.zip / figs3.zip, 64 drawing sheets, USPTO
full-text TIFF/PNG scans). Every sheet was read from the 300 KB downscaled copies in
`input/figures-raw/_small/src-NN.png`; the printed "FIG. N" label and "Sheet N of 64" header
were used as ground truth (not the source filenames, which are generic `Safari-N 2.PNG`).
All 64 sheets carry a clean 1:1 sheet-number -> FIG-number mapping — no sheet's printed FIG
number diverged from its position in the "Sheet N of 64" sequence.

Orientation: every sheet is a landscape figure rotated inside a portrait page. All 64 sheets
needed the same fix: rotate 90° clockwise (`img.rotate(-90, expand=True)` in PIL / the
skill script's `rotate --degrees 90`) to bring the "FIG. N" caption and drawing content to
normal upright, left-to-right reading orientation.

Cleaned in this run (priority set only — FIG. 1, 2, 3, 4, 6, 38, 42, 43, 45, 46): loaded the
full-resolution original (path via `_small/mapping.txt`), rotated 90° CW, white-margin
trimmed, long edge capped at 2000 px, saved as optimized PNG to `input/figures/fig-NN.png`.
The other 54 sheets are catalogued below (identified, oriented, not cleaned to fig-NN.png in
this run).

| Figure | File | Labels seen | Description (one line) | Flags |
|---|---|---|---|---|
| FIG. 1 | fig-01.png | FIG. 1 | Accelerator block diagram: 32x32 digital compute-in-memory macro (101) with input buffer, quantization scales/dequantization (106), output register (108), mode decoding (110) | |
| FIG. 2 | fig-02.png | FIG. 2 | CIM macro (101) 32x32 array: Row 0-31 x Col 0-31 grid with Act[] row inputs and Wdata[] column weight inputs | |
| FIG. 3 | fig-03.png | FIG. 3 | Column cell (Col 0, Row 0) detail: sign/exponent/mantissa bit-cell logic feeding exponent-handling and mantissa-handling blocks | |
| FIG. 4 | fig-04.png | FIG. 4 | Functional block for mantissa alignment (adder tree, 3880/3882/3884/426): per-row shift calculation (Emax-E), 2's-complement shift, feeding the column adder tree | |
| FIG. 5 | (not cleaned) | FIG. 5 | Operations flow (500, S1-S4): multiply activation x weight, align mantissas, add primitive products, dequantize to reduced FP precision | |
| FIG. 6 | fig-06.png | FIG. 6 | Data flow through one column (600): FP8 activation x FP6 weight -> FP11 multiply block, adder, mapped onto the 32x32 column array (101/220/222) | |
| FIG. 7 | (not cleaned) | FIG. 7 | Enlarged column cell (Col 0/Row 0, 220/222): sign/exponent/mantissa bit-cell + logic detail with adder-tree-per-column context | |
| FIG. 8 | (not cleaned) | FIG. 8 | Enlarged column cell (continuation, 830/832): exponent handling and mantissa handling block detail | |
| FIG. 9 | (not cleaned) | FIG. 9 | Exponent-bit scheme (830): exponent handling full-adder chain (E0-E4) with the underlying addition table | |
| FIG. 10 | (not cleaned) | FIG. 10 | Mantissa-bit scheme (832): mantissa handling full-adder chain with the underlying multiply/add table | |
| FIG. 11 | (not cleaned) | FIG. 11 | Mantissa-bit scheme variant (832): "normal"/"Anormal" partial-product terms feeding the mantissa handling adder chain | |
| FIG. 12 | (not cleaned) | FIG. 12 | Lower-FP-precision scheme: column cell with blacked-out (unused) exponent/mantissa bit positions for a narrower FP format | |
| FIG. 13 | (not cleaned) | FIG. 13 | Lower-FP exponent scheme (830): exponent handling with blacked-out unused bit positions and adder chain | |
| FIG. 14 | (not cleaned) | FIG. 14 | Lower-FP exponent scheme comparison: FP8(1-4-3)xFP6(1-3-2) vs FP8(1-4-3)xFP4(1-2-1) exponent adder trees (1440/1442) | |
| FIG. 15 | (not cleaned) | FIG. 15 | Lower-FP mantissa scheme (832): mantissa handling adder chain with multiply/add table | |
| FIG. 16 | (not cleaned) | FIG. 16 | Lower-FP mantissa scheme comparison: FP8xFP6 vs FP8xFP4 mantissa handling (832), shared terms circled | |
| FIG. 17 | (not cleaned) | FIG. 17 | Lower-FP mantissa scheme: FP6xFP4 multiply equation and mantissa handling block (832) | |
| FIG. 18 | (not cleaned) | FIG. 18 | Lower-FP mantissa scheme comparison: FP8xFP6 vs FP8xFP4 (832), additional shared-term circles annotated | |
| FIG. 19 | (not cleaned) | FIG. 19 | Various FP formats (1950/1952): bit-cell columns 0-5 feeding multiplexers that select FP4/FP6 weight data per bit line | |
| FIG. 20 | (not cleaned) | FIG. 20 | Exponent scheme comparison (830): FP6(1-3-2)xFP6(1-3-2) vs FP6(1-3-2)xFP4(1-2-1) exponent handling adder chains | |
| FIG. 21 | (not cleaned) | FIG. 21 | Exponent scheme comparison (830): FP6(1-2-3)xFP6(1-3-2) vs FP6(1-2-3)xFP4(1-2-1) | |
| FIG. 22 | (not cleaned) | FIG. 22 | Exponent scheme comparison (830): FP4(1-2-1)xFP6(1-3-2) vs FP4(1-2-1)xFP4(1-2-1) | |
| FIG. 23 | (not cleaned) | FIG. 23 | Mantissa scheme comparison (832): FP6(1-3-2)xFP6(1-3-2) vs FP6(1-3-2)xFP4(1-2-1) mantissa handling | |
| FIG. 24 | (not cleaned) | FIG. 24 | Mantissa scheme comparison (832): FP6(1-2-3)xFP6(1-3-2) vs FP6(1-2-3)xFP4(1-2-1) | |
| FIG. 25 | (not cleaned) | FIG. 25 | Mantissa scheme comparison (832): FP4(1-2-1)xFP6(1-3-2) vs FP4(1-2-1)xFP4(1-2-1) | |
| FIG. 26 | (not cleaned) | FIG. 26 | Logic circuit: single column-cell (220) sign/exponent/mantissa primitive block detail | |
| FIG. 27A-27C | (not cleaned) | FIG. 27A, FIG. 27B, FIG. 27C | Logic circuits: bit-cell schematics (WL/BL) with write-select transistors and XOR/XNOR gate combinations producing mantissa bit outputs M[0]/M[1]/M[2] and carry/sign signals | multi-panel sheet, one figure family |
| FIG. 28 | (not cleaned) | FIG. 28 | Exponent column cell (2860/2862/2864/2866): full-adder pair merging two adjacent column-cell exponent bits (Ej-1/Ej) | |
| FIG. 29 | (not cleaned) | FIG. 29 | Exponent column cells array (220): 12 column-cell bit-cell + half-adder units (S0-S11/C0-C11) across the Wdata/Act bus | |
| FIG. 30 | (not cleaned) | FIG. 30 | Mantissa scheme (832): 3b x 3b multiply equation feeding a cascaded full-adder mantissa-handling tree | |
| FIG. 31 | (not cleaned) | FIG. 31 | Mantissa scheme (832): 4b x 3b multiply equation feeding a larger cascaded full-adder mantissa-handling tree | |
| FIG. 32 | (not cleaned) | FIG. 32 | Resource-utilization method (3200, steps 3202-3208): determine exponent bits, weight elements, mantissa bits, and full adders needed per column cell | |
| FIG. 33 | (not cleaned) | FIG. 33 | Resource-utilization method (3300, steps 3302-3308): mirrored steps keyed to mantissa bits first, then weight elements, exponent bits, full adders per column cell | |
| FIG. 34 | (not cleaned) | FIG. 34 | Mantissa alignment method (3400, steps 3402-3408): determine Emax, shift value per primitive product, align mantissas, send to adder tree | |
| FIG. 35 | (not cleaned) | FIG. 35 | Mantissa alignment scheme (3574): shift-register array showing P_M_i<6:0> mantissa bits positioned relative to Emax | |
| FIG. 36 | (not cleaned) | FIG. 36 | Mantissa alignment scheme (3676): 22 shift-position options per 7-bit group, shown as overlapping shift windows over the 3574 register | |
| FIG. 37 | (not cleaned) | FIG. 37 | Mantissa alignment scheme (3770/3772/3778): multiplexer bank selecting shifted mantissa bits from the 3574/3676 shift registers | |
| FIG. 38 | fig-38.png | FIG. 38 | Column cell for mantissa alignment (222): adder tree (426) + fp2int block (2's-complement + sign, multiplexer bank, shift calculation, 3772/3880) + bitcell_mul layout (sign/exponent/mantissa bitcells, 3882) | |
| FIG. 39 | (not cleaned) | FIG. 39 | Another alignment scheme (3970/3972/3978): 5-stage shift network applying Eshift[0]-Eshift[4] to mantissa bits | |
| FIG. 40 | (not cleaned) | FIG. 40 | RTL script: Verilog `always_comb` block computing p_shift, p_m_sint, p_m_s, p_m_tc (2's-complement mantissa shift) | |
| FIG. 41 | (not cleaned) | FIG. 41 | CIM signals: DCIM macro (101) block diagram with 5-to-32 weight decoder (4190), row adder trees (220/222), output registers/muxes (4196), clock gating (4192/4194/4198) | |
| FIG. 42 | fig-42.png | FIG. 42 | Compute timing diagram (4200): clk / act_valid / clk_act / act_data / out_valid / clk_out / out_data waveforms | |
| FIG. 43 | fig-43.png | FIG. 43 | Double-bitcell design (4303): bitcell_double blocks (BC0/BC1) per column, BL0-BL31 bit lines, ww10/ww11 write-word-lines | |
| FIG. 44 | (not cleaned) | FIG. 44 | Write timing diagram (4400): clk / wgt_valid / clk_wgt / wgt_data / wgt_addr / addr / wl0 / wl1 / bc0_q / bc1_q waveforms | |
| FIG. 45 | fig-45.png | FIG. 45 | Double-bitcell design (4503/4505/4507/4509): scan-input mux + bc0/bc1 latches + output select mux producing wgt_out | |
| FIG. 46 | fig-46.png | FIG. 46 | Double-bitcell scan design (4603): bc0/bc1 latches with EN/ENB driven by wl/wlb (write) and wgt_update/wgt_updateb (read) | |
| FIG. 47 | (not cleaned) | FIG. 47 | Double-bitcell scan design (4703/4711/4713): bc0/bc1 latches with scan-clock muxes selecting clk_scan vs wlb/wgt_update | |
| FIG. 48 | (not cleaned) | FIG. 48 | Double-bitcell scan design (4803): Bitcell Latch 0 / Latch 1 chained through Scan In Mux 0 / Mux 1 (si/se scan shift path) | |
| FIG. 49 | (not cleaned) | FIG. 49 | Wordline-signal circuit (4900): clk_scan-gated mux (sm select) choosing wl0/wl1, producing wlb0/wlb1 | |
| FIG. 50 | (not cleaned) | FIG. 50 | Scan timing (5000): master/slave latch waveforms showing t1-t4 closing/opening transitions on wlb0/wlb1 | |
| FIG. 51 | (not cleaned) | FIG. 51 | Scan clock circuit (5100): cross-coupled NOR-gate clock generator producing clk/clkb from clk_orig via td1/td2 delay cells | |
| FIG. 52A-52B | (not cleaned) | FIG. 52A, FIG. 52B | Double-bitcell scan design (5200) + scan-clock timing (5202): bitcell_double ww0/ww1 gating and clk_orig/clkb/clk waveform with td1/td2 markers | multi-panel sheet, one figure family |
| FIG. 53 | (not cleaned) | FIG. 53 | Wordline scan circuit (5300): NAND2 decode trees (X4/X8) gated by clk/clkb and bc_sel/bc_sellb producing ww10/ww11/wwlb0/wwlb1 | |
| FIG. 54 | (not cleaned) | FIG. 54 | Bitcell scan signals: addr[4:0] -> wgt_clk gating cell and bc_sel -> clk_orig gating cell | |
| FIG. 55 | (not cleaned) | FIG. 55 | Wordline scan circuit (5500): NAND2 decode trees (X4/X8), scanmode-gated clk/clkb producing ww11/wwlb1/ww10/wwlb0 (variant of FIG. 53) | |
| FIG. 56A-56B | (not cleaned) | FIG. 56A, FIG. 56B | Parallel scheme (5600A/5600B): bl/act row-column grid showing wl0-wl3 write-line activation pattern, transposed view | multi-panel sheet, one figure family |
| FIG. 57A-57B | (not cleaned) | FIG. 57A, FIG. 57B | Parallel scheme (5700A/5700B): expanded bl/act grid, 4 wordlines x 4 bitlines per block (bl10-bl33), transposed view | multi-panel sheet, one figure family |
| FIG. 58A-58C | (not cleaned) | FIG. 58A, FIG. 58B, FIG. 58C | Parallel scheme: (A) single-row bitcell strip (bl0-bl7/act0/wl0); (B) stacked column of bitcell rows (b10-b17/act0); (C) 32x32 row/column array (Row 0-31 x Col 0-31) | multi-panel sheet, one figure family |
| FIG. 59A-59B | (not cleaned) | FIG. 59A, FIG. 59B | Parallel scheme: (A) 6-bitcell row strip (b10-b15/wl0/act[7:0]); (B) stacked column view (b10-b15/act[0:2]/act[3:6]/act[7]/wl0) | multi-panel sheet, one figure family |
| FIG. 60 | (not cleaned) | FIG. 60 (Table 2) | FP-format table: activation/weight bit assignments and primitive-product outputs across 8 modes of operation (FP8/FP6/FP4 combinations) | |
| FIG. 61 | (not cleaned) | FIG. 61 (Table 4) | Resource-optimization scheme: full-adder counts per row for FP8/FP6/FP4 multiplier bit sizes, at 60 vs 12 total exponent bits per row (4-bit multiplicand) | |
| FIG. 62 | (not cleaned) | FIG. 62 (Table 5) | Resource-optimization scheme: full-adder counts per row for FP8/FP6/FP4, 3-bit mantissa multiplicand variant | |
| FIG. 63 | (not cleaned) | FIG. 63 (Table 6) | Resource-optimization scheme: full-adder counts per row keyed to total mantissa bits per row (4-bit multiplicand) | |
| FIG. 64 | (not cleaned) | FIG. 64 (Table 7) | Resource-optimization scheme: full-adder counts per row keyed to total mantissa bits per row (3-bit multiplicand) | |

## Cleaned this run (10 files -> `input/figures/`)

| fig-NN.png | Source sheet | Rotation applied |
|---|---|---|
| fig-01.png | src-01 (`_extracted/figs1/Safari-1 2.PNG`) | 90° CW |
| fig-02.png | src-02 (`_extracted/figs1/Safari-2 2.PNG`) | 90° CW |
| fig-03.png | src-03 (`_extracted/figs1/Safari-3 2.PNG`) | 90° CW |
| fig-04.png | src-04 (`_extracted/figs1/Safari-4 2.PNG`) | 90° CW |
| fig-06.png | src-06 (`_extracted/figs1/Safari-6 2.PNG`) | 90° CW |
| fig-38.png | src-38 (`_extracted/figs2/Safari-38 2.PNG`) | 90° CW |
| fig-42.png | src-42 (`_extracted/figs2/Safari-42 2.PNG`) | 90° CW |
| fig-43.png | src-43 (`_extracted/figs3/Safari-43 2.PNG`) | 90° CW |
| fig-45.png | src-45 (`_extracted/figs3/Safari-45 2.PNG`) | 90° CW |
| fig-46.png | src-46 (`_extracted/figs3/Safari-46 2.PNG`) | 90° CW |

All 10 re-Read post-clean: visible "FIG. N" caption matches the filename, no reference
numeral was cut by the white-margin trim, and text is readable at the delivered (long-edge
capped at 2000 px) size. No `legibility: poor` flags — every cleaned figure's labels were
confirmed readable, including the denser FIG. 38 (multiplexor/bitcell layout) where the
smallest "sign" / "bitcell" cell labels remain legible at delivered resolution.

## Notes

- No sheet's printed FIG number diverged from its position in the "Sheet N of 64" sequence
  (i.e., src-NN carries FIG. N, or FIG. NA/NB/NC for the multi-panel sheets) — the ground-truth
  Brief-Description list in the task prompt held exactly, contrary to the general warning that
  the src-to-FIG mapping is not always 1:1 after the first multi-figure sheet.
- Multi-panel sheets (27, 52, 56, 57, 58, 59) each carry panels of a SINGLE figure family
  (e.g. FIG. 56A/56B), so per the skill's convention these would be named `fig-56AB.png` etc.
  if/when cleaned — none mixes panels from different figure numbers, so no `crop` split is
  needed for any of the 64 sheets.
- `input/figures-raw/` sources were not modified. No `__MACOSX` / `._*` junk was found under
  `input/figures-raw/` (already absent from `_extracted/`); nothing to delete.
- `input/figures-work/` (staged PNGs from a prior `clean_figures.py all` run) was left in
  place for audit, per the skill's postcondition; it was not used to produce the fig-NN.png
  files above (the priority set was cleaned directly from the full-resolution originals per
  this task's crash-avoidance instructions).
