# Self-Audit Round 2 — Adversarial Reader B

- **Persona**: skeptical domain expert (memory / semiconductor)
- **Target**: `handoff/03-edit/essay-final.md` (draft_version 3, closing_posture: measured)
- **Method**: evidence-forced; every verdict carries a quoted span or ABSENT. Blind to other round-2 readers.
- **Section map**: §1 "A Memory Architecture From the Company That Left It" · §2 "Claim 1 Turns on a Single Word: Backend" · §3 "A Tower Built to Match HBM4's Footprint" · §4 "A Back-End Cell Could Loosen the DRAM-Fab Bottleneck" · §5 "Read Cold, It Is One Filing That Keeps the Capacitor" · §6 "The Direction Is Real; the Numbers Are the Test"

---

## Part 1 — Did the three round-1 fixes land?

### FIX 1 (§4) — false "TSV gutters + UCIe instead of hybrid bonding" dichotomy GONE; ZAM contrast now on the cell/architecture axis; no bonding claim that contradicts `[0020]` / `[0023]`
**VERDICT: YES.**

Current §4 contrast span (line 60):
> "ZAM's public signature is its diagonal Z-angle stacking; what this filing turns on is the back-end transistor cell, organized by vertical TSV gutters. Same goal, different document, and no ground for calling them one chip."

- The axis is now **cell/geometry** (back-end transistor cell + vertical stacking) vs ZAM's **Z-angle** stacking. Both descriptors are accurate: the patent's dies are vertically aligned (`[0025]` aligned databases, vertical TSVs `[0033]`); "vertical TSV gutters" is `[0033]`.
- Grep for `instead` / `hybrid` in the body: the only `hybrid` hit is §6 "hybrid-bonded cousin" (a descriptor of ZAM, external fact); no "instead of hybrid bonding" phrasing survives. The essay makes **no** claim about the filing's own bonding method, so nothing contradicts `[0020]` "both-sided high bandwidth interconnect (HBI) connections" or `[0023]` "die stacking is achieved wafer-to-wafer." §6 "hybrid-bonded cousin of this filing" describes ZAM only and leaves the filing's bonding unstated — consistent with the patent's HBI, not a contrast. LANDED.

### FIX 2 (§5) — "a front-end fab cannot" GONE; affirmative core = HBM-class memory "without owning a DRAM front-end"; no self-contradiction with the incumbents-3D-DRAM sentence
**VERDICT: YES.**

Current §5 affirmative-core span (line 68):
> "The cell is backend. That is the property a logic-and-packaging line can carry without owning a DRAM front-end, which makes the open question the numbers, not the direction. The incumbents being on the 3D-DRAM road is not a rebuttal. It confirms the road is real, and this filing sketches a different lane onto it."

- Grep for `cannot`: two hits, both benign — §3 "a part that cannot be reworked after stacking" and (line 78, matched on `hybrid`). No "front-end fab cannot" / "foundry cannot" anywhere. ABSENT as required.
- The affirmative core is now the possibility framing ("a logic-and-packaging line can carry [it] without owning a DRAM front-end"), which is grounded in the patent's own claim word "backend DRAM" (`[0069]`), and is consistent with §4's "could in principle carry an HBM-class memory through its own line." No contradiction with "SK hynix, Samsung and Micron each run their own 3D-DRAM programs" — the essay reframes incumbent presence as validation of the road, not exclusion of front-end makers. LANDED.

### FIX 3 (§6) — VLSI 2026 / ZAM readout labeled a class/direction test; back-end-cell differentiator stated to have no public proof point yet
**VERDICT: YES.**

Current §6 span (line 78):
> "Its density, yield and cost per bit will show whether this class of tall, stacked challenger can beat HBM4. That tests the direction, not the differentiator: ZAM is not established to use a back-end-transistor cell, and the back-end cell at the center of this application has no public proof point yet."

- Explicitly labeled a **class** test ("this class of tall, stacked challenger") and a **direction, not differentiator** test.
- Connect-don't-conflate honored: "ZAM is not established to use a back-end-transistor cell."
- Differentiator proof-point gap stated outright: "the back-end cell ... has no public proof point yet." LANDED.

---

## Part 2 — Guard hunt (each → verdict + evidence)

| Guard | Verdict | Evidence |
|---|---|---|
| ZAM conflation | CLEAN | §4 "The link is real but partial ... Same goal, different document, and no ground for calling them one chip"; §6 "ZAM is not established to use a back-end-transistor cell." |
| 1T1C ≠ capacitor-less | CLEAN | §2 "This is still a one-capacitor cell. The back-end move relocates DRAM's hardest part. It does not remove it."; §5 correctly assigns capacitor-less to imec ("two thin-film transistors replace the storage capacitor entirely"); §6 "the capacitor was relocated ... rather than removed." Matches `imec-2t0c-igzo` (2T0C) vs this filing's 1T1C `[0069]`. |
| Channel material not imported | CLEAN | §5 "It never names the channel material" — no IGZO/oxide/amorphous imported to this filing. Matches Claim scope map ("channel MATERIAL is never named"). |
| "beats HBM4" number not on the patent | CLEAN | Patent framing kept to "match HBM4's footprint" (`[0034]`, quoted §3); §3 disclaims ("the filing reports no bandwidth, no cost, no yield"); "beat HBM4" attributed only to ZAM/future test (§4, §6) and to news in Sources. |
| Productization not asserted | CLEAN | §1 "This is one published application, not a product"; §5 "not a granted patent and not a product"; §6 verdict stays conditional ("If a back-end die matches HBM4 ..."). |
| Over-hedge (6G) symmetric — §6 | CLEAN (proportionate) | See Part 4. |

---

## Part 3 — Grounding spot-checks

**Anchors verified verbatim / paragraph-supported (§2, §3):**
- `[0018]` §2 "Embodiments are directed to ultra high bandwidth memory (HBM) with backend transistors" — verbatim in `[0018]`. ✓
- `[0069]` §2 block quote "Each memory die in the die stack includes one transistor one capacitor (1T1C) backend dynamic random access memory (DRAM)." — verbatim in `[0069]`. ✓
- `[0027]` §2 "can be an approximately 1.5 GB die based on back-end-of-line transistors" — verbatim in `[0027]`; presented as description ("can be"), not a claim pin. ✓
- `[0031]` §2 thin-film-transistor layers stacked — `[0031]` "first thin film transistor database 151 ... second thin film transistor database 153." ✓
- `[0023]` §3 "memory cube stacked eight high and beyond" — `[0023]` "die stacking cube is 8-high and beyond" (paraphrase, unquoted). ✓
- `[0031]` §3 "silicon thinned to enable that many-layer stacking" — `[0031]` "thinning of the silicon can be implemented to enable many-layer stacking." ✓
- `[0073]` §3 sub-channels — `[0073]` "plurality of alternating sub-channels and through-silicon via (TSV) gutters." ✓
- `[0020]` §3 UCIe base-die link — `[0020]` "high speed universal chiplet interconnect express (UCIe) connections." ✓
- `[0034]` §3 "to have a die capacity of 0.5-5 GB" and "With the goal of matching HBM4's footprint" — both verbatim in `[0034]`. ✓
- FIG 1G caption "Eight sub-channels (161A to 161H) ... four vertical TSV gutters (162 to 165)" — `[0033]`. ✓

**Claim-scope / Claim scope map honored:** §2 "Claim 1, as filed, then requires..."; §4 "Claim 1 says backend. It never says foundry, never says logic fab, never says without a DRAM fab ... the leap is mine, not the document's"; §5 "Claim 1 fixes a single word." All consistent with the map's sought-locked "backend" + external-inference fencing. **Pins not described as bounds:** "eight high" tracked to `[0023]` "8-high and beyond" (never asserted as a claim-1 requirement); "0.5-5 GB" and "~1.5 GB" presented as description/design targets, not claim pins. ✓

**External facts vs fact-check-log:** SK hynix "around 60%" (log: ~61-62%, safe rounding); Optane wind-down 2022; NAND sale to SK hynix 2021; imec 2T0C; incumbent 3D DRAM ~2030; ZAM Powerchip fab; ZAM VLSI 2026 June; ~2029 commercialization — all match. ✓

---

## Part 4 — Over-hedge (6G) symmetric check on §6

**§6 is evidence-proportionate — neither overreach nor over-hedge. VERDICT: YES.**

- **Leads with the direction-commitment:** line 74 "The direction is not in doubt. The one thing claim 1 settles is that the memory cell is built in the back-end."
- **Prices uncertainty with patent-specific guards, not boilerplate:** the capacitor ceiling (line 76 "this is 1T1C ... A back-end capacitor at HBM density and yield is precisely what no one has shipped") and the this-cell proof-point gap (line 78 "no public proof point yet") are both THIS-patent-specific. No "a patent guarantees nothing" boilerplate.
- **Closes firm:** line 82 "The cell is in the back-end. Whether that becomes a fourth path to HBM is now a question of yield, not of architecture."
- The fix-3 addition ("no public proof point yet") is a **precision/calibration** clause (it tells the investor exactly what the June readout will and will not settle), not a safe-harbor hedge. It does **not** tip the verdict into over-hedge.

---

## Part 5 — NEW finding introduced by the round-1 edits

### SELFAUDIT-R2-B-01 — "direction" overloaded in the verdict (coherence)
- **Check**: verdict coherence / pass-7 header-as-claim (term collision on the section's headline word)
- **Verdict**: FAIL (new medium issue introduced by fix-3)
- **Severity**: **medium**
- **Origin**: introduced by the fix-3 clause "That tests the direction, not the differentiator."

**Evidence.** Fix-3 added a clause that reuses "direction" in a sense that collides with the section's opening (and its header):
- Header + line 74 (settled sense): **"The Direction Is Real; the Numbers Are the Test"** / **"The direction is not in doubt. The one thing claim 1 settles is that the memory cell is built in the back-end."** Here direction = the settled architectural fact, explicitly opposed to "the Numbers / the Test," and echoed by the close "a question of yield, **not of architecture**."
- Line 78 (being-tested sense): **"Its density, yield and cost per bit will show whether this class ... can beat HBM4. That tests the direction, not the differentiator ..."** Here the numbers TEST "the direction," and "direction" = the tall-stacked-challenger class (the differentiator being this filing's back-end cell).

So within §6, four lines apart, "direction" is asserted to be (a) settled/"not in doubt" and separate from the test, then (b) the thing the numbers test. If it is one referent, lines 74 and 78 contradict (settled vs under test); if two referents, the section's headline word silently flips meaning. Either way the verdict's central distinction — what claim 1 *settles* vs what the June readout *tests* — is momentarily self-contradictory in the highest-stakes section, and it collapses the header's clean direction-vs-numbers split. (The word also oscillates across the essay: §4 line 60 "The same direction is public" = class sense; §5 line 68 "not the direction" = settled sense.)

**Fix (jurisdiction-compliant: label/clarity, not a hedge).** Disambiguate the fix-3 clause — reserve "direction" for the settled architectural read and name the tested thing separately, e.g., "That tests **the class, not this filing's cell**" (or "the approach, not the differentiator"). No hedge, no gate relaxed, verdict substance unchanged.

---

## Summary
- Round-1 fixes landed: **§4 YES · §5 YES · §6 YES**.
- NEW medium+ findings: **1** — SELFAUDIT-R2-B-01 (medium, "direction" term-collision in §6, introduced by fix-3).
- §6 evidence-proportionate (neither overreach nor over-hedge): **YES**.
