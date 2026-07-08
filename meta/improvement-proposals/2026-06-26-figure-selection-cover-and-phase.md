---
proposal_id: 2026-06-26-figure-selection-cover-and-phase
created: 2026-06-26T00:00:00Z
status: applied  # 2026-07-02 architecture refactor; schema + Step 9 edits
lever: reference-edit
goal: "2"
root_cause_stage: design
root_cause_artifact: thesis-architect/references/invention-summary-schema.md (Figure relationships) + thesis-architect/SKILL.md Step 9 (figure mapping)
recurrence_count: 1
confidence: medium
triggering_findings:
  - essay_id: us12560948b2, pattern_tag: figure-cover-undervalued (most on-thesis visual nearly dropped; sequence frames picked by spacing, not the patent's phase decomposition)
---

## Problem

Phase-1 figure selection optimizes for argument economy and claim-scope safety, but has no notion
of **cover/visual value** or of a **sequence figure that depicts the claimed step**. On
US 12,560,948 the FIG. 5 kneel sequence — the filing's most striking visual and the most literal
picture of the claimed core step (lowering the center-of-gravity) — was left out of the first
three-figure plan for economy, and only added after a SETI catch. Worse, when it was added, frames
were first chosen by visual spacing rather than the patent's own four-phase decomposition
([0046]-[0047], which explicitly enumerates phases 5A-5G / 5H-5L / 5M-5W / 5X-5AD). The patent
*defines* the core movement set; the figure plan should inherit that decomposition, not improvise.

## Proposed change (exact diff)

**File 1: `.claude/skills/thesis-architect/references/invention-summary-schema.md`** — extend the
"Figure relationships" table spec with two optional columns and a note:

```markdown
| Figure | Paired with | Relationship | Cover candidate? | Phase map (sequences only) |
|---|---|---|---|---|
| FIG. 5 | 5A-5AD | progressive sequence | yes (most literal picture of the claimed step) | 5A-5G p1 / 5H-5L p2 / 5M-5W p3 / 5X-5AD p4, per [0046]-[0047] |

- **Cover candidate**: mark the single figure that best carries the 5:2 header. It is judged on
  visual force and on depicting the claimed core step, separately from the argument-economy
  selection. A sequence that depicts the claimed step is a strong cover candidate even if a static
  end-state figure already covers the same point in the body.
- **Phase map**: when a figure is a progressive sequence and the specification enumerates phases,
  record the phase-to-panel ranges with the enumerating paragraph anchor. Keyframes chosen for a
  cover strip map one-per-phase from this column, not from visual spacing.
```

**File 2: `.claude/skills/thesis-architect/SKILL.md`** — Step 9 (figure mapping), add:

```diff
-9. **Figure mapping** — write `figure-selection.md` and `figure-rationale.md`. Each figure maps to a thesis point + caption_role. **Paired-figure relationships** ... pull from `invention-summary.md` §"Figure relationships".
+9. **Figure mapping** — write `figure-selection.md` and `figure-rationale.md`. Each figure maps to a thesis point + caption_role. **Paired-figure relationships** ... pull from `invention-summary.md` §"Figure relationships". Additionally: (a) tag one **cover candidate** for the 5:2 header, judged on visual force + whether it depicts the claimed core step — do NOT drop a sequence that depicts the claimed step purely for economy; (b) for a progressive sequence whose spec enumerates phases, take keyframes one-per-phase from the §"Figure relationships" Phase map (cite the enumerating paragraph), never by visual spacing.
```

## Why this lever

- The defect is a Phase-1 coverage gap (goal 2): the design hand-off had no field for cover value or
  for inheriting the patent's own phase decomposition, so Compose/cover work improvised both. A
  reference-edit adds the missing fields where the patent text is in hand.
- Not a gate: "is this the best cover image" and "does the spec enumerate phases" are judgments that
  no regex can make.

## Regression expectation

- Documentation-only (schema + SKILL). `test_gates.py` and `meta/regression.py` unchanged. Success
  criterion: the next sequence-bearing patent yields a `figure-selection.md` with a cover candidate
  and, for any enumerated sequence, a phase map that the cover keyframes follow.

## Related

- Pairs with the recommended `tools/compose_figure_sequence.py` build (retro L6): selection decides
  *which* frames and *why*; the tool composes them to spec (5:2, aligned ground line, uniform
  captions). And with `2026-06-11-figure-token-panel-suffix.md`: lettered-panel references only work
  once the figure regex parses them.
