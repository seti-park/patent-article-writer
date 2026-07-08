# Self-audit round 3 — Reader B (skeptical pro-subject reader)

- essay: `handoff/03-edit/essay-final.md` (draft_version 4, closing_posture: firm)
- persona: AI-infrastructure practitioner (tensor parallelism, NVSwitch-class fabrics,
  Megatron sharding, systolic arrays); hunting technical overclaim AND unearned hedging
  with equal appetite
- inputs read: essay-final.md, input/patent.md (full CLAIMS section read directly,
  lines 931-977), input/essay-context.md, input/figures/fig-07C/07A/07B/01/06/09A.png
- blind protocol honored: no edit-log, no revision-response/notes, no score-history, no
  prior selfaudit reports read
- verdict vocabulary: HOLDS / STRETCHES / BREAKS per claims-scope statement;
  findings sa3B-F1..F7, evidence-forced

## 1. Pass-7 checklist (persona-weighted)

| # | Check | Verdict | Evidence | Severity |
|---|---|---|---|---|
| 1 | BLUF lead-altitude | YES (pass) | Para 1: "Half of the loudest architecture claim in the thread already has a granted US patent standing behind it. The other half ... has no granted substance in the filings you can read today." Declarative verdict, no deferred question. | — |
| 2 | Header-as-claim | YES (pass) | All seven `##` headers are assertions ("Etched Patented the Wiring Half...", "No Latency Number, No Memory Claim", "One Leg Substantiated, One Leg Absent"). Header-only skim reconstructs the argument. No overpromising header found: "Every Chip Reaches Every Chip Without a Switch" is exactly claim 1's content ([0386]+[0387]). | — |
| 3 | Steelman present AND correct | YES (pass) | "The objection an informed reader should press lands at full strength. Claim 1 recites a wiring pattern and nothing else. ... A topology-only claim over standard link technologies is a thin moat for a 'proprietary ultra-low-latency, high-bandwidth interconnect'." THIS-patent objection (claim-1 text, [0134] link list, claim 5 equality-not-magnitude), conceded at full strength, then refined ("Structure is what an apparatus claim can lock..."). Not a generic truism. Two refinement-precision defects logged as F1 (medium), F2 (low) — presence and strength are NOT in question. | see F1/F2 |
| 4 | No meta posturing | YES (pass) | ABSENT. "The document to check is US 12,361,091 B1" is functional scope, not reader-instruction. | — |
| 5 | Jargon as signpost | YES (pass) | "(In graph-theory terms, this is a complete bipartite graph, K4,4 in the eight-chip case.)" — one parenthetical, no dive. Systolic array, reduction, gather, MLP each glossed in a single clause. | — |
| 6 | No stub / rhythm break | YES (pass) | Closing section (3 paras) is a conventional verdict coda, not markedly short vs siblings. | — |
| 7 | Thesis not over-restated | NO (fail) | Core verdict (wiring claimed / memory not) asserted in FOUR sections: S1 lead; S5 coda "The patent claims the wiring and the lane schedule that make such behavior cheap. It does not claim the store."; S6 "Described, never claimed." + bold line; S7 verdict section. Bar is <= 3. | F6, low |

## 2. Deep technical-claim audit — every claims-scope statement vs CLAIMS text

Granted claims read directly (patent.md lines 933-977). Note: paragraph anchors
[0384]-[0417] are the spec's numbered-Examples block, whose Example 2.1 floor is
"two or more" [0385]; granted claims 1/14 raise it to four-or-more. The essay tracks this
delta correctly.

| Statement (quoted) | Vs claims | Verdict |
|---|---|---|
| "two sets, every cross-set pair directly wired, nothing wired inside a set [0386]" | Claim 1 limitation, verbatim-identical text also at [0386] | HOLDS |
| "Any chip can reach any other through at most one chip in between [0387]" | Claim 1 wherein: "through at most one other of the plurality of processing devices" | HOLDS |
| "None of its claims mention latency, a bandwidth magnitude, or memory." | Verified over claims 1-23: no "latency", no bandwidth magnitude (claim 5 recites equality only), no "memory" | HOLDS |
| "four or more a side under the granted claim" | Claims 1 and 14: "first set of four or more ... second set of four or more" | HOLDS |
| Blockquote of claim 1's channel limitation, cited "claim 1, [0386]" | Character-identical in claim 1 (line 933) and [0386] | HOLDS (verbatim) |
| "Claim 1 makes that bound a requirement" | Wherein clause is a claim limitation, correctly presented as required | HOLDS |
| "each device couples to the same number of chips, the same number of channels, and channels of the same bandwidth (claims 3 to 5)" | Claims 3, 4, 5 respectively | HOLDS |
| "claim 8 binds the data transfer for each sub-operation exclusively to one channel subset. Claim 11 names the pair" | Claim 8: "occurs only via the first subset ... only via the second subset"; claim 11: reduction + gather | HOLDS |
| "Claim 9 has the two sub-operations running in overlapping time periods, one channel family carrying each [0142]" | Claim 9 verbatim concept ("in overlapping time periods ... at the same time") | HOLDS |
| "Which physical family carries which is the description's worked example rather than a claim requirement, with gather traffic on the first channels and reduction traffic on the second [0140]" | Exactly right, and quietly resolves that claim 11 labels reduction as "first sub-operation" while [0140] maps gather to 730: family assignment is unclaimed. Sharp claim-craft. | HOLDS |
| "the claims' only workload hooks are the systolic array (claim 7), matrix multiplication (claims 10 and 23), and the reduction and gather sub-operations (claims 11 and 23). AI, transformers, and inference are absent from the claim language." | Verified: no AI/transformer/inference token in claims 1-23 | HOLDS |
| "A rack that keeps its networking switch ... in place of the claimed direct channels sits outside claim 1." | Claim 1 requires channels that "directly communicatively couple" every cross-set pair; switch-mediated is the [0032] foil | HOLDS |
| "A rack that copies the pattern but adds links inside a set arguably steps outside claims 1 and 14 as written." | Negative limitation "without communicatively coupling any ... in the same set" vs comprising-open-endedness is a genuine construction question; "arguably ... as written" is earned precision, not hedge | HOLDS |
| "That leaves claim 18, which tolerates the added links but, like the scheduling claims (8, 9, 11), binds only traffic routed the claimed way, a firmware choice." | Claim-18 half HOLDS (no negative limitation — that is dependent claim 19 — so added intra-set links do not escape it; its routing wherein is conduct/configuration). The "(8, 9, 11)" aside STRETCHES: those are dependents of claim 1 and bind its full structure plus routing; only their incremental limitation is traffic. In the add-links hypothetical they fall WITH claims 1/14 automatically, not as live-but-firmware-avoidable claims. | STRETCHES → F1 (medium) |
| "The specification's summary covers two sets of 'two or more' devices [0385], while granted claims 1 and 14 require four or more per set." | Substance HOLDS ([0004] SUMMARY and Example 2.1 [0385] both say "two or more"; claims 1/14 say four-or-more). Anchor label imprecise: [0385] sits in the numbered-Examples block ([0336]), not the SUMMARY section. | HOLDS w/ anchor nit → F3 (low) |
| "claim 18 keeps the two-or-more floor but pays for it in structure: each set must contain two device groups, wired in at least the dual-family pattern of FIGS. 7A and 7B, with each sub-operation's traffic confined to its own family" | Claim 18 verbatim structure: two-or-more sets each including two groups; first channels g1↔g3, g2↔g4; second channels g1↔g4, g2↔g3; exclusivity wherein. "at least" correctly signals comprising. | HOLDS |
| "Three independents, three different trades of breadth for structure" | Claims 1 and 14 make the SAME trade (four-or-more floor + negative limitation), at group vs system level; only claim 18's trade differs. Rhetorical overcount, contradicted by the essay's own preceding sentences. | STRETCHES (minor) → F7 (low) |
| "claim 5 requires equal bandwidth across channels, not high bandwidth" | Claim 5: "configured for a same data bandwidth" | HOLDS |
| "none of them mentions memory" / "Described, never claimed" (memory 630, per-chip memory option [0133], [0119]) | No memory recitation anywhere in claims 1-23 | HOLDS |
| "at most one device between any two chips, ever [0387]" | "ever" is rhetorical but claim-backed ("at most one other") | HOLDS |

Absence claims verified by direct scan of the claims text: latency ABSENT, bandwidth
magnitude ABSENT, memory ABSENT, AI/transformer/inference ABSENT. All four absence
statements HOLD.

Design-around inventory completeness (persona task): switch-retained fabric (covered);
full-mesh / added intra-set links (covered, incl. the claim-19-vs-18 asymmetry); claim-18
firmware escape (covered). Not enumerated but immaterial for this audience: sub-four-per-set
builds (implicitly covered by the floor discussion + claim-18 trade), >2-partition
topologies (avoid claims 1/14 on the same negative-limitation logic; multi-hop toruses fail
the hypothetical anyway). No material omission; the overcorrection risk is F2, not a gap.

## 3. Mechanism + arithmetic honesty

| Item | Check | Verdict |
|---|---|---|
| 16 channels in FIG. 7C | Counted on fig-07C.png: 8 devices x 4 cross-links / 2 = 16 (7A shows 8, 7B shows 8) | HOLDS |
| 28 for all-pairs | C(8,2) = 28 | HOLDS |
| "both counts read off the figure, not numbers the patent states" | [0129] states "coupled to four other" devices but never 16 or 28; derivation correctly labeled, footnote [^derived-counts] matches | HOLDS |
| "inside nine months" | 2024-10-22 → 2025-07-15 = 266 days (< 9 months = Jul 22); footnote arithmetic correct | HOLDS |
| p, q "about 4.35 and about 1.84 ... Rounded to divisors, that is 4 and 2 ... input matrix lives spread across four of the eight chips [0061]" | [0061]: p=4.35235, q=1.83809; "when n=8, p=4 and q=2"; "an entirety of the input matrix is found on 4 of the 8 processing devices" | HOLDS |
| Two-hop mechanism ("rides through one chip of the opposite set: two hops ... never more") | [0130]: "at most two communication hops", via one device of the other set | HOLDS |
| Cut-through relay ("may begin forwarding data before it has finished receiving it [0143]") | [0143] verbatim concept; presented as description ("may"), never credited to claims | HOLDS |
| Balance mechanism ("the same amount of data may be shared by each of the processing devices A0-A7", same per channel, conditioned on the prescribed split) | [0168]/[0178] verbatim; the essay states the equal-tile precondition twice ("pre-cut", "follows from the split the description prescribes") | HOLDS |
| MLP 4x pressure ("four times the depth" [0313]; "four times greater than the model's other computations" [0258]; sizing basis [0121]) | All three verbatim-supported | HOLDS |

## 4. Grounding spot-check (exceeds 5-sample; sections 3, 4, 5, 6 fully anchor-checked)

Verified verbatim against input/patent.md: [0021], [0026], [0032], [0036], [0037],
[0039], [0061], [0112], [0119], [0121], [0123], [0124], [0125], [0126], [0128], [0129],
[0130], [0133], [0134], [0135], [0136], [0138], [0139], [0140], [0142], [0143], [0168],
[0178], [0251], [0252], [0254], [0258], [0259], [0267], [0278], [0313], [0336], [0337],
[0384], [0385], [0386], [0387], [0418]. All four blockquotes are character-verbatim
(claim 1 limitation; [0140] exclusivity sentence; [0278] no-entirety rule; plus inline
[0124], [0168], [0251], [0267], [0313] spans). One anchor-precision nit: F3 ([0385]
labeled "the specification's summary"). No dangling or misattributed anchor found.

Figures vs captions: fig-07C (710a right = a1/a3/a5/a7, 710b left = a0/a2/a4/a6, 16
channels, families overlaid) — caption VERIFIED including left/right placement and the
drawing's lowercase a-labels; fig-07A (730: 712a↔712c, 712b↔712d) VERIFIED; fig-07B (740
criss-cross) VERIFIED; fig-01 (Tensor Parallel Group / processing devices / systolic
arrays / processing elements) VERIFIED; fig-06 (system 610, groups 620a/b, memory 630,
host 602) VERIFIED; fig-09A (decoding layers 905: normalization 910 → self-attention 915
[QKV 916, attention 918] → projection 920 → MLP 925 → decoding 930) VERIFIED.

External-fact fencing: all thread numbers attributed ("every number in them is the
company's own account", "The company says"); quote chain footnoted; patent-family facts
match essay-context (WIPS-verified). Two loose legal generalizations: F4, F5.

Pinned values as pinned, not bounds: 4.35/1.84 presented as the description's worked
optimum; eight chips as "the drawings' eight-chip example"; four-or-more presented as a
claim floor. HONORED.

## 5. Over-hedge symmetric check (6G direction)

- Claim-locked facts carry firm verbs throughout ("lock", "fixes", "makes that bound a
  requirement", "binds", "requires"); every "may" in the essay is either inside a verbatim
  patent quote or attached to a description-only embodiment. No may/appears/suggests on a
  claim-locked fact: ABSENT (pass).
- Verdict section leads with the call ("Hold the thread against the grant and the verdict
  is firm both ways."), no safe-harbor boilerplate, boundaries framed as scoping ("They do
  not soften it."). gate_hedge posture honored (pass).
- "arguably steps outside claims 1 and 14 as written" — earned by a genuine
  negative-limitation/comprising construction question; NOT an over-hedge (pass).
- "Later filings may yet cover LVI. Nothing readable today does." — epistemically exact
  (pass).
- New design-around passage overcorrection check: one topic sentence concedes past its own
  evidence → F2 (low). It does not infect the verdict; the bolded rebuttal and fence
  paragraph restore full strength.
- Conclusion-vs-body proportionality: conclusion is neither bolder nor safer than the body
  ("the wiring half is the one you can check today, and it holds" is exactly what sections
  3-6 establish) (pass).

## 6. Findings

### sa3B-F1 — medium — claims-scope precision inside the steelman refinement
- pass: pass-7-adversarial-reader (persona B deep claims audit)
- check: technical-claim audit / design-around inventory
- verdict: STRETCHES
- span: "That leaves claim 18, which tolerates the added links but, like the scheduling
  claims (8, 9, 11), binds only traffic routed the claimed way, a firmware choice."
- evidence: claims 8, 9, 11 are dependents of claim 1 (patent.md lines 947-953); each
  incorporates claim 1's full structure (four-or-more sets, cross-set-only direct
  channels, hop bound) PLUS routing. "Binds only traffic routed the claimed way" is true
  only of their incremental limitations; in the add-links hypothetical they fall together
  with claims 1/14 as dependents, not as surviving firmware-avoidable claims. The aside
  also collides with the fence paragraph four sentences later that names exactly claims
  8/9/11's disjoint-family simultaneity "the non-generic, inference-shaped part" of the
  fence — handing a skeptical pro the attack "your fence's crown jewel is a firmware
  choice" with the reconciliation (a faithful copier who reroutes still infringes claim 1;
  escaping claim 18's routing rule forfeits the reduce/gather overlap that motivated the
  copy) left off the page.
- recommendation (jurisdiction fence: narrow/label, no hedging): narrow the aside so
  firmware-avoidability attaches to the routing LIMITATION, not to claims 8/9/11
  wholesale — e.g. attribute it to "claim 18's routing rule (the same kind of limitation
  claims 8, 9, and 11 stack on top of claim 1's structure)" — and/or state the forfeit:
  rerouting to escape the exclusivity gives up the simultaneity win. This strengthens the
  verdict; it does not soften it.

### sa3B-F2 — low — over-concession topic sentence in the design-around passage
- check: steelman refinement / over-hedge symmetric check (concession direction)
- verdict: STRETCHES (concedes past its own paragraph)
- span: "In practice the fence reaches only builders who copy the wiring and stop there."
- evidence: the same paragraph then shows claim 18 also reaches builders who copy AND add
  intra-set links while routing sub-operations exclusively per family — i.e. the fence
  reaches more than copy-and-stop builders. The unstated cost of the claim-18 firmware
  escape (losing the overlapping reduce/gather) makes the escape less free than "a
  firmware choice" implies.
- recommendation: narrow the topic sentence (e.g. "reaches builders who copy the wiring,
  and, through claim 18, those who copy it and keep the lane discipline"). Anti-hedge
  direction; verdict unchanged.

### sa3B-F3 — low — anchor label imprecision on the floor comparison
- check: grounding spot-check / anchor fix
- verdict: substance HOLDS, label imprecise
- span: "The specification's summary covers two sets of 'two or more' devices [0385]"
- evidence: [0385] sits in the numbered-Examples block introduced at [0336] ("described
  as numbered examples ... a non-limiting summary of some example implementations"), not
  in the SUMMARY section; the literal SUMMARY paragraph [0004] carries the same
  "two or more" framing verbatim.
- recommendation: anchor fix — cite [0004] (or rename the pointer "the specification's
  example clauses [0385]"). Quoted span "two or more" is verbatim in both, so gate_quotes
  is unaffected either way.

### sa3B-F4 — low — external legal generalization stated as absolute
- check: external-fact fencing
- verdict: STRETCHES (tail case)
- span: "US applications can stay unpublished for up to 18 months after filing, so the
  visible record is a floor, not a census."
- evidence: applications under a nonpublication request stay dark PAST 18 months, until
  grant. Error direction is conservative — it makes the record even more of a floor — so
  the argument survives; the sentence as written does not.
- recommendation: narrow ("typically stay unpublished for up to 18 months — longer if the
  filer requests secrecy"). No hedge on the verdict; this is a fact fix.

### sa3B-F5 — low — PCT verb overstates foreign reach
- check: external-fact fencing
- verdict: STRETCHES
- span: "a PCT filing extends each abroad, and a US continuation, published in 2026,
  keeps each open at home"
- evidence: a PCT application reserves national-phase rights; it grants no foreign
  protection yet. An investor can read "extends each abroad" as existing foreign coverage.
- recommendation: verb swap to the accurate half of the essay's own parallelism ("keeps
  each open abroad ... and ... at home").

### sa3B-F6 — low — thesis-restatement-redundancy (pass-7 check 7)
- check: thesis not over-restated (bar: <= 3 sections)
- verdict: NO — 4 sections assert the core verdict
- spans: S1 "Half of the loudest architecture claim ... The other half ... has no granted
  substance"; S5 "The patent claims the wiring and the lane schedule that make such
  behavior cheap. It does not claim the store."; S6 "Described, never claimed."; S7
  "One Leg Substantiated, One Leg Absent" (entire section).
- recommendation: cut or fold the S5 coda (its "does not claim the store" duplicates S6's
  "Described, never claimed" one section later); S5 can end on the [0267]/[0278]
  distributed-tensor evidence and let S6 draw the conclusion once.

### sa3B-F7 — low — internal overcount of independent-claim trades
- check: technical-claim audit (rhetorical precision)
- verdict: STRETCHES (minor)
- span: "Three independents, three different trades of breadth for structure, and none of
  them mentions memory."
- evidence: by the essay's own preceding sentences, claims 1 and 14 make the same trade
  (four-or-more floor + negative limitation), packaged at group vs system level; only
  claim 18 trades differently.
- recommendation: narrow ("Three independents, two distinct trades of breadth for
  structure" or drop "three different"). "None of them mentions memory" HOLDS.

## 7. Persona verdict

This essay survives a hostile practitioner read unusually well: every claims-scope
statement I audited against the granted claims HOLDS except two rhetorical stretches, all
blockquotes are character-verbatim, the gather/reduction family-assignment subtlety (claim
labels vs [0140]'s worked example) is handled more carefully than most litigation
summaries, and the firm verdict is exactly evidence-proportionate in both directions. The
one sentence I would attack in a reply thread is "like the scheduling claims (8, 9, 11),
binds only traffic routed the claimed way, a firmware choice" — it mislabels dependent
claims as traffic-only and tees up "your fence's non-generic element is firmware-avoidable"
against the essay's own fence paragraph (sa3B-F1).

Finding count: 0 critical, 0 high, 1 medium, 6 low. No finding touches the verdict's
direction or firmness; every recommended fix is anchor/narrow/label/cut, none is a hedge.
