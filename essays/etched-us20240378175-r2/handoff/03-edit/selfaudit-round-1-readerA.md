# Self-audit round 1 — Reader A: impatient investor

- **Artifact:** `handoff/03-edit/essay-final.md` (draft_version 3, closing_posture: firm, register: discovery)
- **Persona:** curious retail investor per `_shared/references/reader-profile.md`; 6-minute read; headers first, captions before body; came from the Etched stealth-exit thread.
- **Inputs:** essay-final.md, input/patent.md (full text + claims), input/essay-context.md, input/figures/fig-03.png + fig-05.png, handoff/01-design/invention-summary.md (Claim scope map + quote anchors), handoff/01-design/fact-check-log.md, thesis-trace.md `## Signature lines` only. No edit-log, no revision-response, no score-history, no other self-audit artifact read.
- **Rules honored:** evidence-forced; add-only; jurisdiction fence (fix recommendations are anchor/narrow/label/cut, never hedge).

## Checklist (items 1-9)

| # | Check | Verdict | Evidence (quoted span or ABSENT) | Severity |
|---|---|---|---|---|
| 1a | Hook: ¶1 lands discovery beat, declarative, no insurance ahead | **yes (pass)** | ¶1 s1: "Three years before Etched pitched \"the best layer is no layer\" as its memory philosophy on stage, both of its co-founders had signed that idea into the company's very first patent filing." Insurance arrives only at ¶1's end ("the patent office still hasn't said yes to it"), after the beat. Cover caption carries no insurance. First-two-lines test: the beat starts at word one. | — |
| 1b | Full two-sided call by end of lead section | **yes (pass)** | §1 ¶3: "That mix is the verdict in miniature. The filing proves authorship... What the filing is not, yet, is the property itself. Three years in, the no-switch memory idea remains a bet the company keeps paying to convert into an asset." Both sides land inside the lead. | — |
| 2 | Header-as-claim; header-only skim reconstructs argument | **yes (pass)** | "The Pitch Has a Paper Trail" / "One Giant Array, Stitched From Identical Chips" / "The Memory Claims Delete the Switch" / "Math That Forgets, a Sidecar That Remembers" / "Etched Keeps Paying to Own It" / "An Asset in Formation". Skim reconstructs: written-down early, what it is, what it deletes, how it splits the work, the spend, the verdict. Two headers are noun phrases but claim-bearing. | — |
| 3 | Steelman present: strongest THIS-patent objection, conceded then refined | **yes (pass)** | Conceded at full strength: "The bear case is genuinely strong, and it is already on file. The examiner has assembled eight references... Claim 1, as drafted, reads on more or less any multi-chip systolic-array package" plus "Even claim 39's distinctive absence, the no-switch hardwiring, could yet be judged routine for weight-stationary designs". Refined, not neutralized: "What survives the bear case is the record of behavior... None of that requires the claims to survive." No generic patent truism used as steelman. | — |
| 4 | No meta posturing / reader instruction | **yes, one borderline** | Labeling devices are functional and brief-mandated ("One timing detail belongs on the record with its label attached", "offered as an observation"). Borderline forward pointer: "a detail that matters later [0021]" (finding sa1A-F05, low). | low |
| 5 | Jargon as signpost, no over-depth | **yes (pass)** | Every term of art glossed on first use: systolic array ("a grid of small arithmetic units that pass data to their neighbors on every tick"), HBM ("the stacked memory that feeds modern AI accelerators"), independent claim ("one that stands alone instead of refining another"), RCE ("a fee paid to keep arguing after the examiner has said no with finality"), security interests ("a lender's registered claim on the assets if the loan sours"), PCT, continuation, weight-stationary, layer normalization ("a housekeeping step between stages"). Claim language translated before the [0016] blockquote ("Translated: a package with a chip carrying a math array..."). Numbers land on owned scales (16,384 -> "roughly sixteen thousand multipliers"; 1 TB/s -> "a feature film's worth of data every five thousandths of a second"). Nits below flag-threshold: "reel/frame" unglossed (parenthetical citation, skippable), "PCIe" caption-only. FIG. 7 depth pays off with an investor read ("A document that only wanted to impress would have stopped at the giant array. This one budgeted its idle cycles."), so not jargon-overdepth. | — |
| 6 | No stub / rhythm break | **yes (pass)** | Section paragraph counts: 3 / 5 / 6 / 5 / 6 / 3. The two 3-paragraph sections are the lead and the verdict, both dense; no section reads as a stub against its siblings. ABSENT (no stub found). | — |
| 7 | Thesis not over-restated (<= 3 sections; declared signature lines exempt) | **yes (pass)** | Non-exempt verdict assertions in 3 sections: §1 ¶3 ("That mix is the verdict in miniature..."), §5 ("What survives the bear case is the record of behavior..."), §6 ("The verdict is firm..."). §3's bolded "The no-layer pitch is not marketing retrofitted onto hardware. It is claim language, dated May 2023." is declared signature line 2 (exempt from count; factual review applied, see item 8). Within budget. | — |
| 8 | Grounding spot-checks (5-sample + full-anchor sweep of §2, §3, §4 + claim scope map + pinned values) | **pass with 1 medium + 4 low findings** | See section below. Every sampled anchor verbatim-verified except two precision nits; claim-scope statements match the claims and the map; application-era language held throughout; no pinned value exists and none is described as a bound. The one medium is an EXTERNAL venue fact ("on stage"/"keynote"), not a patent anchor. | medium (F01) |
| 9 | Over-hedge symmetric check, incl. pending-as-crutch | **yes (pass, no finding)** | Call leads unwrapped: "The verdict is firm. This document is the real origin of Etched's memory story." Pending status is priced inside the call ("It is not yet the asset itself."), never deployed as an escape hatch; the close sets a binary, watchable test ("If claim 39 and its memory-side siblings emerge with the no-switch limitation materially intact... If they narrow to ornament or die..."). Exactly ONE patent-specific anti-hype guard in the closing: "Racks shipping this summer, if they ship, are not evidence that these claims will grant." No safe-harbor boilerplate anywhere (no "patents don't guarantee products", no "time will tell", no DYOR). Symmetric overreach also checked: "authentically the founders' own" is cabined to authorship, with originality explicitly ceded to the office ("The patent office decides whether early also meant original."). Conclusion is NOT safer than the body's evidence; no 6G finding either direction. | — |

## Grounding spot-check detail (item 8)

### 5-sample verbatim-span check (essay -> patent.md)

| # | Essay span (quoted) | Anchor | Patent text | Verdict |
|---|---|---|---|---|
| 1 | Blockquote "from the perspective of the host 205, the systolic array 250 appears to be one large array, even though it is physically made up of smaller local systolic arrays 220 distributed on separate ICs 215" | [0028] | identical, word for word | pass |
| 2 | Blockquote "Another embodiment in this disclosure is a package that includes an IC comprising a systolic array of data processing units (DPUs) and a separate memory device comprising a plurality of channels where each of the plurality of channels is hardwired to respective one or more columns in the systolic array without any switching element." | [0016] | identical, word for word; also matches claim 39's operative language | pass |
| 3 | "most chips have, at most, floating point systolic arrays with a size of 128×128" | [0018] | verbatim substring; essay's "roughly sixteen thousand multipliers" is a correct, clearly-owned comparison (128×128 = 16,384) | pass |
| 4 | "could extend through all the ICs 215 in a column" and "can be directly wired (or hardwired) to a particular column 515 in the local systolic array" | [0044] | verbatim substrings; essay's "the top of the package to the bottom" is fair gloss | pass |
| 5 | "a 98% or greater utilization" | [0057] | verbatim substring, BUT the frame verb overstates: see sa1A-F03 ([0057] says "may be small... and still result in", essay says "the array holds") | pass with low finding |

### Full-anchor sweep of three sections

- **§2 (One Giant Array):** [0013], [0028], [0018]x2, [0002], [0021]x2, [0024], [0019]x2, [0038], [0028] blockquote, [0028] "all identical" — ALL verified verbatim or accurate paraphrase. TPU external fact matches fact-check-log `tpu-mxu-128x128` and is source-attributed. One low: "The background gives two reasons" cites [0018], which sits in the detailed description, not the Background section (sa1A-F04).
- **§3 (Memory Claims):** [0043]x2 (incl. blockquote), [0044]x2, [0045]x2 (quote split cleanly around the source's "220and" run-on, per verbatim discipline), [0016] (translation-then-blockquote, translation accurate), [0037], [0014], [0039]x2, [0040], [0041 implied via FIG. 4 sentence] — ALL verified. Claim-39 statements ("independent claim", "does not require the multi-chip package at all") match claim text and map row 39. FIG. 5 part inventory (505/510/520/515) matches the image. Same [0043]-as-"background" labeling nit (sa1A-F04). FIG. 3 "six memory chips" literal-count nit (sa1A-F06).
- **§4 (Math That Forgets):** [0027] (verbatim + correctly labeled "lives in the description rather than in any claim"), [0003], [0047]x2, [0048], [0051] (verbatim), claims 11-13 summary matches claim text ("As drafted" prefix held), [0053], [0055], [0056], [0057] — verified, with two precision nits: "in batches" rides the [0053] anchor but is [0055] content (sa1A-F02), and the [0057] "holds" framing (sa1A-F03). The "none of what it shows is claimed anywhere" statement about FIG. 7 is TRUE per the claims and is exactly the map's description-only note, correctly presented as labeled analysis.

### Claim scope map conformance

- **No locked class exists; essay never uses grant-era language for claim content.** Verbs audited: "asks for", "It claims", "the application claims", "As drafted", "Claim 1, as drafted, reads on", "seeks", "Etched is seeking"-equivalents. Zero instances of "locks/requires/fences" for this application's claims. The single grant-register phrase ("the part Etched has since gotten granted") correctly refers to the OTHER, granted patent (US 12,361,091 B1).
- **Pinned values:** map declares none exist; essay presents 128×128, 100×400/400×100, 1 TB/s, three passes, 98% as the description's/background's own figures, never as claim bounds. Pass.
- **Both-or-neither edition rule:** collateral facts and the prosecution label sentence are both present (§5). Label budget honored: exactly one status sentence ("As of the May 2026 record, this application is still pending, with examination continuing after a final rejection mailed 23 October 2025 and a request for continued examination (an RCE) docketed 24 April 2026."); no battle narrative follows.
- **Lien discipline:** "Both liens are blanket, selecting nothing and saying nothing about any single filing's worth." — the hard rule is honored verbatim in spirit; timing detail carries its label ("The dates are facts. Any motive read into them is inference.").

## Findings

### sa1A-F01 — unsupported venue: "on stage" / "keynote" / "the stage version" (external-fact attribution)
- **check:** 8 (grounding, external fact) — also touches 1 and the protected surface
- **verdict:** no (venue not in evidence)
- **severity:** **medium** (escalate to high if the cited TechCrunch source does not describe a stage/keynote event)
- **evidence:** six occurrences place the July 2026 pitch on a stage: cover caption "Etched pitched this on stage as its no-layer memory philosophy in July 2026."; §1 "as its memory philosophy on stage" and "The stage version arrived in July 2026"; §6 "The one thing the stage cannot do is finish the paperwork.", "The place to watch is not the keynote but the application's public docket", and signature line 3 "On stage the layer is already gone." The run's entire evidence record sources the pitch to a THREAD: essay-context ("Etched's July 2026 stealth-exit thread (LVI + CSM claims...)") and fact-check-log `thread-claims-2026-07` ("the 'each memory layer adds latency; the best layer is no layer' philosophy line is the thread's pitch (company framing)"). The essay's own §3 correctly attributes the pillar to "the company's stealth-exit thread". No stage or keynote event appears anywhere in the run's fact base. Signature-line protection covers style and count, never accuracy (reader-energy.md §5), so line 3 is reviewable.
- **recommended fix (fence-compliant):** verify a stage/keynote event against the TechCrunch source; if unsupported, NARROW the venue ("in its launch thread" / "in public" / "in the company's telling") or CUT the stage imagery, including reworking signature line 3 and the cover caption's second sentence. Do not add a hedge; this is an attribution alignment.

### sa1A-F02 — anchor imprecision: "in batches" carried by [0053]
- **check:** 8 (grounding, anchor)
- **verdict:** no (anchor does not carry the clause)
- **severity:** low
- **evidence:** §4: "FIG. 7 charts one row of the combined array pushing a transformer layer through in batches [0053]". [0053] covers one row / one layer only; batching is [0055] ("input tensors may be divided up and processed in multiple batches").
- **recommended fix:** anchor fix — add [0055] (or cite [0053], [0055]).

### sa1A-F03 — hedged source value rendered as steady-state fact
- **check:** 8 (grounding, fidelity of a quantitative claim)
- **verdict:** no (verb firmer than source)
- **severity:** low
- **evidence:** §4: "even with that stall the array holds \"a 98% or greater utilization\" [0057]". Source [0057]: "the stalled time may be small relative to the computation time and still result in a 98% or greater utilization" — a may-outcome, not a held state.
- **recommended fix:** narrow — "the description puts utilization at \"a 98% or greater utilization\"" or "can still hold". Keeps the number, restores the source's modality.

### sa1A-F04 — "the background" mislabels detailed-description paragraphs
- **check:** 8 (grounding, document-structure claim)
- **verdict:** no (section label wrong twice)
- **severity:** low
- **evidence:** §2: "The background gives two reasons why anyone would bother." citing [0018]; §3: "the background is candid about how the industry handles it" citing [0043]. The Background section is [0002]-[0003]; [0018] and [0043] live in the detailed description. Anchors and quotes themselves are correct.
- **recommended fix:** narrow the label — "the filing gives two reasons" / "the description is candid".

### sa1A-F05 — forward-pointer meta: "a detail that matters later"
- **check:** 4 (meta-reader-instruction, judgment backstop past gate_meta resolution)
- **verdict:** borderline no
- **severity:** low (multi-vote candidate; arguably functional signposting that helps this persona)
- **evidence:** §2: "the filing notes they may be constants, a detail that matters later [0021]" — self-reference to the essay's own later section.
- **recommended fix:** if peers concur, cut the clause or replace with the payoff itself ("constants, which is what later makes the no-switch wiring possible").

### sa1A-F06 — FIG. 3 count stated more precisely than the drawing
- **check:** 8 (grounding, figure-literal)
- **verdict:** borderline no
- **severity:** low (weakest finding; the drawing does show exactly six labeled boxes)
- **evidence:** §3: "FIG. 3 draws the square-grid version with six memory chips across the top". fig-03.png draws six labeled memory chips (305A-305F) but with ellipsis dots between each pair, marking the count as open-ended, per [0040]'s "multiple memory chips 305 can be attached" (e.g. three per IC).
- **recommended fix:** narrow — "six labeled memory chips (and room for more)" or reuse the caption's accurate "multiple memory chips (305) feed each top-row chip".

## Persona verdict (impatient investor)

- **Hooked?** Yes, by the title plus caption before the body started: a dated drawing vs a dated pitch is exactly my kind of fact. ¶1 sentence one delivered it; I never had to wait for the point.
- **Stop-point:** none. The slowest stretch is §4's attention/sidecar middle (money thread thinnest there), but both paragraphs cash out in plain investor terms ("This one budgeted its idle cycles"), and I kept going. §5 is the section I came for and it pays the ¶3 collateral tease on time.
- **Un-glossed jargon hit:** none that stopped me. "reel/frame" and caption-only "PCIe" are skippable citations, not homework.
- **Leaving question:** "How do I watch the docket, and when is the next office-action decision due?" The essay names the place to watch (the application's public docket, application number in Sources) but gives no cadence. Acceptable, not a defect.
- **Share yes/no:** YES — I would quote "On stage the layer is already gone. At the patent office, Etched is still paying to own the deletion." — which is exactly why sa1A-F01 (is "on stage" real?) must be resolved before I repost it.
- **Reader-sentence repeatable after one read:** YES. I can say unaided: "Etched wrote the no-switch memory idea into its first patent filing in May 2023, three years before the hype thread, and the patent office still hasn't said yes." Note the essay corrected the brief's "two years" to "three years" (May 2023 -> July 2026), which is arithmetically right; content of the declared reader_sentence is fully delivered.

## Summary

- **Counts:** critical 0 / high 0 / **medium 1** / low 5.
- Checklist items 1, 2, 3, 6, 7, 9 pass clean with evidence; item 4 passes with one low; item 5 passes; item 8 passes the patent-anchor chain (all sampled anchors verbatim-true, claim scope map honored, no pinned-value abuse) but surfaces the one medium: the "on stage"/"keynote" venue is unsupported by the run's fact record and sits on the essay's most-shareable surfaces (cover caption, ¶1, closing signature line).
- No over-hedge and no pending-as-crutch: the firm verdict is evidence-proportionate in both directions.
