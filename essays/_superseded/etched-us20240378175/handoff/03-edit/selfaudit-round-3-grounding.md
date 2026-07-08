# Self-Audit Grounding Verification — Round 3 (FINAL dry-check)

**Draft under review:** `handoff/03-edit/essay-final.md` (draft_version 5)
**Blind inputs only:** invention-summary.md (incl. q-0056-1 + PENDING-edition Claim scope map),
patent.md, fact-check-log.md, essay-context.md, figures-manifest.md (known FIG. 6 605/610 swap).
No edit logs / revision notes / prior self-audit reports were consulted.

---

## 1. Mechanical gates

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

Both mechanical gates are clean. Every invention-summary "verbatim" quote is present in
patent.md, and every draft `[dddd]` anchor traces to the invention-summary. This is the floor,
not the ceiling — the tables below do the judgment-level work the gates cannot.

---

## 2. Anchor-by-anchor fidelity table (every `[dddd]`-anchored clause, incl. captions/blockquotes)

36 anchor instances in the draft. Multi-anchor sentences are split per clause (matching the
brief's instruction to check FIG. 7's dual anchors clause-by-clause; applied consistently
elsewhere).

| # | Loc | Sentence / clause (anchor) | Invention-summary span leaned on | Patent paragraph | Verdict | Fix |
|---|---|---|---|---|---|---|
| 1 | L15 cap. | "...each independent channel (510A to 510D) runs over its own wires (520) straight into a dedicated column (515A to 515D) of the chip's systolic array (220) **[0044]**." | q-0044-1: "the independent channels 510 can be directly wired (or hardwired) to a particular column 515..." | [0044]: "the columns 515 of DPUs...can be hardwired to a particular channel 510...the column 515A...connected...to the channel 510A in memory chip 505A..." | SUPPORTED | — |
| 2 | L15 cap. | "This is the interface the application claims, as drafted, in claim 39 **[0016]**." | q-0016-1 (verbatim = claim 39 body almost word for word) | [0016] / Claim 39 | SUPPORTED | — |
| 3 | L33-34 | Blockquote: "a package that includes a plurality of integrated circuits (ICs)...to form a larger, combined systolic array" **[0013]** | q-0013-1 | [0013] verbatim | SUPPORTED (gate_quotes-verified) | — |
| 4 | L36 | "The filing frames this as the way past single-chip limits, a multi-chip approach where local arrays are joined by high-speed chip-to-chip links into one larger, combined array **[0019]**." | q-0019-1 | [0019]: "a multi-chip approach where multiple local systolic arrays on multiple chips...are connected using high-speed chip-to-chip connections to form a larger, combined systolic array" | SUPPORTED | — |
| 5 | L40 | "...hardware built for algorithms that 'perform the same task with different data at different times' **[0002]**." | q-0002-1 | [0002] verbatim | SUPPORTED | — |
| 6 | L40 | "For transformer-style AI models...the task that dominates the hardware's work is matrix multiplication **[0003]**." | q-0003-1 | [0003]: "For many...AI applications (e.g., transformer models), matrix multiplications dominate the operations..." | SUPPORTED (narrowed framing) | Lower-confidence: [0003] scopes to "many AI applications (e.g. transformer models)," not transformer-exclusive; essay's "For transformer-style AI models" reads as if the paragraph is transformer-scoped. Not a meaning change (transformers are the named example) — no fix required, flagged for visibility only. |
| 7 | L40 | "Model weights (110)...enter from the top row of cells (105) **[0021]**." | q-0021-1 | [0021]: "The topmost row of DPUs 105 receive AI model weights 110..." | SUPPORTED | — |
| 8 | L42 cap. | "Weights (110) come down from the top **[0021]**, data (115) comes in from the left, and every crossing of the two is a multiply-and-add." | q-0021-1 | [0021] covers weights-from-top AND tensor-from-left (both in same paragraph); "multiply-and-add" is [0003]/[0020]'s MAC description, already anchored one clause earlier in the same paragraph (row 6) | SUPPORTED | Lower-confidence: the caption's third clause is sourced from a different paragraph than the one tagged; harmless since [0003]'s MAC content is already anchored in the surrounding prose. |
| 9 | L44 | "...most chips top out at 'floating point systolic arrays with a size of 128×128' **[0018]**." | q-0018-1 | [0018] verbatim | SUPPORTED | — |
| 10 | L46-47 | Blockquote: "it is unreasonable to expect a single chip to interface with 100s of GB of memory used to store parameters and intermediate computation values" **[0018]** | q-0018-2 | [0018] verbatim | SUPPORTED (gate_quotes-verified) | — |
| 11 | L49 | "...the filing's premise is that no single chip realistically interfaces with that much memory **[0018]**." | q-0018-2 | [0018] | SUPPORTED | — |
| 12 | L51 | "Horizontal connections (230) and vertical connections (225) **[0029]** join neighboring tiles..." | (implicit — [0029] paragraph itself, not in Quotable-span list, but reference-number table maps 225/230 to [0029]) | [0029]: "the package 201 includes two types of chip-to-chip connections: horizontal chip-to-chip connections 230 and vertical chip-to-chip connections 225." | SUPPORTED | — |
| 13 | L51 | "...until they compute as one combined systolic array (250) **[0019]**." | q-0019-1 | [0019] | SUPPORTED | — |
| 14 | L51 | "...with a physical layer that 'supports up to 32 GT/s' **[0030]**." | q-0030-2 | [0030] verbatim ("...supports up to 32 GT/s with 16 to 64 lanes") | SUPPORTED | — |
| 15 | L51 | "...the combined array 'appears to be one large array' **[0028]**." | q-0028-1 | [0028] verbatim | SUPPORTED | — |
| 16 | L51 | "...adding more rows of chips adds compute without adding memory chips at the top **[0039]**." | q-0039-1 | [0039] | SUPPORTED | — |
| 17 | L55 | "...the combined array 'does not take instructions at runtime, and only executes instructions in a preset loop' **[0027]**." | q-0027-1 | [0027] verbatim | SUPPORTED | — |
| 18 | L61-62 | Blockquote: "a switch (or some kind of switching element such as a crossbar) is typically used so that the device can access the entire memory of the HBM" **[0043]** | q-0043-1 | [0043] verbatim | SUPPORTED (gate_quotes-verified) | — |
| 19 | L67-69 | Blockquote: "a separate memory device comprising a plurality of channels where each of the plurality of channels is hardwired to respective one or more columns in the systolic array without any switching element" **[0016]** | q-0016-1 | [0016] verbatim | SUPPORTED (gate_quotes-verified) | — |
| 20 | L71 | "The weights streaming into the top of the array 'may be constants' **[0021]**, so a given column always eats the same slice of the model, and a rerouting layer buys nothing." | q-0021-1 | [0021] quote verbatim; the added clause ("eats the same slice...buys nothing") is an inferential gloss, not itself patent text | SUPPORTED | Lower-confidence: the causal gloss is essay-authored reasoning layered on the quote, consistent with [0044]/[0045]'s "same weights...same columns" rationale but not a direct restatement. |
| 21 | L71 | "...the channels 'can be directly wired (or hardwired) to a particular column' **[0044]**" | q-0044-1 | [0044] verbatim (truncated before "515", per the anchor-artifact note) | SUPPORTED | — |
| 22 | L71 | "...concludes that 'hardwiring the memory chips 505 to the columns 515 is permissible' **[0045]**" | q-0045-1 | [0045] verbatim | SUPPORTED | — |
| 23 | L71 | "...books the deletion as a gain, 'which can save space and power' **[0045]**." | q-0045-2 | [0045] verbatim | SUPPORTED | — |
| 24 | L71 | "...the arrangement 'can enable the memory chips 305 to transmit more than 1 TB/s of data to each of the ICs' **[0040]**." | q-0040-1 | [0040] verbatim | SUPPORTED | — |
| 25 | L73 | "Claim 15 frames the system version, an AI accelerator whose memory chips, coupled to the ICs forming the top row, store the model's weights **[0014]**." | q-0014-1 | [0014] mirrors Claim 15 almost verbatim | SUPPORTED | — |
| 26 | L75 | "The 2023 filing books the gain as space and power **[0045]**." | q-0045-2 | [0045] | SUPPORTED | — |
| 27 | L79 | "'self-attention operations use data computed from previous tokens, which means such data should be saved' **[0047]**." | q-0047-1 | [0047] verbatim | SUPPORTED | — |
| 28 | L79 | "'Most of the parts of a transformer AI model do not use data from previous tokens' **[0047]**." | q-0047-2 | [0047] verbatim | SUPPORTED | — |
| 29 | L83-84 | Blockquote: "In this embodiment, the local systolic arrays 220 do not have access to the local memory chips 610." **[0051]** | q-0051-1 | [0051] verbatim | SUPPORTED (gate_quotes-verified) | — |
| 30 | L86 | "...and the two never contend for the same store **[0051]**." | q-0051-1 | [0051] | SUPPORTED | — |
| 31 | L90 | "...the filing says the result can still be '98% or greater utilization of the systolic array' **[0057]**." | q-0057-1 | [0057] verbatim | SUPPORTED | — |
| 32 | L92 cap. | "Attention queries, keys, and values, projection, and the MLP layers follow each other through the row, and at Time A a new computation has already entered while the previous one drains **[0056]**." | q-0056-1 | [0056] covers the Time-A / "previous computation" clause; the **stage-name list** ("Attention queries, keys, and values, projection") is [0055]'s content, not [0056]'s — [0055] has no Quotable span / quote-anchor row in the invention-summary at all | **OVERREACHED-BEYOND-ANCHOR** (sa3G-F1) | See Finding sa3G-F1 below. |
| 33 | L92 cap. | "The only idle gap is the layer-normalization stall, marked at Time B **[0057]**." | q-0057-1 | [0057]: layer normalization causes the only stall; "the stalled time may be small...98% or greater utilization" | SUPPORTED | — |
| 34 | L110 | "...claim 39's hardwired channels 'without any switching element' **[0016]**..." | q-0016-1 | [0016] / Claim 39 | SUPPORTED | — |
| 35 | L110 | "...inverts the crossbar practice the specification itself calls typical **[0043]**." | q-0043-1 | [0043] | SUPPORTED | — |
| 36 | Footnote (L140) | "...their one load-bearing point, more compute rows without more memory chips, travels in prose via **[0039]**." | q-0039-1 | [0039] | SUPPORTED | — |

---

## 3. Sub-table 1 — Claim statements vs. CLAIMS + Claim scope map

Checked every explicit claim-number reference and every scope-verb ("requires," "as drafted,"
"sought," "enforceable," "locked/fences/grants") for grant-era or enforceability leakage.

| # | Loc | Statement | Claims text / Scope map row | Verdict | Grant-era/enforceability verb? |
|---|---|---|---|---|---|
| C1 | L15 | "the interface the application claims, as drafted, in claim 39" | Claim 39 verbatim = [0016] | SUPPORTED | None — "as drafted" is application-era per edition note |
| C2 | L51 | "That is a description preference, not something claim 1 requires as drafted" (re: UCIe) | Scope map, Claim 1 row, "Leaves open": "Connection technology (UCIe is a description preference, [0030])" | SUPPORTED — exact match to scope map | "requires as drafted" is the scope map's own approved header language; not a locked-claim assertion |
| C3 | L73 | "Claims 7 and 8 put HBMs on that same switchless hardwiring, with claim 8 asking for several per top-row chip" | Claim 7: "HBMs are hardwired to respective columns...without any switching element"; Claim 8: "multiple HBMs are hardwired to each of the...ICs in the topmost row" | SUPPORTED | "asking for" — application-era, correct |
| C4 | L73 | "Claim 15 frames the system version..." | Claim 15 text | SUPPORTED | — |
| C5 | L81 | "Claims 11 to 13 add auxiliary circuitry (605)...backed by local memory chips (610) that hold the token history" | Claims 11-12 text | SUPPORTED | — |
| C6 | L81-84 | "claim 13, then draws a boundary the arrays cannot cross" + quote of [0051] | Claim 13: "local systolic arrays do not communicate with the local memory chips"; quoted text is [0051]'s paraphrase ("do not have access to"), correctly cited to [0051] not to "claim 13" verbatim | SUPPORTED — citation is to the spec paragraph, not falsely presented as claim text | None |
| C7 | L102 | "The broad combined-array claims, claim 1 and claim 26 as drafted, sit closest to that art and are exactly the kind of claims that shrink in it" | Scope map: Claim 1 "Broadest of the four...likeliest to narrow or die"; Claim 26 "Rises and falls with claim 1...likely shares claim 1's fate" | SUPPORTED | "as drafted" — correct |
| C8 | L102 | "Three years of prosecution have produced no enforceable claim at all" | Consistent with pending status; correctly states absence of enforceability | SUPPORTED | Correctly negates enforceability — no grant-era leakage |
| C9 | L110 | "the application's four independent claims, the ones that stand on their own rather than adding to another" | Scope map lists exactly 4 independents: 1, 15, 26, 39 | SUPPORTED | — |
| C10 | L110 | "claim 39's hardwired channels...is the best candidate to survive in some form" | Scope map Claim 39 row: "likeliest of the four to survive in some form" | SUPPORTED | "sought," not "granted"/"locked" |
| C11 | L110 | "broad claim 1...is the part of this filing likeliest to shrink or die" | Scope map Claim 1 row | SUPPORTED | — |

**No grant-era verb ("locks," "requires" in a binding sense, "fences," "enforceable" used
affirmatively) found anywhere in the claim-scope prose.** The two apparent regex hits on "lock"
(L40 "clock tick," L88 "block") are false positives (substring matches inside unrelated words).

---

## 4. Sub-table 2 — External (non-patent) facts vs. fact-check-log

| # | Loc | Fact | fact-check-log ID | Tier / evidence_level | Verdict |
|---|---|---|---|---|---|
| E1 | L19, L100 | Patent stack pledged as loan collateral | tp-lien-1-2024 / tp-lien-2-2025 | tier-2/registry-extract; tier-1/registry-verified | Logged |
| E2 | L21 | Thread claims: $1B+ contracts, $800m raised, summer 2026 ship, LVI+CSM pillars, all under "the company says" | etched-thread-2026-07 | tier-1 (as record of statement) / company-claimed | Logged, attribution present |
| E3 | L27 | "granted wiring patent, US 12,361,091 B1, the subject of an earlier analysis" (one continuity clause) | prior-essay-wiring-half | tier-2 / internal-prior-run | Logged, within one-clause budget |
| E4 | L49 | "roughly a whole laptop's storage" (100s of GB illustration) | [^derived-comparisons] | essay's own scale illustration, self-labeled | Logged |
| E5 | L71 | "roughly a full laptop drive's contents moving every second" (1 TB/s illustration) | [^derived-comparisons] | essay's own scale illustration, self-labeled | Logged |
| E6 | L98 | Prosecution-status label sentence (pending; final rejection; RCE; as of 2026-05) | prosecution-record | tier-2 / registry-extract | Logged — **this is the ONE budgeted label sentence** (see below) |
| E7 | L98 | "family is US-only, with no international filing and no continuation" | family-us-only | tier-2 / bibliographic | Logged |
| E8 | L100 | 1st lien: TriplePoint, 2024-04-19, reel/frame 067204/0877, four 2023-era applications incl. two rejected compiler filings | tp-lien-1-2024 | tier-2 / registry-extract | Logged, reel/frame matches exactly |
| E9 | L100 | 2nd lien: TriplePoint, 2025-07-18, reel/frame 071792/0869, portfolio incl. three granted patents | tp-lien-2-2025 | tier-1 / registry-verified | Logged, reel/frame matches exactly |
| E10 | L100 | "second and third of those grants had issued three days earlier, on 15 July 2025" + explicit inference label for any motive reading | grant-lien-timing | tier-1 / registry-verified (dates); inference (motive) | Logged, inference correctly labeled |
| E11 | L100 | "Both liens are blanket over the portfolio at signing, with no selectivity...say nothing about this application in particular" | Collateral-discipline note (fact-check-log "Notes") | — | Logged, matches the hard rule near-verbatim |
| E12 | L102 | "examination record lists 8 references, all examiner-cited, clustered in multi-node ML acceleration, hybrid parallelism, and neural-network accelerator architectures" | examiner-cited-field | tier-2 / registry-extract | Logged |

**Tally: 12/12 external facts matched to a fact-check-log entry with tier + evidence_level carried
correctly. Zero unlogged external facts found.**

**Prosecution-label occurrence count (budget: ONE):** the detailed prosecution chronology
(final rejection + RCE + "as of the 2026-05 record") appears exactly **once**, at L98. Later
references to "rejection"/"prosecution" (L102, L108, L110, L112) are thematic callbacks to that
single established fact — no new chronology, no new dates, no second office-action narrative
introduced. **Budget compliant (count = 1).**

---

## 5. Sub-table 3 — Figure captions vs. images + cited paragraphs

| # | Figure | Caption clause | Manifest / image | Cited paragraph(s) | Verdict |
|---|---|---|---|---|---|
| F1 | FIG. 1 | Full caption (rows 7-8 above) | Manifest: "DPU cells 105 fed by Model Weights 110 and Previous Tensor 115...propagate diagonally" | [0021] (+[0003]/[0020] for MAC, unattributed) | SUPPORTED |
| F2 | FIG. 2 | "ICs 215A to 215I...join through horizontal (230) and vertical (225)...into Combined Systolic Array 250. Memory chips (210A to 210C) sit only on the top row, and the host computer (205) connects over a standard PCIe link (240)." (unanchored) | Manifest: "package 201 combining ICs 215A-215I...into...250, wired to three external memory chips 210A-210C and a host 205 over PCIe connections 240" | [0025]-[0038] range (esp. [0028], [0034]-[0035]) | SUPPORTED |
| F3 | FIG. 5 | "Two memory chips (505A, 505B) sit above one IC (215)" (unanchored positional clause) + channel/wire/column clause (row 1 above, [0044]) | Manifest: "Two external memory chips 505A-505B hardwired via channels...into dedicated columns...of array tile 220 inside IC 215" | [0043]-[0045] | SUPPORTED |
| F4 | FIG. 6 | "Each IC (615A to 615D) holds an array tile (220) plus an auxiliary-circuitry block (605). The local memory chips (610A to 610D) are reachable only by that auxiliary circuitry." (unanchored) | **Manifest mislabels 605 as "local memory chips"** (known defect) — essay caption instead matches the specification: 605 = auxiliary circuitry, 610 = local memory chips, per invention-summary's explicit correction note | [0046]-[0047] (605 = aux circuitry), [0051] ("only the auxiliary circuitry 605 can access the local memory chips 610") | SUPPORTED — **essay correctly resolves the known manifest defect; verified against spec, not the mislabeled manifest line** |
| F5 | FIG. 7 | Stage-name clause (row 32, [0056]) | Manifest: "Timeline chart...Attention Queries/Keys/Values, Projection, MLP Hidden/Output Layer stages" | **[0055]** (stage names) mixed with [0056] (Time-A detail) under a single anchor | **OVERREACHED-BEYOND-ANCHOR** (sa3G-F1, same as row 32) |
| F6 | FIG. 7 | Time-B / layer-norm clause (row 33, [0057]) | Manifest: consistent | [0057] | SUPPORTED |

---

## 6. Findings

### sa3G-F1 (medium — anchor-citation scope, not a meaning distortion)

- **Sentence:** "*FIG. 7: pipelining one array row. Attention queries, keys, and values, projection, and the MLP layers follow each other through the row, and at Time A a new computation has already entered while the previous one drains [0056].*"
- **Invention-summary span leaned on:** q-0056-1 — "To achieve 100% efficiency...at Time A, the leftmost DPU in the row (e.g., DPU 0) is performing the computation associated with the output layer of the MLP, while the rightmost DPU in the row (e.g., DPU Y) is still working on the previous computation, the MLP hidden layer."
- **Patent paragraph tagged:** [0056]. **Patent paragraph the stage-name list actually comes from:** [0055] — "to calculate the query values (e.g., perform the 'Attention: queries' computation)...This is the same for performing the 'Attention: keys', 'Attention: values', and 'Projection' operations...the hidden and output layers for multi-layer perceptron (MLP)..."
- **Ruling:** OVERREACHED-BEYOND-ANCHOR. The clause is true to the patent and to the figure, but the single [0056] anchor does not cover the "Attention queries, keys, and values, projection" stage-name content — that content is [0055]'s. [0055] has no Quotable span or quote-anchor row anywhere in the invention-summary, so this caption clause is effectively citing a paragraph that doesn't contain it.
- **Recommended fix (anchor > narrow > cut):** Anchor, not narrow or cut — the content is accurate and load-bearing for the caption. Split the citation at the clause boundary: "...follow each other through the row [0055], and at Time A a new computation has already entered while the previous one drains [0056]." (Requires adding [0055] as a citable paragraph; it is not currently in the invention-summary's Quotable-spans or quote-anchor table, so Design would need to add it, or Compose could narrow the clause to omit the stage-name list and keep only the [0056]-covered "new computation entering before the previous drains" idea.)

No other non-SUPPORTED verdicts were found across the 36-row main table, the 11-row claim
sub-table, the 12-row external-fact sub-table, or the figure-caption sub-table.
