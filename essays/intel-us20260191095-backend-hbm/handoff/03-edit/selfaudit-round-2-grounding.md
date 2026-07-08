# Self-Audit Round 2 — Grounding RE-Verification (post-revision, draft_version 3)

Instrument: `grounding-verifier` (blind to adversarial-A/B and cold-reader reviewers; blind to
its own round-1 report — this is a fresh anchor-by-anchor pass, not a diff). Scope: fidelity
only — no comment on tone, stance, hedging, or structure. Target:
`handoff/03-edit/essay-final.md`, `draft_version: 3` (revised from the accepted `v2` by the
composer in revision mode to apply self-audit round-1 findings; see
`handoff/03-edit/revision-notes.md`).

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

Both mechanical gates PASS (identical result to round 1; the revision changed prose, not
anchors or quoted spans, so no gate regression is expected or found). The FIGREF-000 line is
a WARN about missing `--figures` input to this invocation, not a finding against the draft.

Supplementary mechanical cross-checks run for this round (script-verified, not gated):
- All 5 quotation-marked patent phrases confirmed byte-for-byte present in both
  `input/patent.md` and `handoff/03-edit/essay-final.md` via direct substring match.
- Every essay Sources URL confirmed to be a subset of `fact-check-log.md` URLs (no unlogged
  URL).
- `input/patent.md` confirmed to contain **zero** occurrences of: `front-end`, `front end`,
  `temperature`, `hybrid bond`, `foundry`, `logic fab`, `channel material`, `igzo`, `oxide`,
  `z-angle`, `zam` (case-insensitive) — confirming every one of these terms in the essay is
  correctly external/inferential color, never misattributed as patent text (none carry a
  `[dddd]` anchor).

## A. Anchor-by-anchor fidelity table (fresh pass, all 11 `[dddd]` instances)

| # | Essay sentence (anchor in bold) | Invention-summary span | Patent paragraph (key text) | Verdict | Recommended fix |
|---|---|---|---|---|---|
| S1 | §2: "One line states the whole idea: 'Embodiments are directed to ultra high bandwidth memory (HBM) with backend transistors' **[0018]**." | q-0018-1: "Embodiments are directed to ultra high bandwidth memory (HBM) with backend transistors." | [0018] "Embodiments are directed to ultra high bandwidth memory (HBM) with backend transistors." | **SUPPORTED** — byte-for-byte verbatim. | n/a |
| S2 | §2 block quote: "Each memory die in the die stack includes one transistor one capacitor (1T1C) backend dynamic random access memory (DRAM)." / "US 2026/0191095 A1, **[0069]**" — introduced by "Claim 1, as filed, then requires that each memory die in the stack carry a particular kind of cell." | q-0069-1 (verbatim match) + invention-summary's own claim-quoting rule (line 174): "Phase 2 cites the Example spans (anchored), and may attribute them as 'the claim language as filed' only with the Example anchor attached." | [0069] "Example embodiment 1: ... Each memory die in the die stack includes one transistor one capacitor (1T1C) backend dynamic random access memory (DRAM)." Claim 1 (unanchored, line 144) reads "comprises" where the Example reads "includes" — the only wording difference, both verbatim in patent.md. | **SUPPORTED** — verbatim quote; the "Claim 1, as filed" attribution follows the invention-summary's own sanctioned Example-anchor convention exactly; the prose claims only "carry a particular kind of cell," no more. | n/a |
| S3 | §2: "The filing's description spells this out, showing thin-film-transistor layers stacked one atop another **[0031]**..." | q-0031-1: "a first thin film transistor database 151, a first region 152 of TSV/HBI connections, a second thin film transistor database 153" | [0031] "...a die stack includes a first thin film transistor database 151, a first region 152 of TSV/HBI connections, a second thin film transistor database 153, and a second region 154 of TSV/HBI connections..." | **SUPPORTED** — "layers stacked one atop another" is a plain-language rendering of the alternating TFT-database/TSV-HBI-region structure; consistent with FIG. 1F. | n/a |
| S4 | §2: "...and it puts a size on one such die, at what 'can be an approximately 1.5 GB die based on back-end-of-line transistors' **[0027]**." | q-0027-1 (verbatim match) | [0027] "...Each such die 120 can be an approximately 1.5 GB die based on back-end-of-line transistors." | **SUPPORTED** — exact verbatim substring, framed as description-level ("puts a size"), never a claim pin — matches Claim scope map row 1. | n/a |
| S5 | §3: "It describes a memory cube stacked eight high and beyond **[0023]**..." | q-0023-1 (verbatim match) | [0023] "...a die stacking cube is 8-high and beyond..." | **SUPPORTED** — accurate paraphrase, attributed to "the filing describes," never to claim 1 (8-high is dependent claim 2/7 per the map). | n/a |
| S6 | §3: "...with the silicon thinned to enable that many-layer stacking **[0031]**." | q-0031-2 (verbatim match) | [0031] "...thinning of the silicon can be implemented to enable many-layer stacking." | **SUPPORTED** — accurate paraphrase. | n/a |
| S7 | §3: "Data drops down the stack through what the patent calls TSV gutters: columns of through-silicon vias punched straight through each die. They split the traffic into many independent sub-channels, the parallel data lanes whose combined width is where a memory's bandwidth comes from **[0073]**." | q-0073-1: "wherein each memory die in the die stack includes a plurality of alternating sub-channels and through-silicon via (TSV) gutters" | [0073] "...each memory die in the die stack includes a plurality of alternating sub-channels and through-silicon via (TSV) gutters." (Gutter/sub-channel routing detail also at [0034]: "four TSV gutters in each die, one carrying data and control for sub-channels 0-1...") | **SUPPORTED, with a note.** The gutters-split-into-sub-channels claim is grounded ([0073] + [0034]/q-0034-6, not anchored here but consistent). "The parallel data lanes whose combined width is where a memory's bandwidth comes from" is generic engineering background (channel-count → bandwidth is not stated in these words anywhere in patent.md — confirmed zero occurrences of "bandwidth" outside "high bandwidth memory/interconnect" boilerplate) — same class as the essay's other unanchored definitional glosses (TSV, front-end/back-end, UCIe-as-standard), which round 1 explicitly did not count as defects. Not contradicted by, and does not overstate, the patent. | n/a — if the orchestrator wants zero ambiguity, this generic clause could be logged at fact-check-log tier-1/common-knowledge, matching round 1's own disposition for equivalent clauses; not a rewrite. |
| S8 | §3: "The base die carries the high-speed link to the processor over UCIe, or Universal Chiplet Interconnect Express, an industry standard for wiring one chiplet to another **[0020]**." | q-0020-2: "high speed universal chiplet interconnect express (UCIe) connections are included to funnel out the data from and XBM construct" | [0020] "...built-in self-test (BIST), redundancy, TSVs and high speed universal chiplet interconnect express (UCIe) connections are included to funnel out the data from and XBM construct." (Acronym spelled out verbatim at [0027]: "Universal Chiplet Interconnect Express (UCIe) 132".) | **SUPPORTED** — "carries the high-speed link... funnel[s]... data" matches [0020]; the acronym expansion is verbatim patent language (from [0027]); "an industry standard for wiring one chiplet to another" is true, uncontested, external background (UCIe Consortium), not patent content and not an overstatement of it. | n/a |
| S9 | §3: "It also holds spare memory arrays that can stand in for defective ones once the stack is bonded **[0034]**, a built-in repair budget for a part that cannot be reworked after stacking." | q-0034-5 (verbatim match) | [0034] "...The base die has 4 die-sub-channels of redundant memory arrays (32 datablocks) to act as fungible recoverability resources for unrepairable defects in the top memory dies." | **SUPPORTED** — "spare memory arrays... stand in for defective ones" = "redundant memory arrays... fungible recoverability resources"; "cannot be reworked after stacking" restates "unrepairable defects" and is consistent with the "post-assembly repair" framing at [0027]. | n/a |
| S10 | §3: "Intel sizes each die 'to have a die capacity of 0.5-5 GB' **[0034]**..." | q-0034-2 (verbatim match) | [0034] "...each XBM memory die is architected with 'N' datablocks to have a die capacity of 0.5-5 GB." | **SUPPORTED** — exact verbatim substring, correctly kept off Claim 1 (description-level per the map). | n/a |
| S11 | §3: "...and designs the whole block, in the document's words, 'With the goal of matching HBM4's footprint' **[0034]**. That is a goal on the page, not a result on a bench: the filing reports no bandwidth, no cost, no yield to show the match was made." | q-0034-1 (verbatim match) | [0034] "With the goal of matching HBM4's footprint, each XBM memory die is architected..." | **SUPPORTED** — exact verbatim substring; "goal... not a result" matches invention-summary's own characterization ("states effects sparingly and mostly as design goals rather than measured results... gives no cost, yield, retention, bandwidth-vs-HBM4... number"). | n/a |

**Tally: 11/11 anchor instances SUPPORTED. 0 UNSUPPORTED. 0 MISREAD. 0 OVERREACHED-BEYOND-ANCHOR.**

(Round 1 counted 12 instances; the §3 compression [F1] cut one `[0034]`-anchored sentence —
"Four gutters are cut into every die, each carrying the data for a pair of sub-channels" — from
prose. That fact is preserved verbatim in the kept FIG. 1G caption's numerals, so no grounding
was lost, only a prose anchor instance.)

## B. Claim-scope verification (vs. Claim scope map, invention-summary.md lines 67-81)

Rule under test: **claim 1 requires only "backend"** (as part of "1T1C backend DRAM"); 8-high
is dependent claim 2/7; UCIe / "match HBM4 footprint" / capacities / clock rates are
description `[0034]`; BIST / redundancy / sub-channels+TSV-gutters are dependent claims 3/4/5.

| Essay statement | What it attributes to Claim 1 | Correct? |
|---|---|---|
| "Claim 1, as filed, then requires that each memory die in the stack carry a particular kind of cell" → quotes 1T1C backend DRAM only | Only the 1T1C-backend-DRAM cell type | **Correct.** |
| "Claim 1 says backend. It never says foundry, never says logic fab, never says without a DRAM fab." (§4) | Negative claim about Claim 1's text | **Correct** — verified directly against Claim 1 text (patent.md line 144): no occurrence of "foundry," "logic fab," or "DRAM fab." |
| "Claim 1 fixes a single word. It never names the channel material, never claims a logic-compatible process, never promises a yield." (§5) | Negative claim | **Correct** — matches the map ("The channel MATERIAL is never named"). |
| "The one thing claim 1 settles is that the memory cell is built in the back-end." (§6) | Only the backend-cell requirement | **Correct**, consistent with §2/§4/§5. |
| 8-high stack, TSV gutters, UCIe, base-die redundancy, "match HBM4's footprint," 0.5-5 GB (§3) | Attributed to "the filing," "Intel," "the document's words" — never "claim 1" | **Correct** — no dependent-claim/description feature is promoted into a Claim 1 requirement. |
| §4/§5 foundry-capability reading ("the leap is mine, not the document's"; "That is the property a logic-and-packaging line can carry without owning a DRAM front-end") | Explicitly labeled essay inference, not a claim or description assertion | **Correct** — matches the map's guard: "the logic-foundry / no-DRAM-fab / cost / yield / channel-material reading is EXTERNAL strategic inference, never attributed to claim or description." Note: this is the corrected form of the round-1 `adversarial-B F2` overreach ("...and a front-end fab cannot"), now narrowed to "without owning," removing the false incapability claim and its self-contradiction against §5's own "incumbents are already building 3D DRAM" sentence two lines later. |

**No instance found of a spec/dependent-claim feature being promoted into a Claim 1
requirement anywhere in `v3`.**

## C. External (non-patent) fact verification (vs. `fact-check-log.md`)

| Essay claim | Fact ID | Tier | Match |
|---|---|---|---|
| "Intel sold its NAND flash business to SK hynix in 2021 and wound down its Optane memory line the year after" (§1) | `intel-exited-memory` | tier-3 / trade-press-reported | **Matches.** |
| "Three companies make the world's HBM, and Intel sells none of it" (§1) | `hbm-supply-concentration` + `intel-exited-memory` | tier-3 | **Matches** (compound of two logged facts). |
| "The world's DRAM comes from just three makers" (§4) | `dram-three-player` | tier-2 / analyst-estimate | **Matches.** |
| "SK hynix alone holds around 60% of the market, with Samsung and Micron dividing most of the rest" [HBM] (§4) | `hbm-supply-concentration` + `hbm-share-crosscheck` | tier-3 | **Matches** — correctly scoped to the HBM clause, not the DRAM clause; "around 60%" is a conservative rounding of 61-62%. |
| "Intel and SoftBank are co-developing a stacked memory called ZAM, or HB3DM, aimed squarely at beating HBM" (§4) | `zam-hb3dm-specs` | tier-3 | **Matches.** |
| "ZAM's public signature is its diagonal Z-angle stacking" (§4) | `zam-hb3dm-specs` + fact-check-log's own "Connect, do not conflate" Notes guard ("public ZAM = diagonal 'Z-angle' + hybrid bonding") | tier-3 | **Matches** the guard's own wording; correctly kept separate from the patent's own (unstated) die-joining method. |
| "SK hynix, Samsung and Micron each run their own 3D-DRAM programs, SK hynix's aimed at around 2030" (§5) | `incumbent-3d-dram` | tier-3 | **Matches.** |
| "in imec's capacitor-less cell, two thin-film transistors replace the storage capacitor entirely, and even that remains a lab result" (§5) | `imec-2t0c-igzo` | tier-2 / bibliographic | **Matches** — 2T0C correctly contrasted with this patent's 1T1C. |
| "In ZAM, the partner reported to actually fabricate the DRAM is Powerchip, not Intel" (§5) | `zam-powerchip-fab` | tier-3 | **Matches**; correctly fenced with "reported to." |
| "Intel and SoftBank's ZAM, a hybrid-bonded cousin of this filing, is due to be presented at VLSI 2026 in June" (§6) | `zam-hb3dm-specs` (hybrid-bonded) + `zam-hb3dm-vlsi2026` (June VLSI 2026) | tier-3 | **Matches** — "hybrid-bonded" grammatically modifies ZAM/"cousin," not "this filing." |
| "ZAM is not established to use a back-end-transistor cell" (§6) | Absence-of-fact check against `zam-hb3dm-specs` (the only ZAM fact row: 9-layer, hybrid-bonded, ~13,700 TSVs/layer, ~171 mm², ~10 GB module, ~5.3 TB/s, 2-3x capacity, ~half power — no mention of a back-end/thin-film transistor cell) | — | **Confirmed true-as-stated** — this is a defensible negative claim (no logged fact asserts a back-end cell for ZAM), and it resolves round-1 `adversarial-B F3` exactly as recommended. |
| "The same technology family is aimed at commercialization around 2029" (§6) | `zam-timeline` | tier-3 | **Matches.** |
| All 9 Sources-list URLs (imec, Astute Group, Counterpoint, S&P Global, 3x Tom's Hardware, TrendForce, TechPowerUp) | cross-checked programmatically against fact-check-log URLs | — | **All match** (script-verified; zero essay URLs outside the fact-check-log set). |

**No unlogged, load-bearing external fact found.** One borderline item, disclosed for
transparency, consistent with round 1's own disclosure practice, **not counted as a fidelity
defect**:

- §6: "A back-end capacitor at HBM density and yield is precisely what no one has shipped." This
  is an evaluative synthesis of already-logged facts (imec = lab-stage 2T0C only;
  `incumbent-3d-dram` roadmaps are dated ~2029-2031, i.e., not yet shipped; ZAM's own cell type
  is not established as back-end per the row above) rather than a single sourced external fact
  in its own right. It is not contradicted by anything in the log. If the orchestrator wants
  zero ambiguity, this could be re-worded as an explicit "on the record above" callback rather
  than a freestanding universal claim — a label change, not a hedge, and not required.

## D. Verbatim quote verification (byte-for-byte, script-checked against `input/patent.md`)

| Essay quote | Patent source | Verbatim? |
|---|---|---|
| "Embodiments are directed to ultra high bandwidth memory (HBM) with backend transistors" | [0018] | **Yes**, exact (confirmed by direct substring match). |
| "Each memory die in the die stack includes one transistor one capacitor (1T1C) backend dynamic random access memory (DRAM)." | [0069] | **Yes**, exact, including terminal period. |
| "can be an approximately 1.5 GB die based on back-end-of-line transistors" | [0027] | **Yes**, exact substring. |
| "to have a die capacity of 0.5-5 GB" | [0034] | **Yes**, exact substring. |
| "With the goal of matching HBM4's footprint" | [0034] | **Yes**, exact substring. |

No other quotation-marked strings in the essay body are patent text (remainder are bibliography
article titles in Sources, correctly presented as such).

## E. Special focus 1 — §4 ZAM contrast rewrite (die-joining neutrality + no ZAM-property leak)

**New text (essay-final.md line 60):**
> "This is not a lone paper. The same direction is public: Intel and SoftBank are
> co-developing a stacked memory called ZAM, or HB3DM, aimed squarely at beating HBM. The link
> is real but partial. ZAM's public signature is its diagonal Z-angle stacking; what this
> filing turns on is the back-end transistor cell, organized by vertical TSV gutters. Same
> goal, different document, and no ground for calling them one chip."

**Old text (quoted in round-1 `adversarial-B` F1, now removed):** "ZAM stacks on a diagonal
Z-angle joined by hybrid bonding, which fuses two dies face to face without solder. This filing
uses vertical TSV gutters and UCIe instead." — the word "instead" asserted a false
mutual-exclusivity between hybrid bonding (a die-joining method) and TSV gutters/UCIe
(via-routing and I/O-protocol concepts on different axes), and, per F1, likely contradicted
`[0020]` ("both-sided high bandwidth interconnect (HBI) connections") and `[0023]`
("die stacking is achieved wafer-to-wafer"), both of which point toward a hybrid-bonding-class
die-joining method for this filing.

**Verification against `input/patent.md`:**
- `[0020]`: "...a stack of N memory dies containing 1T1C backend DRAM, through silicon via
  (TSV) gutters and **both-sided high bandwidth interconnect (HBI) connections**."
- `[0023]`: "...die stacking is achieved **wafer-to-wafer**. In another embodiment, die
  stacking is achieved die-to-die."
- `[0031]`: "...a first region 152 of **TSV/HBI connections**... a second region 154 of
  TSV/HBI connections."

The new §4 sentence contains no reference to "bond," "bonding," "solder," "wafer-to-wafer," or
"HBI" at all (confirmed by direct grep of the essay body — the only "hybrid-bonded" occurrence
in the whole essay is in §6, and it grammatically modifies "ZAM... a hybrid-bonded cousin," never
"this filing"). The sentence's two clauses are cleanly separated by subject:
1. "ZAM's public signature is its diagonal Z-angle stacking" — a ZAM-only property, traceable to
   `fact-check-log.md`'s own "Connect, do not conflate" Notes guard ("public ZAM = diagonal
   'Z-angle' + hybrid bonding").
2. "what this filing turns on is the back-end transistor cell, organized by vertical TSV
   gutters" — attributes to the patent only (a) the back-end cell (claim 1, `[0018]`/`[0069]`)
   and (b) TSV-gutter channel organization (`[0033]`/`[0034]`, dependent claim 5/10 territory,
   never called claim 1) — a data/channel-organization axis, not a die-joining/bonding axis.
   "Organized by vertical TSV gutters" is directly supported: `[0033]` "a basic memory building
   block 160 includes sub-channel 0 **161A**... TSV gutter 0 **162**..."; `[0034]` "There are
   four TSV gutters in each die, one carrying data and control for sub-channels 0-1...".

**Verdict: the sentence neither asserts nor denies the patent's own die-joining method** — it
simply does not address that axis, so there is no contradiction with `[0020]`'s HBI or
`[0023]`'s wafer-to-wafer stacking. **It does not attribute a ZAM property (Z-angle, hybrid
bonding, or any of ZAM's specific numeric specs — 9-layer, ~13,700 TSVs/layer, ~171 mm²,
~10 GB, ~5.3 TB/s, 2-3x capacity, ~half power — none of which appear anywhere in the essay) to
the patent, and does not attribute a patent property (backend transistor cell, TSV-gutter
channel organization) to ZAM.** The contrast rests exactly on the cell/architecture axis the
task described. **SUPPORTED — defensible, grounded, no new defect introduced.**

## F. Special focus 2 — §3 compression (retained claims still trace correctly)

Round-1 `adversarial-A F1` flagged §3's TSV-gutter/sub-channel plumbing as over-elaborated
("Four gutters are cut into every die, each carrying the data for a pair of sub-channels
`[0034]`" plus the FIG. 1G caption repeating the same tile). The fix compressed this to the
load-bearing idea and left the four-gutters granularity to the caption only.

Checked every claim retained after compression:
- "eight high and beyond" `[0023]` — present, verbatim-paraphrase, SUPPORTED (S5 above).
- "silicon thinned... many-layer stacking" `[0031]` — present, SUPPORTED (S6 above).
- "TSV gutters," "sub-channels" `[0073]` — present, SUPPORTED (S7 above, with note).
- "match HBM4's footprint" / "0.5-5 GB" `[0034]` — present, verbatim, SUPPORTED (S10/S11
  above).
- "eight-high" (dependent claim 2/7) — never promoted to claim 1 anywhere; consistent.
- The cut sentence's underlying fact (four TSV gutters, each pairing two sub-channels) is
  **not lost** — it survives verbatim-consistent in the kept FIG. 1G caption ("Eight
  sub-channels (161A to 161H) are divided by four vertical TSV gutters (162 to 165)"), which
  matches `[0033]`'s numerals exactly. Cutting the prose sentence removed detail, not accuracy;
  no misstatement was created by the compression.

**Verdict: SUPPORTED — the compression is a clean cut, not a fidelity regression.**

## G. Special focus 3 — §6 back-end-cell proof-point framing (vs. fact-check-log)

**Text (essay-final.md line 78):**
> "Intel and SoftBank's ZAM, a hybrid-bonded cousin of this filing, is due to be presented at
> VLSI 2026 in June. Its density, yield and cost per bit will show whether this class of tall,
> stacked challenger can beat HBM4. That tests the direction, not the differentiator: ZAM is
> not established to use a back-end-transistor cell, and the back-end cell at the center of
> this application has no public proof point yet. The same technology family is aimed at
> commercialization around 2029."

This is the fix for round-1 `adversarial-B F3` ("the named test... may not test the thing the
essay spent five sections on"). Checked against `fact-check-log.md`:
- `zam-hb3dm-specs`: ZAM/HB3DM is "hybrid-bonded" — matches "a hybrid-bonded cousin."
- `zam-powerchip-fab`: Powerchip, not Intel, fabricates ZAM's DRAM — consistent with (does not
  contradict) "ZAM is not established to use a back-end-transistor cell" (no fact-check-log row
  anywhere claims ZAM uses a back-end/thin-film-transistor cell; the ZAM fact row lists 9-layer,
  hybrid-bonded, TSV count, die area, module capacity/bandwidth, and power/capacity multiples —
  nothing about cell architecture).
- `zam-hb3dm-vlsi2026`: SAIMEMORY's HB3DM paper is scheduled for VLSI 2026 in June — matches "due
  to be presented at VLSI 2026 in June."
- `zam-timeline`: commercialization targeted ~2029 — matches "aimed at commercialization around
  2029."
- The claim "the back-end cell at the center of this application has no public proof point yet"
  is consistent with the invention-summary's own characterization (no cost/yield/retention/
  bandwidth-vs-HBM4/$-per-bit figure anywhere in the patent) and with the essay's own §3 close
  ("the filing reports no bandwidth, no cost, no yield to show the match was made").

**Verdict: factually consistent with fact-check-log on every point. SUPPORTED.** The
class/direction-vs-differentiator separation is exactly the fix `adversarial-B F3` called for,
and it introduces no new external claim beyond what is already logged.

## H. Supplementary — figure captions (no `[dddd]` anchor, spot-checked)

- **FIG. 1B caption** — unchanged from round 1; matches `[0025]`/`[0023]`/`[0034]`. No defect.
- **FIG. 1F caption** — unchanged from round 1; matches `[0031]` numerals. No defect.
- **FIG. 1G caption** ("...the repeating tile the filing sizes toward HBM4's footprint") —
  numerals match `[0033]` exactly; "the repeating tile the filing sizes toward HBM4's
  footprint" is a reasonable synthesis of `[0032]`-`[0034]` (building block 160 = the
  "datablock" unit the die is built from; `N` such units are sized "to have a die capacity of
  0.5-5 GB... with the goal of matching HBM4's footprint"). No defect.
- **FIG. 1A caption** (new gloss, `adversarial-A F4` fix: "...joined on a single interposer, the
  silicon bridge that wires the two dies together") — matches `[0022]` numerals (106, 104, 102);
  the added gloss is standard, accurate packaging terminology, not a patent-specific claim
  requiring its own anchor. No defect.

## Summary

| Category | SUPPORTED | UNSUPPORTED | MISREAD | OVERREACHED-BEYOND-ANCHOR |
|---|---|---|---|---|
| `[dddd]`-anchored sentences (11 instances) | 11 | 0 | 0 | 0 |
| Claim-scope statements (6 checked) | 6 correct | 0 | 0 | 0 |
| External facts (12 checked + 9 Sources URLs) | all traced | 0 unlogged (1 disclosed synthesis note, not a defect) | — | — |
| Verbatim quotes (5) | 5 exact | 0 | — | — |
| §4 die-joining / ZAM-property check | clean | 0 | 0 | 0 |
| §3 compression trace check | clean | 0 | 0 | 0 |
| §6 proof-point framing check | clean | 0 | 0 | 0 |

**All items SUPPORTED. No non-SUPPORTED findings to report. Double-clean grounding confirmed
across round 1 and round 2 (post-revision).**
