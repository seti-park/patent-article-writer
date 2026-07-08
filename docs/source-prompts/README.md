# Source prompts — HISTORICAL only (not loaded at runtime)

**Status: archive.** Live skills are under `.claude/skills/`. Do not edit these as
runbooks; they may **differ** from live ports. See `docs/architecture/CURRENT.md`.

The patent-essay system was originally run as separate claude.ai Projects. Originals
were snapshotted here; bodies were ported into `.claude/skills/`.

| Dir | Original skill(s) | Ported into | Status |
|-----|-------------------|-------------|--------|
| `01-design/thesis-architect/`     | Phase 1 Design (voice-off)   | `.claude/skills/thesis-architect/` + understand split → `patent-understand` | ported (diverged) |
| `02-compose/essay-en-composer/`   | Phase 2 Compose (voice-on)   | `.claude/skills/essay-en-composer/` | ported (diverged) |
| `02-compose/voice-canon-lookup/`  | Phase 2 voice helper          | `.claude/skills/voice-canon-lookup/` | ported |
| `03-edit/editorial-review/`       | Phase 3 Edit (voice-fenced)  | `.claude/skills/editorial-review/` | ported (diverged) |
| `04-promote/promo-composer/`      | Phase 4 Promote               | `.claude/skills/promo-composer/` | **ported** (this table used to say otherwise) |

## How the port works

The live skills under `.claude/skills/` are the real ported bodies (SKILL.md + their own
`references/`, and voice-canon-lookup's `voice-canon/` corpus). This folder is the canonical
record of the originals — the live system reads from `.claude/skills/`, not from here. When
porting `promo-composer`, copy its body into a new `.claude/skills/promo-composer/`, map any
Project Knowledge it needs to `_shared/references/`, and keep its output contract
(`handoff/04-promote/promotion-post.md`) intact.
