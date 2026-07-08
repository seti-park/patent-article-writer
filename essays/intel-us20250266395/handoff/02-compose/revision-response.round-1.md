# Revision response — round 1

draft_version: 2

## r1-F1

- disposition: applied
- change: Narrowed the universal negative to the anchor's scope per the grounding fix
  priority (narrow, not hedge). "Then comes the half no shipped bridge flow contains" is now
  "Then comes the half Intel's shipped bridge flow does not contain, the test-and-commit
  order:" — resting on fact-check-log `emib-chips-last-flow` (tier-2), which supports exactly
  the Intel-shipped-EMIB chips-last claim and nothing industry-wide. Sentence force preserved;
  §5's parallel formulation already used the narrow form.
- location: §2, sentence introducing the second blockquote

## r1-F2

- disposition: applied
- change: FIG. 8 caption reworded so numeral 882 attaches to the solder bumps, strictly per
  the invention-summary reference table row for `[0056]` ("882/982 | solder bumps, dies to
  substrate top surface"): "the dies land across the substrate top on solder bumps (882)".
  872 (bridge) and 860 (underfill) untouched. Same fix mirrored into
  `figures-rationale.md`'s "Caption (as written)" record for FIG. 8 so the placement log
  matches the draft.
- location: §4, FIG. 8 caption

## r1-F3

- disposition: applied
- change: Cut "face-down": the plain-English method sentence now reads "set two chips on a
  temporary carrier, mold them into one rigid piece...". Orientation was not load-bearing.
- upstream flag (fix-at-source): the drift originated in
  `handoff/01-design/invention-summary.md` Layer 2 step 1, which reads "Assemble a first IC
  die and a second IC die **face-down** on a carrier" — per the reviewer's grep of patent.md,
  "face-down" appears nowhere in `[0060]`/`[0061]`/claim 19. Orchestrator should have Phase 1
  correct the Layer-2 mechanism text, or a future recompose reintroduces it.
- location: §2, paragraph 1

## r1-F4

- disposition: applied
- change: Kept the (true) sentence and made the Example/claim divergence explicit at the
  anchor, per fix priority (anchor first) and the Claim scope map's own instruction
  ("attribute breadth to the Example, not the claim"). Final form after gate self-check
  (LONGSENT-001 warn on the single-sentence version, then STRUCT-001 on the 8-sentence
  paragraph it created): "...not off the cavity packages described above. The parallel
  Example paragraph is written broader [0138]. The claim as filed is not." — with the §5
  dissection paragraph split at the beat seam (claim-17 scope / no-single-claim + EMIB-absence
  synthesis; 4 + 4 sentences). A skeptical reader who follows [0138] now finds the divergence
  named rather than an apparent contradiction. "described above" also absorbs r1-F14's first
  recastable self-reference.
- location: §5, paragraph 2

## r1-F5

- disposition: applied
- change: Both reader-instruction spans recast declaratively, cadence checked against the
  canon entries already on trace. §1: "So read it two-sided from the start:" is now "That
  cuts two ways. This is the most concrete piece of after-EMIB-T assembly thinking on the
  public record. It is also a pending application: ..." (two-sided call intact, lands at
  lead end). §2: "Hold on to what just happened there:" is now "That one step moves the
  dividing line:" staging the unchanged bold anchor as a claim, matching
  `inline-bold-thesis-anchor-etherloop-steady-state`'s declarative build.
- location: §1 paragraph 2 (now 2b), §2 bold-anchor line

## r1-F6

- disposition: applied
- change: Guard re-pointed at this filing using the spine's own sanctioned wording (thesis-
  spine closing directive: "nothing here schedules a product"): "It is one pending
  application, and nothing in it schedules a product." Weight unchanged, budget stays at
  exactly one guard, no caveat added; closing_posture remains firm.
- location: §6, paragraph 2, first sentence

## r1-F7

- disposition: applied
- change: Both medium-severity paragraphs split at the reviewer's seams. §1 ¶2 splits after
  "(Google Patents)." — gloss + EMIB-T context + bibliographic in ¶2a (4 sentences), the
  reading + two-sided call in ¶2b (4 sentences, call still inside the lead section; 6A/6H
  unaffected). §4 EMIB paragraph splits after "(IEEE ECTC paper; see Sources)." — caution +
  shipped-flow in one paragraph (3 sentences), chips-last consequence + EMIB-T + this
  filing's inversion in the next (3 sentences). The two quote-integrated paragraphs the
  finding demotes to low (§2 ¶3, §4 glass paragraph) are left intact: their inline verbatim
  quotes + anchors are the seam-breakers, and splitting them would orphan quote from
  interpretation (quote-interpretation adjacency rule). All neighboring paragraphs re-counted
  after the splits: every prose paragraph sits in the 3-7 sentence band; no figure token
  orphaned.
- location: §1 ¶2, §4 EMIB-comparison paragraph

## r1-F8

- disposition: applied
- change: Rewrote as the reviewer's first variant: "and its impressive numbers do not sit
  where the previous sections may have left the impression they do." The second variant
  ("are not in the claims") was NOT used: claim 17 as filed carries an exact numeric range
  (20 µm-1.4 mm, Claim scope map), so "not in the claims" would trade a grammar defect for a
  scope overstatement. Also absorbs r1-F14's second recastable self-reference.
- location: §5, paragraph 1, second sentence

## r1-F9 (low)

- disposition: applied
- change: Dual anchor "[0060], [0061]" on the plain-English method sentence — the
  carrier/mold steps (1102/1104) live in `[0060]` per the invention-summary Layer-2
  mechanism; `[0061]` keeps covering detach/bridge-attach.

## r1-F10 (low)

- disposition: applied
- change: "the one quantified-effect sentence" → "the one stated-effect sentence in the
  document" (the [0035] effect sentence contains no quantity; design artifacts call it the
  only stated yield/effect sentence).

## r1-F11 (low)

- disposition: applied
- change: §1 ¶1 split so [0142] anchors only the patent half: the shipped-flow contrast is
  now its own unanchored sentence ("In the flow Intel ships today, the little bridge die is
  buried in the board, and the chips land on top." — content per emib-chips-last-flow,
  sourced with label in §4), followed by "The filed method bonds the bridge straight onto
  the chips first, then tests the whole cluster before a board ever enters the picture
  [0142]." No EMIB term rides a [dddd] anchor.

## r1-F12 (low)

- disposition: rejected
- justification: Orchestrator instruction on the intake flag: it is FACTUALLY WRONG — the
  patent snapshot DOES contain claim 20 (final line of the claims section,
  method-of-claim-19 + cavity). The draft's "one dependent claim away, 'placing the bridge
  component in the cavity' [0144]" is verifiable against the snapshot and matches the Claim
  scope map row for claim 20. No weakening applied; recorded here per orchestrator note.

## r1-F13 (low)

- disposition: applied
- change: Time reference re-attached to the rollout per emib-package-roadmap-120mm: "Intel
  has discussed rolling out EMIB packages up to roughly 120 by 120 millimeters from 2026,
  carrying as many as twelve HBM memory stacks plus compute chiplets (single-outlet report;
  see Sources)."

## r1-F14 (low)

- disposition: applied
- change: Both recastable self-references removed via the r1-F4 ("the cavity packages
  described above") and r1-F8 rewrites. The three functional attribution labels the finding
  exempts are untouched.

## r1-F15 (low)

- disposition: rejected
- justification: The proposed comparison ("a human hair is about 70 microns across") is an
  external factual claim with no fact-check-log entry; `references/execution-boundary.md`
  forbids fact introduction beyond invention-summary spans + fact-check-log external facts
  in ALL modes, revision included. Reader-profile rule 2 applies "when the magnitude carries
  the point" — here the draft deflates the number's claim status one clause later, which the
  finding itself notes as the mitigator. Upstream option for the orchestrator: if a
  familiar-scale comparison is wanted, Phase 1 adds a logged tier-4 entry for hair-width and
  round 3 can take it in one clause.

## r1-F16 (low)

- disposition: applied
- change: Substrate glossed at first §1 use: "embedded in the package substrate, the
  board-like base the whole package is built on." Used freely thereafter.

## r1-F17 (low)

- disposition: rejected
- justification: Resolving the ECTC entry to its real title and authors requires fetching
  the ieeexplore record — information not present in any Phase-1 artifact (fact-check-log
  carries only the URL and a claim summary). The composer's source fence and
  execution-boundary forbid introducing externally fetched material in revision. Flag
  upstream: Phase 1 (or the orchestrator) should enrich the `emib-chips-last-flow` /
  `emib-t-ectc-2025` log entries with the paper's bibliographic fields; the Sources entry
  then updates mechanically.

## r1-F18 (low)

- disposition: applied
- change: Cut "And the names on it are not a side project." The Mahajan sentence now opens
  the beat directly; paragraph re-counted (6 sentences).

## Volunteered changes (beyond findings)

- `figures-rationale.md`: FIG. 8 "Caption (as written)" record synced to the r1-F2 caption
  fix (no placement, role, or rendering change).
- `thesis-trace.md`: §2 `paragraph_anchors_used` gains `[0060]` (r1-F9); §1/§5 word_actuals
  refreshed after the splits/cuts; the coverage-check line quoting the old §6 guard wording
  updated to the r1-F6 wording. Signature lines UNCHANGED (all three verbatim intact in the
  draft).
- §5 dissection paragraph split into two (4 + 4 sentences) as part of the r1-F4 final form —
  caught by the self-check recount (STRUCT-001), not a content change.
- One micro-smoothing adjacent to r1-F10: "The stated payoff is the one stated-effect
  sentence" would have doubled "stated"; final wording is "The payoff on offer is the one
  stated-effect sentence in the document" (no factual change).
- No other prose moved.
