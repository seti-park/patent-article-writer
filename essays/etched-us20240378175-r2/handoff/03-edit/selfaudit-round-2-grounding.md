# Self-Audit Grounding Verification — Round 2 (Dry-Check)

**Draft under review:** `handoff/03-edit/essay-final.md` (draft_version: 4, essay_id:
etched-0378175-memory-in-writing-r2, closing_posture: firm)
**Blind to:** edit-log*.md, revision-response*.md, revision-notes.md,
selfaudit-round-1-*.md, score-history.md (per task instruction; not read this round).
**Inputs used:** invention-summary.md, input/patent.md, fact-check-log.md,
essay-context.md, figures-manifest.md + the 7 source PNGs (input/figures/), thesis-spine.md
and title-lead-candidates.md (read only for their round-1 erratum notes, as directed).

---

## 1. Mechanical gate layer

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

Independent re-check (outside the gate script): every double-quoted span in the essay body
(31 spans) was extracted and matched against `input/patent.md` after NBSP (U+00A0)
normalization, mirroring `gate_quotes.py`'s own `_normalize()`. 25/31 matched verbatim as
patent-paragraph quotes. The 6 that did not match are, correctly, the ones that are **not**
patent text: `"the best layer is no layer"`, `"$1B+ contracts"`, `"$800m raised"`, `"each
memory layer adds latency; the best layer is no layer"` (all company/press quotes, tier-3),
`"Multi-Chip Systolic Arrays,"` (bibliographic title-case rendering of the patent's all-caps
heading, in the Sources line), and `"the wiring half"` (the essay's own coined label for the
companion analysis). No hidden NBSP-driven mismatch found.

Both figures shown in this report (FIG. 5, FIG. 6) and four more (FIG. 1, 2, 3, 7) were
opened and visually inspected directly against their captions, not just cross-checked
against the manifest text — see Table 4.

---

## 2. Main table — every `[dddd]`-anchored sentence + blockquote (34 rows)

Verdict key: SUPPORTED / MISREAD / OVERREACHED-BEYOND-ANCHOR / UNSUPPORTED.

| # | Sentence (essay) | Anchor(s) | Patent text (quoted) | Verdict | Note |
|---|---|---|---|---|---|
| R1 | "US 2024/0378175 A1, filed 10 May 2023, asks for memory channels wired straight into the columns of a giant multi-chip math array, no switch in between." | [0016],[0044] | [0016] "...a separate memory device comprising a plurality of channels where each...is hardwired to respective one or more columns in the systolic array without any switching element." [0044] "...the independent channels 510 can be directly wired (or hardwired) to a particular column 515... This systolic array column could extend through all the ICs 215 in a column." | SUPPORTED | "Multi-chip" is licensed by [0044]'s own "through all the ICs 215 in a column," not asserted from [0016] alone. Essay itself later correctly narrows: Claim 39 "does not require the multi-chip package at all." Lowest-confidence pick #1 (see §6). |
| R2 | "It claims a package holding many small chips, each carrying its own modest math array, joined to its neighbors so that the whole package computes as one enormous array." | [0013],[0028] | [0013] "a package that includes a plurality of...ICs, each comprising a local systolic array of...DPUs and chip-to-chip connections...to form a larger, combined systolic array." [0028] "from the perspective of the host 205, the systolic array 250 appears to be one large array..." | SUPPORTED | Plain-English paraphrase of claim-1-mirroring SUMMARY text; "claims" used as the sanctioned application-era verb. |
| R3 | ""most chips have, at most, floating point systolic arrays with a size of 128×128" [0018], roughly sixteen thousand multipliers." | [0018] | [0018] "Currently, most chips have, at most, floating point systolic arrays with a size of 128×128." | SUPPORTED | Quote verbatim substring. "Sixteen thousand" = 128×128 = 16,384, patent-internal arithmetic (no external reference point), self-evidently correct. |
| R4 | ""unreasonable to expect a single chip to interface with 100s of GB of memory" [0018], which is the scale a large model's parameters occupy." | [0018] | [0018] "...it is unreasonable to expect a single chip to interface with 100s of GB of memory used to store parameters and intermediate computation values." | SUPPORTED | Verbatim substring; gloss ("scale a large model's parameters occupy") restates "used to store parameters," outside the quotation marks. |
| R5 | "A systolic array...is a grid of small arithmetic units that pass data to their neighbors on every tick, built for jobs that "perform the same task with different data at different times" [0002]." | [0002] | [0002] "Systolic arrays are hardware structures built for fast and efficient operation of algorithms that typically perform the same task with different data at different times." | SUPPORTED | Quote verbatim. "Pass data to neighbors on every tick" paraphrases [0002]'s "network of DPUs which each accumulate...using data received from both upstream directions" plus general per-clock-cycle mechanics detailed elsewhere ([0003]/[0021]-[0023], unanchored here). Lowest-confidence pick candidate. |
| R6 | "Model weights drop in from the top, and the filing notes they may be constants, a detail that matters later [0021]." | [0021] | [0021] "The topmost row of DPUs 105 receive AI model weights 110, which may be constants." | SUPPORTED | Direct match. |
| R7 | "The tensor being processed streams in from the left [0021]." | [0021] | [0021] "...the DPUs in the leftmost column receive a tensor 115, which can be a previous tensor 115 calculated by the systolic array 100." | SUPPORTED | Direct match. |
| R8 | "FIG. 1 shows the shape, plus a property the description spells out: one grid can carry two computations at once, for a single layer of an AI model or for different layers [0024]." | [0024] | [0024] "...the systolic array 100 can perform different operations for a single layer in an AI model, or perform operations for different layers in the AI model, simultaneously." | SUPPORTED | Direct paraphrase. |
| R9 | ""adapt a multi-chip approach"..."using high-speed chip-to-chip connections to form a larger, combined systolic array" [0019]." | [0019] | [0019] "Instead, the embodiments herein adapt a multi-chip approach where multiple local systolic arrays on multiple chips (or ICs) are connected using high-speed chip-to-chip connections to form a larger, combined systolic array." | SUPPORTED | Both quoted fragments verbatim substrings. |
| R10 | "Four chips of 100×100 in a row make one 100×400 array, and the same four stacked as a column make a 400×100 [0038]." | [0038] | [0038] "...a single row of four ICs 215 would form a 100×400 combined systolic array 250 while a single column of four ICs 215 would form a 400×100 combined systolic array 250." | SUPPORTED | Numbers match exactly. |
| R11 | Blockquote: "from the perspective of the host 205, the systolic array 250 appears to be one large array, even though it is physically made up of smaller local systolic arrays 220 distributed on separate ICs 215" — US 2024/0378175 A1, [0028] | [0028] | [0028] same sentence, verbatim. | SUPPORTED | Verbatim block quote confirmed character-for-character. |
| R12 | "the chips are all interchangeable: "In one embodiment, the ICs 215 are all identical." [0028]" | [0028] | [0028] "In one embodiment, the ICs 215 are all identical." | SUPPORTED | Verbatim. |
| R13 | "the different channels 510 cannot communicate with each other" [0043]" | [0043] | [0043] "For example, in HBM, the different channels 510 cannot communicate with each other." | SUPPORTED | Verbatim substring. |
| R14 | Blockquote: "a switch (or some kind of switching element such as a crossbar) is typically used so that the device can access the entire memory of the HBM" — US 2024/0378175 A1, [0043] | [0043] | [0043] same sentence, verbatim. | SUPPORTED | Verbatim block quote confirmed. |
| R15 | ""can be directly wired (or hardwired) to a particular column 515 in the local systolic array" [0044]" | [0044] | [0044] "...the independent channels 510 can be directly wired (or hardwired) to a particular column 515 in the local systolic array 220 of the IC 215." | SUPPORTED | Verbatim substring. |
| R16 | "it "could extend through all the ICs 215 in a column" [0044], the top of the package to the bottom." | [0044] | [0044] "This systolic array column could extend through all the ICs 215 in a column." | SUPPORTED | Verbatim; gloss is a fair physical restatement. |
| R17 | "Hardwiring "avoids having to add a switching element between the local systolic array" and the memory chips, "which can save space and power" [0045]." | [0045] | [0045] "This avoids having to add a switching element between the local systolic array 220and the memory chips 505, which can save space and power." | SUPPORTED | Two clean substrings bridged exactly around the source's own "220and" run-on typo, per invention-summary's verbatim-discipline note — a correct, careful handling. |
| R18 | "a column can now read only its own channel. The filing accepts that because the weights parked in those channels are constants that always go to the same columns [0045], [0035]." | [0045],[0035] | [0045] "...this column may be unable to read data in the memory chip 505A assigned to the channel 510B... since the memory chips 505 may be used to store constant weight data that is always provided to the same columns 515..." [0035] "In one embodiment, the weights are constant when executing the combined systolic array 250." | SUPPORTED | Both anchors support the paraphrase. |
| R19 | "a package with a chip carrying a math array, plus a separate memory device, with every memory channel hardwired to its own column or columns, "without any switching element" in between [0016]." | [0016] | [0016]/Claim 39 verbatim: "...without any switching element." | SUPPORTED | Matches claim-39-mirroring SUMMARY paragraph and the claim itself. |
| R20 | Blockquote: full [0016] paragraph — US 2024/0378175 A1, [0016] | [0016] | [0016] verbatim, matches Claim 39 text exactly. | SUPPORTED | Verbatim block quote confirmed. |
| R21 | ""may not be needed" [0037]" (re: memory chips, broadest package claim) | [0037] | [0037] "Further, in some embodiments, the memory chips 210 may not be needed." | SUPPORTED | Verbatim; see also Table 2 (C4). |
| R22 | "memory chips storing an AI model's weights, coupled to the chips that form the array's top row [0014]." | [0014] | [0014] "...a plurality of memory chips configured to store weights for performing matrix multiplications...as part of an AI model, the plurality of memory chips coupled to the plurality of ICs forming a top row of the combined systolic array." | SUPPORTED | Direct match; see also Table 2 (C5). |
| R23 | ""data fed from the memory chips 305 is reused across the rows" [0039], so adding rows of chips adds compute without adding a single memory chip [0039]." | [0039] | [0039] "...adding more rows of ICs 215 increases the compute power of the systolic array 350, without having to add more memory chips 305...since data fed from the memory chips 305 is reused across the rows..." | SUPPORTED | Quote verbatim; "without adding a single memory chip" = idiomatic paraphrase of "without having to add more," not overreach. |
| R24 | ""transmit more than 1 TB/s of data to each of the ICs" [0040], by the description's own numbers, about a feature film's worth of data every five thousandths of a second." | [0040] | [0040] "...using multiple memory chips 305 can enable the memory chips 305 to transmit more than 1 TB/s of data to each of the ICs 215..." | SUPPORTED | Quote verbatim. Film comparison matches fact-check-log's `film-per-5ms` entry word for word, correctly scoped by "by the description's own numbers." |
| R25 | "The combined array "does not take instructions at runtime, and only executes instructions in a preset loop" [0027]." | [0027] | [0027] "...the systolic array 250 does not take instructions at runtime, and only executes instructions in a preset loop." | SUPPORTED | Verbatim. |
| R26 | "Transformers, the model family the document uses as its running example [0003]..." | [0003] | [0003] "For many...(AI) applications (e.g., transformer models), matrix multiplications dominate..." | SUPPORTED | [0003] introduces transformers as an example; the document's own later paragraphs ([0047],[0053]-[0057]) confirm transformers recur as the running example. |
| R27 | ""self-attention operations use data computed from previous tokens" [0047], so somewhere in the machine, history has to be stored." | [0047] | [0047] "...self-attention operations use data computed from previous tokens, which means such data should be saved." | SUPPORTED | Verbatim substring; gloss restates "should be saved." |
| R28 | "Most of a transformer's work treats each token in isolation, which is exactly what the combined array is built for [0047]." | [0047] | [0047] "Most of the parts of a transformer AI model do not use data from previous tokens, and thus, can be calculated efficiently using the combined systolic array 650 which may consider each token in isolation..." | SUPPORTED | Direct match. |
| R29 | ""the auxiliary circuitry 605 in each IC 615 is coupled to at least one local memory chip 610" [0048]." | [0048] | [0048] same sentence, verbatim (essay drops the trailing "(e.g., one or more HBMs)"). | SUPPORTED | Verbatim substring. |
| R30 | ""the local systolic arrays 220 do not have access to the local memory chips 610" [0051]." | [0051] | [0051] "In this embodiment, the local systolic arrays 220 do not have access to the local memory chips 610." | SUPPORTED | Verbatim; correctly bracketed to [0051] (description), not misattributed as claim-13's own wording — see Table 2 (C6). |
| R31 | "FIG. 7 charts one row of the combined array pushing a transformer layer through in batches [0053], [0055], and none of what it shows is claimed anywhere." | [0053],[0055] | [0053] "FIG. 7 illustrates the contents of one row of the combined systolic array while computing the output for one layer of the AI model." [0055] "...input tensors may be divided up and processed in multiple batches." | SUPPORTED | Matches; "none of what it shows is claimed anywhere" verified against Claims 1-42 (no claim recites batching/pipelining) — matches invention-summary's own description-only flag. |
| R32 | "computing the queries, means the data "passes through the systolic array three times" [0055]." | [0055] | [0055] "...to calculate the query values...the data passes through the systolic array three times." | SUPPORTED | Verbatim. |
| R33 | "inputs for the next computation are fed in "before the previous computation completes" [0056]." | [0056] | [0056] "...the inputs for the subsequent computation are fed into the systolic array before the previous computation completes." | SUPPORTED | Verbatim; essay omits the patent's own "100% efficiency" framing rather than repeating it — no overreach. |
| R34 | "the array can still hold "a 98% or greater utilization" [0057]." | [0057] | [0057] "...still result in a 98% or greater utilization of the systolic array." | SUPPORTED | Verbatim; "layer normalization" / "Time B" cross-checked in Table 4 (FC7). |

**Table 2 tally: 34/34 SUPPORTED. 0 MISREAD. 0 UNSUPPORTED. 0 OVERREACHED-BEYOND-ANCHOR.**

---

## 3. Sub-table 1 — claim statements vs CLAIMS text + Claim scope map (grant-era verb flagging)

Grant-era-verb sweep: the essay was scanned for "the patent locks/requires/fences/grants/
owns/covers/infringes" (the banned enforceability-implying pattern). Result: zero instances
of "the patent" used as the subject of an enforceability verb. All occurrences of "grant(ed)"
correctly refer only to the *other*, already-granted patent (US 12,361,091 B1) or the
granted trio (US 12,306,903 / 12,361,091 / 12,361,262), or appear in future/conditional tense
("if...will grant," "if claim 39...emerge...intact"). "Requires" and "claims" (as verbs) are
used only with a specific claim number as subject ("Claim 39...does not require," "the
broadest package claim does not require," "the application claims") — exactly the pattern
the Claim scope map itself sanctions ("required by the claim text as drafted"). "As drafted"
/ "sought" / "seeks" are used consistently. No grant-era-verb violation found.

| # | Statement | Claim(s) checked | Scope-map row | Verdict |
|---|---|---|---|---|
| C1 | "It claims a package holding many small chips...joined to its neighbors" | Claim 1 | Row "1 (indep.)" | SUPPORTED — matches Claim 1's recited elements exactly (plurality of ICs, local arrays, chip-to-chip connections forming a combined array); "claims" = sanctioned verb. |
| C2 | "Claim 39 is where the drawing becomes a legal ask...a package with a chip carrying a math array, plus a separate memory device...without any switching element" | Claim 39 | Row "39 (indep.)" | SUPPORTED — Claim 39 text confirmed verbatim: "an IC comprising a systolic array of...DPUs; and a separate memory device comprising a plurality of channels...hardwired to respective one or more columns...without any switching element." |
| C3 | "Claim 39 is an independent claim, one that stands alone instead of refining another, and it does not require the multi-chip package at all." | Claim 39 | Row "39 (indep.)": "it does NOT require multi-chip" | SUPPORTED — confirmed against claim text: 39 recites a single "an IC," no "plurality of ICs," no chip-to-chip connections. Matches scope map and thesis-spine Axis 1 verbatim. |
| C4 | "The reverse is also true: the broadest package claim does not require memory chips, which the description concedes "may not be needed" [0037]." | Claim 1 | Row "1 (indep.)": "Leaves open...memory presence ([0037]: memory chips may not be needed)" | SUPPORTED — Claim 1's text has no memory-chip element; memory chips first appear at dependent Claim 5. Matches scope map exactly. |
| C5 | "A second independent claim seeks the weight-streaming arrangement itself: memory chips storing an AI model's weights, coupled to the chips that form the array's top row [0014]." | Claim 15 | Row "15 (indep.)" | SUPPORTED — Claim 15 confirmed independent ("An AI accelerator, comprising:", no claim-dependency); text matches [0014]/essay paraphrase. "Seeks" = sanctioned verb. |
| C6 | "As drafted, claims 11 through 13 give each chip the sidecar, give the sidecar the attention work, and wall its memory off from the arrays, down to a flat negative rule: "...do not have access to..." [0051]." | Claims 11, 12, 13 | Rows "11," "12," "13" | SUPPORTED — Claim 11 (auxiliary circuitry + local memory chips coupled to it), Claim 12 (auxiliary circuitry performs self-attention using previous-token data), Claim 13 ("the local systolic arrays do not communicate with the local memory chips") map exactly onto the essay's three-part description. Note: the quoted phrase is [0051]'s wording ("do not have access to"), correctly bracketed to [0051] rather than presented as Claim 13's own text (which reads "do not communicate with") — precise sourcing, not a misattribution, since the two verbs describe the same negative limitation and the citation tag correctly names its actual source paragraph. Lowest-confidence pick candidate (see §6). |
| C7 | "Claim 1, as drafted, reads on more or less any multi-chip systolic-array package, and breadth like that is usually the first casualty of examination." | Claim 1 | Row "1 (indep.)": "the breadth is the part most likely to shrink" | SUPPORTED — near-verbatim restatement of the scope map's own Prosecution-risk-note language for Claim 1. "Reads on" is standard claim-scope terminology (describes breadth, not enforceability). |
| C8 | "Even claim 39's distinctive absence, the no-switch hardwiring, could yet be judged routine for weight-stationary designs...which is precisely the category this filing lives in." | Claim 39 | Row "39": "the negative...limitation is the distinctive fence" + thesis-spine Adversarial defense | SUPPORTED — mirrors thesis-spine's adversarial-defense language almost verbatim ("claim 39's no-switch hardwiring may yet be found routine for weight-stationary designs"). |
| C9 | "If claim 39 and its memory-side siblings emerge with the no-switch limitation materially intact, the philosophy Etched pitches becomes property it owns...If they narrow to ornament or die, the document stays what it is today..." | Claim 39 + family (7/19/32 implied by "siblings," not numbered) | thesis-spine "Residual risk" | SUPPORTED — conditional/future-tense framing matches the spine's falsifiability test exactly; no present-tense ownership or enforceability claim made. |

**Table 2 (sub-table 1) tally: 9/9 SUPPORTED.**

---

## 4. Sub-table 2 — external (non-patent) facts vs fact-check-log

| # | Fact as used in essay | fact-check-log ID | Tier / evidence_level | Attribution in essay | Verdict |
|---|---|---|---|---|---|
| E1 | ""$1B+ contracts", "$800m raised", first racks shipping in the summer, every figure the company's own claim" | thread-claims-2026-07 | tier-3 / company-claimed | "(TechCrunch)"; "every figure the company's own claim" | SUPPORTED |
| E2 | "Gavin Uberti and Christopher Zhu, the two founders, as its inventors" | (patent front-matter; not a fact-check-log tier item) | — | Sources: patent citation | SUPPORTED — matches invention-summary metadata and patent.md inventor listing exactly. |
| E3 | "the part Etched has since gotten granted, was read separately in a companion analysis of US 12,361,091 B1. That granted record never wrote the memory half down." | wiring-half-essay | tier-4 / internal-prior-analysis | "companion analysis" + Sources line | SUPPORTED |
| E4 | "Google's TPU ran its floating-point matrix units at 128×128 on generations through v5p, and moved to 256×256 with Trillium" | tpu-mxu-128x128 | tier-1 / press-official-doc | "(Google Cloud TPU documentation)" | SUPPORTED — see minor note below. |
| E5 | "named it CSM, Cluster Scale Memory in the press's expansion (TechCrunch)" + ""each memory layer adds latency; the best layer is no layer"" | thread-claims-2026-07 | tier-3 / company-claimed | "(TechCrunch)"; expansion correctly attributed to "the press," not the company | SUPPORTED — careful attribution matches fact-check-log's "CSM = 'Cluster Scale Memory' per press" framing precisely. |
| E6 | "a power-delivery story the company calls LVI, appears nowhere in this filing" | lvi-absent-here | tier-1 / full-text-verified | "in this filing" (correctly scoped) | SUPPORTED |
| E7 | "applications younger than 18 months can exist unpublished and unseen" | (essay-context Scope-boundaries brief; standard USPTO/PCT 18-month publication rule) | — | framed as "a standing caveat" | SUPPORTED |
| E8 | "As of the May 2026 record, this application is still pending, with examination continuing after a final rejection mailed 23 October 2025 and a request for continued examination (an RCE) docketed 24 April 2026." | prosecution-record | tier-1 / registry-extract | — | SUPPORTED. Dates match exactly (2025-10-23 / 2026-04-24). Prosecution-label-count check: this is the only fully-dated instance of the label sentence in the essay; other mentions ("still being argued with an examiner," "examination has been paid for through a rejection and beyond it") are narrative references that never restate the specific dates — **budget-ONE requirement satisfied.** |
| E9 | "an RCE is, in substance, a fee paid to keep arguing after the examiner has said no with finality" | (general USPTO procedural definition, not Etched-specific) | — | — | SUPPORTED |
| E10 | "The examiner has assembled eight references...multi-node machine-learning acceleration, hybrid parallelism and neural-network accelerator architectures, with Intel, IBM and Rambus among the assignees" | examiner-art-8refs | tier-1 / registry-extract | "among the assignees" (correctly non-exhaustive; log also lists ETRI, omitted here without overclaiming completeness) | SUPPORTED |
| E11 | "The first, effective 19 April 2024 (USPTO reel/frame 067204/0877), covered the four applications Etched had at the time...two compiler applications that were later rejected." | lien-1-triplepoint-2024 | tier-1 / registry-extract | inline reel/frame cite | SUPPORTED — effective date used (2024-04-19), not the recordation date (2024-04-24); no date-mixing. |
| E12 | "The second, effective 18 July 2025 (reel/frame 071792/0869), covered the portfolio including the three patents that had by then granted: US 12,306,903, US 12,361,091 and US 12,361,262." | lien-2-triplepoint-2025 | tier-1 / registry-verified | inline reel/frame cite | SUPPORTED — effective date used (2025-07-18), not recordation date (2025-07-22); patent numbers match exactly. |
| E13 | "Both liens are blanket, selecting nothing and saying nothing about any single filing's worth...bankable asset class...what a creditor reaches if the bet goes wrong." | fact-check-log "Collateral discipline" note | tier-1 | — | SUPPORTED — near-verbatim compliance with the hard discipline rule (never implies patent-specific selectivity). |
| E14 | "The second and third of those grants issued on 15 July 2025, and the second lien is effective three days later. The dates are facts. Any motive read into them is inference." | grant-lien-timing | tier-1 / registry-verified | labeled as inference | SUPPORTED — arithmetic verified exact: 2025-07-15 + 3 days = 2025-07-18. |
| E15 | "This application is US-only...It has no continuation either...while the granted trio got both treatments." | family-us-only | tier-1 / bibliographic | "offered as an observation" | SUPPORTED — hedge matches the lower (bibliographic) evidence tier; "the record does not say why" avoids speculation. |
| E16 | "about a feature film's worth of data every five thousandths of a second" | film-per-5ms (derived comparison) | logged, origin self-audit sa1G-F2 | "by the description's own numbers" scopes the underlying 1 TB/s figure | SUPPORTED — exact word-for-word match to the logged rendering. |
| E17 | "roughly sixteen thousand multipliers" (128×128) | not logged — pure patent-internal arithmetic (no external reference value involved, unlike E16) | — | — | SUPPORTED — 128×128 = 16,384 ≈ "roughly sixteen thousand"; correct, and does not need fact-check-log treatment since, unlike E16, it introduces no external comparison point. |
| E18 | Sources line: "TechCrunch, Etched stealth-exit coverage (30 June 2026)" vs. in-body "late June 2026" (cover caption; §1 ¶1) | thread-claims-2026-07 | tier-3 | — | SUPPORTED — 30 June is late June; no discrepancy between the Sources date and the in-body date register. Confirmed zero stray "July 2026" or "on stage" language remains anywhere in the draft (both were round-1 correction targets per thesis-spine/title-lead-candidates erratum notes) — grepped clean. |
| E19 | Temporal arithmetic: five "three years" statements (¶1 lead, §1 ¶1 close, §1 ¶3, §2 opening, §3 close) + "the second lien is effective three days later" (§5) | derived from filing date 2023-05-10 + thread date late June 2026 | — | — | SUPPORTED — 2023-05-10 to ~2026-06-30 ≈ 3 years + 51 days (≈3.14 years); "three years" is a consistent, conservative (rounds down, not up) approximation used identically in all five instances. "Three days later" (15 Jul 2025 → 18 Jul 2025) is exact, not an approximation. |

**Minor note on E4 (not a finding):** the Sources section lists two Google Cloud URLs under
"Technical specs" — "in-depth look at Google's first Tensor Processing Unit" and "TPU
documentation, introduction to TPU" — while the in-text attribution names only "(Google
Cloud TPU documentation)." The underlying fact is still fully supported by the fact-check-log
entry, which cites both URLs jointly; this is a bibliography-completeness question, not a
fidelity gap (the asserted fact is correctly sourced regardless of which listed URL a reader
consults), so no verdict is affected and no finding is raised.

**Table 3 (sub-table 2) tally: 19/19 SUPPORTED.**

---

## 5. Sub-table 3 — figure captions vs images + cited paragraphs

Figures FIG. 1, 2, 3, 5, 6, 7 were opened and visually inspected directly (not just checked
against the manifest text) given the task's flag on the known FIG. 6 605/610 manifest defect.

| # | Figure | Caption / description in essay | Verified against | Verdict |
|---|---|---|---|---|
| FC1 | FIG. 5 (cover) | Alt text: "memory channels hardwired straight to the columns of the math array." Caption: "independent memory channels (510) run through dedicated wires (520) straight into individual columns (515) of the on-chip math array, with no switch anywhere in the path...late June 2026...dated May 2023." | Image (viewed directly): 2 memory chips (505A/505B), 4 channels (510A-D), wires (520), 4 columns (515A-D) in array 220 inside IC 215, no switch element drawn. [0043]-[0045]. | SUPPORTED — element counts and structure match the image exactly; venue wording ("stealth-exit thread," no stage) and date ("late June 2026") both correct per erratum/Sources. |
| FC2 | FIG. 1 | "the basic systolic array, two computations sharing one grid." | Image (viewed directly): grid of DPU cells, "Model Weights" from top, "Previous Tensor" from left, two overlaid diagonal patterns labeled "Multiplication #1" / "Multiplication #2." [0024]. | SUPPORTED — exact visual match. |
| FC3 | FIG. 2 | "nine ICs (215), each holding a local array (220), fused into one combined array (250); memory chips (210) line the top row; the host (205) attaches over PCIe (240)." | Image (viewed directly): 3×3 grid, ICs 215A-215I / arrays 220A-220I, 3 memory chips 210A-210C on top row, Host 205 + PCIe 240 connections, bounded by label "250 Combined Systolic Array." [0025]-[0038]. | SUPPORTED — all five counted elements (9 ICs, top-row memory chips, host, PCIe, combined-array label) confirmed against the image. |
| FC4 | FIG. 3 | Caption: "the square-grid variant; multiple memory chips (305) feed each top-row chip." Body: "FIG. 3 draws the square-grid version with six memory chips across the top." | Image (viewed directly): 3×3 grid (220A-220I), 6 memory-chip rectangles (305A-305F) across the top in 3 pairs. [0039]-[0040]. | SUPPORTED — "six" is an exact visual count; caption's generic "multiple...feed each top-row chip" (rather than committing to [0040]'s illustrative "three per IC") is a careful hedge, since the drawing shows 2 per IC, not 3 — avoids a potential mismatch between the description's example number and the actual drawing. |
| FC5 | FIG. 4 | Prose-only, no dedicated image caption block: "a sibling sheet, FIG. 4, redraws the same design with unequal rows and columns." | figures-manifest ("6 ICs...smaller multi-chip array than FIG. 3") + [0041]-[0042] ("an unequal number of rows and columns...only have two rows of ICs rather than the three rows shown in FIG. 3"). | SUPPORTED — matches; no separate figure embed for FIG. 4 is a legitimate compose-phase choice, not a fidelity gap. |
| FC6 | FIG. 6 | "inside each IC (615), the array tile (220) and the auxiliary circuitry (605) sit side by side; the private local memory chips (610) hang off the auxiliary circuitry, outside the combined array (650)." | Image (viewed directly): confirms 605A-605D sit INSIDE each IC 615A-615D alongside 220A/220B/220D/220E; small boxes 610A-610D sit OUTSIDE the ICs, connected only to the 605 boxes, not to 220. [0047]-[0051]. | SUPPORTED — the known figures-manifest 605/610 swap defect (flagged in invention-summary's reference-number-table note) is correctly NOT reproduced in the essay; the caption uses the corrected labeling (605 = auxiliary circuitry, 610 = local memory chips), matching both the spec and the image pixel-for-pixel. This is the strongest-confidence row in the whole report precisely because it was checked against the actual artwork, not just text. |
| FC7 | FIG. 7 | "a row's clock-by-clock schedule for one transformer layer. Description-only, no claim covers it: attention passes, pre-fed next batches, and the lone stall at layer normalization (Time B)." | Image (viewed directly): X-axis labeled "0, Time B, X/2, Time A, X," Y-axis "Operation of DPU_i," legend listing Attention: Queries/Keys/Values, Projection, MLP Hidden/Output Layer. [0053]-[0057]. | SUPPORTED — "Time B" is the patent's own label for the stall point ([0057]: "shown at Time B where the array stalls"), correctly distinguished from "Time A" (used at [0056] for a non-stall point); essay does not conflate the two. |

**Table 4 (sub-table 3) tally: 7/7 SUPPORTED.**

---

## 6. Findings

**None.** Zero MISREAD, zero UNSUPPORTED, zero OVERREACHED-BEYOND-ANCHOR verdicts across
all 69 rows (34 main + 9 claim + 19 external-fact + 7 figure-caption). No `sa2G-F*` finding
IDs are issued this round — there is nothing to anchor/narrow/label/cut. This is consistent
with the round being labeled a dry-check following the round-1 (sa1B/sa1G) corrections,
which this essay version (draft_version 4) fully carries forward (venue-wording erratum,
date correction, film-per-5ms logging).

Three lowest-confidence SUPPORTED rows (still ruled SUPPORTED, but the ones requiring the
most interpretive judgment to clear):

1. **R1** — "...asks for memory channels wired straight into the columns of a giant
   multi-chip math array, no switch in between [0016], [0044]." The "multi-chip" framing in
   this lead sentence blends claim-39/[0016] language (which is silent on chip count) with
   [0044]'s "could extend through all the ICs 215 in a column." It clears only because [0044]
   itself supplies the multi-IC detail, and because the essay's own later section correctly
   narrows the claim-scope point ("Claim 39...does not require the multi-chip package at
   all").
2. **C6** — the [0051] quote ("...do not have access to the local memory chips 610")
   standing in to illustrate Claims 11-13's negative limitation, whose own text uses a
   different verb ("do not communicate with"). Correctly bracketed to its actual source
   paragraph rather than misattributed as claim text, but it asks the reader to accept that
   the two verbs describe the same restriction.
3. **R5** — "A systolic array...is a grid of small arithmetic units that pass data to their
   neighbors on every tick..." [0002]. The "every tick" / neighbor-passing mechanics are only
   partly in [0002] itself; the fuller mechanical detail lives in [0003]/[0021]-[0023], not
   anchored on this particular sentence.
