# patent-essay-pipeline

Refactor of [`patent-essayist`](https://github.com/seti-park/patent-essayist) with an
**Understand-first** control plane.

English patent (+ figures) → frozen patent model for the **Owner** → angled thesis →
English essay (X Articles / retail investor) → Korean briefing + promo pack.

## Why a new repo

`patent-essayist` grew by scar-driven patches. Quality mechanisms are strong; the
**control plane** was patchwork. This fork:

1. Makes **`understand`** the first content stage (Problem · Solution · Benefits)  
2. Stops Design from angling before the Owner has a study pack  
3. Thins `CLAUDE.md` into a router; truth lives in `contracts/`  
4. Names roles: Owner / Orchestrator / Stage worker  
5. Adds run **profiles** (`understand-only`, `draft`, `publish`, …)  

Legacy essays under `essays/` and the gate suite are preserved.

## Quick start

```bash
# Full publish path (default)
# /patent-essay input/patent.md --profile publish

# Owner study only (kills the self-study bottleneck)
# /patent-essay input/patent.md --profile understand-only

python3 meta/regression.py
```

Inputs: `input/patent.md`, `input/figures/` or `figures-raw/`, optional `essay-context.md`.

## Docs

| Doc | Purpose |
|-----|---------|
| [`CLAUDE.md`](./CLAUDE.md) | Operator brief (always-on) |
| [`docs/architecture/CURRENT.md`](./docs/architecture/CURRENT.md) | Living architecture |
| [`contracts/pipeline.yaml`](./contracts/pipeline.yaml) | Stage graph + profiles |
| [`contracts/glossary.md`](./contracts/glossary.md) | Roles |
| [`docs/architecture/history/`](./docs/architecture/history/) | Historical overhauls (not live runbooks) |

## Understand triad

| # | Aspect | Owner question |
|---|--------|----------------|
| 1 | Problem | What was wrong? |
| 2 | Solution | How does this invention fix it (mechanism + claim scope)? |
| 3 | Benefits | What upside does the patent assert? |

Primary learning artifact: `handoff/00-understand/owner-study-pack.md`.

## Status

Active refactor fork. See `meta/CHANGELOG.md` for applied system patches.
