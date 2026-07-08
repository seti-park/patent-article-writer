# Source prompts — original claude.ai assets (preserved)

The patent-essay system was originally run as separate claude.ai Projects, each with its own
Instructions + Knowledge + skill. The **five original skills are preserved here verbatim** as
the reference baseline; their real bodies have been **ported into `.claude/skills/`**.

| Dir | Original skill(s) | Ported into | Status |
|-----|-------------------|-------------|--------|
| `01-design/thesis-architect/`     | Phase 1 Design (voice-off)   | `.claude/skills/thesis-architect/` | ported |
| `02-compose/essay-en-composer/`   | Phase 2 Compose (voice-on)   | `.claude/skills/essay-en-composer/` | ported |
| `02-compose/voice-canon-lookup/`  | Phase 2 voice helper          | `.claude/skills/voice-canon-lookup/` | ported (incl. 33-entry canon) |
| `03-edit/editorial-review/`       | Phase 3 Edit (voice-fenced)  | `.claude/skills/editorial-review/` | ported |
| `04-promote/promo-composer/`      | Phase 4 Promote               | — | **preserved, not yet ported** |

Phase 4 Promote and Layer-1 figure cleaning are out of scope for this conversion. The
`promo-composer` source is kept here so it can be ported later without re-supplying it.

## How the port works

The live skills under `.claude/skills/` are the real ported bodies (SKILL.md + their own
`references/`, and voice-canon-lookup's `voice-canon/` corpus). This folder is the canonical
record of the originals — the live system reads from `.claude/skills/`, not from here. When
porting `promo-composer`, copy its body into a new `.claude/skills/promo-composer/`, map any
Project Knowledge it needs to `_shared/references/`, and keep its output contract
(`handoff/04-promote/promotion-post.md`) intact.
