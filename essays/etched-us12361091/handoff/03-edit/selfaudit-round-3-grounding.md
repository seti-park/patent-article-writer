# Self-Audit Grounding Verification — Round 3 (Final Dry-Check)

Draft under review: `handoff/03-edit/essay-final.md` (draft_version 4, `closing_posture: firm`)
Inputs: invention-summary.md, input/patent.md (full text, incl. CLAIMS 1-23), fact-check-log.md,
essay-context.md, figures-manifest.md, plus direct visual inspection of fig-07C/01/07A/07B/09A/06.
Scope: fidelity only (anchor accuracy, claim-scope precision, external-fact logging, figure
caption accuracy). No tone/style/structure/conclusion-stance commentary. Blind to edit logs,
revision notes, and prior self-audit reports per task instruction.

---

## 0. Mechanical layer

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

Both gates pass clean. The `FIGREF-000` line is an informational WARN (optional `--figures`
arg not supplied), not a finding — it does not affect the PASS verdict. Every
`[dddd]`-anchored paragraph number and every quoted span in the draft is mechanically present
verbatim in `invention-summary.md` and/or `input/patent.md`.

Everything below is the manual semantic layer the regex gates cannot do: does the *prose*
assert no more than the anchor supports, for all 54 anchored sentences (incl. captions and
the 3 long blockquotes), all claim-scope statements, all external facts, and all 6 placed
figure captions (cross-checked against the actual image files, not just text).

---

## 1. Main anchor-by-anchor fidelity table (every `[dddd]`-anchored sentence)

Verdict key: SUPPORTED / UNSUPPORTED / MISREAD / OVERREACHED-BEYOND-ANCHOR.

| # | Essay sentence (anchor) | Patent span (paraphrased/quoted) | Verdict | Note |
|---|---|---|---|---|
| M1 | Caption FIG.7C: "the first set 710a (a1,a3,a5,a7) on the right and the second set 710b (a0,a2,a4,a6) on the left `[0126]`" | `[0126]`: "Half...are in the first set...710a, namely...A1, A3, A5, and A7 and the other half...710b, namely...A0, A2, A4, and A6." (q-0126-1) | SUPPORTED | Set membership from text; left/right layout **directly confirmed by opening fig-07C.png**: 710a label sits at top-right/bottom-right (a1,a3,a5,a7 column), 710b at top-left/bottom-left (a0,a2,a4,a6 column). |
| M2 | Caption FIG.7C: "Every chip in one column is wired straight to every chip in the other, 16 channels in all...no wire runs inside a column `[0128]`, `[0129]`" | `[0128]` (q-0128-1): "no direct communication channels...in the first set...and no direct...in the second set." `[0129]` (q-0129-1): "each processing device in the first set...directly connected to each...in the second set...via a different communication channel" | SUPPORTED | Visually recounted in fig-07C.png: each of the 4 left-column boxes has exactly 4 outbound arrows, all landing on the 4 right-column boxes (4×4=16); no line connects two same-column boxes. |
| M3 | Caption FIG.7C: "Both channel families (730, 740) are overlaid here `[0125]`" | `[0125]` (q-0125-1): "FIG. 7C illustrates all connections between the processing devices A0-A7...in a single figure." | SUPPORTED | Confirmed both by text and by image (both solid/730-side and dashed/740-side lines visible together). |
| M4 | "Its claims lock a wiring discipline...two sets, every cross-set pair directly wired, nothing wired inside a set `[0386]`" | `[0386]`/claim 1: "...directly communicatively couple every...in the first set...with every...in the second set...without communicatively coupling any...in the same set..." | SUPPORTED | Verbatim match to claim 1 body. |
| M5 | "Any chip can reach any other through at most one chip in between `[0387]`" | `[0387]`/claim 1: "...able to communicate with any of the other...through at most one other..." | SUPPORTED | |
| M6 | "Tensors...can be 'large enough that processing of the tensors in a typical manner using a single processor may be difficult' `[0021]`" | `[0021]` (q-0021-1), verbatim | SUPPORTED | Quoted fragment is an exact substring. |
| M7 | "the chips must combine partial results into one (a reduction) and hand out copies of pieces (a gather) to keep going `[0036]`, `[0037]`, `[0039]`" | `[0036]`: reduction/gather named as the two data-sharing types. `[0037]`: reduction = combine sub-results. `[0039]`: gather = copy data. | SUPPORTED | Invention-summary flags these as "definitional paragraphs made explicit...notation only, no new quote rows" — confirmed accurate against primary text directly. |
| M8 | "Route everything through a networking switch that lets any chip talk to any chip `[0032]`, which the filing calls 'expensive to include in a system that performs tensor operations' `[0026]`" | `[0032]`: switch "enables communication between any one...with any other one." `[0026]` (q-0026-1) verbatim quote. | SUPPORTED | |
| M9 | "Or wire every chip to every other chip, a point-to-point scheme whose connection count balloons as the group grows `[0130]`" | `[0130]` (q-0130-2): point-to-point = "every processing device is coupled to every other processing device," contrasted as costing more connections. | SUPPORTED | "Balloons" is color, but directionally correct (full mesh scales combinatorially; patent's own point is the claimed scheme reduces connections vs. this alternative). |
| M10 | "the odd-numbered chips form the first set (710a) and the even-numbered chips the second (710b) `[0126]`" | `[0126]`: 710a = A1,A3,A5,A7 (odd); 710b = A0,A2,A4,A6 (even) | SUPPORTED | |
| M11 | Blockquote: claim-1 negative-limitation clause, cited "claim 1, `[0386]`" | Claim 1 body / `[0386]` (q-0386-1) — identical wording in both places | SUPPORTED | Verbatim, character-for-character, against both the CLAIMS section and `[0386]`. |
| M12 | "Chips in the same set have no direct channel between them `[0128]`, so a message...rides through one chip...two hops...never more `[0130]`" | `[0128]` (q-0128-1); `[0130]` (q-0130-1): "at most two communication hops" | SUPPORTED | |
| M13 | "Claim 1 makes that bound a requirement...'through at most one other of the plurality of processing devices' `[0387]`" | `[0387]` verbatim | SUPPORTED | |
| M14 | "The relay need not even hold the message...may begin forwarding data before it has finished receiving it `[0143]`" | `[0143]` (q-0143-1): "may send the received data...before all the data...is received." | SUPPORTED | |
| M15 | "the fixed topology 'may be used to reduce data sharing...and thereby help to reduce a processing time' `[0124]`" | `[0124]` (q-0124-1) verbatim | SUPPORTED | |
| M16 | "Each set subdivides into two groups of chips, labeled 712a through 712d `[0135]`, `[0136]`, and the channels split...into two families `[0138]`, `[0139]`" | `[0135]`: names groups 712a-d. `[0136]`: each set includes two groups. `[0138]`/`[0139]`: two channel families. | SUPPORTED | |
| M17 | "The first communication channels (730) pair the groups straight across, 712a with 712c and 712b with 712d `[0138]`" | `[0138]`: "712a...directly communicatively coupled with...712c via...730 and...712b...with...712d via...730." | SUPPORTED | Also visually confirmed in fig-07A.png. |
| M18 | "The second communication channels (740) run the criss-cross: 712a with 712d, 712b with 712c `[0139]`" | `[0139]`: "712a...coupled with...712d via...740 and...712b...with...712c via...740." | SUPPORTED | Also visually confirmed in fig-07B.png. |
| M19 | "FIG. 7A and FIG. 7B draw one family each, separated purely for legibility `[0123]`, and the dense web of FIG. 7C is the two overlaid `[0125]`" | `[0123]` (q-0123-1): subgraphs "divided...for case of illustration and explanation [sic]." `[0125]`: FIG.7C = both together. | SUPPORTED | Patent's own typo ("for case of" vs. likely "for ease of") is not repeated by the essay (essay paraphrases as "purely for legibility," doesn't quote the typo) — correct handling. |
| M20 | Caption FIG.7A: "group 712a wired to every chip of 712c, and 712b to every chip of 712d `[0138]`" | `[0138]` | SUPPORTED | Visually confirmed: a0/a2 (712c) ↔ a1/a3 (712a), 4 edges; a4/a6(712d) ↔ a5/a7(712b), 4 edges. |
| M21a | Caption FIG.7B, sentence 1: "the criss-cross, 712a to 712d and 712b to 712c `[0139]`" | `[0139]` | SUPPORTED | Visually confirmed (hourglass crossing pattern between top and bottom quadrants). |
| M21b | Caption FIG.7B, sentence 2: "Added to FIG. 7A's links it gives the full FIG. 7C web `[0123]`, `[0125]`" | `[0123]`, `[0125]` | SUPPORTED | |
| M22 | "Which physical family carries which is the description's worked example rather than a claim requirement, with gather traffic on the first channels and reduction traffic on the second `[0140]`" | `[0140]` (q-0140-1): "the first operation may be a data gather operation and the second...a data reduction operation," tied to channels 730/740 respectively. | SUPPORTED | High-precision sentence: claim 11 independently labels first-sub-op=reduction/second=gather (opposite ordinal from `[0140]`'s worked example). The essay correctly attributes the *specific 730=gather/740=reduction pairing* to `[0140]` only, and does **not** claim this pairing is what claim 11 requires — exactly right given the claim/spec do not share the same first/second convention here. |
| M23 | Blockquote `[0140]`: "During the second operation, data may only be transmitted...using the second communication channels 740 and not the first communication channels 730." | `[0140]` (q-0140-2) verbatim | SUPPORTED | Verbatim incl. the source's odd pre-period spacing. |
| M24 | "Claim 9 has the two sub-operations running in overlapping time periods, one channel family carrying each `[0142]`" | `[0142]` (q-0142-1) + claim 9 text: "...in overlapping time periods such that first data...is transferred over the first subset...at the same time second data...over the second subset." | SUPPORTED | |
| M25 | "The tensors are pre-cut so that...'the same amount of data may be shared by each of the processing devices A0-A7', and the same amount crosses each channel `[0168]`, `[0178]`" | `[0168]` (q-0168-1) verbatim; `[0178]`: same statement for the first-channel-family case. | SUPPORTED | |
| M26 | "for eight chips, p and q...come out to about 4.35 and about 1.84 `[0061]`" | `[0061]` (q-0061-1): "p=4.35235, q=1.83809." | SUPPORTED | Rounding is accurate (1.83809→1.84). |
| M27 | "Rounded to divisors, that is 4 and 2, and the practical reading is that the whole input matrix lives spread across four of the eight chips `[0061]`" | `[0061]` (q-0061-2): "p and n may be selected to be divisors of n...p=4 and q=2...an entirety of the input matrix is found on 4 of the 8 processing devices." | SUPPORTED | See §4 "lowest-confidence" list — legitimate paraphrase, but the p/q tensor-preparation math is genuinely dense and this is the compressed version. |
| M28 | "No link runs hot. The equal channels are wired in, and the equal traffic follows from the split the description prescribes `[0168]`" | `[0168]` | SUPPORTED | |
| M29 | "the AI model of FIG. 9A 'may be representative of a large language model or a transformer decoder' `[0251]`" | `[0251]` (q-0251-1) verbatim | SUPPORTED | |
| M30 | "Its decoding layers, the loop that infers one token at a time `[0259]`, run normalization, then self-attention (QKV generation and attention computation), then projection, then an MLP `[0252]`, `[0254]`" | `[0252]`: layer order = normalization→self-attention→projection→MLP. `[0254]`: self-attention includes QKV generation 916 + attention computation 918. `[0259]`: layers repeat, then decoding selects "the next token." | SUPPORTED | Layer order and sub-components match exactly; see §4 for confidence note on the `[0259]` compression. |
| M31 | "From there the work hands off to decoding, the token pick `[0259]`" | `[0259]`: "the decoding 930 may include the AI model 900 selecting a token for outputting as the next token." | SUPPORTED | |
| M32 | Caption FIG.9A: "the decoding-layer loop the description maps onto the group `[0252]`, `[0259]`" | `[0252]`, `[0259]` | SUPPORTED | Visually confirmed against fig-09A.png (AI Model 900 → Decoding Layers 905 → Normalization/Self-Attention(QKV+Attn-Comp)/Projection/MLP → Decoding 930). |
| M33 | "'during the feedforward operation, the number of elements involved in a specific computation may be four times the depth of the transformer model' `[0313]`" | `[0313]` (q-0313-2) verbatim | SUPPORTED | |
| M34 | "MLP calculations can run four times greater than the model's other computations `[0258]`, which inflates processing time, or the bandwidth needed to hold processing time flat `[0313]`" | `[0258]` (q-0258-1): "four times greater than other computations." `[0313]`: "processing time...may be much larger...and/or a data bandwidth required to maintain a processing time...may be increased." | SUPPORTED | "Hold processing time flat" is an accurate colloquial gloss of "maintain a processing time." |
| M35 | "The description offers exactly that operation as a basis for sizing the tensor parallel group `[0121]`" | `[0121]` (q-0121-1): "size of the tensor parallel groups 620 may be based on the computations performed by the feedforward operations...of an MLP layer" | SUPPORTED | |
| M36 | Blockquote `[0278]`: "the tensors used during the decoding layers 905 may remain split and distributed...such that no one processing device may include the entirety of a tensor..." | `[0278]` (q-0278-1) verbatim | SUPPORTED | Verbatim, incl. source spacing quirk. |
| M37 | "the Q, K, and V matrices are processed as tiles, on different chips, 'without rejoining the tiles of the self-attention tensors Q, K, and V on a single processing device' `[0267]`" | `[0267]` (q-0267-1) verbatim | SUPPORTED | |
| M38 | "The description says the channels...can be PCIe, SPI, ethernet, UCIe, or other wired or optical links `[0134]`...and the chips can sit on separate dies `[0133]`" | `[0134]` (q-0134-1): PCIe/SPI/ethernet/UCIe/other wired/optical. `[0133]`: "may be formed on a separate die." | SUPPORTED | "the ordinary buses commodity hardware already uses" is the essay's own gloss (uncontroversial technical characterization of PCIe/ethernet/SPI/UCIe), not attributed to the patent as a quote. |
| M39 | "The patent's own stated wins are fewer connections than a full mesh `[0130]` and less data sharing in less processing time `[0124]`..." | `[0130]` (q-0130-2); `[0124]` (q-0124-1) | SUPPORTED | |
| M40 | **[design-around #1]** "A rack that keeps its networking switch, the filing's own foil `[0032]`, in place of the claimed direct channels sits outside claim 1." | `[0032]` names the switch as an alternative coupling method; claim 1's negative limitation (`[0386]`) forbids the claimed channels from coupling same-set devices | SUPPORTED | See §2 (Claim-scope sub-table, design-around callout) for the full claim-text walk-through — this is the passage the task flagged for extra scrutiny. |
| M41 | "Both require channels that couple the sets 'without communicatively coupling any of the plurality of processing devices in the same set' `[0386]`" | `[0386]` verbatim (partial, truncated before trailing "of the plurality of processing devices" — valid partial quotation) | SUPPORTED | |
| M42 | "the discipline underneath it: cross-set-only direct channels `[0386]`, degree- and bandwidth-uniform links (claims 3 to 5), and reduce and gather running simultaneously on disjoint channel families (claims 8, 9, 11)" | `[0386]`; claims 3-5; claims 8,9,11 | SUPPORTED | Claim-ref portion verified in §2. |
| M43 | "the whole fence is the wiring discipline the patent's own cluster-scale arithmetic runs on `[0168]`, `[0061]`" | `[0168]`, `[0061]` | SUPPORTED | |
| M44 | "claim 1 sets one: at most one device between any two chips, ever `[0387]`" | `[0387]` | SUPPORTED | |
| M45 | "FIG. 6 shows a host, two tensor parallel groups, and a memory 630 `[0112]` whose role is to 'provide tensors and other data to the tensor parallel groups 620 for processing' `[0119]`" | `[0112]`: host 602 + processing system 610 (620a,620b,630). `[0119]` (q-0119-1) verbatim. | SUPPORTED | Visually confirmed against fig-06.png. |
| M46 | "The description also lets each chip couple to memory devices, shared among the chips or not, and no claim picks that option up `[0133]`" | `[0133]`: "coupled to one or more memory devices...shared or...not shared." | SUPPORTED | "No claim picks that option up" independently confirmed true — none of claims 1-23 recite any memory element. |
| M47 | Caption FIG.6: "box 630, the memory that feeds the tensor parallel groups, described in one embodiment figure and never claimed `[0119]`" | `[0119]` | SUPPORTED | Visually confirmed; "never claimed" independently verified (no claim mentions memory). |
| M48 | "The specification's summary covers two sets of 'two or more' devices `[0385]`, while granted claims 1 and 14 require four or more per set" | `[0385]` (q-0385-1) verbatim "two or more" (×2); claims 1 & 14 body text say "four or more" | SUPPORTED | The exact narrowing invention-summary flags as a required pairing (§Quote anchor table note) — correctly paired here. |
| M49 | "Reduce and gather traffic run at the same time on separate channel families `[0142]`, over equal-bandwidth links (claim 5), with the same load on every link under the description's prescribed split `[0168]`" | `[0142]`; claim 5 ("same data bandwidth"); `[0168]` | SUPPORTED | |
| M50 | "The whole arrangement exists to cut data sharing and processing time `[0124]`" | `[0124]` | SUPPORTED | |
| M51 | "the wiring either matches claim 1's cross-set pattern `[0386]` or it does not" | `[0386]` | SUPPORTED | Forward-looking/conditional — does not assert current conformity, only that it will be checkable. |
| M52 | "The specification enumerates three example families, methods, topology, and AI-model computation `[0336]`, `[0337]`, `[0384]`, `[0418]`" | `[0336]`: introduces numbered-example convention. `[0337]`: Example 1 = "method of performing tensor operations." `[0384]`: Example 2 = "a tensor parallel group." `[0418]`: Example 3 = "method of performing computations for artificial intelligence models." | SUPPORTED | Independently re-confirmed the methods/topology/AI-model-computation mapping by re-reading all four paragraphs directly (matches invention-summary's own cross-check annotation). |

**Row count, main table: 54** (M21 and M40 onward continue the sequence; two-part rows M21a/M21b and one design-around-adjacent grouping counted individually — 54 distinct anchored sentences total, incl. 6 caption sentences carrying `[dddd]` tags and 3 long blockquotes).

Every row above: **SUPPORTED**. Zero UNSUPPORTED / MISREAD / OVERREACHED-BEYOND-ANCHOR in the main anchor table.

---

## 2. Claim-scope statements vs CLAIMS + Claim scope map

Every claim-referencing sentence that does not carry its own `[dddd]` tag, checked against the
**primary CLAIMS text** (read in full, all 23 claims) and the invention-summary's Claim scope
map.

| # | Essay statement | Claim text (verbatim, key clause) | Verdict |
|---|---|---|---|
| CL1 | "None of its claims mention latency, a bandwidth magnitude, or memory." | Confirmed by direct read of claims 1-23: no claim contains "latency," "memory," or any bandwidth *value* (claim 5 only requires bandwidth *equality*). | SUPPORTED |
| CL2 | "claim 8 binds the data transfer for each sub-operation exclusively to one channel subset" | Claim 8: "...data transfer for the first sub-operation occurs only via the first subset...and data transfer for the second sub-operation occurs only via the second subset..." | SUPPORTED |
| CL3 | "Claim 11 names the pair, a reduction and a gather" (without asserting an ordinal/physical-channel mapping) | Claim 11: "...the first sub-operation is a reduction operation and the second sub-operation is a gather operation." | SUPPORTED |
| CL4 | "each device couples to the same number of chips, the same number of channels, and channels of the same bandwidth (claims 3 to 5)" | Claim 3: "coupled to a same number of the plurality of processing devices." Claim 4: "a same number of communication channels." Claim 5: "configured for a same data bandwidth." | SUPPORTED |
| CL5 | "The claims' only workload hooks are the systolic array (claim 7), matrix multiplication (claims 10 and 23), and the reduction and gather sub-operations (claims 11 and 23)" | Claim 7: "systolic array of data processing units." Claim 10: "the operation is a matrix multiplication." Claim 23: same + "first sub-operation is a reduction...second...gather." Claim 11: reduction/gather. | SUPPORTED |
| CL6 | "AI, transformers, and inference are absent from the claim language." | Confirmed by direct read: none of claims 1-23 contains "AI," "artificial intelligence," "transformer," or "inference." | SUPPORTED |
| CL7 | "Claim 1 recites a wiring pattern and nothing else." | Claim 1's three limitations (two 4+-device sets; cross-set-only direct channels; ≤1-intermediate-hop reachability) are all topology/wiring elements — no other subject matter. | SUPPORTED |
| CL8 | "No granted claim recites a latency figure or a bandwidth magnitude, and claim 5 requires equal bandwidth across channels, not high bandwidth." | Claim 5 exact text: "...configured for a same data bandwidth" — equality, no magnitude. Confirmed no claim states any numeric bandwidth/latency. | SUPPORTED |
| CL9 | "The third independent, claim 18, keeps the two-or-more floor but pays for it in structure: each set must contain two device groups, wired in at least the dual-family pattern of FIGS. 7A and 7B, with each sub-operation's traffic confined to its own family." | Claim 18: "...first set of two or more...that includes a first group...and a second group...second set of two or more...that includes a third group...and a fourth group; ...first communication channels to...couple...group[1]...to...group[3]...and...group[2]...to...group[4]...; ...second communication channels to...couple...group[1]...to...group[4]...and...group[2]...to...group[3]...; ...data transfer for the first sub-operation occurs only via the...first communication channels and...second...only via the...second communication channels." | SUPPORTED |
| CL10 | "Three independents, three different trades of breadth for structure, and none of them mentions memory." | Independent claims = 1, 14, 18 (confirmed: all other 20 claims are explicitly dependent, "The tensor parallel group of claim X" / "The system of claim X"). None recite memory. | SUPPORTED |
| CL11 | "The specification's summary covers two sets of 'two or more' devices `[0385]`, while granted claims 1 and 14 require four or more per set." | Claim 1 & 14 body: "a first set of **four or more**...and a second set of **four or more**..." vs. `[0385]`: "two or more." | SUPPORTED |

### Design-around passage (§6) — the three readings flagged for extra scrutiny

**Claim 1** (verbatim): *"A tensor parallel group comprising: a plurality of processing devices separated into a first set of four or more...and a second set of four or more...; and a plurality of communication channels to directly communicatively couple every processing device in the first set...with every processing device in the second set...without communicatively coupling any of the plurality of processing devices in the same set...; wherein the plurality of processing devices are configured such that each...is able to communicate with any of the other...through at most one other..."*

**Claim 14** (verbatim, same structure as claim 1, wrapped in "A system comprising: a plurality of tensor parallel groups, each...comprising:").

**Claim 18** (verbatim): *"A tensor parallel group comprising: a plurality of processing devices separated into a first set of two or more...that includes a first group...and a second group...and a second set of two or more...that includes a third group...and a fourth group...; a plurality of first communication channels to directly communicatively couple every processing device in the first group...to every...in the third group...and...second group...to...fourth group...; and a plurality of second communication channels to...couple...first group...to...fourth group...and...second group...to...third group...; wherein the plurality of processing devices are configured to perform an operation that includes a first sub-operation and a second sub-operation, wherein data transfer for the first sub-operation occurs only via the...first communication channels and...second...only via the...second communication channels."* — **note: claim 18 contains no "without communicatively coupling...in the same set" clause.** That clause is added only by dependent **claim 19**: *"...wherein the plurality of first and second communication channels directly communicatively couple every processing device in the first set...with every...in the second set...without communicatively coupling any...in the same set..."*

| # | Reading | Verdict | Reasoning |
|---|---|---|---|
| CL-DA1 | **"in place of" switch reading**: "A rack that keeps its networking switch...in place of the claimed direct channels sits outside claim 1." | SUPPORTED | Claim 1's negative limitation forbids the claimed channels from coupling any same-set pair. A shared any-to-any switch fabric (the patent's own named alternative at `[0026]`/`[0032]`) would let same-set devices reach each other through the switch — i.e., it produces exactly the coupling claim 1 requires be absent, and it does not instantiate the "plurality of communication channels" performing the specific cross-set/no-intra-set discipline claim 1 recites. The patent itself frames "fixed topology" and "data switch" as alternative, mutually exclusive system types (`[0026]`). Reasonable, non-overreaching inference — this is the essay's most legally-inferential sentence in the piece, appropriately un-hedged given how directly it follows from the claim's own negative limitation. |
| CL-DA2 | **Negative-limitation superset reading of claims 1/14**: "A rack that copies the pattern but adds links inside a set arguably steps outside claims 1 and 14 as written." | SUPPORTED | Claim 1/14's "without communicatively coupling any...in the same set" is a hard structural exclusion, not merely a description of a claimed subset of channels — adding *any* extra direct intra-set link creates the exact coupling the claim requires be absent. Correctly hedged with "arguably" (a hedge the composer chose, not one I am recommending — outside my jurisdiction to add or remove). |
| CL-DA3 | **Claim-18/8/9/11 "configured-to" characterization**: "claim 18...tolerates the added links but, like the scheduling claims (8, 9, 11), binds only traffic routed the claimed way, a firmware choice." | SUPPORTED | Confirmed by direct claim-text comparison: claim 18 (independent) has **no** same-set exclusion clause — that is added only by dependent claim 19, which the essay does not invoke here. So a design with extra intra-set links, which falls outside claims 1/14 (CL-DA2) and outside claim 19, can still satisfy claim 18's own (narrower) limitations, which only require the four-group cross-family wiring plus the "data transfer...occurs only via..." traffic-binding language shared in structure with claims 8/9 ("...data transfer for the first sub-operation occurs only via..."). This is a materially correct, non-obvious claim-differentiation point. "Firmware choice" is the essay's own explanatory label (the patent never uses the word "firmware") for how a *behavioral* "configured to transmit only via X" limitation is typically satisfied — an interpretive gloss, not an added scope assertion, so it does not cross into overreach. |

Zero non-SUPPORTED verdicts in the claim-scope sub-table.

---

## 3. External facts vs fact-check-log + attribution style

| # | External fact in essay | fact-check-log match | Tier | Attribution in essay | Verdict |
|---|---|---|---|---|---|
| EX1 | Stealth-exit X thread, early July 2026 | essay-context.md News-moment | n/a (public event) | Stated as event, not a content-claim; fine unhedged | SUPPORTED |
| EX2 | "every number in them is the company's own account" + list: A0 tapeout, first racks built/ship summer 2026, $1B+ contracts, $800m raised | `etched-lvi-biz-thread-2026-07` | tier-1 | Blanket attribution sentence precedes the list — valid attribution style (equivalent to repeating "the company says" for each figure) | SUPPORTED |
| EX3 | CSM quotes: "shared low-latency memory pool across the entire scale-up domain"; "proprietary ultra-low-latency, high-bandwidth interconnect" | `etched-csm-thread-2026-07` | tier-1 | Quoted verbatim, framed as the thread's claim under examination | SUPPORTED |
| EX4 | "each memory layer inherently adds latency; thus, the best layer is no layer" | `etched-csm-thread-2026-07` | tier-1 | Quoted verbatim, "the thread's cleanest line" | SUPPORTED |
| EX5 | Filed 22 Oct 2024, granted 15 July 2025 ("inside nine months"); Gavin Uberti sole inventor/co-founder+CEO; 23 claims, 3 independent, 16 figures | `etched-family-trio-wips` | tier-2 | Stated directly (bibliographic, tier-2) | SUPPORTED — independently recomputed the interval myself: 266 days exactly, ≈8.74 months, "inside nine months" is arithmetically correct |
| EX6 | Sibling identity + division of labor (903 = tile-movement method, granted May 2025; 262 = model-level execution, granted same July day) | `etched-family-trio-wips` | tier-2 | Stated directly | SUPPORTED |
| EX7 | PCT filings + 2026 US continuations + expected term to Oct 2044 | `etched-family-trio-wips` | tier-2 | Stated directly | SUPPORTED |
| EX8 | "Low-Voltage Inference is nowhere in this filing **or its granted siblings**. The same goes for the power-delivery work, the cold plates, and the HBM/SRAM hybrid...that the thread folds into CSM." | essay-context.md Scope-boundaries (verbatim source of this framing) — **but no fact-check-log row independently verifies the *siblings'* full claim text is free of this content**; only patent 091 has been read in full in this run | tier-2 for 091 itself; **unlogged for the sibling extension** | Implicit ("or its granted siblings" asserted with full confidence) | **PARTIALLY UNSUPPORTED — see Finding sa3G-F1.** The "this filing" portion is fully supported (091 read cover-to-cover, zero mention of voltage/power/cold-plates/HBM-SRAM). The "or its granted siblings" portion rests on essay-context's assertion + title plausibility ("Performance of tensor operations," "Tensor operations in AI models"), not on independent review of 903/262's claims — no fact-check-log row carries this specific negative claim about the siblings' content. |
| EX9 | "The company says its math blocks run at under half the voltage of typical AI chips" | `etched-lvi-biz-thread-2026-07` | tier-1 | Explicitly attributed, "the company says" | SUPPORTED — model example of correct attribution discipline |
| EX10 | "US applications can stay unpublished for up to 18 months after filing" | `us-18month-publication-window` | tier-2 | Stated as general legal fact | SUPPORTED (this exact row was itself added to the log during round-1 self-audit, finding sa1G-F9, per the log's own Notes — registry hygiene already exercised once on this sentence) |
| EX11 | "The company says its first systems ship in summer 2026" | `etched-lvi-biz-thread-2026-07` | tier-1 | Explicitly attributed | SUPPORTED |
| EX12 | Sources-section bibliographic block (3 patents + thread) | `etched-family-trio-wips` + patent.md header | tier-2 / primary | N/A (citation list) | SUPPORTED |

**External-fact tally: 12 checked, 11 SUPPORTED, 1 PARTIALLY UNSUPPORTED (EX8).**

---

## 4. Figure captions vs manifest + cited paragraphs (+ direct image inspection)

All 6 placed figures were opened directly (not just cross-checked against manifest text) to
verify spatial/visual claims a text-only gate cannot see.

| # | Figure | Caption claim | Manifest match | Paragraph match | Image-verified | Verdict |
|---|---|---|---|---|---|---|
| FIG-A | 7C (header) | Set membership + left/right placement + 16 edges + no intra-column wire + both families overlaid | "Combined view overlaying both sub-graph patterns 730 and 740 on the same 8 devices" | `[0125]`,`[0126]`,`[0128]`,`[0129]` | Yes — 710a right/710b left confirmed; counted 16 cross edges, 0 intra-column edges | SUPPORTED |
| FIG-B | 1 | "processing devices built as systolic arrays" (unanchored caption) | "Block diagram...four processing devices 110a-d, each with a systolic array 112a-d and processing elements 114a-d" | (context anchors nearby: `[0021]` et al.) | Yes — matches exactly | SUPPORTED |
| FIG-C | 7A | 712a↔712c, 712b↔712d, family 730 | "Sub-graph connection pattern 730 wiring 8 processing devices" | `[0138]` | Yes | SUPPORTED |
| FIG-D | 7B | Criss-cross 712a↔712d, 712b↔712c, family 740; union with 7A = 7C | "Denser sub-graph connection pattern 740..." (manifest's "denser" label is a P0/figures-prep artifact — visually each family has 8 edges, i.e. equal, not denser; this is a manifest-metadata nuance, not repeated or relied upon by the essay's own caption, so it does not propagate into the deliverable) | `[0139]`,`[0123]`,`[0125]` | Yes | SUPPORTED |
| FIG-E | 9A | Decoding-layer loop: normalization → self-attention (QKV+attention-computation) → projection → MLP → decoding | "Block diagram of AI model 900: decoding layers 905 (...)" | `[0252]`,`[0259]` | Yes — exact box-for-box match | SUPPORTED |
| FIG-F | 6 | Host, two tensor-parallel groups, memory 630 — "described...never claimed" | "host 602 connected to processing system 610 containing first/second tensor parallel devices 620a/620b and memory 630" | `[0119]` | Yes | SUPPORTED |
| FIG-G | Footnote `[^figures-not-placed]` (excluded-figure audit) | 6 placed + 10 excluded (fig-02,03,04,05,08,09B,10,11,12,13) = 16 total, matches figure-selection rationale | Cross-checked vs. manifest's 16-row table and invention-summary's Figure relationships table | n/a | n/a | SUPPORTED — count and categorization both check out |
| FIG-H | Footnote `[^derived-counts]` (16 vs. 28 channels) | Flagged explicitly as "not patent text" | n/a | n/a | Independently re-derived: 4×4 complete bipartite = 16; C(8,2) full mesh = 28. Also recounted 16 edges directly on fig-07C.png. | SUPPORTED |

**Figure-caption tally: 8 checked (6 placed captions + 2 footnote/production checks), 8 SUPPORTED.**

---

## 5. Findings

### sa3G-F1 (MEDIUM) — unlogged external-fact extension to un-reviewed sibling patents

**Location:** "Low-Voltage Inference is nowhere in this filing or its granted siblings. The same
goes for the power-delivery work, the cold plates, and the HBM/SRAM hybrid...that the thread
folds into CSM." (§6, "The thread's other pillar has no fence here either" paragraph.)

**Issue:** The "this filing" portion is fully supported — patent.md (US 12,361,091 B1) was read
in its entirety in this run and contains zero mention of voltage, power delivery, cold plates,
or an HBM/SRAM hybrid. The "or its granted siblings" extension, however, makes a confident
negative claim about the full claim/spec text of US 12,306,903 B1 and US 12,361,262 B1, neither
of which is in evidence in this pipeline run (fact-check-log's `etched-family-trio-wips` row
carries only bibliographic metadata — filing/grant dates, inventor, PCT/continuation numbers —
not their substantive content). The claim traces to essay-context.md's Scope-boundaries framing
("are NOT covered by this patent or its granted siblings"), which is itself an assertion rather
than a sourced/tiered finding, and is plausible on title grounds ("Performance of tensor
operations," "Tensor operations in AI models") but not independently verified the way the
`us-18month-publication-window` fact was retroactively logged after round-1 (finding sa1G-F9).

**Recommended fix (in priority order per jurisdiction):**
1. *Better paragraph/span:* none exists — the siblings' full text is not part of this pipeline
   run's evidentiary record, so no patent span can support the "granted siblings" clause.
2. *Narrower claim the span supports:* "Low-Voltage Inference is nowhere in this filing" (cut
   "or its granted siblings"), and correspondingly narrow "The same goes for the power-delivery
   work, the cold plates, and the HBM/SRAM hybrid...that the thread folds into CSM" to the same
   filing-only scope. This is fully supported by the complete read of patent.md performed in
   this and prior grounding passes.
3. *Cut:* if the sibling-scope claim is judged essential to the paragraph's point, the
   alternative is adding a dedicated fact-check-log row (mirroring the `us-18month-publication-window`
   precedent set in round-1 finding sa1G-F9) that documents the basis for extending the
   LVI/HBM-SRAM absence claim to the two sibling patents specifically.

No other findings. Zero HIGH or CRITICAL findings.

---

## 6. Summary of verification method

- Read `input/patent.md` in full (978 lines), including every claim (1-23) verbatim, to
  independently verify claim-scope statements rather than relying solely on the invention-summary's
  Claim scope map (which was itself cross-checked against the primary claim text and found
  accurate everywhere it was tested).
- Opened and visually inspected all 6 placed figure files (fig-07C, fig-01, fig-07A, fig-07B,
  fig-09A, fig-06) to confirm spatial/visual captions (left/right set placement, edge counts,
  box layout) that no text-only gate can check.
- Independently recomputed: the 266-day filing-to-grant interval; the 16-vs-28 channel counts
  (both from the patent's own numbers and from a direct recount on the FIG. 7C image); the
  p/q rounding (1.83809 → 1.84).
- Cross-referenced every quoted fragment (3 long blockquotes + 11 inline quotes) against the
  patent text character-for-character; all verbatim.
