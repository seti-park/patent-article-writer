# Revision notes — 2026-06-26-us12560948b2-investor-selfaudit

> **The revision-delta capture channel, run AUTONOMOUSLY.** This file is the same `## delta`
> schema the human-post-accept channel uses (`handoff-template/03-edit/revision-notes.md`), but
> the edits below were proposed and applied by the **self-audit loop itself**, not a human. After
> the inner Compose↔Edit loop returned `overall_assessment == pass` and all ten deterministic
> gates were green with zero findings, a fresh-context adversarial pass (the pass-7 personas,
> run in separate contexts with no commitment to the draft) found the editorial and grounding
> blind-spots the loop's own passes missed, and a second round verified convergence.
>
> Normalized with `origin: self-post-accept` / `source: self-audit` (vs the human channel's
> `human-post-accept` / `human-revision`, vs the inner loop's `inner-loop`). The distinction
> matters to `pipeline-retro`: `inner-loop` = "a pass should have caught this"; `self-post-accept`
> = "no pass scored this dimension yet, but the model caught it adversarially without a human";
> `human-post-accept` = "only a human caught it." Each motivates a different fix.
>
> Run shape: v1 = the loop-PASSED `essay-final.md`. v2 = round-1 fixes (8 adversarial findings).
> v2.1 = a self-introduced echo the dupe gate caught on re-run. v2.2 = round-2 multi-vote fixes
> (2 reviewers). v2.3 = a round-3 confirmation pair on the final draft, which caught two off-by-one
> paragraph anchors traced to the Phase-1 invention-summary and fixed them at the source. Final
> v2.3 passes all 10 gates with 0 findings and the anchor chain intact; both fresh reviewers call it
> publishable, with the round-1 high/medium all resolved.
> One block per edit; keys (`class` `round` `before` `after` `rationale`) each on ONE line.

<!-- ROUND 1 — fresh-context adversarial pass on the loop-PASSED v1 (1 high + 6 medium + a
     claim-scope grounding slip the loop's pass-3 missed). Applied autonomously to v2. -->

## delta
class: nonclaim-section-header
round: v2
before: noun-phrase labels ("What The Body Forces", "What Claim 1 Locks", "How Wide Is The Moat", "Why It Matters Now", "What This Patent Does Not Do", "The Investor Read")
after: every header an assertion ("The Body Rules Out Both Standard Safety Answers", "Claim 1 Locks A Rising-Risk, Clearance-Gated Drop", "Most Ways Around It Make A Worse Robot", "The Safe Stop Is The Deployment Gate", "One Method Claim In A Crowded Field", "A Real But Bounded Moat")
rationale: a header-only skim must reconstruct the argument; pass-7 check 2, the round-1 HIGH.

## delta
class: lead-thesis-deferral
round: v2
before: lead closed on "It does not patent walking. It patents how the robot comes to rest." (verdict implied, not stated)
after: inserted the declarative verdict before the close: "It reveals a real but bounded moat."
rationale: BLUF / 두괄식 — the impatient diligence reader wants the moat verdict in paragraph 1; pass-7 check 1.

## delta
class: claim-scope-misattribution
round: v2
before: the fall-extent reduction "by at least 30%, by at least 50%" [0029] "is pinned only as far as claim 13 commits it" (implies claim 13 commits the whole range)
after: "claim 13 commits only to 'at least 50%'; the 'at least 30%' figure sits in the description [0029] and binds nothing on its own"
rationale: claim 13 reads "by at least 50%"; the 30% is description-only. Crediting a claim with a spec-only number is the most damaging class in the system — the grounding slip the loop's pass-3 missed and the fresh pass caught.

## delta
class: venue-ticker-convention
round: v2
before: "expected to trade on Nasdaq as AGLT"
after: "expected to trade on Nasdaq as $AGLT"
rationale: X Articles cashtag convention on first ticker mention — native, linkable token; the gate's regex did not fire on "trade on Nasdaq as", so this is a judgment-layer catch.

## delta
class: legal-posture-language-slip
round: v2
before: "something Agility is actively claiming as its own" / "the part Agility has moved to own"
after: "something this filing actively claims" / "the part Agility has moved to protect"
rationale: owning a patent is not owning the capability or the market; "claim as its own" / "own" overstates what a filing does. Protecting/claiming is exact.

## delta
class: steelman-absent
round: v2
before: the limits section listed weaknesses without ever stating the strongest bear case at full strength
after: "The bear case is that this is one method claim in a crowded field, easy to step around, and it is the right worry, the reason the moat is bounded rather than absolute. Where it overstates is in 'easy to step around': ..."
rationale: concede the single strongest pro-skeptic counter at full strength, then refine; pass-7 check 3.

## delta
class: meta-reader-instruction
round: v2
before: the limits section opened "Honesty about the limits is what makes the rest credible." (a claim about the essay's own rhetoric)
after: opened on substance — "The limits are real." then straight into the bear case
rationale: the reader buys insight, not commentary on the essay's credibility strategy; pass-7 check 4.

## delta
class: figure-caption-scope-deferral
round: v2
before: FIG. 5 caption put the claim-scope disclaimer LAST ("...compact kneel. One embodiment of the locked step. Claim 1 requires lowering a center-of-gravity, not this exact choreography.")
after: scope disclaimer moved FIRST ("FIG. 5A-5AD. Claim 1 requires lowering a center-of-gravity, not this exact choreography; the sequence is one embodiment of the locked step. It runs in the patent's four phases...")
rationale: a caption-only skimmer must get the scope discipline before the choreography, so the striking visual never reads as "the claim."

<!-- ROUND 2 — gate re-run + a SECOND fresh-context pair (multi-vote). v2.1 is a regression the
     dupe gate caught on the round-1 output; v2.2 are the two findings both reviewers agreed on. -->

## delta
class: revision-induced-duplication
round: v2.1
before: the round-1 steelman ended "...so the cheap ways around it tend to build a worse robot" — a 5-gram echo of the verdict section's "so the cheap ways around it tend to produce a more dangerous or less productive robot"
after: reworded to "...it is anchored to the physics of a fault, not to one arbitrary pose."
rationale: a round-1 fix introduced its own distinctive-phrase echo; the dupe gate (DUPE-001, warn) caught it on re-run — mechanical layer backstopping the judgment layer's own edit.

## delta
class: prosecution-record-overstatement
round: v2.2
before: "The examiner allowed this filing over directly adjacent work, including a 2021 framework... Clearing that art is a real positive signal..."
after: "Among the references of record, disclosed by the applicant itself, are three directly adjacent works: ... The claims issued with that art on the record, which is a real positive signal..."
rationale: the three papers are "cited by applicant", not documented examiner-applied rejections; "allowed over" overstates the prosecution record. Flagged low by reviewer A, medium by reviewer B — applied on the majority and the higher severity.

## delta
class: anchor-incomplete
round: v2.2
before: FIG. 5 caption cited "[0046]" for "the patent's four phases", but phases 3-4 (the 5W and 5AD frames) are described in [0047]
after: cited "[0046]-[0047]"
rationale: the anchor must cover every frame the caption names; both [0046] and [0047] are in the invention-summary anchor set, so the range stays gate-clean.

<!-- ROUND 3 — a SECOND confirmation pair (blind) on the final draft. Caught two off-by-one
     paragraph anchors that originated in the Phase-1 invention-summary and were inherited by the
     essay; fixed at the source so a recompose would not reintroduce them. -->

## delta
class: anchor-offbyone
round: v2.3
before: the disable-switch irony was anchored [0011], but para (11) only sets up the generic E-stop; the explicit irony ("Ironically, this includes close encounters associated with accessing and activating a disabling feature") is para (12)
after: corrected to [0012] in BOTH the essay and the invention-summary Quotable span (the mislabel originated upstream; the essay inherited it)
rationale: off-by-one anchor flagged by both round-3 reviewers (C medium, D low); fixed at the source so a recompose from the handoff cannot reintroduce it.

## delta
class: anchor-offbyone
round: v2.3
before: the "Category-1 and Category-2 stops" quote was anchored [0041], but that quote is para (42); para (41) is collision-avoidance reconfiguration selection
after: corrected to [0042] in BOTH the essay and the invention-summary quote row (q-0041-1 -> q-0042-1)
rationale: off-by-one anchor inherited from the invention-summary; reviewer C caught it on spot-check. Fixed at the source.

## delta
class: anchor-incomplete
round: v2.3
before: the FIG. 3 caption anchored "the escalation the claim locks" to [0033], but FIG. 3 is introduced and walked as a decision tree in [0035]-[0039]; [0033] supports only the "standing still is safer" caveat (where the essay still cites it correctly)
after: caption anchor changed to [0035]; the [0033] cite elsewhere is kept where it is accurate
rationale: point a figure caption at the paragraph that actually describes the figure; reviewer C, low.

## delta
class: revision-induced-duplication
round: v2.3
before: the round-2 prosecution-record rewrite left "issued with the nearest adjacent art already before the examiner" (steelman) and "The claims issued with that art on the record" (next paragraph) as a near-verbatim within-section echo
after: the second occurrence trimmed to "That the patent issued anyway is a real positive signal about the novelty of the specific combination."
rationale: a round-2 fix introduced a conceptual echo across two consecutive paragraphs; reviewer D flagged it (the judgment-pass analog of the v2.1 gate_dupe catch).

# Considered and not applied (logged, not edited)

These were raised in the self-audit and deliberately NOT applied — the discipline that keeps the
loop from over-editing. The system's rubric gates OVERREACH, not OVER-HEDGE; a finding both
reviewers did not agree on, or that does not survive grounding, is logged and dropped, not forced
into the draft.

- **physics-motif echo (round-3, NOT applied).** Reviewer C noted "anchored to the physics of a
  fault" (limits section) and "the claim sits on the physics of the problem" (conclusion) as a mild
  echo, but rated the check PASS ("reinforcement, not bloat"); reviewer D did not flag it. It is the
  thesis spine, within the 3-section verdict ceiling; trimming would weaken the through-line. Watch.
- **thesis-restatement-redundancy (round-2, NOT applied).** Reviewer A flagged the "bounded rather
  than absolute" refrain as heavy (low); reviewer B scored the same check PASS ("verdict in 3
  sections, within the at-most-3 limit"). No majority, and trimming would weaken the steelman
  concession, which structurally must reference boundedness. Logged as `watch`.
- **ordering-design-around (round-1 design candidate, NOT applied).** A proposed 4th competitor
  escape-route ("reorder the steps") for the physics section. On grounding check it collapses into
  existing routes 1 and 3, and [0033] is already load-bearing in the adjacent paragraph; adding it
  would be completeness-theater. Declined on grounding + non-redundancy.
- **meta-pointer cosmetics (round-2, NOT applied).** Reviewer A flagged "Read what that actually
  requires" / "the ones set out above" as mild internal pointers (low); reviewer B scored no-meta
  PASS/ABSENT. Singleton cosmetic, no majority — not applied.

## Deferred candidate criteria (need sourcing or an editorial decision, not a self-fix)

Surfaced by the personas as POSSIBLE new pass-7 criteria, but each needs external sourcing or a
taste call a self-audit should not make unilaterally. Recorded for `pipeline-retro` to weigh, not
applied:

- **competitor-naming** — name the wheeled-humanoid / biped rivals the "bipedal→mobile" reach
  forecloses (needs sourced competitor list).
- **quantified-watch-triggers** — turn the three "watch over the next year" items into numeric
  triggers (needs a defensible threshold).
- **traction-in-lead** — pull one deployment proof point (100,000 totes) into the lead (trades
  BLUF purity for concreteness; an editorial call).
- **hero-figure-choice** — test FIG. 3 (the decision tree, the literal picture of the claimed
  escalation) against FIG. 5 as the cover (a visual-force vs claim-literalness judgment).

## Round map

| round | trigger | findings | applied |
|---|---|---|---|
| v1 | inner Compose↔Edit loop | `overall_assessment == pass`, 10/10 gates 0 findings | (baseline) |
| v2 | round-1 fresh-context pair (2 reviewers, multi-vote) | 1 high + 6 medium + 1 grounding slip | 8 fixes |
| v2.1 | dupe gate re-run on v2 | 1 self-introduced 5-gram echo (warn) | 1 fix |
| v2.2 | round-2 fresh-context pair (2 reviewers, multi-vote) | 0 high, 0 medium of the round-1 classes; 2 agreed lows (1 medium per B) | 2 fixes |
| v2.3 | round-3 confirmation pair on final v2.2 | 0 high; 2 medium + 2 low (two off-by-one anchors traced to the invention-summary, 1 caption anchor, 1 within-section echo) | 4 fixes (2 at source) |
| final | 10-gate re-run + anchor-chain check | 0 gate findings; anchor chain intact; both reviewers "publishable as-is" | converged |
