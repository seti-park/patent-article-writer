# Improvement proposal format + the 4 levers

A proposal is a single Markdown file under `meta/improvement-proposals/<date>-<slug>.md`. It is
the meta-loop's only system-changing output, and it changes nothing until a human applies it.

## File format

```markdown
---
proposal_id: 2026-06-09-citation-drift-gate
created: 2026-06-09T10:30:00Z
status: recommended-apply | watch | escalated
lever: reference-edit | gate-promotion | voice-canon-admission | rubric-tuning
goal: "1"
root_cause_stage: compose
root_cause_artifact: essay-en-composer/references/citation-format.md
recurrence_count: 3
confidence: high | medium | low
triggering_findings:
  - essay_id: 044-..., iter: 2, pattern_tag: paraphrase-accidental-drift
  - essay_id: 045-..., iter: 1, pattern_tag: paraphrase-accidental-drift
  - essay_id: 047-..., iter: 3, pattern_tag: paraphrase-accidental-drift
---

## Problem

<What recurs, across which essays, and which north-star goal it threatens.>

## Proposed change (exact diff)

<The precise edit — a unified diff or a before/after block against the named artifact.
Must be applyable verbatim by a human.>

## Why this lever

<Why this is the right level to fix it — and why a cheaper/safer lever won't.>

## Regression expectation

<Which meta/fixtures/ case and which gate tests must still pass after applying.>
```

## The 4 levers

Pick exactly one per proposal. Prefer the cheapest lever that durably fixes the class.

1. **reference-edit** — edit a skill body or a `references/*.md` (e.g. tighten
   `citation-format.md`, add a `section-blueprint.md` rule). Best for procedural gaps.

2. **gate-promotion** — promote a recurring mechanical defect into a deterministic gate, or
   strengthen one: add a literal/regex to `_shared/scripts/banned_terms.txt`, or add a check to
   a `gate_*.py`. Only for patterns that are mechanically safe (no false positives). Must ship
   with a new `test_gates.py` case in the diff.

3. **voice-canon-admission** — admit an exemplar. When a *pass-grade* essay contains a
   paragraph that is a strong instance of an under-served voice category (weak/missing canon
   entry was the root cause), propose adding it to
   `voice-canon-lookup/voice-canon/<entry_id>.md` (frontmatter: `entry_id`, `pattern_category`,
   `source_essay`, `usage_note`, `added_timestamp`) and registering it in
   `voice-canon/index.yaml`. This is the controlled re-introduction of the v1 admit step — but
   evidence-gated and human-approved. Fencing: admission is a Phase-2 change; never routes a
   Phase-3 voice finding back into `voice-profile.md`.

4. **rubric-tuning** — adjust `_shared/references/scoring-rubric.md` weights/threshold, a
   posture default, or the banned-list policy. Highest blast radius — reserve for clear,
   repeated mis-calibration, and always `confidence: medium` or lower unless overwhelming.

## Promotion rules

- `recurrence_count >= RECUR_THRESHOLD` (3) and not capped → `status: recommended-apply`.
- single occurrence → `status: watch` (no diff required yet; record the hypothesis).
- artifact already patched > `CASCADE_CAP` (2) times with the defect persisting →
  `status: escalated`, no further proposals for the class (needs a human design decision).
