# System CHANGELOG

One line per applied control-plane / skill / gate change. Proposal details live under
`meta/improvement-proposals/`.

## 2026-07-09 — patent-article-writer (understand-first)

- **New repo** `patent-article-writer` (was briefly `patent-understand-pipeline`) from
  `patent-essayist` snapshot.
- **Stage `understand`** (`patent-understand` / `patent-reader`): Problem · Solution · Benefits triad, `owner-study-pack.md`, invention-summary, owner-briefing, figure-primer; gates via `gate_quotes`.
- **Design slimmed**: `thesis-architect` consumes frozen understand/; does not re-extract summary.
- **Contracts layer**: `contracts/pipeline.yaml`, `contracts/stages/*`, `glossary.md`, `invariants.md`.
- **Thin CLAUDE.md** + `docs/architecture/CURRENT.md`; historical docs → `docs/architecture/history/`.
- **Profiles**: understand-only | draft | publish | wire | promo-only.
- **check_run RUN-009**: require understand triad when `00-understand/` present; RUN-008 accepts briefing from 00-understand or 01-design.
