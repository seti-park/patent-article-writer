# Self-Audit Grounding Verification — Round 3 (FINAL dry-check)

**Draft**: `handoff/03-edit/essay-final.md` (draft_version: 5, r2 run, etched-0378175-memory-in-writing-r2)
**Blind inputs only**: invention-summary.md, patent.md, fact-check-log.md, essay-context.md, figures-manifest.md, thesis-spine.md (for errata alignment only), figure image files. No edit logs / revision notes / other self-audit reports consulted.
**Scope**: fidelity only. No tone/style/structure/hedge recommendations issued.

## 1. Mechanical layer

```
$ python gate_quotes.py handoff/03-edit/essay-final.md --invention-summary handoff/01-design/invention-summary.md --patent input/patent.md
[PASS] gate=quotes  (no findings)

$ python gate_anchors.py handoff/03-edit/essay-final.md --invention-summary handoff/01-design/invention-summary.md --figures handoff/01-design/figures-index.txt
[PASS] gate=anchors  (no findings)

$ python run_gates.py --draft ... --invention-summary ... --figures ... --figure-selection ... --patent ...
OVERALL: PASS — all 14 gates PASS, 0 fail, 0 warn
```

## 2. Thesis-spine errata alignment check

- Venue erratum (round 1, sa1B-F1: "pitched it on stage" → "pitched it in its stealth-exit thread"): essay uses "stealth-exit thread" / "the thread" consistently at L16, L18, L20, L22, L67, L107. No "stage"/"keynote" language found anywhere. **Aligned.**
- Founder-count erratum (round 2, sa2B-F2: "both co-founders" → "co-founders Uberti and Zhu"): essay uses "two of its co-founders" (L20), "co-founders Gavin Uberti and Christopher Zhu" (L22), "co-founders Uberti and Zhu" (L93), "The founders" (generic, L91/L103) — **no instance of "both co-founders" found anywhere in the essay.** Aligned.
- Note (observation, not an essay finding): thesis-spine.md's own one-line spine ("...two years before the company pitched it in its stealth-exit thread; three years of examination later...") is internally inconsistent — filing (2023-05-10) to thread (2026-06-30) is ~3.15 years, not 2. **The essay itself never repeats "two years"; it says "three years" consistently and correctly at L20, L24, L28, L67.** This is a slip in the design-phase summary sentence only; it does not propagate into the draft, so no essay-fidelity finding is raised. Flagging for awareness only.

## 3. Main anchor-by-anchor fidelity table (41 rows: every `[dddd]`-anchored sentence + all captions + all blockquotes, in essay order)

| # | Sentence (essay) | Anchor | Invention-summary span | Patent paragraph (verbatim) | Verdict |
|---|---|---|---|---|---|
| R01 | Title: "...in Writing in May 2023" | metadata | Filing date: 2023-05-10 | "Filed: May 10, 2023" | SUPPORTED |
| R02 | Alt-text: "FIG. 5: memory channels hardwired straight to the columns of the math array." | FIG.5 / [0043]-[0044] | q-0044-1 | [0044] "the independent channels 510 can be directly wired (or hardwired) to a particular column 515 in the local systolic array" | SUPPORTED |
| R03 | Caption S1: "independent memory channels (510) run through dedicated wires (520) straight into individual columns (515)...with no switch anywhere in the path." | [0043]-[0045] + FIG.5 image | q-0043-1/2, q-0044-1/2, q-0045-2 | [0043]-[0045] hardwiring description; image confirms no switch/crossbar box drawn | SUPPORTED |
| R04 | Caption S2: "Etched pitched this...in its stealth-exit thread in late June 2026." | external | fact `thread-claims-2026-07` | TechCrunch, 30 June 2026 | SUPPORTED |
| R05 | Caption S3: "The drawing is dated May 2023." | metadata | Filing date 2023-05-10 | "Filed: May 10, 2023" | SUPPORTED |
| R06 | "Three years before...two of its co-founders had signed that idea" | external (dates+founders) | thesis-spine axis 1; essay-context origin facts | filing 2023-05-10 vs thread 2026-06-30 ≈ 3.15 yr | SUPPORTED |
| R07 | "asks for memory channels wired straight into the columns...no switch in between [0016], [0044]" | [0016],[0044] | q-0016-1, q-0044-1 | [0016] full match (see R35); [0044] "can be directly wired (or hardwired) to a particular column 515..." | SUPPORTED |
| R08 | "public pitch arrived in late June 2026, presented as shipping hardware in the company's telling" | external | `thread-claims-2026-07` | TechCrunch: "first racks shipping in the summer" (company-claimed) | SUPPORTED — attribution present |
| R09 | "patent office still hasn't said yes to it" | external (status) | prosecution-status metadata | "PENDING APPLICATION...no enforceable claims exist" | SUPPORTED (soft callback, not the full label — see §5) |
| R10 | "names the architecture's authors, co-founders Gavin Uberti and Christopher Zhu, as its inventors" | metadata | Inventors field | "UBERTI; Gavin (Kirkland, WA), ZHU; Christopher (West Roxbury, MA)" | SUPPORTED |
| R11 | "It claims a package holding many small chips...one enormous array [0013], [0028]" | [0013],[0028] | q-0013-1, q-0028-1 | [0013] "a package that includes a plurality of...ICs...to form a larger, combined systolic array"; [0028] "appears to be one large array" | SUPPORTED |
| R12 | "\"most chips have, at most, floating point systolic arrays with a size of 128×128\" [0018], roughly sixteen thousand multipliers" | [0018] | q-0018-1 | [0018] "Currently, most chips have, at most, floating point systolic arrays with a size of 128×128." (exact) | SUPPORTED — 128×128=16,384≈"sixteen thousand" is essay arithmetic on an anchored figure only (no external number introduced); correct |
| R13 | "the filing calls it \"unreasonable to expect a single chip to interface with 100s of GB of memory\" [0018]" | [0018] | q-0018-2 | [0018] "it is unreasonable to expect a single chip to interface with 100s of GB of memory used to store parameters..." (exact) | SUPPORTED |
| R14 | "...built for jobs that \"perform the same task with different data at different times\" [0002]" | [0002] | q-0002-1 | [0002] "...algorithms that typically perform the same task with different data at different times." (exact) | SUPPORTED |
| R15 | "Model weights drop in from the top, and the filing notes they may be constants [0021]" | [0021] | (paraphrase, no anchor row needed) | [0021] "The topmost row of DPUs 105 receive AI model weights 110, which may be constants." | SUPPORTED |
| R16 | "The data being processed, the tensor, streams in from the left [0021]" | [0021] | — | [0021] "the DPUs in the leftmost column receive a tensor 115" | SUPPORTED |
| R17 | "one grid can carry two computations at once, for a single layer...or for different layers [0024]" | [0024] | q-0024-1 | [0024] "the systolic array 100 can perform two different computations in parallel...can perform different operations for a single layer...or perform operations for different layers...simultaneously" | SUPPORTED — "two" is directly stated in [0024]'s own earlier sentence, not an overreach |
| R18-cap | Caption: "FIG. 1: the basic systolic array, two computations sharing one grid." | FIG.1 image | q-0024-1 | matches image (hashed vs solid DPU boxes = two overlapping computations) | SUPPORTED (image-verified, §6) |
| R19 | "adapt a multi-chip approach...\"using high-speed chip-to-chip connections to form a larger, combined systolic array\" [0019]" | [0019] | q-0019-1 | [0019] exact substrings present | SUPPORTED |
| R20 | "Four chips of 100×100 in a row make one 100×400 array...same four stacked as a column make a 400×100 [0038]" | [0038] | q-0038-1 | [0038] "a single row of four ICs 215 would form a 100×400...a single column of four ICs 215 would form a 400×100" (exact) | SUPPORTED |
| R21-bq | Blockquote: "from the perspective of the host 205, the systolic array 250 appears to be one large array...distributed on separate ICs 215" — cited "[0028]" | [0028] | q-0028-1 | [0028] exact substring (drops leading "For example, ") | SUPPORTED — verbatim |
| R22 | "\"In one embodiment, the ICs 215 are all identical.\" [0028]" | [0028] | q-0028-2 | [0028] exact match | SUPPORTED — verbatim |
| R23-cap | Caption: "FIG. 2: nine ICs (215), each holding a local array (220), fused into one combined array (250); memory chips (210) line the top row; the host (205) attaches over PCIe (240)." | FIG.2 image | q-0028-1; ref-no table | Image: 9 ICs (215A-I), 210A-C top row, host 205 + PCIe 240 labeled | SUPPORTED (image-verified, §6) |
| R24 | "the different channels 510 cannot communicate with each other" [0043] | [0043] | q-0043-1 | [0043] "in HBM, the different channels 510 cannot communicate with each other." (exact) | SUPPORTED |
| R25-bq | Blockquote: "a switch (or some kind of switching element such as a crossbar) is typically used so that the device can access the entire memory of the HBM" — cited [0043] | [0043] | q-0043-2 | [0043] exact substring | SUPPORTED — verbatim |
| R26 | "the channels \"can be directly wired (or hardwired) to a particular column 515 in the local systolic array\" [0044]" | [0044] | q-0044-1 | [0044] exact substring (clean cut before "220 of the IC 215") | SUPPORTED |
| R27 | "it \"could extend through all the ICs 215 in a column\" [0044]" | [0044] | q-0044-2 | [0044] exact substring | SUPPORTED |
| R28 | "FIG. 5 draws it: two memory chips (505), four independent channels (510), dedicated wires (520), four columns (515)" | FIG.5 (context [0043]-[0045]) | ref-no table | Image: 505A/505B, 510A-D, 520 wires, 515A-D — exact count match | SUPPORTED (image-verified, §6) |
| R29 | "Hardwiring \"avoids having to add a switching element between the local systolic array\" and the memory chips, \"which can save space and power\" [0045]" | [0045] | q-0045-2 | [0045] "This avoids having to add a switching element between the local systolic array 220and the memory chips 505, which can save space and power." | SUPPORTED — the de-quoted connective "and the memory chips" correctly bridges the source's own "220and" OCR run-on per invention-summary's explicit handling instruction; meaning preserved exactly |
| R30 | "constants that always go to the same columns [0045], [0035]" | [0045],[0035] | q-0045-1, q-0035-2 | [0045] "constant weight data that is always provided to the same columns 515"; [0035] "the weights are constant when executing the combined systolic array 250" | SUPPORTED |
| R31 | Claim-39 "Translated" paraphrase citing [0016] | [0016] | q-0016-1; claim scope map row 39 | Claim 39 text (verified §4) | SUPPORTED — labeled "Translated," does not overreach into granted/locked language |
| R32-bq | Blockquote: full [0016] paragraph, cited "[0016]" | [0016] | q-0016-1 | [0016] full paragraph — **verbatim, word-for-word identical** | SUPPORTED — exact |
| R33 | "the description concedes \"may not be needed\" [0037]" | [0037] | q-0037-1 | [0037] "the memory chips 210 may not be needed." (exact) | SUPPORTED |
| R34 | "memory chips storing an AI model's weights, coupled to the chips that form the array's top row [0014]" | [0014] | q-0014-1 | [0014] full paragraph (paraphrased, no quote marks — accurate) | SUPPORTED |
| R35 | "\"data fed from the memory chips 305 is reused across the rows\" [0039]...adding rows...adds compute without adding a single memory chip [0039]" | [0039] | q-0039-1 | [0039] exact substring + "adding more rows of ICs 215 increases the compute power...without having to add more memory chips" | SUPPORTED |
| R36 | "\"transmit more than 1 TB/s of data to each of the ICs\" [0040]...about a feature film's worth of data every five thousandths of a second" | [0040] | q-0040-1 | [0040] exact substring (clean cut before "215in" run-on) | SUPPORTED — quote verbatim; film-per-5ms is the logged derived comparison (fact-check-log, origin sa1G-F2); scoping clause "by the description's own numbers" correctly isolates the 1 TB/s figure to the patent |
| R37 | "FIG. 3 draws the square-grid version with six memory chips across the top, and a sibling sheet, FIG. 4, redraws the same design with unequal rows and columns" | FIG.3/4 (context [0039]-[0041]) | figure-relationships table | Images: FIG.3 = 3×3 (9 ICs, 6 mem chips); FIG.4 = 2×3 (6 ICs, 6 mem chips, unequal) | SUPPORTED (image-verified, §6) |
| R38-cap | Caption: "FIG. 3: the square-grid variant; multiple memory chips (305) feed each top-row chip." | FIG.3 image | q-0039-1 | Image confirms 3×3 grid, 2 memory chips per top-row IC ("multiple" correctly non-specific vs. [0040]'s "three" example) | SUPPORTED (image-verified, §6) |
| R39 | "the combined array \"does not take instructions at runtime, and only executes instructions in a preset loop\" [0027]. That sentence lives in the description rather than in any claim" | [0027] | q-0027-1; map-wide note (description-only) | [0027] exact substring | SUPPORTED — description-only status correctly flagged |
| R40 | "Transformers, the model family the document uses as its running example [0003]" | [0003] | q-0003-1 | [0003] "e.g., transformer models"; corroborated by continued transformer framing at [0047],[0053],[0055] | SUPPORTED |
| R41 | "\"self-attention operations use data computed from previous tokens\" [0047]" | [0047] | q-0047-1 | [0047] exact substring | SUPPORTED |
| R42 | "Most of a transformer's work treats each token in isolation, which is exactly what the combined array is built for [0047]" | [0047] | q-0047-2 | [0047] "Most of the parts of a transformer AI model do not use data from previous tokens...may consider each token in isolation" | SUPPORTED |
| R43 | "gives the sidecar its own private memory: \"the auxiliary circuitry 605 in each IC 615 is coupled to at least one local memory chip 610\" [0048]" | [0048] | q-0048-1 | [0048] exact substring | SUPPORTED |
| R44 | "claims 11 through 13...down to a flat negative rule: \"the local systolic arrays 220 do not have access to the local memory chips 610\" [0051]" | [0051] | q-0051-1; claim map row 13 | [0051] exact substring; claims 11-13 verified against claim text (§4) | SUPPORTED — quote correctly anchored to description twin, not mislabeled as claim's own wording |
| R45-cap | Caption: "FIG. 6: inside each IC (615), the array tile (220) and the auxiliary circuitry (605) sit side by side; the private local memory chips (610) hang off the auxiliary circuitry, outside the combined array (650)." | FIG.6 image | corrected ref-no table + manifest-defect note | Image confirms: 605A inside IC-615A box beside 220A; 610A external small box, outside dashed "650" boundary | SUPPORTED — uses corrected labels, NOT the manifest's swapped 605/610 (image-verified, §6) |
| R46 | "FIG. 7 charts one row of the combined array pushing a transformer layer through in batches [0053], [0055], and none of what it shows is claimed anywhere" | [0053],[0055] | q-0053-1; map-wide description-only note | [0053] "contents of one row...one layer of the AI model"; [0055] "processed in multiple batches" | SUPPORTED — description-only correctly flagged |
| R47 | "the data \"passes through the systolic array three times\" [0055]" | [0055] | q-0055-1 | [0055] exact substring | SUPPORTED |
| R48 | "inputs for the next computation are fed in \"before the previous computation completes\" [0056]" | [0056] | q-0056-1 | [0056] exact substring | SUPPORTED |
| R49 | "the array can still hold \"a 98% or greater utilization\" [0057]" | [0057] | q-0057-2 | [0057] exact substring | SUPPORTED |
| R50-cap | Caption: "FIG. 7: a row's clock-by-clock schedule for one transformer layer. Description-only, no claim covers it: attention passes, pre-fed next batches, and the lone stall at layer normalization (Time B)." | FIG.7 image | map-wide description-only note | Image: X-axis clock cycles w/ Time A, Time B, X/2 marked; legend lists Attention Q/K/V, Projection, MLP layers; [0057] "shown at Time B where the array stalls" | SUPPORTED (image-verified, §6) |

**Row count, main table: 41.**

## 4. Sub-table — Claim statements (grant-era-verb flagging)

Every sentence in the essay that characterizes claim scope was checked for grant-era verbs ("locks," "requires" [asserted as fact rather than claim structure], "fences," "grants," "guarantees," "owns" in the present tense, "must") misapplied to SOUGHT (not locked) scope. Full-text scan found **zero misapplied instances** — every occurrence of a risk-flagged verb was either (a) about the OTHER, actually-granted patents (US 12,306,903/12,361,091/12,361,262), correctly distinguished, or (b) inside an explicit future-conditional ("if...will grant," "if claim 39...emerges intact...becomes property it owns").

| Claim ref | Essay sentence (essay wording) | Verb used | Grant-era? | Verdict |
|---|---|---|---|---|
| Claim 39 (indep.) | "Claim 39 is where the drawing becomes a legal ask. Translated:...\"without any switching element\" in between [0016]." | "Translated," no assertion of grant | No | SUPPORTED — matches map row 39 exactly (no multi-chip requirement, "without any switching element" is the fence) |
| Claim 39 vs Claim 1 | "Claim 39 is an independent claim...does not require the multi-chip package at all. The reverse is also true: the broadest package claim does not require memory chips" | "require" (structural, about claim recitation, not enforceability) | No — describes what the claim TEXT recites, not an enforceable right | SUPPORTED — verified against Claim 1 (no memory-chip element) and Claim 39 (single IC, no "plurality" of ICs) text directly |
| Claim 15 (indep.) | "A second independent claim seeks the weight-streaming arrangement itself" | "seeks" | Correct application-era verb | SUPPORTED |
| Claims 11-13 | "The application claims the split too. As drafted, claims 11 through 13 give each chip the sidecar..." | "As drafted" | Correct application-era framing | SUPPORTED |
| Claim 39 (bear case) | "Even claim 39's distinctive absence...could yet be judged routine for weight-stationary designs" | "could yet be judged" (subjunctive/future) | No | SUPPORTED — matches thesis-spine adversarial-defense framing verbatim in substance |
| Claim 1 (bear case) | "Claim 1, as drafted, reads on more or less any multi-chip systolic-array package" | "reads on," "as drafted," "more or less" | No | SUPPORTED — matches claim-1 text breadth and invention-summary's own characterization |
| General (verdict) | "until the patent office says yes, Etched holds a dated, signed statement of the memory idea it pitches, not an exclusive right to it" | explicit negation of "exclusive right" | N/A — correctly disclaims | SUPPORTED |
| General (closing) | "Racks shipping this summer...are not evidence that these claims will grant." / "If claim 39...emerge[s]...intact, the philosophy...becomes property it owns" | "will grant" / "becomes...owns" | Both inside future-conditional | SUPPORTED |
| Claim-1 / Claim-39 block quotes | No literal block-quoted claim text anywhere in the essay | N/A | — | N/A — the only verbatim block quote touching claim-39 content is the **[0016] description twin** (R32), correctly labeled "The description's twin sentence," never presented as claim 39's own text |

**Grant-era-verb flags: 0.**

## 5. Sub-table — External (non-patent) facts: evidence_level + attribution + specific checks requested

| Fact-check-log ID | Essay usage (location) | Tier / evidence_level | Attribution in essay | Verdict |
|---|---|---|---|---|
| `thread-claims-2026-07` | "$1B+ contracts", "$800m raised", "first racks shipping in the summer" (L22); CSM name + pitch line (L67); LVI name (L67) | tier-3 / company-claimed | "(TechCrunch)", "the company's own claim", "the company calls LVI", "the company says" — present at every use | SUPPORTED — logged, correctly attributed every time |
| `tpu-mxu-128x128` | "Google's...TPU...128×128 on generations through v5p, and moved to 256×256 with Trillium" (L28) | tier-1 / press-official-doc | "(Google Cloud TPU documentation)" | SUPPORTED |
| `lien-1-triplepoint-2024` | "The first, effective 19 April 2024 (USPTO reel/frame 067204/0877), covered the four applications...including two...later-rejected compiler applications" (L95) | tier-1 / registry-extract | Implicit (Sources section cites reel/frame) | SUPPORTED — **effective date used (19 Apr 2024), not the 24 Apr 2024 recordation date** — no mixing per fact-check-log's explicit rule |
| `lien-2-triplepoint-2025` | "The second, effective 18 July 2025 (reel/frame 071792/0869), covered the portfolio including the three patents that had by then granted: US 12,306,903, US 12,361,091 and US 12,361,262" (L95) | tier-1 / registry-verified | Sources section | SUPPORTED — **effective date used (18 Jul 2025), not the 22 Jul 2025 recordation date** |
| `grant-lien-timing` | "The second and third of those grants issued on 15 July 2025, and the second lien is effective three days later. The dates are facts. Any motive read into them is inference." (L97) | tier-1 / registry-verified | Explicit inference-labeling clause present | SUPPORTED — 15→18 July = 3 days, arithmetic correct; motive-labeling requirement satisfied verbatim |
| `prosecution-record` (THE required label) | "As of the May 2026 record, this application is still pending, with examination continuing after a final rejection mailed 23 October 2025 and a request for continued examination (an RCE) docketed 24 April 2026." (L87) | tier-1 / registry-extract | Implicit via framing ("As of the...record") | SUPPORTED — **label-budget check: this exact full-content sentence (pending + final-rejection date + RCE date) appears exactly ONCE**, at L87. Other pending/rejection references (L20, L93, L103, L105) are soft callbacks that restate no new dates/facts — no duplicate "battle narrative." Both-or-neither rule: collateral (L95/L97) and this label (L87) co-occur in the same section (§5, "Etched Keeps Paying to Own It") — satisfied. |
| `examiner-art-8refs` | "The examiner has assembled eight references...with Intel, IBM and Rambus among the assignees" (L89) | tier-1 / registry-extract | "among the assignees" (correctly non-exhaustive; omits ETRI without asserting completeness) | SUPPORTED |
| `family-us-only` | "This application is US-only, with no international counterpart under the PCT...no continuation either...while the granted trio got both treatments" (L99) | tier-1 / bibliographic | "One more registry note, offered as an observation" | SUPPORTED — matches fact-check-log's "allowed as a labeled observation" |
| `wiring-half-essay` | "The wiring half of that story...was read separately in a companion analysis of US 12,361,091 B1. That granted record never wrote the memory half down." (L43) | tier-4 / internal-prior-analysis | "a companion analysis" (Sources: "prior essay in this series") | SUPPORTED — one clause of continuity only, no dependence asserted |
| `lvi-absent-here` | "a power-delivery story the company calls LVI, appears nowhere in this filing. That absence carries one standing caveat: applications younger than 18 months can exist unpublished and unseen." (L67) | tier-1 / full-text-verified* | Explicit caveat sentence present | SUPPORTED. *Note: fact-check-log records this fact's evidence_level as "full-text-verified," which is not one of the six canonical values the log's own header defines (registry-verified/extract/bibliographic/company-claimed/third-party-read/internal-prior-analysis). This is a fact-check-log housekeeping inconsistency, not an essay defect — the essay's use of the fact is accurate either way. Flagged for awareness only, no essay finding. |
| `third-party-sohu-linkage` | Not used anywhere in the essay | tier-5 / third-party-read | N/A | N/A — correctly omitted (tier-5, color-only; conservative not to use it) |
| Derived: film-per-5ms | "about a feature film's worth of data every five thousandths of a second" (L63) | essay-own arithmetic, logged (origin: self-audit sa1G-F2) | "by the description's own numbers" scopes the 1 TB/s figure only | SUPPORTED — matches logged derivation exactly (1 TB/s × 5ms = 5GB ≈ HD feature film) |
| Derived (unlogged, but no external fact introduced): "roughly sixteen thousand multipliers" | L28 | 128×128 = 16,384, arithmetic on an anchored patent figure only | N/A (no external reference value introduced, unlike film-per-5ms) | SUPPORTED — does not require a fact-check-log entry since no external data point is combined with the patent figure; distinguishable from film-per-5ms |

**Temporal arithmetic — dedicated check:**
- Filing (2023-05-10) → thread (2026-06-30) ≈ 3.15 yr → essay says "Three years before" (L20), "Three years after" (L67): correct rounding, used consistently, never "two years." **PASS**
- Filing → "As of the May 2026 record" (L87) ≈ 3.0 yr → "Three years in" (L24): correct. **PASS**
- Grant date (15 July 2025) → 2nd lien effective (18 July 2025) = 3 days → essay: "effective three days later" (L97): correct. **PASS**
- Lien effective dates vs recordation dates: essay uses effective dates only (19 Apr 2024, 18 Jul 2025), never the recordation dates (24 Apr 2024, 22 Jul 2025) which would double-count/confuse the record. **PASS, no mixing.**

**Liens — dedicated check:** blanket/non-selective framing preserved ("Both liens are blanket, selecting nothing and saying nothing about any single filing's worth," L97); the two later-rejected compiler applications in lien-1's pool are disclosed (L95), which is the single strongest anti-overreach signal available and the essay includes it. **PASS.**

**Label budget ONE — dedicated check:** confirmed above under `prosecution-record`. **PASS — exactly one full label sentence.**

**Founder-count phrasing — dedicated check:** confirmed in §2 and R06/R10/R58-equivalent. **PASS — no "both co-founders" anywhere; "two of its co-founders," "co-founders Uberti and Zhu," and generic "the founders" are all count-safe.**

## 6. Sub-table — Figure captions vs. images (all 7 figures; images opened and read directly)

| Figure | Caption (essay) | Image content (as read) | Manifest cross-check | Verdict |
|---|---|---|---|---|
| FIG. 1 | "the basic systolic array, two computations sharing one grid" | Grid of DPUs (105), Model Weights (110) top, Previous Tensor (115) left; dashed boxes = "Multiplication #1," solid boxes = "Multiplication #2," overlapping diagonally | Matches manifest description | SUPPORTED |
| FIG. 2 | "nine ICs (215), each holding a local array (220), fused into one combined array (250); memory chips (210) line the top row; the host (205) attaches over PCIe (240)" | 3×3 grid of ICs 215A-I (each with 220A-I), 210A-C on top row, Host 205 + PCIe 240 labeled | Matches manifest ("ICs 215A-215I...three external memory chips 210A-210C...host 205 over PCIe") | SUPPORTED |
| FIG. 3 | "the square-grid variant; multiple memory chips (305) feed each top-row chip" | 3×3 grid (350), memory chips 305A-F, each top-row IC fed by a pair (with "•••" ellipsis suggesting more) | Matches manifest ("9 ICs...fed by six memory chips 305A-305F") | SUPPORTED |
| FIG. 4 | (no dedicated caption block; one clause in body text: "redraws the same design with unequal rows and columns") | 2×3 grid (450, unequal vs. FIG.3's 3×3), memory chips 305A-F on top | Matches manifest ("6 ICs...smaller multi-chip array than FIG. 3") | SUPPORTED |
| FIG. 5 | Alt-text + full caption: channels (510)/wires (520)/columns (515), no switch | 2 memory chips (505A/B), 4 channels (510A-D), wavy "wires 520," 4 columns (515A-D) inside IC 215, no switch/crossbar drawn | Matches manifest exactly | SUPPORTED |
| FIG. 6 | "array tile (220) and auxiliary circuitry (605) sit side by side; private local memory chips (610) hang off the auxiliary circuitry, outside the combined array (650)" | IC 615A contains 605A + 220A side by side; 610A is a small box fully external to 615A, outside the dashed "650" boundary | **Manifest has a known 605/610 swap** ("Local memory chips 605A-605D built into each IC block"); essay uses the **corrected** labeling (605=auxiliary circuitry, 610=local memory), matching the image and invention-summary's explicit correction note | SUPPORTED — correctly bypasses the manifest defect |
| FIG. 7 | "a row's clock-by-clock schedule...attention passes, pre-fed next batches, and the lone stall at layer normalization (Time B)" | X-axis clock cycles (0, Time B, X/2, Time A, X); Y-axis "Operation of DPU_i"; legend: Attention Queries/Keys/Values, Projection, MLP Hidden/Output | Matches manifest; Time B location matches [0057]'s layer-norm stall | SUPPORTED |

**All 7 figures: SUPPORTED, 0 caption/image mismatches.**

## 7. Findings

No fidelity defects found. **0 findings raised (sa3G-F0 — dry).**

Two non-finding observations (source-document housekeeping, not essay defects, no action against the essay warranted):
- **sa3G-OBS1**: thesis-spine.md's one-line spine contains an internal "two years"/"three years" arithmetic inconsistency (see §2). Does not appear in the essay.
- **sa3G-OBS2**: fact-check-log.md's `lvi-absent-here` row uses "full-text-verified" as its evidence_level value, which isn't one of the six canonical values the log's own header defines. Does not affect essay accuracy.
