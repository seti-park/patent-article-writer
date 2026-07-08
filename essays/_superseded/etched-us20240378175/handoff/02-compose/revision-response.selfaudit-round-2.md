# Revision response — post-acceptance self-audit round 2 (surgical)

draft_version: 5  <!-- the version this revision produced (v4 -> v5) -->
inputs: selfaudit-round-2-grounding.md (dry; sa2G-F1 informational), selfaudit-round-2-readerA.md
(sa2A-F1..F7, all low), selfaudit-round-2-readerB.md (sa2B-F1 medium, sa2B-F2..F7 low).
multi-vote convergences: "mirrored word for word" (sa2A-F2 + sa2B-F3, 2/2 readers);
FIG. 7 Time-A anchor (sa2G-F1 + sa2B-F7); verdict echo count (sa2A-F7 + sa2B-F6).
Scope: surgical — §7 call sentence and landing untouched; no structural edits.

## sa2B-F1 (medium — adopted premise stated in essay voice)

- disposition: applied (orchestrator-arbitrated label fix)
- change: "and no single chip realistically interfaces with that much memory [0018]" ->
  "and the filing's premise is that no single chip realistically interfaces with that much
  memory [0018]". The clause now speaks in the filing's May-2023 frame, matching the
  attributed blockquote above it. Label, not hedge: no 2026 HBM-capacity adjudication
  added, verdict untouched.
- location: §3, memory-ceiling paragraph

## sa2A-F2 + sa2B-F3 (low, 2 votes — "word for word" off by one word)

- disposition: applied
- change: "mirrored word for word in the filing's own summary" -> "mirrored almost word for
  word in the filing's own summary" (claim 39 "wherein" vs [0016] "where"). The [0016]
  blockquote below it remains verbatim.
- location: §4, claim-39 lead-in

## sa2B-F2 (low — conditional strengthened)

- disposition: applied
- change: "the filing puts the result at '98% or greater utilization of the systolic array'
  [0057]" -> "the filing says the result can still be '98% or greater utilization of the
  systolic array' [0057]" — restores [0057]'s "may... still result in" shape ("can still
  be") while keeping the number and the verbatim fragment.
- location: §5, pipelining paragraph

## sa2G-F1 (informational) = sa2B-F7 (low) — FIG. 7 Time-A clause needs [0056]

- disposition: applied (initially BLOCKED upstream — no [0056] span in invention-summary.md,
  so the token would have hard-failed gate_anchors ANCHOR-001; unblocked mid-round when
  Phase 1 added the q-0056-1 Quotable span + quote-anchor-table row, gate_quotes PASS)
- change: "...at Time A a new computation has already entered while the previous one drains
  [0056]. The only idle gap is the layer-normalization stall, marked at Time B [0057]." —
  [0056] added on the Time-A clause; [0057] stays on the Time-B sentence. One-token edit
  within v5, completing round-2's applied set; gate_anchors validates the new token against
  the Phase-1 span. Caption content was already grounding-verified accurate (sub-table 3);
  this closes the citation-completeness gap.
- location: FIG. 7 caption, §5

## sa2A-F6 (low — "as drafted" rhythm tic)

- disposition: applied (3 trims of 8)
- change: cut at (1) "Claim 39 of this application asks for the opposite" ("asks for"
  carries pending status), (2) the claims-7/8 rewrite ("with claim 8 asking for several per
  top-row chip"), (3) "Claims 11 to 13 add auxiliary circuitry" (claim-content description,
  section saturated with application-era framing). Kept the load-bearing five: header
  caption, §2 definitional sentence, claim-1 "requires as drafted" scope line (scope-map
  phrasing), the AI-limitation sentence, the steelman's "claim 1 and claim 26 as drafted".
- location: §4 x2, §5

## sa2B-F4 (low — claims 7/8 joint attribution)

- disposition: applied (one clause)
- change: "Claims 7 and 8, as drafted, put HBMs on that same switchless hardwiring, several
  of them per top-row chip" -> "Claims 7 and 8 put HBMs on that same switchless hardwiring,
  with claim 8 asking for several per top-row chip" — multiplicity pinned to claim 8;
  doubles as one sa2A-F6 trim.
- location: §4, claim-family paragraph

## sa2A-F5 (low, conditional — orphan Footnotes annex)

- disposition: verified, no edit needed
- evidence: publication.md re-emitted from the v5 draft via strip_publication.py; grep for
  "Footnotes", "fact-check-log", "figure-selection": 0 hits. The annex does not ship; the
  finding's condition does not occur on the publication path.

## sa2A-F1 (low — un-glossed 32 GT/s)

- disposition: rejected (prior ruling, selfaudit-1 sa1A-F3 rejected items)
- justification: the rate sits inside a verbatim patent quote; a familiar-scale conversion
  would be a new derived comparison requiring a fact-check-log entry for a value the
  sentence itself dismisses ("a description preference, not something claim 1 requires as
  drafted").

## sa2A-F3 (low — parameters-only gloss)

- disposition: rejected
- justification: [0018]'s full "parameters and intermediate computation values" scope is on
  the page verbatim in the blockquote one line above; the gloss sentence is the essay's own
  scale illustration (footnoted `derived-comparisons`), and the sa2B-F1 fix has already
  re-attributed the clause to the filing. Single-reader low.

## sa2A-F4 (low — "Identical chips" drops "In one embodiment")

- disposition: rejected
- justification: the paragraph opens "The application's answer is composition" and
  describes the filing's layout throughout; the neighboring [0027] sentence carries the
  section's explicit embodiment label ("In the embodiment the filing describes"). A second
  per-fact embodiment tag in the same section is label clutter for a single-reader low.

## sa2B-F5 (low — claim 15 inside the "family" frame)

- disposition: rejected
- justification: per-claim wording accurate (reader's own finding: "frame-level only");
  the frame reads at section level (memory-fed top row + switchless interface). Adding the
  claim-19/20 mirrors would introduce new claim content in a surgical pass.

## sa2B-F6 = sa2A-F7 (low x2 — verdict echo count at the marginal bar)

- disposition: rejected (prior rounds adjudicated)
- justification: selfaudit-1 (sa1A-F1 medium + sa1B-F5) already cut the §4 restatement to
  reach 3 sections + title; both round-2 readers rate the residue low with the mitigation
  stated ("each restatement carries new content... reads as spine, not padding"). The S2
  "A patent application is not a patent" paragraph is the edition's load-bearing
  definitional beat; compressing it (sa2A-F7's S2-repeats-S1 half) is not a cheap surgical
  edit and risks the beat every claim discussion leans on.

## Volunteered changes (beyond findings)

- None. draft_version bumped 4 -> 5; essay-draft.md synced byte-identical to
  essay-final.md; publication.md re-emitted via strip pipeline. figures-rationale.md and
  thesis-trace.md unchanged (no placement or spine-trace movement).

## Recount after edits

- No structural edits (no split/merge/move; all changes in-sentence). Edited paragraphs:
  §3 memory-ceiling gloss sentence (paragraph 1 sentence, unchanged count), §4 claim-39
  lead-in (3 sentences), §4 claim-family (4 sentences), §5 claims-11-13 (3 sentences),
  §5 pipelining (3 sentences). All within the 3-7 band; figure tokens FIG. 1/2/5/6/7 +
  fig-05 header all present and unmoved.

## Gate self-check (post-edit)

run_gates.py on the v5 draft: 13/13 PASS — see final report for the run output.
