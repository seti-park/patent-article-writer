# Architecture — CURRENT (patent-article-writer)

**Status:** living. Historical overhauls live in `docs/architecture/history/`.

## What this system is

A multi-agent pipeline that turns an English patent (+ figures) into:

1. A frozen **patent understanding** (Problem · Solution · Benefits) for the Owner  
2. An angled **thesis** and English **essay** for retail-investor readers  
3. Korean **owner briefing** + **promo pack**  
4. Mechanical proof the quality loop actually ran  

## Stage graph

```
figures? → understand → [owner confirm] → design → compose ⇄ review_loop
         → self_audit? → polish? → verify → archive → promo? → retro?
```

| Stage | Skill | Output root |
|-------|--------|-------------|
| figures | patent-figures-clean | `input/figures/` |
| **understand** | **patent-understand** | **`handoff/00-understand/`** |
| design | thesis-architect | `handoff/01-design/` |
| compose | essay-en-composer | `handoff/02-compose/` |
| review_loop | editorial-review | `handoff/03-edit/` |
| self_audit | adversarial-reader, grounding-verifier | `03-edit/selfaudit-*` |
| polish | prose-polish | polish-notes |
| verify | check_run.py, run_gates.py | — |
| archive | orchestrator | `essays/`, `runs/` |
| promo | promo-composer | `essays/<id>/promo/` |
| retro | pipeline-retro | `meta/` |

Profiles: `contracts/pipeline.yaml` (`understand-only`, `draft`, `publish`, `wire`, `promo-only`).

## Understand triad (north star of stage 1)

| Aspect | Meaning |
|--------|---------|
| Problem | What this document says was wrong |
| Solution | Mechanism + claim scope (locked/open/pinned or sought-*) |
| Benefits | Effects the **patent** asserts |

Owner artifact: `owner-study-pack.md`. Machine warehouse: `invention-summary.md`.

## Load-bearing quality mechanisms

- Physical agent isolation (compose ≠ review context)  
- Double-clean on `publish`  
- Composer never reads raw patent  
- gate_quotes / gate_anchors / gate_hedge / gate_figure_use / gate_surface  
- Grounding fix priority: anchor → narrow → label → cut  
- Meta-loop propose-only + `meta/regression.py`  

## Control plane files

| File | Role |
|------|------|
| `CLAUDE.md` | Thin operator brief |
| `contracts/pipeline.yaml` | Graph + profiles |
| `contracts/stages/*.yaml` | I/O contracts |
| `contracts/glossary.md` | Owner / Orchestrator / Stage worker |
| `contracts/invariants.md` | Never-break list |
| `.claude/skills/patent-essay/SKILL.md` | Orchestrator runbook |

## Relationship to patent-essayist

This repo is a **refactor fork** of `seti-park/patent-essayist`. Legacy essays and
gates are preserved; the control plane is understand-first and contract-driven.
Scar history: `docs/architecture/history/`.
