# Self-Audit Grounding Verification — Round 2 (independent, blind)

Draft under review: `handoff/03-edit/essay-final.md` (draft_version 3, accepted).
Inputs: `handoff/01-design/invention-summary.md`, `input/patent.md` ([0001]-[0453] + CLAIMS,
read in full), `handoff/01-design/fact-check-log.md`, `input/essay-context.md`,
`input/figures/figures-manifest.md`. This pass did not read edit-log*, revision-notes.md,
score-history.md, or any selfaudit-round-1/round-2-readerA/readerB file — independent table,
mechanical fidelity only. Tone, hedging, structure, and the verdict's stance are out of
jurisdiction and are not commented on below.

## 1. Mechanical gate output

```
$ python .claude/skills/_shared/scripts/gate_quotes.py handoff/03-edit/essay-final.md \
    --invention-summary handoff/01-design/invention-summary.md --patent input/patent.md
[PASS] gate=quotes
  (no findings)

$ python .claude/skills/_shared/scripts/gate_anchors.py handoff/03-edit/essay-final.md \
    --invention-summary handoff/01-design/invention-summary.md \
    --figures handoff/01-design/figures-index.txt
[PASS] gate=anchors
  (no findings)
```

Both mechanical gates pass clean with zero findings. Every direct-quote span in the draft
verbatim-matches `input/patent.md`, and every `[dddd]` anchor chains back through
invention-summary to a real patent paragraph. The tables below are the human layer on top:
did the prose around each anchor assert only what the anchor supports, and are the
claim-scope / external-fact / figure-caption cross-checks clean.

Anchor-token census: 73 `[dddd]` occurrences in the draft body, collapsing to 53 distinct
anchored sentences/clauses (several sentences carry 2-4 anchors; both blockquote citations
and all 6 placed figure captions carry anchors and are included below).

---

## 2. Main fidelity table — every `[dddd]`-anchored sentence

Verdict key: SUPPORTED / UNSUPPORTED / MISREAD / OVERREACHED-BEYOND-ANCHOR.

| seq | section | sentence (claim-bearing clause) | anchors | patent-paragraph check (operative words) | verdict | note |
|---|---|---|---|---|---|---|
| 1 | Header caption (FIG.7C) | "the first set 710a (a1, a3, a5, a7) on the right and the second set 710b (a0, a2, a4, a6) on the left" | [0126] | [0126]: "Half of the processing devices A0-A7 are in the first set... namely A1, A3, A5, and A7 and the other half...in the second set...namely A0, A2, A4, and A6." | SUPPORTED | Device lists match exactly; left/right is a direct visual read of the figure, permissible in a caption. |
| 2 | Header caption | "Every chip in one column is wired straight to every chip in the other...and no wire runs inside a column" | [0128], [0129] | [0128]: "there are no direct communication channels between the processing devices in the first set...and no direct...in the second set." [0129]: "each processing device in the first set...may be directly connected to each of the processing devices in the second set...via a different communication channel." | SUPPORTED | "16 channels...counted off the drawing" is self-flagged as non-patent arithmetic (matches footnote `[^derived-counts]`); 4×4=16 checks out. |
| 3 | Header caption | "Both channel families (730, 740) are overlaid here" | [0125] | [0125]: "FIG. 7C illustrates all connections between the processing devices A0-A7...in a single figure." | SUPPORTED | |
| 4 | S1 Checkable Half | "Its claims lock a wiring discipline...two sets, every cross-set pair directly wired, nothing wired inside a set" | [0386] | [0386]/claim 1: "a plurality of communication channels to directly communicatively couple every processing device in the first set...with every processing device in the second set...without communicatively coupling any...in the same set." | SUPPORTED | |
| 5 | S1 Checkable Half | "Any chip can reach any other through at most one chip in between" | [0387] | [0387]/claim 1: "each...is able to communicate with any of the other...through at most one other of the plurality of processing devices." | SUPPORTED | |
| 6 | S2 Structure Patent | "The specification enumerates three example families, methods, topology, and AI-model computation...and the claims granted here track only the topology family" | [0336], [0337], [0384], [0418] | [0336]: numbered-example convention. [0337]: "Example 1 may include method of performing tensor operations." [0384]: "Example 2 may include a tensor parallel group." [0418]: "Example 3 may include method of performing computations for artificial intelligence models." | SUPPORTED | Exact match to invention-summary's own "claims-vs-narrative-split" evidence citations `[0385]`,`[0119]`,`[0336]` note; confirmed by independently scanning claims 1-23 (none recite Example-1/3-style generic method or AI-model steps). |
| 7 | S3 Every Chip Reaches | "Tensors...can be 'large enough that processing of the tensors in a typical manner using a single processor may be difficult'" | [0021] | [0021] verbatim: "tensors may be large enough that processing of the tensors in a typical manner using a single processor may be difficult." | SUPPORTED | Quote gate already verifies verbatim; independently re-confirmed. |
| 8 | S3 Every Chip Reaches | "Mid-computation, the chips must combine partial results into one (a reduction) and hand out copies of pieces (a gather) to keep going" | [0036] | [0036]: "data sharing between the processing device 110 may include a data reduction process and/or a data gather process." (Does not itself define which does what.) | SUPPORTED | See finding sa2G-F1 — [0036] names the two processes but the "combine sub-results" / "copy data" definitions sit at [0037]/[0039]. Content is true and verified there; anchor could be tighter. |
| 9 | S3 Every Chip Reaches | "Route everything through a networking switch that lets any chip talk to any chip, which the filing calls 'expensive to include in a system that performs tensor operations'" | [0032], [0026] | [0032]: "coupled together using a networking switch that enables communication between any one...with any other." [0026] verbatim: "expensive to include in a system that performs tensor operations." | SUPPORTED | Invention-summary itself treats [0026]'s "data switch" and [0032]'s "networking switch" as the same referent (Layer 3); consistent usage. |
| 10 | S3 Every Chip Reaches | "Or wire every chip to every other chip, a point-to-point scheme whose connection count balloons as the group grows" | [0130] | [0130]: "...as compared to a point-to-point connection scheme where every processing device is coupled to every other processing device." | SUPPORTED | "Balloons as group grows" is an accurate gloss of full-mesh quadratic scaling, not a patent-stated number; no magnitude asserted here. |
| 11 | S3 Every Chip Reaches | "In the drawings' eight-chip example, the odd-numbered chips form the first set (710a) and the even-numbered chips the second (710b)" | [0126] | [0126]: first set 710a = A1,A3,A5,A7 (odd); second set 710b = A0,A2,A4,A6 (even). | SUPPORTED | |
| 12 | S3 Every Chip Reaches (blockquote) | "a plurality of communication channels to directly communicatively couple every processing device in the first set...through at most one other of the plurality of processing devices" [cut at "same set" clause] — labeled "claim 1, [0386]" | [0386] | Verified by direct grep: identical substring in both `input/patent.md` claim 1 text and paragraph [0386]. | SUPPORTED | Verbatim confirmed independently (see §5 below); dual-sourced correctly (spec Example 2.1 text is word-for-word identical to claim 1's middle clause). |
| 13 | S3 Every Chip Reaches | "Chips in the same set have no direct channel between them, so a message between two set-mates rides through one chip of the opposite set: two hops, one intermediate device, never more" | [0128] | [0128]: "no direct communication channels between the processing devices in the first set...therebetween." (Two-hop mechanic itself is [0130]'s content.) | SUPPORTED | See finding sa2G-F2 — the "no direct channel" clause is squarely [0128]; the "two hops, one intermediate device" consequence is [0130]'s specific content (quoted elsewhere in this same essay, line 41/88), not re-cited here. |
| 14 | S3 Every Chip Reaches | "Claim 1 makes that bound a requirement...'through at most one other of the plurality of processing devices'" | [0387] | [0387] verbatim, quoted span exact. | SUPPORTED | |
| 15 | S3 Every Chip Reaches | "The relay need not even hold the message, since an intermediate chip may begin forwarding data before it has finished receiving it" | [0143] | [0143]: "The second processing device A1 may send the received data to the third processing device A2 before all the data from the first processing device A0 is received." | SUPPORTED | |
| 16 | S3 Every Chip Reaches | "the fixed topology 'may be used to reduce data sharing between the processing devices A0-A7 and thereby help to reduce a processing time'" | [0124] | [0124] verbatim (quote truncated before "for the tensor operations...", no meaning change). | SUPPORTED | |
| 17 | S4 Wiring Schedules Traffic | "Each set subdivides into two groups of chips, labeled 712a through 712d, and the channels split with them into two families" | [0135], [0136], [0138], [0139] | [0135]: groups 712a-712d named. [0136]: "each set...may include two or more of the groups...712a and 712b...formed from the first set...712c and [712]d...from the second set." | SUPPORTED | |
| 18 | S4 Wiring Schedules Traffic | "The first communication channels (730) pair the groups straight across, 712a with 712c and 712b with 712d" | [0138] | [0138]: "712a...directly communicatively coupled with each...of 712c via the first communication channels 730 and...712b...with...712d via the first communication channels 730." | SUPPORTED | |
| 19 | S4 Wiring Schedules Traffic | "The second communication channels (740) run the criss-cross: 712a with 712d, 712b with 712c" | [0139] | [0139]: "712a...coupled with...712d via the second communication channels 740 and...712b...with...712c via the second communication channels 740." | SUPPORTED | |
| 20 | S4 Wiring Schedules Traffic | "FIG. 7A and FIG. 7B draw one family each, separated purely for legibility, and the dense web of FIG. 7C is the two overlaid" | [0123], [0125] | [0123]: "divided into the subgraphs illustrated in FIGS. 7A and 7B for case of illustration and explanation" (patent's own typo, preserved). [0125]: "FIG. 7C illustrates all connections...in a single figure." | SUPPORTED | "Legibility" is a fair plain-English gloss of "ease of illustration." |
| 21 | S4 Wiring Schedules Traffic (FIG.7A caption) | "group 712a wired to every chip of 712c, and 712b to every chip of 712d" | [0138] | Same as row 18. | SUPPORTED | |
| 22 | S4 Wiring Schedules Traffic (FIG.7B caption) | "the criss-cross, 712a to 712d and 712b to 712c" | [0139] | Same as row 19. | SUPPORTED | |
| 23 | S4 Wiring Schedules Traffic (FIG.7B caption) | "Added to FIG. 7A's links it gives the full FIG. 7C web" | [0123], [0125] | Same as row 20. | SUPPORTED | |
| 24 | S4 Wiring Schedules Traffic | "Which physical family carries which is the description's worked example rather than a claim requirement, with gather traffic on the first channels and reduction traffic on the second" | [0140] | [0140]: first channels 730/first operation = "a data gather operation"; second channels 740/second operation = "a data reduction operation." | SUPPORTED | Precisely worded: claim 11 separately assigns first-sub-operation=reduction/second=gather in the abstract claim-language ordinal (not tied to 730/740 by number since claims never cite reference numerals) — the draft correctly avoids conflating the claim's abstract "first/second sub-operation" ordinal with the description's numbered-channel example. This is the single trickiest cross-reference in the patent and it is handled correctly. |
| 25 | S4 Wiring Schedules Traffic (blockquote) | "During the second operation, data may only be transmitted...using the second communication channels 740 and not the first communication channels 730." | [0140] | Verified verbatim by direct grep, including the source's stray space before the final period. | SUPPORTED | |
| 26 | S4 Wiring Schedules Traffic | "Claim 9 has the two sub-operations running in overlapping time periods, one channel family carrying each" | [0142] | [0142]: "in the event that the first and second operations are being performed during overlapping time periods, the processing devices...may receive and/or transmit data for both operations during overlapping time periods." | SUPPORTED | Also a claim-scope statement — see Sub-table 1, row C9. |
| 27 | S4 Wiring Schedules Traffic | "The tensors are pre-cut so that during these group-wide moves 'the same amount of data may be shared by each of the processing devices A0-A7', and the same amount crosses each channel" | [0168], [0178] | [0168] verbatim quote confirmed; [0178] parallels it for the first (730)/gather side: "the same amount of data may be shared...and a same amount of data may be shared across each of the first communication channels 730." | SUPPORTED | Correct pairing: 0168=second/reduction side, 0178=first/gather side, together covering "each channel." |
| 28 | S4 Wiring Schedules Traffic | "'When the number of processing devices is 8, p=4.35235, q=1.83809.'" | [0061] | [0061] verbatim, exact match. | SUPPORTED | |
| 29 | S4 Wiring Schedules Traffic | "Rounded to divisors, that is 4 and 2, and the practical reading is that the whole input matrix lives spread across four of the eight chips" | [0061] | [0061]: "p and n may be selected to be divisors of n, such that when n=8, p=4 and q=2...the input matrix may be split such that an entirety of the input matrix is found on 4 of the 8 processing devices." | SUPPORTED | Faithful paraphrase of the patent's own (dense) math paragraph; any residual ambiguity is inherited from the source, not introduced by the draft. |
| 30 | S4 Wiring Schedules Traffic | "The equal channels are wired in, and the equal traffic follows from the split the description prescribes" | [0168] | Same as row 27. | SUPPORTED | |
| 31 | S5 Transformer Decoding | "the AI model of FIG. 9A 'may be representative of a large language model or a transformer decoder'" | [0251] | [0251] verbatim, exact match. | SUPPORTED | |
| 32 | S5 Transformer Decoding | "Its decoding layers, the loop that infers one token at a time, run normalization, then self-attention (QKV generation and attention computation), then projection, then an MLP" | [0259], [0252], [0254] | [0252]: layer order normalization→self-attention→projection→MLP. [0254]: "QKV generation 916...attention computation 918." [0259]: layers "repeated multiple times for a single token," then "decoding 930...selecting a token." | SUPPORTED | "Loop that infers one token at a time" is a reasonable reader-profile compression of the repeat/decode mechanic; no direction reversed. |
| 33 | S5 Transformer Decoding | "From there the work hands off to decoding, the token pick" | [0259] | [0259]: "the AI model 900 may perform decoding 930...selecting a token for outputting as the next token." | SUPPORTED | |
| 34 | S5 Transformer Decoding (FIG.9A caption) | "the decoding-layer loop the description maps onto the group" | [0252], [0259] | Same as rows 32-33. | SUPPORTED | |
| 35 | S5 Transformer Decoding | "the number of elements in a next-token computation ordinarily tracks the model's depth, but 'during the feedforward operation, the number of elements involved in a specific computation may be four times the depth of the transformer model'" | [0313] | [0313] verbatim: "Typically...equal to a depth of the transformer model. However, during the feedforward operation...may be four times the depth..." | SUPPORTED | |
| 36 | S5 Transformer Decoding | "MLP calculations can run four times greater than the model's other computations, which inflates processing time, or the bandwidth needed to hold processing time flat" | [0258], [0313] | [0258] verbatim: "four times greater than other computations." [0313]: "processing time...may be much larger...and/or a data bandwidth required to maintain a processing time...may be increased." | SUPPORTED | "Hold processing time flat" = "maintain a processing time," accurate gloss. |
| 37 | S5 Transformer Decoding | "The description offers exactly that operation as a basis for sizing the tensor parallel group" | [0121] | [0121]: "the size of the tensor parallel groups 620 may be based on the computations performed by the feedforward operations performed by a MLP layer of an AI model." | SUPPORTED | |
| 38 | S5 Transformer Decoding (blockquote) | "the tensors used during the decoding layers 905 may remain split and distributed...such that no one processing device may include the entirety of a tensor during the tensor operations performed by the decoding layers 905." | [0278] | Verified verbatim by direct grep, including trailing-space artifacts. | SUPPORTED | |
| 39 | S5 Transformer Decoding | "the Q, K, and V matrices are processed as tiles, on different chips, 'without rejoining the tiles of the self-attention tensors Q, K, and V on a single processing device'" | [0267] | [0267] verbatim, exact match. | SUPPORTED | |
| 40 | S6 No Latency/Memory | "The description says the channels realizing it can be PCIe, SPI, ethernet, UCIe, or other wired or optical links...and the chips can sit on separate dies" | [0134], [0133] | [0134] verbatim list. [0133]: "each...may be formed on a separate die of a silicon process." | SUPPORTED | [0133] also allows same-die; draft states only one (true) option, doesn't exclude the other or misrepresent it as exclusive. |
| 41 | S6 No Latency/Memory | "The patent's own stated wins are fewer connections than a full mesh and less data sharing in less processing time, a cost and bandwidth accounting" | [0130], [0124] | Same as rows 10 and 16. | SUPPORTED | |
| 42 | S6 No Latency/Memory | "a rack that keeps its networking switch, the filing's own foil, sits outside claim 1" | [0032] | [0032] as row 9. | SUPPORTED | See finding sa2G-F3 (claim-scope wording, not an anchor problem — logged under Sub-table 1). |
| 43 | S6 No Latency/Memory | "cross-set-only direct channels...degree- and bandwidth-uniform links (claims 3 to 5), and reduce and gather running simultaneously on disjoint channel families (claims 8, 9, 11)" | [0386] | Same as row 4; claims 3-5/8-9-11 validated in Sub-table 1. | SUPPORTED | |
| 44 | S6 No Latency/Memory | "the whole fence is the wiring discipline the patent's own cluster-scale arithmetic runs on" | [0168], [0061] | Same as rows 27/28. | SUPPORTED | |
| 45 | S6 No Latency/Memory | "A hop bound is, and claim 1 sets one: at most one device between any two chips, ever" | [0387] | Same as row 5/14. | SUPPORTED | |
| 46 | S6 No Latency/Memory | "FIG. 6 shows a host, two tensor parallel groups, and a memory 630 whose role is to 'provide tensors and other data to the tensor parallel groups 620 for processing'" | [0112], [0119] | [0112]: environment 600 = host 602 + tensor parallel groups 620a/620b + memory 630. [0119] verbatim quote confirmed. | SUPPORTED | |
| 47 | S6 No Latency/Memory | "The description also lets each chip couple to memory devices, shared among the chips or not, and no claim picks that option up" | [0133] | [0133]: "each...may be coupled to one or more memory devices...that are shared or are not shared." | SUPPORTED | "No claim picks it up" verified by full 23-claim scan — no claim mentions memory. |
| 48 | S6 No Latency/Memory (FIG.6 caption) | "box 630, the memory that feeds the tensor parallel groups, described in one embodiment figure and never claimed" | [0119] | Same as row 46. | SUPPORTED | |
| 49 | S6 No Latency/Memory | "The specification's summary covers two sets of 'two or more' devices, while granted claims 1 and 14 require four or more per set" | [0385] | [0385] verbatim ("two or more" ×2); claims 1 and 14 both read "four or more" in `input/patent.md` CLAIMS section. | SUPPORTED | Central narrowing point; matches invention-summary's own scope-reading note verbatim. |
| 50 | S7 One Leg/One Leg | "a group wired so every chip reaches every other chip through at most one intermediate device" | [0387] | Same as row 5/14/45. | SUPPORTED | Explicitly scoped to the structural/topological fact only, not to "latency" or "bandwidth" — consistent with the essay's own established distinction. |
| 51 | S7 One Leg/One Leg | "Reduce and gather traffic run at the same time on separate channel families, over equal-bandwidth links (claim 5), with the same load on every link under the description's prescribed split" | [0142], [0168] | Same as rows 26/27. | SUPPORTED | |
| 52 | S7 One Leg/One Leg | "The whole arrangement exists to cut data sharing and processing time" | [0124] | Same as row 16. | SUPPORTED | |
| 53 | S7 One Leg/One Leg | "the wiring either matches claim 1's cross-set pattern or it does not" | [0386] | Same as row 4/43. | SUPPORTED | |

**Tally: 53/53 SUPPORTED. 0 UNSUPPORTED, 0 MISREAD, 0 OVERREACHED-BEYOND-ANCHOR.**
(Two of the 53 rows — 8 and 13 — carry a MEDIUM anchor-completeness finding despite a
SUPPORTED verdict: the asserted content is true and independently verified elsewhere in the
patent, but the specific `[dddd]` cited does not itself carry the full definitional/mechanic
detail. See §6.)

---

## 3. Sub-table 1 — claim-scope statements vs CLAIMS text + Claim scope map

Every statement in the draft that names claim 1, 14, 18, a cited dependent, or makes an
all-claims absolute (whether or not it also carries a `[dddd]` anchor).

| ref | statement in draft | claim text checked | verdict | note |
|---|---|---|---|---|
| C1 | "Claim 1 is built to deliver the reach with neither [a switch nor a full mesh]" | Claim 1 requires only direct cross-set channels + hop bound; no switch, no full intra-set/all-pairs wiring recited | SUPPORTED | |
| C2 | "four or more a side under the granted claim" (claim 1) | Claim 1: "a first set of four or more...and a second set of four or more" | SUPPORTED | |
| C3 | Blockquote labeled "claim 1, [0386]" | Verbatim identical to claim 1's middle clause | SUPPORTED | |
| C4 | "None of its claims mention latency, a bandwidth magnitude, or memory" | Full 23-claim scan: confirmed, no claim recites any of the three | SUPPORTED | |
| C5 | "Claim 1 recites a wiring pattern and nothing else" | Claim 1 text is entirely: device-set structure + channel topology + hop bound | SUPPORTED | |
| C6 | "claim 5 requires equal bandwidth across channels, not high bandwidth" | Claim 5: "each...channel...configured for a same data bandwidth" — equality only, no magnitude | SUPPORTED | |
| C7 | "claims 3 to 5" = same # coupled devices / same # channels / same bandwidth | Claim 3: "communicatively coupled to a same number of the plurality of processing devices." Claim 4: "coupled to a same number of communication channels." Claim 5: as C6. | SUPPORTED | |
| C8 | "claim 8 binds the data transfer for each sub-operation exclusively to one channel subset" | Claim 8: "data transfer for the first sub-operation occurs only via the first subset...and...second...only via the second subset" | SUPPORTED | |
| C9 | "Claim 9 has the two sub-operations running in overlapping time periods, one channel family carrying each" | Claim 9: "perform the first sub-operation and the second sub-operation in overlapping time periods such that first data...is transferred...at the same time second data..." | SUPPORTED | |
| C10 | "Claim 11 names the pair, a reduction and a gather" (deliberately unordered — see row 24 above) | Claim 11: "the first sub-operation is a reduction operation and the second sub-operation is a gather operation" | SUPPORTED | Draft correctly avoids asserting which physical channel family (730/740) claim 11's ordinal maps to — claims never cite reference numerals, so that mapping is description-only. |
| C11 | "The claims' only workload hooks are the systolic array (claim 7), matrix multiplication (claims 10 and 23), and the reduction and gather sub-operations (claims 11 and 23)" | Claim 7: "systolic array of data processing units." Claim 10: "operation is a matrix multiplication." Claim 23: matrix mult + reduction + gather. Claim 11: as C10. Full scan of claims 1-6,8-9,12-22 confirms no other workload-specific term. | SUPPORTED | Verbatim match to invention-summary's Claim scope map closing note ("Closest workload hooks in the claims: systolic array (7), matrix multiplication (10, 23), reduction/gather (11, 23)"). |
| C12 | "AI, transformers, and inference are absent from the claim language" | Full 23-claim scan: confirmed | SUPPORTED | |
| C13 | "**Structure is what an apparatus claim can lock, and structure is exactly what this one locks.**" | Consistent with the totality of claims 1-23 (structural/topological, with the narrow workload hooks in C11) | SUPPORTED | |
| C14 | "a rack that keeps its networking switch...sits outside claim 1" | Claim 1 uses open "comprising" transitional language | SUPPORTED (see sa2G-F3) | Accurate under the natural reading (a switch-*only*/switch-*instead-of* architecture lacks the required direct cross-set channels); "comprising" claims are not avoided merely by an *added* switch alongside the required wiring, so the sentence is correct only under that natural, contextually-signaled reading. |
| C15 | "the scheduling claims (8, 9, 11) bind only traffic routed the claimed way, a firmware choice" | Consistent with C8-C10 | SUPPORTED | |
| C16 | "The memory half has no equivalent fence anywhere in the claims" / "no claim picks that option up" [memory] | Full 23-claim scan: no claim recites memory | SUPPORTED | |
| C17 | "The granted claims are also narrower than the description's framing...granted claims 1 and 14 require four or more per set" [vs `[0385]`'s "two or more"] | Claims 1, 14 both read "four or more...four or more" | SUPPORTED | |
| C18 | "The third independent, claim 18, keeps the two-or-more floor but pays for it in structure: each set must contain two device groups, wired in at least the dual-family pattern of FIGS. 7A and 7B, with each sub-operation's traffic confined to its own family" | Claim 18 verbatim: "a first set of two or more...that includes a first group...and a second group...second set of two or more...that includes a third group...and a fourth group"; first/second communication channels cross-couple the groups; "data transfer for the first sub-operation occurs only via the...first communication channels and...second...only via the...second communication channels" | SUPPORTED | Precisely scoped — correctly omits claiming that 18 also requires the hop-bound (that is dependent claim 22 only) or overlapping-time execution (claim 9, not restated in 18) or a fixed reduction/gather assignment (claim 23 only). |
| C19 | "Three independents, three different trades of breadth for structure, and none of them mentions memory" | Claims 1, 14, 18 are the three independents (confirmed by claim numbering); none recites memory | SUPPORTED | |

No claim-scope statement in the draft mis-attributes a description-only preference (link
technology, die packaging, AI/LLM workload, equal set sizes) as a claim requirement, and none
inflates a "two or more" floor into "four or more" (or vice-versa) at the wrong claim.
Claims 2, 6, 12, 13, 15-17, 19-22 are simply not discussed in the draft — an omission, not a
fidelity defect (nothing false is asserted about them).

---

## 4. Sub-table 2 — external (non-patent) facts vs fact-check-log + attribution

| ref | fact in draft | fact-check-log entry | tier | verdict |
|---|---|---|---|---|
| E1 | "In early July 2026, Etched came out of stealth with an X thread" | `etched-csm-thread-2026-07` / `etched-lvi-biz-thread-2026-07` | tier-1 (company statement) | SUPPORTED |
| E2 | "Out of stealth after finishing its first chip design, the A0" | `etched-lvi-biz-thread-2026-07` ("out of stealth after A0 tapeout") | tier-1 | SUPPORTED — "finishing its first chip design" is a plain-English gloss of "tapeout" |
| E3 | "First racks built, shipping in summer 2026" | `etched-lvi-biz-thread-2026-07` | tier-1 | SUPPORTED |
| E4 | "More than $1 billion in customer contracts against $800 million raised" | `etched-lvi-biz-thread-2026-07` ("$1B+..."; "$800m raised") | tier-1 | SUPPORTED |
| E5 | Thread quotes: "shared low-latency memory pool across the entire scale-up domain"; "proprietary ultra-low-latency, high-bandwidth interconnect"; "each memory layer inherently adds latency; thus, the best layer is no layer" | `etched-csm-thread-2026-07` | tier-1 | SUPPORTED — quote chain documented in footnote `[^quote-chain]`, matches fact-check-log note verbatim |
| E6 | "Twelve months before the thread, in July 2025, the US patent office granted..." | `etched-family-trio-wips` (grant 2025-07-15) | tier-2 | SUPPORTED — "twelve months" is a reasonable approximation given "early July 2026" imprecision |
| E7 | Filing/grant dates, sole inventor (co-founder/CEO), 23 claims/3 independent/16 figures | `etched-family-trio-wips` | tier-2 | SUPPORTED |
| E8 | Sibling patents 903 (granted May 2025, tensor-tile movement) and 262 (granted same July day, model-level execution) | `etched-family-trio-wips` | tier-2 | SUPPORTED |
| E9 | PCT filings, 2026 US continuations, expected expiry 2044-10-22 | `etched-family-trio-wips` | tier-2 | SUPPORTED |
| E10 | "The company says its math blocks run at under half the voltage of typical AI chips" | `etched-lvi-biz-thread-2026-07` | tier-1 | SUPPORTED — attributed ("the company says") |
| E11 | "US applications can stay unpublished for up to 18 months after filing" | `us-18month-publication-window` | tier-2 | SUPPORTED — registry entry confirmed present (post-audit addition, per fact-check-log's own note) |
| E12 | "The company says its first systems ship in summer 2026" | `etched-lvi-biz-thread-2026-07` | tier-1 | SUPPORTED — attributed |
| E13 | Sources/bibliographic block (all 3 patents: numbers, titles, priority/publication dates, inventor) | `etched-family-trio-wips` | tier-2 | SUPPORTED |
| E14 | Scope-boundary statements: LVI, power delivery, cold plates, HBM/SRAM hybrid "nowhere in this filing or its granted siblings" | `essay-context.md` Scope boundaries section, tier-1 thread claims + patent-absence cross-check | tier-1/tier-2 mix | SUPPORTED — matches essay-context.md's scope-boundary prose almost verbatim |

**No unlogged external fact found.** Every non-patent factual assertion in the draft traces
to a fact-check-log row (or, for E14, directly to essay-context.md's explicit scope-boundary
framing, which is itself sourced from the same tier-1 thread entry). Attribution discipline
("the company says") is applied consistently wherever thread content is asserted as
company-claimed rather than independently verified.

---

## 5. Sub-table 3 — figure captions vs figures-manifest.md + cited paragraphs

All 6 figures placed in the draft body, checked against `input/figures/figures-manifest.md`.

| ref | figure | draft caption content | manifest description | cited paragraphs | verdict |
|---|---|---|---|---|---|
| FIG-1 | FIG. 7C (header) | "claimed core...eight chips...two columns...set 710a...set 710b...16 channels...no wire runs inside a column...both channel families (730,740) overlaid" | "Combined view overlaying both sub-graph patterns 730 and 740 on the same 8 devices" | [0125], [0126], [0128], [0129] | SUPPORTED |
| FIG-2 | FIG. 1 | "inside one tensor parallel group: processing devices built as systolic arrays" | "Block diagram of tensor parallel group 100: four processing devices 110a-d, each with a systolic array 112a-d..." | (figure reference only, no `[dddd]` on this caption line) | SUPPORTED |
| FIG-3 | FIG. 7A | "the first channel family (730): group 712a wired to every chip of 712c, and 712b to every chip of 712d" | "Sub-graph connection pattern 730 wiring 8 processing devices...groups 710a/710b, 712a-712d" | [0138] | SUPPORTED |
| FIG-4 | FIG. 7B | "the second channel family (740): the criss-cross, 712a to 712d and 712b to 712c...gives the full FIG. 7C web" | "Denser sub-graph connection pattern 740 wiring the same 8 processing devices" | [0139], [0123], [0125] | SUPPORTED |
| FIG-5 | FIG. 9A | "the decoding-layer loop the description maps onto the group" | "Block diagram of AI model 900: decoding layers 905 (normalization 910, self attention 915..., projection 920, MLP 925), then decoding 930" | [0252], [0259] | SUPPORTED |
| FIG-6 | FIG. 6 | "box 630, the memory that feeds the tensor parallel groups, described in one embodiment figure and never claimed" | "Example environment 600: host 602 connected to processing system 610 containing first/second tensor parallel devices 620a/620b and memory 630" | [0119] | SUPPORTED |

No caption asserts a panel, label, or connection pattern the manifest or the cited paragraph
does not support. Figure-asset footnotes (`[^figure-assets]`, `[^figures-not-placed]`) list
exactly the 6 placed files (fig-07C, fig-01, fig-07A, fig-07B, fig-09A, fig-06) plus a
self-consistent 10-figure excluded set; 6 + 10 = 16, matching the patent's full 16-figure
count with no orphans.

---

## 6. Findings (sa2G-F*)

All findings below are anchor-completeness or claim-scope-wording precision items on
otherwise-SUPPORTED rows. No fabricated, contradicted, or meaning-changing content was
found anywhere in the draft. Per jurisdiction, every recommendation below is anchor / narrow
/ label / cut only — no hedge is recommended anywhere.

- **sa2G-F1 (medium — recoverable anchor).** Row 8 (S3, "Mid-computation, the chips must
  combine partial results into one (a reduction) and hand out copies of pieces (a gather) to
  keep going `[0036]`"). `[0036]` names that data sharing "may include a data reduction
  process and/or a data gather process" but does not itself state that reduction means
  combining sub-results or that gather means copying data — that specific mapping sits at
  `[0037]` ("the sub-results...may be shared amongst the processing devices...and combined
  to generate the final result") and `[0039]` ("in a data gather process, data is copied
  between the processing devices"). Content is accurate and independently verified at those
  paragraphs. Recommended fix: **anchor** — append `[0037]`, `[0039]` alongside `[0036]`.
- **sa2G-F2 (medium — recoverable anchor).** Row 13 (S3, "Chips in the same set have no
  direct channel between them `[0128]`, so a message between two set-mates rides through one
  chip of the opposite set: two hops, one intermediate device, never more"). The "no direct
  channel" clause is squarely `[0128]`'s content; the specific "two hops, one intermediate
  device" mechanic is `[0130]`'s content ("at most two communication hops via a first
  communication channel with a first processing device and a separate communication channel
  between the first processing device and a second processing device"), not `[0128]`'s.
  `[0130]` is quoted correctly elsewhere in the same essay (lines 41, 88) but not re-cited at
  this specific clause. Recommended fix: **anchor** — append `[0130]` to this clause.
- **sa2G-F3 (low — claim-scope wording precision).** Sub-table 1, row C14 / main-table row
  42 (S6, "a rack that keeps its networking switch...sits outside claim 1"). Claim 1 uses
  open "comprising" language, so an embodiment that has *both* the required direct cross-set
  channels *and* an incidental switch would still read on claim 1 — the sentence is accurate
  only under the (contextually clear, and more likely) reading that "keeps its networking
  switch" means an architecture built around switch-mediated communication *instead of* the
  claimed direct wiring, i.e., one that altogether lacks the required structure. Recommended
  fix: **narrow** — reword to something like "a rack wired through a switch instead of the
  claimed direct topology" to foreclose a "comprising"-claim misreading by a legally literate
  reader.

No critical or high findings. No UNSUPPORTED, MISREAD, or OVERREACHED-BEYOND-ANCHOR verdicts
were assigned anywhere in the main table or the three sub-tables.
