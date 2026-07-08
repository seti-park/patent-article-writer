# Invention Summary

## Metadata

- **Patent ID**: US 2024/0378175 A1 (PENDING APPLICATION — publication of application US 18/195,769; no enforceable claims exist)
- **Title**: Multi-Chip Systolic Arrays
- **Filing date**: 2023-05-10
- **Publication date**: 2024-11-14
- **Inventors**: Gavin Uberti (Kirkland, WA), Christopher Zhu (West Roxbury, MA) — both Etched co-founders
- **Classification**: Int. Cl. G06F 15/80, G06F 17/16; CPC G06F 15/8046, G06F 17/16
- **Assignee**: Etched.ai, Inc. (Menlo Park, CA) — applicant of record
- **Prosecution status (external registry, evidence_level: registry-extract)**: pending; examination continuing after a final rejection (mailed 2025-10-23) and a request for continued examination (docketed 2026-04-24); a third non-final office action issuing as of 2026-05. All claim scope below is SOUGHT, not locked.

## 발명 명칭 / 기술분야

Essay-ready phrasing: stitching many chips into one giant math array, and wiring memory
straight into its columns with no switch in between. Technical field: forming large systolic
arrays from multiple chips (ICs) containing smaller systolic arrays `[0001]`, aimed at AI
workloads (transformer models) where matrix multiplications dominate `[0003]`, with express
extension to cryptography, DNA/protein sequencing, and signal processing `[0019]`.

## 종래 문제 / 과제

The background names two ceilings. First, compute: systolic arrays are the efficient way to
do the matrix multiplications that dominate AI hardware, but achievable FLOPs scale with
array size, and single-chip arrays are capped by current IC design — the document puts the
industry's floating-point ceiling at about 128×128 per chip `[0003]`, `[0018]`. Second,
memory: even if one chip could carry enough compute, it cannot reasonably interface with the
hundreds of gigabytes of parameters a large model needs `[0018]`. A third, quieter problem
sits in the memory path itself: HBM channels cannot talk to each other, so conventional
designs interpose a switch or crossbar between memory and compute so that any consumer can
reach any channel `[0043]` — a layer this filing exists to delete.

**Quotable spans:**
- `[0003]`: "However, the number of floating-point operations per second (FLOPs) that can be achieved is often dependent on the size of the systolic array, which is limited in current IC design."
- `[0018]`: "Currently, most chips have, at most, floating point systolic arrays with a size of 128×128."
- `[0018]`: "One of which, notably, is that it is unreasonable to expect a single chip to interface with 100s of GB of memory used to store parameters and intermediate computation values."
- `[0043]`: "a switch (or some kind of switching element such as a crossbar) is typically used so that the device can access the entire memory of the HBM"

## 청구항 분석 — 4-layer core mechanism

### Layer 1 — What (one sentence)

A package of many identical chips whose small on-chip systolic arrays are wired together
into one large combined systolic array that the host sees as a single device, with model
weights streamed in from memory chips at the top — and, in the claim-39 family, memory
channels hardwired directly to array columns with no switching element at all.

### Layer 2 — How (mechanism)

1. Build many identical ICs (215), each carrying a local systolic array (220) of DPUs (105) that multiply-accumulate every clock cycle `[0020]`, `[0023]`, `[0028]`.
2. Arrange the ICs in a grid on an interposer, or stack them, and join neighbors with chip-to-chip connections — bidirectional horizontal links (230) and top-to-bottom vertical links (225), e.g. UCIe `[0029]`, `[0030]`, `[0031]`.
3. Operate the joined local arrays as one combined systolic array (250/350/450/650): the host (205) loads data over PCIe (240) and sees one large array; the array takes no instructions at runtime, executing a preset loop `[0025]`, `[0027]`, `[0028]`.
4. Feed AI model weights (110) from memory chips (210/305) into the top row of ICs; weights are constants that flow down the columns and are reused across rows, while tensors (115) flow left to right and results feed back right to left `[0021]`, `[0032]`, `[0035]`, `[0039]`.
5. For constant-weight workloads, delete the switching layer: hardwire each independent channel (510) of a separate memory device (505) to a particular column (515) of the array via wires (520) — no switch, at the cost that each column can read only its own channel `[0043]`, `[0044]`, `[0045]`.
6. Put auxiliary circuitry (605) on each IC (615) beside the local array for work the array cannot do efficiently — self-attention needs data from previous tokens — and give that circuitry private local memory chips (610) the systolic arrays never touch `[0047]`, `[0048]`, `[0051]`.
7. Pipeline a transformer layer through the combined array in batches, pre-feeding the next computation before the previous completes; stall only where layer normalization forces it, keeping utilization at 98% or greater `[0055]`, `[0056]`, `[0057]`.

**Key components**: ICs (215/615), local systolic arrays (220), DPUs (105), horizontal connections (230), vertical connections (225), combined systolic array (250/350/450/650), host (205) + PCIe (240), weight-feed memory chips (210/305), hardwired memory chips (505) with channels (510), array columns (515), wires (520), auxiliary circuitry (605), local memory chips (610)

### Layer 3 — Why novel

- **Relative to prior art**: The document cites no references in its text; it differentiates against practice. Instead of waiting for a bigger monolithic chip (the 128×128-per-chip world of `[0018]`), it composes one logical array from many chips `[0019]`, `[0028]`; instead of the switch/crossbar every conventional HBM consumer needs `[0043]`, it dedicates memory channels to array columns because weights are constant and always go to the same columns `[0044]`, `[0045]`.
- **Industry practice contrast**: Accelerators normally keep memory access general — any compute block can reach any memory — paying for that generality in switching layers, space, and power. This filing trades the generality away (a column can only read its own channel `[0045]`) and buys back space and power, which is only a sane trade for a single-workload chip whose weights never move. The architecture is workload-shaped: the same document also gives the array no runtime instruction stream `[0027]`.

### Layer 4 — Innovation angles

- **no-switch-memory-channels**: memory channels hardwired to array columns, no switching element (the claim-39 family; the memory half of the later CSM story)
  - Evidence paragraphs: `[0016]`, `[0043]`, `[0044]`, `[0045]`
  - Quote anchor refs: `q-0016-1`, `q-0043-2`, `q-0044-1`, `q-0045-2`
- **one-array-from-many-chips**: many identical chips fused into one combined systolic array the host sees as a single large array; the array is also splittable into simultaneous computations
  - Evidence paragraphs: `[0013]`, `[0019]`, `[0024]`, `[0028]`, `[0038]`
  - Quote anchor refs: `q-0013-1`, `q-0019-1`, `q-0024-1`, `q-0028-1`
- **transformer-asic-division-of-labor**: auxiliary circuitry with private local memory handles self-attention; the arrays never touch that memory; the array itself runs a preset loop with no runtime instructions
  - Evidence paragraphs: `[0027]`, `[0047]`, `[0048]`, `[0051]`
  - Quote anchor refs: `q-0027-1`, `q-0047-1`, `q-0047-2`, `q-0051-1`
- **preset-loop-pipelining**: batching, pre-feeding the next computation, and the layer-normalization stall; 98%+ utilization (NOTE: description-only — no claim covers FIG. 7 pipelining, batching, or the utilization figure)
  - Evidence paragraphs: `[0053]`, `[0055]`, `[0056]`, `[0057]`
  - Quote anchor refs: `q-0053-1`, `q-0055-1`, `q-0056-1`, `q-0057-2`

## Claim scope map

PENDING-APPLICATION EDITION: there is NO locked class anywhere in this map. Every entry is
**sought** — what the application claims as drafted, which may narrow or die before grant
(final rejection 2025-10-23; RCE 2026-04-24; third non-final action issuing as of 2026-05,
evidence_level: registry-extract). Use application-era language only: "the application
claims / Etched is seeking / as drafted." Never "the patent locks/requires/fences."

Claims 1-42; independents are 1, 15, 26, 39.

| Claim | Sought (required by the claim text as drafted) | Leaves open (description preference only) | Pins (approximate point limitations) | Prosecution-risk note |
|---|---|---|---|---|
| 1 (indep.) | Package with a plurality of ICs, each with a local systolic array of DPUs; chip-to-chip connections joining each local array to at least one other to form a larger, combined systolic array | Grid layout (that is claim 26's add), interposer vs stack (deps 9/10; `[0031]`), UCIe (`[0030]` example only), link directionality (deps 3/4), memory presence (`[0037]`: memory chips may not be needed) | none — no "about X" point limitation in any claim | Broadest independent; the multi-chip-array concept sits in a crowded examiner-cited field (8 refs, incl. Intel/IBM/Rambus/ETRI assignees) and has already been through a final rejection — the breadth is the part most likely to shrink |
| 5 (dep. of 3) | Plurality of memory chips, at least one connected to each top-row IC | How many chips per IC (`[0035]`, `[0040]`) | none | Rides on claims 1-3 surviving |
| 6 (dep. of 5) | Memory chips store weight data for matrix multiplication for an AI model | Weight constancy (`[0035]` says weights are constant — description, not claim text) | none | AI-weight storage on top-row memory is TPU-adjacent, weight-stationary territory |
| 7 (dep. of 5) | Memory chips are HBMs, hardwired to respective columns in the local systolic arrays without any switching element | Which columns, how many channels per column | none | The memory-half echo inside the claim-1 family; same art risk as claim 39 |
| 11 (dep. of 1) | Each IC has auxiliary circuitry separate from the local array; local memory chips coupled to that auxiliary circuitry | What the auxiliary circuitry is (`[0050]`: could be another systolic array, a micro-processor, an ALU) | none | Division-of-labor claim; functional breadth of "auxiliary circuitry" invites art |
| 12 (dep. of 11) | Auxiliary circuitry performs self-attention operations using previous-token data stored in the local memory chips, as part of an AI model | Which attention algorithm (`[0048]`: many types) | none | The transformer-specific claim; most workload-shaped of the family |
| 13 (dep. of 12) | The local systolic arrays do not communicate with the local memory chips | `[0051]` flags the opposite as an alternative embodiment (arrays MAY use them as scratchpad) — the description deliberately keeps what the claim closes | none | A negative limitation; narrow but distinctive |
| 15 (indep.) | AI accelerator: ICs with local arrays; connections forming combined array; plurality of memory chips storing weights for matrix multiplications as part of an AI model, coupled to the ICs forming a top row | HBM type (dep. 19), hardwiring (dep. 19), directionality (deps 16-18) | none | Weight-streaming-from-top-row is the classic weight-stationary pattern; expect the examiner to read TPU-style art directly onto it |
| 19 (dep. of 15) | Memory chips are HBMs hardwired to respective columns without any switching element | As claim 7 | none | As claim 7 |
| 26 (indep.) | Package with plurality of ICs in a grid-like pattern, local arrays connected to form combined array | Connection mechanics (deps 27-29 add them; claim 26 itself does not recite chip-to-chip connections as an element) | none | Even sparser than claim 1; "grid-like pattern" is the only structural add — high rejection exposure |
| 32 (dep. of 30) | HBMs hardwired to respective columns without any switching element | As claim 7 | none | As claim 7 |
| 39 (indep.) | Package: an IC with a systolic array of DPUs; a separate memory device with a plurality of channels; EACH channel hardwired to respective one or more columns WITHOUT ANY switching element | Memory type (dep. 41 adds HBM), purpose (dep. 40 adds weight storage), device count (dep. 42 adds plurality) | none | The no-switch memory claim standing alone — it does NOT require multi-chip; the negative "without any switching element" limitation is the distinctive fence, and the most architecture-specific of the four independents |
| 40 (dep. of 39) | Memory device stores weight data for AI matrix multiplication | — | none | Rides on 39 |
| 41 (dep. of 39) | Memory device is an HBM | — | none | Rides on 39 |
| 42 (dep. of 39) | Plurality of memory devices, each with channels hardwired to columns without any switching element (claim text reads "hardwire" — sic) | — | none | Rides on 39; note the claim's own typo "is hardwire to" preserved verbatim |

Map-wide notes:
- **No pinned point limitations exist.** No claim recites an "about X" value. The
  description's "approximately 100-10000 rows and 100-10000 columns" `[0033]` is
  description preference, never claim content.
- **Description-only material (in NO claim):** the preset instruction loop `[0027]`, UCIe
  `[0030]`, 32 GT/s / 16-64 lanes `[0030]`, hundreds-of-GBs / tens-of-GBs link asymmetry
  `[0032]`, 128×128 industry ceiling `[0018]`, 1 TB/s per top-row IC `[0040]`, all of FIG. 7
  (batching, three passes, GeLU pre-feed, layer-norm stall, 98% utilization `[0053]`-`[0057]`),
  and the add-rows-without-adding-memory advantage `[0039]`. Narrate these as the
  description's, on description anchors.

## Reference number table

| Number | Label | Paragraphs | Figures |
|---|---|---|---|
| 100 | Systolic array (logical) | `[0020]`-`[0024]`, `[0028]` | FIG. 1 |
| 105 | Data processing units (DPUs) | `[0020]`-`[0024]` | FIG. 1 |
| 110 | Model weights (top input) | `[0021]`, `[0022]` | FIG. 1 |
| 115 | Previous tensor (left input) | `[0021]`, `[0022]` | FIG. 1 |
| 200 | System (host + package) | `[0025]` | FIG. 2 |
| 201 | Package | `[0025]`-`[0031]`, `[0034]`, `[0038]` | FIG. 2 |
| 205 | Host | `[0025]`-`[0027]`, `[0035]`, `[0037]` | FIG. 2 |
| 210 | Memory chips (top-row weight feed) | `[0034]`-`[0037]`, `[0046]`, `[0049]` | FIG. 2, FIG. 6 |
| 215 | ICs (chips containing local arrays) | `[0027]`-`[0038]`, `[0040]`-`[0044]` | FIG. 2, FIG. 3, FIG. 4, FIG. 5 |
| 220 | Local systolic arrays | `[0028]`-`[0035]`, `[0038]`, `[0043]`-`[0045]`, `[0051]` | FIG. 2, FIG. 3, FIG. 4, FIG. 5, FIG. 6 |
| 225 | Vertical chip-to-chip connections (unidirectional) | `[0029]`-`[0032]`, `[0034]`, `[0035]`, `[0046]`, `[0052]` | FIG. 2, FIG. 3, FIG. 6 |
| 230 | Horizontal chip-to-chip connections (bidirectional) | `[0029]`-`[0032]`, `[0046]`, `[0052]` | FIG. 2, FIG. 3, FIG. 6 |
| 240 | PCIe connections (host link) | `[0026]`, `[0027]`, `[0037]` | FIG. 2 |
| 250 | Combined systolic array | `[0025]`-`[0038]` | FIG. 2 |
| 301 | Package (square-grid variant) | `[0039]` | FIG. 3 |
| 305 | Memory chips (multiple per top-row IC) | `[0039]`, `[0040]` | FIG. 3, FIG. 4 |
| 350 | Combined systolic array (equal rows/columns) | `[0039]`, `[0040]` | FIG. 3 |
| 401 | Package (unequal-grid variant) | `[0041]` | FIG. 4 |
| 450 | Combined systolic array (unequal rows/columns) | `[0041]`, `[0042]` | FIG. 4 |
| 505 | Memory chips (hardwired, with channels) | `[0043]`-`[0045]` | FIG. 5 |
| 510 | Channels (independent memory channels) | `[0043]`-`[0045]` | FIG. 5 |
| 515 | Columns of DPUs in the local array | `[0044]`, `[0045]` | FIG. 5 |
| 520 | Wires (channel-to-column hardwiring) | `[0043]`, `[0044]` | FIG. 5 |
| 605 | Auxiliary circuitry (inside each IC 615) | `[0047]`-`[0052]`, `[0054]` | FIG. 6 |
| 610 | Local memory chips (private to auxiliary circuitry) | `[0048]`-`[0051]` | FIG. 6 |
| 615 | ICs (variant with auxiliary circuitry) | `[0046]`-`[0052]` | FIG. 6 |
| 650 | Combined systolic array (FIG. 6 variant) | `[0046]`, `[0047]` | FIG. 6 |

> Note — figures-manifest defect (Phase 0): the manifest line for FIG. 6 swaps 605/610,
> describing "local memory chips 605A-605D built into each IC block". Per `[0047]`-`[0051]`
> and the image itself: **605 = auxiliary circuitry (inside the ICs 615); 610 = local memory
> chips (the small boxes outside each IC)**. Trust the spec and the image, not the manifest
> line. Caption work in Phase 2 must use the corrected labels above.

## Figure relationships

| Figure | Paired with | Relationship | Page (if known) | Cover candidate? | Phase map (sequences only) |
|---|---|---|---|---|---|
| FIG. 1 | FIG. 2 | logical/physical pair — `[0028]`: "a logical view of the array 250 can be represented by the array 100 in FIG. 1" | sheet 1 of 7 | | |
| FIG. 2 | FIG. 1 | physical layout whose logical view is FIG. 1; standalone otherwise | sheet 2 of 7 | | |
| FIG. 3 | FIG. 4 | variant pair — equal vs unequal rows/columns of ICs (`[0041]`) | sheets 3-4 of 7 | | |
| FIG. 4 | FIG. 3 | variant pair (see above) | sheet 4 of 7 | | |
| FIG. 5 | (standalone) | — | sheet 5 of 7 | **yes** — the most literal picture of the claim-39 core step (channels 510 hardwired by wires 520 to columns 515, no switch), and the cleanest figure at card scale | |
| FIG. 6 | (standalone) | — (extends FIG. 2's package with auxiliary circuitry) | sheet 6 of 7 | | |
| FIG. 7 | (standalone) | single timing chart, not a multi-panel sequence | sheet 7 of 7 | | (not a sequence; no phase map) |

## Quote anchor table

| Quote ID | Paragraph | Verbatim text | Significance |
|---|---|---|---|
| q-0002-1 | `[0002]` | "Systolic arrays are hardware structures built for fast and efficient operation of algorithms that typically perform the same task with different data at different times." | mechanism-critical |
| q-0003-1 | `[0003]` | "For many artificial intelligence (AI) applications (e.g., transformer models), matrix multiplications dominate the operations that must be performed in hardware." | mechanism-critical |
| q-0003-2 | `[0003]` | "However, the number of floating-point operations per second (FLOPs) that can be achieved is often dependent on the size of the systolic array, which is limited in current IC design." | prior-art-contrast |
| q-0013-1 | `[0013]` | "Embodiments presented in this disclosure is a package that includes a plurality of integrated circuits (ICs), each comprising a local systolic array of data processing units (DPUs) and chip-to-chip connections configured to connect the local systolic array in each of the plurality of ICs to at least one other local systolic array in another one of the plurality of ICs to form a larger, combined systolic array." | claim-supporting |
| q-0014-1 | `[0014]` | "Another embodiment in this disclosure is an AI accelerator that includes a plurality of integrated circuits (ICs) each comprising a local systolic array of DPUs; chip-to-chip connections configured to connect the local systolic arrays to form a larger, combined systolic array; and a plurality of memory chips configured to store weights for performing matrix multiplications in the combined systolic array as part of an AI model, the plurality of memory chips coupled to the plurality of ICs forming a top row of the combined systolic array." | claim-supporting |
| q-0016-1 | `[0016]` | "Another embodiment in this disclosure is a package that includes an IC comprising a systolic array of data processing units (DPUs) and a separate memory device comprising a plurality of channels where each of the plurality of channels is hardwired to respective one or more columns in the systolic array without any switching element." | claim-supporting |
| q-0018-1 | `[0018]` | "Currently, most chips have, at most, floating point systolic arrays with a size of 128×128." | quantitative |
| q-0018-2 | `[0018]` | "One of which, notably, is that it is unreasonable to expect a single chip to interface with 100s of GB of memory used to store parameters and intermediate computation values." | prior-art-contrast |
| q-0018-3 | `[0018]` | "Large systolic arrays are also efficient with respect to input/output bandwidth." | mechanism-critical |
| q-0019-1 | `[0019]` | "Instead, the embodiments herein adapt a multi-chip approach where multiple local systolic arrays on multiple chips (or ICs) are connected using high-speed chip-to-chip connections to form a larger, combined systolic array." | mechanism-critical |
| q-0021-1 | `[0021]` | "The topmost row of DPUs 105 receive AI model weights 110, which may be constants." | mechanism-critical |
| q-0024-1 | `[0024]` | "In this manner, the systolic array 100 can perform different operations for a single layer in an AI model, or perform operations for different layers in the AI model, simultaneously." | mechanism-critical |
| q-0027-1 | `[0027]` | "the systolic array 250 does not take instructions at runtime, and only executes instructions in a preset loop" | mechanism-critical |
| q-0028-1 | `[0028]` | "from the perspective of the host 205, the systolic array 250 appears to be one large array, even though it is physically made up of smaller local systolic arrays 220 distributed on separate ICs 215" | mechanism-critical |
| q-0028-2 | `[0028]` | "In one embodiment, the ICs 215 are all identical." | mechanism-critical |
| q-0029-1 | `[0029]` | "the vertical connections 225 are unidirectional which permits data to flow only from top to bottom (not from bottom to top)" | mechanism-critical |
| q-0030-1 | `[0030]` | "Universal Chiplet Interconnect Express (UCIe) can be used to form the chip-to-chip (or die-to-die) connections" | mechanism-critical |
| q-0030-2 | `[0030]` | "a physical layer that supports up to 32 GT/s with 16 to 64 lanes" | quantitative |
| q-0031-1 | `[0031]` | "However, in another embodiment, the ICs 215 may be formed in a stack, rather than being disposed side-by-side as shown in FIG. 2." | mechanism-critical |
| q-0032-1 | `[0032]` | "As a non-limiting example, the left-to-right data paths in the horizontal connections 230 may support data streams of hundreds of GBs" | quantitative |
| q-0035-1 | `[0035]` | "If the systolic array 250 is used in an AI accelerator application, the memory chips 210 can store the weights for the AI model being used at runtime." | mechanism-critical |
| q-0035-2 | `[0035]` | "In one embodiment, the weights are constant when executing the combined systolic array 250." | mechanism-critical |
| q-0037-1 | `[0037]` | "Further, in some embodiments, the memory chips 210 may not be needed." | claim-supporting |
| q-0038-1 | `[0038]` | "a single row of four ICs 215 would form a 100×400 combined systolic array 250 while a single column of four ICs 215 would form a 400×100 combined systolic array 250" | quantitative |
| q-0039-1 | `[0039]` | "Advantageously, adding more rows of ICs 215 increases the compute power of the systolic array 350, without having to add more memory chips 305 at the top to feed in data in the vertical direction, since data fed from the memory chips 305 is reused across the rows within the combined systolic array 350." | mechanism-critical |
| q-0040-1 | `[0040]` | "using multiple memory chips 305 can enable the memory chips 305 to transmit more than 1 TB/s of data to each of the ICs" | quantitative |
| q-0043-1 | `[0043]` | "For example, in HBM, the different channels 510 cannot communicate with each other." | mechanism-critical |
| q-0043-2 | `[0043]` | "a switch (or some kind of switching element such as a crossbar) is typically used so that the device can access the entire memory of the HBM" | prior-art-contrast |
| q-0044-1 | `[0044]` | "However, for some accelerator applications such as AI applications where the weight data does not change, the independent channels 510 can be directly wired (or hardwired) to a particular column 515 in the local systolic array 220 of the IC 215." | claim-supporting |
| q-0044-2 | `[0044]` | "This systolic array column could extend through all the ICs 215 in a column." | mechanism-critical |
| q-0045-1 | `[0045]` | "However, since the memory chips 505 may be used to store constant weight data that is always provided to the same columns 515, hardwiring the memory chips 505 to the columns 515 is permissible." | mechanism-critical |
| q-0045-2 | `[0045]` | "This avoids having to add a switching element between the local systolic array 220and the memory chips 505, which can save space and power." | claim-supporting |
| q-0047-1 | `[0047]` | "for AI accelerators, self-attention operations use data computed from previous tokens, which means such data should be saved" | mechanism-critical |
| q-0047-2 | `[0047]` | "Most of the parts of a transformer AI model do not use data from previous tokens, and thus, can be calculated efficiently using the combined systolic array 650 which may consider each token in isolation from the other tokens being computed on." | mechanism-critical |
| q-0048-1 | `[0048]` | "the auxiliary circuitry 605 in each IC 615 is coupled to at least one local memory chip 610 (e.g., one or more HBMs)" | claim-supporting |
| q-0051-1 | `[0051]` | "In this embodiment, the local systolic arrays 220 do not have access to the local memory chips 610." | claim-supporting |
| q-0051-2 | `[0051]` | "in this example, only the auxiliary circuitry 605 can access the local memory chips 610" | mechanism-critical |
| q-0053-1 | `[0053]` | "FIG. 7 illustrates the contents of one row of the combined systolic array while computing the output for one layer of the AI model" | mechanism-critical |
| q-0055-1 | `[0055]` | "For example, to calculate the query values (e.g., perform the "Attention: queries" computation) used in the attention mechanism of transformer AI models, the data passes through the systolic array three times." | quantitative |
| q-0056-1 | `[0056]` | "To achieve 100% efficiency (or close to 100% efficiency), the inputs for the subsequent computation are fed into the systolic array before the previous computation completes." | mechanism-critical |
| q-0056-2 | `[0056]` | "To prevent a stall, this post-processing can be performed on the values that have already been generated (e.g., compute a GeLU for every value) and fed back into the input to start a new computation while the previous computation is still occurring." | mechanism-critical |
| q-0057-1 | `[0057]` | "This means the systolic array may stall during layer normalization." | mechanism-critical |
| q-0057-2 | `[0057]` | "the stalled time may be small relative to the computation time and still result in a 98% or greater utilization of the systolic array" | quantitative |

> Note — preserved source typos (verbatim discipline): the USPTO full text runs several
> reference numerals into the following word. These are PRESERVED in the spans above and
> must never be "fixed" when quoting: `[0045]` "array 220and the memory chips" (q-0045-2).
> Claim 42's "is hardwire to" is likewise the claim's own text. Where a run-on numeral would
> disfigure an essay quote, cite a clean substring of the recorded span instead of editing
> it (all essay quotes must remain substrings of these rows). The `[0018]` FLOPs formula
> contains the artifact "2N{circumflex over ( )} 2" (USPTO rendering of 2N^2); it is left
> out of the anchors — use the Metric table's value and paraphrase the scaling in prose.

## Timeline

- **Filing date**: 2023-05-10 (application US 18/195,769 — Etched's earliest patent filing; both co-founders are the inventors)
- **Publication date**: 2024-11-14 (US 2024/0378175 A1)
- **Examination period**: 553 days filing-to-publication; prosecution ongoing as of the 2026-05 record (pending; non-final actions 2024-11 and 2025-07; final rejection mailed 2025-10-23; RCE docketed 2026-04-24; third non-final action issuing as of 2026-05 — external registry facts, evidence_level: registry-extract)
- **Prior-art chronology**:
  | Citation | Filing date | Publication date | Days relative to subject filing |
  |---|---|---|---|
  | (none cited in the document text) | — | — | — |

  The specification cites no prior-art references. The examination record carries 8 unique
  references, all examiner-cited (multi-node ML acceleration, hybrid parallelism, NN
  accelerator architectures; assignees include Intel, IBM, Rambus, ETRI) — external fact,
  evidence_level: registry-extract; see fact-check-log `examiner-art-8refs`.

## Prior-art references + differentiation

- **In-document**: none. The Background differentiates against current practice, not named
  references: single-chip array size "limited in current IC design" `[0003]`, the 128×128
  per-chip ceiling and the 100s-of-GB memory-interface premise `[0018]`, and the
  switch/crossbar "typically used" between an HBM and its consumers `[0043]`.
- **Examiner-cited (external, registry-extract)**: 8 unique references, all examiner-cited,
  in multi-node ML acceleration, hybrid parallelism, and NN accelerator architectures
  (assignees include Intel Corporation, IBM, Rambus Inc., ETRI). A crowded field: the
  differentiation the applicant must win in prosecution is against this art, and it has
  already lost one round (final rejection 2025-10-23, now under RCE).
- **Industry baseline (external, for Axis 4)**: Google's TPU MXU — a 128×128 systolic array
  through v5p-era generations, 256×256 from Trillium (v6e) — is the concrete instance of the
  `[0018]` per-chip-array world; conventional accelerator memory paths keep a switching
  layer so any consumer reaches any channel, the exact layer `[0043]` describes and claim 39
  deletes. See fact-check-log `tpu-mxu-128x128`.

## 유리한 효과 + 정량 데이터

Three effects carry the document. Scale: joining chips yields one large array (a 100×400 or
400×100 array from four 100×100 chips `[0038]`), and the host sees a single device `[0028]`.
Memory economy: adding rows of ICs adds compute without adding memory chips, because weight
data is reused down the rows `[0039]`; and for constant-weight workloads the switching layer
between memory and array can be deleted outright, saving space and power `[0045]`. And
utilization: pipelining batches back-to-back keeps the array at or above 98% busy even with
layer-normalization stalls `[0056]`, `[0057]`.

**Quotable spans:**
- `[0028]`: "from the perspective of the host 205, the systolic array 250 appears to be one large array, even though it is physically made up of smaller local systolic arrays 220 distributed on separate ICs 215"
- `[0039]`: "Advantageously, adding more rows of ICs 215 increases the compute power of the systolic array 350, without having to add more memory chips 305 at the top to feed in data in the vertical direction, since data fed from the memory chips 305 is reused across the rows within the combined systolic array 350."
- `[0045]`: "This avoids having to add a switching element between the local systolic array 220and the memory chips 505, which can save space and power."
- `[0056]`: "To achieve 100% efficiency (or close to 100% efficiency), the inputs for the subsequent computation are fed into the systolic array before the previous computation completes."
- `[0057]`: "the stalled time may be small relative to the computation time and still result in a 98% or greater utilization of the systolic array"

| Metric | Value | Paragraph |
|---|---|---|
| FLOPs per clock for an N×N array | 2N^2 FLOPs for 2N inputs per cycle (source renders the exponent as "{circumflex over ( )}") | `[0018]` |
| Industry per-chip array ceiling (applicant-stated) | ~128×128 floating-point | `[0018]` |
| Local array dimensions (description) | approximately 100-10000 rows × 100-10000 columns of DPUs | `[0033]` |
| Combined array from 4 chips of 100×100 | 100×400 (row) or 400×100 (column) | `[0038]` |
| UCIe physical layer (example interconnect) | up to 32 GT/s, 16 to 64 lanes | `[0030]` |
| Horizontal link asymmetry | left-to-right: hundreds of GBs; right-to-left: tens of GBs (or less) | `[0032]` |
| Weight bandwidth per top-row IC (multiple memory chips) | more than 1 TB/s | `[0040]` |
| Attention-queries computation | data passes through the array three times | `[0055]` |
| Utilization with layer-norm stalls | 98% or greater | `[0057]` |

All values are the description's own figures for embodiments (sought scope only; none of
these numbers appears in any claim).
