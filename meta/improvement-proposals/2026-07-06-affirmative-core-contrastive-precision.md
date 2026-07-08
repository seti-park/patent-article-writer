---
proposal_id: 2026-07-06-affirmative-core-contrastive-precision
created: 2026-07-06T18:00:00Z
status: watch   # per promotion rules the specific sub-mechanism is first-isolated (count 1); filed with a full pre-verified diff + apply-early justification, mirroring the 2026-06-11-claim-scope-lock-map precedent (residual of an APPLIED fix on the system's most-damaging class)
lever: reference-edit
goal: "1"
root_cause_stage: design
root_cause_artifact: thesis-architect/references/adversarial-defense.md (affirmative-core "concede-and-return" spec + thesis-spine Output schema Mitigation field) — no rule that the affirmative core's CONTRASTIVE term carry the claim-supported precision
recurrence_count: 1   # this exact sub-mechanism (spine seeds the affirmative-core contrastive-term imprecision). Parent class claim-scope-misattribution = 15 across the ledger (the system's dominant class), 4 this run
confidence: high
triggering_findings:
  - essay_id: intel-us20260191095-backend-hbm, iter: 1, finding_id: r1-F2, pattern_tag: claim-scope-misattribution, severity: medium (pass-4, the PIVOTAL inference sentence)
  - essay_id: intel-us20260191095-backend-hbm, iter: 2, finding_id: r2-F1, pattern_tag: claim-scope-misattribution, severity: low (§5 restatement, same seam one clause downstream)
  - essay_id: intel-us20260191095-backend-hbm, origin: self-post-accept, delta: SA-r1-7, pattern_tag: claim-scope-misattribution (§5 "a front-end fab cannot" — the same seam, caught AGAIN post-accept)
related_applied_proposal: 2026-06-11-claim-scope-lock-map (applied 2026-07-02) — this is a residual GAP in that fix: the map pins claim ELEMENTS (locked/open/pinned); it does not pin the precision of the contrastive TERM the spine's own affirmative core turns on
---

## Problem

The system's single most damaging finding class — `claim-scope-misattribution` (15 records
across the ledger, the top class; 4 of them in this one run) — recurred here as the run's
**most severe finding** (r1-F2, medium, on the **pivotal inference sentence**), and the
applied claim-scope-lock-map did **not** prevent it. Root cause traces **upstream into
Phase 1's own output**, exactly the pattern the claim-scope-lock-map proposal itself named for
its Run 2 (`both-and-steel`): *the design artifact that exists to prevent the drift seeds it.*

The essay's thesis rests on one contrastive inference: *"backend" is the property a
logic-plus-packaging flow can carry, where a **DRAM** front-end cell cannot.* The precise,
claim-supported contrastive term is the **DRAM** front-end (a logic foundry also runs a
crystalline-silicon front-end; the defensible claim is the DRAM FEOL specifically). The
`thesis-spine.md` says this **correctly in four places** and **incorrectly in one** — and the
one it gets wrong is the **affirmative core**, the exact template Compose is instructed to
"return to":

| thesis-spine location | contrastive term | precise? |
|---|---|---|
| Axis-4 anchor (line 22) | "dedicated DRAM front-end (FEOL) fabs" / "must be a DRAM FEOL fab" | ✅ |
| Q7 hook (line 26) | "need not come off a dedicated DRAM fab" | ✅ |
| Steelman beat (line 37) | "a non-DRAM-fab flow" | ✅ |
| **Mitigation → affirmative core (line 33)** | **"where a crystalline-silicon FEOL cell cannot"** | ❌ generic superset |

Compose drafted the affirmative core from the one imprecise instance and propagated it:

- **§4 pivotal sentence (r1-F2, medium):** *"it does not need the crystalline-silicon
  front-end that only a dedicated DRAM fab runs"* — generic "crystalline-silicon front-end,"
  true of logic dies too. This is *the* load-bearing inference of the essay, and it opened the
  exact skeptical objection the §5 steelman exists to pre-empt.
- **§5 restatement (r2-F1, low):** *"a logic-and-packaging line can carry and a front-end fab
  cannot"* — the same over-broad contrast, one clause downstream. The round-1 §4 fix did **not
  reach** it; it survived to acceptance as a carried low and was only closed **post-accept in
  self-audit** (SA-delta-7 → "without owning a DRAM front-end").

Two independent signals confirm this is a **system** gap, not a one-off compose slip:

1. **The owner had to police it by hand.** `input/essay-context.md` carries a bespoke guard:
   *"§4/§5/§6 affirmative-core ('without a DRAM front-end' family) stays PRECISE — a
   DRAM-front-end claim, not over-broad 'logic can do everything memory can'."* The owner
   pre-empted per-run a precision the design artifact should have carried. Promoting the
   owner's manual guard into the standard design output is exactly the meta-loop's job.
2. **It cost cycles in two loops.** The seam produced a round-1 medium (a full revision round)
   AND survived into a post-accept self-audit fix — the imprecise contrastive term was drafted,
   caught, narrowed, then *re-caught downstream and narrowed again*.

The applied `2026-06-11-claim-scope-lock-map` closes the **claim-element** scope gap (what a
claim locks / leaves open / pins). It has no jurisdiction over the **contrastive term** the
spine's affirmative core turns on — so a spine can pass the claim-scope map with every claim
element correctly pinned and still hand Compose an over-broad "X can do what Y cannot" where Y
is a generic superset of the claim-supported narrow term. That is the residual this closes.

## Proposed change (exact diff)

Two documentation-only edits to `.claude/skills/thesis-architect/references/adversarial-defense.md`.
No script, no gate, no banned list, no fixture input.

**Edit 1 — add a contrastive-term precision rule to §D "Steelman beat — carry into Compose"**,
immediately after the `steelman-overweight` / ratio paragraph (after line 127, before the
generic-truism-ban paragraph):

```markdown
**The affirmative core's contrastive term must carry the claim-supported precision.** The
affirmative core is almost always a contrast — *"X can carry it, where Y cannot"* / *"it does
not need Z."* State the contrastive term (Y / Z) in the **narrowest form the claim actually
supports**, matching the precision the spine's Axis/anchor already uses — never a generic
superset that a skeptical pro-subject reader can immediately widen. If the Axis anchor says
"a dedicated DRAM front-end fab," the affirmative core says "a DRAM front-end," NOT
"a crystalline-silicon front-end" (logic dies have one too); if the anchor says "a fixed-function
ASIC," the core says "a fixed-function ASIC," not "any chip." The spine is the seed: an
imprecise contrastive term in the Mitigation / affirmative-core line is inherited verbatim by
Compose onto the pivotal inference sentence (the drift the artifact exists to prevent). Before
finalizing the spine, grep your own affirmative core against the Axis-4 anchor: the contrastive
term must read **identically precise** in both. Carry the narrow term into
`phase2-handoff-notes.md` as a **term-precision trap** row (DO use "<narrow term>"; DON'T widen
to "<generic superset>"), alongside the claim-scope traps the Claim scope map already requires.
This is `claim-scope-misattribution` — the system's most damaging class — leaking through the
contrastive TERM rather than a claim element (ledger: intel-us20260191095-backend-hbm r1-F2
medium / r2-F1 / SA-r1-7).
```

**Edit 2 — pin it in the Output schema (thesis-spine.md) so it is not optional:**

```diff
-**Mitigation**: <how the essay disarms it + where in the essay>
+**Mitigation**: <how the essay disarms it + where in the essay. If the affirmative core is a
+contrast ("X can carry it, where Y cannot" / "it does not need Z"), state the contrastive term
+Y/Z in the narrowest claim-supported form — matching the Axis-4 anchor's precision, never a
+generic superset — and carry that exact term into phase2-handoff-notes as a term-precision trap.>
```

## Why this lever

- **The defect is born in Design.** The composer is fenced (execution-boundary) from
  re-deriving claim scope; it can only be as precise as the affirmative-core template the spine
  hands it, and here that template carried the generic term. A compose-side rule would fight the
  handoff; a gate can't read whether "crystalline-silicon front-end" is too broad for *this*
  claim (that requires reading the claim). reference-edit at the spine spec is the only lever
  that hits the seed.
- **It extends, not duplicates, the applied claim-scope-lock-map.** Same owner stage (design),
  same class, adjacent artifact — the map governs claim *elements*; this governs the affirmative
  core's contrastive *term*. Together they cover both routes by which the class leaks.
- **Not gate-promotion.** "Is this contrastive term an over-broad superset of the claim-supported
  one?" is a claim-semantics judgment; any regex would false-positive on every legitimate
  broad-then-narrowed contrast.
- **Filed `watch`, not `recommended-apply`, honestly:** the *specific* sub-mechanism (spine
  seeds the affirmative-core contrastive term) is first cleanly isolated here (count 1). But it
  is a residual of an APPLIED fix on the dominant class, it seeded the run's most-severe finding
  on the pivotal sentence, it survived into a second (self-audit) loop, and the owner already
  police-guards it by hand — so, exactly as `2026-06-11-claim-scope-lock-map` did at count 2,
  the full pre-verified diff is included so a human can **apply early** rather than wait for the
  class to breach a grounding hard-gate through this route on another patent.

## Cascade check

`claim-scope-lock-map` has been applied **once** (2026-07-02); CASCADE_CAP is 2. This is a
first extension of that artifact-family for a distinct sub-mechanism, not a repeated patch of
the same one — no cascade concern. If a *third* essay shows the affirmative-core contrastive
term leaking after this is applied, that promotes the sub-mechanism to `recommended-apply` and
bumps cascade accounting on adversarial-defense.md.

## Regression expectation

Documentation-only (one reference file; the Output-schema block is a template, not executed).

- `python .claude/skills/_shared/scripts/test_gates.py` — all cases pass, unchanged (no gate
  reads adversarial-defense.md or thesis-spine.md).
- `python meta/regression.py` — `clean-baseline` and `figure-orphan` fixtures produce identical
  verdicts.
- Observable next-run criterion: for any essay whose thesis rests on an "X can carry it, where Y
  cannot" contrast, `thesis-spine.md`'s affirmative core and its Axis anchor use the **identical
  narrow** contrastive term; `phase2-handoff-notes.md` carries a term-precision trap for it; and
  no pass-4 `medium` fires on the pivotal inference sentence for an over-broad contrastive term.
