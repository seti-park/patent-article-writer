# Invention Summary

> **EDITION NOTE (controls all downstream language):** US 2024/0378175 A1 is a PENDING
> PATENT APPLICATION, not a grant. Every claim in this summary is SOUGHT, not locked —
> the claim set may narrow or die before grant. Application-era language only ("the
> application claims", "Etched is seeking", "as drafted"); never grant-era language
> ("the patent locks/requires/fences"); no enforceability language anywhere.

## Metadata

- **Patent ID**: US 2024/0378175 A1 (Application No. US 18/195,769) — PENDING APPLICATION
- **Title**: Multi-Chip Systolic Arrays
- **Filing date**: 2023-05-10 (Etched's earliest patent filing)
- **Publication date**: 2024-11-14
- **Inventors**: Gavin Uberti, Christopher Zhu (the two co-founders)
- **Classification**: Int. Cl. G06F 15/80; G06F 17/16 — CPC G06F 15/8046; G06F 17/16
- **Assignee**: Etched.ai, Inc. (Menlo Park, CA)
- **Prosecution status** (registry-extract, 2026-07-02 WIPS/DOCDB export): pending;
  examination continuing after a final rejection (mailed 2025-10-23) and a request for
  continued examination (docketed 2026-04-24); a third non-final office action issuing
  as of 2026-05. See fact-check-log `prosecution-record`.

## 발명 명칭 / 기술분야

Stitching many chips into one giant math engine: a package of identical ICs, each carrying
a small systolic array, wired chip-to-chip so they behave as a single larger, combined
systolic array — with memory channels hardwired straight into the array's columns, no
switch in between. Technical field: forming large systolic arrays from multiple chips
containing smaller systolic arrays, aimed primarily at AI (transformer-model) matrix
multiplication `[0001]` `[0003]`.

## 종래 문제 / 과제

Systolic arrays are the workhorse structure for the matrix multiplications that dominate
AI inference, but a systolic array's throughput scales with its size, and single-chip
arrays are capped by current IC design — the application puts the practical ceiling at
128×128 for most chips `[0003]` `[0018]`. Worse, the bottleneck is not only compute: a
transformer model's parameters run to hundreds of gigabytes, and no single chip can
realistically interface with that much memory `[0018]`. The background also notes that
accessing a full HBM normally requires a switching element (a crossbar), because a device
wired to one channel cannot reach memory assigned to another `[0043]` — a cost the
invention's memory-side design exists to delete.

**Quotable spans:**
- `[0003]`: "For many artificial intelligence (AI) applications (e.g., transformer models), matrix multiplications dominate the operations that must be performed in hardware."
- `[0003]`: "However, the number of floating-point operations per second (FLOPs) that can be achieved is often dependent on the size of the systolic array, which is limited in current IC design."
- `[0018]`: "Currently, most chips have, at most, floating point systolic arrays with a size of 128×128."
- `[0018]`: "it is unreasonable to expect a single chip to interface with 100s of GB of memory used to store parameters and intermediate computation values"

## 청구항 분석 — 4-layer core mechanism

### Layer 1 — What (one sentence)

The application claims (sought, not locked) a package in which multiple ICs — each holding
a local systolic array of data processing units — are joined by chip-to-chip connections
into one larger, combined systolic array, with memory channels hardwired to specific array
columns without any switching element.

### Layer 2 — How (mechanism)

1. Tile a package (201) with identical ICs (215), each containing a local systolic array
   (220) of DPUs (105) that each perform a multiply-accumulate every clock cycle.
2. Couple neighboring local arrays with horizontal chip-to-chip connections (230,
   bidirectional) and vertical chip-to-chip connections (225, unidirectional, top-to-bottom)
   so the tiles act as one combined systolic array (250) — to the host (205), it appears
   as one large array.
3. Stream AI model weights (110) from memory chips (210 / 305) into the top row of ICs;
   weights flow downward through the tiles while activations (previous tensor 115) flow
   left-to-right, entering from the host over PCIe connections (240); the array takes no
   runtime instructions, executing a preset loop.
4. Hardwire each independent memory channel (510) of an external memory chip (505) to a
   particular column (515) of the array via wires (520) — no switch or crossbar — because
   weight data is constant and always feeds the same columns.
5. Delegate operations that need token history (self-attention) to auxiliary circuitry
   (605) on each IC (615), backed by local memory chips (610) that the systolic arrays
   themselves never touch.
6. Pipeline successive operations (attention queries/keys/values, projection, MLP layers)
   through the combined array so a new computation starts before the previous one drains,
   keeping utilization at 98% or greater.

**Key components**: DPUs (105), model weights (110), previous tensor (115), package (201),
host (205), memory chips (210, 305, 505), ICs (215, 615), local systolic arrays (220),
vertical connections (225), horizontal connections (230), PCIe connections (240), combined
systolic arrays (250, 350, 450, 650), channels (510), columns (515), wires (520), auxiliary
circuitry (605), local memory chips (610)

### Layer 3 — Why novel

- **Relative to prior art**: The specification cites no prior-art documents; its stated
  contrast is with current IC practice — single-chip systolic arrays capped around 128×128
  `[0018]` and HBM access mediated by a switching element/crossbar `[0043]`. The
  application's answer is structural on both fronts: combine chip-level arrays into one
  logical array `[0019]`, and delete the memory switch by hardwiring channels to columns
  `[0044]` `[0045]`. (Examiner-cited art — 8 references in multi-node ML acceleration,
  hybrid parallelism, and NN accelerator architectures — is registry-external; see
  fact-check-log `examiner-cited-field`.)
- **Industry practice contrast**: Mainstream accelerators scale by networking discrete
  chips through switched fabrics and software coordination, and reach memory through
  shared controllers/switches; this application scales by making the chips physically
  compose into one array with a fixed, preset dataflow (`[0027]` — no runtime
  instructions) and memory permanently bonded to the columns it feeds.

### Layer 4 — Innovation angles

- **combined-array-scaling**: many chips presented to the host as one large systolic array
  — the "splittable math arrays" idea of the company's later public thread, in its origin
  form
  - Evidence paragraphs: `[0013]`, `[0019]`, `[0028]`
  - Quote anchor refs: `q-0013-1`, `q-0019-1`, `q-0028-1`
- **switchless-memory-hardwiring**: memory channels hardwired to specific array columns
  "without any switching element" (claim 39 family; claims 7/8 put HBMs on the same
  hardwiring) — the memory-side half of the "every layer between memory and compute costs
  you" philosophy
  - Evidence paragraphs: `[0016]`, `[0043]`, `[0044]`, `[0045]`
  - Quote anchor refs: `q-0016-1`, `q-0043-1`, `q-0044-1`, `q-0045-1`
- **transformer-division-of-labor**: self-attention delegated to auxiliary circuitry with
  private local memory the arrays never touch (claims 11-13) — a transformer-shaped split
  of the silicon
  - Evidence paragraphs: `[0047]`, `[0051]`
  - Quote anchor refs: `q-0047-1`, `q-0047-2`, `q-0051-1`
- **preset-loop-inflexibility**: the combined array takes no instructions at runtime — the
  specialization-over-flexibility bet, in the origin filing
  - Evidence paragraphs: `[0027]`
  - Quote anchor refs: `q-0027-1`

## Claim scope map (pending-application edition: sought / open / pinned)

> **Retitled for a pending application.** There is NO "locked" class in this map — every
> "requires as drafted" entry is scope Etched is SEEKING, and the claim set has already
> drawn a final rejection (see fact-check-log `prosecution-record`). Each independent
> carries a one-line prosecution-risk note against the examiner-cited field (multi-node ML
> acceleration, hybrid parallelism, NN accelerator architectures).

| Claim | Scope class | Requires as drafted (SOUGHT, not locked) | Leaves open (description preference only) | Pins (approximate point limitations) | Prosecution-risk note |
|---|---|---|---|---|---|
| 1 (indep.) | sought-broad | A package; plurality of ICs each with a local systolic array of DPUs; chip-to-chip connections connecting each local array to at least one other to form a larger, combined systolic array | Connection technology (UCIe is a description preference, `[0030]`); horizontal/vertical directionality (deps 2-4); grid vs stack (deps 9-10); any memory arrangement | none | Broadest of the four; "connect chip-level arrays into a bigger array" sits closest to the examiner-cited multi-node ML acceleration / hybrid parallelism art — likeliest to narrow or die; the set has already been finally rejected once. |
| 15 (indep.) | sought-system | An AI accelerator; ICs with local arrays; chip-to-chip connections forming a combined array; plurality of memory chips storing weights for matrix multiplications, coupled to the ICs forming a top row | HBM as the memory type and switchless hardwiring (deps 19-20); interposer vs stacked ICs (deps 21-22); auxiliary circuitry (deps 23-25) | none | Middle risk — top-fed, weight-stationary arrays are the accelerator mainstream, so the memory-chips-on-top-row element alone may not carry allowance over the cited NN-accelerator art. |
| 26 (indep.) | sought-structured | A package; plurality of ICs each with a local systolic array, arranged in a grid-like pattern; local arrays connected to form a larger, combined systolic array (no explicit chip-to-chip-connections element) | How the arrays are connected (deps 27-29); interposer/stack (deps 34-35); auxiliary circuitry (deps 36-38) | none | Rises and falls with claim 1 — "grid-like pattern" adds little distance from the same multi-node acceleration art; likely shares claim 1's fate. |
| 39 (indep.) | sought-memory-interface | A package; an IC with a systolic array of DPUs; a separate memory device with a plurality of channels, EACH channel hardwired to respective one or more columns in the array without any switching element | Memory device being an HBM (dep 41); storing weight data (dep 40); multiple such memory devices (dep 42) | none | Most structurally specific independent — switchless channel-to-column hardwiring inverts the typical crossbar practice the spec itself describes `[0043]`; likeliest of the four to survive in some form, though the "without any switching element" negative limitation remains examinable. |
| 7-8 (dep. on 1→5) | sought-memory-interface (HBM form) | HBMs hardwired to respective columns in the local arrays without any switching element; multiple HBMs per top-row IC | Number of HBMs beyond "multiple" | none | Inherits claim 1's fate as dependents — but their subject matter overlaps claim 39's, giving the memory-interface idea a second prosecution path. |
| 11-13 (dep. on 1) | sought-auxiliary-division | Auxiliary circuitry separate from the local array, with local memory chips coupled to it (11); auxiliary circuitry performs self-attention using previous-token data in local memory (12); local systolic arrays do NOT communicate with the local memory chips (13) | What the auxiliary circuitry is (separate systolic array, micro-processor, ALU — `[0050]`); how many local memories (`[0048]`-`[0049]`) | none | Inherit claim 1's fate; the arrays-never-touch-local-memory division (13) is the most transformer-specific limitation in the set. |

## Reference number table

| Number | Label | Paragraphs | Figures |
|---|---|---|---|
| 100 | Systolic array (single, logical) | `[0020]`-`[0024]`, `[0028]` | FIG. 1 |
| 105 | DPUs (data processing units) | `[0020]`-`[0024]` | FIG. 1 |
| 110 | Model weights | `[0021]`, `[0022]` | FIG. 1 |
| 115 | Previous tensor | `[0021]`, `[0022]` | FIG. 1 |
| 200 | System | `[0025]` | FIG. 2 |
| 201 | Package | `[0025]`-`[0038]` | FIG. 2 |
| 205 | Host | `[0025]`-`[0027]`, `[0037]` | FIG. 2 |
| 210 | Memory chips (top-row feed) | `[0034]`-`[0037]`, `[0046]` | FIG. 2, FIG. 6 |
| 215 | ICs (chips with local arrays) | `[0027]`-`[0045]` | FIG. 2, FIG. 3, FIG. 4, FIG. 5 |
| 220 | Local systolic arrays (array tiles) | `[0028]`-`[0035]`, `[0044]`-`[0046]`, `[0051]` | FIG. 2, FIG. 3, FIG. 4, FIG. 5, FIG. 6 |
| 225 | Vertical chip-to-chip connections | `[0029]`-`[0032]`, `[0034]`, `[0040]`, `[0046]`, `[0052]` | FIG. 2, FIG. 6 |
| 230 | Horizontal chip-to-chip connections | `[0029]`-`[0032]`, `[0046]`, `[0052]` | FIG. 2, FIG. 6 |
| 240 | PCIe connections | `[0026]`, `[0027]`, `[0037]` | FIG. 2 |
| 250 | Combined systolic array | `[0025]`-`[0038]` | FIG. 2 |
| 301 | Package (square-grid variant) | `[0039]` | FIG. 3 |
| 305 | Memory chips (multiple per IC) | `[0039]`, `[0040]` | FIG. 3, FIG. 4 |
| 350 | Combined systolic array (square) | `[0039]`, `[0040]` | FIG. 3 |
| 401 | Package (unequal-grid variant) | `[0041]` | FIG. 4 |
| 450 | Combined systolic array (unequal rows/columns) | `[0041]`, `[0042]` | FIG. 4 |
| 505 | Memory chips (hardwired external) | `[0043]`-`[0045]` | FIG. 5 |
| 510 | Channels (independent memory channels) | `[0043]`-`[0045]` | FIG. 5 |
| 515 | Columns (of DPUs in the local array) | `[0044]`, `[0045]` | FIG. 5 |
| 520 | Wires (hardwiring, no switch) | `[0043]`, `[0044]` | FIG. 5 |
| 605 | Auxiliary circuitry | `[0047]`-`[0052]` | FIG. 6 |
| 610 | Local memory chips | `[0048]`-`[0051]` | FIG. 6 |
| 615 | ICs (with auxiliary circuitry) | `[0046]`-`[0052]` | FIG. 6 |
| 650 | Combined systolic array (with aux circuitry) | `[0046]`, `[0047]`, `[0052]` | FIG. 6 |

> Note: the figures-manifest one-liner for FIG. 6 mislabels 605 as "local memory chips";
> per the specification and the drawing itself, 605A-D are the auxiliary-circuitry blocks
> inside ICs 615A-D and 610A-D are the external local memory chips. This table follows the
> specification.

## Figure relationships

| Figure | Paired with | Relationship | Page (if known) | Cover candidate? | Phase map (sequences only) |
|---|---|---|---|---|---|
| FIG. 1 | FIG. 2 | logical/physical pair — `[0028]`: the combined array 250 of FIG. 2 "can be represented by the array 100 in FIG. 1" (one is the logical view of the other) | sheet 1 | | |
| FIG. 2 | FIG. 3, FIG. 4 | variant family — FIG. 3 (square grid, multiple memory chips per IC) and FIG. 4 (unequal rows/columns) are sizing variants of FIG. 2's package concept, not a progressive sequence | sheets 2-4 | | |
| FIG. 5 | (standalone; detail of the memory-to-array interface) | zooms into one IC to show channels 510 hardwired to columns 515 — the claim-39 core step | sheet 5 | **yes** — most literal picture of the claimed core step (claim 39 switchless hardwiring), strong graphic hierarchy (two memory chips over four columns) | |
| FIG. 6 | (standalone; extends FIG. 2) | adds auxiliary circuitry 605 + local memory 610 per IC to the combined-array concept (claims 11-13) | sheet 6 | | |
| FIG. 7 | (standalone) | timeline chart of pipelined transformer operations over one array row | sheet 7 | | |

No progressive sequences; no Phase map required.

## Quote anchor table

| Quote ID | Paragraph | Verbatim text | Significance |
|---|---|---|---|
| q-0002-1 | `[0002]` | "Systolic arrays are hardware structures built for fast and efficient operation of algorithms that typically perform the same task with different data at different times." | mechanism-critical |
| q-0003-1 | `[0003]` | "For many artificial intelligence (AI) applications (e.g., transformer models), matrix multiplications dominate the operations that must be performed in hardware." | mechanism-critical |
| q-0003-2 | `[0003]` | "However, the number of floating-point operations per second (FLOPs) that can be achieved is often dependent on the size of the systolic array, which is limited in current IC design." | prior-art-contrast |
| q-0013-1 | `[0013]` | "a package that includes a plurality of integrated circuits (ICs), each comprising a local systolic array of data processing units (DPUs) and chip-to-chip connections configured to connect the local systolic array in each of the plurality of ICs to at least one other local systolic array in another one of the plurality of ICs to form a larger, combined systolic array" | claim-supporting |
| q-0014-1 | `[0014]` | "a plurality of memory chips configured to store weights for performing matrix multiplications in the combined systolic array as part of an AI model, the plurality of memory chips coupled to the plurality of ICs forming a top row of the combined systolic array" | claim-supporting |
| q-0015-1 | `[0015]` | "the plurality of ICs are arranged in a grid-like pattern and the local systolic arrays are connected to form a larger, combined systolic array" | claim-supporting |
| q-0016-1 | `[0016]` | "a separate memory device comprising a plurality of channels where each of the plurality of channels is hardwired to respective one or more columns in the systolic array without any switching element" | claim-supporting |
| q-0018-1 | `[0018]` | "Currently, most chips have, at most, floating point systolic arrays with a size of 128×128." | prior-art-contrast |
| q-0018-2 | `[0018]` | "it is unreasonable to expect a single chip to interface with 100s of GB of memory used to store parameters and intermediate computation values" | prior-art-contrast |
| q-0019-1 | `[0019]` | "Instead, the embodiments herein adapt a multi-chip approach where multiple local systolic arrays on multiple chips (or ICs) are connected using high-speed chip-to-chip connections to form a larger, combined systolic array." | mechanism-critical |
| q-0021-1 | `[0021]` | "The topmost row of DPUs 105 receive AI model weights 110, which may be constants." | mechanism-critical |
| q-0027-1 | `[0027]` | "the systolic array 250 does not take instructions at runtime, and only executes instructions in a preset loop" | mechanism-critical |
| q-0028-1 | `[0028]` | "from the perspective of the host 205, the systolic array 250 appears to be one large array, even though it is physically made up of smaller local systolic arrays 220 distributed on separate ICs 215" | mechanism-critical |
| q-0030-1 | `[0030]` | "Universal Chiplet Interconnect Express (UCIe) can be used to form the chip-to-chip (or die-to-die) connections" | mechanism-critical |
| q-0030-2 | `[0030]` | "which has a physical layer that supports up to 32 GT/s with 16 to 64 lanes" | quantitative |
| q-0035-1 | `[0035]` | "If the systolic array 250 is used in an AI accelerator application, the memory chips 210 can store the weights for the AI model being used at runtime." | claim-supporting |
| q-0039-1 | `[0039]` | "adding more rows of ICs 215 increases the compute power of the systolic array 350, without having to add more memory chips 305 at the top to feed in data in the vertical direction" | mechanism-critical |
| q-0040-1 | `[0040]` | "can enable the memory chips 305 to transmit more than 1 TB/s of data to each of the ICs" | quantitative |
| q-0043-1 | `[0043]` | "a switch (or some kind of switching element such as a crossbar) is typically used so that the device can access the entire memory of the HBM" | prior-art-contrast |
| q-0044-1 | `[0044]` | "the independent channels 510 can be directly wired (or hardwired) to a particular column 515 in the local systolic array 220 of the IC 215" | mechanism-critical |
| q-0045-1 | `[0045]` | "hardwiring the memory chips 505 to the columns 515 is permissible" | claim-supporting |
| q-0045-2 | `[0045]` | "which can save space and power" | mechanism-critical |
| q-0047-1 | `[0047]` | "for AI accelerators, self-attention operations use data computed from previous tokens, which means such data should be saved" | mechanism-critical |
| q-0047-2 | `[0047]` | "Most of the parts of a transformer AI model do not use data from previous tokens" | mechanism-critical |
| q-0051-1 | `[0051]` | "In this embodiment, the local systolic arrays 220 do not have access to the local memory chips 610." | claim-supporting |
| q-0055-1 | `[0055]` | "For example, to calculate the query values (e.g., perform the "Attention: queries" computation) used in the attention mechanism of transformer AI models, the data passes through the systolic array three times. For example, the input tensor for calculating the query values may be divided into three portions, where the portions are inputted into the systolic array in three batches. This is the same for performing the "Attention: keys", "Attention: values", and "Projection" operations, which also appear in the example of running a transformer AI model. Continuing this example, the hidden and output layers for multi-layer perceptron (MLP)—a portion of a transformer which performs non-linear transformations on the input embeddings—operations may also use multiple batches or passes to calculate the outputs." | mechanism-critical |
| q-0056-1 | `[0056]` | "To achieve 100% efficiency (or close to 100% efficiency), the inputs for the subsequent computation are fed into the systolic array before the previous computation completes. For example, at Time A, the leftmost DPU in the row (e.g., DPU 0) is performing the computation associated with the output layer of the MLP, while the rightmost DPU in the row (e.g., DPU Y) is still working on the previous computation, the MLP hidden layer." | mechanism-critical |
| q-0057-1 | `[0057]` | "the stalled time may be small relative to the computation time and still result in a 98% or greater utilization of the systolic array" | quantitative |

> Note — typographic artifacts in patent.md: the markdown conversion produced run-on
> tokens in a few paragraphs ("105passes" `[0022]`, "230are" `[0029]`, "225and 230"
> `[0030]`, "250formed" `[0025]`, "215in" `[0040]`, "220and" `[0045]`) and the exponent
> artifact "2N{circumflex over ( )} 2" `[0018]`. The anchors above are chosen to stop
> BEFORE these artifacts. Phase 2 must not extend any quote across them (a longer quote
> would either reproduce the artifact or fail verbatim verification).

## Timeline

- **Filing date**: 2023-05-10
- **Publication date**: 2024-11-14
- **Examination period**: 554 days filing-to-publication; still in examination as of
  2026-05 (final rejection mailed 2025-10-23, 897 days after filing; RCE docketed
  2026-04-24; third non-final office action issuing as of 2026-05 — registry-extract)
- **Prior-art chronology**:
  | Citation | Filing date | Publication date | Days relative to subject filing |
  |---|---|---|---|
  | (none applicant-cited — the specification cites no prior-art documents) | — | — | — |

  The examination record lists 8 unique references, all examiner-cited (multi-node ML
  acceleration, hybrid parallelism, NN accelerator architectures) — registry-external,
  dates not in this run's inputs; see fact-check-log `examiner-cited-field`.

## Prior-art references + differentiation

- **No applicant-cited references**: the specification's Background contrasts only with
  current practice, not named documents — the single-chip array-size ceiling (`[0018]`,
  q-0018-1) and the hundreds-of-GB memory-interface problem (`[0018]`, q-0018-2).
- **Examiner-cited field (external, registry-extract)**: 8 unique references, all
  examiner-cited, clustered in multi-node ML acceleration, hybrid parallelism, and NN
  accelerator architectures — a crowded field, and the art against which the sought
  claims (especially broad claims 1/26) have already drawn a final rejection. Fact-check
  log: `examiner-cited-field`, `prosecution-record`.
- **Industry-practice contrast within the spec**: switched/crossbar HBM access is the
  stated norm (`[0043]`, q-0043-1); the application differentiates by hardwiring channels
  to columns and deleting the switch (`[0044]`-`[0045]`).

## 유리한 효과 + 정량 데이터

The claimed effects are architectural: one logical array with the I/O economics of a large
systolic array (an N×N array computes ~2N² FLOPs per cycle on 2N inputs, per `[0018]`);
compute that scales by adding rows of ICs without adding memory chips, since weight data
is reused down the rows `[0039]`; more than 1 TB/s of weight bandwidth into each top-row
IC when multiple memory chips are attached `[0040]`; a deleted switching element between
memory and array, saving space and power `[0045]`; and pipelining that holds the combined
array at 98%-or-greater utilization even with layer-normalization stalls `[0057]`.

**Quotable spans:**
- `[0039]`: "adding more rows of ICs 215 increases the compute power of the systolic array 350, without having to add more memory chips 305 at the top to feed in data in the vertical direction"
- `[0040]`: "can enable the memory chips 305 to transmit more than 1 TB/s of data to each of the ICs"
- `[0045]`: "which can save space and power"
- `[0055]`: "This is the same for performing the "Attention: keys", "Attention: values", and "Projection" operations, which also appear in the example of running a transformer AI model. Continuing this example, the hidden and output layers for multi-layer perceptron (MLP)—a portion of a transformer which performs non-linear transformations on the input embeddings—operations may also use multiple batches or passes to calculate the outputs."
- `[0056]`: "To achieve 100% efficiency (or close to 100% efficiency), the inputs for the subsequent computation are fed into the systolic array before the previous computation completes. For example, at Time A, the leftmost DPU in the row (e.g., DPU 0) is performing the computation associated with the output layer of the MLP, while the rightmost DPU in the row (e.g., DPU Y) is still working on the previous computation, the MLP hidden layer."
- `[0057]`: "the stalled time may be small relative to the computation time and still result in a 98% or greater utilization of the systolic array"

| Metric | Value | Paragraph |
|---|---|---|
| Single-chip systolic array ceiling (stated baseline) | 128×128 | `[0018]` |
| Model memory footprint (stated problem) | 100s of GB | `[0018]` |
| Local systolic array size range | ~100-10000 rows × 100-10000 columns | `[0033]` |
| UCIe chip-to-chip physical layer | up to 32 GT/s, 16-64 lanes | `[0030]` |
| Weight bandwidth into each top-row IC (multi-chip) | >1 TB/s | `[0040]` |
| Combined-array utilization with pipelining | ≥98% | `[0057]` |
| N×N array I/O economics | 2N² FLOPs per cycle for 2N inputs per cycle | `[0018]` |
