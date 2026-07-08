# Self-Audit Grounding Verification — Round 1 (BLIND)

**Subject:** `handoff/03-edit/essay-final.md` (`draft_version: 3`, the ACCEPTED r2 essay)
**Verifier:** grounding-verifier (fidelity only; no tone/structure/verdict-stance comments)
**Inputs used:** essay-final.md · invention-summary.md (44-row quote table + Claim scope map) ·
input/patent.md ([0001]-[0066] + claims 1-42) · fact-check-log.md · essay-context.md ·
figures-manifest.md (+ direct inspection of fig-01/02/03/04/05/06/07.png) — blind to edit logs,
revision notes, and any other self-audit report.

---

## 0. Mechanical gate layer

```
$ python .claude/skills/_shared/scripts/gate_quotes.py handoff/03-edit/essay-final.md \
    --invention-summary handoff/01-design/invention-summary.md --patent input/patent.md
[PASS] gate=quotes
  (no findings)
```

```
$ python .claude/skills/_shared/scripts/gate_anchors.py handoff/03-edit/essay-final.md \
    --invention-summary handoff/01-design/invention-summary.md \
    --figures handoff/01-design/figures-index.txt
[PASS] gate=anchors
  (no findings)
```

Both mechanical gates are clean: every quoted span is a verbatim (U+00A0-normalized) substring
of `patent.md`, and every `[NNNN]` anchor/figure token resolves. The gates cannot judge
*meaning* — that's the hand verification below, which found four findings the regex layer
cannot see (a date that contradicts the essay's own Sources line, two unlogged analogies/
connections, and one scope generalization beyond its anchor's own hedge).

---

## 1. Main fidelity table — every `[dddd]`-anchored sentence, in order of appearance

Quotes are trimmed to the operative fragment; full paragraph text is in `input/patent.md`.

| # | Sentence (essay, trimmed) | Anchor(s) | Patent span (trimmed) | Verdict |
|---|---|---|---|---|
| M1 | "asks for memory channels wired straight into the columns of a giant multi-chip math array, no switch in between" | [0016],[0044] | [0016] separate memory device, channels hardwired to columns "without any switching element"; [0044] "independent channels 510 can be directly wired (or hardwired) to a particular column 515" | SUPPORTED |
| M2 | "a package holding many small chips, each carrying its own modest math array, joined to its neighbors so that the whole package computes as one enormous array" | [0013],[0028] | [0013] package of ICs, each w/ local systolic array, chip-to-chip connections "to form a larger, combined systolic array"; [0028] host sees "one large array" | SUPPORTED |
| M3 | "'most chips have, at most, floating point systolic arrays with a size of 128×128,' roughly sixteen thousand multipliers" | [0018] | "most chips have, at most, floating point systolic arrays with a size of 128×128" (128×128=16,384; "roughly sixteen thousand" is a fair round) | SUPPORTED |
| M4 | "the filing calls it 'unreasonable to expect a single chip to interface with 100s of GB of memory'" | [0018] | "unreasonable to expect a single chip to interface with 100s of GB of memory" | SUPPORTED |
| M5 | "a grid of small arithmetic units that pass data to their neighbors on every tick, built for jobs that 'perform the same task with different data at different times'" | [0002] | "hardware structures built for fast and efficient operation of algorithms that typically perform the same task with different data at different times" | SUPPORTED |
| M6 | "Model weights drop in from the top, and the filing notes they may be constants" | [0021] | "The topmost row of DPUs 105 receive AI model weights 110, which may be constants." | SUPPORTED |
| M7 | "The tensor being processed streams in from the left" | [0021] | "the DPUs in the leftmost column receive a tensor 115" | SUPPORTED |
| M8 | "one grid can carry two computations at once... a property the later pitch leaned on" | [0024] | "the systolic array 100 can perform different operations for a single layer... or perform operations for different layers... simultaneously" | **OVERREACHED-BEYOND-ANCHOR** — see sa1G-F3 |
| M9 | "'adapt a multi-chip approach' and connect the small arrays 'using high-speed chip-to-chip connections to form a larger, combined systolic array'" | [0019] | exact phrases present | SUPPORTED |
| M10 | "Four chips of 100×100 in a row make one 100×400 array... 400×100" | [0038] | "a single row of four ICs 215 would form a 100×400 combined systolic array 250 while a single column of four ICs 215 would form a 400×100" | SUPPORTED |
| M11 (blockquote) | "from the perspective of the host 205, the systolic array 250 appears to be one large array... distributed on separate ICs 215" | [0028] | verbatim (confirmed substring, script-checked) | SUPPORTED |
| M12 | "'In one embodiment, the ICs 215 are all identical.'" | [0028] | verbatim | SUPPORTED |
| M13 | "'the different channels 510 cannot communicate with each other'" | [0043] | verbatim | SUPPORTED |
| M14 (blockquote) | "a switch (or some kind of switching element such as a crossbar) is typically used so that the device can access the entire memory of the HBM" | [0043] | verbatim (confirmed substring, script-checked) | SUPPORTED |
| M15 | "channels 'can be directly wired (or hardwired) to a particular column 515 in the local systolic array'" | [0044] | verbatim | SUPPORTED |
| M16 | "it 'could extend through all the ICs 215 in a column'" | [0044] | verbatim | SUPPORTED |
| M17 | "Hardwiring 'avoids having to add a switching element between the local systolic array' and the memory chips, 'which can save space and power'" | [0045] | verbatim, split around the source's own "220and" run-on typo (correctly NOT reproduced as a run-on) | SUPPORTED |
| M18 | "the weights parked in those channels are constants that always go to the same columns" | [0045],[0035] | [0045] "constant weight data that is always provided to the same columns"; [0035] "weights are constant when executing the combined systolic array" | SUPPORTED |
| M19 | "a package with a chip carrying a math array, plus a separate memory device... 'without any switching element' in between" (Claim 39 paraphrase) | [0016] | claim-39 text tracks [0016] almost word for word; "without any switching element" verbatim in both | SUPPORTED |
| M20 (blockquote) | full [0016] paragraph | [0016] | verbatim (confirmed substring, script-checked) | SUPPORTED |
| M21 | "the broadest package claim does not require memory chips, which the description concedes 'may not be needed'" | [0037] | "in some embodiments, the memory chips 210 may not be needed" | SUPPORTED |
| M22 | "A second independent claim seeks the weight-streaming arrangement itself: memory chips storing an AI model's weights, coupled to the chips that form the array's top row" | [0014] | [0014] embodiment text matches claim 15 near-verbatim; claim 15 is the 2nd-numbered of the four independents (1, 15, 26, 39) | SUPPORTED |
| M23 | "'data fed from the memory chips 305 is reused across the rows'... adding rows of chips adds compute without adding a single memory chip" | [0039] | verbatim quote + "adding more rows of ICs 215 increases the compute power... without having to add more memory chips" | SUPPORTED |
| M24 | "can 'transmit more than 1 TB/s of data to each of the ICs'... about a feature film's worth of data every five thousandths of a second" | [0040] | verbatim quote for the bandwidth figure; the film-size analogy is NOT patent content | **OVERREACHED-BEYOND-ANCHOR** — see sa1G-F2 |
| M25 | "does not take instructions at runtime, and only executes instructions in a preset loop" | [0027] | verbatim | SUPPORTED |
| M26 | "Transformers, the model family the document aims at" | [0003] | [0003] frames transformers as one example ("e.g., transformer models") of "many AI applications," and [0019] extends scope to crypto/DNA/signal processing | **OVERREACHED-BEYOND-ANCHOR** — see sa1G-F4 |
| M27 | "'self-attention operations use data computed from previous tokens'" | [0047] | verbatim | SUPPORTED |
| M28 | "Most of a transformer's work treats each token in isolation, which is exactly what the combined array is built for" | [0047] | "Most of the parts of a transformer AI model do not use data from previous tokens... calculated efficiently using the combined systolic array 650 which may consider each token in isolation" | SUPPORTED |
| M29 | "'the auxiliary circuitry 605 in each IC 615 is coupled to at least one local memory chip 610 (e.g., one or more HBMs)'" | [0048] | verbatim | SUPPORTED |
| M30 | "'the local systolic arrays 220 do not have access to the local memory chips 610'" | [0051] | verbatim; correctly claim-scoped to claims 11-13, not asserted as universal (the [0051] "may also have access" alternative embodiment is not contradicted) | SUPPORTED |
| M31 | "FIG. 7 charts one row of the combined array pushing a transformer layer through in batches... none of what it shows is claimed anywhere" | [0053] | "FIG. 7 illustrates the contents of one row of the combined systolic array while computing the output for one layer"; matches invention-summary's explicit note that FIG. 7/batching/utilization are description-only, no claim | SUPPORTED |
| M32 | "'passes through the systolic array three times'" | [0055] | verbatim | SUPPORTED |
| M33 | "'before the previous computation completes'" | [0056] | verbatim | SUPPORTED |
| M34 | "the array holds 'a 98% or greater utilization'" | [0057] | verbatim | SUPPORTED |

**Main-table tally: 34 rows — 31 SUPPORTED, 3 OVERREACHED-BEYOND-ANCHOR (M8, M24, M26), 0 UNSUPPORTED, 0 MISREAD.**

No MISREAD found anywhere in the main table: direction (top-to-bottom weights, left-to-right
tensors, column-restricted channel reads, auxiliary-circuitry-only memory access) is preserved
correctly in every case checked against the patent text and the FIG. 1/2/5/6 images.

---

## 2. Sub-table 1 — Claim statements vs CLAIMS + Claim scope map

| # | Essay claim statement | Patent claim text / scope-map row | Verdict |
|---|---|---|---|
| CL1 | "Claim 39 is an independent claim, one that stands alone instead of refining another, and it does not require the multi-chip package at all." | Claim 39: "A package, comprising: an IC comprising a systolic array..." — singular "an IC," no plurality-of-ICs element; claims 40-42 (dependents) never reintroduce plurality of ICs. Scope map lists 39 as one of 4 independents (1, 15, 26, 39). | SUPPORTED |
| CL2 | "the broadest package claim does not require memory chips" (claim 1) | Claim 1 text has no memory-chip element (memory chips first appear at dependent claim 5). Scope map row 1: "Broadest independent." | SUPPORTED |
| CL3 | "A second independent claim seeks the weight-streaming arrangement itself... coupled to the chips that form the array's top row" (claim 15, via [0014]) | Claim 15 text matches scope-map row 15 exactly; claim 15 is the 2nd of the four independents by number | SUPPORTED |
| CL4 | "claims 11 through 13 give each chip the sidecar, give the sidecar the attention work, and wall its memory off from the arrays" | Claim 11 (auxiliary circuitry + local memory chips), claim 12 (self-attention using previous-token data), claim 13 ("local systolic arrays do not communicate with the local memory chips") — matches scope-map rows 11-13 exactly | SUPPORTED |
| CL5 | "Claim 1, as drafted, reads on more or less any multi-chip systolic-array package, and breadth like that is usually the first casualty of examination." | Scope map row 1 prosecution-risk note: "the multi-chip-array concept sits in a crowded examiner-cited field... the breadth is the part most likely to shrink" | SUPPORTED |
| CL6 | "**It is claim language, dated May 2023.**" / "the memory half can be judged, and owned, on its own" | Filing date 2023-05-10 confirmed; claim 39 language appears in the Nov-2024 publication we hold. Current (2026, post-RCE) claim 39 text is not independently re-confirmed identical to the as-published version — reasonable given standard publication practice, but not directly evidenced beyond this document. "Owned" is used in the future/conditional sense (paired with "judged," and the essay elsewhere explicitly says "not an exclusive right to it" at line 103) | SUPPORTED (lower confidence — see three lowest-confidence rows below) |
| CL7 | Global scan: grant-era/enforceability verbs ("locks," "fences," "infringe," "protects," "enforceable," unqualified "grant/granted" for THIS application) | Searched full essay text (`lock\|fence\|infring\|exclusiv\|protect\|enforc\|grant`, case-insensitive). Every "grant/granted" hit refers to the OTHER, already-granted patents (US 12,361,091 B1 / the trio) or is future-conditional ("these claims will grant"). The one "exclusive" hit is negated ("not an exclusive right to it"). No "lock," "fence," "infring," "protect," or "enforc-" instance found anywhere. Application-era verbs ("asks for," "seeks," "is where the drawing becomes a legal ask") are used consistently for claim content. | **SUPPORTED — no violations found** |

**Claims sub-table tally: 7 rows, all SUPPORTED (0 violations of grant-era/enforceability discipline).**

---

## 3. Sub-table 2 — External (non-patent) facts vs fact-check-log

| # | Essay fact | fact-check-log entry | Tier / evidence_level | Verdict |
|---|---|---|---|---|
| EF1 | "As of the May 2026 record, this application is still pending, with examination continuing after a final rejection mailed 23 October 2025 and a request for continued examination (an RCE) docketed 24 April 2026." | `prosecution-record` | tier-1 / registry-extract | SUPPORTED — **and this is the ONLY full-detail (dated) prosecution-status sentence in the essay** — budget of ONE is met. Two further narrative allusions exist ("a rejection," "a final rejection," lines 93) but neither restates dates nor becomes a battle narrative. |
| EF2 | "The examiner has assembled eight references... multi-node machine-learning acceleration, hybrid parallelism and neural-network accelerator architectures, with Intel, IBM and Rambus among the assignees" | `examiner-art-8refs` | tier-1 / registry-extract | SUPPORTED (drops ETRI; "among the assignees" is correctly non-exhaustive) |
| EF3 | Claim-1-breadth / crowded-field framing (line 89) | `examiner-art-8refs` | tier-1 / registry-extract | SUPPORTED — see CL5 (not double-counted) |
| EF4 | "could yet be judged routine for weight-stationary designs" | not a distinct fact-check-log fact; synthesis of already-anchored [0035]/[0044]/[0045]/[0021] + invention-summary's own "weight-stationary" framing (design-phase term) | n/a (analytical synthesis, not new empirical claim) | SUPPORTED |
| EF5 | "The authorship is dated and signed: 10 May 2023, both founders." | patent metadata (filing date, inventors) | tier-1 / full-text-verified | SUPPORTED |
| EF6 | Lien 1: effective 19 April 2024, reel/frame 067204/0877, four applications incl. two later-rejected compiler applications | `lien-1-triplepoint-2024` | tier-1 / registry-extract | SUPPORTED — uses effective date (not recordation date 2024-04-24), per fact-check-log's "do not mix" rule |
| EF7 | Lien 2: effective 18 July 2025, reel/frame 071792/0869, covers granted trio | `lien-2-triplepoint-2025` | tier-1 / registry-verified | SUPPORTED — uses effective date (not recordation date 2025-07-22) |
| EF8 | "Both liens are blanket, selecting nothing... Etched's patent stack is the company's bankable asset class... what a creditor reaches if the bet goes wrong" | fact-check-log Notes: "Collateral discipline" | n/a (log's own framing note) | SUPPORTED — near-verbatim match to the mandated disclosure |
| EF9 | "The second and third of those grants issued on 15 July 2025, and the second lien is effective three days later." | `grant-lien-timing` | tier-1 / registry-verified | SUPPORTED — arithmetic verified: 2025-07-15 → 2025-07-18 = 3 days; "any motive read into them is inference" carried over correctly |
| EF10 | "This application is US-only... no PCT... no continuation... while the granted trio got both treatments" | `family-us-only` | tier-1 / **bibliographic** (not independently re-fetched this run) | SUPPORTED — but the weakest-tier fact actually used (see three lowest-confidence rows) |
| EF11 | "'$1B+ contracts', '$800m raised', first racks shipping in the summer, every figure the company's own claim" | `thread-claims-2026-07` | tier-3 / company-claimed | SUPPORTED — correctly attributed as the company's own claim, not TechCrunch's |
| EF12 | "Google's TPU ran its floating-point matrix units at 128×128 on generations through v5p, and moved to 256×256 with Trillium" | `tpu-mxu-128x128` | tier-1 / press-official-doc | SUPPORTED |
| EF13 | "The wiring half of that story, the part Etched has since gotten granted, was read separately in a companion analysis of US 12,361,091 B1. That granted record never wrote the memory half down." | `wiring-half-essay` | tier-4 / internal-prior-analysis | SUPPORTED |
| EF14 | "Etched pitched this on stage as its no-layer memory philosophy in July 2026" (caption) / "The stage version arrived in July 2026" (body, line 20) | `thread-claims-2026-07` cites TechCrunch, and the essay's own Sources line reads "TechCrunch, Etched stealth-exit coverage (**30 June 2026**)" | tier-3 / company-claimed, but the **month is internally inconsistent with the essay's own cited source** | **UNSUPPORTED** — see sa1G-F1 |
| EF15 | Feature-film-per-5ms analogy (line 63) | not in fact-check-log; assumes an uncited feature-film file size | n/a | flagged — see M24 / sa1G-F2 (not double-counted) |
| EF16 | "a property the later pitch leaned on" (line 30, re: [0024]'s dual-computation capability) | not in fact-check-log's `thread-claims-2026-07` entry (which lists only LVI/CSM/$-figures/the "best layer" pitch line — no "splittable"/dual-computation claim); traces only to essay-context.md's framing prose ("The thread's 'splittable math arrays' is this document's subject") | n/a | flagged — see M8 / sa1G-F3 (not double-counted) |
| EF17 | "Three years before..." / "Three years in..." / "Three years after these paragraphs were filed..." (temporal arithmetic) | Filing 2023-05-10; thread/pitch coverage ~mid-2026 | derived | SUPPORTED — May 2023 to the TechCrunch date (30 June 2026) is 3 years + ~51 days; "three years" is a fair round in either direction. (The MONTH label is the problem — see EF14 — not the three-year arithmetic itself.) |
| EF18 | "applications younger than 18 months can exist unpublished and unseen" | general US patent-publication rule (35 U.S.C. 122(b), 18-month publication), echoed as a standing caveat in essay-context.md | n/a (uncontested procedural fact) | SUPPORTED |

**External-fact tally: 18 external facts examined — 15 SUPPORTED (14 directly + EF3 via CL5), 2 flagged as unlogged (EF15, EF16 — counted once each under M24/M8 in the grand tally), 1 UNSUPPORTED (EF14, date contradicts the essay's own Sources line).**

---

## 4. Sub-table 3 — Figure captions vs images + cited paragraphs

Each figure file was opened directly (`input/figures/fig-0N.png`) and checked against its caption
and the paragraphs it illustrates.

| # | Caption (essay) | Image check | Cited paragraphs | Verdict |
|---|---|---|---|---|
| FC1 | Header caption: "FIG. 5, from Etched's first patent filing: independent memory channels (510) run through dedicated wires (520) straight into individual columns (515)... **Etched pitched this on stage as its no-layer memory philosophy in July 2026.** The drawing is dated May 2023." | Image confirms 2 memory chips (505A/B), 4 channels (510A-D), wires (520), 4 columns (515) — the figure-content half is correct | n/a for the date clause (external fact, not a patent paragraph) | **UNSUPPORTED** on the "July 2026" clause — same issue as EF14; the figure-content clause is SUPPORTED |
| FC2 | "FIG. 1: the basic systolic array, two computations sharing one grid." | Image confirms: Systolic Array 100, DPUs 105, Model Weights 110 (top), Previous Tensor 115 (left), two overlapping hashed/solid computation patterns | [implicit: 0020-0024] | SUPPORTED |
| FC3 | "FIG. 2: nine ICs (215), each holding a local array (220), fused into one combined array (250); memory chips (210) line the top row; the host (205) attaches over PCIe (240)." | Image confirms exactly 9 ICs (215A-I) in a 3×3 grid, each with tile 220, labeled Combined Systolic Array 250, 3 memory chips (210A-C) atop the 3 top-row ICs, Host 205 + PCIe 240 | [0025]-[0028], [0034]-[0035] | SUPPORTED |
| FC4 | "FIG. 3: the square-grid variant; multiple memory chips (305) feed each top-row chip." | Image confirms 3×3 grid of ICs (350), six memory chips 305A-F, two chips per top-row IC | [0039]-[0040] | SUPPORTED |
| FC5 | "FIG. 6: inside each IC (615), the array tile (220) and the auxiliary circuitry (605) sit side by side; the private local memory chips (610) hang off the auxiliary circuitry, outside the combined array (650)." | Image confirms 605A-D (paired beside 220A/B/D/E inside each 615 block) connect outward via arrows to smaller external boxes 610A-D, which sit outside the dashed "650" boundary. **This correctly avoids the KNOWN DEFECT**: figures-manifest.md's line for FIG. 6 swaps the labels ("local memory chips 605A-605D built into each IC block"); the essay uses the corrected assignment (605 = auxiliary circuitry, 610 = local memory chips) per [0047]-[0051] and the image itself | [0046]-[0051] | SUPPORTED |
| FC6 | "FIG. 7: a row's clock-by-clock schedule for one transformer layer. Description-only, no claim covers it: attention passes, pre-fed next batches, and the lone stall at layer normalization (Time B)." | Image confirms axes (Operation of DPU_i vs. clock cycles 0→X), legend (Attention Queries/Keys/Values, Projection, MLP Hidden/Output), and markers "Time B" / "X/2" / "Time A." [0057] explicitly ties "Time B" to the layer-norm stall | [0053]-[0057] | SUPPORTED |

**Figure-caption tally: 6 rows — 5 SUPPORTED, 1 partially UNSUPPORTED (FC1's date clause only; its figure-content clause is accurate).**

The FIG. 6 605/610 defect specifically flagged in the task brief was checked against the actual
image and **is correctly avoided** in both the caption (FC5) and the body text ("a sidecar
processor sitting beside the tile, and gives the sidecar its own private memory," line 75).

---

## 5. Findings (fixes only: anchor a better span -> narrow the claim -> cut)

**sa1G-F1 (MEDIUM).** The essay states twice — in the header caption (FIG. 5, "in July 2026")
and in the lead ("The stage version arrived in July 2026") — that Etched's stage
pitch/stealth-exit event happened in July 2026. But the essay's own Sources section dates its
sole source for that event as "TechCrunch, Etched stealth-exit coverage (**30 June 2026**)"
(and the underlying URL is `.../2026/06/30/...`). No source in fact-check-log documents a
distinct July event. **Fix priority:** narrow both instances to match the cited source (e.g.,
"in late June 2026" or drop the month and say "in 2026" / "this summer"), or — if a genuinely
separate July stage appearance exists — add a citation for it. Does not affect the "three
years" arithmetic itself (fair either way), only the specific month label.

**sa1G-F2 (LOW).** "About a feature film's worth of data every five thousandths of a second"
(line 63) is not in fact-check-log; it silently assumes an uncited real-world feature-film file
size to translate the patent's own ">1 TB/s" [0040] figure into a lay analogy. **Fix priority:**
no better patent span exists for this specific number (it's an illustrative addition, not a
patent fact) — cut the specific analogy and keep the patent-sourced ">1 TB/s" figure alone, or
replace with a sourced comparison.

**sa1G-F3 (LOW).** "One grid can carry two computations at once... a property the later pitch
leaned on" (line 30, anchored to [0024]) asserts a specific connection to what Etched's pitch
emphasized. [0024] itself is solidly supported, but fact-check-log's `thread-claims-2026-07`
entry lists only LVI, CSM, the dollar figures, and the "best layer is no layer" pitch line — no
"splittable"/dual-computation claim is logged as company-claimed. The connection traces only to
essay-context.md's framing prose, not a quotable source. **Fix priority:** narrow to a
description-only framing ("a property this description anticipates") or add the source that
shows the pitch discussed this specifically.

**sa1G-F4 (LOW).** "Transformers, the model family the document aims at [0003]" overstates
[0003]'s own hedge — the patent says "e.g., transformer models" as one example of "many AI
applications," and [0019] explicitly extends the invention's applicability to cryptography,
DNA/protein sequencing, and signal processing. **Fix priority:** narrow to "a model family the
document uses as its running example" (defensible given how much of [0047]-[0057] is
transformer-specific) rather than asserting singular aim.

No MISREAD and no other UNSUPPORTED items were found. No finding recommends adding a hedge,
caveat, or disclaimer (out of jurisdiction) — every recommendation above is anchor/narrow/cut.

---

## 6. Three lowest-confidence SUPPORTED rows

1. **CL6** — "**It is claim language, dated May 2023.**" The claim-39 text we can verify is the
   one published in this Nov-2024 document; the application has since been through two more
   office actions, a final rejection, and an RCE, and none of those post-publication amendments
   (if any) are independently confirmed to have left claim 39's wording untouched. The sentence
   is defensible read as "this document's as-published claim language dates to May 2023," but
   the present-tense "is" invites a stronger reading than the record independently supports.
2. **EF10** — The US-only/no-PCT/no-continuation observation (line 99) is accurate to
   fact-check-log's `family-us-only` entry, but that entry's own evidence_level is
   **bibliographic** — the weakest tier actually used anywhere in the essay ("not independently
   re-fetched this run"). The essay hedges appropriately ("offered as an observation... the
   record does not say why"), which is exactly why it clears the bar, but it's the thinnest
   evidentiary floor among the SUPPORTED rows.
3. **"Before the company had a product to sell" / "before there was anything to sell"**
   (lines 24, 103) — a reasonable timeline inference (patent filed 2023; shipping claims dated
   2026) rather than a fact tied to any specific fact-check-log entry verifying Etched had zero
   commercial product or revenue as of the May 2023 filing date.
