# Figure Rationale

## FIG. 7C — The whole claimed topology in one image (header / cover candidate)

- **Purpose**: Overlays both channel families (730 + 740) on the eight devices a0-a7,
  showing claim 1's core as drawn: every device in set 710a directly wired to every device
  in set 710b, no wire inside a set `[0125]`, q-0386-1. This is the granted structure
  itself, not an embodiment flourish.
- **Intended effect**: Instant visual thesis - the reader sees "a dense, deliberate web
  with no switch box in the middle" before reading a word of claim language. As the 5:2
  header it also carries the essay's identity: the story is a wiring diagram, and here is
  the wiring diagram.

## FIG. 7A — First channel family (730)

- **Purpose**: Isolates the first communication channels: group 712a↔712c and
  712b↔712d, each a complete two-by-two cross-wiring `[0138]`. One of the two exclusive
  traffic lanes of claims 8/18; the description's gather lane `[0140]`.
- **Intended effect**: Makes "the channels are separated into two subsets" concrete -
  the reader sees that half the web is a clean, regular pattern, setting up the
  simultaneity point (claim 9) when 7B adds the other half. (Adjacent placement with 7B
  in section 4-traffic; the pair reads as one argument.)

## FIG. 7B — Second channel family (740)

- **Purpose**: The complementary criss-cross: 712a↔712d and 712b↔712c `[0139]` - the
  description's reduction lane `[0140]`, q-0140-2.
- **Intended effect**: Completes the decomposition: 7A + 7B visibly sum to 7C, which is
  the figure-level proof of the claim-18 structure and of why reduce and gather traffic
  never contend for the same wire (claims 8/9/11). The reader gets the "two disjoint rail
  systems" idea from the pictures alone.

## FIG. 1 — Inside one tensor parallel group

- **Purpose**: Shows the unit of the story: four processing devices 110a-110d, each with
  a systolic array 112 of processing elements 114, forming a group systolic array 120
  `[0028]`, `[0029]` - the "chips" the topology wires, and claim 7's systolic-array
  limitation.
- **Intended effect**: Grounds the vocabulary cheaply so section 3's wiring discussion
  can move fast; prose fully covers the content (caption_role:
  body_figure_prose_covers_fully), the figure exists so the reader never wonders what a
  "processing device" is.

## FIG. 6 — Where memory sits (the boundary exhibit)

- **Purpose**: The environment view: host 602 beside a processing system 610 containing
  two tensor parallel groups 620a/620b and a memory 630 block `[0112]`, `[0119]`. This is
  the ONLY memory in the patent - a supporting box in one embodiment figure, absent from
  every claim.
- **Intended effect**: Carries the memory-leg half of the verdict visually: the reader
  sees that "memory" here is a labeled rectangle feeding the groups, not a claimed
  cluster-scale pool. Section 6 points at this figure when it states what the filing does
  NOT substantiate. (caption_role: body_figure_carries_unique_info - the caption should
  name memory 630 as described-not-claimed.)

## FIG. 9A — The workload the wiring is shaped for

- **Purpose**: The AI model 900's decoding layers 905: normalization 910, self-attention
  915 (QKV generation 916, attention computation 918), projection 920, MLP 925, then
  decoding 930 `[0251]`, `[0252]` - the transformer-decoder loop whose tensor operations
  the description maps onto the topology (`[0262]`-`[0278]`).
- **Intended effect**: Connects the abstract wiring to the thing readers care about (LLM
  inference) while keeping the claim-scope line clean: this mapping lives in the
  description, and the caption/prose must present it as the patent's intended workload,
  not a claim limitation. Prose covers the layer walk-through; the figure anchors the
  names (caption_role: body_figure_prose_covers_fully).

## Not selected (rationale recorded for audit)

- **FIG. 9B**: equation-level restatement of 9A (T1×WQ=Q, Softmax(Q×K^T)V, P×WH=I,
  I×WO=O) - notation above the reader profile; pair-break intentional, flagged in
  phase2-handoff-notes.md.
- **FIG. 2**: tensor-into-tiles split - one sentence of prose does the same work.
- **FIG. 3 / 4 / 5 / 8 / 10 / 11 / 12**: method-flowchart family; tile-movement mechanics
  are the sibling patents' territory per essay-context (one context paragraph only).
  FIG. 8's worked example survives in prose via the balanced-channel anchors (`[0168]`,
  `[0231]`).
- **FIG. 13**: generic computer-system boilerplate; no thesis point.
