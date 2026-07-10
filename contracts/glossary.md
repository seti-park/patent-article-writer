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
| **OWNER_QUESTION** | Structured block a forked worker emits to request an Owner decision; orchestrator relays it as a checkpoint instance. Shape: `OWNER_QUESTION:` / `FILES:` / optional `DEFAULT:`. Under `--yes`, a missing `DEFAULT:` aborts the run (no guessing); a present `DEFAULT:` is used and recorded in the run report. |
| **comprehension loop** | Optional mode of `understand_confirm`: interactive Owner quiz + teach at the checkpoint (design: `docs/architecture/comprehension-loop.md`). P2 = keyed grading + pass predicate + claim-scope hard STOP. |
| **comprehension-quiz** | `handoff/00-understand/comprehension-quiz.md` — worker-produced keyed bank (IF-2): per item `question:` / `options:` / `key:` / `aspect:` (`problem\|claim-scope\|benefits\|boundary`) / `rationale:`. ≥1 item per aspect; claim-scope mandatory. |
| **comprehension-notes** | `handoff/00-understand/comprehension-notes.md` — teaching brief from the comprehension dialogue (stumble points, framing that landed, Owner-declared crux, claim-scope framing). |
| **explanation-prior** | Framing/emphasis guidance from the Owner's learning dialogue; never a fact source (facts stay in invention-summary / owner-study-pack). |
| **comprehension** (confirm field) | On `understand-confirmed.md` (IF-1): `demonstrated` \| `self-asserted` \| `skipped-unattended` \| `risk-accepted`. `risk-accepted` requires notes string `claim-scope risk accepted by owner`. |
| **claim-scope hard STOP** | On a second miss of the `claim-scope` quiz item, the checkpoint does not advance; Owner must re-answer after re-read or accept risk in writing (§4.3). |

## Run identity

| Term | Meaning |
|------|---------|
| **run_id** | `<assignee>-<publication-number>[-<suffix>]` lowercased (e.g. `intel-us20250266395`), matching `essays/` directory names. Governed suffixes: `-r2`/`-r3`… = a re-run of the same patent; `-<topic>` (lowercase kebab, e.g. `-backend-hbm`) = an optional **human-readable keyword** that both distinguishes multiple editions of one patent *and* keeps ids scannable as the corpus grows — bare `<assignee>-us<number>` ids blur together at scale, so a topic keyword is **encouraged** for new runs. Never retrofit a suffix onto an existing id: `essay_id` is an append-only ledger key, so a rename would rewrite history (see `pipeline-retro/references/ledger-schema.md`); existing bare ids stay bare. Generated at bootstrap. `essay_id` ≡ `run_id`. Written to `handoff/run-manifest.md`. |

## Legacy alias

If you see **SETI** in historical docs under `docs/architecture/history/` or
`docs/source-prompts/`, read it as **Owner**. Live skills should say Owner / Orchestrator / Stage worker only.
