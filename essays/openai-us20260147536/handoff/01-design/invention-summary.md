# Invention Summary

## Metadata

- **Patent ID**: US 2026/0147536 A1 (publication; Appl. No. 19/397,773)
- **Title**: Alignment in Hardware Accelerators
- **Filing date**: 2025-11-21 (provisional 63/724,159 filed 2024-11-22)
- **Publication date**: 2026-05-28
- **Inventors**: Burak Erbagci (San Jose, CA), Cagla Cakir (San Francisco, CA), Alexander Almela Conklin (San Jose, CA), Tracey DellaRova (Wake Forest, NC), Jean-Didier Allegrucci (Sunnyvale, CA)
- **Classification**: Int. Cl. G06F 7/487; G06F 5/08; G06F 7/501; G06F 17/16. CPC G06F 7/4876; G06F 5/08; G06F 7/501; G06F 17/16
- **Assignee**: OpenAI Opco, LLC (San Francisco, CA)
- **Status**: pending application (published, pre-grant). Claims 11-19 are marked "(canceled)" in this publication.

## 발명 명칭 / 기술분야

Essay-ready phrasing: a compute-in-memory math engine for AI accelerators that multiplies low-precision floating-point activations and weights inside the memory array, then lines up the results so a plain integer adder tree can sum them, converting back to floating point only once at the end. 기술분야: hardware accelerators for AI and high-performance computing, specifically digital compute-in-memory (CIM) architectures performing vector-matrix operations with format-agile floating-point handling and dequantization to higher-precision outputs `[0001]`.

## 종래 문제 / 과제

AI training and inference are dominated by matrix-vector multiplications executed in compact numeric formats on accelerators `[0002]` `[0004]`. Conventional pipelines move activations and weights back and forth between numeric domains (higher-precision floating point for training/software, lower-precision integer in the datapath), and every conversion step costs silicon: scaling, rounding, and saturation logic that adds area, power, and latency, and can accumulate quantization error across layers `[0005]`. As new sub-8-bit floating-point variants keep appearing, fixed conversion pipelines and format-specific datapaths become hard to adapt `[0005]`. Separately, conventional (von Neumann) accelerators shuttle data between memory and arithmetic cores, which CIM architectures exist to avoid `[0133]`.

**Quotable spans:**
- `[0005]`: "These operations can involve transforming activations and weights back and forth between different numeric domains"
- `[0005]`: "Each conversion step requires additional scaling, rounding, and saturation logic, which adds area, power, and latency to already dense compute fabrics, and can introduce cumulative quantization errors that degrade numerical behavior over many layers."
- `[0005]`: "fixed conversion pipelines and format-specific data paths become increasingly difficult to adapt, limiting the flexibility of the hardware to support evolving models and deployment scenarios"
- `[0133]`: "This architecture is beneficial for accelerating AI workloads like deep learning by reducing the von Neumann bottleneck."

## 청구항 분석 — 4-layer core mechanism

### Layer 1 — What (one sentence)

A compute-in-memory macro whose column cells generate floating-point products of activations and stored weights, whose functional block aligns the products' mantissa bits by shifting them against the block's maximum exponent, and whose adder tree then accumulates everything in integer format, deferring the return to floating point to a single dequantization step (independent claims 1, 20, and 29) `[0011]`.

### Layer 2 — How (mechanism)

1. A mode decoding unit (110) reads the floating-point formats chosen for activations (FP8/FP6/FP4) and weights (FP6/FP4) and issues control signals that set the arithmetic mode of the whole vector-matrix multiplication (VMM) `[0146]` `[0130]` (Table 1 lists 8 modes).
2. Weight values sit resident in memory cells inside the CIM macro (101); a 1×32 vector of activations streams in through an input buffer (102), with a shared per-block scaling factor held in a scale buffer (104) per the microscale (MXFP) block format `[0141]` `[0142]` `[0143]`.
3. Each column cell (220) multiplies one activation by one stored weight in floating point: an XOR gate produces the sign, half adders plus the exponent handling block (830) add the exponents, and AND-gate partial products plus a full-adder array in the mantissa handling block (832) multiply the mantissas, yielding a "primitive product" (e.g., FP11 for FP8×FP6) `[0159]` `[0164]` `[0166]` `[0170]`.
4. The functional block for mantissa alignment (3880) finds the maximum exponent among the column's 32 primitive products, computes a per-product shift value in the shift calculation and select decoding unit (3882), and shifts each product's mantissa bits accordingly through a multiplexer shifter (3770) or a logarithmic multiplexer tree (3970), placing all products on one common integer scale `[0199]` `[0200]` `[0204]` `[0206]`.
5. Two's complement and sign are computed (3884) so negative products can ride the same integer path `[0205]` `[0209]`.
6. The adder tree (426) sums the 32 aligned mantissas in the integer domain, outputting one INT35 accumulation value plus an INT5 exponent per column, every cycle in pipelined operation `[0207]` `[0147]`.
7. A dequantization unit (106) outside the macro fuses the stored scaling factor once, converting the integer dot products to FP22 for output (108) `[0145]`.
8. In parallel with compute, double bitcells (BC0/BC1) in each memory cell allow the next weight matrix to be written into one bank while the other bank feeds the ongoing VMM, steered by a weight select signal (wgt_sel) through the weight address decoder (4190) and weight output multiplexers (4509) `[0219]` `[0229]` `[0230]`; the same cells double as a scan chain for testing `[0118]`.

**Key components**: compute engine (100), CIM macro (101), input buffer (102), scale buffer (104), dequantization unit (106), output register (108), mode decoding unit (110), column cell (220), computing unit column (222), adder tree (426), exponent handling block (830), mantissa handling block (832), functional block for mantissa alignment (3880), shift calculation and select decoding unit (3882), two's complement and sign unit (3884), shifters (3770/3970), weight address decoder (4190), double-bitcell memory cells (4303/4503/4603/4703), weight output multiplexer (4509)

### Layer 3 — Why novel

- **Relative to prior art (as the patent frames it)**: conventional flows convert between numeric domains at each stage and hard-wire one format per datapath `[0005]`; this design keeps the accumulation entirely in the integer domain after ONE mantissa alignment, and one physical datapath serves many FP formats under mode control, "without requiring separate conversion pipelines or dedicated cores for each format" `[0006]`.
- **Industry practice contrast**: mainstream AI accelerators (GPU/TPU tensor cores) fetch weights from memory into arithmetic units and accumulate in floating-point units; here the multiplication happens where the weights are stored ("computations ... directly performed within a memory array to minimize data movement" `[0133]`), and the reduction network is a synthesizable integer adder tree rather than FP hardware `[0139]` `[0160]`. Note: block-scaled (block floating point / MX) data formats themselves are an industry standard (OCP MX, 2023); what this document claims is circuit structure that executes them natively, not the format idea (see fact-check-log `ocp-mx-spec-2023-09`).

### Layer 4 — Innovation angles

- **integer-domain-accumulation**: multiply in FP, align mantissas once per block, accumulate on integer adders, dequantize once. The core of independent claims 1, 20, and 29.
  - Evidence paragraphs: `[0011]`, `[0100]`, `[0104]`, `[0145]`, `[0199]`
  - Quote anchor refs: `q-0011-1`, `q-0011-2`, `q-0011-3`, `q-0104-1`, `q-0145-1`, `q-0199-1`
- **format-agile-arithmetic**: one column-cell datapath serves FP8/FP6/FP4 activation and weight combinations under a mode decoding unit; multiplexers zero out unused bits instead of duplicating hardware. Description/aspect material in this publication; NOT required by the pending claims (see Claim scope map).
  - Evidence paragraphs: `[0006]`, `[0130]`, `[0182]`, `[0183]`
  - Quote anchor refs: `q-0006-1`, `q-0006-2`, `q-0130-1`, `q-0183-1`
- **stall-free-weight-double-buffering**: two independently addressed bitcells per memory cell let a write and a VMM run in parallel, hiding weight reloads behind compute. Description/aspect material; the claim block that covered adjacent ground (claims 11-19) is canceled in this publication.
  - Evidence paragraphs: `[0012]`, `[0015]`, `[0154]`, `[0230]`
  - Quote anchor refs: `q-0012-1`, `q-0015-1`, `q-0154-1`, `q-0154-2`
- **production-grade-silicon-depth**: the document specifies latch-level bitcell circuits, non-overlapping clock generation, setup-time relations, PVT timing checks, and scan/test modes reusing compute storage, i.e., engineering at tape-out depth rather than concept depth.
  - Evidence paragraphs: `[0118]`, `[0234]`, `[0262]`, `[0289]`
  - Quote anchor refs: `q-0118-1`, `q-0154-3`

## Claim scope map

Pending application: nothing is locked. All "sought-locks" below are what the claim text as published requires IF granted in this form (sought, not settled). Never present these as granted scope, and never attribute description preferences to the claims.

| Claim | Sought-locks (required by claim text as published) | Leaves open (description preference only) | Pins (approximate point limitations) |
|---|---|---|---|
| 1 (independent) | A computing system with a CIM macro having columns of computing units comprising: (a) a column cell generating a primitive product of an activation value and a weight value in A floating point format; (b) a functional block aligning mantissa bits of primitive products BY SHIFTING; (c) an adder tree outputting an accumulation value in an INTEGER format by adding the shifted mantissa bits | Which FP formats (FP4/FP6/FP8 are examples); block size 32; the mode decoding unit; dequantization to FP22; SRAM vs other memory; single vs double bitcells; DAZ subnormal handling; scan/test structures | none |
| 2 | + a shift calculation and select decoding unit determining a shift value per primitive product | how the shift value is computed (Emax subtraction is description: `[0200]`) | none |
| 3 | + a shift register whose bit count equals maximum exponent value plus mantissa bit count of the primitive product | the concrete widths (29b for FP8×FP6 is an example: `[0202]`) | none |
| 6-9 | + shifter realized as a logarithmic multiplexer tree, rows controlled by bits of the shift value | tree sizing (83 muxes etc. is an example: `[0206]`) | none |
| 10 | + a unit computing a "completement" (sic, typo preserved) and a sign of the shifted mantissa bits | fusing two's complement into the shift (`[0209]`) | none |
| 20 (independent) | Same triad as claim 1 plus the shift calculation and select decoding unit folded into the independent claim | as claim 1 | none |
| 21-23 | + column cell logic gates (incl. AND gates) outputting mantissa partial products; array of full adders producing mantissa bits | NOR-gate alternative; staggering; DAZ | none |
| 24 | + half adder for exponent bits, a full adder, and three multiplexers feeding the full adder (claim text as published is garbled: "selecting between zero and a corresponding one of the logic gates include AND gates") | the fourth multiplexer (`[0189]` / Aspect II) | none |
| 25-26 | + memory cells storing the weight value; a bitcell storing an exponent bit feeding the half adder | double bitcells, shared bitlines | none |
| 27 | + bitcell count in the column cell determined by a least common multiple of possible exponent-bit counts | LCM over mantissa bits (method aspect only) | none |
| 28 | + multiplexers selecting zero or a partial product into full adders based on a control signal | that the control signal comes from a mode decoding unit (description: `[0191]`) | none |
| 29 (independent) | Same triad as claim 1 (CIM macro configured to perform a VMM operation), with the functional block folded to comprise a shift register in the independent claim itself | as claim 1 | none |

Registry facts inside the document: this publication has THREE independent claims to the core triad — claim 1, claim 20 (triad + shift calculation and select decoding unit), and claim 29 (triad + shift register, CIM configured for VMM). Claims 11-19 read "(canceled)". The dual-bank parallel write+compute scheme and the scan-mode bitcell scheme appear only in the Summary/Aspects (`[0012]`, `[0013]`, Aspects CI-CXL), not in the pending claim set of this publication. Do not narrate them as claimed.

## Reference number table

No cleaned figure assets exist for this run (text-only); the Figures column cites the patent's FIG. numbers from the Brief Description `[0019]`-`[0058]` for the record only.

| Number | Label | Paragraphs | Figures |
|---|---|---|---|
| 100 | compute engine | `[0127]`, `[0142]`, `[0147]` | FIG. 1 |
| 101 | CIM macro | `[0128]`, `[0133]`, `[0135]` | FIG. 1, FIG. 2 |
| 102 | input buffer | `[0142]` | FIG. 1 |
| 104 | scale buffer | `[0143]`, `[0145]` | FIG. 1 |
| 106 | dequantization unit | `[0145]`, `[0147]` | FIG. 1 |
| 108 | output register | `[0145]` | FIG. 1 |
| 110 | mode decoding unit | `[0146]`, `[0147]`, `[0182]` | FIG. 1 |
| 220 | column cell | `[0135]`, `[0161]`, `[0162]` | FIG. 2, FIG. 3, FIGS. 7-8 |
| 222 | computing unit (column) | `[0135]`, `[0136]`, `[0139]` | FIG. 2 |
| 340 | column cell (row 0/col 0 example) | `[0140]` | FIG. 3 |
| 426 | adder tree | `[0137]`, `[0139]`, `[0207]` | FIG. 4, FIG. 38 |
| 830 | exponent handling block | `[0163]`, `[0167]`, `[0189]` | FIGS. 7-9, FIG. 28 |
| 832 | mantissa handling block | `[0163]`, `[0170]`, `[0171]`, `[0174]` | FIGS. 7-8, FIGS. 10-11 |
| 1440 / 1442 | first / second half adder (optimized exponent path) | `[0183]` | FIG. 14 |
| 1950 / 1952 | write multiplexers / storage units | `[0182]` | FIG. 19 |
| 2860 / 2862 / 2864 / 2866 | first-fourth exponent multiplexers | `[0189]` | FIG. 28 |
| 3574 / 3676 / 3778 | first / second / third shift registers | `[0202]`, `[0203]`, `[0204]` | FIGS. 35-37 |
| 3770 / 3772 | decoded shifter / its multiplexers | `[0204]`, `[0205]` | FIG. 37 |
| 3880 | functional block for mantissa alignment | `[0138]`, `[0205]` | FIG. 4, FIG. 38 |
| 3882 | shift calculation and select decoding unit | `[0138]`, `[0205]` | FIG. 4, FIG. 38 |
| 3884 | two's complement and sign unit | `[0138]`, `[0205]` | FIG. 4, FIG. 38 |
| 3970 / 3972 / 3974 / 3978 | logarithmic-tree shifter / muxes / registers | `[0206]` | FIG. 39 |
| 4190 | weight address decoder | `[0211]`, `[0221]`, `[0228]` | FIG. 41 |
| 4192 / 4194 / 4196 / 4198 | activation / weight / output / select latches | `[0210]`, `[0212]`, `[0213]`, `[0222]` | FIG. 41 |
| 4303 / 4503 / 4603 / 4703 / 4803 | double-bitcell memory cells (variants) | `[0217]`, `[0225]`, `[0260]`, `[0263]`, `[0282]` | FIGS. 43, 45-48 |
| 4505 / 4507 / 4509 | first / second weight select mux, weight output mux | `[0227]` | FIG. 45 |
| 4711 / 4713 | first / second scan multiplexers | `[0263]`, `[0268]` | FIG. 47 |

## Figure relationships

Text-only run: NO figure assets exist; nothing can be selected or rendered. The table below records the relationships stated in the Brief Description `[0019]`-`[0058]` purely so figure-selection.md can document the empty selection deliberately.

| Figure | Paired with | Relationship | Page (if known) | Cover candidate? | Phase map (sequences only) |
|---|---|---|---|---|---|
| FIG. 1 | FIG. 2 | system block diagram then CIM-macro detail | unknown | (no asset; would have been the natural cover) | |
| FIGS. 7-8 | each other | enlarged column-cell pair (single vs double bitcell) `[0025]` `[0162]` | unknown | | |
| FIGS. 34-39 | sequence | mantissa-alignment scheme progression `[0038]`-`[0040]` | unknown | | 34 flow / 35-36 shift steps / 37 decoded shifter / 38 physical block / 39 log-tree, per `[0198]`-`[0206]` |
| FIGS. 43-48 | sequence | double-bitcell design variants incl. scan `[0044]`-`[0047]` | unknown | | |
| FIG. 60 | (standalone) | Table 2, FP format mapping `[0057]` `[0184]` | unknown | | |

## Quote anchor table

| Quote ID | Paragraph | Verbatim text | Significance |
|---|---|---|---|
| q-0005-1 | `[0005]` | "Each conversion step requires additional scaling, rounding, and saturation logic, which adds area, power, and latency to already dense compute fabrics, and can introduce cumulative quantization errors that degrade numerical behavior over many layers." | prior-art-contrast |
| q-0005-2 | `[0005]` | "These operations can involve transforming activations and weights back and forth between different numeric domains" | prior-art-contrast |
| q-0005-3 | `[0005]` | "fixed conversion pipelines and format-specific data paths become increasingly difficult to adapt, limiting the flexibility of the hardware to support evolving models and deployment scenarios" | prior-art-contrast |
| q-0006-1 | `[0006]` | "natively supporting multiple, flexible numeric formats for activations and weights under the control of a mode decoding unit" | mechanism-critical |
| q-0006-2 | `[0006]` | "without requiring separate conversion pipelines or dedicated cores for each format" | prior-art-contrast |
| q-0011-1 | `[0011]` | "a column cell configured to generate a primitive product of an activation value and a weight value in a floating point format" | claim-supporting |
| q-0011-2 | `[0011]` | "a functional block configured to align mantissa bits of primitive products generated by column cells in the computing unit by shifting the mantissa bits" | claim-supporting |
| q-0011-3 | `[0011]` | "an adder tree configured to output an accumulation value of the primitive products in an integer format by adding the shifted mantissa bits" | claim-supporting |
| q-0012-1 | `[0012]` | "The CIM macro is further configured to perform, in parallel, a write operation to the first set of bitcells and the VMM operation in the second set of bitcells based on a weight select signal." | mechanism-critical |
| q-0015-1 | `[0015]` | "This arrangement can support efficient double-buffering of weights, minimize compute stalls during updates, and allow seamless switching between weight sets in high-throughput processing scenarios." | mechanism-critical |
| q-0104-1 | `[0104]` | "This alignment can ensure that all contributions are represented on a consistent scale, which may be crucial for maintaining accuracy when summing many floating-point products." | mechanism-critical |
| q-0118-1 | `[0118]` | "This dual-purpose design can allow the same memory cells to serve both compute storage and scan-test roles, improving test coverage and reusing circuitry." | mechanism-critical |
| q-0130-1 | `[0130]` | "The streaming operand provided to CIM macro 101 can be represented in FP8, FP6 or FP4 format and the stationary operand stored in CIM macro 101 can be represented in FP6 or FP4 format." | mechanism-critical |
| q-0131-1 | `[0131]` | "Reduced precision formats (i.e., reduced bit widths) can greatly increase computation speed and lower memory usage with minimal loss in accuracy, and thereby greatly improve the latency and throughput of a deep learning process in a neural network." | mechanism-critical |
| q-0133-1 | `[0133]` | "computations (e.g., VMM operations) can be directly performed within a memory array to minimize data movement" | mechanism-critical |
| q-0133-2 | `[0133]` | "This architecture is beneficial for accelerating AI workloads like deep learning by reducing the von Neumann bottleneck." | prior-art-contrast |
| q-0141-1 | `[0141]` | "Unlike traditional floating-point representations that allocate a dedicated scaling factor for each element, MX format employs a shared scaling factor across a block of elements." | prior-art-contrast |
| q-0145-1 | `[0145]` | "1×32 dot products in INT35 and INT5 formats can be provided by the CIM macro 101 to the dequantization unit 106, and can be converted to FP22 format by the dequantization unit 106" | quantitative |
| q-0147-1 | `[0147]` | "the CIM macro 101 operates in a pipelined fashion, returning a VMM product (i.e., a vector of dot products) every cycle" | quantitative |
| q-0154-1 | `[0154]` | "allowing concurrent loading of the next matrix of weight values while the previous weight values are still in use for the VMM computation" | mechanism-critical |
| q-0154-2 | `[0154]` | "a single set of weight values may be used for 256 VMM operations before a new set of weight values is needed" | quantitative |
| q-0154-3 | `[0154]` | "In some embodiments, 100% utilization of the compute engine 100 may be possible." | quantitative |
| q-0183-1 | `[0183]` | "64×64 number of half adders and full adders can be saved" | quantitative |
| q-0199-1 | `[0199]` | "For multiplication of FP8 (1-4-3)×FP6 (1-3-2), the maximum exponent value E.sub.max of the resulting primitive product is 22, which can be represented by a 5-bit integer INT5(22)." | quantitative |

> Note: the patent labels floating-point formats as FPn (sign-mantissa-exponent), so "FP8 (1-4-3)" means 1 sign, 4 mantissa, 3 exponent bits `[0132]`. This is NOT the OCP MX "E4M3" naming order; do not equate them. Claim 10 contains the typo "completement" and claim 24's final clause is garbled in the published text; both preserved verbatim wherever quoted.

## Timeline

- **Filing date**: 2025-11-21 (non-provisional); provisional priority 2024-11-22
- **Publication date**: 2026-05-28
- **Examination period**: 188 days (filing to publication; publication falls at the standard 18-month mark from the 2024-11-22 provisional priority date)
- **Prior-art chronology**:
  | Citation | Filing date | Publication date | Days relative to subject filing |
  |---|---|---|---|
  | (none cited in the document text as provided) | | | |

## Prior-art references + differentiation

The publication text as provided cites no specific prior-art documents. Differentiation is argued against characterized conventional practice, not named references:

- **Conversion-pipeline accelerators** (characterized at `[0005]`): fixed per-format datapaths with repeated domain conversions; this design claims one align-then-integer-accumulate path and describes (but does not claim here) mode-controlled format agility `[0006]`.
- **Von Neumann accelerator organization** (characterized at `[0133]`): data shuttled between memory and arithmetic cores; the CIM macro computes within the memory array `[0133]`.
- **Per-element-scaled floating point** (characterized at `[0141]`): traditional FP carries one scale per element; the macro operates on MX-style blocks with a shared scaling factor `[0141]`. External context: the MX block-format concept is an open industry standard since 2023 (OCP MX v1.0; see fact-check-log) — the differentiation available to this document is the claimed circuit structure, not the data format.

## 유리한 효과 + 정량 데이터

The macro keeps the whole accumulation in the integer domain after a single mantissa alignment, so the expensive part of low-precision floating-point matrix math runs on synthesizable integer adders, and format changes are absorbed by control signals rather than new datapaths `[0006]` `[0011]`. The pipelined engine returns a full vector of dot products every cycle `[0147]`, the optimized exponent path saves 64×64 half/full adders for the 32×32 example array `[0183]`, and double-buffered weights let loading overlap compute toward full utilization `[0154]`.

**Quotable spans:**
- `[0006]`: "without requiring separate conversion pipelines or dedicated cores for each format"
- `[0131]`: "Reduced precision formats (i.e., reduced bit widths) can greatly increase computation speed and lower memory usage with minimal loss in accuracy, and thereby greatly improve the latency and throughput of a deep learning process in a neural network."
- `[0147]`: "the CIM macro 101 operates in a pipelined fashion, returning a VMM product (i.e., a vector of dot products) every cycle"
- `[0154]`: "In some embodiments, 100% utilization of the compute engine 100 may be possible."
- `[0183]`: "64×64 number of half adders and full adders can be saved"

| Metric | Value | Paragraph |
|---|---|---|
| Supported streaming-operand formats | FP8 / FP6 / FP4 | `[0130]` |
| Supported stationary-operand formats | FP6 / FP4 | `[0130]` |
| Arithmetic modes (Table 1) | 8 | `[0131]` (Table 1) |
| Block size (MXFP) | 32 elements | `[0141]` |
| Macro output per column | INT35 + INT5 | `[0145]` |
| Dequantized output format | FP22 (1-8-13) | `[0145]` (Table 1) |
| Throughput | one VMM product (vector of dot products) per cycle | `[0147]` |
| Max exponent, FP8×FP6 primitive product | 22 (INT5-representable) | `[0199]` |
| Adders saved by optimized exponent path (32×32 array) | 64×64 half + full adders | `[0183]` |
| Weight reuse per load (example) | 256 VMM operations | `[0154]` |
| Claimed utilization potential | 100% (some embodiments) | `[0154]` |
