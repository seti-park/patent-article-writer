# Invention Summary

## Metadata

- **Patent ID**: US 12,361,091 B1
- **Title**: Tensor parallel group
- **Filing date**: 2024-10-22 (US 18/922,976)
- **Publication date**: 2025-07-15 (grant date; B1 document)
- **Inventors**: Gavin Uberti (sole inventor; Etched co-founder/CEO per fact-check-log `etched-family-trio-wips`)
- **Classification**: <unknown> (CPC codes not included in the provided patent.md text)
- **Assignee**: Etched.ai Inc.

## 발명 명칭 / 기술분야

Essay-ready phrasing: a fixed wiring plan for a group of AI accelerator chips ("tensor
parallel group") that lets every chip talk to every other chip through at most one
intermediate chip, with no network switch, by splitting the chips into two sets and
directly wiring every chip in one set to every chip in the other set and none within the
same set. 기술분야: parallel computing hardware topology for tensor operations, aimed at
tensor parallelism in large AI models `[0001]`, `[0002]`.

## 종래 문제 / 과제

Large tensors overwhelm a single processor, so the work is split across devices
(tensor parallelism) `[0021]`. But splitting creates a data-sharing problem: devices must
exchange sub-results (reduction `[0037]`) and copies (gather `[0039]`) mid-computation
`[0036]`-`[0040]` (definitional paragraphs made explicit per the round-2 self-audit
grounding pass; notation only, no new quote rows).
The two conventional ways to wire that exchange both carry a cost the patent names: a
data/networking switch that allows any-to-any sharing is expensive `[0026]`, `[0032]`,
and a full point-to-point mesh multiplies the number of physical connections `[0130]`.
The pressure is worst in transformer feedforward (MLP) layers, where a single computation
involves four times the model depth, inflating processing time or the bandwidth needed to
hold processing time `[0313]`.

**Quotable spans:**
- `[0021]`: "In some situations, tensors may be large enough that processing of the tensors in a typical manner using a single processor may be difficult."
- `[0026]`: "In some circumstances, a data switch that allows sharing of data amongst different processing device may be expensive to include in a system that performs tensor operations."
- `[0313]`: "the processing time for the feedforward operation may be much larger than for other operations and/or a data bandwidth required to maintain a processing time for the feedforward operation may be increased"

> Note: `[0026]` reads "different processing device" (singular) in the source; preserved
> verbatim. Do not silently correct when citing.

## 청구항 분석 — 4-layer core mechanism

### Layer 1 — What (one sentence)

A tensor parallel group whose processing devices are separated into two disjoint sets and
wired as a complete cross-set network (every device in one set directly linked to every
device in the other set, none linked within its own set), so that any device reaches any
other device through at most one intermediate device, without a switch.

### Layer 2 — How (mechanism)

1. Separate the processing devices (A0-A7; 110a-110d in FIG. 1) into a first set (710a)
   and a second set (710b) with no device in both sets `[0126]`, claims 1-2.
2. Directly wire every device in set 710a to every device in set 710b via dedicated
   communication channels; create no channel inside a set `[0128]`, `[0129]`, claim 1.
3. Subdivide each set into two groups (712a-712d; each set includes two of the groups
   `[0136]`) and split the channels into two families: first communication channels 730
   (712a↔712c, 712b↔712d) and second communication channels 740 (712a↔712d, 712b↔712c)
   `[0135]`-`[0139]`, claim 18.
4. Bind each sub-operation of a tensor operation exclusively to one channel family (the
   description's example: gather traffic on 730, reduction traffic on 740) and run both
   sub-operations during overlapping time periods `[0140]`, `[0142]`, claims 8-9, 11.
5. Split tensors into tiles distributed so no device holds a whole tensor and each device
   and each channel moves the same amount of data during collectives `[0146]`-`[0168]`,
   `[0278]`.
6. For same-set communication, route through exactly one opposite-set device (at most two
   channel hops); a relay device may start forwarding before it has received all the data
   `[0130]`, `[0143]`.

**Key components**: tensor parallel group 700 (100), processing devices A0-A7 (110a-110d),
systolic arrays 112a-112d, processing elements 114a-114d, group systolic array 120, first
set 710a / second set 710b, groups 712a-712d, first communication channels 730, second
communication channels 740, processing system 610, tensor parallel groups 620a/620b,
memory 630, host 602.

### Layer 3 — Why novel

- **Relative to prior art**: The patent cites no prior-art documents in the provided text;
  it differentiates against the two conventional wiring alternatives it names itself: an
  any-to-any networking/data switch, which is "expensive" `[0026]`, `[0032]`, and a full
  point-to-point scheme, which needs a direct channel for every pair `[0130]`. The claimed
  bipartite fixed topology keeps any-to-any reachability (at most one intermediate device)
  while removing the switch and cutting the link count relative to a full mesh (derived,
  not stated in the patent: 8 devices need 16 cross-set channels vs 28 for a full mesh).
- **Industry practice contrast**: Conventional scale-up domains buy any-to-any reachability
  with switch fabrics, and balanced collective traffic is a scheduling problem. Here the
  wiring itself encodes the collective patterns: reduce and gather each get a dedicated
  channel family (claims 8, 11) that can run simultaneously (claim 9), and equal tile
  splits make every channel carry the same amount of data `[0168]`, `[0178]`. (Framing
  contrast only; no external switch-fabric spec was verifiable in this environment - see
  search-log.md.)

### Layer 4 — Innovation angles

- **switchless-bipartite-topology**: claim 1's structure - all-to-all across sets, nothing
  within a set, any-to-any through at most one intermediate device, no switch.
  - Evidence paragraphs: `[0128]`, `[0129]`, `[0130]`, `[0386]`, `[0387]`
  - Quote anchor refs: `q-0128-1`, `q-0129-1`, `q-0130-1`, `q-0386-1`, `q-0387-1`
- **channel-family-traffic-segregation**: two channel subsets with exclusive sub-operation
  traffic (reduction on one, gather on the other), running in overlapping time periods -
  the inference-collective-shaped part of the wiring (claims 8-11, 18-23).
  - Evidence paragraphs: `[0138]`, `[0139]`, `[0140]`, `[0142]`
  - Quote anchor refs: `q-0140-1`, `q-0140-2`, `q-0142-1`
- **never-gather-the-tensor**: the execution invariant that no single device ever holds an
  entire tensor through the decoding layers - tensors live as tiles spread across the
  group, with balanced per-channel data movement.
  - Evidence paragraphs: `[0278]`, `[0267]`, `[0168]`
  - Quote anchor refs: `q-0278-1`, `q-0267-1`, `q-0168-1`
- **claims-vs-narrative-split**: what is granted here is structure only - the claims track
  the spec's "Example 2" family (tensor parallel group topology), while the Example 1
  (tensor-operation methods) and Example 3 (AI-model computation) families are described
  but not claimed in this patent; and claims 1/14 narrow the description's "two or more"
  per set `[0385]` to "four or more" per set. Memory 630 is described `[0119]` and never
  claimed.
  - Evidence paragraphs: `[0385]`, `[0119]`, `[0336]` (the numbered-example convention;
    the three families' contents sit at `[0337]` Example 1, `[0384]` Example 2, `[0418]`
    Example 3 - paragraph attributions confirmed by the self-audit grounding pass)
  - Quote anchor refs: `q-0385-1`, `q-0119-1`

## Claim scope map

Independent claims: 1 (tensor parallel group), 14 (system of groups), 18 (dual-channel-family
group). One row per independent claim plus the dependent claims the spine relies on.

| Claim | Locks (required by claim text) | Leaves open (description preference only) | Pins (approximate point limitations) |
|---|---|---|---|
| 1 | Two sets of processing devices, each set "four or more" devices (so 8+ total); a plurality of communication channels that "directly communicatively couple every processing device in the first set ... with every processing device in the second set" and do NOT couple any devices "in the same set"; every device can communicate with any other "through at most one other" processing device. | Link technology (PCIe, SPI, ethernet, UCIe, optical, on-die are description options `[0134]`, `[0133]`); separate-die vs same-die packaging `[0133]`; equal set sizes `[0126]`-`[0127]`; any latency or bandwidth magnitude (never claimed); memory attachment `[0119]`, `[0133]`; AI/LLM workload (description only, `[0251]`+). | none |
| 2 | No intersection of devices between the two sets. | — | none |
| 3 | Each device communicatively coupled to a same number of devices. | The number itself (4 is the FIG. 7 example `[0129]`). | none |
| 4 | Each device coupled to a same number of communication channels. | The number itself. | none |
| 5 | Each channel configured for a same data bandwidth. | The bandwidth value (equality is claimed, magnitude is not). | none |
| 6 | Each device can simultaneously transmit and receive over different channels. | — | none |
| 7 | Each device includes a systolic array of data processing units. | Output-stationary vs weight/input-stationary array styles `[0029]`. | none |
| 8 | Channels separated into two subsets; every device coupled to at least one channel of each subset; an operation with a first and a different second sub-operation; data transfer for the first sub-operation ONLY via the first subset, for the second ONLY via the second subset. | Which sub-operation rides which physical channel family (gather-on-730 / reduction-on-740 is the description's example `[0140]`). | none |
| 9 | The two sub-operations run in overlapping time periods: first-sub-operation data on subset one at the same time as second-sub-operation data on subset two. | — | none |
| 10 | The operation is a matrix multiplication. | — | none |
| 11 | First sub-operation is a reduction operation and second is a gather operation. | — | none |
| 12 | Device count is a multiple of two. | — | none |
| 13 | Device count is eight (exact count, locked by this dependent claim only - NOT a claim-1 requirement). | — | none |
| 14 | A system with a PLURALITY of tensor parallel groups, each with claim-1's structure ("four or more" per set, cross-set all-to-all coupling, none within set, at-most-one-intermediate communication). | How the groups interconnect with each other (not specified); pipeline arrangement is dependent claim 15. | none |
| 15 | Two or more groups arranged in a parallel pipeline configuration. | Pipeline depth, task split `[0117]`-`[0118]`. | none |
| 18 | Two sets of "two or more" devices each (broader floor than claim 1's four); first set contains a first and second group, second set contains a third and fourth group; first communication channels couple every device group1↔group3 and group2↔group4; second communication channels couple every device group1↔group4 and group2↔group3; an operation with two sub-operations whose data transfer is exclusive per channel family. | Overlapping-time execution (that is claim 9's limitation under claim 1, not restated in 18); which sub-operation is reduction vs gather (locked only by dependent 23); the at-most-one-intermediate property (added by dependent 22). | none |
| 22 | Adds to 18: every device communicates with any other through at most one other device. | — | none |
| 23 | Adds to 18: operation is matrix multiplication; first sub-operation reduction, second gather. | — | none |

Scope-reading notes (Phase 2 traps restate these; see phase2-handoff-notes.md §d):
- The abstract and SUMMARY `[0004]` and Example 2.1 `[0385]` say "two or more" per set; the
  GRANTED claims 1 and 14 require "four or more" per set. The narrowing happened in
  prosecution; never quote the abstract as the scope of claim 1.
- Claim 18 keeps the "two or more" floor but pays for it with the four-group,
  two-channel-family structure. The three independents do not share one floor.
- "Eight devices" is FIG. 7's worked example and dependent claim 13's exact count. Claim 1
  requires at least four per set.
- No independent claim mentions memory, latency, bandwidth magnitude, AI, transformers, or
  inference. Closest workload hooks in the claims: systolic array (7), matrix
  multiplication (10, 23), reduction/gather (11, 23).

## Reference number table

| Number | Label | Paragraphs | Figures |
|---|---|---|---|
| 100 | Tensor parallel group | `[0028]`, `[0033]`, `[0068]` | FIG. 1 |
| 110a-110d | First-fourth processing devices | `[0028]`, `[0029]`, `[0032]` | FIG. 1 |
| 112a-112d | Systolic arrays | `[0029]`, `[0030]` | FIG. 1 |
| 114a-114d | Processing elements | `[0029]`, `[0031]` | FIG. 1 |
| 120 | Group systolic array | `[0033]`, `[0034]` | FIG. 1 (dashed boundary) |
| 200 | Tensor splitting (of tensor B into tiles C, D) | `[0035]` | FIG. 2 |
| 300 (302-332) | Method to perform tensor operations (blocks) | `[0069]`-`[0093]` | FIG. 3 |
| 400 (402-408) | Method to perform tensor operations (blocks) | `[0094]`-`[0103]` | FIG. 4 |
| 500 (502-510) | Method to perform matrix operations (blocks) | `[0104]`-`[0111]` | FIG. 5 |
| 600 | Example environment | `[0112]`, `[0122]` | FIG. 6 |
| 602 | Host | `[0112]`-`[0114]` | FIG. 6 |
| 610 | Processing system | `[0112]`-`[0116]` | FIG. 6 |
| 620a/620b | First/second tensor parallel groups (labeled "Tensor Parallel Device" in the drawing) | `[0112]`, `[0116]`-`[0120]` | FIG. 6 |
| 630 | Memory | `[0112]`, `[0119]` | FIG. 6 |
| 700 | Tensor parallel group (8-device topology) | `[0123]`-`[0125]`, `[0144]` | FIGS. 7A, 7B, 7C |
| 710a / 710b | First / second set of processing devices | `[0126]`, `[0128]`-`[0130]` | FIGS. 7A, 7B, 7C |
| 712a-712d | First-fourth groups of processing devices | `[0135]`-`[0139]` | FIGS. 7A, 7B, 7C |
| 730 | First communication channels | `[0138]`, `[0140]`, `[0169]`, `[0241]` | FIG. 7A, FIG. 7C |
| 740 | Second communication channels | `[0139]`, `[0140]`, `[0159]`, `[0211]` | FIG. 7B, FIG. 7C |
| A0-A7 | Processing devices of group 700 | `[0123]`, `[0126]`, `[0146]`-`[0243]` | FIGS. 7A, 7B, 7C |
| 800 (802-818) | Method using the FIG. 7A/7B topology (blocks) | `[0145]`-`[0246]` | FIG. 8 |
| 900 | AI model | `[0251]`, `[0260]` | FIG. 9A |
| 905 | Decoding layers | `[0252]`, `[0259]`, `[0278]` | FIG. 9A |
| 910 | Normalization layer | `[0252]`, `[0253]` | FIG. 9A |
| 915 | Self-attention layer | `[0252]`, `[0254]`-`[0255]`, `[0262]`-`[0268]` | FIG. 9A, FIG. 9B |
| 916 | QKV generation | `[0254]` | FIG. 9A |
| 918 | Attention computation | `[0254]` | FIG. 9A |
| 920 | Projection layer | `[0252]`, `[0256]`, `[0269]`-`[0271]` | FIG. 9A, FIG. 9B |
| 925 | Multi-layer perception (MLP) layer | `[0252]`, `[0257]`-`[0258]`, `[0272]`-`[0277]` | FIG. 9A, FIG. 9B |
| 930 | Decoding (token selection) | `[0259]` | FIG. 9A |
| 1000 (1002-1026) | Method for AI-model tensor operations (blocks) | `[0279]`-`[0304]` | FIG. 10 |
| 1100 (1102-1106) | Method for AI-model tensor operations (blocks) | `[0305]`-`[0312]` | FIG. 11 |
| 1200 (1202-1210) | Feedforward-operation method (blocks) | `[0315]`-`[0321]` | FIG. 12 |
| 1300 | Example system | `[0322]`-`[0334]` | FIG. 13 |
| 1310 / 1312 / 1316 / 1318 / 1320 / 1322 | Processor / memory / communication unit / display / user interface unit / peripheral devices | `[0322]`, `[0324]`-`[0333]` | FIG. 13 |

## Figure relationships

| Figure | Paired with | Relationship | Page (if known) | Cover candidate? | Phase map (sequences only) |
|---|---|---|---|---|---|
| FIG. 1 | (standalone) | — | sheet 1 | | |
| FIG. 2 | (standalone) | — | sheet 2 | | |
| FIG. 3 | FIG. 4, FIG. 5 | sibling method flowcharts (same concept family) | sheets 3-5 | | |
| FIG. 6 | (standalone) | — | sheet 6 | | |
| FIG. 7A | FIG. 7B, FIG. 7C | decomposition pair + union: 7A and 7B are the two channel-family subgraphs of ONE fixed topology, split "for case of illustration" [sic] `[0123]`; 7C overlays both in a single figure `[0125]`. NOT a temporal sequence. | sheets 7-9 | yes - FIG. 7C (most literal picture of claim 1's claimed core; highest visual force) | n/a (structural decomposition, not phases) |
| FIG. 8 | FIGS. 7A/7B | method flowchart executing on the FIG. 7 topology `[0145]` | sheet 10 | | |
| FIG. 9A | FIG. 9B | same-subject pair: block diagram + its tensor-equation detail | sheets 11-12 | | |
| FIG. 10 | FIG. 8 | AI-model method whose blocks cite FIG. 8's processes `[0287]`, `[0297]`, `[0298]`, `[0300]` | sheet 13 | | |
| FIG. 11 | (standalone) | — | sheet 14 | | |
| FIG. 12 | FIG. 8 | feedforward method citing FIG. 8 blocks `[0318]`-`[0320]` | sheet 15 | | |
| FIG. 13 | (standalone) | generic computer-system boilerplate | sheet 16 | | |

Pairing rule for Step 9: FIGS. 7A/7B/7C travel as one cognitive unit. Selecting only 7C
loses the channel-family split that claims 8/11/18 hang on; selecting only 7A/7B loses the
union that claim 1 hangs on.

## Quote anchor table

| Quote ID | Paragraph | Verbatim text | Significance |
|---|---|---|---|
| q-0021-1 | `[0021]` | "In some situations, tensors may be large enough that processing of the tensors in a typical manner using a single processor may be difficult." | prior-art-contrast |
| q-0026-1 | `[0026]` | "In some circumstances, a data switch that allows sharing of data amongst different processing device may be expensive to include in a system that performs tensor operations." | prior-art-contrast |
| q-0026-2 | `[0026]` | "the tensors on which operations may be performed may be divided amongst the processing devices in the fixed topology in a particular manner to reduce data sharing between the processing devices and thereby help to reduce a processing time for the tensor operations" | mechanism-critical |
| q-0032-1 | `[0032]` | "the processing devices 110 may be coupled together using a networking switch that enables communication between any one of the processing devices 110 with any other one of the one of the processing devices 110 ." | prior-art-contrast |
| q-0061-1 | `[0061]` | "When the number of processing devices is 8, p=4.35235, q=1.83809." | quantitative |
| q-0061-2 | `[0061]` | "it is understood to reduce the maximum transfer bandwidth, the input matrix may be split such that an entirety of the input matrix is found on 4 of the 8 processing devices so that the parallelism of the input is 4" | quantitative |
| q-0117-1 | `[0117]` | "The two tensor parallel groups 620 may be used to perform pipeline parallelism." | claim-supporting |
| q-0119-1 | `[0119]` | "The memory packages may be configured to provide tensors and other data to the tensor parallel groups 620 for processing." | mechanism-critical |
| q-0121-1 | `[0121]` | "the size of the tensor parallel groups 620 may be based on the computations performed by the feedforward operations performed by a MLP layer of an AI model" | mechanism-critical |
| q-0123-1 | `[0123]` | "the fixed topology connecting the processing devices A0-A7 may include all the connections of FIGS. 7 A and 7 B ." | mechanism-critical |
| q-0124-1 | `[0124]` | "the fixed topology as illustrated in FIGS. 7 A and 7 B and described in this disclosure may be used to reduce data sharing between the processing devices A0-A7 and thereby help to reduce a processing time for the tensor operations performed by a tensor parallel group 700 ." | claim-supporting |
| q-0125-1 | `[0125]` | "FIG. 7 C illustrates all connections between the processing devices A 0 -A 7 of the tensor parallel group 700 in a single figure." | mechanism-critical |
| q-0126-1 | `[0126]` | "Half of the processing devices A0-A7 are in the first set of processing devices 710 a , namely processing devices A1, A3, A5, and A7 and the other half of the processing devices A0-A7 are in the second set of processing devices 710 b , namely processing devices A0, A2, A4, and A6." | mechanism-critical |
| q-0128-1 | `[0128]` | "there are no direct communication channels between the processing devices in the first set of processing devices 710 a and no direct communication channels between the processing devices in the second set of processing devices 710 b ." | claim-supporting |
| q-0128-2 | `[0128]` | "A direct communication channel may be a communication channel that directly links two of the processing devices A0-A7 without another one of the processing devices A0-A7 therebetween." | mechanism-critical |
| q-0129-1 | `[0129]` | "each processing device in the first set of processing devices 710 a may be directly connected to each of the processing devices in the second set of processing devices 710 b via a different communication channel" | claim-supporting |
| q-0129-2 | `[0129]` | "each of the processing devices A0-A7 may be coupled to four other of the processing devices A0-A7." | quantitative |
| q-0130-1 | `[0130]` | "each of the processing devices A0-A7 may communicate with each of the other processing devices A0-A7 using at most two communication hops via a first communication channel with a first processing device and a separate communication channel between the first processing device and a second processing device" | mechanism-critical |
| q-0130-2 | `[0130]` | "Not having every one of the processing devices A0-A7 communicate with each of the other processing devices A0-A7 with a direct communication channel may reduce a number of connections between the processing devices A0-A7 as compared to a point-to-point connection scheme where every processing device is coupled to every other processing device." | prior-art-contrast |
| q-0133-1 | `[0133]` | "each of the processing devices A0-A7 may be formed on a separate die of a silicon process" | mechanism-critical |
| q-0134-1 | `[0134]` | "the communication channels between the processing devices A0-A7 may be wired communication channels such as a peripheral component interconnect express (PCIe), a serial peripheral interface (SPI), ethernet, universal chiplet interconnect express channels (UCIe), or some other wired communication channel and/or optical channel" | mechanism-critical |
| q-0140-1 | `[0140]` | "the first operation may be a data gather operation and the second operation may be a data reduction operation" | claim-supporting |
| q-0140-2 | `[0140]` | "During the second operation, data may only be transmitted between the processing devices A0-A7 using the second communication channels 740 and not the first communication channels 730 ." | claim-supporting |
| q-0142-1 | `[0142]` | "in the event that the first and second operations are being performed during overlapping time periods, the processing devices A0-A7 may receive and/or transmit data for both operations during overlapping time periods" | claim-supporting |
| q-0143-1 | `[0143]` | "The second processing device A1 may send the received data to the third processing device A2 before all the data from the first processing device A0 is received." | mechanism-critical |
| q-0168-1 | `[0168]` | "the same amount of data may be shared by each of the processing devices A0-A7 and a same amount of data may be shared across each of the second communication channels 740 ." | mechanism-critical |
| q-0250-1 | `[0250]` | "the tensor parallelism may allow computational operations of an AI model to be split across multiple processing devices in a manner that may reduce a processing time or a data bandwidth for a given processing time" | claim-supporting |
| q-0251-1 | `[0251]` | "The AI model 900 may be representative of a large language model or a transformer decoder." | mechanism-critical |
| q-0258-1 | `[0258]` | "the MLP calculations may result in computations that are four times greater than other computations performed by the AI model 900 ." | quantitative |
| q-0267-1 | `[0267]` | "the operations performed by the self-attention layer 915 may be performed on the individual tiles of the self-attention tensors Q, K, and V and intermediate tensors by different ones of the processing devices without rejoining the tiles of the self-attention tensors Q, K, and V on a single processing device" | mechanism-critical |
| q-0278-1 | `[0278]` | "the tensors used during the decoding layers 905 may remain split and distributed among the processing devices such that no one processing device may include the entirety of a tensor during the tensor operations performed by the decoding layers 905 ." | mechanism-critical |
| q-0313-1 | `[0313]` | "Typically, in transformer models the number of elements involved in a computation for inferring the next token is equal to a depth of the transformer model." | prior-art-contrast |
| q-0313-2 | `[0313]` | "during the feedforward operation, the number of elements involved in a specific computation may be four times the depth of the transformer model" | quantitative |
| q-0385-1 | `[0385]` | "a plurality of processing devices separated into a first set of two or more of the plurality of processing devices and a second set of two or more of the plurality of processing devices" | claim-supporting |
| q-0386-1 | `[0386]` | "a plurality of communication channels to directly communicatively couple every processing device in the first set of the plurality of processing devices with every processing device in the second set of the plurality of processing devices without communicatively coupling any of the plurality of processing devices in the same set of the plurality of processing devices" | claim-supporting |
| q-0387-1 | `[0387]` | "wherein the plurality of processing devices are configured such that each of the plurality of processing devices is able to communicate with any of the other of the plurality of processing devices through at most one other of the plurality of processing devices." | claim-supporting |

> Note: `[0385]`-`[0387]` are the spec's numbered Example 2.1, whose wording is identical
> to granted claim 1 EXCEPT that claim 1 (and claim 14) require "four or more" devices per
> set where `[0385]` says "two or more". q-0386-1 and q-0387-1 appear verbatim in claim 1;
> q-0385-1 exists only in the description/abstract framing. Phase 2 must pair q-0385-1
> with the narrowing note whenever it is used (see phase2-handoff-notes.md §d).
> Note: `[0123]` contains the source typo "for case of illustration" (likely "ease");
> `[0032]` contains "any other one of the one of the processing devices"; preserved
> verbatim above.

## Timeline

- **Filing date**: 2024-10-22
- **Publication date**: 2025-07-15 (grant)
- **Examination period**: 266 days (computed: grant date minus filing date; unusually fast
  for the art unit - present as computed metadata, not a quote)
- **Prior-art chronology**:
  | Citation | Filing date | Publication date | Days relative to subject filing |
  |---|---|---|---|
  | (none - the provided patent.md text contains no references-cited list and the Background cites no specific documents) | — | — | — |

Family context (external facts, from fact-check-log `etched-family-trio-wips`): filed
2024-10-22 alongside US 12,306,903 B1 ("Performance of tensor operations", granted
2025-05-20) and US 12,361,262 B1 ("Tensor operations in AI models", granted 2025-07-15),
same sole inventor; each of the trio carries a PCT filing (WO 2026/090208, 090209, 090210)
and a US continuation published 2026 (US 2026-0111513 / 0111514 / 0111709 A1). Expected
expiry 2044-10-22; small-entity status on filing.

## Prior-art references + differentiation

- **No patent or literature citations appear in the provided patent.md text.** The
  Background (`[0002]`-`[0003]`) describes tensor parallelism generically and cites no
  documents. Differentiation therefore runs against the practice alternatives the
  description itself names:
- **Networking/data switch** (named at `[0026]`, `[0032]`): enables any-to-any sharing but
  "may be expensive to include in a system that performs tensor operations" `[0026]`. The
  invention replaces the switch with fixed direct channels while keeping any-to-any
  reachability through at most one intermediate device `[0387]`.
- **Full point-to-point scheme** (named at `[0130]`): every device wired to every other.
  The invention cuts the connection count by wiring only cross-set pairs `[0130]` (q-0130-2)
  at the cost of two-hop paths within a set, softened by relay-before-complete forwarding
  `[0143]`.
- Patent-internal corroboration of the family division of labor: this patent's spec
  enumerates three example families (`[0336]`+) - Example 1 (methods of tensor operations),
  Example 2 (tensor parallel group topology), Example 3 (AI-model computations) - but its
  GRANTED claims track only Example 2. The method and AI-model families match the granted
  claims of same-day siblings US 12,306,903 B1 and US 12,361,262 B1 (external fact,
  fact-check-log `etched-family-trio-wips`).

## 유리한 효과 + 정량 데이터

The fixed topology reduces data sharing between devices and thereby processing time
`[0124]`, `[0026]`; it reduces the number of physical connections relative to a full
point-to-point mesh `[0130]`; equal tile splits make every device and every channel carry
the same amount of data during collectives (no hot link) `[0168]`, `[0178]`, `[0231]`;
reduce and gather traffic can run at the same time on disjoint channel families `[0142]`,
claim 9; and for AI models the split cuts processing time or the bandwidth needed for a
given processing time `[0250]`. The tensor-preparation math behind the topology minimizes
the maximum per-link transfer bandwidth `[0060]`-`[0061]`.

**Quotable spans:**
- `[0124]`: "the fixed topology as illustrated in FIGS. 7 A and 7 B and described in this disclosure may be used to reduce data sharing between the processing devices A0-A7 and thereby help to reduce a processing time for the tensor operations performed by a tensor parallel group 700 ."
- `[0130]`: "Not having every one of the processing devices A0-A7 communicate with each of the other processing devices A0-A7 with a direct communication channel may reduce a number of connections between the processing devices A0-A7 as compared to a point-to-point connection scheme where every processing device is coupled to every other processing device."
- `[0168]`: "the same amount of data may be shared by each of the processing devices A0-A7 and a same amount of data may be shared across each of the second communication channels 740 ."
- `[0250]`: "the tensor parallelism may allow computational operations of an AI model to be split across multiple processing devices in a manner that may reduce a processing time or a data bandwidth for a given processing time"
- `[0061]`: "When the number of processing devices is 8, p=4.35235, q=1.83809."

| Metric | Value | Paragraph |
|---|---|---|
| Minimum devices under claims 1/14 | 4 + 4 = 8 total ("four or more" per set) | claims 1, 14 |
| Worst-case communication path | at most 1 intermediate device (= 2 channel hops) | `[0130]`, `[0387]` |
| Channels per device (8-device topology) | 4 | `[0129]` |
| Bandwidth-optimal split, n=8 | p=4.35235, q=1.83809; rounded to divisors p=4, q=2 | `[0061]` |
| Channel link count, 8 devices | 16 cross-set channels vs 28 full-mesh (DERIVED from FIG. 7C / claim 1; not stated in the patent - do not cite as patent text) | (derived) |
| MLP computation scale | 4x other computations; weight tensors 4x model depth | `[0258]`, `[0313]` |
| Channel reuse, worked example | each channel used 2x (first reduce/gather), 4x (second reduce/gather), balanced both directions | `[0168]`, `[0178]`, `[0231]`, `[0243]` |
| Model depth example | 12,288 dimensions (= 3 x 2^12) | `[0251]`, `[0121]` |
| Exam period | 266 days filing-to-grant (computed) | metadata |
