# Revision notes — etched-us12361091

> Post-acceptance self-audit round 1 revision (composer revision mode, origin:
> `self-post-accept`). Target: `handoff/03-edit/essay-final.md`, edited in place
> (draft_version 2 → 3) and synced to `handoff/02-compose/essay-draft.md` +
> `publication.md`. One `## delta` block per applied finding cluster; alias ids from the
> inner-loop leftovers (r2-*/r3-*) and cross-reader convergences are folded into their
> primary block. Grounding fix priority observed throughout (anchor → narrow → label →
> cut); no hedge added anywhere; the §7 verdict call and landing are byte-identical
> outside the sa1B-F2 clause. Upstream artifacts touched: `handoff/01-design/
> invention-summary.md` (anchor-token inventory only — no new Quotable-span rows, so
> gate_quotes obligations are unchanged) and `handoff/01-design/fact-check-log.md`
> (sa1G-F9 registry row).

## delta
finding_id: sa1A-F1 (= r2-F3)
origin: self-post-accept
class: paraphrase-hedge-compression
fix_class: narrow
round: selfaudit-1
before: "The description sizes the tensor parallel group around exactly that operation [0121]."
after: "The description offers exactly that operation as a basis for sizing the tensor parallel group [0121]."
rationale: [0121] offers MLP-based sizing as one may/for-example option among alternatives; verb narrowed to option level per the reader-A recommendation; the section's other anchors ([0251], [0258], [0313], [0278]) still carry the header's verdict unchanged.

## delta
finding_id: sa1B-F2
origin: self-post-accept
class: claim-scope-misattribution
fix_class: label
round: selfaudit-1
before: "Reduce and gather traffic run at the same time on separate channel families [0142], with the same load on every link [0168]."
after: "Reduce and gather traffic run at the same time on separate channel families [0142], over equal-bandwidth links (claim 5), with the same load on every link under the description's prescribed split [0168]."
rationale: the "granted, checkable substance" list now contains only claim-locked items (hop bound claim 1, disjoint simultaneous families claims 8/9/11, equal bandwidth claim 5) and the equal-load property is explicitly labeled as following from the described split, per [0168]'s own unequal-tiles counterfactual; verdict call, firmness, and every other §7 sentence byte-identical ("under the split the description prescribes" was tried first and varied to "the description's prescribed split" after gate_dupe flagged a 5-gram echo of the §4 sentence).

## delta
finding_id: sa1B-F1 (+ sa1A-F7, 2/2 reader convergence on the design-around question)
origin: self-post-accept
class: steelman-absent
fix_class: label
round: selfaudit-1
before: steelman argued thinness only against the marketing adjective ("A topology-only claim over standard link technologies is a thin moat...")
after: added one labeled-analysis sentence completing the objection: "In practice the fence reaches only builders who copy the wiring: a rack that keeps its networking switch, the filing's own foil [0032], sits outside claim 1, and the scheduling claims (8, 9, 11) bind only traffic routed the claimed way, a firmware choice."
rationale: names the fence's binding condition (switchless two-tier builds only; switched fabrics outside claim 1 by the patent's own foil [0032]) and the firmware-avoidable leg (claims 8/9/11), at full strength, as "In practice"-labeled analysis; the verdict is not flipped — the closing's existing reframe ("published the diagram its own hardware can now be checked against") already answers it and is untouched, preserving that continuity.

## delta
finding_id: sa1G-F1
origin: self-post-accept
class: anchor-incomplete
fix_class: anchor
round: selfaudit-1
before: "three example families, methods, topology, and AI-model computation [0336]"
after: "three example families, methods, topology, and AI-model computation [0336], [0337], [0384], [0418]"
rationale: [0336] states only the numbered-example convention; the three families' contents live at [0337] (Example 1), [0384] (Example 2), [0418] (Example 3) per the grounding report; tokens made resolvable upstream in invention-summary.md Layer-4 evidence list (notation only, no new quote rows).

## delta
finding_id: sa1G-F2 (= r2-F1)
origin: self-post-accept
class: anchor-offbyone
fix_class: anchor
round: selfaudit-1
before: "Each set subdivides into two groups of chips, labeled 712a through 712d, and the channels split with them into two families [0135]."
after: "Each set subdivides into two groups of chips, labeled 712a through 712d [0135], [0136], and the channels split with them into two families [0138], [0139]."
rationale: [0135] carries the four-group naming only; the each-set-includes-two-groups mapping is [0136] (per the grounding report), and the two-families clause is [0138]/[0139]; each clause now carries its own anchor. Upstream: [0136] made explicit in invention-summary.md Layer-2 step 3, where Phase 1 had already extracted the fact under the [0135]-[0139] range notation.

## delta
finding_id: sa1G-F3 (+ sa1A-F3 loop clause)
origin: self-post-accept
class: anchor-offbyone
fix_class: anchor
round: selfaudit-1
before: "Its decoding layers, the loop that infers one token at a time [0313], run..."
after: "Its decoding layers, the loop that infers one token at a time [0259], run..."
rationale: the repeat-per-token / next-token framing lives at [0259]; [0313] is the feedforward element-count comparison and stays only at its two §5 uses where that is the content.

## delta
finding_id: sa1G-F9
origin: self-post-accept
class: external-fact-registry-gap
fix_class: upstream-registry (no essay text change)
round: selfaudit-1
before: §6's "US applications can stay unpublished for up to 18 months after filing" sourced only via essay-context.md Scope-boundaries prose
after: fact-check-log.md external-facts row `us-18month-publication-window` (tier-2 general patent-law fact, 35 U.S.C. §122(b), source chain essay-context.md prose) + a Notes entry recording the post-audit addition
rationale: the fact is accurate and sanctioned; the gap was registry-process only — every external fact the essay uses now has a registry row.

## delta
finding_id: r2-F2 (+ sa1G-F5)
origin: self-post-accept
class: anchor-offbyone
fix_class: anchor
round: selfaudit-1
before: "...separated purely for legibility, and the dense web of FIG. 7C is the two overlaid [0123]." / caption "...712a to 712d and 712b to 712c. Added to FIG. 7A's links it gives the full FIG. 7C web [0123]."
after: "...separated purely for legibility [0123], and the dense web of FIG. 7C is the two overlaid [0125]." / caption "...712a to 712d and 712b to 712c [0139]. Added to FIG. 7A's links it gives the full FIG. 7C web [0123], [0125]."
rationale: [0123] covers subgraphs-for-legibility and the union of 7A+7B but never names FIG. 7C; the 7C-single-figure fact is [0125] (q-0125-1); the criss-cross pairing detail in the FIG. 7B caption is [0139]'s content (sa1G-F5).

## delta
finding_id: r3-F1 (= sa1B-F5, sa1G-F6; + sa1A-F3 parenthetical)
origin: self-post-accept
class: anchor-incomplete
fix_class: anchor
round: selfaudit-1
before: "...then projection, then an MLP [0252]."
after: "...then projection, then an MLP [0252], [0254]."
rationale: [0252] lists the four decoding layers; the "(QKV generation and attention computation)" sub-blocks (916, 918) are named at [0254], which is in the Phase-1 reference-number table (gate-safe).

## delta
finding_id: r3-F2 (= sa1G-F7)
origin: self-post-accept
class: anchor-incomplete
fix_class: anchor
round: selfaudit-1
before: "*FIG. 9A: the decoding-layer loop the description maps onto the group [0251].*"
after: "*FIG. 9A: the decoding-layer loop the description maps onto the group [0252], [0259].*"
rationale: minimal correct set for the caption's two claims — the loop is [0259], the maps-onto-the-group fact is [0252] (tensor parallel group performing the decoding-layer operations, per the round-3 reviewer's patent quote); [0251] (what the model is) dropped as not asserted by the caption; [0263] avoided as not Phase-1-resolvable.

## delta
finding_id: r3-F3
origin: self-post-accept
class: external-fact-universalization
fix_class: narrow
round: selfaudit-1
before: "It carries 23 claims, three of them independent, over 16 figures of one idea: how the chips of an AI cluster should be wired to each other."
after: "It carries 23 claims, three of them independent, across 16 figures, and every claim pursues one idea: how the chips of an AI cluster should be wired to each other."
rationale: the one-idea attribution moved from the figures (7 of 16 sheets belong to the other example families, as §2 itself says two paragraphs later) to the claims, where it is verified true.

## delta
finding_id: sa1G-F4
origin: self-post-accept
class: figure-caption-scope-deferral
fix_class: label
round: selfaudit-1
before: header caption "...16 channels in all, and no wire runs inside a column [0128], [0129]."
after: header caption "...16 channels in all, counted off the drawing, and no wire runs inside a column [0128], [0129]."
rationale: the caption now carries the figure-derived caveat the body already gives the count ("read off the figure, not numbers the patent states"), so the anchored clause no longer implies the number is patent text.

## delta
finding_id: sa1G-F8
origin: self-post-accept
class: anchor-incomplete
fix_class: anchor
round: selfaudit-1
before: "FIG. 6 shows a host, two tensor parallel groups, and a memory 630 whose role is to ... [0119]."
after: "FIG. 6 shows a host, two tensor parallel groups, and a memory 630 [0112] whose role is to ... [0119]."
rationale: the host/two-groups/memory-630 descriptive clause is [0112]'s content; the quoted role clause stays on [0119].

## delta
finding_id: sa1B-F3
origin: self-post-accept
class: claim-scope-misattribution
fix_class: narrow
round: selfaudit-1
before: "each set must contain two device groups, wired in exactly the dual-family pattern of FIGS. 7A and 7B"
after: "each set must contain two device groups, wired in at least the dual-family pattern of FIGS. 7A and 7B"
rationale: claim 18 is a comprising floor (no-intra-set is dependent 19, hop bound dependent 22); "exactly" implied a closed blueprint.

## delta
finding_id: sa1B-F4
origin: self-post-accept
class: claim-scope-misattribution
fix_class: narrow
round: selfaudit-1
before: "The patent claims the movement pattern that makes such behavior cheap."
after: "The patent claims the wiring and the lane schedule that make such behavior cheap."
rationale: the antecedent could bind to the just-quoted unclaimed no-rejoin residency ([0278]/[0267]); narrowed to what is actually claimed (wiring + lane scheduling, claims 1/3-5/8-11); the fence sentence "It does not claim the store." kept verbatim.

## delta
finding_id: sa1B-F6
origin: self-post-accept
class: paraphrase-accidental-drift
fix_class: narrow
round: selfaudit-1
before: "The patent's own stated wins are fewer connections than a mesh [0130]"
after: "The patent's own stated wins are fewer connections than a full mesh [0130]"
rationale: [0130]'s comparator is a full (all-pairs) mesh; unqualified "mesh" reads as 2D mesh/torus to practitioners and inverts the comparison.

## delta
finding_id: sa1B-F7 (= sa1A-F8)
origin: self-post-accept
class: claim-scope-misattribution
fix_class: cut
round: selfaudit-1
before: "Its claims lock a wiring discipline for a group of AI chips"
after: "Its claims lock a wiring discipline for a group of chips"
rationale: 2/2 reader convergence — §5 correctly says AI is absent from the claim language; the lede's "AI" shorthand was a self-contradiction handed to a quote-tweeter; the Etched context already supplies the AI framing.

## delta
finding_id: sa1A-F5
origin: self-post-accept
class: jargon-gloss-gap
fix_class: cut
round: selfaudit-1
before: "Out of stealth after taping out its A0 silicon."
after: "Out of stealth after finishing its first chip design, the A0."
rationale: first jargon hit of the essay, un-glossed; replaced with reader A's plainer-verb restatement of the same registered fact (A0 tapeout, fact `etched-lvi-biz-thread-2026-07`), preserving the fragment cadence and the company's-own-account fence.

## delta
finding_id: sa1A-F6
origin: self-post-accept
class: reader-engagement-break
fix_class: label
round: selfaudit-1
before: "The first communication channels (730) join group 712a with 712c and group 712b with 712d [0138]."
after: "The first communication channels (730) pair the groups straight across, 712a with 712c and 712b with 712d [0138]."
rationale: the persona's nearest bail point gets the plain-words shape ("straight across" vs the existing "criss-cross") before the labels; group-level geometry verified against fig-07A/07B (730 pairs same-height groups, 740 pairs diagonally); labels kept because claim 18 needs them later.

## Considered, not applied

- **sa1A-F2** (low; "connection count balloons as the group grows [0130]"): not applied.
  2-of-3 auditors examined and passed it — the grounding verifier ruled the row SUPPORTED
  ("qualitative color on an undisputed graph-theoretic property, not a numeric patent
  claim") and the round-3 reviewer deliberately declined to flag it; the numeric instance
  (16-vs-28) is already labeled derived in body and footnote. Narrowing would trade
  accurate, common-knowledge color for no grounding gain.
- **sa1A-F4** (low; §7 "The boundaries set out above scope that call. They do not soften
  it."): not applied. The orchestrator's constraint holds §7 byte-identical outside the
  sa1B-F2 clause, and the sentence pair is the sanctioned 6G limits-referenced-not-relisted
  device (rounds 2-3 pass-6 both cite it; reader B's over-hedge check quotes it
  approvingly). One-reader stylistic objection does not outweigh the verdict-section
  contract.
- **sa1A-F9** (low; memory-absent beat in 4 sections + title): not applied. Reader A's own
  recommendation was "no standalone revision needed"; each instance rides new evidence
  (rounds 2-3 census), and none of this round's edits touched those beats, so no free
  consolidation existed.

> Post-acceptance self-audit ROUND 2 revision (composer revision mode, origin:
> `self-post-accept`), appended per protocol — round-1 blocks above are untouched.
> Target: `handoff/03-edit/essay-final.md` edited in place (draft_version 3 → 4) and
> synced to `handoff/02-compose/essay-draft.md` + `publication.md`. Applied: 6 blocks
> below (sa2B-F1 + sa2G-F3 arbitrated by the orchestrator as ONE claim-scope precision
> edit). §7 is byte-identical to draft_version 3 (verified by cmp on the §7-to-EOF
> region). Grounding fix priority observed (anchor → narrow → label → cut); no hedge
> added anywhere; the verdict call is unchanged. Upstream artifact touched:
> `handoff/01-design/invention-summary.md` (`[0037]`/`[0039]` anchor tokens made
> explicit in the 종래 문제 paragraph — notation only, no new Quotable-span rows, so
> gate_quotes obligations are unchanged). thesis-trace.md word_actual values trued up
> for all sections (whitespace-token counts on publication.md; prior values were stale
> from round 1). figures-rationale.md: no figure content touched this round.

## delta
finding_id: sa2G-F1
origin: self-post-accept
class: anchor-incomplete
fix_class: anchor
round: selfaudit-2
before: "the chips must combine partial results into one (a reduction) and hand out copies of pieces (a gather) to keep going [0036]."
after: "...to keep going [0036], [0037], [0039]."
rationale: [0036] names the two processes but the definitional mapping sits at [0037] (sub-results combined to generate the final result) and [0039] (data is copied between the processing devices), per the round-2 grounding report; tokens made resolvable upstream in invention-summary.md 종래 문제 (notation only).

## delta
finding_id: sa2G-F2
origin: self-post-accept
class: anchor-incomplete
fix_class: anchor
round: selfaudit-2
before: "Chips in the same set have no direct channel between them [0128], so a message ... two hops, one intermediate device, never more."
after: "...two hops, one intermediate device, never more [0130]."
rationale: the no-direct-channel clause is [0128]'s content; the at-most-two-hops-via-one-intermediate mechanic is [0130]'s (q-0130-1), quoted correctly elsewhere in the essay but not previously cited at this clause; each clause now carries its own anchor.

## delta
finding_id: sa2B-F1 (medium; + sa2G-F3 low, orchestrator-arbitrated as one claim-scope precision edit)
origin: self-post-accept
class: steelman-absent
fix_class: narrow + label
round: selfaudit-2
before: "In practice the fence reaches only builders who copy the wiring: a rack that keeps its networking switch, the filing's own foil [0032], sits outside claim 1, and the scheduling claims (8, 9, 11) bind only traffic routed the claimed way, a firmware choice."
after: five-sentence design-around inventory paragraph under the same "In practice" label: switch kept "in place of the claimed direct channels" sits outside claim 1 [0032] (sa2G-F3 narrow: instead-of reading, foreclosing the comprising-claim misreading); "A rack that copies the pattern but adds links inside a set arguably steps outside claims 1 and 14 as written. Both require channels that couple the sets 'without communicatively coupling any of the plurality of processing devices in the same set' [0386]." (sa2B-F1: the superset-add escape priced on the claims' own negative limitation, quote copied exactly from reader B's report, verbatim substring of q-0386-1); claim 18 "tolerates the added links but, like the scheduling claims (8, 9, 11), binds only traffic routed the claimed way, a firmware choice."
rationale: the steelman's strongest THIS-patent variant was the unnamed copy-and-add class (negative limitations are avoided by addition); now §6 reads as one three-leg inventory (switch-instead / superset-add / firmware-decline) split into its own 5-sentence paragraph to stay inside the 3-7 sentence band (single-sentence fold would have run ~100 words); translate-then-quote order per reader-profile rule 3; sa2B-F1's alternative (cutting "cross-set-only" from the fence-strength inventory) NOT needed — the pricing paragraph now immediately precedes that inventory, so the negative limitation is no longer listed as unpriced strength; verdict not flipped, §7 byte-identical, bold refinement line untouched.

## delta
finding_id: sa2A-F5
origin: self-post-accept
class: claim-scope-misattribution
fix_class: narrow
round: selfaudit-2
before: "every claim pursues one idea: how the chips of an AI cluster should be wired to each other"
after: "every claim pursues one idea: how the chips of a cluster should be wired to each other"
rationale: claims 1-23 never mention AI (the essay's own §5 states it); "AI cluster" imported the description's aim into a claims characterization; reader A's narrow adopted, Etched context already supplies the AI framing.

## delta
finding_id: sa2A-F1
origin: self-post-accept
class: jargon-overdepth
fix_class: narrow
round: selfaudit-2
before: "The description works the optimum once: 'When the number of processing devices is 8, p=4.35235, q=1.83809.' [0061]"
after: "The description works the optimum once: for eight chips, p and q, the two factors that set how many chips share a tensor, come out to about 4.35 and about 1.84 [0061]."
rationale: raw unglossed symbols broke reader-profile rule 1; decimals demoted to labeled approximations ("about") with the one-clause what-p-and-q-set gloss, per the orchestrator's arbitrated fix; gloss grounded in q-0061-2 (input-matrix split across 4 of 8 = "parallelism of the input"); divisor rounding and the four-of-eight practical reading unchanged; verbatim span q-0061-1 remains in invention-summary (gate_quotes unaffected); the [0061] nerd-candy number still spent exactly once per phase2-handoff-notes.

## delta
finding_id: sa2A-F3
origin: self-post-accept
class: thesis-restatement-redundancy
fix_class: cut
round: selfaudit-2
before: "The memory half has no equivalent fence anywhere in the claims. In the description, memory is scenery."
after: "In the description, memory is scenery."
rationale: the memory-absence one-liner ran 4 instances (S1/S5/S6/S7); the §6 instance cut per the keep-<=3 rule and the orchestrator's preference (cut the §6-side echo, never the §7 landing, which is byte-locked); the paragraph still carries the point via "no claim picks that option up [0133]" and "Described, never claimed", and §6's header states the memory half.

## Considered, not applied (self-audit round 2)

- **sa2A-F4** (low; §7 "The boundaries set out above scope that call. They do not
  soften it."): not applied, per orchestrator instruction. Round-1 ruling stands: this
  is the sanctioned 6G limits-referenced-not-relisted device (rounds 2-3 pass-6 cite it;
  reader B round 1 quoted it approvingly), reader A itself flags it as "plausibly exempt
  as functional scope disclaimer", and §7 is byte-locked this round.
- **sa2A-F2** (low, sweep; 712a/712c numeral density in §4): evaluated, not applied. The
  sweep condition was "only if a pronoun swap does it without losing anchor precision".
  No such swap exists: removing the explicit pairings from the body would detach the
  [0138]/[0139] anchors from the pairing content both grounding passes verified as
  SUPPORTED (rows 18-19), trading verified precision for at best one warn-free clause.
  The FIG. 7A/7B captions directly below already restate the pairings, the verbal
  handles ("straight across", "criss-cross") carry the intuition, and reader A's own
  persona verdict is "skim, not stop". Touch not light; rejected.

> Post-acceptance self-audit ROUND 3 revision (composer revision mode, origin:
> `self-post-accept`) — FINAL revision round, self-audit cap (3) reached; after this,
> orchestrator mechanical verification only. Appended per protocol — round-1 and round-2
> blocks above are untouched. Target: `handoff/03-edit/essay-final.md` edited in place
> (draft_version 4 → 5) and synced to `handoff/02-compose/essay-draft.md` +
> `publication.md` (strip pipeline re-run). Applied: 6 delta blocks below covering 8
> finding ids (sa3B-F2 folded into the sa3B-F1 rework — same passage, reader B's own
> narrow; sa3B-F6 converges with sa3A-F5). §7 is byte-identical to draft_version 4,
> verified by cmp on the §7-to-EOF region (incl. # Sources and # Footnotes) — no round-3
> edit touches §7. Grounding fix priority observed (anchor → narrow → label → cut); no
> hedge added anywhere; the sa3B-F1/sa3G-row-2 edits move in the anti-hedge direction
> (stronger grounding, priced escape). No upstream artifact changes: no new anchors
> beyond the essay's existing set ([0026]/[0032] already anchored in §3), no new quotes
> (gate_quotes obligations unchanged), no fact-check-log rows needed. thesis-trace.md
> 6-boundary description, anchor list, coverage notes, and all word_actual values
> refreshed; figures-rationale.md round-3 note appended (no figure content touched).

## delta
finding_id: sa3B-F1 (medium; + sa3B-F2 low, folded — same passage, reader B's own narrow)
origin: self-post-accept
class: claim-scope-misattribution
fix_class: narrow + label
round: selfaudit-3
before: "In practice the fence reaches only builders who copy the wiring and stop there. [...] That leaves claim 18, which tolerates the added links but, like the scheduling claims (8, 9, 11), binds only traffic routed the claimed way, a firmware choice."
after: "In practice the fence reaches builders who copy the claimed wiring, and through claim 18 it reaches builders who add links but keep the lane discipline. [...] That leaves claim 18, which tolerates the added links and binds the traffic instead, the same kind of rule claims 8, 9, and 11 stack on top of claim 1's structure. Declining that rule is a firmware choice with a price: reroute the traffic and you forfeit the cheap overlap of reduce and gather, the property that made the pattern worth copying."
rationale: claims 8/9/11 are dependents of claim 1 — each binds claim 1's full structure PLUS routing (reader B's claim-relationship walk, patent.md lines 947-953 per the report), so "binds only traffic ... a firmware choice" mislabeled them as traffic-only and handed a skeptical pro the attack "your fence's non-generic element is firmware-avoidable" against the fence paragraph four sentences later. Firmware-avoidability now attaches to claim 18's routing RULE only (labeled as the same kind of limitation 8/9/11 stack on claim 1's structure), and the decline is priced: rerouting forfeits the cheap disjoint-family overlap of reduce and gather — the reconciliation with the fence paragraph's "non-generic, inference-shaped part" (§4's simultaneity win) that reader B found left off the page. sa3B-F2 folded: the topic sentence "reaches only builders who copy the wiring and stop there" conceded past the paragraph's own evidence (claim 18 also reaches copy-and-add builders who keep the lane discipline); narrowed per reader B's recommended shape. Strengthens the fence pricing; verdict direction, firmness, bold line, and fence paragraph untouched. Grounding basis: CL-DA3 (claim 18 has no same-set exclusion — that is dependent claim 19) already verified SUPPORTED by the round-3 grounding report.

## delta
finding_id: sa3G low-confidence row 2 (grounding report §2 CL-DA1 commentary; orchestrator-listed sweep item)
origin: self-post-accept
class: confidence-asymmetry
fix_class: anchor
round: selfaudit-3
before: "A rack that keeps its networking switch, the filing's own foil [0032], in place of the claimed direct channels sits outside claim 1."
after: "A rack that keeps its networking switch in place of the claimed direct channels sits outside claim 1: the switch is the foil the filing itself sets against the fixed topology [0026], [0032]."
rationale: the flat "sits outside claim 1" sat next to the "arguably"-hedged superset sentence with no visible reason for the confidence gap. Harmonized by option (b) of the report: the flat sentence now carries the patent's-own-dichotomy grounding — [0026] frames the data switch and the fixed topology as alternative system types (grounding CL-DA1: "appropriately un-hedged given how directly it follows from the claim's own negative limitation") — rather than by adding an "arguably", which the jurisdiction fence forbids as a grounding fix. The neighbor's "arguably" (CL-DA2's genuine negative-limitation/comprising construction question) is retained as earned precision. "In place of" (the sa2G-F3 instead-of reading) preserved. [0026] already in the essay's anchor set via §3; no gate_quotes impact.

## delta
finding_id: sa3G-F1 (medium)
origin: self-post-accept
class: external-fact-overextension
fix_class: narrow
round: selfaudit-3
before: "Low-Voltage Inference is nowhere in this filing or its granted siblings."
after: "Low-Voltage Inference is nowhere in this filing."
rationale: the "granted siblings" extension asserted a confident negative about the full text of US 12,306,903 B1 and US 12,361,262 B1, neither of which is in this run's evidentiary record (fact-check-log `etched-family-trio-wips` is bibliographic metadata only; the claim traced to essay-context.md prose, unverified). The filing-only claim is fully supported by the run's complete read of patent.md (grounding EX8: "this filing" portion fully supported). The following "The same goes for the power-delivery work, the cold plates, and the HBM/SRAM hybrid..." sentence inherits the filing-only scope from its antecedent, so one cut narrows both. Alignment sweep: no # Footnotes or # Sources entry references the sibling absence (Sources lists the trio bibliographically — supported, kept); §2's sibling identity/division-of-labor sentences are bibliographic (EX6 SUPPORTED, tier-2) and kept intact per instruction; §7's "no substance in this filing" was already filing-scoped. Fix option 2 of the report chosen over option 3 (a new registry row for the siblings) — no new external-fact research is sanctioned at cap.

## delta
finding_id: sa3A-F1 (low)
origin: self-post-accept
class: jargon-gloss-gap
fix_class: label
round: selfaudit-3
before: "run normalization, then self-attention (QKV generation and attention computation), then projection, then an MLP [0252], [0254]."
after: "run normalization, then self-attention (QKV generation and attention computation, the making and use of the query, key, and value matrices), then projection, then an MLP [0252], [0254]."
rationale: reader-profile rule 1 — one-clause gloss at first use. "QKV" now expands to query/key/value at its first appearance, so §5's later "the Q, K, and V matrices are processed as tiles" [0267] resolves for the lay reader. The patent's two sub-block names (QKV generation 916, attention computation 918, per [0254]) are kept verbatim so the FIG. 9A box-for-box mapping the grounding pass verified still holds; the gloss maps generation → making and computation → use without asserting any unanchored attention mechanism. Anchors unchanged. Cost: the list sentence picks up one LONGSENT-001 warn (38 words) — accepted over splitting a grounding-verified span (M30) at cap.

## delta
finding_id: sa3A-F3 (nit)
origin: self-post-accept
class: paraphrase-subject-conflation
fix_class: anchor
round: selfaudit-3
before: "Route everything through a networking switch that lets any chip talk to any chip [0032], which the filing calls \"expensive to include in a system that performs tensor operations\" [0026]."
after: "Route everything through a networking switch that lets any chip talk to any chip [0032], a data switch the filing calls \"expensive to include in a system that performs tensor operations\" [0026]."
rationale: [0026]'s "expensive" sentence says it of "a data switch" while the essay's relative clause attributed the quote to [0032]'s networking switch — same foil, both anchors present, subject conflated by a word (reader A). The apposition renames the quote's subject with [0026]'s own term; the any-to-any clause stays on [0032]. One-word-level precision, not a hedge; §6's switch-out sentence now uses the neutral "the switch" with both anchors, consistent.

## delta
finding_id: sa3A-F5 (low; = sa3B-F6, 2/2 reader convergence on pass-7 check 7)
origin: self-post-accept
class: thesis-restatement-redundancy
fix_class: cut
round: selfaudit-3
before: "The description also lets each chip couple to memory devices, shared among the chips or not, and no claim picks that option up [0133]. Described, never claimed."
after: "The description also lets each chip couple to memory devices, shared among the chips or not, and no claim picks that option up [0133]."
rationale: both readers counted the core verdict asserted in 4 sections (§1/§5/§6/§7) against the <=3 letter, and both name §6's "Described, never claimed." as the §6 instance. Cut per orchestrator preference (§6's echo, never §7; §5's coda kept — it carries the essay's precise wiring-vs-store boundary, the sa1B-F4 fix both graders verified). The paragraph keeps the point in evidence form ("In the description, memory is scenery." + "no claim picks that option up" [0133]) and the FIG. 6 caption's "described in one embodiment figure and never claimed [0119]" stands, so nothing factual is lost; the assertion-form aphorism is what leaves. Verdict echo count returns to 3 (§1 lead, §5 coda, §7 verdict). Paragraph recount: 3 sentences, in band.

## Considered, not applied (self-audit round 3)

- **sa3A-F2** (nit; bare "scale-up domain" in §7): not applied, per orchestrator
  instruction. §7 is byte-locked this round, and the term is the thread's own quoted
  vocabulary (§1: "across the entire scale-up domain") — §7's use deliberately hands the
  inspection moment back in the thread's own term. Cost is one beat for reader A's
  persona, no bail; a §7 gloss would trade the locked verdict text for a nit.
- **sa3A-F4** (nit; §7 imperative opener "Hold the thread against the grant..."): not
  applied, per orchestrator instruction and prior rulings (rounds 1-2 considered-not-
  applied). The sanctioned firm-verdict device: rounds 2-3 pass-6 cite it, reader B's 6G
  check quotes it as the call leading, and reader A itself judges it functional. §7
  byte-locked.
- **sa3B-F3** (low; [0385] labeled "the specification's summary"): not applied. The
  numbered-Examples block is itself introduced as "a non-limiting summary of some example
  implementations" [0336] (quoted in the round-3 reports), so the label is fair to the
  patent's own framing; the grounding verifier independently ruled the row SUPPORTED
  (M48/CL11, "two or more" verbatim at [0385]); an anchor swap to [0004] would add a new
  upstream anchor row at cap for no gate gain. Judged not worth prose/anchor risk at cap.
- **sa3B-F4** (low; "up to 18 months" stated without the nonpublication-request tail):
  not applied. The sentence matches its registered external fact
  (`us-18month-publication-window`, tier-2, added round 1 per sa1G-F9); reader B's own
  analysis says the error direction is conservative — the record is even MORE of a floor —
  so the argument survives as written; extending the legal nuance would push the sentence
  beyond its registry row with no new registry work sanctioned at cap.
- **sa3B-F5** (low; PCT "extends each abroad" readable as existing foreign coverage): not
  applied. Outside the orchestrator's curated final list at cap. Mitigations standing:
  the sentence describes Etched's filing conduct inside a paying-to-keep-alive frame
  ("Etched is paying to keep all three alive"), and the "keeps each open at home"
  parallel signals pendency rather than granted rights; the registered family row is
  bibliographic and supports the PCT filings' existence. Logged as a residual for any
  future edition pass.
- **sa3B-F7** (low; "Three independents, three different trades of breadth for
  structure"): not applied. The grounding verifier independently ruled the sentence
  SUPPORTED (CL10); claims 1 and 14 package the same limitations at group vs system
  scope, which is itself a difference in what breadth is traded (claim 14 reaches
  multi-group assemblies), so the rhetoric has a defensible reading; "none of them
  mentions memory" HOLDS regardless. A recount to "two distinct trades" would reopen the
  census sentence adjacent to the narrowing exhibit at cap for a minor rhetorical gain.

## Self-audit closing status

- **Self-audit cap reached**: 3 rounds run, round 3 is the FINAL revision. What remains
  is orchestrator mechanical verification only (run_gates + check_run + archive); no
  further prose changes under self-audit authority.
- **Applied counts**: round 1 — 19 delta blocks applied (incl. inner-loop leftover
  aliases r2-*/r3-*), 3 considered-not-applied; round 2 — 6 delta blocks applied covering
  7 finding ids, 2 considered-not-applied; round 3 — 6 delta blocks applied covering 8
  finding ids (2 medium: sa3B-F1, sa3G-F1; the rest low/nit incl. the folded sa3B-F2 and
  the convergent sa3A-F5 = sa3B-F6), 6 considered-not-applied.
- **Residual open items** (considered-not-applied, round 3, by id): sa3A-F2, sa3A-F4,
  sa3B-F3, sa3B-F4, sa3B-F5, sa3B-F7 — all low/nit; none touches verdict direction,
  grounding chain, or hard-gate territory. Standing prior-round residuals: sa1A-F2,
  sa1A-F4, sa1A-F9, sa2A-F4, sa2A-F2 (all low, rationales in their round blocks).
- **Final state**: essay-final.md draft_version 5 (= essay-draft.md byte-identical;
  publication.md regenerated via strip pipeline); closing_posture: firm; §7 byte-identical
  to draft_version 4 (and to draft_version 3 — §7 last moved in selfaudit round 1,
  sa1B-F2 clause only); gates 13/13 PASS (STRUCT-004 triad warn 2 → 3 from the factual
  query/key/value enumeration; LONGSENT warn 7 → 8 from the glossed §5 list sentence —
  both advisory). Pending orchestrator mechanical verification.
