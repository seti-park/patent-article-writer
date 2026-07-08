---
proposal_id: 2026-07-06-steelman-two-sided
created: 2026-07-06T00:00:00Z
status: applied (2026-07-06, user-authorized, regression-gated: test_gates 111/111 + fixtures incl. new steelman-overweight; all 4 layers landed)
lever: multi (reference-edit + rubric-tuning + gate-strengthen)
goal: "4b"
root_cause_stage: design + edit
root_cause_artifact: >
  thesis-architect/references/adversarial-defense.md (§D steelman beat, "at full strength")
  + editorial-review/references/pass-7-adversarial-reader.md (check 3, one-sided steelman-absent)
  + scoring-rubric.md (steelman failure class is absent-only) + reader-energy.md /
  gate_surface (attention-budget doctrine exists but does not bind the steelman/concession beat)
recurrence_count: 2
confidence: medium
triggering_findings:
  - essay_id: intel-us20250266395
    source: human-revision (origin human-post-accept, 2026-07-06, class procedure-overweight + redundant-caveat-restatement)
    pattern_tag: steelman-overweight
    detail: >
      §5 "One Filing Among Hundreds, Except for One Claim" shipped double-clean +
      self-audit DRY + 14/14 gates, yet the owner read it as safe-harbor and low on
      net-new information. The concede beat spent a full prosecution/spend passage
      (18-months framing, JP/KR/CN/DE counterpart list, fee-money inference) and
      restated two caveats already made in §2 (pitch-is-description-only) and §4
      (EMIB-is-our-synthesis). Compressed 6→4 paragraphs; the affirmative core
      (locked order-of-operations) was unchanged, only the concession was un-elaborated.
  - essay_id: etched-us20240378175-r2
    source: human-revision (origin human-post-accept, 2026-07-05, class procedure-overweight-lead)
    pattern_tag: steelman-overweight
    detail: >
      The §5 concede/limits beat carried a full RCE explainer paragraph, a repeated-spending
      motif, and a two-paragraph lien walk. Same section, same failure shape: the concession
      out-weighed the affirmative core. Fixed by the applied procedure-attention-budget proposal,
      but that fix targets the LEAD and essay-wide spend motif, not the steelman-section ratio.
related:
  - 2026-07-05-procedure-attention-budget (APPLIED) — the attention-budget doctrine, reader-energy.md
    §6, gate_surface SURF-005/006, and pass-6 6I. This proposal EXTENDS it to the steelman beat;
    it does not duplicate it (see "Distinct from procedure-attention-budget" below).
  - 2026-06-24-conclusion-over-hedge-check → the 6G/gate_hedge two-sided verdict defense. This is
    the exact symmetry precedent: a one-sided guard (overreach-only) made two-sided (over-hedge).
    This proposal does the analogous move for the steelman (absent ↔ overweight).
---

## Headline: the steelman is the pipeline's last one-sided guard — punished when absent, never when it over-primes

The pipeline has twice made a one-sided guard two-sided, and is proud of it:

- **Verdict hedging:** pass-3/pass-4 punished overreach; `2026-06-24-conclusion-over-hedge-check`
  added the symmetric over-hedge defense (pass-6 6G + `gate_hedge`, hard-fail under firm posture).
  Overreach ↔ over-hedge.
- **Attention:** every instance was individually grounded, so no pass counted the aggregate;
  `2026-07-05-procedure-attention-budget` (applied) added the attention-budget doctrine so
  procedure/spend can no longer eat the essay unpunished. Present ↔ over-weighted.

The **steelman** has not had this treatment. Its only failure class is `steelman-absent`
(`pass-7` check 3, `scoring-rubric.md`): a missing or truism concession is punished. **Nothing
punishes a steelman that is present, specific, and correct but over-elaborated** — the concession
beat that states the objection *at full strength* (the literal instruction in
`adversarial-defense.md:108` and `pass-7-adversarial-reader.md:38`) and, in doing so, spends more
of the reader's attention on the objection than on the invention it is supposed to defend.

## The cognitive cost this leaves undefended (why "at full strength" is the wrong target)

Elaborating an objection **primes the objection**. This is the negation / framing effect — Lakoff's
"don't think of an elephant": the instruction to negate a frame activates it. A concession beat that
spends three paragraphs building the strongest case *against* the thesis, then one sentence returning
to the core, leaves the reader carrying the objection, not the invention. The affirmative core — the
one thing the essay wants the reader to leave with (goal 5's `reader_sentence`) — competes for
attention against a concession the doctrine actively told the composer to maximize.

The fix is **not** to weaken the steelman toward weak-man. Concession must stay **specific** (the
generic-truism ban holds; a THIS-patent objection is still mandatory). The fix is that concession
≠ elaboration: **state the objection once, compactly, specifically — then return to the core with at
least as much weight as the concession got, and never restate a caveat an earlier section already made.**
"Lean" here means *specific-but-bounded-and-net-new*, not brief-and-vague. This run's v6 §5 is the
proof of concept: it concedes claim-17-hangs-off-claim-16 and no-single-claim at full specificity,
and drops only the elaboration, the spend passage, and the restated caveats.

## Evidence (two runs, same section, same shape, both human-caught post-accept)

| Run | Section | What the concession over-spent | Affirmative core | Caught by |
|---|---|---|---|---|
| intel-us20250266395 (v6) | §5 | prosecution/spend passage (JP/KR/CN/DE, fee-money) + 2 restated caveats (§2 pitch, §4 EMIB-synthesis) | locked order-of-operations [0142]/[0144] — untouched | human post-accept |
| etched-us20240378175-r2 (v6) | §5 | RCE explainer ¶ + spend motif + 2-¶ lien walk | the no-switch memory thesis | human post-accept |

Both shipped double-clean, self-audit DRY, 14/14 gates, zero warns. In both, the concession beat is
the failure site, and in both the affirmative core was correct and left intact by the fix — only the
concession was un-elaborated. Within-class recurrence = **2**, same section role across two distinct
essays.

## Distinct from procedure-attention-budget (not a duplicate)

`procedure-attention-budget` (applied) binds the **lead** (SURF-005, procedure sentences before the
first tech section) and the **essay-wide** spend motif (SURF-006, count > 4). A steelman can be
overweight with **zero** spend motif and **outside** the lead — e.g., a long claim-scope dissection
that never returns to the core — so SURF-006 does not fire and SURF-005 does not reach it. The
uncovered gap is specifically the **negation/affirmative ratio inside the concession beat**, wherever
that beat sits. This proposal adds that one check and the doctrine behind it; the spend/procedure
lexicon it reuses is already defined.

## Proposed change — four layers, mirroring the over-hedge defense

**Layer 1 — Design (`thesis-architect/references/adversarial-defense.md`, §D, line ~108).**
Replace "states the objection **at full strength**, then refines" with a bounded, net-new spec:

> **Steelman beat (concede-and-return).** The beat concedes the strongest THIS-patent objection
> **once, compactly, and specifically** — then returns to the affirmative core, which must carry **at
> least as much attention (sentence/word budget) as the concession**. The concession must be
> **net-new**: it may not restate a caveat the spine already places in an earlier section (those are
> spent once, where they first land). A spend/procedure motif inside the concession beat is barred —
> it is what turns a concession into safe-harbor. Carry the concession:core ratio target into
> `phase2-handoff-notes`.

Add the rationale (the negation-priming cost) as a one-paragraph doctrine note, symmetric with how
the over-hedge doctrine records "the cheapest way to satisfy a grounding critic is to hedge."

**Layer 2 — Compose (`essay-en-composer` section-blueprint / the steelman beat).**
The steelman beat drafts the concession compactly and the return-to-core with ≥ its weight; bans the
spend/procedure lexicon inside the beat; does not re-quote or re-assert a caveat already spent earlier.

**Layer 3 — Edit (`editorial-review/references/pass-7-adversarial-reader.md` check 3 + the 6-series).**
Add the symmetric finding **`steelman-overweight`** beside `steelman-absent`. It fires when, in the
concession beat: (a) concession/negation sentences out-weigh the affirmative-core sentences; or
(b) the beat restates a caveat an earlier section already made (the `redundant-caveat-restatement`
half); or (c) a spend/procedure motif rides inside it. Symmetric with 6G over-hedge ↔ overreach:
present-but-overweight is a finding, not only absent.

**Layer 4 — Mechanical (`gate_surface.py` SURF-007, warn-only + `scoring-rubric.md`).**
Add **SURF-007** (warn): within the essay's concession/steelman section (located by the thesis-trace
steelman-beat tag, or the section whose header carries the concede marker), warn when
negation-and-concession sentences outnumber affirmative-core sentences, or when the spend/procedure
lexicon (already defined for SURF-006) appears inside that section. Warn-only, feeds the reviewer —
same status as SURF-005/006; no loop-policy change. Register `steelman-overweight` in the goal-4b
finding classes.

## Proposed attribution-table row (apply with the change; do not hand-edit the table before then)

| `steelman-overweight` | pass-7 check 3 (symmetric) / SURF-007 / human-post-accept | 4b | design + edit | adversarial-defense.md steelman-beat spec + pass-7 two-sided check + gate_surface SURF-007 | multi (reference-edit + rubric-tuning + gate-strengthen) |

## Regression expectation / promotion path

- Layers 1–3 are reference/rubric edits (no code path changes `meta/regression.py` outcomes); Layer 4
  adds a gate check, so a **new fixture `steelman-overweight`** is required, symmetric with the existing
  `hedged-verdict` and `procedure-overweight` fixtures. A human applies only after
  `python meta/regression.py` is green *including* the new fixture.
- `watch`, not `recommended-apply`: count 2, both human-caught post-accept, newly-named class. Promotion
  to `recommended-apply` on any one of: (a) a third instance in a later run; (b) the applied
  procedure-attention-budget's SURF-006 demonstrably missing a steelman-section pile-up (proving the
  coverage gap this closes is real, not hypothetical); (c) a self-audit `adversarial-reader` catching a
  `steelman-overweight` autonomously (the class field-testing itself, as several run-045 classes did).
- Success criterion: the next verdict-edition run drafts a concession beat whose affirmative core
  out-weighs the concession, carries no restated caveat, and needs no post-accept compression — and if
  a draft violates it, SURF-007 warns and pass-7 flags `steelman-overweight` before acceptance, not a
  human after it.

## Guard against over-correction

The proposal must not let the pipeline swing to weak-man. Two hard floors stay:
1. The **generic-truism ban** is untouched — a THIS-patent, specific objection is still mandatory;
   `steelman-absent` still fires on a missing or truism concession.
2. `steelman-overweight` measures the concession **relative to the affirmative core in the same beat**,
   not an absolute length cap — a long section is fine if the core out-weighs the concession. The
   target is ratio and net-new-ness, never brevity for its own sake.
