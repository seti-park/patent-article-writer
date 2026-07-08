# Self-Audit Round 1 — Grounding Verification (blind, mechanical fidelity only)

Draft: `handoff/03-edit/essay-final.md` (accepted essay, pending-application edition)
Inputs: `handoff/01-design/invention-summary.md`, `input/patent.md`, `handoff/01-design/fact-check-log.md`,
`input/essay-context.md`, `input/figures/figures-manifest.md` + source images `input/figures/fig-0{1,2,5,6,7}.png`.

Jurisdiction: fidelity only. No comment on tone/hedging/structure. Recommendations restricted to
anchor / narrow / label / cut.

## 0. Mechanical gates

```
$ python .claude/skills/_shared/scripts/gate_quotes.py handoff/03-edit/essay-final.md \
    --invention-summary handoff/01-design/invention-summary.md --patent input/patent.md
[PASS] gate=quotes
  (no findings)

$ python .claude/skills/_shared/scripts/gate_anchors.py handoff/03-edit/essay-final.md \
    --invention-summary handoff/01-design/invention-summary.md --figures handoff/01-design/figures-index.txt
[PASS] gate=anchors
  (no findings)
```

Both mechanical gates are clean. Everything below is the manual layer the gates cannot do:
paragraph-precision, claim-scope/edition-verb discipline, external-fact attribution, and
figure-caption-vs-image verification.

## 1. Full anchor-by-anchor fidelity table (every `[dddd]`-anchored sentence, in document order)

| seq | section | sentence (operative clause) | anchor(s) | patent check (operative words) | verdict | note |
|---|---|---|---|---|---|---|
| S1 | Header/FIG.5 caption | "each independent channel (510A to 510D) runs over its own wires (520) straight into a dedicated column (515A to 515D) of the chip's systolic array (220)" | [0044] | "the independent channels 510 can be directly wired... to a particular column 515... the column 515A... connected... to the channel 510A in memory chip 505A, the column 515B is hardwired to the channel 510B..." | SUPPORTED | Matches [0044] and the FIG. 5 image exactly (505A→510A/510B; 505B→510C/510D → 515A-D). |
| S2 | Header/FIG.5 caption | "This is the interface the application claims, as drafted, in claim 39" | [0016] | [0016] text is substantively identical to claim 39's text ("a separate memory device comprising a plurality of channels where each ... is hardwired ... without any switching element") | SUPPORTED | Correct application-era verb ("claims, as drafted"). [0016] and claim 39 verified word-for-word equivalent (claims §, line 171). |
| S3 | Founders section, blockquote | "a package that includes a plurality of integrated circuits (ICs)... to form a larger, combined systolic array" | [0013] | verbatim substring of [0013] | SUPPORTED | Quote gate confirms verbatim; drops only the non-quoted lead-in "Embodiments presented in this disclosure is". |
| S4 | Founders section | "a multi-chip approach where local arrays are joined by high-speed chip-to-chip links into one larger, combined array" | [0019] | "the embodiments herein adapt a multi-chip approach where multiple local systolic arrays on multiple chips... are connected using high-speed chip-to-chip connections to form a larger, combined systolic array" | SUPPORTED | Accurate paraphrase. |
| S5 | Many Small Arrays | "hardware built for algorithms that 'perform the same task with different data at different times'" | [0002] | verbatim substring of [0002] | SUPPORTED | |
| S6 | Many Small Arrays | "the task that dominates the hardware's work is matrix multiplication" | [0003] | "matrix multiplications dominate the operations that must be performed in hardware" | SUPPORTED | |
| S7 | Many Small Arrays | "Model weights (110)... enter from the top row of cells (105)" | [0021] | "The topmost row of DPUs 105 receive AI model weights 110" | SUPPORTED | |
| S8 | Many Small Arrays | "most chips top out at 'floating point systolic arrays with a size of 128×128'" | [0018] | verbatim substring of [0018] | SUPPORTED | |
| S9 | Many Small Arrays, blockquote | "it is unreasonable to expect a single chip to interface with 100s of GB of memory..." | [0018] | verbatim substring of [0018] | SUPPORTED | |
| S10 | Many Small Arrays | "Hundreds of gigabytes is the working size... no single chip realistically interfaces with that much memory" | [0018] | same [0018] passage | SUPPORTED | "roughly a whole laptop's storage" is the essay's own scale illustration, logged in footnote `derived-comparisons`. |
| S11 | Many Small Arrays | "Horizontal connections (230) and vertical connections (225) join neighboring tiles until they compute as one combined systolic array (250)" | [0019] | [0019] contains no mention of "horizontal"/"vertical" or 230/225; the horizontal/vertical distinction is taught in **[0029]** ("the package 201 includes two types of chip-to-chip connections: horizontal chip-to-chip connections 230 and vertical chip-to-chip connections 225") | **MISREAD** | Right content (230/225 are correctly identified per the invention-summary's own reference table), wrong paragraph. [0019] supports only the generic "joined... into one combined array" clause; it does not support the specific horizontal/vertical naming. Fix: cite [0029] (in addition to or instead of [0019]) for the horizontal/vertical clause. |
| S12 | Many Small Arrays | "a physical layer that 'supports up to 32 GT/s'" | [0030] | verbatim substring of [0030] | SUPPORTED | Correctly labeled "a description preference, not something claim 1 requires as drafted" — matches Claim scope map row 1 ("Connection technology (UCIe is a description preference, [0030])"). |
| S13 | Many Small Arrays | "the combined array 'appears to be one large array'" | [0028] | verbatim substring of [0028] | SUPPORTED | |
| S14 | Many Small Arrays | "adding more rows of chips adds compute without adding memory chips at the top" | [0039] | "adding more rows of ICs 215 increases the compute power of the systolic array 350, without having to add more memory chips 305 at the top..." | SUPPORTED | [0039] describes FIG. 3's package (350/305); generalizing to "chips"/"memory chips" without the figure number is explicitly pre-authorized by invention-summary q-0039-1 and footnote `figures-not-placed` (FIG. 3/4 intentionally dropped, point carried in prose). |
| S15 | Memory-interface section | "The combined array 'does not take instructions at runtime, and only executes instructions in a preset loop'" | [0027] | verbatim substring of [0027] | SUPPORTED | |
| S16 | Memory-interface, blockquote | "a switch (or some kind of switching element such as a crossbar) is typically used so that the device can access the entire memory of the HBM" | [0043] | verbatim substring of [0043] | SUPPORTED | |
| S17 | Memory-interface, blockquote | "a separate memory device comprising a plurality of channels where each... is hardwired to respective one or more columns... without any switching element" | [0016] | verbatim substring of [0016] | SUPPORTED | Correctly introduced as "mirrored in the citable summary" rather than quoted-as-claim-39, which is the accurate framing. |
| S18 | Memory-interface | "The weights streaming into the top of the array 'may be constants'" | [0021] | verbatim substring of [0021] | SUPPORTED | |
| S19 | Memory-interface | "the channels 'can be directly wired (or hardwired) to a particular column'" | [0044] | verbatim substring of [0044] | SUPPORTED | |
| S20 | Memory-interface | "'hardwiring the memory chips 505 to the columns 515 is permissible'" | [0045] | verbatim substring of [0045] | SUPPORTED | |
| S21 | Memory-interface | "'which can save space and power'" | [0045] | verbatim substring of [0045] | SUPPORTED | |
| S22 | Memory-interface | "'can enable the memory chips 305 to transmit more than 1 TB/s of data to each of the ICs'" | [0040] | verbatim substring of [0040] | SUPPORTED | Quote correctly truncated before the run-on artifact "215in" flagged in the invention-summary. |
| S23 | Memory-interface | "Claim 15 frames the system version, an AI accelerator whose memory chips, coupled to the ICs forming the top row, store the model's weights" | [0014] | [0014] text matches claim 15 verbatim in substance | SUPPORTED | |
| S24 | Memory-interface | "The filing books the gain as space and power" | [0045] | "...which can save space and power" | SUPPORTED | |
| S25 | Transformer-shaped section | "'self-attention operations use data computed from previous tokens, which means such data should be saved'" | [0047] | verbatim substring of [0047] | SUPPORTED | |
| S26 | Transformer-shaped section | "'Most of the parts of a transformer AI model do not use data from previous tokens'" | [0047] | verbatim substring of [0047] | SUPPORTED | |
| S27 | Transformer-shaped section, blockquote | "In this embodiment, the local systolic arrays 220 do not have access to the local memory chips 610." | [0051] | verbatim (NBSP-normalized) match to [0051] | SUPPORTED | |
| S28 | Transformer-shaped section | "Attention's bookkeeping gets its own circuit and its own private memory, and the two never contend for the same store" | [0051] | consistent with [0051] + [0047] | SUPPORTED | |
| S29 | Transformer-shaped section | "the filing puts the result at '98% or greater utilization of the systolic array'" | [0057] | verbatim substring of [0057] | SUPPORTED | |
| S30 | FIG.7 caption | "The only idle gap is the layer-normalization stall, marked at Time B" | [0057] | "This is shown at Time B where the array stalls..." | SUPPORTED | The preceding Time-A clause in the same caption ("at Time A a new computation has already entered while the previous one drains") carries **no anchor tag** and is not in the anchor-verdict scope, but is verified separately in §3 (figure sub-table) against [0056], which is the correct paragraph for Time A. |
| S31 | Verdict section | "claim 39's hardwired channels 'without any switching element', inverts the crossbar practice the specification itself calls typical" | [0016], [0043] | [0016] verbatim quote; [0043] crossbar-typical passage | SUPPORTED | |
| S32 | Footnote `figures-not-placed` | "their one load-bearing point, more compute rows without more memory chips, travels in prose via [0039]" | [0039] | matches S14 | SUPPORTED | Self-consistent with S14. |

**Tally: 32 anchored-sentence rows — 31 SUPPORTED, 1 MISREAD (S11).**

## 2. Sub-table 1 — Claim statements vs CLAIMS text + Claim scope map

| Claim statement in essay | Location | CLAIMS text check | Claim scope map check | Verdict | Edition-verb check |
|---|---|---|---|---|---|
| Claim 1 (indep.): "the plain combined-array package"; UCIe "not something claim 1 requires as drafted" | lines 51, 104, 112 | Claim 1 text has no UCIe/connection-tech element — confirmed a "leaves open" item | Matches row 1 exactly ("Connection technology (UCIe is a description preference...)") | SUPPORTED | "requires as drafted" — correct application-era phrasing (mirrors the map's own column header) |
| Claim 1/26 "sit closest to that [examiner-cited] art... are exactly the kind of claims that shrink in it" | line 104 | — (prosecution risk is not claim text) | Matches map's prosecution-risk notes for both row 1 and row 26 verbatim in substance | SUPPORTED | "as drafted" used; no grant-era verb |
| Claims 7 and 8 "put HBMs on that same switchless hardwiring, several of them per top-row chip" | line 73 | Claim 7: "the HBMs are hardwired to respective columns in the local systolic arrays without any switching element"; Claim 8: "multiple HBMs are hardwired to each of the plurality of ICs in the topmost row" | Matches map row "7-8" | SUPPORTED | |
| Claim 15 "an AI accelerator whose memory chips, coupled to the ICs forming the top row, store the model's weights" | line 73 | Claim 15 text matches (paraphrase of "the plurality of memory chips coupled to the plurality of ICs forming a top row... configured to store weights...") | Matches map row 15 | SUPPORTED | |
| Claims 11-13 "add auxiliary circuitry (605) beside each array tile, backed by local memory chips (610) that hold the token history... draw a boundary the arrays cannot cross" | line 83 | Claim 11 (aux. circuitry + local memory chips), Claim 12 (self-attention using previous-token data), Claim 13 ("local systolic arrays do not communicate with the local memory chips") — all three elements present | Matches map row 11-13 exactly, incl. "most transformer-specific limitation in the set" | SUPPORTED | Quote used for the "boundary" clause is [0051] (spec), correctly NOT presented as claim-13's verbatim text — precise attribution |
| Claim 39 "the likeliest survivor among the application's four independent claims" | line 112 | Claim 39 text confirmed; "four independent claims" verified by claim-by-claim scan (1, 15, 26, 39 are the only independents; all others are "The package/accelerator of claim X") | Matches map row 39 ("likeliest of the four to survive in some form") | SUPPORTED | Count-of-independents statement verified exactly correct |
| Absence statement: "The broad combined-array claims carry no AI limitation as drafted, and neither does claim 39's memory interface" | line 96 | Confirmed: claim 1, claim 26, and claim 39 text contain no AI/transformer/model term anywhere; AI first appears only in dependent claims (6, 31, 40, etc.) | Consistent with map ("ordinary drafting breadth") | SUPPORTED | |
| Edition-verb scan (whole essay) | global | grep sweep for locks/requires/grants/fences/enforc/infring/own | No instance of a grant-era verb applied to claim scope; "requires as drafted" and "enforceable"/"does not yet own" are all used to state the ABSENCE of enforceability, which is the correct direction | SUPPORTED (no edition violation found) | |

## 3. Sub-table 2 — External facts vs fact-check-log

| External fact in essay | Location | fact-check-log entry | Tier / evidence_level | Attribution style | Verdict |
|---|---|---|---|---|---|
| 1st security interest, TriplePoint, eff. 2024-04-19, reel/frame 067204/0877, covers four applications incl. two since-rejected compiler filings | line 102 | `tp-lien-1-2024` | tier-2 / registry-extract | Correct — no over-claim of selectivity | SUPPORTED |
| 2nd security interest, TriplePoint, eff. 2025-07-18, reel/frame 071792/0869, covers portfolio incl. three granted patents | line 102 | `tp-lien-2-2025` | tier-1 / registry-verified | Correct | SUPPORTED |
| "The second and third of those grants had issued three days earlier, on 15 July 2025" — motive reading explicitly flagged as inference | line 102 | `grant-lien-timing` | tier-1 (dates) / inference (motive) | Correctly labeled: "reading them... is an inference, not a record" | SUPPORTED |
| Prosecution label sentence: pending; final rejection + RCE, as of 2026-05 record | line 100 | `prosecution-record` | tier-2 / registry-extract | Consumed by exactly one label sentence per the log's budget rule | SUPPORTED |
| "The examiner has said no once" (restates the final-rejection fact a second time, in the steelman paragraph) | line 104 | `prosecution-record` | tier-2 / registry-extract | Same underlying fact as the label sentence, echoed a second time with no new chronology | **MIS-ATTRIBUTED (low)** — not a wrong fact, but the log's own discipline note reads "consumed by exactly ONE sentence... No battle narrative." A second, shorter callback isn't a battle narrative, but strict compliance would fold it into or cross-reference the existing label sentence rather than restate it. |
| Examiner-cited field: 8 references, multi-node ML acceleration / hybrid parallelism / NN accelerator architectures | line 104 | `examiner-cited-field` | tier-2 / registry-extract | Correct | SUPPORTED |
| "...which is to say the field was already crowded when the founders filed" | line 104 | `examiner-cited-field` | tier-2 / registry-extract — but the log and invention-summary Timeline table explicitly state the 8 references' own dates are "registry-external, dates not in this run's inputs" | The temporal claim ("when the founders filed") asserts a timing relationship the logged fact does not itself establish (only that 8 references exist and were examiner-cited) | **OVERREACHED-BEYOND-ANCHOR (low)** — reasonable patent-prosecution inference (examiner rejections require prior art), but goes past the bare logged fact. Recommend cutting "when the founders filed" or labeling as inference. |
| Family US-only, no PCT, no continuation — contrast with granted trio labeled as observation only | line 100 | `family-us-only` | tier-2 / bibliographic | Correctly labeled: "a bibliographic observation... proves nothing by itself about intent" | SUPPORTED |
| Thread claims: $1B+ contracts, $800M raised, summer 2026 ship, LVI/CSM pillars, memory-layer philosophy | line 21 | `etched-thread-2026-07` | tier-1 (as record) / company-claimed | Every use carries "the company says" | SUPPORTED |
| "So is the memory half that is absent from the company's granted wiring patent, US 12,361,091 B1, the subject of an earlier analysis" | line 27 | `prior-essay-wiring-half` | tier-2 / internal-prior-run | One clause of continuity, as required | SUPPORTED |
| UCIe described as "an open chip-to-chip standard" | line 51 | **no matching entry** — not in fact-check-log | unlogged | UCIe's status as an open industry standard is real-world background not sourced to the patent text (which never uses the word "open") and not present in fact-check-log.md | **UNSUPPORTED / unlogged external fact (medium)** — recommend cutting "open" (the patent-anchored content, "UCIe... physical layer that supports up to 32 GT/s," stands fine without it) or logging it with an evidence_level. |

**External-fact tally: 9 SUPPORTED, 1 low mis-attribution (echoed label), 1 low overreach (timing inference), 1 unlogged (UCIe "open").**

## 4. Sub-table 3 — Figure captions vs images + cited paragraphs

| Figure | Essay caption claim | Image check | Paragraph check | Verdict |
|---|---|---|---|---|
| FIG. 1 | "a systolic array, logically" | Image: grid of DPUs 105, Model Weights 110 top, Previous Tensor 115 left, two multiplication patterns | [0020]-[0024] | SUPPORTED (plain, unembellished) |
| FIG. 2 | "ICs 215A to 215I, each carrying an array tile (220), join through horizontal (230) and vertical (225) chip-to-chip connections into Combined Systolic Array 250. Memory chips (210A to 210C) sit only on the top row, and the host (205) connects over PCIe (240)." | Image confirms: 3×3 grid 215A-I/220A-I; 210A-C at top row only; 230 label between top-row ICs, 225 label between vertical neighbors; host 205 with PCIe 240 arrows into the array | [0025], [0028], [0029], [0034] | SUPPORTED |
| FIG. 5 (header) | Two memory chips (505A, 505B), channels 510A-D, wires 520, columns 515A-D, IC 215, array 220 | Image confirms exact topology: 505A→510A/510B; 505B→510C/510D; each channel one wire to one column 515A-D | [0043]-[0045] | SUPPORTED (see S1/S2 above) |
| FIG. 6 | "Each IC (615A to 615D) holds an array tile (220) plus an auxiliary-circuitry block (605). The local memory chips (610A to 610D) are reachable only by that auxiliary circuitry." | **Verified against the image itself, per the KNOWN DEFECT instruction.** Image shows 615A/615B/615C/615D each containing one array tile (220A, 220B, 220D, 220E) and one auxiliary-circuitry block (605A-605D); the EXTERNAL boxes labeled 610A-610D connect only to the 605 blocks via bidirectional arrows, never to the 220 tiles. This is the **opposite** of the figures-manifest's one-liner ("Local memory chips 605A-605D built into each IC block... feeding array tiles... directly"), confirming the manifest defect is real and the essay caption is correct against both the image and the specification. | [0046]-[0051], esp. [0051] "the local systolic arrays 220 do not have access to the local memory chips 610" | SUPPORTED — essay caption correctly followed the specification/image, not the defective manifest |
| FIG. 7 | "Attention queries, keys, and values, projection, and the MLP layers follow each other through the row, and at Time A a new computation has already entered while the previous one drains. The only idle gap is the layer-normalization stall, marked at Time B [0057]." | Image confirms legend order (Queries/Keys/Values/Projection/MLP Hidden/MLP Output) and the Time A / Time B axis markers, with Time B left of Time A | Time A content matches **[0056]** ("the inputs for the subsequent computation are fed into the systolic array before the previous computation completes... at Time A, the leftmost DPU... is performing the [new] computation... while the rightmost DPU... is still working on the previous computation"); Time B content matches [0057] and carries the sentence's only anchor tag | SUPPORTED | The Time-A clause carries no anchor tag in the draft, so it is out of the anchor-verdict table (§1), but it is accurate against [0056] and does not overreach — no finding needed, noted here for completeness. |

## Findings (sa1G-F*)

- **sa1G-F1 (medium)** — S11: "Horizontal connections (230) and vertical connections (225) join neighboring tiles..." is anchored to [0019], which does not mention horizontal/vertical connections or 230/225 at all; the correct paragraph is **[0029]** ("the package 201 includes two types of chip-to-chip connections: horizontal chip-to-chip connections 230 and vertical chip-to-chip connections 225"). Wrong-paragraph-right-content = MISREAD per rubric. Fix: re-anchor to [0029].
- **sa1G-F2 (medium)** — UCIe is described as "an open chip-to-chip standard" (line 51) with no corresponding fact-check-log entry; [0030] never uses the word "open." Unlogged external fact. Fix: cut "open" (the patent-anchored "32 GT/s" content needs no help from it) or add a logged entry.
- **sa1G-F3 (low)** — "The examiner has said no once" (line 104) re-states the `prosecution-record` fact a second time outside the log's declared "consumed by exactly ONE sentence" budget. Not a battle narrative and not a new fact, but strict compliance would fold the callback into/cross-reference the existing label sentence rather than restate the underlying fact. Fix: cut the standalone restatement or make it explicitly refer back to the earlier label sentence.
- **sa1G-F4 (low)** — "which is to say the field was already crowded when the founders filed" (line 104) asserts a timing relationship (crowded *at the time of filing*) that the logged `examiner-cited-field` fact does not itself establish — the invention-summary's own Timeline table notes the 8 references' dates are "registry-external, dates not in this run's inputs." A defensible patent-prosecution inference, but goes beyond the bare logged fact. Fix: cut "when the founders filed" or label the timing as inference.

No critical or high findings. No claim-1/claim-39/spec block-quote failed verbatim verification. No grant-era/enforceability verb was found applied to claim content anywhere in the essay (edition discipline holds). The FIG. 6 caption is confirmed correct against the image itself, resolving the manifest's known defect in the essay's favor.
