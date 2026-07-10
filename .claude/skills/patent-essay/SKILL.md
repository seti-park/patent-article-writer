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

## Owner checkpoint protocol (STOP/CONFIRM)

Every owner checkpoint is a PROCEDURE, not a state. When the orchestrator reaches one:

1. **RENDER** — print the checkpoint's required content INLINE in the assistant
   response (actual content, never just file paths). Each checkpoint defines its
   render block (see the stage contract's `owner_checkpoint.render`).
2. **ASK** — utter the checkpoint's `question:` from the stage contract verbatim,
   then list the Owner's options (confirm / edit open-questions / re-run stage).
3. **STOP** — end the assistant turn immediately after ASK. In the same turn it is
   FORBIDDEN to: invoke the next stage, call Task/Skill for any downstream worker,
   or write the confirm file. "Hard stop" means: no further tool calls this turn.
4. **RECORD** — only in a LATER turn, after the Owner has replied with an explicit
   affirmative to the ASK question, write the confirm file (`by: owner`, quote the
   Owner's confirming utterance in `notes:`). `--yes` is the ONLY path that writes
   without an Owner utterance (`by: orchestrator-yes-flag`). The stage worker never
   writes the confirm file.
5. **RESUME** — on any (re-)entry into the graph: if a VALID confirm file for the
   CURRENT patent exists, continue to the next stage without re-asking; otherwise
   run RENDER→ASK→STOP again.

Soft checkpoints (`draft`/`wire` profiles): RENDER and ASK are still mandatory;
STOP is waived — the orchestrator may proceed in the same turn after rendering,
noting "soft checkpoint: continuing; reply to override".

Confirm-file validity (all required):
- `status: confirmed`
- `by: owner` or `by: orchestrator-yes-flag`
- `date:` is a real date (placeholder `<YYYY-MM-DD>` ⇒ INVALID)
- `patent:` matches the identifier of the current `input/patent.md`

Checkpoint instances: `understand_confirm` (hard on publish/understand-only),
`cap_hit` (hard unless `--yes`), worker-raised `OWNER_QUESTION` relays (hardness
follows the raising stage's profile), design title-lead override (soft).

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

**Owner checkpoint (`understand_confirm`) — protocol instance:**

Follow **Owner checkpoint protocol (STOP/CONFIRM)** above. This instance:

1. **RENDER** (per `contracts/stages/understand.yaml` `owner_checkpoint.render`):
   - `owner-study-pack.md` "한 줄" line, then a 2–4 sentence summary of each of
     Problem / Solution / Benefits (Korean, from the study pack)
   - `open-questions.md` in full
   - the five output paths (study pack, briefing, invention-summary, figure-primer,
     open-questions)
2. **ASK** — utter the stage contract `question:` verbatim:
   > Can you restate Problem, Solution (incl. claim scope), and Benefits without
   > reopening the full patent? If yes, confirm. If no, edit open-questions or
   > request re-run of understand.
3. **STOP** — hard on `publish` / `understand-only` (end turn; no design, no Task/Skill
   for downstream, no confirm-file write this turn). Soft on `draft` / `wire` (RENDER
   and ASK still mandatory; may continue same turn with "soft checkpoint: continuing;
   reply to override").
4. **RECORD** — only after Owner's explicit affirmative in a later turn, write
   `handoff/00-understand/understand-confirmed.md` (`by: owner`, quote utterance in
   `notes:`). **`--yes` only** writes without Owner utterance
   (`by: orchestrator-yes-flag`). Stage worker never writes this file.
5. **RESUME** — valid confirm file for the current patent (see protocol validity) ⇒
   skip to design without re-asking; else RENDER→ASK→STOP again.

**Forbidden on hard checkpoints:** invoking design (or any next stage) in the same turn
as ASK; writing the confirm file without an Owner utterance (except `--yes`).

Profile **`understand-only`**: after confirm (or soft continue), stop; do not design.

### 2. Design — `thesis-architect` / design-architect

Only after understand. Consumes frozen `00-understand/` (and 01-design compat copies).
Must **not** recreate invention-summary from scratch. Surfaces title-lead candidates for
Owner override (soft checkpoint: RENDER candidates + ASK; STOP waived). May update
briefing section ⑤ only (promo link) with a Revision note. Cascade pauses that need an
Owner decision use the **OWNER_QUESTION relay** (below).

### 3. Compose — `essay-en-composer` / essay-composer

Reads design handoff (+ understand spans). **Never** raw patent. Writes `handoff/02-compose/`.
Inside the pipeline the forked worker runs **strict-execution** only; gap-stops and
mode-shift proposals go through the **OWNER_QUESTION relay**, not in-session elicitation.

### 4. Review loop — `editorial-review` / editorial-reviewer

Per round N:

1. `run_gates.py` → `handoff/03-edit/gate-result.round-N.json`
2. Fresh forked review → `edit-log.round-N.md`. **Orchestrator assigns `round_type`** in
   the fork instruction: `confirmation` or `revision`. Reviewer writes
   `round_type: confirmation | revision` in the edit-log header. Confirmation rounds
   have no `revision-response.round-N.md` (if one exists, the round counts as revision).
3. **CLEAN(N)** ⇔ gates pass + assessment ≥ threshold + grounding hard-gate + goal-2 hard-gate + verdict hard-gate  
   (same hard-gates as legacy patent-essayist; see scoring-rubric)
4. After each round, append one row to `handoff/03-edit/score-history.md`
   (template: `handoff-template/03-edit/score-history.md`):
   `round | round_type | assessment | gates | clean | notes`.

**Acceptance:**

- `publish`: **double-clean** = one clean **revision-signal** (or first-clean) round + one
  clean **confirmation** round with **no revision between**
- `draft` / `wire`: **single-clean** OK
- Cap: see **CAP HIT** below

Revision mode: composer dispositions every medium+ finding → `revision-response.round-N.md`.

**Arbitration (LOOP-07):** after one full reject→re-assert cycle on the same finding id,
the orchestrator must rule (`apply` / `sustain rejection` / escalate to Owner as
`OWNER_QUESTION`) and record the ruling in that round's edit-log under `arbitration:`.

#### CAP HIT (owner checkpoint `cap_hit`)

Reaching `max_revision` without acceptance is an owner checkpoint:

1. **RENDER** — last round's edit-log summary + the full `score-history.md` table.
2. **ASK** — "ship last draft as-is, revise once more with narrowed scope, or stop?"
3. **STOP** — hard unless `--yes`. With `--yes`: ship the **last draft**, append a
   score-history row with `notes: CAP HIT`.
4. What ships on cap: the **LAST draft** only (never a "best round" selection).
5. Downstream after a cap-accepted ship: `self_audit` and later stages still run on
   `publish`.

### 5. Self-audit (publish)

≥2 adversarial-reader + grounding-verifier + cold reader; multi-vote; fix via revision mode;
normalize deltas to ledger. Cap 3 dry-loop iterations.

### 6. Polish (publish) — `prose-polish`

Surface-only 윤문; zero-new gate findings.

**Two-step drift check (AUD-W7):**

1. Polish worker returns a changed-sentence list and marks `drift-check PENDING` in its
   final message (worker does **not** spawn the verifier).
2. Orchestrator forks `grounding-verifier` on old/new pairs. Any `MEANING-CHANGED` ⇒
   re-fork polish to revert that sentence; re-run gates as needed.

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

## Worker-raised questions (OWNER_QUESTION relay)

Any forked worker that needs an Owner decision ends its final message with:

```
OWNER_QUESTION: <question>
FILES: <paths>
```

The orchestrator treats this as a checkpoint instance of the Owner checkpoint protocol:

1. **RENDER** — the worker's named files (content inline) + the question text.
2. **ASK** — the question (and options if the worker supplied them).
3. **STOP** — hard/soft per profile and `--yes` (same rules as other checkpoints).
4. After Owner reply (or `--yes` with a recorded default), re-invoke the worker with the
   answer.

Covers: compose gap-stops, design cascade pauses, mode-shift proposals. In-pipeline
compose does not elicit mid-session; it raises `OWNER_QUESTION` instead.

## Final report to Owner

Each checkpoint reports at its own STOP; this is the end-of-run summary only — it never
substitutes for a checkpoint.

- Profile used + understand confirm status  
- Confirm-file path + `by:` value  
- Study pack + briefing paths  
- Final essay (if any)  
- Promo (if any)  
- Score history + check_run line  
- CAP HIT / open findings if any  

## Optional /goal

```
/goal patent-essay complete for profile: understand artifacts + understand-confirmed.md valid
+ (if publish) check_run 0, double-clean or CAP HIT, gates green, owner-study-pack archived
```
