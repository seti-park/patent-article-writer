# Self-audit round 2, reader B: skeptical pro-subject reader

- **Persona:** AI-infrastructure practitioner (tensor parallelism, NVSwitch-class fabrics,
  Megatron sharding, systolic arrays). Hunting technical overclaim AND unearned hedging.
- **Read (blind protocol honored):** `handoff/03-edit/essay-final.md`,
  `input/patent.md` (full CLAIMS section read directly), `input/essay-context.md`,
  figures `input/figures/fig-07A.png`, `fig-07B.png`, `fig-07C.png`. No edit logs, no
  revision artifacts, no other self-audit reports.
- **Finding ids:** sa2B-F*.

## 1. BLUF

**Verdict: yes.** Paragraph 1 lands a declarative two-sided verdict, not a deferred
question: "Half of the loudest architecture claim in the thread already has a granted US
patent standing behind it. The other half, the shared memory pool that gives Cluster-Scale
Memory its name, has no granted substance in the filings you can read today."

## 2. Headers-as-claims

All seven `##` headers are assertions and a header-only skim reconstructs the argument
(checkable half -> structure patent being extended -> any-to-any without a switch -> lane
scheduling -> transformer aim lives in the description -> no latency number, no memory
claim -> one leg substantiated, one absent).

One header runs a notch hotter than its section: "The Wiring Schedules the Traffic". The
section itself attributes the scheduling to claim language ("claim 8 binds the data
transfer for each sub-operation exclusively to one channel subset"), and the essay's own
steelman later prices exactly this as "a firmware choice". Wiring enables; the claimed
configuration schedules. See sa2B-F5 (nano).

## 3. Steelman

**Verdict: present, THIS-patent, conceded at full strength, then refined.** Quoted
concession: "Claim 1 recites a wiring pattern and nothing else. The description says the
channels realizing it can be PCIe, SPI, ethernet, UCIe, or other wired or optical links
[0134] ... No granted claim recites a latency figure or a bandwidth magnitude, and claim 5
requires equal bandwidth across channels, not high bandwidth ... A topology-only claim over
standard link technologies is a thin moat for a 'proprietary ultra-low-latency,
high-bandwidth interconnect'." That is not a generic patent truism; it is built from claim
5, [0134], and the thread's load-bearing adjective. The refinement ("Structure is what an
apparatus claim can lock...") answers it rather than deflecting.

**It misses a stronger variant.** See sa2B-F1 (medium): the negative limitation in claims
1/14 ("without communicatively coupling any of the plurality of processing devices in the
same set") is itself the cheapest literal design-around: copy the cross-set web AND add
intra-set links, and claims 1/14 are arguably not met, while claim 18 (which tolerates
intra-set wires) hangs on a declinable configured-to scheduling wherein. The essay's
conceded escapes (switch rack, firmware scheduling) are the weaker "don't copy" class;
"copy-and-add-wires" is unnamed, and the essay lists "cross-set-only direct channels
[0386]" purely on the fence-strength side of the ledger.

## 4. Technical-claim audit (against the CLAIMS text, lines 933-977 of input/patent.md)

| Item | Essay statement | Claims text | Verdict |
|---|---|---|---|
| Four-or-more floor | "Split the group's chips into two sets, four or more a side under the granted claim." / "granted claims 1 and 14 require four or more per set" | Claim 1: "a first set of four or more ... and a second set of four or more"; claim 14 identical inside each group | **HOLDS** |
| Spec-vs-claim narrowing | "The specification's summary covers two sets of 'two or more' devices [0385]" | [0385]: "a first set of two or more ... and a second set of two or more" | **HOLDS** (verbatim) |
| No intra-set coupling | Blockquote attributed "claim 1, [0386]" | Verbatim identical string appears in claim 1 and in [0386] | **HOLDS** |
| No intra-set coupling, lead altitude | "Its claims lock a wiring discipline ... nothing wired inside a set [0386]" (plural "claims") | Only claims 1/14 (+ dependent 19) carry the negative limitation; independent claim 18's scope tolerates intra-set wiring | **STRETCHES** (sa2B-F2, low) |
| At-most-one-intermediate | "through at most one other of the plurality of processing devices [0387]"; "two hops, one intermediate device, never more" | Claim 1 wherein clause, verbatim; [0130] "at most two communication hops" | **HOLDS** |
| Hop bound as extra fence | "A hop bound is [claimable], and claim 1 sets one" | True as recited, but the bound is mathematically entailed by the complete-bipartite channel limitation (cross-set pairs direct; same-set pairs share every opposite-set neighbor), so it adds no scope beyond [0386] | **STRETCHES** (evidence under sa2B-F1) |
| Claim 18 structure | "keeps the two-or-more floor but pays for it in structure: each set must contain two device groups, wired in at least the dual-family pattern of FIGS. 7A and 7B, with each sub-operation's traffic confined to its own family" | Claim 18: two-or-more sets each including two groups; first channels g1-g3/g2-g4 (= [0138]/FIG. 7A), second channels g1-g4/g2-g3 (= [0139]/FIG. 7B); "data transfer for the first sub-operation occurs only via the plurality of first communication channels..." ("at least" is honest: comprising claim) | **HOLDS** |
| Absence claims | "None of its claims mention latency, a bandwidth magnitude, or memory." / "AI, transformers, and inference are absent from the claim language." | Scanned claims 1-23: no "latency", no "memory", no "AI"/"artificial intelligence"/"transformer"/"inference"; bandwidth appears only in claim 5 as "a same data bandwidth" | **HOLDS** |
| Claim 5 reading | "claim 5 requires equal bandwidth across channels, not high bandwidth" | Claim 5: "each of the plurality of communication channels is configured for a same data bandwidth" | **HOLDS** |
| Uniformity claims | "same number of chips, the same number of channels, and channels of the same bandwidth (claims 3 to 5)" | Claims 3, 4, 5 verbatim match that inventory | **HOLDS** |
| Channel-family claims | "claim 8 binds the data transfer for each sub-operation exclusively to one channel subset. Claim 11 names the pair ... Which physical family carries which is the description's worked example rather than a claim requirement, with gather traffic on the first channels and reduction traffic on the second [0140]" | Claim 8: "occurs only via the first subset ... only via the second subset"; claim 11: first = reduction, second = gather; [0140]: gather on 730, reduction on 740. Note claim 11's ordering is the FLIP of [0140]'s example, and claim 8's subsets carry no structural tie to the 730/740 patterns, so "not a claim requirement" is exactly right for claims 8/11 | **HOLDS** (correctly navigated trap) |
| Simultaneity | "Claim 9 has the two sub-operations running in overlapping time periods, one channel family carrying each [0142]" | Claim 9: "in overlapping time periods such that first data ... at the same time second data..." | **HOLDS** |
| Workload hooks | "The claims' only workload hooks are the systolic array (claim 7), matrix multiplication (claims 10 and 23), and the reduction and gather sub-operations (claims 11 and 23)" | Claim 7 systolic array; claims 10/23 matrix multiplication; claims 11/23 reduction/gather; nothing else workload-named in 1-23 | **HOLDS** |
| Three independents | "Three independents, three different trades of breadth for structure, and none of them mentions memory." | Independents are 1, 14, 18; 14 = claim-1 group at system plurality; 18 = 2+ floor + dual-family + exclusivity; none mentions memory | **HOLDS** |
| Design-around phrasing | "a rack that keeps its networking switch, the filing's own foil [0032], sits outside claim 1" | Claim 1 is a comprising claim: a rack with the claimed direct cross-set channels PLUS a switch still infringes; only switch-INSTEAD-of-direct-wiring builds sit outside | **STRETCHES** (sa2B-F3, low) |
| Scheduling as firmware | "the scheduling claims (8, 9, 11) bind only traffic routed the claimed way, a firmware choice" | Claims 8/9/11 are configured-to limitations on claim-1 hardware; a vendor can decline the configuration | **HOLDS** |
| Granted family = topology only | "the claims granted here track only the topology family" [0336],[0337],[0384],[0418] | Example 1 = methods, Example 2 = tensor parallel group (topology), Example 3 = AI-model computation; granted claims 1-23 are the Example-2 family (with the 4+ narrowing) | **HOLDS** |

## 5. Mechanism honesty

- 2-hop story: "a message between two set-mates rides through one chip of the opposite
  set: two hops, one intermediate device, never more" vs [0130] "at most two communication
  hops" and claim 1's wherein. **HOLDS.**
- Cut-through relay: "an intermediate chip may begin forwarding data before it has
  finished receiving it [0143]" vs [0143] "may send the received data ... before all the
  data ... is received". **HOLDS** (possibility framing preserved).
- Link counts: "16 channels, where wiring all pairs directly would take 28 (both counts
  read off the figure, not numbers the patent states)". K4,4 = 16 (verified on fig-07C:
  8 + 8 across FIGS. 7A/7B, none intra-column), C(8,2) = 28. Labeled as derived in body
  and footnote. **HOLDS.**
- p/q example: "When the number of processing devices is 8, p=4.35235, q=1.83809." [0061]
  verbatim; "Rounded to divisors, that is 4 and 2" vs [0061] "when n=8, p=4 and q=2";
  "the whole input matrix lives spread across four of the eight chips" vs [0061] "an
  entirety of the input matrix is found on 4 of the 8 processing devices". **HOLDS.**
  Pinned values presented as pinned, not as bounds.
- Balance: "the same amount of data may be shared by each of the processing devices A0-A7"
  verbatim in [0168]; equal-per-channel in [0168]/[0178]; essay correctly conditions it on
  "the split the description prescribes". **HOLDS.**
- Stated payoff kept inside the patent's own hedge: quotes "may be used to reduce data
  sharing ... and thereby help to reduce a processing time" [0124]. **HOLDS.**
- MLP pressure point: [0258] "four times greater than other computations" ("can run"
  preserves "may"); [0313] quote verbatim, incl. the bandwidth-or-time trade; [0121] MLP
  as group-sizing basis. **HOLDS.**

## 6. External-fact fencing

**NONE unfenced.** Company numbers arrive under a blanket attribution: "The thread's
claims are specific, and every number in them is the company's own account." ($1B+
contracts, $800m raised, A0, summer 2026 racks all inside that fence; "The company says
its first systems ship in summer 2026"; "The company says its math blocks run at under
half the voltage of typical AI chips.") Thread quotations match `input/essay-context.md`
verbatim and carry the quote-chain footnote. Bibliographic facts (dates, 23 claims/3
independent/16 figures, PCT + continuations, 2044 term, sole inventor) match the verified
patent-family facts in essay-context; "inside nine months" = 266 days, correct and
footnoted.

## 7. Grounding spot-checks (my picks)

1. [0061] p/q quote + divisor rounding + 4-of-8 input spread: **HOLDS** (verbatim + faithful).
2. [0140] exclusivity blockquote + gather-on-730/reduction-on-740 + "worked example rather
   than a claim requirement": **HOLDS**, and correctly resolves the claim-11 ordering flip.
3. [0278] blockquote ("the tensors used during the decoding layers 905 may remain split
   and distributed..."): **HOLDS**, verbatim to the character.
4. [0313] "four times the depth of the transformer model" quote + framing: **HOLDS**.
5. [0026] "which the filing calls 'expensive to include in a system that performs tensor
   operations'": **STRETCHES** (nano, sa2B-F4). Patent says "may be expensive to include";
   the lead-in drops the filing's own "may be", firming the foil one notch. Quoted span
   itself is a verbatim substring.
6. (bonus) fig-07C caption vs drawing: 710a right = a1/a3/a5/a7, 710b left = a0/a2/a4/a6,
   16 cross links, zero intra-column: **HOLDS**. fig-07A/7B captions match [0138]/[0139]
   patterns exactly.

## 8. Over-hedge symmetric check

**NONE.** Claim-locked facts are stated as locked: "Claim 1 makes that bound a
requirement"; "The exclusivity itself, though, is strict"; "Uniformity is claimed as
structure"; verdict leads with "the verdict is firm both ways" and closes "it holds."
The remaining "may"s are either the patent's own words inside quotes ([0124], [0140],
[0278]) or genuinely unknowable facts (18-month unpublished-application window: "the
visible record is a floor, not a census"), which is correct calibration, not hedging.
"The claims cannot say what Etched actually built. The racks can." converts the one
patents-vs-products caution into a falsifiable check rather than a safe harbor.

## Findings (ADD-only)

### sa2B-F1 — steelman misses its strongest variant (check 3/4) — severity: medium

- **Verdict:** yes (gap).
- **Evidence:** The refinement lists the negative limitation purely as fence strength:
  "The granted fence is not the adjective. It is the discipline underneath it:
  cross-set-only direct channels [0386], degree- and bandwidth-uniform links (claims 3 to
  5)..." The conceded escapes are only the "don't copy" class: "a rack that keeps its
  networking switch ... sits outside claim 1, and the scheduling claims (8, 9, 11) bind
  only traffic routed the claimed way, a firmware choice."
- **What's missing:** the copy-and-add class. Claims 1/14 require coupling cross-set pairs
  "without communicatively coupling any of the plurality of processing devices in the same
  set"; [0128] reads this at group level ("there are no direct communication channels
  between the processing devices in the first set"). A builder who copies the bipartite
  web and ADDS intra-set links (a superset fabric, which real scale-up racks routinely
  have) has a serious literal non-infringement position on claims 1/14, and claim 18,
  which tolerates intra-set wires, is avoidable by declining its configured-to exclusive
  scheduling. So the strongest THIS-patent objection is: the fence's most distinctive leg
  is a negative limitation, and negative limitations are avoided by addition, not only by
  omission. Supporting evidence of the same tilt: the essay counts the [0387] hop bound as
  a second fence element ("A hop bound is [claimable], and claim 1 sets one") when the
  bound is mathematically entailed by the [0386] wiring, adding no scope.
- **Jurisdiction-fenced recommendation:** labeled analysis or narrower characterization,
  not a verdict hedge. E.g., one clause in the steelman paragraph naming the superset
  design-around ("wire the web and add set-mate links and claims 1 and 14 arguably no
  longer read"), or cut "cross-set-only" from the fence-strength inventory and let claims
  3-5 + 8/9/11 carry it. The verdict sentence ("granted, checkable substance") survives
  unchanged; this prices the moat, it does not soften the call.

### sa2B-F2 — lead generalizes the no-intra-set lock across "claims" (check 4) — severity: low

- **Verdict:** yes.
- **Evidence:** "Its claims lock a wiring discipline for a group of chips: two sets, every
  cross-set pair directly wired, nothing wired inside a set [0386]." Independent claim 18
  does not carry the negative limitation (dependent 19 restores it); the essay's own later
  claim-18 sentence is accurate, so this is lead-altitude compression.
- **Recommendation (anchor/narrow):** "its lead claim locks" or "claims 1 and 14 lock".

### sa2B-F3 — switch design-around phrased as immunity (check 4) — severity: low

- **Verdict:** yes.
- **Evidence:** "a rack that keeps its networking switch, the filing's own foil [0032],
  sits outside claim 1". Claim 1 is open ("comprising"): a rack with the claimed direct
  cross-set channels plus a switch still infringes. Only a rack that routes through a
  switch instead of the direct web sits outside.
- **Recommendation (narrow):** "a rack that routes chip-to-chip traffic through a switch
  instead of the direct web sits outside claim 1."

### sa2B-F4 — [0026] foil de-hedged in attribution (check 7) — severity: nano

- **Verdict:** yes.
- **Evidence:** essay: "which the filing calls 'expensive to include in a system that
  performs tensor operations' [0026]"; patent: "may be expensive to include in a system
  that performs tensor operations."
- **Recommendation (anchor fix):** include "may be" in the quoted span or soften the
  attribution verb ("the filing warns can be expensive").

### sa2B-F5 — header 4 one notch above its section (check 2) — severity: nano

- **Verdict:** yes.
- **Evidence:** "## The Wiring Schedules the Traffic" vs the section's own accurate
  attribution ("claim 8 binds the data transfer...") and the steelman's later "a firmware
  choice". The wiring enables the schedule; the claimed configuration is what schedules.
- **Recommendation:** acceptable as-is; if touched, "The Wiring Gives Each Traffic Type
  Its Own Lanes" keeps the claim honest.

## 9. Persona verdict

Survives my quote-tweet: the claim quotes are verbatim, every scope call I checked
(four-or-more floor, [0385] contrast, claim-18 trade, claims 3-5/8/9/11, the
latency/memory/AI absences, the [0140]-vs-claim-11 flip) holds against the claims text,
derived arithmetic is labeled derived, and the two-way verdict is earned rather than
hedged. The one sentence I'd attack: "The granted fence is not the adjective. It is the
discipline underneath it: cross-set-only direct channels [0386]" -- because
"cross-set-only" is a negative limitation, which a competitor escapes by adding wires,
not just by omitting them, and the essay never prices that.

## Tally

- critical: 0
- high: 0
- medium: 1 (sa2B-F1)
- low: 2 (sa2B-F2, sa2B-F3)
- nano: 2 (sa2B-F4, sa2B-F5)
