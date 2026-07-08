# Self-Audit Round 1 — Grounding Verification

Instrument: `grounding-verifier` (blind to other self-audit reviewers). Scope: fidelity only —
no comment on tone, stance, hedging, or structure. Target: `handoff/03-edit/essay-final.md`
(accepted essay).

## 0. Mechanical gate layer

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

Both mechanical gates PASS. (The anchors gate does not accept `--patent`; re-run without it
per its own usage string. The FIGREF-000 line is a WARN about missing `--figures` input to
this invocation, not a finding against the draft.)

## A. Anchor-by-anchor fidelity table

Every `[dddd]`-bracket anchor in the essay (12 instances across 6 sentences/blocks).

| # | Essay sentence (anchor in bold) | Invention-summary span | Patent `input/patent.md` paragraph | Verdict |
|---|---|---|---|---|
| 1 | "One line states the whole idea: 'Embodiments are directed to ultra high bandwidth memory (HBM) with backend transistors' **[0018]**." | q-0018-1: "Embodiments are directed to ultra high bandwidth memory (HBM) with backend transistors." | [0018] "Embodiments are directed to ultra high bandwidth memory (HBM) with backend transistors." | **SUPPORTED** — byte-for-byte verbatim (essay quote omits only the terminal period, standard for a quote followed by a citation, not a wording change). |
| 2 | Block quote: "Each memory die in the die stack includes one transistor one capacitor (1T1C) backend dynamic random access memory (DRAM)." / "US 2026/0191095 A1, **[0069]**" — introduced by "Claim 1, as filed, then requires that each memory die in the stack carry a particular kind of cell." | q-0069-1: "Each memory die in the die stack includes one transistor one capacitor (1T1C) backend dynamic random access memory (DRAM)." Invention-summary's own claim-quoting rule (line 174): "claim 1 ↔ Example 1 [0069]... Phase 2 cites the Example spans (anchored), and may attribute them as 'the claim language as filed' only with the Example anchor attached." | [0069] "Example embodiment 1: ...Each memory die in the die stack includes one transistor one capacitor (1T1C) backend dynamic random access memory (DRAM)." Actual Claim 1 (unanchored, line 144) uses "comprises" where the Example uses "includes" — the only wording difference, both verbatim-present in patent.md. | **SUPPORTED** — verbatim quote, and the "Claim 1, as filed" attribution follows the invention-summary's own sanctioned convention (Example span, anchor attached) exactly. The prose claims only "carry a particular kind of cell," matching the quoted span with no addition. |
| 3 | "The filing's description spells this out, showing thin-film-transistor layers stacked one atop another **[0031]**..." | q-0031-1: "a first thin film transistor database 151, a first region 152 of TSV/HBI connections, a second thin film transistor database 153" | [0031] "...a die stack includes a first thin film transistor database 151, a first region 152 of TSV/HBI connections, a second thin film transistor database 153, and a second region 154 of TSV/HBI connections..." | **SUPPORTED** — "layers stacked one atop another" is a plain-language rendering of the alternating TFT-database / TSV-HBI-region structure; confirmed against the actual FIG. 1F image (see §E) which shows repeating "TRANSISTOR" bands. No overreach. |
| 4 | "...and it puts a size on one such die, at what 'can be an approximately 1.5 GB die based on back-end-of-line transistors' **[0027]**." | q-0027-1: "can be an approximately 1.5 GB die based on back-end-of-line transistors" | [0027] "...Each such die 120 can be an approximately 1.5 GB die based on back-end-of-line transistors." | **SUPPORTED** — exact verbatim substring. Correctly framed as "the filing's description... puts a size" (description-level, not a claim pin) — matches Claim scope map: "'approximately 1.5 GB die'... [is] description... not a claim limitation." |
| 5 | "It describes a memory cube stacked eight high and beyond **[0023]**, with the silicon thinned to enable that many-layer stacking **[0031]**." | q-0023-1: "a die stacking cube is 8-high and beyond." / q-0031-2: "thinning of the silicon can be implemented to enable many-layer stacking" | [0023] "...a die stacking cube is 8-high and beyond..." / [0031] "...thinning of the silicon can be implemented to enable many-layer stacking." | **SUPPORTED** (both anchors) — accurate paraphrase of both spans. Correctly framed as "the filing... describes" — not attributed to Claim 1 (8-high is dependent claim 2/7 per the Claim scope map; the essay never calls it a claim-1 requirement here). |
| 6 | "Traffic moves down the stack through what the patent calls TSV gutters: columns of through-silicon vias, the vertical wires punched straight through a die **[0073]**." | q-0073-1: "wherein each memory die in the die stack includes a plurality of alternating sub-channels and through-silicon via (TSV) gutters" | [0073] "Example embodiment 5: ...each memory die in the die stack includes a plurality of alternating sub-channels and through-silicon via (TSV) gutters." | **SUPPORTED** — the anchor covers the term "TSV gutters" itself (verbatim in [0073], a dependent-claim-5 span, not attributed to claim 1). The appositive "columns of through-silicon vias, the vertical wires punched straight through a die" is a definitional gloss of the industry-standard term "through-silicon via," not a claim beyond the patent. |
| 7 | "Four gutters are cut into every die, each carrying the data for a pair of sub-channels **[0034]**." | q-0034-6: "There are four TSV gutters in each die, one carrying data and control for sub-channels 0-1, and another for sub-channels 2-3 and so on." | [0034] "...There are four TSV gutters in each die, one carrying data and control for sub-channels 0-1, and another for sub-channels 2-3 and so on..." | **SUPPORTED** — accurate paraphrase, no addition. |
| 8 | "The base die carries the high-speed link to the processor over UCIe, or Universal Chiplet Interconnect Express, an industry standard for wiring one chiplet to another **[0020]**." | q-0020-2: "high speed universal chiplet interconnect express (UCIe) connections are included to funnel out the data from and XBM construct" | [0020] "...built-in self-test (BIST), redundancy, TSVs and high speed universal chiplet interconnect express (UCIe) connections are included to funnel out the data from and XBM construct." | **SUPPORTED**, with one note — "carries the high-speed link... funnel[s]... data" matches [0020]/the acronym expansion (verbatim "Universal Chiplet Interconnect Express (UCIe)" is at [0027], not [0020], but is the plain acronym expansion, not a substantive claim). The clause "an industry standard for wiring one chiplet to another" is true, external, uncontested background (UCIe Consortium) rather than patent content — see §C note; it does not overstate the patent and is not counted as a fidelity defect. |
| 9 | "It also holds spare memory arrays that can stand in for defective ones once the stack is bonded **[0034]**, a built-in repair budget for a part that cannot be reworked after stacking." | q-0034-5: "The base die has 4 die-sub-channels of redundant memory arrays (32 datablocks) to act as fungible recoverability resources for unrepairable defects in the top memory dies." | [0034] "...The base die has 4 die-sub-channels of redundant memory arrays (32 datablocks) to act as fungible recoverability resources for unrepairable defects in the top memory dies." | **SUPPORTED** — "spare memory arrays... stand in for defective ones" = "redundant memory arrays... fungible recoverability resources... unrepairable defects." "Once the stack is bonded" / "cannot be reworked after stacking" reflects the "post-assembly repair" framing at [0027] (used earlier in the same essay for the 1.5 GB quote), consistent with, not contradicting, [0034]. |
| 10 | "Intel sizes each die 'to have a die capacity of 0.5-5 GB' **[0034]**, and designs the whole block, in the document's words, 'With the goal of matching HBM4's footprint' **[0034]**." | q-0034-2: "to have a die capacity of 0.5-5 GB" / q-0034-1: "With the goal of matching HBM4's footprint" | [0034] "With the goal of matching HBM4's footprint, each XBM memory die is architected with 'N' datablocks to have a die capacity of 0.5-5 GB..." | **SUPPORTED** (both anchors) — both exact verbatim substrings. Correctly labeled "in the document's words" and as a stated goal, not a result; correctly kept off Claim 1 (this is spec [0034] per the Claim scope map, and the essay never calls it a claim requirement). |

**Tally: 12/12 anchor instances SUPPORTED. 0 UNSUPPORTED. 0 MISREAD. 0 OVERREACHED-BEYOND-ANCHOR.**

## B. Claim-scope verification

Checked every claim-scope statement against the Claim scope map (invention-summary.md
lines 67-81). The load-bearing rule under test: **claim 1 requires only "backend"** (as part
of "1T1C backend DRAM"); 8-high is dependent claim 2; UCIe / "match HBM4 footprint" is spec
[0034]; BIST / redundancy / sub-channels+TSV-gutters are dependent claims 3/4/5.

| Essay statement | What it attributes to Claim 1 | Correct per Claim scope map? |
|---|---|---|
| "Claim 1, as filed, then requires that each memory die in the stack carry a particular kind of cell" → quotes 1T1C backend DRAM only | Only the 1T1C-backend-DRAM cell requirement | **Correct.** Matches row 1: "each memory die comprises 1T1C backend DRAM (the word 'backend' is in the claim text)." |
| "Claim 1 says backend. It never says foundry, never says logic fab, never says without a DRAM fab." | Negative claim: what Claim 1 does *not* say | **Correct** — verified against claim 1 text directly (line 144 of patent.md): no occurrence of "foundry," "logic fab," or "DRAM fab." |
| "Claim 1 fixes a single word. It never names the channel material, never claims a logic-compatible process, never promises a yield." | Negative claim | **Correct** — matches Claim scope map: "The channel MATERIAL is never named (no oxide / IGZO / amorphous)." |
| "That is the strategic weight of the claim word. Backend belongs to the logic-and-packaging world, not the DRAM front-end." / "the reading begins... the leap is mine, not the document's" | Explicitly labeled as essay inference, not a claim assertion | **Correct** — matches the map's guard: "the logic-foundry / no-DRAM-fab / cost / $-per-bit / yield / channel-material reading is EXTERNAL strategic inference, never attributed to claim or description." |
| 8-high stack, TSV gutters, UCIe, base-die redundancy, "match HBM4's footprint," 0.5-5 GB (§3, "A Tower Built to Match HBM4's Footprint") | Attributed to "the filing," "the filing describes," "the document's words" — never to "claim 1" | **Correct** — none of these dependent-claim/spec-only features is promoted into a Claim 1 requirement anywhere in the essay. |
| "The one thing claim 1 settles is that the memory cell is built in the back-end" (§6 closing) | Only the backend-cell requirement | **Correct**, consistent throughout. |

**No instance found of a spec/dependent-claim feature (8-high, UCIe, match-HBM4-footprint,
BIST, redundancy, sub-channels/TSV-gutters, the 1.5 GB or 0.5-5 GB figures) being promoted
into a Claim 1 requirement.** Every such feature is consistently attributed to "the filing,"
"the description," or "the document," never to "claim 1."

## C. External (non-patent) fact verification

Every external factual claim in the essay, matched to its `fact-check-log.md` entry.

| Essay claim | fact-check-log Fact ID | Tier / evidence_level | Match |
|---|---|---|---|
| "Intel sold its NAND flash business to SK hynix in 2021 and wound down its Optane memory line the year after" | `intel-exited-memory` | tier-3 / trade-press-reported | **Matches.** |
| "Three companies make the world's HBM, and Intel sells none of it" | `hbm-supply-concentration` (three-maker HBM market) + `intel-exited-memory` | tier-3 / analyst-estimate + tier-3 / trade-press-reported | **Matches** (reasonable compound of two logged facts). |
| "The world's DRAM comes from just three makers" | `dram-three-player` | tier-2 / analyst-estimate | **Matches.** |
| "SK hynix alone holds around 60% of the market [HBM], with Samsung and Micron dividing most of the rest" | `hbm-supply-concentration` (SK hynix ~61-62%, Micron ~21%, Samsung ~17%) + `hbm-share-crosscheck` | tier-3 / analyst-estimate | **Matches** — "around 60%" is a conservative (not inflated) rounding of 61-62%. |
| "Intel and SoftBank are co-developing a stacked memory called ZAM, or HB3DM, aimed squarely at beating HBM" | `zam-hb3dm-specs` | tier-3 / trade-press-reported | **Matches.** |
| "ZAM stacks on a diagonal Z-angle joined by hybrid bonding... This filing uses vertical TSV gutters and UCIe instead" | `zam-hb3dm-specs` + fact-check-log's own "Connect, do not conflate" guard | tier-3 / trade-press-reported | **Matches** the guard's own wording almost exactly; correctly posture as "same-family cousin," never "this patent is ZAM." |
| "the partner reported to actually fabricate the DRAM is Powerchip, not Intel" | `zam-powerchip-fab` | tier-3 / trade-press-reported | **Matches.** |
| "SK hynix, Samsung and Micron each run their own 3D-DRAM programs, SK hynix's aimed at around 2030" | `incumbent-3d-dram` | tier-3 / trade-press-reported | **Matches.** |
| "In imec's capacitor-less cell, two thin-film transistors replace the storage capacitor entirely, and even that remains a lab result" | `imec-2t0c-igzo` | tier-2 / bibliographic | **Matches** — 2T0C correctly contrasted with this patent's 1T1C (capacitor retained, not removed). |
| "The related work is due to surface at VLSI 2026 in June" | `zam-hb3dm-vlsi2026` | tier-3 / trade-press-reported | **Matches.** |
| "The same technology family is aimed at commercialization around 2029" | `zam-timeline` | tier-3 / trade-press-reported | **Matches.** |
| All 9 "Sources" list entries (imec, Astute Group, Counterpoint, S&P Global, 3x Tom's Hardware, TrendForce, TechPowerUp) | cross-checked against fact-check-log source URLs | — | **All match** the logged URLs. |

**No unlogged, load-bearing external fact found.** Two borderline items, disclosed for
transparency but **not counted as fidelity defects** because they are uncontested,
non-numeric technical/definitional background (the same class as explaining what "DRAM" or
"TSV" means) rather than contestable claims of the kind the fact-check-log is built to track:

- "UCIe... an industry standard for wiring one chiplet to another" (line 46) — true and
  well-known (UCIe Consortium), but not itself a fact-check-log row.
- "the layer engineers call the front-end" (line 34) and "hybrid bonding, which fuses two
  dies face to face without solder" (line 60) — standard semiconductor-industry vocabulary,
  correctly left unanchored to the patent (confirmed: "front-end"/"front end" does not appear
  anywhere in `input/patent.md`; not falsely attributed to it).

If the orchestrator wants zero ambiguity, the minimal fix for all three is a one-line
addition to `fact-check-log.md` at tier-1/common-knowledge — not a rewrite, and not a hedge.

## D. Verbatim quote verification

Every quotation-marked patent phrase in the essay (5 distinct quotes, one delivered as a
block quote), checked byte-for-byte against `input/patent.md`.

| Essay quote | Patent source | Verbatim? |
|---|---|---|
| "Embodiments are directed to ultra high bandwidth memory (HBM) with backend transistors" | [0018] | **Yes**, exact. |
| "Each memory die in the die stack includes one transistor one capacitor (1T1C) backend dynamic random access memory (DRAM)." | [0069] | **Yes**, exact, including terminal period. |
| "can be an approximately 1.5 GB die based on back-end-of-line transistors" | [0027] | **Yes**, exact substring. |
| "to have a die capacity of 0.5-5 GB" | [0034] | **Yes**, exact substring. |
| "With the goal of matching HBM4's footprint" | [0034] | **Yes**, exact substring (capitalization matches sentence-initial "With" in the patent). |

No other quotation-marked strings in the essay body are patent text (the remainder are
bibliography article titles in the Sources section, correctly presented as such).

## E. Supplementary check — figure captions (no `[dddd]` anchor, spot-checked anyway)

Figure captions make direct factual/numeral claims about the patent's drawings without
carrying bracket anchors. Spot-checked all four for consistency with `input/patent.md` text
and, for FIG. 1F, against the actual image (`input/figures/fig-01F.png`), since the caption's
"tiers labeled TRANSISTOR" claim is a testable visual assertion:

- **FIG. 1B caption** ("Identical memory dies stack eight-high and beyond as one die stack
  (111)... base die (115) that routes every signal in and out") — consistent with [0025]
  (111/112/114/115 numerals) + [0023] (8-high) + [0034] ("All I/O to the compute die is
  routed through a base die"). Accurate synthesis, no overreach.
- **FIG. 1F caption** ("tiers labeled TRANSISTOR, the thin-film transistors (151, 153)...
  separated by regions of vertical interconnect (152, 154)") — **verified directly against
  the image**: the figure shows repeating rows literally labeled "TRANSISTOR" and "GM,"
  with columns 151/153 (TRANSISTOR/GM bands) and 152/154 (HBI PAD/TPH PAD + via columns),
  matching both [0031]'s numeral list and the `figures-manifest.md` entry ("transistor/GM
  layers, HBI/TPH pads, groups 151-157"). Accurate.
- **FIG. 1G caption** (eight sub-channels 161A-161H, four TSV gutters 162-165) — matches
  [0033] exactly.
- **FIG. 1A caption** (logic die 106 beside HBM stack 104, joined on one interposer) —
  matches [0022] exactly.

No defects found.

## Summary

| Category | SUPPORTED | UNSUPPORTED | MISREAD | OVERREACHED-BEYOND-ANCHOR |
|---|---|---|---|---|
| `[dddd]`-anchored sentences (12 instances / 10 sentences) | 12 | 0 | 0 | 0 |
| Claim-scope statements (6 checked) | 6 correct | 0 | 0 | 0 |
| External facts (11 checked) | 11 traced | 0 unlogged (2 minor common-knowledge notes, not defects) | — | — |
| Verbatim quotes (5) | 5 exact | 0 | — | — |

**All items are SUPPORTED.** No non-SUPPORTED findings to report.
