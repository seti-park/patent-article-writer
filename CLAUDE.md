# Patent Article Writer

Skill-based system: English patent (+ figures) → English X Articles **article** for a
curious retail investor, plus a Korean **owner** briefing and promo pack.

Repo: `patent-article-writer`. Fork of `patent-essayist` with an **Understand-first**
control plane: the patent model is frozen and owner-confirmed before any thesis angle
is chosen.

## North-star goals

Full matrix: `.claude/skills/_shared/references/scoring-rubric.md`.

1. Catch the patent's core accurately  
2. Use figures + specification sufficiently  
3. Easy for the reader to understand  
4. Well-structured (4a) and natural (4b) — including firm, evidence-proportionate verdicts  
5. Reader energy — lead hooks; leave with a repeatable sentence  

**Owner contract (beside the rubric):** understanding must reach the publisher
(Korean study pack + briefing) as well as the reader (essay + promo).

## How to run

```
/patent-essay <patent path | text | number> \
  [--profile understand-only|draft|publish|wire|promo-only] \
  [--threshold pass|revise-recommended] [--max-iter 4] \
  [--mode essay|wire] [--self-audit on|off] [--yes]
```

- **`publish`** (default essay): full graph including owner confirm after Understand  
- **`understand-only`**: triad study pack + briefing; stop (kills the self-study bottleneck)  
- **`draft`**: understand → design → compose → review (single-clean); no audit/polish/promo  
- **`--yes`**: skip owner checkpoints (unattended only)

Inputs: `input/patent.md`, `input/figures/` or `figures-raw/`, optional `essay-context.md`. Provisioned by **Run bootstrap** (argument → `input/patent.md`, stale-workspace reset, `handoff/run-manifest.md`).

## Stage graph (names, not phase numbers)

```
figures? → understand → [owner confirm] → design → compose ⇄ review_loop
         → self_audit? → polish? → verify → archive → promo? → retro?
```

`[owner confirm]` = hard STOP/CONFIRM checkpoint; `?` = optional stage

| Stage | Skill / agent | Job |
|-------|----------------|-----|
| `figures` | patent-figures-clean / figures-prep | raw drop → fig-NN.png |
| `understand` | patent-understand / patent-reader | **Problem · Solution · Benefits** triad + invention-summary + owner study pack |
| `design` | thesis-architect / design-architect | angle only — consumes frozen understand/ |
| `compose` | essay-en-composer / essay-composer | draft; never raw patent |
| `review_loop` | editorial-review / editorial-reviewer | gates + fresh review; double-clean on publish |
| `self_audit` | adversarial-reader + grounding-verifier | post-accept blind pass |
| `polish` | prose-polish | surface 윤문, drift-checked |
| `verify` | check_run.py + run_gates.py | mechanical completeness |
| `promo` | promo-composer | KR long + EN thread; safe-claims |
| `retro` | pipeline-retro | propose-only system learning |

Profiles and required files: `contracts/pipeline.yaml`, `contracts/stages/`.

## Hard invariants (never violate)

1. **Physical isolation** — compose and review never share agent context  
2. **Double-clean on `publish`** — one clean round is a hypothesis  
3. **Composer never reads raw patent** — only Quotable spans from understand/design  
4. **Understand before design** — no thesis candidates until triad artifacts exist  
5. **Owner confirm on `publish`** — via the Owner checkpoint protocol (STOP/CONFIRM) in the orchestrator runbook; unless `--yes`  
6. **Grounding fix priority** — anchor → narrow → label → cut (never “add a hedge”)  
7. **Meta-loop is propose-only** — humans apply after `meta/regression.py`  

## Where truth lives

| Concern | Source |
|---------|--------|
| Stage graph / profiles | `contracts/pipeline.yaml` |
| Stage I/O contracts | `contracts/stages/*.yaml` |
| Roles | `contracts/glossary.md` |
| Invariants (expanded) | `contracts/invariants.md` |
| Orchestrator runbook | `.claude/skills/patent-essay/SKILL.md` |
| Living architecture | `docs/architecture/CURRENT.md` |
| Historical overhauls | `docs/architecture/history/` |
| Gates + fixtures | `_shared/scripts/`, `meta/regression.py` |

## Glossary (short)

- **Owner** — human publisher (formerly “SETI” in older docs)  
- **Orchestrator** — main session: loop policy only  
- **Stage worker** — forked agent for one stage  

## Regression

```
python3 meta/regression.py
```
