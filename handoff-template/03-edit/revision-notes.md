# Revision notes — <essay-id>

> **The revision-delta capture channel.** Post-acceptance human edits — the delta from the
> edit-log-applied draft to the *published* final (and any further hand-revision rounds) — are
> logged here. `pipeline-retro` normalizes each `## delta` block into
> `meta/findings-ledger.jsonl` with `origin: human-post-accept` (via
> `meta/normalize_revision_notes.py`), so the editorial blind-spots a human catches AFTER the
> loop says "pass" are no longer invisible to the meta-loop. This is what makes the system
> self-improving on the dimensions the gates/passes don't yet score. Rationale:
> `meta/improvement-proposals/2026-06-26-human-revision-blindspots.md`.
>
> One block per edit. Keys: `class` (required; a pattern_tag from `meta/attribution-table.md`),
> `round`, `before`, `after`, `rationale` — each on ONE line. The normalizer fills
> goal / owner-stage / owner-artifact from `class`. Unknown classes flag for a new
> attribution-table row.

<!-- WORKED EXAMPLE — run 045 (the channel's first real dataset: the v2 -> v2.4 hand-revision
     that ran AFTER the pipeline returned overall_assessment == pass). -->

## delta
class: lead-thesis-deferral
round: pre-v2
before: lead deferred the thesis to a question ("what fences a competitor out?")
after: para 1 states the verdict up front ("a strong claim to territory and a thin claim to technology")
rationale: BLUF / 두괄식 — the impatient diligence reader wants the verdict first, then the proof.

## delta
class: nonclaim-section-header
round: v2
before: "What '638 Actually Claims"
after: "The Claim Is a Delivery Workflow, Not a Robot"
rationale: headers must be claims so a header-only skim reconstructs the argument.

## delta
class: steelman-absent
round: v2
before: no concession that workflow-claiming is a deliberate breadth strength
after: "Claiming the workflow ... is not the patent's weakness ... a fence is not an engine"
rationale: pre-rebut the strongest pro-subject counter (concede-then-refine) instead of leaving it to the reader.

## delta
class: revision-induced-duplication
round: v2.1
before: "the tell is there from the first date" (duplicated "the clearest tell" in section 4)
after: "the timeline is the first clue" (then folded into "The idea was never the secret")
rationale: the restructure introduced a distinctive-word echo; a revision must re-scan the whole doc.

## delta
class: venue-ticker-convention
round: v2.1
before: "trading as AGLT"
after: "trading as $AGLT"
rationale: X Articles cashtag convention — native, linkable token.

## delta
class: meta-reader-instruction
round: v2.2
before: "Read it the way an examiner would" / "Everything below is the reading" / "Watch how the patent handles each"
after: removed; each beat opens with the insight instead of a stage direction
rationale: the reader buys insight, not instructions on how to read.

## delta
class: thesis-restatement-redundancy
round: v2.3
before: the two-axis verdict was stated in ~5 sections (lead, section-1 steelman, section-1 button, section-3, section-5)
after: section-3 compressed to its one fresh beat (no performance metrics)
rationale: restating the verdict in > 3 sections is bloat; keep each section's fresh contribution.

## delta
class: jargon-overdepth
round: v2.3
before: "generic computer implementation of an abstract idea is 'not significantly more'" (Alice doctrinal quote)
after: cut the doctrinal quote; kept the short "Section 101 / Alice" signposts
rationale: keep the term-of-art the diligence reader scans for; drop the deep-dive only a specialist needs.

## delta
class: section-stub-imbalance
round: v2.4
before: compressed section-3 was a 4-sentence stub between larger sections
after: merged section-3 + section-4 into "The Territory Is Not the Moat"
rationale: a section far shorter than its siblings is a rhythm break; merge or expand.
