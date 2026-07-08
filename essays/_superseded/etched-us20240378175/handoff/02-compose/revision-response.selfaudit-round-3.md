# Revision response — post-acceptance self-audit round 3 (single-fix, at cap)

draft_version: 6  <!-- the version this revision produced (v5 -> v6) -->
inputs: selfaudit-round-3-grounding.md (sa3G-F1), selfaudit-round-3-readerA.md
(sa3A-F1..F4, all low), selfaudit-round-3-readerB.md (sa3B-F1..F4, all low).
Round shape: 0 critical / 0 high / 0 medium across all three auditors; both readers report
all pass-7 checklist items PASS and no 6G finding. Orchestrator arbitration: apply the one
grounding-verifier-prescribed citation fix (sa3G-F1, source unblocked by Phase 1's q-0055-1
span); reader lows considered-not-applied at cap.

## sa3G-F1 — FIG. 7 stage-name clause rode on [0056]

- disposition: applied
- change: citation split at the clause boundary in the FIG. 7 caption: "Attention queries,
  keys, and values, projection, and the MLP layers follow each other through the row
  [0055], and at Time A a new computation has already entered while the previous one drains
  [0056]. The only idle gap is the layer-normalization stall, marked at Time B [0057]." —
  stage list anchored to [0055] (its actual source), Time-A clause keeps [0056], Time-B
  sentence keeps [0057]. Applied once Phase 1 added the q-0055-1 Quotable span +
  quote-anchor-table row (gate_quotes PASS); gate_anchors validates the new token. Caption
  wording unchanged; reader B verified the legend order against fig-07.png and
  [0055]-[0057] this round.
- location: FIG. 7 caption, §5

## Reader lows — considered, not applied (at cap; one-line reasons)

- sa3A-F1 (un-glossed "32 GT/s"): rejected — third raise, prior ruling stands (sa1A-F3,
  sa2A-F1): the rate sits inside a verbatim patent quote and a familiar-scale conversion
  would need a new derived-comparison log entry for a value the sentence itself dismisses.
- sa3A-F2 (header-caption "IC"/"systolic array" cold for captions-first readers): rejected —
  prior ruling (sa1A-F3 rejected items): the header composite's topology-first role stands,
  and the reader's own report notes the plain framing ("No switch, no crossbar, nothing
  between memory and math") mostly rescues it.
- sa3A-F3 (shrink call lacks the survival call's basis label): rejected — the shrink call
  already names its evidential basis in-sentence ("sits closest to the examiner-cited
  multi-node art"); a second explicit label in the paragraph carrying the single anti-hype
  guard is label clutter, not added precision.
- sa3A-F4 ("formal no" gloss may read terminal to a lay reader): rejected — any fix must
  live inside the single budgeted label sentence, whose existing RCE gloss ("a paid restart
  that keeps the argument alive") plus the falsifier paragraph already restore the two-way
  frame, per the reader's own mitigation note.
- sa3B-F1 ("no program counter... no scheduler" is the essay's own gloss of [0027]):
  rejected at cap — technically sound inference sitting directly after the labeled
  embodiment quote (reader's own assessment); the labeling tweak is real but is a new prose
  edit outside this round's single arbitrated fix.
- sa3B-F2 ("Identical chips" unmarked embodiment detail): rejected — repeat of sa2A-F4,
  prior ruling stands: the neighboring [0027] sentence carries the section's explicit
  embodiment label; a per-fact tag is label clutter for a single-reader low.
- sa3B-F3 (numeral 250 rides [0019], which lacks the numeral): rejected at cap — the
  concept is [0019]'s and the claim is true and one paragraph-hop verifiable (reader's own
  assessment); re-anchoring the numeral-bearing clause is a candidate for a future round,
  not this one's single fix.
- sa3B-F4 (claim 15 under the "switchless family" umbrella without claim 19): rejected —
  repeat of sa2B-F5, prior ruling stands: per-claim wording is accurate ("coupled"), and
  citing claim 19/20 introduces new claim content in a post-acceptance surgical pass.

## Volunteered changes (beyond findings)

- None. draft_version bumped 5 -> 6; essay-draft.md synced byte-identical to
  essay-final.md; publication.md re-emitted via strip pipeline. figures-rationale.md and
  thesis-trace.md unchanged (no placement or spine-trace movement).

## Recount after edits

- No structural edits (one caption citation split; no split/merge/move of paragraphs).
  FIG. 7 caption remains 3 sentences; all figure tokens (fig-05 header + FIG. 1/2/5/6/7)
  present and unmoved; paragraph bands unchanged from v5.

## Gate self-check (post-edit)

run_gates.py on the v6 draft: 13/13 PASS — see final report for the run output.
