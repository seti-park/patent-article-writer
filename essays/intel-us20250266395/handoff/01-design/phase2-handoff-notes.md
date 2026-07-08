# Phase 2 Handoff Notes

## (a) Audience reframe decision

Default reader-profile holds (curious retail investor), with the per-run note from `input/essay-context.md`: the reader has likely SEEN EMIB-T headlines but cannot define a bridge die, TSV, or hybrid bonding. Consequences:
- One-clause gloss on first use for: bridge die, TSV/TGV, hybrid bonding, substrate/cavity, known-good test. Gloss then move on (jargon-overdepth is the failure mode, not jargon).
- The EMIB-T hook needs no explanation of EMIB-T's internals beyond "power comes up through vias in the bridge from the package bottom" — one clause, fact-check-log anchored.

## (b) Citation priority mapping

| Quotable span / anchor | Primary section | Role |
|---|---|---|
| `[0142]` (method: attach bridge → create MD assembly; test → attach substrate when passes) | 2-flip-the-flow, re-cited in 5 | THE claims anchor; quote the two halves as separate spans (q-0142-1, q-0142-2); translate-then-quote per reader-profile rule 3 |
| `[0061]` / `[0062]` (steps 1108/1110/1112) | 2 and 3 | narrative walk of the flow; `[0062]` is the test-gate payoff — do NOT spend it in the lead |
| `[0030]` (FIG. 1 assembly) | 2 | anatomy support under fig-01 |
| `[0025]` (solder-attach substrates persist; "small" pitches) | 2 | HBI-meets-solder beat (ex-Candidate-3 material) |
| `[0034]` (1-10 micron HBI pitch on the bridge) | 2 | quantitative color; description-only — never present as claim-required |
| `[0024]` (passive Imax limit; active TSV challenges) | 4 | problem framing for power-through-the-floor |
| `[0035]` (power from cavity floor; fewer routing layers, can improve product yield) | 4 | effect anchor; the ONLY yield sentence in the patent — belongs to the TSV routing, NOT the test step |
| `[0123]` (claim 2 through-contact) | 4, re-cited in 5 | the via structure as claimed vs its described purpose |
| `[0054]` / `[0138]` (TGVs; glass layer 20 µm-1.4 mm) | 4 (one paragraph) | glass tie-in; claim 17 scope caveat below |
| `[0122]` (claim 1 direct bonding) | 5 | claim-map walk |
| `[0144]` (claim 20 cavity) | 5 | claim-map walk |
| `[0059]` (SoC-class functionality) | 6 or 4 close | scale-of-ambition line |
| `[0001]` / `[0022]` / `[0023]` | 4 or 2, one use total | background problem color; do not stack all three |

External facts: cite by Fact ID from fact-check-log.md; EMIB/EMIB-T content NEVER carries a `[dddd]` anchor (the patent does not contain the term).

## (c) Framing trace (rejected candidates)

- Candidate 2 ("the test is the patent") rejected as spine: the specification never states the test's benefit — `[0035]`'s yield sentence belongs to the TSV routing. The yield economics live in §3 as clearly-labeled external industry math (kgd-yield-multiplier). Phase 2 must NOT re-center the essay on the test alone or let the yield math read as the patent's claim.
- Candidate 3 ("two bonding worlds") rejected: Axis 4 unanchored this run; survives only as §2 mechanism support. Do not reframe the essay around hybrid-bonding-vs-solder.
- Candidate 4 ("the glass filing") rejected 2/4: glass is one paragraph in §4, not a thread. Do not let the Intel-glass-roadmap tie-in grow beyond that paragraph.

## (d) Traps to avoid

**Claim-scope traps (restating the Claim scope map — sought/open/pinned vocabulary):**
- PENDING APPLICATION: every "locks" is a SOUGHT lock. Do say "the claim as filed requires", "Intel is claiming"; don't say "Intel owns/has locked/secured". No granted claim exists (us20250266395-bibliographic: status pending).
- Claim 19 (the spine claim): DO present the order (bridge-to-dies → test → substrate-on-pass) as required by the method claim as filed. DON'T attribute hybrid bonding, TSVs, pitch numbers, cavities, or glass to claim 19 — bonding method is open in 19 (hybrid bonding and solder are separate dependent options, `[0145]`/`[0146]`), and the cavity is claim 20.
- Claim 1: DO say the apparatus claim's direct-bonding language is hybrid bonding in claim text. DON'T import the 1-10 µm / sub-micron pitch numbers into any claim — they are description examples (`[0025]`, `[0034]`); present them as the description's numbers, on description anchors.
- Claim 2 / power: the claim locks only "a contact on the second surface providing an electrical pathway to the first surface". The PURPOSE (power from the cavity floor) is the description's "often used to" sentence `[0035]`. DO narrate purpose as the description's; DON'T write "claim 2 claims power delivery from the cavity floor".
- Claim 17 (glass + TGV): as filed it depends on claim 16 — the NO-cavity inverted package — not on the cavity packages. DON'T write "the cavity package claims a glass-TGV substrate". Example 17 `[0138]` is written broader than the claim; if quoting `[0138]`, attribute breadth to the Example, not the claim.
- Pins: there are none in the claims (claim 17's 20 µm-1.4 mm is an exact stated range, not an "about" pin). The description's "about 20 microns to about 1.5 millimeter, +/-10%" `[0054]` is a description-level approximate range — never call either a floor or ceiling the claims impose beyond what they state, and never harmonize the two numbers (1.4 vs 1.5 mm) — they differ; quote whichever you anchor.

**Attention-budget trap (motif budget):**
- Prosecution/status/finance is priced in exactly ONE section: §5 (payload: pricing). Elsewhere: at most one status clause inside the lead's two-sided call, plus the closing recap. The MOTIF counts paraphrase echoes: "still just paper", "one filing among hundreds", "defensive filing", "not a roadmap", "pending before an examiner" all draw on the SAME budget. If §5 says "one filing among hundreds", the close's guard must not repeat that phrasing family a second time — the total across lead clause + §5 + close is the whole allowance.
- Generic-truism ban downstream: "patents don't guarantee products" appears at most ONCE, as the single anti-hype guard inside the firm close — never as the steelman, never as a recurring hedge.

**Other traps:**
- The patent NEVER says "EMIB" or "EMIB-T". Never write "this is EMIB-T('s successor)" as fact. Permitted posture: same problem family, same TSV-bridge power-delivery idea (`[0024]`, `[0035]` on the patent side; emib-t-ectc-2025 on the news side), assembly order inverted relative to the publicly described chips-last EMIB flow (emib-chips-last-flow).
- The KGD yield numbers (81% / 35%) are external tier-4 industry math — always the essay's/industry's arithmetic, never the patent's. The patent's only quantified effect sentence is `[0035]`.
- "Known-good" is a gloss; the patent's words are "performance testing" / "passes performance metrics". Keep verbatim quotes verbatim; gloss outside the quotes.
- The 12-HBM-stack / 120x120 mm package numbers are the EMIB-T roadmap (emib-package-roadmap-120mm, tier-3), not this filing. This filing draws TWO dies; the abstract says "two or more integrated circuit die".
- Figure family-break is decided: FIG. 9 and FIG. 10 are not shown; do not reopen. If citing their variants, use `[0057]`/`[0058]` prose.
- Em dash banned in essay body; patent verbatim quotes keep their original characters (incl. "+/−").
- Filing date discipline: filed 2024-02-20, published 2025-08-21, EMIB-T unveiled at ECTC May 2025. "Filed ~15 months before the EMIB-T unveiling" is the correct comparison; do NOT say the filing predates EMIB-T's development (unknowable) — only its public unveiling.

## (e) Open questions for Phase 2 (awaiting orchestrator/SETI)

- reader_sentence drafted at the top of title-lead-candidates.md — needs orchestrator confirmation.
- Cover crop check: if fig-11 (flowchart) crops poorly at 5:2, the declared fallback is fig-08 as header with fig-11 demoted to body — surface, don't decide silently (figure-selection.md §Header).
- Whether §5's claim-map walk quotes claim 1's direct-bonding span (`[0122]`) in full blockquote or paraphrase-then-cite; default: translate-then-quote once, for claim 19's two spans only, and cite the rest inline.
- Mahajan/EMIB-origin footnote (mahajan-intel-fellow, tier-2): use at most one sentence in §5 ("mainline packaging org" support). Drop entirely if §5 runs long — it is credibility color, not load-bearing.
