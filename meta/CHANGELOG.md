# System CHANGELOG

One line per applied control-plane / skill / gate change. Proposal details live under
`meta/improvement-proposals/`.

## 2026-07-14 — GPT lane: prompt on stdin, not argv

- **`cli_lane.py` GPT lane**: prompt now reaches `codex exec` via stdin (`codex exec -`)
  instead of riding on argv. Linux caps a single argv entry at 128 KiB (`MAX_ARG_STRLEN`),
  so every prompt above that failed `execve` with `E2BIG` *before any network call* and
  fell back to Claude. Compose-lane prompts measure 165-434 KB, so `--compose-vendor gpt`
  could never have worked; pregate prompts already reach 69 KB (53% of the ceiling).
  Grok was unaffected (it takes `--prompt-file`).
- **New substitute reason `exec-failed`**: an `OSError` from `subprocess.run` means the CLI
  never produced an exit status. It used to be reported as `nonzero`, which read as "the CLI
  ran and failed" and hid the real cause. Contract updated in `contracts/stages/self_audit.yaml`.
- **Regression**: `test_cli_lane.py` gains a >128 KiB prompt round-trip, an argv-purity check
  (`codex` argv ends in `-`, carries no prompt bytes), and an `exec-failed` case. The existing
  never-EOF-stdin guard now also asserts the child received the prompt itself.

## 2026-07-09 — patent-article-writer (understand-first)

- **New repo** `patent-article-writer` (was briefly `patent-understand-pipeline`) from
  `patent-essayist` snapshot.
- **Stage `understand`** (`patent-understand` / `patent-reader`): Problem · Solution · Benefits triad, `owner-study-pack.md`, invention-summary, owner-briefing, figure-primer; gates via `gate_quotes`.
- **Design slimmed**: `thesis-architect` consumes frozen understand/; does not re-extract summary.
- **Contracts layer**: `contracts/pipeline.yaml`, `contracts/stages/*`, `glossary.md`, `invariants.md`.
- **Thin CLAUDE.md** + `docs/architecture/CURRENT.md`; historical docs → `docs/architecture/history/`.
- **Profiles**: understand-only | draft | publish | wire | promo-only.
- **check_run RUN-009**: require understand triad when `00-understand/` present; RUN-008 accepts briefing from 00-understand or 01-design.
