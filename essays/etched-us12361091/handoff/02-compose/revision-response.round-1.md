<!--
  handoff/02-compose/revision-response.round-1.md
  Produced by: essay-en-composer (revision mode, references/revision-mode.md)
  Consumed by: editorial-review round 2 (re-review protocol) + _shared/scripts/check_run.py
  Source findings: handoff/03-edit/edit-log.round-1.md (17 findings: 3 high, 7 medium, 7 low)
  Gate context: gate-result.round-1.json all 13 gates PASS; no failing check_ids to
  disposition. Warn-only items (1x STRUCT-004, 9x LONGSENT-001) handled only where a
  finding made them real work (r1-F7 cut removes one parser-merge LONGSENT hit); parser
  artifacts not chased, per reviewer instruction.
-->

# Revision response — round 1

draft_version: 2

## r1-F1 (high, pass-4)

- disposition: applied
- change: Lead ¶1 recast in halves-of-the-memory-claim vocabulary per the reviewer's
  proposed wording; "pillar" is now reserved for LVI/CSM throughout.
  Before: "One of the thread's two architecture pillars already has a granted US patent
  standing behind it. The other pillar, the shared memory pool that gives Cluster-Scale
  Memory its name, has no granted substance in the filings you can read today."
  After: "Half of the loudest architecture claim in the thread already has a granted US
  patent standing behind it. The other half, the shared memory pool that gives
  Cluster-Scale Memory its name, has no granted substance in the filings you can read
  today."
  Coherence extension (volunteered, same vocabulary system): §1 ¶3's pillar definition no
  longer uses "half" for the pillars, so halves-vocabulary belongs only to the CSM split —
  "Low-Voltage Inference is the power half. Cluster-Scale Memory... is the half that
  pulled readers in" became "Low-Voltage Inference is the power pillar. Cluster-Scale
  Memory, or CSM, is the one that pulled readers in". §6's "The thread's other pillar"
  (= LVI) now reads against a clean pillar definition. BLUF stays declarative; the firm
  split is unchanged; title/§7 scope now match ¶1.
- location: §1 ¶1 sentences 2-3; §1 ¶3 sentences 2-3

## r1-F2 (high, pass-3)

- disposition: applied
- change: Grounding fix priority = narrow + better anchor (no hedge). The false document
  absolute is narrowed to the claims-level absolute (which the reviewer verified against
  claims 1-23 and the lead sentence already carries), and the description's other memory
  mention is absorbed on the reviewer-verified [0133] anchor, strengthening the boundary
  beat per the reviewer's option (a).
  Before: "The only memory in the patent is a labeled rectangle: FIG. 6 shows a host, two
  tensor parallel groups, and a memory 630 whose role is to 'provide tensors and other
  data to the tensor parallel groups 620 for processing' [0119]. It is an embodiment
  detail, described once and claimed never."
  After: "In the description, memory is scenery. FIG. 6 shows a host, two tensor parallel
  groups, and a memory 630 whose role is to 'provide tensors and other data to the tensor
  parallel groups 620 for processing' [0119]. The description also lets each chip couple
  to memory devices, shared among the chips or not, and no claim picks that option up
  [0133]. Described, never claimed."
  [0133] use is Phase-1-traceable (Claim scope map, claim 1 "Leaves open: memory
  attachment [0119], [0133]"; anchor reserved for §6 per phase2-handoff-notes §b); the
  shared-or-not modality stays permissive (no option-to-lock drift). Spillover fixed at
  the same time: the FIG. 6 caption repeated the same false absolute ("the patent's only
  memory") and now reads "box 630, the memory that feeds the tensor parallel groups,
  described in one embodiment figure and never claimed [0119]." The memory-leg verdict is
  untouched.
- location: §6 ¶3 + FIG. 6 caption

## r1-F3 (high, pass-3)

- disposition: applied
- change: Necessity claim narrowed to the patent's own design, per the spine mitigation
  ("exactly the wiring discipline its CSM math needs") and the reviewer's first option.
  Firmness kept; no hedge.
  Before: "...and the balanced-channel arithmetic the description builds on it [0168],
  [0061] is the wiring discipline any cluster-scale memory story would have to run on."
  After: "...and the whole fence is the wiring discipline the patent's own cluster-scale
  arithmetic runs on [0168], [0061]."
  This also removes the tension with §3's switched-fabric foil (a pool can run on a
  switch) and stops un-conceding the thin-moat steelman.
- location: §6 ¶2 sentence 3

## r1-F4 (medium, pass-3)

- disposition: applied
- change: Restored the spine's narrower claim (mitigation wording: "the latency adjective
  was never claimable as such") in place of the false general statement about apparatus
  claims; the hop-bound punch and its colon (reviewer-designated keeper) survive, with the
  bound tied to claim 1 per the reviewer's example.
  Before: "A latency figure was never going to sit in an apparatus claim. A hop bound can,
  and it does: at most one device between any two chips, ever [0387]."
  After: "The thread's adjective was never claimable as such. A hop bound is, and claim 1
  sets one: at most one device between any two chips, ever [0387]."
- location: §6 ¶2 sentences 4-5

## r1-F5 (medium, pass-4)

- disposition: applied
- change: Punchline narrowed to what structure locks vs what the prescribed split
  supplies, per the reviewer's recommended shape (comma-and instead of semicolon; the
  claims 3-5 parenthetical not repeated because sentence 3 of the same paragraph already
  carries it).
  Before: "No link runs hot, and nothing about that depends on scheduling software. It is
  wired in."
  After: "No link runs hot. The equal channels are wired in, and the equal traffic follows
  from the split the description prescribes [0168]."
- location: §4 final paragraph, last two sentences

## r1-F6 (medium, pass-4)

- disposition: applied
- change: Closing binary test recast as match/no-match against claim 1 (the reviewer's
  core version; the optional switch-fabric clause not re-added, to keep the test strictly
  binary). Closing-binary-test posture preserved.
  Before: "either the chips hang off a switch fabric, or they are wired chip to chip in
  claim 1's cross-set pattern [0386]"
  After: "the wiring either matches claim 1's cross-set pattern [0386] or it does not"
- location: §7 ¶2 sentence 4

## r1-F7 (medium, pass-7)

- disposition: applied
- change: Cut §1 ¶4's closing restatement, exactly as recommended; ¶4 now lands on "None
  of its claims mention latency, a bandwidth magnitude, or memory." The split-verdict
  statement count drops to three sections plus the verdict (§1 ¶1, §5, §6, §7), each doing
  local work.
  Cut: "Held against each other, the two documents split the CSM story cleanly in two."
  (Side effect: removes one of the parser-merge LONGSENT-001 warns.)
- location: §1 ¶4 final sentence

## r1-F8 (medium, pass-2)

- disposition: applied
- change: Hop bound now stated once in §6 — dropped "the at-most-one-intermediate
  guarantee [0387]," from the fence list, leaving three elements; the full-strength
  restatement two sentences later ("A hop bound is, and claim 1 sets one: at most one
  device between any two chips, ever [0387]") is the section's single carry, exactly as
  recommended.
- location: §6 ¶2 sentence 2 (fence list)

## r1-F9 (medium, pass-1)

- disposition: applied
- change: Broke seven colon pivots body-wide (roughly a third of the ~22 counted),
  keeping the reviewer-named strongest (claim-1 lead-in "...a group of AI chips:", the
  hop-bound pivot, §7's verdict pivots) and quotation lead-ins:
  1. §2: "visible inside this patent's own text: the specification..." -> period split.
  2. §3: "(In graph-theory terms: ...)" -> "(In graph-theory terms, this is ...)".
  3. §3: "The wire count stays modest: 16 channels..." -> period split ("The eight-chip
     drawing gets by with 16 channels...").
  4. §4: "Disjoint lanes make simultaneity cheap: claim 9..." -> period split.
  5. §4: "Claim 11 names the pair: a reduction and a gather." -> comma apposition.
  6. §6: "The only memory in the patent is a labeled rectangle: ..." -> removed by the
     r1-F2 rewrite.
  7. §6: "narrower than the description's framing: the specification's summary..." ->
     period split.
  Deviation, argued: the finding's example instance "Uniformity is claimed as structure
  too:" is KEPT — converting it pushes §4's final paragraph to 8 sentences
  (STRUCT-001 / Pass 2C band, and the recount rule in revision-mode.md). The finding's
  stated target (no more than one colon pivot per paragraph) is met there: the
  paragraph's only other colon is a full-sentence quotation lead-in. Post-edit count: 20
  body colons total, 9 of them quotation/blockquote lead-ins, leaving ~11 true pivots in
  ~1,700 words of body prose (one per ~155 words, from one per ~77). One paragraph still
  carries two non-quotation pivots (§6 ¶2: the fence-list introduction and the hop-bound
  pivot) — both are in the finding's keep-the-strongest class, the hop-bound one by name.
- location: body-wide (7 conversions listed above)

## r1-F10 (medium, pass-5)

- disposition: applied
- change: Both flagged paragraphs split at the recommended seams — §2 ¶2 after "...the
  model-level execution those moves add up to." (trio identity | commitment signal) and
  §6 ¶6 after "...that the thread folds into CSM." (what is absent | what that absence
  means today). Post-split recount per revision-mode.md: all body paragraphs sit in the
  3-7 sentence band (§2 = 4+5 after the r1-F11 gloss split; §6 tail = 3+4); no figure
  reference orphaned; marginal paragraphs (§6 ¶2, §7 ¶1) untouched as noted-no-action.
- location: §2 ¶2; §6 ¶6

## Low findings sweep (r1-F11 through r1-F17)

All seven applied — none was expensive:

- r1-F11: PCT/continuation gloss split per recommendation — "Etched is paying to keep all
  three alive: a PCT filing extends each abroad, and a US continuation, published in 2026,
  keeps each open at home. This one's expected term runs to October 2044." (continuation
  no longer filed under the beyond-US umbrella).
- r1-F12: "granted 15 July 2025, 266 days later" -> "granted 15 July 2025, inside nine
  months" (translated unit, arithmetic class); the 266-day computation moved to the
  derived-counts footnote so the attribution survives. No unanchored pendency baseline
  added.
- r1-F13: header caption re-anchored — cross-pair + no-wire-inside sentence now cites
  [0128], [0129]; [0125] moved to the families-overlaid sentence it actually supports.
- r1-F14: "...then an MLP [0252], then hand off to decoding, the token pick [0259]" —
  decoding block 930 no longer attributed to what the 905 layers "run"; [0259] is in the
  Phase-1 reference-number table for 905/930.
- r1-F15: "...and the same amount crosses each channel [0168], [0178]" — second family's
  mirror anchor added from the Phase-1 anchor set.
- r1-F16: cut "and precision matters here" (the store/movement distinction that follows is
  the precision).
- r1-F17: "The relay does not even hold the message" -> "The relay need not even hold the
  message" — option restored to modality ([0143] capability, not property); kept the
  since-clause form rather than the suggested colon form to avoid adding a pivot (r1-F9).

## Volunteered changes (beyond findings)

- §1 ¶3 pillar-vocabulary alignment (recorded under r1-F1 above).
- FIG. 6 caption narrowed (recorded under r1-F2 above); FIG. 7C caption re-anchored
  (r1-F13). Both caption transcriptions synced into figures-rationale.md; placements,
  roles, and the six-figure set unchanged.
- thesis-trace.md refreshed: draft_version 2, per-section word_actual recounts, [0178]
  added to §4's anchor list, [0259] to §5's, and the §2 exam-period presentation note
  ("inside nine months", 266 days in footnote).
- [^derived-counts] footnote reworded to carry the 266-day computation (r1-F12).
- Nothing else moved: verdict section ¶1 and ¶3 are byte-identical to round 1; the
  steelman concession, the bold thesis anchor, the anti-hype guard, and all blockquotes
  are untouched.
