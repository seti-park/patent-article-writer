# Self-Audit Round 1 — Grounding Verification (on ACCEPTED essay)

Instrument: grounding-verifier (fidelity only; no stance/tone/hedge jurisdiction).
Target: `handoff/03-edit/essay-final.md` (post-acceptance self-audit).
Inputs: `handoff/01-design/invention-summary.md`, `input/patent.md`, `handoff/01-design/fact-check-log.md`, `input/essay-context.md`, `input/figures/figures-manifest.md`, `input/figures/*.png` (visually inspected: fig-07C, fig-01, fig-06, fig-07A, fig-07B, fig-09A).

## 1. Mechanical gate outputs

```
$ python .claude/skills/_shared/scripts/gate_quotes.py handoff/03-edit/essay-final.md \
    --invention-summary handoff/01-design/invention-summary.md --patent input/patent.md
[PASS] gate=quotes
  (no findings)

$ python .claude/skills/_shared/scripts/gate_anchors.py handoff/03-edit/essay-final.md \
    --invention-summary handoff/01-design/invention-summary.md
[PASS] gate=anchors
  WARN  FIGREF-000   no figures_index provided, figure-ref check skipped  ((global))
```

Note: `--figures input/figures/figures-manifest.md` was attempted but the script expects a bare
int/comma list, not the manifest's Markdown table (`ValueError: invalid literal for int() with
base 10: '#'`) — a tool-format mismatch, not an essay defect. Figure-caption fidelity below was
therefore verified by hand against the manifest text and by direct visual inspection of the six
placed PNGs (fig-07C, fig-01, fig-07A, fig-07B, fig-09A, fig-06).

Both mechanical gates PASS with zero findings. Everything below is the manual anchor-by-anchor
layer the gates cannot do (paragraph-content match, quote byte-match, claim-scope reading).

## 2. Main anchor-by-anchor fidelity table

Every `[dddd]` bracket in the essay, in order of appearance (60 bracket tokens / 56 distinct
citation rows, incl. figure captions and blockquotes). "Patent para. check" quotes the operative
patent words. Verdicts: SUPPORTED / MISREAD / OVERREACHED-BEYOND-ANCHOR / UNSUPPORTED.

| # | Section | Essay sentence (claim-bearing clause) | Anchor(s) | Invention-summary span | Patent paragraph check | Verdict | Note |
|---|---|---|---|---|---|---|---|
| 1 | FIG.7C caption | "the first set 710a (a1, a3, a5, a7) on the right and the second set 710b (a0, a2, a4, a6) on the left" | [0126] | q-0126-1 | "Half of the processing devices A0-A7 are in the first set... namely A1, A3, A5, and A7... the other half... second set... namely A0, A2, A4, and A6" | SUPPORTED | Left/right verified by direct visual inspection of fig-07C.png: 710a (a1,a3,a5,a7) is drawn on the right, 710b (a0,a2,a4,a6) on the left. Exact. |
| 2 | FIG.7C caption | "Every chip in one column is wired straight to every chip in the other, 16 channels in all, and no wire runs inside a column" | [0128],[0129] | q-0128-1, q-0129-1/2 | [0128]: "no direct communication channels between the processing devices in the first set... and no direct... in the second set." [0129]: "each processing device... directly connected to each... via a different communication channel... coupled to four other" | SUPPORTED | "Wired straight"/"no wire inside a column" are verbatim-level matches. "16 channels" is not stated as a number in [0128]/[0129] — it is arithmetic (4 channels/device × 8 devices ÷ 2) confirmed both by q-0129-2 and by counting arrows in fig-07C.png. The essay body (unanchored, line ~50) discloses this is "read off the figure, not numbers the patent states"; the caption itself doesn't repeat that caveat. Low-severity precision note (sa1G-F4). |
| 3 | FIG.7C caption | "Both channel families (730, 740) are overlaid here" | [0125] | q-0125-1 | "FIG. 7C illustrates all connections between the processing devices A0-A7... in a single figure" | SUPPORTED | Confirmed visually: fig-07C.png shows solid (730) and dashed (740) lines together. |
| 4a | Sec.1 | "Its claims lock a wiring discipline... two sets, every cross-set pair directly wired, nothing wired inside a set" | [0386] | q-0386-1 | Matches claim 1 verbatim (see row 12). | SUPPORTED | |
| 4b | Sec.1 | "Any chip can reach any other through at most one chip in between" | [0387] | q-0387-1 | "each of the plurality of processing devices is able to communicate with any of the other... through at most one other of the plurality of processing devices" | SUPPORTED | |
| 5 | Sec.2 | "The specification enumerates three example families, methods, topology, and AI-model computation" | [0336] | (Layer-3/claims-vs-narrative-split framing) | [0336] only says aspects "are described as numbered examples (1, 2, 3, etc.)" — it does not itself name the three families. The contents are at [0337] ("Example 1 may include method of performing tensor operations"), [0384] ("Example 2 may include a tensor parallel group"), [0418] ("Example 3 may include method of performing computations for artificial intelligence models"). | OVERREACHED-BEYOND-ANCHOR | Right idea, accurate patent-wide, but the single cited paragraph doesn't carry the three-family content. **Finding sa1G-F1** (medium). Fix: extend anchor to [0337], [0384], [0418]. |
| 6 | Sec.3 | quote: "large enough that processing of the tensors in a typical manner using a single processor may be difficult" | [0021] | q-0021-1 | Byte-exact substring of [0021]. | SUPPORTED | Verbatim confirmed. |
| 7 | Sec.3 | "the chips must combine partial results into one (a reduction) and hand out copies of pieces (a gather)" | [0036] | (Layer-2 mechanism) | "data sharing between the processing device 110 may include a data reduction process and/or a data gather process" | SUPPORTED | |
| 8 | Sec.3 | "Route everything through a networking switch that lets any chip talk to any chip" | [0032] | (prior-art contrast) | "coupled together using a networking switch that enables communication between any one of the processing devices 110 with any other one" | SUPPORTED | |
| 9 | Sec.3 | quote: "expensive to include in a system that performs tensor operations" | [0026] | q-0026-1 | Byte-exact substring (tail of "...may be expensive to include in a system that performs tensor operations."). | SUPPORTED | Verbatim confirmed. "Data switch" (0026) and "networking switch" (0032) merged into one sentence — same alternative-to-fixed-topology concept in the patent; invention-summary itself pairs 0026/0032 this way. |
| 10 | Sec.3 | "wire every chip to every other chip, a point-to-point scheme whose connection count balloons as the group grows" | [0130] | q-0130-2 | "as compared to a point-to-point connection scheme where every processing device is coupled to every other processing device" | SUPPORTED | "Balloons as the group grows" is qualitative color on an undisputed graph-theoretic property (n(n-1)/2 growth), not a numeric patent claim. |
| 11 | Sec.3 | "the odd-numbered chips form the first set (710a) and the even-numbered chips the second (710b)" | [0126] | q-0126-1 | A1,A3,A5,A7 (odd) = 710a; A0,A2,A4,A6 (even) = 710b. | SUPPORTED | |
| 12 | Sec.3 blockquote | Claim-1 block quote ("a plurality of communication channels to directly communicatively couple...") | [0386], claim 1 | q-0386-1 | Byte-exact substring of granted Claim 1 (and identical spec language at [0386]). | SUPPORTED | Verbatim confirmed against CLAIMS text directly — full claim-1 quote check passes. |
| 13 | Sec.3 | "Chips in the same set have no direct channel between them" | [0128] | q-0128-1 | Exact match. | SUPPORTED | |
| 14 | Sec.3 | quote: "through at most one other of the plurality of processing devices" | [0387] | q-0387-1 | Byte-exact substring. | SUPPORTED | Verbatim confirmed. |
| 15 | Sec.3 | "an intermediate chip may begin forwarding data before it has finished receiving it" | [0143] | q-0143-1 | "may send the received data to the third processing device A2 before all the data from the first processing device A0 is received" | SUPPORTED | |
| 16 | Sec.3 | quote: "may be used to reduce data sharing between the processing devices A0-A7 and thereby help to reduce a processing time" | [0124] | q-0124-1 | Exact prefix-truncation of the [0124] clause (patent continues "...for the tensor operations performed by a tensor parallel group 700."). | SUPPORTED | Valid truncation, no misrepresentation. |
| 17 | Sec.4 | "Each set subdivides into two groups of chips, labeled 712a through 712d, and the channels split with them into two families" | [0135] | (mechanism Layer 2 step 3) | [0135] only names groups 712a–712d; the "each set includes two of the groups" mapping is at [0136]: "each set of processing devices 710 may include two or more of the groups of processing devices 712... 712a and... 712b may be formed from the first set... 712c and... 712d may be formed from the second set." | MISREAD | **Finding sa1G-F2** (medium). Anchor cited doesn't carry the set→group-count assertion; correct paragraph is [0136]. Fix: anchor — add [0136]. |
| 18 | Sec.4 | "The first communication channels (730) join group 712a with 712c and group 712b with 712d" | [0138] | (mechanism Layer 2 step 3) | Exact match. | SUPPORTED | |
| 19 | Sec.4 | "The second communication channels (740) run the criss-cross: 712a with 712d, 712b with 712c" | [0139] | (mechanism Layer 2 step 3) | Exact match. | SUPPORTED | |
| 20 | Sec.4 | "FIG. 7A and FIG. 7B draw one family each, separated purely for legibility, and the dense web of FIG. 7C is the two overlaid" | [0123] | (figure relationships) | "divided into the subgraphs illustrated in FIGS. 7A and 7B for case of illustration and explanation" + "fixed topology... may include all the connections of FIGS. 7A and 7B" | SUPPORTED | |
| 21 | FIG.7A caption | "group 712a wired to every chip of 712c, and 712b to every chip of 712d" | [0138] | — | Exact match; confirmed visually (fig-07A.png shows exactly this half of the web). | SUPPORTED | |
| 22 | FIG.7B caption | "the criss-cross, 712a to 712d and 712b to 712c. Added to FIG. 7A's links it gives the full FIG. 7C web" | [0123] | — | The criss-cross detail is [0139]'s content (already cited at row 19), not [0123]'s; [0123] covers only the "gives the full FIG. 7C web" clause. Confirmed visually accurate (fig-07B.png shows the crossing pattern). | SUPPORTED | Low-severity note **sa1G-F5**: caption's sole anchor [0123] doesn't cover the 712a/712d, 712b/712c detail; recommend adding [0139]. |
| 23 | Sec.5 | "Which physical family carries which is the description's worked example rather than a claim requirement, with gather traffic on the first channels and reduction traffic on the second" | [0140] | (Claim scope map, claim 8 "leaves open") | "the first operation may be a data gather operation and the second operation may be a data reduction operation" | SUPPORTED | Precisely matches Claim-scope map's own locked/open distinction for claim 8. |
| 24 | Sec.5 blockquote | "During the second operation, data may only be transmitted... using the second communication channels 740 and not the first communication channels 730." | [0140] | q-0140-2 | Byte-exact, including the patent's own "730 ." spacing quirk. | SUPPORTED | Verbatim confirmed. |
| 25 | Sec.5 | "Claim 9 has the two sub-operations running in overlapping time periods, one channel family carrying each" | [0142] | q-0142-1 | Claim 9 text confirmed verbatim (see claim-scope table); [0142] echoes it at spec level. | SUPPORTED | |
| 26 | Sec.5 | quote: "the same amount of data may be shared by each of the processing devices A0-A7", "same amount crosses each channel" | [0168],[0178] | q-0168-1 | Phrase appears near-verbatim in BOTH [0168] (re: 740) and [0178] (re: 730). | SUPPORTED | Verbatim confirmed in both paragraphs. |
| 27 | Sec.5 | quote: "When the number of processing devices is 8, p=4.35235, q=1.83809." | [0061] | q-0061-1 | Byte-exact. | SUPPORTED | Verbatim confirmed. |
| 28 | Sec.5 | "Rounded to divisors, that is 4 and 2, and the practical reading is that the whole input matrix lives spread across four of the eight chips" | [0061] | q-0061-2 | "p and n may be selected to be divisors of n, such that when n=8, p=4 and q=2... the input matrix may be split such that an entirety of the input matrix is found on 4 of the 8 processing devices" | SUPPORTED | |
| 29 | Sec.5 | "The equal channels are wired in, and the equal traffic follows from the split the description prescribes" | [0168] | q-0168-1 | Confirmed. | SUPPORTED | |
| 30 | Sec.6 | quote: "may be representative of a large language model or a transformer decoder" | [0251] | q-0251-1 | Byte-exact. | SUPPORTED | Verbatim confirmed. |
| 31 | Sec.6 | "Its decoding layers, the loop that infers one token at a time" | [0313] | (none directly) | [0313] is about element-count comparison for the feedforward operation, not the decode/repeat loop. The "repeated... for a single token" / "selecting a token... as the next token" framing is at [0259]. | MISREAD | **Finding sa1G-F3** (medium). Fix: anchor — [0313] → [0259]. |
| 32 | Sec.6 | "run normalization, then self-attention (QKV generation and attention computation), then projection, then an MLP" | [0252] | (mechanism) | [0252] confirms the 4-layer sequence (normalization, self-attention, projection, MLP) exactly; the QKV-generation/attention-computation sub-detail is at [0254], not [0252]. | SUPPORTED | Low-severity note **sa1G-F6**: main sequence fully supported by [0252]; parenthetical sub-detail more precisely sourced at [0254]. |
| 33 | Sec.6 | "From there the work hands off to decoding, the token pick" | [0259] | (mechanism) | "the AI model 900 may perform decoding 930... selecting a token for outputting as the next token in the sequence" | SUPPORTED | |
| 34 | FIG.9A caption | "the decoding-layer loop the description maps onto the group" | [0251] | — | [0251] establishes AI model 900 = LLM/transformer decoder only; the "loop" is [0259], "maps onto the group" is [0263] ("one or more tensor operations of the self-attention layer 915 may be performed by a tensor parallel group"). Figure content itself confirmed accurate by direct visual inspection against figures-manifest. | SUPPORTED | Low-severity note **sa1G-F7**: caption anchor is thin for a two-part synthesis claim; recommend [0259]+[0263]. |
| 35 | Sec.6 | quote: "during the feedforward operation, the number of elements involved in a specific computation may be four times the depth of the transformer model" (+ preceding clause) | [0313] | q-0313-1, q-0313-2 | Byte-exact, both clauses. | SUPPORTED | Verbatim confirmed. |
| 36 | Sec.6 | "MLP calculations can run four times greater than the model's other computations" | [0258] | q-0258-1 | "the MLP calculations may result in computations that are four times greater than other computations performed by the AI model 900" | SUPPORTED | |
| 37 | Sec.6 | "which inflates processing time, or the bandwidth needed to hold processing time flat" | [0313] | (continuation of q-0313) | "processing time for the feedforward operation may be much larger... and/or a data bandwidth required to maintain a processing time... may be increased" | SUPPORTED | |
| 38 | Sec.6 | "The description sizes the tensor parallel group around exactly that operation" | [0121] | q-0121-1 | "size of the tensor parallel groups 620 may be based on the computations performed by the feedforward operations performed by a MLP layer" | SUPPORTED | |
| 39 | Sec.6 blockquote | "the tensors used during the decoding layers 905 may remain split and distributed... such that no one processing device may include the entirety of a tensor..." | [0278] | q-0278-1 | Byte-exact, incl. trailing " ." formatting. | SUPPORTED | Verbatim confirmed. |
| 40 | Sec.6 | quote: "without rejoining the tiles of the self-attention tensors Q, K, and V on a single processing device" | [0267] | q-0267-1 | Byte-exact substring. | SUPPORTED | Verbatim confirmed. |
| 41 | Sec.7 | "the channels realizing it can be PCIe, SPI, ethernet, UCIe, or other wired or optical links" | [0134] | q-0134-1 | Exact match (all five terms present). | SUPPORTED | |
| 42 | Sec.7 | "the chips can sit on separate dies" | [0133] | q-0133-1 | "each of the processing devices A0-A7 may be formed on a separate die of a silicon process" | SUPPORTED | |
| 43 | Sec.7 | "The patent's own stated wins are fewer connections than a mesh" | [0130] | q-0130-2 | Confirmed. | SUPPORTED | |
| 44 | Sec.7 | "less data sharing in less processing time" | [0124] | q-0124-1 | Confirmed. | SUPPORTED | |
| 45 | Sec.7 | "cross-set-only direct channels" | [0386] | q-0386-1 | Confirmed. | SUPPORTED | |
| 46 | Sec.7 | "the whole fence is the wiring discipline the patent's own cluster-scale arithmetic runs on" | [0168],[0061] | q-0168-1, q-0061-1/2 | Confirmed both. | SUPPORTED | |
| 47 | Sec.7 | "A hop bound is, and claim 1 sets one: at most one device between any two chips, ever" | [0387] | q-0387-1 | Confirmed. | SUPPORTED | |
| 48 | Sec.7 | "FIG. 6 shows a host, two tensor parallel groups, and a memory 630 whose role is to \"provide tensors and other data...\"" | [0119] | q-0119-1 | Quote clause byte-exact to [0119]. Descriptive clause ("host, two tensor parallel groups, memory 630") is [0112]'s content, not [0119]'s. | SUPPORTED | Low-severity note **sa1G-F8**: recommend adding [0112] for the descriptive clause; content confirmed correct and matches figures-manifest + direct image inspection of fig-06.png. |
| 49 | Sec.7 | "each chip couple to memory devices, shared among the chips or not, and no claim picks that option up" | [0133] | (claims-vs-narrative-split) | "each of the processing devices A0-A7 may be coupled to one or more memory devices... shared or are not shared" | SUPPORTED | |
| 50 | FIG.6 caption | "box 630, the memory that feeds the tensor parallel groups, described in one embodiment figure and never claimed" | [0119] | q-0119-1 | Confirmed; matches figures-manifest description and direct image inspection. | SUPPORTED | |
| 51 | Sec.7 | quote: "two or more" [devices per set] | [0385] | q-0385-1 | Byte-exact. Correctly paired in the same sentence with the claim-1/14 "four or more" narrowing note per invention-summary's explicit pairing instruction. | SUPPORTED | Verbatim confirmed; narrowing-note pairing rule followed. |
| 52 | Sec.8 | "a group wired so every chip reaches every other chip through at most one intermediate device" | [0387] | q-0387-1 | Confirmed. | SUPPORTED | |
| 53 | Sec.8 | "Reduce and gather traffic run at the same time on separate channel families" | [0142] | q-0142-1 | Confirmed. | SUPPORTED | |
| 54 | Sec.8 | "with the same load on every link" | [0168] | q-0168-1 | Confirmed. | SUPPORTED | |
| 55 | Sec.8 | "The whole arrangement exists to cut data sharing and processing time" | [0124] | q-0124-1 | Confirmed. | SUPPORTED | |
| 56 | Sec.8 | "the wiring either matches claim 1's cross-set pattern [0386] or it does not" | [0386] | q-0386-1 | Confirmed. | SUPPORTED | |

**Tally: 56 rows. SUPPORTED 53 (incl. 5 with low-severity precision notes) · MISREAD 2 (rows 17,
31) · OVERREACHED-BEYOND-ANCHOR 1 (row 5) · UNSUPPORTED 0.**

## 3. Claim-scope verification (Additionally §1)

Every essay statement about what claims 1/5/7/8/9/10/11/14/18 or the claim set overall require or
omit, checked directly against the CLAIMS text (input/patent.md lines 931–977) and the Claim
scope map.

| Essay statement | Claim(s) | CLAIMS text check | Scope-map check | Verdict |
|---|---|---|---|---|
| "None of its claims mention latency, a bandwidth magnitude, or memory" | all 23 | Confirmed by full-text scan: no claim contains "latency," "memory," or a bandwidth figure. | Matches scope-map note verbatim. | SUPPORTED |
| "Split the group's chips into two sets, four or more a side under the granted claim" | 1 | Claim 1: "a first set of four or more... and a second set of four or more..." | Matches row 1. | SUPPORTED |
| Claim-1 block quote (row 12 above) | 1 | Byte-exact. | — | SUPPORTED |
| "claim 8 binds the data transfer for each sub-operation exclusively to one channel subset" | 8 | Claim 8 full text confirms: two subsets, each device coupled to ≥1 channel of each, sub-operation-exclusive transfer. | Matches row 8. | SUPPORTED |
| "Claim 11 names the pair, a reduction and a gather" | 11 | Claim 11: "the first sub-operation is a reduction operation and the second sub-operation is a gather operation." | Matches row 11. | SUPPORTED |
| "Claim 9 has the two sub-operations running in overlapping time periods, one channel family carrying each" | 9 | Claim 9 confirms verbatim. | Matches row 9. | SUPPORTED |
| "each device couples to the same number of chips, the same number of channels, and channels of the same bandwidth (claims 3 to 5)" | 3,4,5 | Claim 3 (same # devices), claim 4 (same # channels), claim 5 (same bandwidth) — all three confirmed verbatim. | Matches rows 3–5. | SUPPORTED |
| "The claims' only workload hooks are the systolic array (claim 7), matrix multiplication (claims 10 and 23), and the reduction and gather sub-operations (claims 11 and 23)" | 7,10,11,23 | Claim 7 (systolic array), 10 (matrix multiplication), 11 (reduction/gather), 23 (matrix multiplication + reduction/gather) — all confirmed. | Matches scope-reading notes exactly. | SUPPORTED |
| "AI, transformers, and inference are absent from the claim language" | all 23 | Confirmed by scan. | Matches scope-map note. | SUPPORTED |
| "Claim 1 recites a wiring pattern and nothing else" | 1 | Confirmed — claim 1's sole content is sets/channels/hop-bound. | Matches row 1. | SUPPORTED |
| "No granted claim recites a latency figure or a bandwidth magnitude, and claim 5 requires equal bandwidth across channels, not high bandwidth" | 5, all | Claim 5: "configured for a same data bandwidth" — equality only, no magnitude. | Matches row 5 "Pins: none." | SUPPORTED |
| "degree- and bandwidth-uniform links (claims 3 to 5)" | 3,4,5 | Confirmed (duplicate of above). | — | SUPPORTED |
| "reduce and gather running simultaneously on disjoint channel families (claims 8, 9, 11)" | 8,9,11 | Confirmed (duplicate of above). | — | SUPPORTED |
| "The memory half has no equivalent fence anywhere in the claims" | all 23 | Confirmed. | — | SUPPORTED |
| "no claim picks that option up" [shared memory devices] | all 23 | Confirmed — no claim recites memory attachment. | — | SUPPORTED |
| "granted claims 1 and 14 require four or more per set" | 1, 14 | Claim 14: "a first set of four or more... and a second set of four or more..." — confirmed identical to claim 1's device-count language. | Matches rows 1, 14. | SUPPORTED |
| "The third independent, claim 18, keeps the two-or-more floor but pays for it in structure: each set must contain two device groups, wired in exactly the dual-family pattern of FIGS. 7A and 7B, with each sub-operation's traffic confined to its own family" | 18 | Claim 18 full text confirms: "two or more" per set, first/second/third/fourth groups, first-channel-family (group1↔group3, group2↔group4), second-channel-family (group1↔group4, group2↔group3), sub-operation-exclusive transfer. | Matches row 18 exactly. | SUPPORTED |
| Essay correctly does **not** attribute the "at most one intermediate device" property to claim 18 itself | 18 vs 22 | Confirmed: that property is added only by dependent claim 22, not recited in claim 18. The essay never claims it for 18. | Matches scope-map note ("added by dependent 22"). | SUPPORTED (correct omission) |
| "Three independents, three different trades of breadth for structure, and none of them mentions memory" | 1,14,18 | Confirmed: 1 (4+/4+, simple bipartite), 14 (wraps 1 in a system claim), 18 (2+/2+, but adds dual-group/dual-family structure). No claim mentions memory. | Matches scope-map "three independents do not share one floor." | SUPPORTED |
| "the claims granted here track only the topology family" | all 23 | Confirmed — every claim's preamble/body matches Example 2's "tensor parallel group"/"system... plurality of tensor parallel groups" pattern; none use Example 1's "method of performing tensor operations" or Example 3's "method of performing computations for an AI model" claim language. | Matches "claims-vs-narrative-split" angle. | SUPPORTED |

**Claim-scope tally: 19/19 statements SUPPORTED. Zero MISREAD, zero OVERREACHED, zero UNSUPPORTED.**
This is the essay's strongest fidelity dimension — every locked/open/pinned distinction in the
Claim scope map is reproduced correctly, including the subtle ones (claim-5 equality-not-magnitude,
claim-18's floor-for-structure trade, the claim-22-only hop-bound for the 18-family).

## 4. External-fact verification (Additionally §2)

| External fact (as stated in essay) | Registry match (fact-check-log.md) | Tier | Attribution required? | Attribution used | Verdict |
|---|---|---|---|---|---|
| Etched exited stealth "early July 2026" via X thread | `etched-csm-thread-2026-07` / `etched-lvi-biz-thread-2026-07`; "early July 2026" itself sourced from essay-context.md line 10 | tier-1 (event/timing, not a content claim) | No (event/date, not a company performance claim) | — | SUPPORTED |
| "Out of stealth after taping out its A0 silicon" | `etched-lvi-biz-thread-2026-07`: "out of stealth after A0 tapeout" | tier-1 | Yes | Framed by preceding sentence: "every number in them is the company's own account" | SUPPORTED |
| "First racks built, shipping in summer 2026" | `etched-lvi-biz-thread-2026-07`: "first racks built"; "first racks ship summer 2026" | tier-1 | Yes | Same frame sentence | SUPPORTED |
| "More than $1 billion in customer contracts against $800 million raised" | `etched-lvi-biz-thread-2026-07`: "$1B+ in customer contracts"; "$800m raised" | tier-1 | Yes | Same frame sentence | SUPPORTED |
| Quote: "shared low-latency memory pool across the entire scale-up domain" | `etched-csm-thread-2026-07` | tier-1 | Yes (quoted) | Quotation marks + "the thread's claims," "CSM... is the one that pulled readers in" | SUPPORTED |
| Quote: "proprietary ultra-low-latency, high-bandwidth interconnect" | `etched-csm-thread-2026-07` | tier-1 | Yes (quoted) | Quotation marks, same frame | SUPPORTED |
| Quote: "each memory layer inherently adds latency; thus, the best layer is no layer" | `etched-csm-thread-2026-07` | tier-1 | Yes (quoted) | Quotation marks + footnote `[^quote-chain]` disclosing thread→essay-context→essay chain | SUPPORTED |
| Grant date 2025-07-15, filing date 2024-10-22, "inside nine months" (266 days) | `etched-family-trio-wips` | tier-2 (bibliographic) | No | — (computed, footnoted as computed in `[^derived-counts]`) | SUPPORTED (266-day math independently re-verified: Oct 22 2024 → Jul 15 2025 = 266 days) |
| Gavin Uberti, Etched co-founder/CEO, sole named inventor | `etched-family-trio-wips` | tier-2 | No | — | SUPPORTED |
| "23 claims, three of them independent, over 16 figures" | `etched-family-trio-wips` | tier-2 | No | — | SUPPORTED (independently recounted: 23 claims / 3 independent / 16 figure labels) |
| Sibling US 12,306,903 B1 granted May 2025 (tiles/method); US 12,361,262 B1 granted same July day (AI-model execution) | `etched-family-trio-wips` | tier-2 | No | — | SUPPORTED |
| PCT filings + US continuations published 2026, keeping all three open | `etched-family-trio-wips` | tier-2 | No | — | SUPPORTED |
| Expected term to October 2044 | `etched-family-trio-wips` | tier-2 | No | — | SUPPORTED |
| "Low-Voltage Inference is nowhere in this filing or its granted siblings" | essay-context.md scope-boundaries | n/a (negative claim about patent content, cross-checked directly against CLAIMS+description) | No | — | SUPPORTED |
| "the power-delivery work, the cold plates, and the HBM/SRAM hybrid... that the thread folds into CSM" | essay-context.md scope-boundaries + `etched-csm-thread-2026-07` (HBM/SRAM hybrid design) | tier-1/registered | Yes | "that the thread folds into" framing | SUPPORTED |
| "The company says its math blocks run at under half the voltage of typical AI chips" | `etched-lvi-biz-thread-2026-07` | tier-1 | Yes | Explicit "The company says" | SUPPORTED |
| "US applications can stay unpublished for up to 18 months after filing" | **Not in fact-check-log.md's external-facts table.** Appears only as prose in essay-context.md's Scope-boundaries section ("18-month window"), not as a sourced/tiered registry row. | — | — | — | **UNSUPPORTED (unlogged)** — Finding **sa1G-F9** (medium). The fact itself is standard, correct US patent-publication practice (35 U.S.C. §122(b)); the gap is a registry-process one, not an accuracy one. Fix: log it in fact-check-log.md (tier-2, general patent-law fact) rather than leaving it sourced only to essay-context.md prose. |
| "The company says its first systems ship in summer 2026" | `etched-lvi-biz-thread-2026-07` | tier-1 | Yes | Explicit "The company says" | SUPPORTED |
| Sources-section bibliographic block (3 patents + 1 official-statement entry) | `etched-family-trio-wips` / thread | tier-2 / tier-1 | n/a (citation block) | — | SUPPORTED, matches patent.md header data and fact-check-log exactly |

**External-fact tally: 19 checked, 18 SUPPORTED, 1 UNSUPPORTED (unlogged registry gap, sa1G-F9).
Zero MIS-ATTRIBUTED** — every tier-1 (company-claimed) fact in the essay carries either an
explicit "the company says" or an equivalent clear thread-attribution frame, consistent with
essay-context.md's attribution rule.

## 5. Figure-caption verification (Additionally §3)

| Figure | Essay caption | figures-manifest.md description | Cited paragraph(s) | Direct image check | Verdict |
|---|---|---|---|---|---|
| FIG. 7C (header) | "the claimed core in one drawing... 16 channels in all... no wire runs inside a column... Both channel families... overlaid" | "Combined view overlaying both sub-graph patterns 730 and 740 on the same 8 devices" | [0125],[0126],[0128],[0129] | Viewed fig-07C.png directly: confirms 710a(a1,a3,a5,a7) right / 710b(a0,a2,a4,a6) left, solid+dashed lines both present, 16 total edges (4 per node × 4 nodes/side), zero within-column edges. | SUPPORTED (rows 1–3 above) |
| FIG. 1 | "inside one tensor parallel group: processing devices built as systolic arrays" | "Block diagram of tensor parallel group 100: four processing devices 110a-d, each with a systolic array 112a-d and processing elements 114a-d" | (unanchored gloss) | Viewed fig-01.png: confirms 4 processing devices, each containing a systolic array containing processing elements. | SUPPORTED |
| FIG. 7A | "the first channel family (730): group 712a wired to every chip of 712c, and 712b to every chip of 712d" | "Sub-graph connection pattern 730 wiring 8 processing devices" | [0138] | Viewed fig-07A.png: confirms exactly this half-pattern, no criss-cross lines present. | SUPPORTED |
| FIG. 7B | "the second channel family (740): the criss-cross, 712a to 712d and 712b to 712c" | "Denser sub-graph connection pattern 740" | [0123] (0139 not cited — sa1G-F5) | Viewed fig-07B.png: confirms crossing/diagonal pattern distinct from 7A. | SUPPORTED |
| FIG. 9A | "the decoding-layer loop the description maps onto the group" | "Block diagram of AI model 900: decoding layers 905 (normalization 910, self attention 915 with QKV generation 916 and attention computation 918, projection 920, MLP 925), then decoding 930" | [0251] (thin — sa1G-F7) | Viewed fig-09A.png: confirms exact layer stack and labels as manifest describes. | SUPPORTED |
| FIG. 6 | "box 630, the memory that feeds the tensor parallel groups, described in one embodiment figure and never claimed" | "Example environment 600: host 602 connected to processing system 610 containing first/second tensor parallel devices 620a/620b and memory 630" | [0119] (0112 not cited — sa1G-F8) | Viewed fig-06.png: confirms Host 602, Processing System 610 containing two Tensor Parallel Devices 620a/620b and Memory 630. "Never claimed" independently verified against all 23 claims (memory absent from claim language). | SUPPORTED |

**Figure tally: 6/6 placed figures SUPPORTED.** All six captions match both the manifest
description and direct visual inspection of the actual PNGs; the "never claimed" assertion for
FIG. 6 is additionally verified against the full CLAIMS text. `[^figures-not-placed]` footnote's
claim that no excluded figure (2,3,4,5,8,9B,10,11,12,13) appears in the body is confirmed by a
full-text grep — accurate.

## 6. Findings summary

| ID | Severity | Location | Issue | Recommended fix |
|---|---|---|---|---|
| sa1G-F1 | medium | Sec.2, "[0336]" | Single anchor doesn't carry the three-family (methods/topology/AI-model) content it's cited for | anchor — extend to [0337], [0384], [0418] |
| sa1G-F2 | medium | Sec.4, "[0135]" | Anchor cited for "each set subdivides into two groups" doesn't state that; correct paragraph is [0136] | anchor — correct/extend to [0136] |
| sa1G-F3 | medium | Sec.6, "[0313]" | Anchor cited for "the loop that infers one token at a time" doesn't cover that; correct paragraph is [0259] | anchor — [0313] → [0259] |
| sa1G-F4 | low | FIG.7C caption | "16 channels in all" stated in an anchored caption clause without the figure-derived caveat the body gives it elsewhere | label — note as figure-derived count, or drop the number from the anchored clause |
| sa1G-F5 | low | FIG.7B caption | "712a to 712d and 712b to 712c" detail not covered by the caption's cited [0123]; content is [0139]'s | anchor — add [0139] |
| sa1G-F6 | low | Sec.6, "[0252]" | "(QKV generation and attention computation)" parenthetical is [0254]'s content, not [0252]'s | anchor — add [0254] |
| sa1G-F7 | low | FIG.9A caption | "[0251]" is thin for the two-part claim ("loop" + "maps onto the group") | anchor — add [0259] (loop), [0263] (maps onto group) |
| sa1G-F8 | low | Sec.7, "[0119]" | Descriptive clause ("host, two tensor parallel groups, memory 630") is [0112]'s content, not [0119]'s | anchor — add [0112] |
| sa1G-F9 | medium | Sec.10 ("18 months") | External fact (US patent publication timing) used in the essay is not itemized in fact-check-log.md's registry table — sourced only via essay-context.md prose | registry — log in fact-check-log.md (tier-2, general patent-law fact); no change to essay text needed since the fact itself is accurate |

No critical findings (nothing fabricated or contradicted). No high findings (no MISREAD/OVERREACHED
that changes subject, direction, or mechanism — both MISREADs found are anchor-pointer errors with
accurate, recoverable content one paragraph away).
