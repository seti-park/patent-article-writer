# Self-audit round 1 — Reader A (impatient investor)

```yaml
reader: A
persona: impatient-investor (reader-profile tier; saw the Etched thread; 6 minutes; skims headers, reads captions first)
essay: handoff/03-edit/essay-final.md
patent: input/patent.md
context: input/essay-context.md
isolation: no edit-log / revision-response / score-history / other-reader output read
figures_inspected: input/figures/fig-07C.png (visual check of header caption)
```

---

## Item 1 — BLUF lead-altitude

```yaml
item: 1-bluf
verdict: yes (pass)
evidence: >
  Paragraph 1, sentences 2-3: "Half of the loudest architecture claim in the thread already
  has a granted US patent standing behind it. The other half, the shared memory pool that
  gives Cluster-Scale Memory its name, has no granted substance in the filings you can read
  today." The title also asserts the verdict: "Etched Patented the Wiring Half of Its Memory
  Story, Not the Memory."
severity: none
recommendation: none — verdict delivered before I could get impatient.
```

## Item 2 — Headers-as-claims

```yaml
item: 2-headers
verdict: yes (pass); filler header: NONE
evidence: >
  The seven ## headers, read alone, reconstruct the argument: "The Memory Story Has a
  Checkable Half" -> "A Structure Patent Etched Keeps Paying to Extend" -> "Every Chip
  Reaches Every Chip Without a Switch" -> "The Wiring Schedules the Traffic" -> "The
  Description Aims It at Transformer Decoding" -> "No Latency Number, No Memory Claim" ->
  "One Leg Substantiated, One Leg Absent". Every header is an assertion; the header-only
  skim already gives the split verdict. ("Sources"/"Footnotes" are functional apparatus.)
severity: none
recommendation: none
```

## Item 3 — Steelman present and patent-specific

```yaml
item: 3-steelman
verdict: yes (pass) — THIS-patent objection, conceded at full strength, then refined
evidence: >
  Concession: "The objection an informed reader should press lands at full strength. Claim 1
  recites a wiring pattern and nothing else. The description says the channels realizing it
  can be PCIe, SPI, ethernet, UCIe, or other wired or optical links [0134] ... No granted
  claim recites a latency figure or a bandwidth magnitude, and claim 5 requires equal
  bandwidth across channels, not high bandwidth ... A topology-only claim over standard link
  technologies is a thin moat for a 'proprietary ultra-low-latency, high-bandwidth
  interconnect'."
  Refinement: "Structure is what an apparatus claim can lock, and structure is exactly what
  this one locks." followed by the fence enumeration ([0386], claims 3-5, claims 8/9/11,
  hop bound [0387]).
  Grounding of the objection verified: [0134] lists exactly those link technologies
  (patent line 291); claim 5 = "a same data bandwidth" (patent line 941); no latency/
  bandwidth-magnitude/memory term appears in claims 1-23 (patent lines 933-977).
severity: none
recommendation: none — this is not the generic "patents don't guarantee products" truism;
  it is built from this patent's claim 1, claim 5, and [0134].
```

## Item 4 — Meta / scaffolding leakage

```yaml
item: 4-meta
verdict: finding (one instance)
evidence: >
  Verdict section, closing of paragraph 1: "The boundaries set out above scope that call.
  They do not soften it." These two sentences are about the essay's own argument apparatus
  ("set out above"), not about Etched or the patent, and read as a compliance assertion
  aimed at a reviewer. The firmness they announce is already demonstrated by the sentences
  around them.
severity: low
finding_id: sa1A-F4
recommendation: cut both sentences, or restate about the facts (e.g. the limits are
  boundaries on the finding, not counterweights) without the "set out above" self-reference.
```

## Item 5 — Jargon depth (first stopping term)

```yaml
item: 5-jargon
verdict: finding (first un-glossed term) + one near-bail paragraph
evidence_a: >
  Paragraph 2: "Out of stealth after taping out its A0 silicon." First jargon hit of the
  essay. "Taping out" and "A0 silicon" are fab terms of art the reader-profile does not
  grant; nothing glosses them. It did not stop me only because the Etched thread itself used
  the term.
severity_a: low
finding_id_a: sa1A-F5
recommendation_a: three-word gloss or plainer verb ("after finishing its first chip design,
  the A0").
evidence_b: >
  Section "The Wiring Schedules the Traffic": "The first communication channels (730) join
  group 712a with 712c and group 712b with 712d [0138]. The second communication channels
  (740) run the criss-cross: 712a with 712d, 712b with 712c [0139]." Six numeric labels in
  two sentences — the one paragraph that reads like the patent instead of the essay, and my
  closest bail point. The captions and "criss-cross" gloss rescue it; claim 18 later needs
  the groups, so the labels are not free to cut.
severity_b: low
finding_id_b: sa1A-F6
recommendation_b: keep 730/740 in the body and push the 712a-d pairings fully into the
  FIG. 7A/7B captions (which already carry them), or add a plain-words clause ("straight
  pairings" vs "criss-cross") before the labels.
other_terms_checked: >
  systolic array — glossed ("a grid of small processing elements that computes as data flows
  through it"); reduction/gather — glossed; K4,4 — labeled graph-theory aside; MLP — glossed;
  HBM/SRAM hybrid — glossed; PCIe/SPI/UCIe — collectively glossed ("the ordinary buses
  commodity hardware already uses"). No deep-dive past the insight anywhere: pass on the
  overdepth side.
```

## Item 6 — Stubs / promise-then-restate

```yaml
item: 6-stubs
verdict: NONE
evidence: >
  No section is markedly shorter than its siblings (shortest body section, "A Structure
  Patent Etched Keeps Paying to Extend", carries three full paragraphs of new prosecution
  facts). Each section advances: topology -> channel families/balance -> transformer target
  -> objection/boundaries -> verdict. No promise-then-restate pattern found.
severity: none
recommendation: none
```

## Item 7 — Grounding spot-checks (6 samples across sections + claim-scope + pinned values)

```yaml
item: 7-grounding-sample-1
section: "The Memory Story Has a Checkable Half"
essay_span: "two sets, every cross-set pair directly wired, nothing wired inside a set [0386]. Any chip can reach any other through at most one chip in between [0387]."
patent_span: >
  [0386] "...directly communicatively couple every processing device in the first set ...
  with every processing device in the second set ... without communicatively coupling any of
  the plurality of processing devices in the same set..."; [0387] "...able to communicate
  with any of the other of the plurality of processing devices through at most one other of
  the plurality of processing devices." Identical limitations appear verbatim in granted
  claim 1 (patent line 933).
verdict: HOLDS
```

```yaml
item: 7-grounding-sample-2
section: "Every Chip Reaches Every Chip Without a Switch"
essay_span: "large enough that processing of the tensors in a typical manner using a single processor may be difficult" [0021]
patent_span: "[0021] In some situations, tensors may be large enough that processing of the tensors in a typical manner using a single processor may be difficult."
verdict: HOLDS (verbatim)
```

```yaml
item: 7-grounding-sample-3
section: "The Wiring Schedules the Traffic"
essay_span: block quote "During the second operation, data may only be transmitted between the processing devices A0-A7 using the second communication channels 740 and not the first communication channels 730 ." [0140]
patent_span: "[0140] ... During the second operation, data may only be transmitted between the processing devices A0-A7 using the second communication channels 740 and not the first communication channels 730 ."
verdict: HOLDS (verbatim, including gather-on-first / reduction-on-second as the description's example: "the first operation may be a data gather operation and the second operation may be a data reduction operation")
```

```yaml
item: 7-grounding-sample-4
section: "The Wiring Schedules the Traffic" (balance)
essay_span: "When the number of processing devices is 8, p=4.35235, q=1.83809." [0061] + "the whole input matrix lives spread across four of the eight chips [0061]"
patent_span: "[0061] ... When the number of processing devices is 8, p=4.35235, q=1.83809. ... the input matrix may be split such that an entirety of the input matrix is found on 4 of the 8 processing devices..."
verdict: HOLDS (verbatim + faithful reading; also [0168]/[0178] "the same amount of data may be shared by each of the processing devices A0-A7" verbatim)
```

```yaml
item: 7-grounding-sample-5
section: "The Description Aims It at Transformer Decoding"
essay_span: "during the feedforward operation, the number of elements involved in a specific computation may be four times the depth of the transformer model" [0313]; block quote of [0278] ("...no one processing device may include the entirety of a tensor during the tensor operations performed by the decoding layers 905 .")
patent_span: "[0313]" and "[0278]" carry both spans verbatim (patent lines 649, 579); [0251] "The AI model 900 may be representative of a large language model or a transformer decoder." also verbatim.
verdict: HOLDS
```

```yaml
item: 7-grounding-sample-6
section: "No Latency Number, No Memory Claim"
essay_span: "PCIe, SPI, ethernet, UCIe, or other wired or optical links [0134]"; memory 630's role is to "provide tensors and other data to the tensor parallel groups 620 for processing" [0119]; "None of its claims mention latency, a bandwidth magnitude, or memory."
patent_span: >
  [0134] "...peripheral component interconnect express (PCIe), a serial peripheral interface
  (SPI), ethernet, universal chiplet interconnect express channels (UCIe), or some other
  wired communication channel and/or optical channel."; [0119] "The memory packages may be
  configured to provide tensors and other data to the tensor parallel groups 620 for
  processing."; grep of the CLAIMS section (patent lines 931-977) returns no "memory" or
  "latency" token.
verdict: HOLDS
```

```yaml
item: 7-claim-scope-and-pinned
checks:
  - "claims 1 and 14 require four or more per set" vs claim 1/14 text "a first set of four
    or more ... and a second set of four or more" (patent lines 933, 959): HOLDS
  - "The specification's summary covers two sets of 'two or more' devices [0385]" vs [0385]
    "a first set of two or more ... and a second set of two or more" (and ## SUMMARY [0004]
    matches): HOLDS — locked narrowing honored, description framing never credited to the
    granted claims
  - claim 18 characterization (two-or-more floor, two groups per set, dual channel families,
    per-family traffic confinement) vs claim 18 (patent line 967): HOLDS
  - pinned values not stated as bounds: "The description works the optimum once:
    'When the number of processing devices is 8, p=4.35235, q=1.83809.'" — presented as the
    worked example, not a bound: HOLDS; eight-chip case kept as "the drawings' eight-chip
    example", not a claim requirement: HOLDS; 16-vs-28 channel count labeled derived in body
    and footnote: HOLDS
  - header caption vs figure: "first set 710a (a1, a3, a5, a7) on the right and the second
    set 710b (a0, a2, a4, a6) on the left" — verified against input/figures/fig-07C.png and
    [0126]: HOLDS
verdict: HOLDS
```

```yaml
item: 7-grounding-stretch-1
section: "Every Chip Reaches Every Chip Without a Switch"
essay_span: "a point-to-point scheme whose connection count balloons as the group grows [0130]"
patent_span: "[0130] ... may reduce a number of connections between the processing devices A0-A7 as compared to a point-to-point connection scheme where every processing device is coupled to every other processing device."
verdict: STRETCHES — [0130] states the comparison, not growth dynamics; "balloons as the
  group grows" is derived arithmetic (true, but unlabeled in-body; the derived-counts
  footnote covers only the 16-vs-28 figure count)
severity: low
finding_id: sa1A-F2
recommendation: narrow to what [0130] states ("a scheme the patent says needs more
  connections") or fold the growth claim into the derived-counts footnote. (Jurisdiction
  fence: fix is narrow/label, not hedge.)
```

```yaml
item: 7-grounding-stretch-2
section: "The Description Aims It at Transformer Decoding"
essay_span: "The description sizes the tensor parallel group around exactly that operation [0121]."
patent_span: >
  [0121] "Alternately or additionally, the size of the tensor parallel groups 620 may be
  based on the largest computation that may be performed by the AI model. For example, the
  size of the tensor parallel groups 620 may be based on the computations performed by the
  feedforward operations performed by a MLP layer of an AI model. As another example, the
  size ... may be selected to be a sub-multiple of the size of the tensor..." — one
  may/for-example option among several ([0120] offers depth-based sizing as well).
verdict: STRETCHES — an optional description embodiment is stated as the description's
  definite practice ("sizes ... around exactly"), and the sentence is load-bearing for the
  section header's "Aims It at". The section's verdict survives without it ([0251], [0258],
  [0313], [0278] all HOLD), so this is a one-verb repair, not a thesis problem.
severity: medium
finding_id: sa1A-F1
recommendation: narrow the verb to match the source: e.g. "The description offers exactly
  that operation as a basis for sizing the tensor parallel group [0121]" or "may be sized
  around exactly that operation [0121]". (Fix = narrow; do not hedge the section verdict.)
```

```yaml
item: 7-anchor-precision
section: "The Description Aims It at Transformer Decoding" (opening sentence)
essay_span: "Its decoding layers, the loop that infers one token at a time [0313], run normalization, then self-attention (QKV generation and attention computation), then projection, then an MLP [0252]."
patent_span: >
  The "loop" (repetition per token) lives at [0259] "the decoding layers 905 may be
  repeated ... multiple times for a single token"; [0313] supports only "inferring the next
  token". The parenthetical "(QKV generation and attention computation)" lives at [0254]
  (QKV generation 916, attention computation 918); [0252] lists the four layers only.
verdict: STRETCHES (anchor placement, content itself accurate and present in adjacent
  cited-elsewhere paragraphs)
severity: low
finding_id: sa1A-F3
recommendation: anchor fix — cite [0259] (or [0252]) for the loop clause and add [0254]
  beside [0252] for the parenthetical.
```

## Item 8 — Persona verdict (impatient investor)

```yaml
item: 8-persona
stopped_reading: no
nearest_bail_point: >
  "The first communication channels (730) join group 712a with 712c and group 712b with
  712d [0138]." — two sentences of label arithmetic; I skimmed to the next paragraph and the
  "two kinds of traffic never share a wire" line pulled me back.
question_left_unanswered: >
  Design-around cost: the essay shows me the fence's shape but never what it costs a rival
  to walk around it — if a competitor wires the same racks through a switch, or adds one
  intra-set link, does claim 1 still reach them, and would dodging it cost them the wire
  savings the shape exists for? One sentence in "No Latency Number, No Memory Claim" or the
  verdict would close the money thread.
finding_id: sa1A-F7
severity: low
would_share: yes
reason: >
  It hands me a checkable, non-hype take with a concrete future test — "the wiring either
  matches claim 1's cross-set pattern [0386] or it does not" is exactly the line I would
  quote-post over the Etched thread.
additional_consistency_note:
  finding_id: sa1A-F8
  severity: low
  evidence: >
    Lede paragraph 4: "Its claims lock a wiring discipline for a group of AI chips" vs
    section 5: "None of this is claimed for AI. ... AI, transformers, and inference are
    absent from the claim language." The lede's "AI chips" is audience shorthand the essay
    itself later disclaims; a careful reader registers it as a small self-contradiction on
    claim scope.
  recommendation: drop "AI" in the lede ("a group of chips") — the Etched context already
    supplies the AI framing.
thesis_restatement_check:
  finding_id: sa1A-F9
  severity: low
  evidence: >
    The memory-absent half of the verdict is punched in four sections plus the title:
    S1 "has no granted substance in the filings you can read today"; S5 "It does not claim
    the store."; S6 "Described, never claimed."; S7 "The memory-pool leg has no substance in
    this filing" — against the pass condition of <= 3 sections. Each instance rides new
    evidence, so it reads as cadence rather than padding; the only place I felt it was the
    verdict recap re-citing four already-used anchors ([0387], [0142], [0168], [0124]) in
    three sentences.
  recommendation: if revising for other findings, let S5's "It does not claim the store."
    or S6's "Described, never claimed." carry the beat alone; no standalone revision needed.
```

## Item 9 — Over-hedge symmetric check (6G)

```yaml
item: 9-overhedge
verdict: NONE
evidence: >
  The verdict leads with the call: "Hold the thread against the grant and the verdict is
  firm both ways." No safe-harbor boilerplate anywhere (no "patents don't guarantee
  products"-class sentence in the essay). The single sanctioned caution (LVI/18-month
  publication window) is stated once as a boundary and ends firm: "Later filings may yet
  cover LVI. Nothing readable today does." Final line is a claim, not a qualifier: "The
  wiring half is the one you can check today, and it holds." Reverse-6G: the conclusion is
  not safer than the body — the body proves exactly the substantiated/absent split the
  close asserts.
severity: none
recommendation: none
```

---

## Summary

```yaml
findings:
  - {id: sa1A-F1, severity: medium, check: grounding (item 7), issue: "[0121] optional sizing embodiment stated as definite ('sizes ... around exactly that operation'); fix = narrow the verb"}
  - {id: sa1A-F2, severity: low, check: grounding (item 7), issue: "[0130] 'connection count balloons as the group grows' — growth dynamics not in the cited paragraph; label as derived or narrow"}
  - {id: sa1A-F3, severity: low, check: grounding (item 7), issue: "anchor precision in S5 opening sentence: loop clause belongs to [0259], QKV/attention parenthetical to [0254]"}
  - {id: sa1A-F4, severity: low, check: meta (item 4), issue: "essay-self-reference in verdict: 'The boundaries set out above scope that call. They do not soften it.'"}
  - {id: sa1A-F5, severity: low, check: jargon (item 5), issue: "un-glossed 'taping out its A0 silicon' in paragraph 2"}
  - {id: sa1A-F6, severity: low, check: jargon/readability (item 5), issue: "712a-d label-soup paragraph is the persona's nearest bail point"}
  - {id: sa1A-F7, severity: low, check: persona (item 8), issue: "design-around cost of the claim-1 fence never addressed — the investor's residual question"}
  - {id: sa1A-F8, severity: low, check: consistency (item 8), issue: "lede 'a group of AI chips' vs S5 'AI ... absent from the claim language'"}
  - {id: sa1A-F9, severity: low, check: thesis restatement (item 8/pass-7 #7), issue: "memory-absent verdict asserted in 4 sections + title (pass condition <= 3); cadence, not padding"}
counts: {critical: 0, high: 0, medium: 1, low: 8}
grounding_samples: {holds: 6-of-6 formal samples plus claim-scope/pinned/figure checks, stretches: 3 (F1, F2, F3), breaks: 0}
hard_gate_relevant: none (no grounding high/critical; no over-hedge; steelman present and patent-specific)
persona_verdict: >
  I got the answer in paragraph one, stayed through the label-soup paragraph, and left with
  one unanswered money question (design-around). I would share it for the "check the racks
  against the diagram" hook. The essay's verdict is proportionate in both directions —
  nothing here relaxes any gate; the medium finding is a one-verb narrowing.
```
