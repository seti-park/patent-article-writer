---
name: essay-en-composer
description: "Composes English long-form patent analysis essays from the Phase 1 Design handoff (thesis-spine.md + invention-summary.md + figure-selection.md + fact-check-log.md). Mode-aware (walkthrough / strict-execution / pair) × posture-aware (aggressive / measured / conservative). Inline [xxxx] paragraph citations from invention-summary Quotable spans. Output: handoff/02-compose/essay-draft.md + figures-rationale.md + thesis-trace.md + publication.md via strip pipeline. Use when user provides handoff/01-design/* and asks to draft, compose, or write the essay. NOT for: thesis design (Phase 1 thesis-architect), voice judgment (delegate to voice-canon-lookup), editorial review (Phase 3 editorial-review), promo digest (Phase 4 promo-composer)."
context: fork
agent: essay-composer
---

# essay-en-composer

**Contract:** `contracts/stages/compose.yaml`

Phase 2 Compose's drafting stage. Reads the Phase 1 handoff bundle and produces the essay draft.

```
handoff/01-design/{thesis-spine.md, invention-summary.md, title-lead-candidates.md,
                    figure-selection.md, figure-rationale.md, fact-check-log.md}
    + the orchestrator's selected title-lead pair (default: the file's recommended pick)
    + voice-canon-lookup (per section)
    → essay-draft.md          (inline [xxxx] cites, # Sources, frontmatter)
    → figures-rationale.md    (compose's actual placement decisions)
    → thesis-trace.md         (spine → section mapping)
    → publication.md          (frontmatter + footnote-defs stripped, # Sources kept)
```

## When to invoke

User has uploaded `handoff/01-design/*` files + `figures/` to the Phase 2 Compose Project and asks to draft, compose, or write the essay. Phase 1's Quotable spans are the only patent source. Reading `input/patent.md` is **FORBIDDEN** by `contracts/stages/compose.yaml` `must_not_read` (invariant 3). If a paragraph cannot be grounded in a Quotable span, do **not** open the patent — raise `OWNER_QUESTION` (or `STOPPED: span gap`) naming the paragraph. A post-hoc detector (`gate_patent_leak`) also enforces this; the fence is not honour-system alone.

## Modes (2 dimensions)

Two orthogonal dimensions, both selectable at invocation. Default: walkthrough + measured.

- **Mode category**: walkthrough (default) / strict-execution / pair — see `references/mode-spec.md`.
- **Posture**: aggressive / measured (default) / conservative — see `references/mode-spec.md`.

A third entry path is **revision mode** (loop round N > 1): the orchestrator feeds back the
round's edit-log findings + failing gate check_ids, and the composer revises in place under the
finding-by-finding disposition contract — see `references/revision-mode.md`. Revision mode is
NOT freeform redrafting: every medium+ finding_id gets an `applied` or argued `rejected`
disposition in `revision-response.round-N.md` before prose moves.

## Process (7 steps)

1. **Mode selection** — adopt or default. Confirm in opening response.
2. **Load handoff** — read all 6 Phase 1 files. Reject if `thesis-spine.md` Q7 hook not declared, or if Quotable spans missing for spine anchors. Adopt the orchestrator's selected `title-lead-candidates.md` pair (register + title + lead sketch); if no selection was passed, use the file's `recommended:` pick and log the fallback in the opening response.
3. **Plan sections** — build internal section blueprint per `references/section-blueprint.md`. Map spine→section, plan `voice_canon_reference` per section, plan `paragraph_anchors_used` + `external_facts_used` per section. The lead section plans hook-first from the selected title-lead pair: ¶1 delivers the chosen register's beat, the full two-sided call lands by the lead section's END, and no verdict-insurance fact (status label, lien, rejection) precedes the beat (see `_shared/references/reader-energy.md`). Plan ≤ 3 signature lines (exact strings) for declaration in `thesis-trace.md`.
4. **Plan figures** — per `references/figure-rendering.md` 4 caption_role types. Default body rendering = `caption-only-italic`; header = `image-plus-caption`.
5. **Compose sections in order** — apply voice canon patterns by invoking `voice-canon-lookup` per section. Use only paragraph anchors from `invention-summary.md`. Respect `word_target` ±20%. Per-mode composition rhythm in `references/mode-spec.md`.
6. **Annotate factual claims** — inline `[XXXX]` at every patent claim. External claims go to `# Sources` block + cross-check `fact-check-log.md`. See `references/citation-format.md`.
7. **Emit draft + publication.md + handoff files** — `essay-draft.md` (frontmatter + footnotes; frontmatter carries `closing_posture` copied from `thesis-spine.md`, read by `gate_hedge`), `publication.md` (stripped via `references/strip-pipeline.md`, one line per paragraph), `figures-rationale.md`, `thesis-trace.md`. `thesis-trace.md` includes a `## Signature lines` section declaring ≤ 3 exact strings (0-3; write `none` explicitly if zero) — declared lines are protected surface per `_shared/references/reader-energy.md` (echo/count-exempt; factual review still applies).

## Plan ⊥ Execute boundary

Composition stays within `thesis-spine.md` constraints. Fact introduction beyond `invention-summary.md` Quotable spans + `fact-check-log.md` external facts is forbidden in all modes. Voice and clarity refinement scope expands with posture (conservative → measured → aggressive) within walkthrough mode; strict-execution suppresses mid-session intervention; pair mode adds sentence-level checkpoints. Spine gaps stop composition rather than provoke improvisation. Full rule list in `references/execution-boundary.md`.

## Pre-conditions

- `handoff/01-design/thesis-spine.md` exists with locked 4-axis grounding + Q7 hook pattern declared.
- `handoff/01-design/title-lead-candidates.md` exists (five register-keyed pairs + `recommended:` line); the orchestrator's selected pair known, or the recommended pick adopted as fallback.
- `handoff/01-design/invention-summary.md` exists with Quotable spans covering every paragraph anchor the spine references.
- `handoff/01-design/figure-selection.md` + `figure-rationale.md` exist with every selected figure mapped to a thesis point.
- `handoff/01-design/fact-check-log.md` exists (may be empty if thesis is entirely patent-anchored).
- `figures/fig-NN.png` accessible via Project file uploads.
- `voice-canon-lookup` skill installed in same Project.
- Phase 2 Knowledge files loaded: `voice-profile.md`, `deliverable-voice-rules.md`, `anti-ai-writing.md`, `caption-roles.md`, `x-article-format.md`, `working-dialogue-voice.md`, `_shared/references/reader-profile.md` (audience contract — jargon gloss budget, familiar-scale numbers, translate-then-quote claim language, money thread), `_shared/references/reader-energy.md` (goal-5 surface contract — hook-first lead, feed-context rules, signature lines).
- Mode and posture confirmed in opening response.

## Post-conditions

- `handoff/02-compose/essay-draft.md` emitted with inline `[XXXX]` markers, `# Sources` block, optional `# Footnotes` block.
- `handoff/02-compose/publication.md` emitted via strip pipeline (Sources kept, frontmatter + footnotes stripped).
- `handoff/02-compose/figures-rationale.md` and `handoff/02-compose/thesis-trace.md` emitted.
- `thesis-trace.md` carries a `## Signature lines` section with 0-3 exact strings (`none` if zero) plus the selected title-lead register.
- The lead's ¶1 opens on the selected register's beat; the full two-sided call lands by the lead section's end; no verdict-insurance fact precedes the beat.
- Per-section word counts within ±20% of plan.
- Mode and posture used logged in opening response.
- Every `[XXXX]` traces to an entry in `invention-summary.md` Quotable spans or Quote anchor table.

## Output format (short example)

```markdown
---
essay_id: 044-tesla-rcm-vindication
patent_reference: US 2026/0125022 A1
spine_source: handoff/01-design/thesis-spine.md
draft_version: 1
mode_used: walkthrough
posture_used: measured
closing_posture: firm   # copied from thesis-spine.md; read by gate_hedge
---

# <Title>

## §1 <Lead title>

<Prose with inline cites [0016]. External baseline (Bosch ECU spec sheet).>

*FIG. 1: <caption>.*

## §N <Closing title>

...

# Sources

## Patents
- US 2026/0125022 A1 — Predictive Airbag Deployment using Vehicle Vision Data

## Technical specs
- Bosch ECU spec sheet — <URL>
```

Full schema → `handoff-template/02-compose/essay-draft.md`. Strip pipeline → `references/strip-pipeline.md`.

## Out of scope

- Thesis design — Phase 1 `thesis-architect`.
- Voice judgment — `voice-canon-lookup` returns examples; this skill applies them.
- Editorial review — Phase 3 `editorial-review`.
- Promo digest — Phase 4 `promo-composer`.
- Korean essay — v2 deliberately drops `tech-essay-ko-pub`; this skill is English only.

## References

- `references/mode-spec.md` — mode + posture detail, mid-pipeline shifts, posture-by-mode scope rules.
- `references/section-blueprint.md` — per-section planning, closing directive, sources structure plan, mode hint.
- `references/figure-rendering.md` — 4 caption_role types, header vs body rendering modes.
- `references/citation-format.md` — `[XXXX]` patent paragraph citations + external attribution rules.
- `references/strip-pipeline.md` — draft.md → publication.md reproducible pipeline.
- `references/revision-mode.md` — loop revision protocol: disposition-first, fix-at-source, grounding fix priority, recount-after-split, revision-response file.
- `references/x-articles-format-en.md` — X Articles platform spec (markdown rendering, tables-as-image, Sources block structure, 5-category enum).
- `references/execution-boundary.md` — Plan ⊥ Execute rules, blueprint gap handling, mode-by-posture scope.
