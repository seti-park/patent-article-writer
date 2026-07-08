# Phase 2 Handoff Notes

## (a) Audience reframe decision

Default reader-profile holds (curious retail investor, advanced-HS to early-undergrad), with the per-run note from `input/essay-context.md`: the reader may have seen "Intel memory comeback" or "HBM shortage" headlines but cannot define FEOL vs BEOL, a thin-film transistor, 1T1C DRAM, a TSV, a base die, or UCIe. Consequences:
- One-clause gloss on first use for: FEOL vs BEOL ("the front-end where transistors are normally built vs the back-end wiring layers on top"), thin-film transistor, 1T1C DRAM ("one transistor + one capacitor per bit"), TSV ("a vertical wire through the die"), base die, UCIe ("a chiplet-to-chiplet I/O standard"), hybrid bonding (only when contrasting ZAM). Gloss then move on — jargon-overdepth is the failure mode, not jargon.
- Establish the stakes briefly: the three-player DRAM oligopoly and the SK-hynix-led ~60% HBM concentration are WHY a fourth path matters. One or two sentences, not a market report.

## (b) Citation priority mapping

| Quotable span / anchor | Primary section | Role |
|---|---|---|
| `[0069]` (claim 1: "1T1C backend DRAM") | 2-the-move (re-cited in 5) | THE claims anchor; translate-then-quote per reader-profile rule 3; note the Example says "includes" where the claim says "comprises" (both verbatim-present); the load-bearing word is "backend" |
| `[0018]` (embodiments directed to HBM with backend transistors) | 2 | frames the move in the patent's own words |
| `[0020]` (stack of N dies of 1T1C backend DRAM + TSV gutters + HBI) | 2, then 3 | mechanism walk |
| `[0027]` ("approximately 1.5 GB die based on back-end-of-line transistors") | 2, then 3 | the "backend transistors → capacity" line; a DESCRIPTION number, never a claim pin |
| `[0031]` (thin film transistor databases 151/153) | 2 | what "backend" means, under fig-01F; DESCRIPTION, not claim 1 |
| `[0023]` ("8-high and beyond") | 3 | stack height; "and beyond" is description; the exact count "eight" is dependent claim 2 |
| `[0034]` ("match HBM4's footprint"; 0.5-5 GB; four TSV gutters; UCIe 32 GHz; base-die redundancy) | 3, one clause in 4 | the architecture; "match HBM4's footprint" is a stated GOAL, not a measured result. `[0034]` is dense — do NOT spend all of it in one paragraph |
| `[0019]` (single-die 1T1C state of the art) | 1 or 4 | problem framing / baseline the filing departs from |
| `[0073]` (claim 5: alternating sub-channels + TSV gutters) | 3 | dependent-claim anchor for the gutters (fig-01G) |
| `[0045]` (coreless architecture "extremely expensive") | 4 or 5, one use | packaging-cost color; do not stack packaging quotes |
| `[0053]` (reversed-overhang DRAM package) | optional, ≤ 1 clause | packaging variant; secondary theme |

External facts: cite by Fact ID from fact-check-log.md; ZAM / EMIB / market-share / incumbent-roadmap / imec content NEVER carries a `[dddd]` anchor (the patent contains none of it).

## (c) Framing trace (rejected candidates)

- Candidate 2 ("beat HBM4's footprint" stack-walk) rejected as spine: the patent gives NO HBM4 comparison number, so a "beats HBM4" frame would ride external ZAM figures and conflate this filing with ZAM/HB3DM. It survives ONLY as §3 mechanism (the stack + "match HBM4's footprint" goal). Phase 2 must NOT re-center the essay on a spec-by-spec HBM4 duel or import ZAM's bandwidth as this patent's.
- Candidate 3 ("Intel's memory comeback") rejected: 0/4 patent grounding and a direct guard violation (a pending application is not productization; Intel exited memory; even ZAM has Powerchip fabbing the DRAM). The comeback/ZAM material lives ONLY as the §1 hook's narrative-friction setup and the §5/close guard — never as the spine, never as "Intel is back in the memory business" stated as fact.

## (d) Traps to avoid

**Claim-scope traps (restating the Claim scope map — sought / open / pinned vocabulary):**
- PENDING APPLICATION: every "locks" is a SOUGHT lock. DO say "the claim as filed requires", "Intel is claiming", "the application seeks". DON'T say "Intel owns / has secured / has locked". No granted claim exists.
- Claim 1 (the spine claim): DO say claim 1 requires "1T1C **backend** DRAM" — "backend" is claim text and is the whole hinge of the thesis. DON'T attribute to claim 1: "thin film transistor" or "back-end-of-line" (DESCRIPTION `[0031]`, `[0027]`), 8-high (dependent claim 2), BIST (claim 3), redundancy (claim 4), sub-channels + TSV gutters (claim 5), UCIe / HBI / "match HBM4's footprint" / capacities / 2 GHz / 32 GHz (DESCRIPTION `[0020]`, `[0034]`). Narrate each as the description's or the dependent claim's, on its own anchor.
- Channel MATERIAL: the patent NEVER names it — no "oxide", "IGZO", or "amorphous". DON'T call this an "oxide-channel" or "IGZO" DRAM. imec's IGZO is EXTERNAL contrast only (fact-check-log `imec-2t0c-igzo`).
- 1T1C is NOT capacitor-less: DO say the capacitor is RELOCATED to the back-end. DON'T write "capacitor-less", "no capacitor", or imply the hard part is removed. The capacitor-less path is 2T0C (imec, external) — the one this 1T1C filing did NOT take.
- Pins: there are NO claim pins. "approximately 1.5 GB die" and "about 9.5 mm" are DESCRIPTION approximate points (`[0027]`), not claim limitations and not floors/ceilings. DON'T present them as claim requirements or as bounds the claim imposes.
- The strategic reframe (logic-foundry / no-DRAM-fab / "memory as a foundry capability" / cost / $-per-bit / yield): EXTERNAL inference. DO label it clearly as the essay's synthesis of the claim word "backend" plus external context. DON'T attribute any of it to the patent text. The patent's own words are "backend transistors", "1T1C backend DRAM", "back-end-of-line transistors", "thin film transistor".

**Attention-budget trap (MOTIF budget, not sentence budget):**
- Prosecution / status / finance is priced in exactly ONE section: §5-the-measured-read (payload: pricing). Elsewhere: at most one status clause inside the lead's two-sided call, plus the closing recap. The MOTIF counts paraphrase echoes: "pending application", "one filing", "still just paper", "not a roadmap", "Intel exited memory", "Powerchip-not-Intel fabs it", "defensive filing" ALL draw on the SAME allowance. If §5 says "one pending filing", the close's guard must not repeat that phrasing family again — the total across the §1 lead clause + §5 + the §6 recap is the whole budget.
- Generic-truism ban: "a patent doesn't guarantee a product / a stock move" appears at most ONCE, as the single anti-hype guard inside the close — never as the steelman, never as a recurring hedge. The steelman is the THIS-patent objection (backend ≠ logic-foundry; capacitor relocated not removed; incumbents already on 3D DRAM; no numbers).

**Measured-posture trap (do not let measured decay into safe-harbor):**
- `closing_posture: measured` — copy it into the draft frontmatter. `gate_hedge` hard-fails boilerplate/qualifier-led verdicts only under `firm`; under `measured` they WARN. That is NOT permission to hedge. The owner rule (essay-context) requires the verdict to COMMIT to a direction (the backend-DRAM move is real and, if it works, consequential) while reserving timing/economics to the falsifiable proof points (VLSI 2026 density/yield/$-per-bit; ~2029-2030). A decayed "only time will tell / a patent isn't a product" close is a defect here even though it would only warn. Pass-6 6G binds. The anti-hype guard must be patent-specific (see the close directive in thesis-spine.md).

**Other traps:**
- The patent NEVER says "EMIB", "ZAM", "Z-angle", "foundry", "logic fab", "hybrid bonding", "cost", "yield", or "$/bit". NEVER write "this patent is ZAM" or "this is EMIB-T's memory". Permitted posture: same DIRECTION (tall custom 3D DRAM to beat HBM4; base die + high-speed I/O), different headline interconnect — this filing = vertical TSV gutters + UCIe; public ZAM = diagonal "Z-angle" + hybrid bonding (fact-check-log `zam-hb3dm-specs`). Same-family cousin, not confirmed identical.
- Patent-side vs news-side numbers must be labeled: "0.5-5 GB per die" is the patent (`[0034]`); ZAM's "~10 GB module / ~5.3 TB/s / 13,700 TSV" are external (fact-check-log). The patent gives NO bandwidth, capacity-vs-HBM4, cost, yield, or retention figure — do not borrow ZAM's to fill the gap.
- `intel-foundry-hbm-basedie` (Intel Foundry base-die roadmap) was NOT re-verified this run (search unavailable). Use as ≤ 1 clause of color, or drop; do not make it load-bearing.
- Claim quoting mechanics: the numbered claims carry no `[dddd]` anchors; quote via the Example-embodiment paragraphs (claim 1 ↔ `[0069]`, claim 5 ↔ `[0073]`, claim 6 ↔ `[0074]`). Examples say "includes", claims say "comprises" — both are verbatim-present; keep verbatim quotes verbatim and gloss outside them.
- Em dash banned in essay body (deliverable voice); patent verbatim quotes keep their original characters. The reader_sentence in title-lead-candidates.md carries the owner's em-dash as a design target only — render the on-page signature line em-dash-free.
- "Backend" gloss: the patent's words are "backend" (claim), "back-end-of-line" and "thin film transistor" (description). Gloss "back-end" once ("the wiring layers built on top of the transistors, at low temperature"); keep the verbatim quotes exact.

## (e) Open questions for Phase 2 (awaiting orchestrator / owner)

- Register: recommended `discovery`; `tension` is the declared fallback (title-lead-candidates.md). Orchestrator/owner to confirm the pair at compose; surface, do not decide silently.
- Cover: FIG. 1B recommended; FIG. 1A (thesis co-package) and FIG. 1F (backend transistors) are the surfaced alternates (figure-selection.md §Cover candidate). Confirm at compose.
- reader_sentence is owner-set (essay-context); confirm the em-dash-free on-page rendering of the signature line.
- Whether §4-who-can-make-it reuses fig-01A (co-package) or leaves it to §2 only. Default: fig-01A anchors §2; §4 is prose + stakes (may reuse fig-01A if the section runs visual-thin).
- `intel-foundry-hbm-basedie`: include as one clause of color in §4, or drop (not re-verified). Default: drop unless the orchestrator re-verifies.
- Signature lines: the composer declares up to 3 in thesis-trace.md; the reader_sentence ("moves the DRAM cell into back-end layers → who can make HBM stops being a three-company club") is the natural first one.
