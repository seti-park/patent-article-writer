# Self-Audit Round 3 — Adversarial Reader B (Dryness Confirmation)

- **persona**: skeptical domain expert (memory / semiconductor), fresh eyes, blind to prior rounds
- **target**: `handoff/03-edit/essay-final.md` (draft_version 4)
- **grounding sources consulted**: `handoff/01-design/invention-summary.md`, `handoff/01-design/fact-check-log.md`, `handoff/01-design/thesis-spine.md`, `handoff/02-compose/thesis-trace.md`, `input/patent.md`
- **mandate**: confirm the two prior-round targets resolved; run a full fresh medium+ sweep (7 passes + owner guard-list); every verdict carries a quoted span or ABSENT.

---

## Targeted confirmations

### 1. §6 "direction" collision resolved — YES

The settled-commitment sense and the thing-being-tested sense are now **different words** inside §6.

- Settled-commitment sense uses "direction":
  - header: `"The Direction Is Real; the Numbers Are the Test"`
  - body: `"The direction is not in doubt. The one thing claim 1 settles is that the memory cell is built in the back-end."`
- Thing-being-tested is now "the class", differentiated from "this filing's cell":
  - `"Its density, yield and cost per bit will show whether this class of tall, stacked challenger can beat HBM4. That tests the class, not this filing's cell: ZAM is not established to use a back-end-transistor cell, and the back-end cell itself has no public proof point yet."`

Within §6, "direction" is used **only** in the settled sense; the tested object is "the class"; the differentiator is "this filing's cell". No residual same-word/two-referents trip. (Minor cross-section note, NOT a finding: §4 uses "the same direction is public" for the shared stacked-challenger push and §6 narrows "direction" to the back-end cell — both remain in the settled/commitment family, never the test-target family, and §6 self-resolves in the next clause: `"The one thing claim 1 settles is that the memory cell is built in the back-end."`) **Verdict: resolved.**

### 2. ZAM caveat no longer over-repeats — YES

The ZAM-is-not-this-filing distinction appears **twice** (§4 + §6), not 3-4×:

- §4 (full form): `"ZAM's public signature is its diagonal Z-angle stacking; what this filing turns on is the back-end transistor cell, organized by vertical TSV gutters. Same goal, different document, and no ground for calling them one chip."`
- §6 (recap form): `"ZAM is not established to use a back-end-transistor cell, and the back-end cell itself has no public proof point yet."`

The third ZAM mention, §5 `"In ZAM, the partner reported to actually fabricate the DRAM is Powerchip, not Intel."`, is the **Powerchip-fabs-not-Intel** design-capability tell — a distinct point, not the conflation guard. So the conflation guard is spent 2×, matching the sanctioned budget (`thesis-spine.md` §Spine→section trace: connect-not-conflate lives in §4; recap in §6).

No conflation was reintroduced:
- The filing's own bonding method stays **unstated** — the essay's stack description is `"a memory cube stacked eight high and beyond [0023], with the silicon thinned to enable that many-layer stacking [0031]"`; it never imports "hybrid bonding" (ZAM's property) and never states wafer-to-wafer/die-to-die.
- No ZAM property (bandwidth, layers, TSV count, die area, module capacity, power, "half the power") is attributed to the patent — none of those specs appear in the essay at all.
- "diagonal Z-angle stacking" and "aimed squarely at beating HBM" are attributed to ZAM (external), never to the filing.

**Verdict: no over-repeat; no conflation reintroduced.**

---

## Grounding spot-checks

### Anchor verification (every `[dddd]` in the essay vs `input/patent.md`)

All patent-anchored beats live in §2 and §3 (the analysis/verdict sections §4–§6 carry no patent anchors by design — external inference, labeled). Every anchor checked:

| Anchor | Essay use | patent.md | Verdict |
|---|---|---|---|
| `[0018]` | "Embodiments are directed to ultra high bandwidth memory (HBM) with backend transistors" | [0018] verbatim identical | PASS (verbatim) |
| `[0069]` | block quote "Each memory die in the die stack includes one transistor one capacitor (1T1C) backend dynamic random access memory (DRAM)." | [0069] verbatim identical | PASS (verbatim, hard-gate) |
| `[0031]` | "thin-film-transistor layers stacked one atop another" | [0031] "a first thin film transistor database 151 … a second thin film transistor database 153" | PASS |
| `[0027]` | "can be an approximately 1.5 GB die based on back-end-of-line transistors" | [0027] verbatim fragment present | PASS (verbatim) |
| `[0023]` | "a memory cube stacked eight high and beyond" | [0023] "a die stacking cube is 8-high and beyond" | PASS (paraphrase faithful) |
| `[0031]` | "the silicon thinned to enable that many-layer stacking" | [0031] "thinning of the silicon can be implemented to enable many-layer stacking" | PASS |
| `[0073]` | "split the traffic into many independent sub-channels … [0073]" | [0073] "a plurality of alternating sub-channels and through-silicon via (TSV) gutters" | PASS (sub-channel/gutter anchor; "independent" glossed from [0034], "bandwidth" is general gloss — within tolerance) |
| `[0020]` | "over UCIe … an industry standard for wiring one chiplet to another [0020]" | [0020] "high speed universal chiplet interconnect express (UCIe) connections … to funnel out the data" | PASS |
| `[0034]` | "spare memory arrays that can stand in for defective ones once the stack is bonded" | [0034] "4 die-sub-channels of redundant memory arrays (32 datablocks) to act as fungible recoverability resources for unrepairable defects" | PASS |
| `[0034]` | "to have a die capacity of 0.5-5 GB" | [0034] verbatim | PASS (verbatim) |
| `[0034]` | "With the goal of matching HBM4's footprint" | [0034] verbatim | PASS (verbatim) |

No mis-anchor, no hallucinated paragraph. 3+ sections spot-checked (§2, §3 exhaustively; §4–§6 confirmed anchor-free by design).

### Claim-scope statements vs claims + Claim scope map

- `"Claim 1, as filed, then requires that each memory die in the stack carry a particular kind of cell."` — sought-locked vocabulary ("as filed", "requires"); matches map (claim 1 sought-locks 1T1C backend DRAM). PASS.
- `"The load-bearing word is backend."` — matches map ("The single load-bearing claim word … is 'backend'"). PASS.
- `"Claim 1 says backend. It never says foundry, never says logic fab, never says without a DRAM fab."` — matches map ("never says 'logic fab,' 'foundry,' or 'without a DRAM fab'"). PASS.
- `"It never names the channel material, never claims a logic-compatible process, never promises a yield."` — matches map ("channel MATERIAL is never named"). PASS.
- Thin-film-transistor attributed to `"The filing's description spells this out … [0031]"` — correctly description-level, not claim 1. PASS (map: "'thin film transistor' … is DESCRIPTION phrasing … not claim 1 words").
- `"not a granted patent"` (§5) — pending status honored; no "owns/secured". PASS.
- `"The one thing claim 1 settles is that the memory cell is built in the back-end."` — "settles" reads as the claim TEXT's determinate content (contrasted with open numbers), not legal grant; §5's "not a granted patent" removes any grant implication. Not a scope overreach. PASS.

### Pinned values not described as bounds

- "approximately 1.5 GB die" — presented as description size ("puts a size on one such die"), not a claim pin, not a bound. PASS.
- "0.5-5 GB" — quoted as a design capacity target from [0034], not a claim lock. PASS.
- "eight high" / "eight high and beyond" — attributed to "The application says" (description [0023]), never to claim 1; matches map (eight is claim-2 dependent count, not claim-1 requirement). PASS.

---

## Full fresh medium+ sweep (7 passes)

| Pass | Check | Verdict | Evidence | Severity |
|---|---|---|---|---|
| 1 | Hook / lead energy | PASS | ¶1 declarative, invention-first: `"Intel's newest memory filing does something quietly radical. It builds the transistor inside each DRAM cell in the chip's back-end wiring layers"`; two-sided call lands by lead end: `"if the yield numbers land, who can make HBM stops being a three-company club."` No deferred question, no verdict-insurance fact ahead of the beat. | none |
| 2 | Header-as-claim | PASS | All six `##` headers are assertions; header-only skim reconstructs the argument (company-that-left-it → one word backend → tower matches HBM4 → back-end cell could loosen bottleneck → one filing keeps the capacitor → direction real, numbers are the test). | none |
| 3 | Steelman present + not overweight | PASS | THIS-patent steelman, not a truism: `"It never names the channel material, never claims a logic-compatible process, never promises a yield."` + imec 2T0C contrast + `"three funded roadmaps, could read as noise."` Conceded at full strength (`"the bear case is strong, and it should be put at full strength"`), then refined: `"none of it touches the one thing the claim does settle. The cell is backend."` Bear case = 2 ¶, rebuttal = 2 ¶ (affirmative ≥ concession). imec counter bounded (`"even that remains a lab result"`). Not overweight. | none |
| 4 | No meta posturing | PASS | Only scope-fence lines, which are exempt: `"Here the filing's own words stop, and the reading begins."` / `"the leap is mine, not the document's."` No reader-instruction ("consider that…"). | none |
| 5 | Jargon as signpost | PASS | Every term-of-art glossed short and moved on: 1T1C `"one transistor to select a bit, one capacitor to hold it"`; thin-film transistor `"a device deposited as a thin coating in the wiring"`; TSV `"columns of through-silicon vias punched straight through each die"`; UCIe glossed; sub-channels `"the parallel data lanes"`; interposer `"the silicon bridge"`. No deep-dive past the insight. HBI never surfaced un-glossed (caption says "vertical interconnect"). | none |
| 6 | No stub / rhythm break | PASS | §1 (3¶), §2 (intro+quote+3¶), §3 (4¶+captions), §4 (4¶+caption), §5 (4¶), §6 (5 short ¶). No section markedly shorter than siblings. | none |
| 7 | Thesis not over-restated | PASS | Core "cell is backend" asserted in §4/§5/§6 = 3 sections (at limit, ≤3); the two declared signature lines (§1, §6) are count-exempt per `thesis-trace.md`; each assertion does distinct work (reframe / steelman-survival / verdict). Capacitor caveat distribution (§2 bold anchor / §5 imec concession / §6 single anti-hype guard) is design-sanctioned per `thesis-spine.md`, each a distinct role — not re-spend. | none |

---

## Owner guard-list sweep

| Guard | Verdict | Evidence | Severity |
|---|---|---|---|
| ZAM conflation | CLEAN | Distinction held 2× (§4/§6); `"no ground for calling them one chip"`, `"ZAM is not established to use a back-end-transistor cell"`. No ZAM spec attributed to patent; bonding method unstated. | none |
| 1T1C not capacitor-less | CLEAN | `"This is still a one-capacitor cell."` (§2) / `"this is 1T1C, so the capacitor was relocated into the back-end rather than removed"` (§6). imec 2T0C kept explicitly separate: `"The more radical path deletes the capacitor; in imec's capacitor-less cell, two thin-film transistors replace the storage capacitor entirely"`. | none |
| Channel material not imported | CLEAN | `"It never names the channel material"`; no IGZO/oxide attributed to the filing anywhere. | none |
| "beats HBM4" not attributed to this filing | CLEAN | `"aimed squarely at beating HBM"` is ZAM (external); `"will show whether this class of tall, stacked challenger can beat HBM4"` is framed as an unproven future test of "the class", not a filing claim. | none |
| Productization not asserted | CLEAN | `"This is one published application, not a product."` (§1) / `"not a granted patent and not a product."` (§5). | none |
| Over-hedge symmetric with overreach | CLEAN | Firm on the settled point: `"The direction is not in doubt."`; conditional (not overreaching) on the speculative point: `"If a back-end die matches HBM4 on capacity and yield at a workable cost, a foundry can quote HBM-class memory as a line item."` No safe-harbor boilerplate in the verdict; the one anti-hype guard is patent-specific (`"A back-end capacitor at HBM density and yield is precisely what no one has shipped."`). Status-motif budget respected (§1 lead + §5 pricing + §6 recap). | none |
| Verdict evidence-proportionate | CLEAN | Commits only to what claim 1 settles (backend, grounded [0069]); reserves timing/economics to falsifiable proof points (VLSI 2026, ~2029). Matches `measured` posture in frontmatter and `thesis-spine.md` recorded owner reason. | none |
| Figure coverage | CLEAN | 4 role-bearing figures used (FIG. 1B cover/stack, FIG. 1F back-end cell, FIG. 1G building block, FIG. 1A co-package); all caption numerals verified against patent (111/114/115; 151/153/152/154; 161A–H/162–165; 106/104). | none |
| Grounding plausibility (external facts) | CLEAN | ~60% SK hynix HBM (`hbm-supply-concentration`), three-maker DRAM (`dram-three-player`), Intel NAND→SK hynix 2021 + Optane wind-down 2022 (`intel-exited-memory`), Powerchip-fabs-ZAM (`zam-powerchip-fab`), VLSI 2026 June (`zam-hb3dm-vlsi2026`), ~2029 commercialization (`zam-timeline`), imec 2T0C lab-stage (`imec-2t0c-igzo`), incumbents ~2030 (`incumbent-3d-dram`) — all match fact-check-log. Patent-side vs news-side numbers kept separate; patent's no-number status stated (`"the filing reports no bandwidth, no cost, no yield"`). | none |

---

## Domain-expert adversarial probes (memory/semiconductor) — all cleared

- "the low-temperature metal stacked on top" for BEOL — acceptable retail simplification, not a fidelity error.
- backend → thin-film-transistor logic — attributed to description [0031], not claim 1; consistent with map. No over-claim.
- "only a dedicated DRAM fab runs [the crystalline-silicon DRAM front-end]" — fenced as inference (`"the leap is mine"`) and hedged (`"could in principle"`); bounded by §5/§6 (capacitor is the unshipped hard part). No unqualified overreach.
- "density, yield and cost per bit will show whether…" — framed as the figures-to-watch for the investor, not a claim that the VLSI paper discloses exact cost-per-bit; patent's $-per-bit absence correctly located as external/future. No finding.

---

## Verdict

- **Confirmation 1 (§6 direction collision):** YES — resolved.
- **Confirmation 2 (ZAM over-repeat + no re-conflation):** YES — 2× only; no conflation reintroduced; bonding method unstated.
- **Medium+ findings this round:** **NONE.**
- **§6 evidence-proportionality:** evidence-proportionate — commits firmly to the one settled fact (the cell is backend, grounded in claim 1 / [0069]) and reserves the numbers to named falsifiable proof points; neither overreach nor over-hedge under the `measured` posture.

**Finding count by severity — critical 0, high 0, medium 0, low 0. Self-audit is dry.**
