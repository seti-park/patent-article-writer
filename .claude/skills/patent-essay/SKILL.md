---
name: patent-essay
description: >
  Orchestrator for patent-essay-pipeline. Understand-first: figures? → understand →
  (owner confirm) → design → compose ⇄ review_loop → self_audit? → polish? → verify →
  archive → promo? → retro?. Profiles: understand-only|draft|publish|wire|promo-only.
  Loop policy and arbitration ONLY; stage work is forked. Use for end-to-end patent essays.
argument-hint: "[patent] [--profile understand-only|draft|publish|wire|promo-only] [--threshold pass|revise-recommended] [--max-iter N] [--mode essay|wire] [--self-audit on|off] [--yes]"
allowed-tools: Read, Write, Edit, Grep, Glob, Bash, Task, Skill, WebFetch, WebSearch
---

# Patent Essay — Orchestrator

You own **loop policy and arbitration** only. Stage domain work runs in forked agents.
Content travels on disk. Graph + profiles: `contracts/pipeline.yaml`. Roles:
`contracts/glossary.md`. Invariants: `contracts/invariants.md`.

## Parameters

| Flag | Default | Meaning |
|------|---------|---------|
| `--profile` | `publish` | `understand-only` \| `draft` \| `publish` \| `wire` \| `promo-only` |
| `--threshold` | `pass` | Min editorial assessment (`revise-recommended` allowed; never `revise-required`) |
| `--max-iter` | profile default | Max **revision** rounds (confirmation does not count) |
| `--mode` | from profile | `essay` \| `wire` |
| `--self-audit` | from profile | `on` \| `off` |
| `--yes` | off | Skip owner checkpoints (unattended) |

## Model allocation

- **Main / judgment workers** (`patent-reader`, design, compose, review, adversarial, polish, promo): `model: inherit` (session strongest).
- **Mechanical** (`figures-prep`, `grounding-verifier`): cheaper pin OK (`sonnet` class).

## Pipeline by stage

### 0. Figures (optional) — `patent-figures-clean` / figures-prep

If no `input/figures/fig-*.png` but raw source exists → run figures stage.

### 1. Understand (required) — `patent-understand` / patent-reader

Invoke `patent-understand`. Writes `handoff/00-understand/` (triad study pack, summary,
briefing, figure-primer, open-questions) and compat-copies summary/briefing to
`handoff/01-design/`.

**Gates (orchestrator re-runs if worker did not):**

```
python3 .claude/skills/_shared/scripts/gate_quotes.py \
  handoff/00-understand/invention-summary.md \
  --invention-summary handoff/00-understand/invention-summary.md \
  --patent input/patent.md
# same for owner-briefing.md and owner-study-pack.md under 00-understand/
```

**Owner checkpoint (`understand_confirm`):**

- Surface `owner-study-pack.md` + open-questions (and briefing path).
- Profiles: `publish` / `understand-only` → **hard stop** until
  `handoff/00-understand/understand-confirmed.md` exists **or** `--yes` writes it with
  `by: orchestrator-yes-flag`.
- `draft` / `wire` → soft surface; may continue.
- Profile **`understand-only`**: stop here; report study pack paths; do not design.

### 2. Design — `thesis-architect` / design-architect

Only after understand. Consumes frozen `00-understand/` (and 01-design compat copies).
Must **not** recreate invention-summary from scratch. Surfaces title-lead candidates for
Owner override (soft). May update briefing section ⑤ only (promo link) with a Revision note.

### 3. Compose — `essay-en-composer` / essay-composer

Reads design handoff (+ understand spans). **Never** raw patent. Writes `handoff/02-compose/`.

### 4. Review loop — `editorial-review` / editorial-reviewer

Per round N:

1. `run_gates.py` → `handoff/03-edit/gate-result.round-N.json`
2. Fresh forked review → `edit-log.round-N.md`
3. **CLEAN(N)** ⇔ gates pass + assessment ≥ threshold + grounding hard-gate + goal-2 hard-gate + verdict hard-gate  
   (same hard-gates as legacy patent-essayist; see scoring-rubric)

**Acceptance:**

- `publish`: **double-clean** (confirmation round, no revision between cleans)
- `draft` / `wire`: **single-clean** OK
- Cap: explicit `CAP HIT` in score-history only

Revision mode: composer dispositions every medium+ finding → `revision-response.round-N.md`.

### 5. Self-audit (publish)

≥2 adversarial-reader + grounding-verifier + cold reader; multi-vote; fix via revision mode;
normalize deltas to ledger. Cap 3 dry-loop iterations.

### 6. Polish (publish) — `prose-polish`

Surface-only 윤문; drift-verified; zero-new gate findings.

### 7. Verify

```
python3 .claude/skills/_shared/scripts/check_run.py --handoff handoff \
  --threshold <threshold> --self-audit <on|off>
```

Must PASS before archive. Never edit artifacts to satisfy it.

### 8. Archive

- `runs/<essay-id>/` — full round evidence  
- `essays/<essay-id>/` — shelf: essay-final, owner-briefing, **owner-study-pack**, patent.md,
  figures, publication-package, promo, score-history, gate-result, README, handoff tree
  (migration: full handoff still allowed under essays/ until slim-archive lands)

Copy from understand:

- `owner-study-pack.md` → `essays/<id>/owner-study-pack.md`
- `owner-briefing.md` → `essays/<id>/owner-briefing.md`
- `patent.md` snapshot from input

### 9. Promo (publish) — `promo-composer`

Post-archive; never edits essay; safe-claims grounding.

### 10. Retro — `pipeline-retro`

Propose-only; surface top proposal one line.

## Final report to Owner

- Profile used + understand confirm status  
- Study pack + briefing paths  
- Final essay (if any)  
- Promo (if any)  
- Score history + check_run line  
- CAP HIT / open findings if any  

## Optional /goal

```
/goal patent-essay complete for profile: understand artifacts + (if publish) check_run 0,
double-clean or CAP HIT, gates green, owner-study-pack archived
```
