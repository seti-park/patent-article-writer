# Phase 2 Handoff Notes

## (a) Audience reframe decision

None. `input/essay-context.md` is absent; the default reader-profile binds: curious retail investor, advanced-high-school to early-undergraduate technical comprehension. They open for OpenAI (the company/story), and leave understanding the invention. Consequences: every term of art (mantissa, exponent, compute-in-memory, adder tree, dequantization) gets a one-clause gloss on first use; the recommended magnitude comparison for the alignment step is "line up the decimal points before you add, then remember where the point was" (clearly the essay's comparison, patent values verbatim).

## (b) Citation priority mapping

| Quotable span / anchor | Primary section | Role |
|---|---|---|
| `[0011]` triad (q-0011-1/2/3) | 2-mechanism | claim-1 wording, used first; the essay's verbatim claim quote source (the claim text and `[0011]` are word-identical for all three elements) |
| `[0005]` conversion-cost (q-0005-1) | 2-mechanism (problem setup) | why the trick matters; do NOT also spend in the lead |
| `[0104]` consistent-scale (q-0104-1) | 2-mechanism | what alignment buys |
| `[0199]` Emax 22 (q-0199-1) + `[0145]` INT35/FP22 (q-0145-1) | 2-mechanism | the worked numeric walk |
| `[0006]` no-separate-pipelines (q-0006-1/2) + `[0130]` formats (q-0130-1) | 3-scope-and-baseline | format-agility beat, explicitly labeled description material |
| `[0141]` MX shared scale (q-0141-1) | 3-scope-and-baseline | bridge to the OCP MX baseline (fact-check-log ocp-mx-spec-2023-09) |
| `[0183]` adders saved (q-0183-1) | 3-scope-and-baseline | claimed-circuits-have-teeth support after the steelman concession |
| `[0147]` product-every-cycle (q-0147-1) | 4-throughput | Axis 3 payoff |
| `[0012]`/`[0015]`/`[0154]` double-buffering (q-0012-1, q-0015-1, q-0154-1/2/3) | 4-throughput | description-anchored beat; see trap 3 |
| `[0118]` scan dual-purpose (q-0118-1) | 5-what-the-filing-is | depth evidence (the document specifies test circuitry) |
| `[0131]` reduced-precision effect (q-0131-1) | 2-mechanism or 3 | context for why FP4/6/8 at all; one use only |

## (c) Framing trace (rejected candidates)

- Candidate 2 ("floating-point math on integer hardware" as the SPINE) rejected: external baseline 3.5/4 and the hook underserves the default reader; its strongest objection ("alignment is textbook") attacks the frame itself. Its mechanism IS the tech core of §2 — keep the walkthrough, drop the "impossible" framing as the essay's entry point.
- Candidate 3 ("never stops to reload") rejected: no claims anchor in this publication (the adjacent claim block 11-19 is canceled); embodiment-only spine per 4-axis Rule 1. Double-buffering appears ONLY as a §4 body beat on description anchors.

## (d) Traps to avoid

1. **Claim-scope trap (restates the Claim scope map; sought-* vocabulary is mandatory).** This is a PENDING APPLICATION: nothing is locked; there are no locked scopes to cite, only sought scopes. DO: present claims 1 and 20 as what OpenAI is *seeking*: (a) FP primitive product per column cell, (b) mantissa alignment BY SHIFTING, (c) INTEGER-format adder-tree accumulation; dependent claims 2-10/20-28 add the shift-calc unit, the register sizing rule (max exponent + mantissa bits), the logarithmic mux tree, AND-gate partial products, LCM bitcell sizing. DON'T: call the mode decoding unit, FP4/FP6/FP8 format agility, dual-bank parallel write+compute, or scan modes "claimed" — in this publication they are description/aspect material (map rows say "leaves open"); narrate them as the description's, on description anchors. DON'T describe any claim element as a "floor", "ceiling", or guaranteed scope; there are no pinned "about X" values in this claim set at all, so no pin vocabulary should appear. DON'T say "OpenAI patented X" for anything in this document — "filed", "claims (pending)", "describes" are the honest verbs.
2. **Canceled-claims trap.** Claims 11-19 read "(canceled)" in the publication. State it as a document fact at most once (§5). DON'T speculate on why, and DON'T assert continuations/divisionals exist — the family's future is in ⑥(b) of the owner briefing (not established).
3. **Description-vs-claims attribution for double-buffering.** §4's double-buffering beat cites `[0012]`/`[0015]`/`[0154]` and must attribute the scheme to the description/summary, never to the pending claims.
4. **Format-naming trap.** The patent labels formats FPn (sign-mantissa-exponent): "FP8 (1-4-3)" = 1 sign, 4 mantissa, 3 exponent `[0132]`. This is NOT the OCP "E4M3" naming order and the encodings are the patent's custom variants `[0160]`. DON'T equate the patent's FP8 (1-4-3) with OCP MXFP8's E4M3/E5M2; say the macro operates on MX-STYLE blocks (32 elements, shared scale `[0141]`) and leave encodings alone.
5. **Novelty inflation trap.** DON'T claim OpenAI invented block floating point, shared-exponent blocks, or "FP math on integer adders" as ideas — OCP MX (2023) standardized the block format and alignment-before-add is standard arithmetic practice. The claimed contribution is specific circuit structure inside a memory macro. The steelman beat in §3 concedes this ONCE and returns to the affirmative core (concede-and-return; affirmative core carries >= the concession; no spend/procedure lexicon in the beat; do not re-spend the pending-status caveat there — it lives in §5).
6. **Biography trap.** DON'T assert where any inventor worked on the provisional date (2024-11-22), and DON'T assert OpenAI acquired Rain AI (unverified, tier-4). Allegrucci's Apple/Rain background is press-reported (label it); the load-bearing facts are only the document's own: OpenAI Opco as applicant/assignee, the priority date, the inventor names.
7. **Implementation trap.** No source says Jalapeño or any Broadcom co-developed chip implements this application's claims, or that this design exists in silicon. The spec's numbers (product per cycle, 100% utilization, 256 reuses) are design statements, not measurements — quote with the patent's own "may/can" hedges intact.
8. **Attention-budget trap (MOTIF budget, not sentence budget).** Prosecution/registry/status material is `payload: pricing` and lives in exactly ONE section (§5-what-the-filing-is), plus at most one lead clause (the pending-application label inside the lead's call) and the closing recap. All variants of the status motif ("still pending", "not yet granted", "not yet an asset", "claims were canceled", "the office hasn't said yes") draw on the SAME budget — paraphrase echoes count. Process narration (examination mechanics, filing procedure, who-filed-what-when beyond the two load-bearing dates) is not lead material at all. The Broadcom/Jalapeño corporate beats are frame/pricing color, not plot: the spine's subject stays the invention.
9. **Hygiene.** Em dash banned in essay body; none of the selected Quotable spans contain one. Preserve patent typos verbatim if quoted (claim 10 "completement", abstract "useful or heavy"); prefer not quoting the garbled claim-24 clause at all — if claim 24 must be discussed, paraphrase with a note, don't "fix" the quote.
10. **Text-only run.** Zero figure assets exist (figure-selection.md). DON'T reference figure files or write captions; FIG.-number mentions in prose are allowed only when quoting/citing the spec's own text. §2 must open with the verbal pipeline map (figure-rationale.md lists the prose compensations).

## (e) Open questions for Phase 2 (awaiting SETI)

- Whether to name Allegrucci (and the Apple background) in the lead or hold to §5. Default: hold to §5; the lead's beat is the document + mechanism, not the roster.
- Whether the §2 alignment walkthrough uses the worked FP8×FP6 numeric example (`[0199]` Emax 22, INT35 out, FP22 back) in full or abbreviates to one sentence. Default: full walk, it is the essay's core payload.
- Title pattern: recommended register is discovery; tension pair is the sanctioned fallback if the orchestrator prefers the date collision on the card. Do not mix the two leads.
- Whether the closing's forward-watching event foregrounds Jalapeño's end-2026 deployment or the family's examination. Default: Jalapeño (reader-checkable), examination fate as the second clause.
