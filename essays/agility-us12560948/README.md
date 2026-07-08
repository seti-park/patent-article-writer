# Agility Robotics moat analysis — US 12,560,948 B2 (formal pipeline run)

An investor-facing technical-moat article on Agility Robotics' granted safety patent
US 12,560,948 B2 ("Escalating hazard-response of dynamically stable mobile robot in a
collaborative environment"), produced through the full `patent-essay` pipeline
(Phase 1 Design → Phase 2 Compose → Phase 3 Edit loop).

This run **supersedes** the earlier ad-hoc article on the same patent. It carries a prior
lesson: the ad-hoc run passed the loop but closed over-defensively, so this run pins a firm,
evidence-proportionate closing posture in Phase 1 and drafts it in from the start.

## Final deliverable

- `essay-final.md` — the clean, reader-facing article (publication form: frontmatter and
  footnote markers stripped, `# Sources` kept). ~1,560 words of body.

## How it was produced (artifacts)

| Stage | Files |
|---|---|
| Phase 1 Design (`thesis-architect`, voice-off) | `handoff/01-design/`: invention-summary (+ claim-scope map), thesis-spine (+ firm-closing posture), thesis-candidates, fact-check-log, figure-selection, figure-rationale, phase2-handoff-notes, search-log, figures-index |
| Phase 2 Compose (`essay-en-composer`, voice-on) | `handoff/02-compose/`: essay-draft, publication, thesis-trace, figures-rationale |
| Phase 3 Edit (`editorial-review`, voice-fenced) | `handoff/03-edit/`: edit-log (6-pass + firm-closing guard), essay-final, gate-result.json, score-history |
| Run evidence (top level) | `edit-log.md`, `score-history.md`, `gate-result.json`, `essay-context.md` |
| Figures | `figures/fig-05-sequence.png` (cover strip) + `fig-01.png`, `fig-03.png`, `fig-06.png`; full kneel-sequence composites `fig-05AF/GO/PX/YAD.png` |

## Result

- Deterministic gates: all six PASS, zero findings.
- Editorial loop: **PASS on iteration 1** (cap 4). The defects the ad-hoc run hit (over-long
  paragraphs, an over-hedged verdict) were prevented upstream, so the loop confirmed rather than
  repaired. See `score-history.md`.

## The thesis in one line

Agility's defensible technology here is not locomotion. It is the graduated, clearance-aware,
center-of-gravity-lowering way a dynamically stable robot comes to rest near a person, the
capability that lets a humanoid leave the cage and work beside people. The verdict is a firm yes,
with its boundaries drawn.

## Reproduce the validation

```
python .claude/skills/_shared/scripts/run_gates.py \
  --draft essays/agility-us12560948/essay-final.md \
  --invention-summary essays/agility-us12560948/handoff/01-design/invention-summary.md \
  --figures essays/agility-us12560948/handoff/01-design/figures-index.txt \
  --figure-selection essays/agility-us12560948/handoff/01-design/figure-selection.md
```

## Scope note

A technical and strategic read for investor diligence, not a legal opinion on claim validity or
freedom to operate. Market and financing facts are sourced from public reporting and are external
to the patent; the patent does not establish them.
