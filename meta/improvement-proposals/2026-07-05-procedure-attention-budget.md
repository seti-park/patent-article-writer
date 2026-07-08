---
proposal_id: 2026-07-05-procedure-attention-budget
created: 2026-07-05T00:00:00Z
status: applied (2026-07-05, user-authorized, regression-gated: test_gates 109/109 + fixtures 5/5 incl. new procedure-overweight)
lever: multi (reference-edit + rubric-tuning + gate-strengthen)
goal: "5"
root_cause_stage: design + compose
root_cause_artifact: thesis-spine arc / spine→section trace + section-blueprint lead block + reader-energy.md (no attention-budget doctrine); gate_surface (no procedural-share check)
recurrence_count: 1
confidence: high
triggering_findings:
  - essay_id: etched-0378175-memory-in-writing-r2
    source: human-revision (origin human-post-accept, 2026-07-05, class procedure-overweight-lead ×2)
---

## Headline: the pipeline has no attention budget — procedure can eat the essay and every check still passes

The r2 Etched essay shipped double-clean, self-audit DRY, 14/14 gates with zero warns —
and the publisher's read found the reader's attention mis-spent: prosecution process
(3-year examination, RCE mechanics, spend narrative, liens) dominated the lead and §5,
crowding out the technology and its consequences. Readers were predicted to disengage
before the tech sections. The owner briefing and promo pack, which have fixed schemas,
were fine. Full reasoning: `meta/implementation-notes.md` (2026-07-05 entry).

## Evidence

- v5 lead ¶2–3: "still being argued with an examiner, and expensive to keep alive",
  "Etched has paid at every step since, from the filing fee through the examination it
  is still in" — before any technical content. Tech began at §2.
- v5 §5: a full RCE explainer paragraph, a repeated-spending motif, a two-paragraph lien
  walk plus a timing-inference paragraph. The essay-context user decision said:
  "prosecution status: exactly ONE label sentence, no battle narrative." The letter held
  (one full-detail sentence); the motif recurred ≥6 times across lead/§5/§6.
- Every instance was individually grounded, so pass-3/pass-4 approved each; no check
  counts the aggregate. gate_surface's checks (SURF-001..004) all point at the first
  two sentences/title; the pile-up sat between the checks.
- Verdict-frame confusion upstream: the pending-application edition contract makes the
  VERDICT about document treatment (collateral, continued prosecution). Phase 1 let that
  verdict frame become the NARRATIVE frame (spine one-liner, Q7 hook, and section trace
  all prosecution-anchored), so procedure became the plot.

## Applied (2026-07-05, user-authorized + regression-gated)

All four layers below were implemented this session (SETI authorized direct application;
`meta/regression.py` passes with the new `procedure-overweight` fixture):

- **Layer 1 Design**: thesis-architect SKILL Step 8 (`payload: tech|pricing|frame` tags in
  the spine→section trace, ≤1 pricing section, verdict-frame ≠ narrative-frame rule) +
  Step 11(d) attention-budget trap (motif budgets); `hook-patterns.md` Pattern 1 payload
  condition; `handoff-template/01-design/thesis-spine.md` trace table gains the payload
  column.
- **Layer 2 Compose**: `section-blueprint.md` attention-budget default (payload-first lead,
  procedure priced once, motif budget with revision-mode re-scan).
- **Layer 3 Edit**: pass-6 **6I attention-budget guard** (volume/placement counterpart to
  6H, severity table row added); patent-essay SKILL cold-reader **early-drag
  auto-escalation** (lead-area drag = medium, no corroboration needed).
- **Layer 4 Gate**: `gate_surface.py` **SURF-005** (lead procedure-narration sentences > 1)
  + **SURF-006** (spend-motif > 4 in prose), warn-only; 7 new test_gates cases (109/109);
  fixture `meta/fixtures/procedure-overweight/` (full v5 essay: SURF-005 fires at 3
  sentences, SURF-006 at 10 hits; v6 stays zero-findings across all gates).
- **Doctrine + registration**: `reader-energy.md` new **§6 Attention budget**;
  scoring-rubric goal-5 matrix + gate table rows; CLAUDE.md gate/editorial lines.

## Proposal (as originally drafted)

1. **reader-energy.md (reference-edit):** add an "attention budget" doctrine section:
   for verdict editions, the lead answers *what the invention does and changes* before
   *what it costs / where it stands*; status/finance material is pricing context with a
   structural home in ONE section plus the closing; a brief's "one label sentence"
   budget covers paraphrase echoes (spend/fee/keep-alive language), not just the literal
   status sentence.
2. **thesis-architect (reference-edit):** the spine→section trace must not place the
   same non-tech beat (prosecution/finance) in more than lead-clause + one section +
   closing; the edition contract's verdict frame is explicitly NOT the narrative frame —
   add this as a trap-class note for pending-application editions.
3. **editorial-review pass-6/pass-7 (rubric-tuning):** add a reader-payload check —
   "does §1 tell the reader what the thing does before what it costs?" and a
   motif-count for procedure language against the brief's budget.
4. **Candidate SURF-005 (gate-strengthen, warn-only; build only if the class recurs):**
   procedural-lexicon share of the lead section (rejection, RCE, examiner, fee, lien,
   security interest, docket, prosecution) above a threshold ⇒ warn; optional
   time-to-first-tech-anchor ([dddd] or figure token) measure.

## Applied this session (essay-side remediation, not skill edits)

- `essays/etched-us20240378175-r2/` v5 → v6: tech-first title + lead; §5 compressed to
  label sentence + steelman + merged lien paragraph; RCE explainer / timing-inference /
  spending motif cut. Gates 14/14 zero findings; signature lines intact.
- `meta/attribution-table.md`: new row `procedure-overweight-lead` (goal 5).
- `meta/normalize_revision_notes.py` CLASS_MAP: same class added (selftest passes).
- Ledger: 2 records appended (origin human-post-accept).
