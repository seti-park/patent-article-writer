# Self-audit round 1 — Reader B (skeptical pro-subject reader)

- **Persona**: AI-infrastructure practitioner (systolic arrays, TPU pods, wafer-scale, HBM
  integration); application-vs-grant discipline native; multi-chip accelerator field known
  to be crowded. Hunting technical overclaim AND unearned hedging, symmetrically.
- **Target**: `handoff/03-edit/essay-final.md` (draft_version 3, closing_posture: firm,
  register: discovery)
- **Read**: essay-final.md; `input/patent.md` claims 1-42 in full + [0001]-[0057];
  `input/essay-context.md`; figures fig-01..07 (images inspected directly);
  `handoff/01-design/invention-summary.md` (Claim scope map + quote-anchor table);
  `handoff/01-design/fact-check-log.md` (external-fact base);
  `handoff/02-compose/thesis-trace.md` (signature-line declaration only, per pass-7 check 7).
- **NOT read** (blind rule): edit-log, revision-response.*, revision-notes, score-history,
  any other self-audit report.
- **Rules honored**: evidence-forced (every check → verdict + quoted span or ABSENT +
  severity); ADD-only; jurisdiction fence (fix classes = anchor / narrow / label / cut,
  never hedge); over-hedge is a first-class finding class.

---

## 1. Pass-7 checklist (evidence-forced)

| # | Check | Verdict | Evidence | Severity |
|---|---|---|---|---|
| 1 | Hook (discovery register) | **yes/pass** | ¶1 opens declarative on the discovery beat: "Three years before Etched pitched 'the best layer is no layer' as its memory philosophy on stage, both of its co-founders had signed that idea into the company's very first patent filing." No deferred question; pending-status clause comes AFTER the beat ("the patent office still hasn't said yes to it", ¶1-final = signature line 1). Full two-sided call lands by lead end: "What the filing is not, yet, is the property itself... a bet the company keeps paying to convert into an asset" (§1 ¶3). BUT the beat's venue ("on stage") is unsourced — see sa1B-F1. | (F1 logged separately, high) |
| 2 | Header-as-claim | **yes/pass** | All six `##` headers are assertions; header-only skim reconstructs: paper trail → one array from identical chips → memory claims delete the switch → forgetting math / remembering sidecar → keeps paying to own it → asset in formation. One header overreaches an embodiment ("Stitched From Identical Chips" — identicality is `[0028]` "In one embodiment", in no claim) — see sa1B-F4. | low (F4) |
| 3 | Steelman present | **yes/pass** | THIS-application objection conceded at full strength then refined: "The bear case is genuinely strong, and it is already on file. The examiner has assembled eight references... a crowded field... Claim 1, as drafted, reads on more or less any multi-chip systolic-array package, and breadth like that is usually the first casualty of examination. Even claim 39's distinctive absence, the no-switch hardwiring, could yet be judged routine for weight-stationary designs" (§5). Refinement retreats to what survives claim death: "None of that requires the claims to survive." No generic patent truism used as steelman. Pro-subject correctness check: this IS the strongest objection (weight-stationary/TPU-adjacent art + breadth); consistent with the Claim scope map's prosecution-risk notes. | none |
| 4 | No meta posturing | **yes/pass** | No reader-instruction found. "One timing detail belongs on the record with its label attached" and "offered as an observation" are evidence-status labels the brief REQUIRES (functional, exempt). Info-only: "a detail that matters later [0021]" (§2) is a three-word forward signpost, cohesion not posturing. | none |
| 5 | Jargon as signpost | **yes/pass** | Every term of art glossed in a clause and dropped: systolic array ("a grid of small arithmetic units that pass data to their neighbors on every tick"), HBM ("the stacked memory that feeds modern AI accelerators"), RCE ("a fee paid to keep arguing after the examiner has said no with finality"), PCT ("the treaty route for filing abroad"), continuation ("the follow-on filing that keeps a patent family growing"), weight-stationary ("accelerators that keep weights parked in place"), independent claim ("one that stands alone instead of refining another"), security interest ("a lender's registered claim on the assets if the loan sours"), layer normalization ("a housekeeping step between stages"). No overdepth. | none |
| 6 | No stub / rhythm break | **yes/pass** | Section paragraph counts ≈ 3 / 5 / 6 / 5 / 5 / 3; the short closer is conventional, no sibling markedly starved. | none |
| 7 | Thesis not over-restated | **yes/pass** | Signature lines declared in thesis-trace (3, exempt): §1 ¶1 close, §3 bold, §6 landing pair. Non-exempt verdict assertions sit in 3 sections: §1 ¶3 ("That mix is the verdict in miniature"), §5 close ("A signed, dated statement... is evidence about the company"), §6 ("The verdict is firm"). 3 ≤ 3. Each restatement does new work (preview → provenance → survives-bear-case → final). | none |

---

## 2. Deep claim audit — claims 1 / 15 / 26 / 39 + dependents, essay statements vs CLAIMS text

Read directly against `input/patent.md` claims 1-42 (not the summary).

| Essay statement | Claim text check | Verdict |
|---|---|---|
| "asks for memory channels wired straight into the columns of a giant multi-chip math array, no switch in between [0016], [0044]" (¶1) | The multi-chip + no-switch combination IS sought: claims 7/19/32 ("HBMs are hardwired to respective columns in the local systolic arrays without any switching element" inside the plurality-of-ICs families) and `[0044]` "This systolic array column could extend through all the ICs 215 in a column." Composite anchor honest. "giant" is embodiment color (see F2). | **accurate** (color noted, F2) |
| "It claims a package holding many small chips... joined to its neighbors so that the whole package computes as one enormous array [0013], [0028]" (§2) | Claim 1: "a plurality of integrated circuits (ICs), each comprising a local systolic array... chip-to-chip connections... to form a larger, combined systolic array." Plurality ≥ 2; "larger", not "enormous". Magnitude adjectives are the drawings'/description's, not the claim's. | **accurate scope, inflated color** (F2, low) |
| "Claim 39... Translated: a package with a chip carrying a math array, plus a separate memory device, with every memory channel hardwired to its own column or columns, 'without any switching element' in between [0016]" | Claim 39 verbatim: "an IC comprising a systolic array of data processing units (DPUs); and a separate memory device comprising a plurality of channels, wherein each of the plurality of channels is hardwired to respective one or more columns in the systolic array without any switching element." Translation is limitation-faithful, incl. "respective one or more columns" → "its own column or columns". | **accurate** |
| "Claim 39 is an independent claim... and it does not require the multi-chip package at all" | Claim 39 recites a single IC; no plurality, no chip-to-chip connections. Independent. | **accurate** |
| "the broadest package claim does not require memory chips, which the description concedes 'may not be needed' [0037]" | Claim 1 recites no memory element; `[0037]`: "the memory chips 210 may not be needed." ("Broadest" = claim 1 is the conventional reading; claim 26 trades chip-to-chip connections for a "grid-like pattern" limitation — neither strictly contains the other; not misleading.) | **accurate** |
| "A second independent claim seeks the weight-streaming arrangement itself: memory chips storing an AI model's weights, coupled to the chips that form the array's top row [0014]" | Claim 15: "...a plurality of memory chips configured to store weights for performing matrix multiplications in the combined systolic array as part of an AI model, the plurality of memory chips coupled to the plurality of ICs forming a top row..." | **accurate** |
| "As drafted, claims 11 through 13 give each chip the sidecar, give the sidecar the attention work, and wall its memory off from the arrays" | Claim 11 (aux circuitry in each IC + local memory chips coupled to it), claim 12 (aux performs self-attention on previous-token data in local memory), claim 13 ("the local systolic arrays do not communicate with the local memory chips"). Mapping exact; "as drafted" keeps it application-era. | **accurate** |
| "the memory idea got a stand-alone independent claim rather than a dependent footnote to the package claim" | Claim 39 independent; memory-half also lives as dependents 7/19/32 — essay's point (stand-alone election) is correct. | **accurate** |
| "Claim 1, as drafted, reads on more or less any multi-chip systolic-array package" (§5 steelman) | Slight breadth overstatement in the bearish direction: the "form a larger, combined systolic array" limitation is real (a multi-die package of INDEPENDENT per-die arrays — the common MCM pattern — does not read). "More or less" hedges it; in a steelman, overstating the examiner's side is the safe direction. | **acceptable** (no finding) |
| Sought-as-owned scan (whole essay) | ABSENT. All scope verbs are application-era: "asks for", "claims", "seeks", "as drafted", "the applicant electing". Ownership appears only negated or conditional: "not the property itself"; "not an exclusive right to it"; "If claim 39 and its memory-side siblings emerge... becomes property it owns." §3's "can be judged, and owned, on its own" is modal ("can be") and sits under the lead's explicit "not, yet, the property". No grant-era "locks/requires/fences" anywhere. | **pass** |

**Claim scope map conformance**: locked class ABSENT from map (pending edition) and essay
uses none. "Leaves open" honored (interposer/stack, UCIe, directionality never asserted as
claim content). **Pins**: map declares "No pinned point limitations exist" — essay presents
every number (128×128, 100s of GB, 1 TB/s, 98%, 100×400) as the background's/description's,
never as a claim bound: "by the description's own numbers", "That sentence lives in the
description rather than in any claim", "none of what it shows is claimed anywhere". Pass.

---

## 3. Mechanism honesty (figures inspected directly)

| Item | Essay | Spec/figure | Verdict |
|---|---|---|---|
| Combined array | "the whole package computes as one enormous array"; seams "hidden from the machine that matters" + block quote `[0028]` | `[0028]` host-perspective quote verbatim; FIG. 2 shows 9 ICs (215A-I), dashed 250 boundary | **pass** — one-array claim correctly pinned to host perspective, not physics |
| Row/column directionality | Weights "enter at the top and get reused all the way down" `[0039]`; tensor "streams in from the left" `[0021]`; no explicit uni/bidirectional claim made | FIG. 2/3: vertical arrows one-way down, horizontal double-headed; `[0029]` | **pass** — nothing asserted beyond spec |
| Top-row feed | claim-15 translation; "adding rows of chips adds compute without adding a single memory chip [0039]"; "multiple memory chips per top-row chip... 'more than 1 TB/s' [0040]" | FIG. 2 (one chip per top-row IC), FIG. 3/4 (multiple per top-row IC, 305A-F); `[0039]`, `[0040]` verbatim substrings | **pass**; "FIG. 3 draws the square-grid version with six memory chips across the top" matches the six drawn boxes (ellipses permit more — not contradicted) |
| FIG. 5 hardwiring | "two memory chips (505), four independent channels (510), dedicated wires (520), four columns (515), and nothing else in the path" | Image: 505A/B, 510A-D, wires 520, columns 515A-D, direct wire per channel-column pair, no intervening element | **pass** — exact |
| FIG. 5 trade | "a column can now read only its own channel" | `[0045]` "this column may be unable to read data... assigned to the channel 510B" | **pass** |
| FIG. 6 sidecar | caption: 605 = auxiliary circuitry inside IC 615, 610 = private local memory OUTSIDE combined array 650 | Image confirms; note invention-summary records a Phase-0 manifest defect swapping 605/610 — the essay uses the CORRECTED labels | **pass** (defect not propagated) |
| FIG. 7 Time A/B | Caption ties the stall to Time B ("the lone stall at layer normalization (Time B)"); Time A not used | `[0057]` "This is shown at Time B where the array stalls"; image: hatched stall band at Time B; `[0056]` Time A = pre-feed overlap, which the essay renders as prose without the label | **pass** |
| FIG. 7 claim status | "none of what it shows is claimed anywhere" | Claims 1-42 are all apparatus claims; no pipelining/batching/utilization claim exists | **pass** |
| FIG. 1 | "one grid can carry two computations at once" | Image: hashed vs non-hashed DPUs, Multiplication #1/#2 legend; `[0024]` | **pass** |
| TPU comparison | "Google's TPU ran its floating-point matrix units at 128×128 on generations through v5p, and moved to 256×256 with Trillium" | fact-check-log `tpu-mxu-128x128` (tier-1, two Google sources, both in `# Sources`). Practitioner check: "floating-point" correctly excludes v1's 256×256 INT8 MXU; v2-v5p MXUs are 128×128; Trillium (v6e) 256×256. Per-unit phrasing ("matrix units at 128×128") survives the multiple-MXUs-per-chip pedantry. | **pass** — well-drafted |
| Arithmetic color | "roughly sixteen thousand multipliers" (128×128 = 16,384); "a feature film's worth of data every five thousandths of a second" (1 TB/s × 5 ms = 5 GB) | — | **pass** |

---

## 4. External-fact fencing

| Rule | Verdict | Evidence |
|---|---|---|
| ONE prosecution label sentence | **pass** | The dated record appears in exactly one sentence: "As of the May 2026 record, this application is still pending, with examination continuing after a final rejection mailed 23 October 2025 and a request for continued examination (an RCE) docketed 24 April 2026." (§5 ¶1). Lead clauses ("still hasn't said yes", "still being argued with an examiner") are status-only, no dates; the RCE gloss defines the term without re-narrating rounds. No battle narrative. |
| Both-or-neither | **pass** | Collateral facts and the rejection record co-occur in §5; neither appears without the other. |
| Portfolio-scope liens | **pass** | "Both liens are blanket, selecting nothing and saying nothing about any single filing's worth"; lien-1 pool includes "two compiler applications that were later rejected"; symmetric creditor frame present ("what a creditor reaches if the bet goes wrong"); lead preview stays portfolio-scoped ("the patent stack this filing belongs to"). Effective dates (19 Apr 2024 / 18 Jul 2025) used, not recordation dates; reel/frames match the log. Timing detail rendered dates-only with the inference label: "The dates are facts. Any motive read into them is inference." |
| Company-claim attribution | **pass** | "$1B+ contracts", "$800m raised", racks "in the company's telling" / "every figure the company's own claim (TechCrunch)". |
| Examiner-art clause | **pass** | "eight references... multi-node machine-learning acceleration, hybrid parallelism and neural-network accelerator architectures, with Intel, IBM and Rambus among the assignees" — fully covered by fact-check-log `examiner-art-8refs` (assignees incl. Intel, IBM, Rambus, ETRI; "among" is accurate). |
| LVI absence + 18-month caveat | **pass** | "appears nowhere in this filing... applications younger than 18 months can exist unpublished and unseen" — matches `lvi-absent-here`. |
| Family observation | **pass** | US-only / no PCT / no continuation / trio contrast, "offered as an observation... the record does not say why" — matches `family-us-only`, motive-free. |
| Venue of the pitch | **FAIL** | See sa1B-F1 below. The evidence base records a THREAD; the essay stages a keynote, six times. |

---

## 5. Grounding spot-check (patent anchors; 6 samples across §2, §3, §4 + both block quotes)

| # | Essay span | Anchor | Patent text | Verdict |
|---|---|---|---|---|
| 1 | "most chips have, at most, floating point systolic arrays with a size of 128×128" | [0018] | verbatim substring of [0018] | pass |
| 2 | Block quote "from the perspective of the host 205... distributed on separate ICs 215" | [0028] | exact | pass |
| 3 | "could extend through all the ICs 215 in a column" | [0044] | verbatim substring | pass |
| 4 | "avoids having to add a switching element between the local systolic array" + "which can save space and power" | [0045] | split quote correctly routes AROUND the USPTO run-on typo "array 220and" (quote-anchor note honored) | pass |
| 5 | "does not take instructions at runtime, and only executes instructions in a preset loop" | [0027] | verbatim substring; essay adds the honest label "lives in the description rather than in any claim" — true (no claim recites instructions) | pass |
| 6 | "a 98% or greater utilization" | [0057] | verbatim substring; presented as description's number, not a bound or claim value | pass |

Beyond the samples, every `[dddd]` anchor in §2, §3 and §4 was checked against
`input/patent.md` during the read ([0002], [0003], [0013], [0014], [0016], [0018], [0019],
[0021], [0024], [0027], [0028], [0035], [0037], [0038], [0039], [0040], [0043], [0044],
[0045], [0047], [0048], [0051], [0053], [0055], [0056], [0057]): no mismatch found. All
essay quotes are substrings of Quote-anchor rows. Block quote [0016] is character-exact.

---

## 6. Over-hedge symmetric check (6G territory; closing_posture: firm)

- **Qualifier-led verdict**: ABSENT. §6 opens "The verdict is firm. This document is the
  real origin of Etched's memory story."
- **Safe-harbor boilerplate**: ABSENT. No "patents don't guarantee products/stock gains"
  truism anywhere; the category-limits sentence was not spent.
- **Anti-hype guard count**: exactly ONE in the closing, and it is THIS-application
  specific: "Racks shipping this summer, if they ship, are not evidence that these claims
  will grant. That question gets decided against the examiner's cited art, nowhere else."
  (§3's "What no filing can show is silicon" is the sanctioned scope fence at the CSM echo,
  not a second closing guard; it does adjacent work but reads as scope labeling, not hedging.)
- **Conclusion safer than body's evidence (6G over-hedge)**: NO. The body's verified
  discovery (claims 7/19/32/39 dated May 2023; founders as inventors; RCE spend; collateral)
  licenses exactly the two-sided call made; nothing earned is withheld.
- **Overreach direction**: "authentically the founders' own" (§6) is provenance
  (inventorship + pre-product claim language), and the essay has already fenced novelty two
  sections earlier ("The patent office decides whether early also meant original") — not an
  overreach. "The test ahead is binary and public" defines its own dichotomy in-sentence
  (materially intact vs narrow-to-ornament-or-die) — acceptable.

**Verdict: symmetric, pass. No hedge finding, no overreach finding at the verdict layer.**

---

## 7. Findings (ADD-only)

### sa1B-F1 — Unsourced venue: the "stage"/"keynote" framing has no fact behind it — **high**
- **Check**: external-fact fencing / grounding of non-patent facts (pass-3 class); also
  contaminates check 1's hook and signature line 3.
- **Verdict**: FAIL — the run's entire evidence base for the July 2026 moment is a social
  **thread** plus press coverage. fact-check-log `thread-claims-2026-07`: "Etched's July
  2026 stealth-exit thread... the 'each memory layer adds latency; the best layer is no
  layer' philosophy line is **the thread's pitch** (company framing)." No logged fact
  records a stage event, launch keynote, or presentation. The essay itself twice says
  "thread" ("The thread that announced Etched's stealth exit...", "the company's
  stealth-exit thread made the same idea its memory pillar") — yet asserts a stage six times:
  1. header caption: "Etched pitched this **on stage** as its no-layer memory philosophy in July 2026."
  2. §1 ¶1: "Three years before Etched pitched 'the best layer is no layer' as its memory philosophy **on stage**"
  3. §1 ¶1: "The **stage version** arrived in July 2026"
  4. §6: "The one thing the **stage** cannot do is finish the paperwork."
  5. §6: "The place to watch is not the **keynote** but the application's public docket"
  6. §6 (signature line 3): "**On stage** the layer is already gone."
- **Why high**: an invented/unevidenced scene detail presented as fact on the three
  highest-trust surfaces (header caption, hook ¶1, closing landing), in an essay whose
  central contrast IS "the pitch venue vs the filing". Provenance note: the stage wording
  originates in the design spine (thesis-trace one-liner: "pitched it on stage"), i.e., an
  upstream injection every downstream pass inherited — exactly the blind spot pass-7 exists
  for. Signature line 3 is protected surface for echo/count only; thesis-trace states
  "pass-3/4 factual review applies in full."
- **Fix (jurisdiction fence — never a hedge)**: EITHER (a) anchor fix: if the TechCrunch
  piece or another citable source documents an actual launch event/keynote, add the fact to
  the evidence base and Sources; OR (b) narrow/cut: recast venue-neutral or thread-true,
  e.g. ¶1 "pitched... as its memory philosophy in its launch thread"; "The public version
  arrived in July 2026"; §6 "The pitch cannot finish the paperwork"; "The place to watch is
  not the launch thread but the application's public docket"; landing "In the pitch the
  layer is already gone. At the patent office, Etched is still paying to own the deletion."
  The verdict and register survive unchanged.

### sa1B-F2 — Claim-1 translations wear the embodiment's magnitude — **low**
- **Check**: deep claim audit (claim-scope color).
- **Verdict**: minor. "a **giant** multi-chip math array" (¶1), "**many small** chips...
  one **enormous** array" (§2) translate claim 1, whose drafted floor is "a plurality"
  forming "a larger, combined systolic array" — two chips suffice. The essay's own steelman
  later states the true breadth ("reads on more or less any multi-chip systolic-array
  package"), so the reader is corrected, but the first-touch translation is dressed in
  FIG. 2/3 scale.
- **Fix**: optional — hang the magnitude on the description where it lives (e.g. the
  drawings' nine-chip grid, `[0033]`'s up-to-10000-column local arrays) or leave as-is;
  the §5 correction already exists.

### sa1B-F3 — "The pitch and the claims describe the same absence" states identity on company framing — **low**
- **Check**: mechanism honesty / external-fact tiering (the attack sentence).
- **Verdict**: minor overstatement. The pitch line is tier-3 company framing for a
  CLUSTER-scale memory story ("CSM, Cluster Scale Memory"); the claims delete a switching
  element between HBM channels and array columns INSIDE a package. Rhyme is established
  (both name a deleted intermediary); identity ("the same absence") is asserted, not
  evidenced — the essay's own next sentences concede the epistemic gap ("What no filing can
  show is silicon... invisible from the patent record"). The mapping itself is
  brief-sanctioned (essay-context: the claim-39 family "is the... philosophy of the
  thread's CSM pillar"), which caps this at low.
- **Fix**: narrow one verb: "the pitch and the claims **name** the same absence" or "the
  claims put a May 2023 date on the philosophy the pitch line sells" — same energy, scope
  honest.

### sa1B-F4 — "Identical chips" generalized from an embodiment — **low**
- **Check**: header-as-claim / overpromising headers.
- **Verdict**: minor. Header "One Giant Array, Stitched From **Identical** Chips" and body
  "The chips are **deliberately** interchangeable" rest on `[0028]` "In one embodiment, the
  ICs 215 are all identical." — no claim requires identicality, and "deliberately" reads
  intent into an embodiment sentence. The body quote does carry its own "In one embodiment"
  label, which keeps the paragraph honest.
- **Fix**: optional — "Stitched From Interchangeable Chips" or keep; the in-body quote
  already labels it.

### sa1B-F5 — Printed date tension: "July 2026" vs the essay's own "(30 June 2026)" source line — **low**
- **Check**: external-fact fencing (internal consistency).
- **Verdict**: minor. Body and caption date the pitch "July 2026" (per the brief and
  fact-check-log, which both say "July 2026 stealth-exit thread") while the essay's Sources
  section prints "TechCrunch, Etched stealth-exit coverage (**30 June 2026**)" — coverage
  cannot predate the thing it covers by a different month. Inherited from the evidence
  base, but the essay is where both dates appear side by side for the reader.
- **Fix**: anchor fix — reconcile to the sourced date ("the thread of 30 June 2026") or
  soften the body to the season ("in the summer of 2026"), whichever the log supports; if
  F1's rewrite lands, fold this into it.

---

## 8. Persona verdict (skeptical pro-subject reader)

The patent-side work survives a hostile practitioner read unusually well: every claim
translation I audited is limitation-faithful, description-only material (preset loop,
FIG. 7, 98%, 1 TB/s) is explicitly labeled as unclaimed, the TPU comparison is drafted
precisely enough to survive the v1-was-INT8 pedantry, and the steelman is the real
objection (weight-stationary art + breadth), conceded before it is refined. What does
outrun the evidence is stagecraft, not analysis: the essay's pitch-vs-paper frame invents
a stage and a keynote that its own fact base records only as a thread — six times, on the
caption, the hook, and the closing landing.

**The one sentence I'd attack**: "The pitch and the claims describe the same absence, and
this document is where the absence has a date." — as a CSM skeptic I'd answer that a
cluster-scale memory pillar and a package-internal channel-to-column hardwire are cousins,
not the same absence; one verb ("name", not "describe") closes the gap. Runner-up: "On
stage the layer is already gone" — there is no stage in this run's record.

**Finding count**: 1 high (sa1B-F1), 0 medium, 4 low (sa1B-F2..F5). No over-hedge finding;
verdict symmetry is clean in both directions.
