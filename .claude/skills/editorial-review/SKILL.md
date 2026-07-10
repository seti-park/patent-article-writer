---
name: editorial-review
description: "Mandatory 7-pass review on every essay draft from Phase 2 Compose. Seven passes (voice canon + anti-AI compliance, redundancy + compression, claim adequacy + fact verification + paraphrase mutation, logical alignment + causality, reader perspective + paragraph readability, lead/conclusion + format compliance incl. 6G over-hedge + 6H defensive-open guards, adversarial reader). Structured YAML feedback — NOT auto-fix. Posture-aware (aggressive / measured / conservative). Use when essay-draft.md lands in Phase 3 Edit. NOT for: format-only verification (folded into Pass 6), pool admission (deprecated), auto-fix, voice training corpus admission."
context: fork
agent: editorial-reviewer
---

# editorial-review

Phase 3 Edit's mandatory inferential review. Six passes. Structured feedback YAML output.

```
handoff/02-compose/essay-draft.md
    + handoff/01-design/{thesis-spine.md, invention-summary.md, fact-check-log.md}
    + patent.md (re-uploaded for Pass 3 verbatim checks)
    + Knowledge: deliverable-voice-rules.md, anti-ai-writing.md, x-article-format.md,
      reader-energy.md
    → 7 passes
    → handoff/03-edit/edit-log.md (structured YAML feedback)
    → orchestrator routes medium+ findings to composer revision mode → handoff/03-edit/essay-final.md
```

## Output role

Findings, not fixes.

- Findings supply input for the orchestrator's revise decision: it routes every medium+ finding to the composer's revision mode, where each gets an `applied`/`rejected` disposition. NOT auto-fix.
- The owner holds override authority at the surfaced decision points (spine and title picks, briefing review, the acceptance report) and through the post-accept `revision-notes.md` channel. This skill cannot substitute for owner catches.
- Conflict resolution: an owner catch overrides skill output.

## Voice fencing (CRITICAL)

Phase 3 Project does NOT load `voice-profile.md` (avoid voice drift bias from re-exposure to canon). Voice compliance is verified against `deliverable-voice-rules.md` mechanical rules + `anti-ai-writing.md` banned-pattern list only. This is enforced by the Phase 3 Project Instructions. `_shared/references/reader-energy.md` IS in-fence (it is the goal-5 surface contract reviewers enforce, not persona voice) — reviewers read it.

## Posture lens

3-tier: aggressive / measured (default) / conservative. The same finding receives different severity classification under different posture. See `references/posture-lens.md`.

## Finding jurisdiction (anti-hedge-ratchet)

Each pass rules ONLY on its own dimension, and grounding pressure never converts into verdict
softening:

- **Pass 3 / Pass 4 (grounding, causality)** judge text↔source fidelity. A finding's
  recommendation names a better anchor, a narrower claim, or an explicitly-labeled-analysis
  reframe — in that priority order. "Add a caveat / disclaimer / hedge to the conclusion" is
  NEVER a valid pass-3/4 recommendation; if a claim cannot be anchored, narrowed, or labeled,
  recommend cutting that claim, not hedging the verdict.
- **Pass 6 6G** owns verdict confidence, symmetrically: it flags overreach the body cannot
  carry AND over-hedge the body does not warrant.
- **Pass 7's steelman check** accepts only a THIS-patent objection; a generic patent truism
  ("patents don't guarantee products") is `steelman-absent`, not a satisfied steelman.
- **Surface jurisdiction (goal 5).** Title, section headers, lead-¶1 style, and the ≤ 3
  signature lines declared in `thesis-trace.md` belong to the energy contract
  (`_shared/references/reader-energy.md`): do not sand their style, and do not count declared
  signature lines in echo/repetition rules (pass-2 2A, pass-7 item 7). Factual findings on
  them remain fully in scope (pass-3/4 bind everywhere). Energy violations ARE findings:
  defensive-open (6H), gap-framed headers that bury the discovery, a title/lead that fails
  the first-two-lines test.

Rationale: without this fence the loop ratchets — every grounding pass adds a caveat, no pass
removes one, and conclusions converge on safe-harbor boilerplate regardless of the evidence
(ledger class `conclusion-over-hedge`). The surface fence is the same defense pointed at the
lead: without it, count rules sand the aphorisms and insurance stacks ahead of the hook.

## When to invoke

After `essay-en-composer` produces `handoff/02-compose/essay-draft.md`. Mandatory on every essay. No skip option. Rationale: v1 historical leaks (paraphrase mutation in published draft) reached publication only because editorial-review was skipped.

## Round type (orchestrator-assigned)

The **orchestrator** is the producer of round type. When forking a reviewer it states
`round_type: confirmation` or `round_type: revision` in the fork instruction. The reviewer
writes `round_type: confirmation | revision` as a YAML field in the header block of
`edit-log.round-N.md`.

- **Confirmation rounds:** no `revision-response.round-N.md` may exist for that round; its
  absence is corroborating evidence. **Veto rule:** if a revision-response for N is present,
  the round counts as a **revision** round. Confirmation-round reviews tolerate the missing
  revision-response (fresh full review, nothing to disposition).
- **Revision rounds:** expect prior-round dispositions; re-review protocol below applies.

## Re-review protocol (round N > 1)

A re-review is NOT a fresh review plus vibes — it starts from the carried state:

1. Read round N-1's `edit-log.round-(N-1).md` and the composer's
   `revision-response.round-(N-1).md` (required for revision rounds; absent on confirmation).
2. **Rule on every carried finding_id first**: verify each `applied` disposition actually
   landed in the draft (quote the fixed span) and did not regress a neighbor (re-count
   paragraph bands around any structural edit); for each `rejected` disposition, either accept
   the rejection (note why) or re-assert the finding under its original id with the escalation
   noted. No id disappears silently. A re-asserted finding carries
   `prior_severity: <sev> (round N)` per `references/feedback-format.md`.
3. Then run the full 7 passes on the current draft for NEW findings (ids `rN-F<k>`).
4. A round-N review that finds zero medium+ findings must still show the carried-id rulings —
   an edit-log that only says "no findings" after a failing round is invalid.

Each review round runs in a FRESH context (no memory of having approved anything): the
orchestrator spawns a new `editorial-reviewer` instance per round. Prior rounds' state travels
through the artifacts above, not through conversation history — commitment to the draft is the
documented failure mode this isolation exists to prevent.

## Seven passes (v2 locked order; pass-7 added run 045)

1. **Voice canon + anti-AI compliance** — voice canon pattern adherence (cadence, structure inheritance) + banned-pattern grep (em-dash count = 0, "delve" / "navigate" / "leverage" etc.). See `references/pass-1-voice-anti-ai.md`.
2. **Redundancy + compression** — claim repetition + sentence tightening + paragraph word-count earn check. See `references/pass-2-redundancy.md`.
3. **Claim adequacy + fact verification + paraphrase mutation** — every `[XXXX]` cite verified against `invention-summary.md` Quotable spans verbatim; external claims verified against `fact-check-log.md` + the (re-uploaded) patent.md; paraphrase variations classified (intentional restatement / accidental drift / substantive change). See `references/pass-3-fact-paraphrase.md`.
4. **Logical alignment + causality** — 인과 vs 상관 vs 우연 distinction, thesis-section 정렬 check against `thesis-spine.md` spine→section trace. See `references/pass-4-logic-causality.md`.
5. **Reader perspective + paragraph readability** — engagement curve, stake clarity, mobile rendering line count. See `references/pass-5-reader-perspective.md`.
6. **Lead/conclusion + format compliance** — hook anchor to thesis, frame closure, `# Sources` 5-category enum check, "First, et al." format, em-dash count, `[xxxx]` format check, banned-words grep (covers the deterministic-gate absorption), **6G over-hedge guard** (verdict confidence proportionate to evidence; the mirror of pass-3/4's overreach defense — judgment complement of `gate_hedge`), **6H defensive-open guard** (disclaimers/insurance stacked before the lead's discovery beat — 6G's mirror at the top of the essay; judgment complement of `gate_surface` SURF-002/004). See `references/pass-6-lead-conclusion-format.md`.
7. **Adversarial reader-pass (fresh-eyes, run 045+)** — a separate-context pass that does NOT trust the draft: read as the impatient investor and the skeptical pro-subject reader and hunt, decomposed yes/no with a quoted span per check, for the hook check (¶1 lands the declared register's beat AND the call lands by the lead's end), header-as-claim, an unrebutted strongest counter (steelman), reader-instruction/self-reference meta, jargon deep-dive, stub rhythm, and the core verdict restated in >3 sections (declared signature lines exempt). The judgment complement of `gate_meta`/`gate_stub`/`gate_cashtag`/`gate_dupe`. See `references/pass-7-adversarial-reader.md`.

Causal claim quality is a recurring cross-pass concern (Pass 3 + Pass 5). See `references/causal-reasoning.md`.

## Output format

Structured YAML feedback. See `references/feedback-format.md` for full schema.

Minimal example:

```yaml
review_id: <essay-id>-editorial-review-1
draft_source: handoff/02-compose/essay-draft.md
round_type: revision          # confirmation | revision (orchestrator-assigned)
posture_applied: measured
overall_assessment: revise-required

findings:
  - finding_id: r1-F1
    pass: pass-3-fact-paraphrase
    location: §3, sentence with "complements"
    severity: high
    severity_under_default_posture: high
    finding: |
      Source verbatim is "supplements" (invention-summary.md Quote anchor q-0024-1).
      Prose uses "complements". Accidental drift.
    recommendation: |
      Re-anchor to source verbatim.
```

Feedback gets written to `handoff/03-edit/edit-log.md`. The orchestrator routes medium+ findings to the composer's revision mode; on acceptance the draft is promoted to `handoff/03-edit/essay-final.md`.

## Pre/post conditions

Pre:
- `handoff/02-compose/essay-draft.md` present.
- `handoff/01-design/{thesis-spine.md, invention-summary.md, fact-check-log.md}` accessible.
- `patent.md` re-uploaded to Phase 3 Knowledge for Pass 3 verbatim verification.
- Knowledge files loaded: `deliverable-voice-rules.md`, `anti-ai-writing.md`, `x-article-format.md`, `working-dialogue-voice.md`, `_shared/references/reader-profile.md` (audience contract for pass-5/pass-7), `_shared/references/reader-energy.md` (goal-5 surface contract for 6H / pass-7 hook check / surface jurisdiction). (NOT `voice-profile.md` — voice fencing.)
- Posture confirmed in opening response.

Post:
- `handoff/03-edit/edit-log.md` emitted with one entry per finding.
- Each finding has specific draft location + severity + recommendation.
- `overall_assessment` set per severity rules in `references/feedback-format.md`.
- Auto-fix NOT performed (the orchestrator routes findings to the composer's revision mode; the composer dispositions each).

## Coupling

- ← `essay-en-composer` (`essay-draft.md` input)
- ← `thesis-architect` (handoff/01-design/* for cross-checks)
- → orchestrator (routes findings to the composer's revision mode → `essay-final.md`; the owner may override at surfaced decision points)

## Out of scope

- Auto-fix (the composer's revision mode applies findings, with dispositions).
- Pool admission (v1 `pool-admission` skill — dropped).
- Strategic adversarial audit (v1 `strategic-audit` skill — dropped).
- Cross-essay coherence sensing (v1 `cross-essay-coherence-sensor` — dropped).
- Voice canon corpus admission (v1 voice-profile-seti admit step — Phase 3 doesn't touch the canon).

## References

- `references/pass-1-voice-anti-ai.md` — voice canon adherence + anti-AI banned-pattern grep, severity calibration per posture.
- `references/pass-2-redundancy.md` — claim repetition, sentence tightening, paragraph word-count earn.
- `references/pass-3-fact-paraphrase.md` — verbatim verification against Quotable spans + fact-check-log + patent.md; paraphrase mutation classification.
- `references/pass-4-logic-causality.md` — thesis-section 정렬 + 인과/상관/우연 distinction.
- `references/pass-5-reader-perspective.md` — engagement curve, stake clarity, mobile rendering.
- `references/pass-6-lead-conclusion-format.md` — hook/closure + mechanical compliance (em-dash, [xxxx] format, banned-words, Sources 5-category enum, "First, et al.") + 6G over-hedge guard + 6H defensive-open guard.
- `references/pass-7-adversarial-reader.md` — fresh-eyes adversarial reader-pass (hook check / header-as-claim / steelman / meta / jargon-depth / stub / thesis-restatement); judgment complement of the run-045 self-check gates.
- `references/posture-lens.md` — 3-tier posture + per-pass posture sensitivity table.
- `references/external-fact-verification.md` — Pass 3 sub-pass detail, 5-tier source authority hierarchy.
- `references/causal-reasoning.md` — causal claim quality checks (Pass 3 + Pass 5).
- `references/feedback-format.md` — output YAML schema + severity criteria.
