# Glossary — roles in this pipeline

Use these terms in all live skills and operator docs. Do not invent synonyms mid-run.

| Role | Who | Authority |
|------|-----|-----------|
| **Owner** | Human publisher (Korean-primary). Formerly called “SETI” in legacy skills. | Confirms Understanding; overrides title/spine; applies human-post-accept edits; applies meta proposals after regression. |
| **Orchestrator** | Main Claude session running `patent-essay`. | Loop policy, gate invocation, arbitration, acceptance calls. Does not write essay prose. |
| **Stage worker** | Forked agent (`.claude/agents/*`) running one skill. | Writes only that stage’s contract outputs; returns a one-line report. |

## Checkpoint vocabulary

| Term | Meaning |
|------|---------|
| **surface** | Render the artifact's CONTENT inline in the assistant response; naming a path is not surfacing. |
| **checkpoint** | A PROCEDURE (RENDER→ASK→STOP→RECORD→RESUME), not a state. See patent-essay SKILL.md "Owner checkpoint protocol". |
| **confirm file** | Disk record written only after Owner affirmative (or `--yes`); validity rules in the protocol. |
| **OWNER_QUESTION** | Structured block a forked worker emits to request an Owner decision; orchestrator relays it as a checkpoint instance. |

## Legacy alias

If you see **SETI** in historical docs under `docs/architecture/history/` or
`docs/source-prompts/`, read it as **Owner**. Live skills should say Owner / Orchestrator / Stage worker only.
