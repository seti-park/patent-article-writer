---
name: thesis-architect
description: >
  Stage `design`: angles a frozen patent model into thesis-spine, title-lead candidates,
  figure↔thesis map, fact-check-log. Consumes handoff/00-understand/ (or 01-design compat
  copies of invention-summary + owner-briefing). Does NOT re-extract the patent triad —
  that is patent-understand. Use after understand is complete. NOT for: raw patent first
  read (patent-understand), prose (essay-en-composer), review, promo.
context: fork
agent: design-architect
---

# thesis-architect (stage: design)

**Contract:** `contracts/stages/design.yaml`  
**Handoff:** `handoff/01-design/`  
**Upstream:** `handoff/00-understand/` must already exist (orchestrator enforces).

Design **angles** a frozen patent model. It does not re-teach the patent.

```
handoff/00-understand/ (invention-summary, study pack, briefing, figure-primer)
  + context research + essay-context
    → thesis candidates → 4-axis → Q7 → adversarial defense
    → thesis-spine.md (+ closing_posture)
    → title-lead-candidates.md
    → figure-selection.md / figure-rationale.md  (figure ↔ thesis)
    → fact-check-log.md / search-log.md / phase2-handoff-notes.md
    → optional: owner-briefing §⑤ promo-link update only
```

## When to invoke

After `patent-understand` completed (or Owner provided equivalent 00-understand bundle).
Standalone “design only” requires existing invention-summary + owner-briefing under
`01-design/` or `00-understand/`.

If `handoff/00-understand/invention-summary.md` is missing **and**
`handoff/01-design/invention-summary.md` is missing → **STOP** and tell the orchestrator
to run `patent-understand` first. Do not silently extract a new summary unless the
orchestrator explicitly passes `repair-understand` (then write Revision notes and prefer
re-running understand).

**Understand confirm (CD-03 residual):** if `handoff/00-understand/understand-confirmed.md`
is absent or its `status:` is not `confirmed` → **STOP** and return
`STOPPED: understand_confirm not satisfied`. Exception: soft profiles — when the
orchestrator passes `owner_confirm: soft` in the fork instruction, proceed (soft path
never writes a confirm file; RUN-010 is the verify-time backstop only).

## Process

### 0. Load frozen model

Read (prefer 00-understand, fall back to 01-design compat copies):

- `invention-summary.md` — sole patent mechanism source for angling  
- `owner-study-pack.md` — triad Problem · Solution · Benefits  
- `owner-briefing.md` — Korean shelf  
- `figure-primer.md` — factual figure inventory  
- `open-questions.md` — Owner answers if any  

**Do not rewrite invention-summary** unless a blocking error is found; if found, append
`> Revision note` and ask orchestrator to re-run understand for material changes.

### 1. Context research

Web-search for industry baseline, corporate narratives, prior launches. Log every query
to `search-log.md`. Classify framing-impact (main thread / paragraph / footnote). Feeds
baseline-difference axis. See `references/context-research.md`.

**Owner briefing §⑤ only:** after research, you may update
`owner-briefing.md` section ⑤ (프로모션 연결) and sync the copy under `00-understand/`
if present. Leave ①–④ and ⑥ untouched unless understand was wrong (then re-run understand).

### 2. Thesis candidate generation

2–4 candidates, single-spine default. Each carries draft 4-axis grounding grounded in the
**frozen** summary/triad — do not invent a new mechanism. Write `thesis-candidates.md`.
See `references/thesis-candidate-presentation.md`.

### 3. 4-axis grounding lock

Claims / problem / effect / baseline-difference. Missing axis disqualifies. See
`references/4-axis-grounding.md`. Problem/effect axes should align with study-pack triad.

### 4. Q7 hook gate (hard)

Exactly one of 2 admitted hook patterns. See `references/hook-patterns.md`.

### 5. Adversarial defense

Strongest **THIS-patent** objection; generic patent truisms banned as steelmen. See
`references/adversarial-defense.md`.

### 6. Spine selection

Single-spine default; auto-select recommended candidate; surface for Owner override.
Multi-spine needs explicit override per `references/single-spine-default.md`.

### 7. Spine lock

Write `thesis-spine.md` with 4-axis anchors, Q7, adversarial defense, spine→section trace,
`closing_posture: firm` default for verdict editions (see prior doctrine; pass-6 6G).
Attention budget: at most one `payload: pricing` section. See reader-energy §6 for
procedure-overweight rules.

### 8. Title-lead candidates (energy registers)

Write `title-lead-candidates.md`: five register pairs riding the **same** locked spine.
See `_shared/references/reader-energy.md`. End with `recommended:` line.

### 9. Figure mapping

Write `figure-selection.md` + `figure-rationale.md` mapping figures to **thesis points**
(use figure-primer + invention-summary figure relationships). Cover candidate + phase
keyframes as before.

### 10. Fact-check log seed

External facts the spine relies on → `fact-check-log.md`.

### 11. Compose handoff notes

Write `phase2-handoff-notes.md`: audience reframe, citation priority from Quotable spans,
rejected-candidate rationale, claim-scope traps (from frozen map), attention-budget traps,
open questions for compose (Owner decisions).

Ensure `figures-index.txt` exists.

## Pre / post

**Pre:**

- `handoff/00-understand/` complete **or** compat invention-summary + owner-briefing in 01-design  
- cleaned figures  
- optional `input/essay-context.md` (`reader_sentence`)  
- voice-off (no voice-canon); reader-energy OK for title-leads  

**Post:**

- thesis-spine, thesis-candidates, title-lead-candidates  
- figure-selection, figure-rationale, fact-check-log, search-log, phase2-handoff-notes  
- figures-index.txt  
- invention-summary / owner-briefing still present (owned by understand)

## Out of scope

- First-pass patent extraction → `patent-understand`  
- Prose → `essay-en-composer`  
- Review / promo / polish  

## Feedback loops

If design finds understand was wrong (misread claim, bad quote), **do not silently rewrite
the triad**. Append Revision note, report to orchestrator, prefer re-run understand.

If cascade >2 revisions on the same file → pause and ask **Owner**.

## References

- `contracts/stages/design.yaml`  
- `contracts/glossary.md`  
- `references/*` (4-axis, hooks, adversarial, single-spine, candidates, schemas)  
- `_shared/references/reader-energy.md`  
- `_shared/references/owner-briefing-schema.md` (for §⑤ updates only)  
