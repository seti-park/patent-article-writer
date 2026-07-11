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
| `--comprehension-check` | from profile | `on` \| `off` — interactive Owner comprehension check at understand_confirm |
| `--yes` | off | Skip owner checkpoints (unattended) |

**`--comprehension-check` defaults:** **on** for `publish` and `understand-only`;
**off** for `draft` / `wire`; **forced off** under `--yes` (no Owner present to quiz).

**`--profile promo-only`:** positional argument MUST be an existing `essays/<id>/` id
(resolved against `essays/`). Missing or ambiguous id ⇒ ask the Owner before promo.

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

Hardness is a property of the **checkpoint instance × profile**, not of the profile
alone. Soft checkpoints: RENDER and ASK are still mandatory; STOP is waived — the
orchestrator may proceed in the same turn after rendering, noting "soft checkpoint:
continuing; reply to override" in the run report.

Confirm-file validity (all required):
- `status: confirmed`
- `by: owner` or `by: orchestrator-yes-flag`
- `date:` is a real date (placeholder `<YYYY-MM-DD>` ⇒ INVALID)
- `patent:` matches the identifier of the current `input/patent.md`

Checkpoint instances (hardness × profile):

| Checkpoint | publish / understand-only | draft / wire |
|---|---|---|
| `understand_confirm` | hard | soft |
| `cap_hit` | hard unless `--yes` | hard unless `--yes` |
| `bootstrap_input_conflict` | hard unless `--yes` | hard unless `--yes` |
| `design_title_lead` | soft | soft |
| worker `OWNER_QUESTION` | hard unless `--yes` | soft |

## Model allocation

- **Main / judgment workers** (`patent-reader`, design, compose, review, adversarial, polish, promo): `model: inherit` (session strongest).
- **Mechanical** (`figures-prep`, `grounding-verifier`): cheaper pin OK (`sonnet` class).

## Pipeline by stage

### -1. Run bootstrap (before any stage)

Before any stage worker or figures check. Orchestrator-inline (no forked agent).
`check_run` RUN-012 consumes `handoff/run-manifest.md`.

1. **Resolve input**
   - Path argument ⇒ copy to `input/patent.md`.
   - Pasted text ⇒ write to `input/patent.md`.
   - Patent number only ⇒ do **not** fetch autonomously; raise `OWNER_QUESTION`
     asking the Owner for the document text/file or explicit fetch authorization
     (name the source).
   - If `input/patent.md` already exists **and** differs from the argument's
     document ⇒ hard STOP/CONFIRM (`bootstrap_input_conflict`; Owner checkpoint
     protocol) before overwriting. Inline checkpoint (no stage contract):

     **RENDER:**
     - old patent identifier + sha256 of current `input/patent.md`
     - new patent identifier + sha256 of the argument document

     **ASK (verbatim):**
     > Overwrite `input/patent.md` with the new document?

     Hard unless `--yes`. On affirmative (or `--yes`), proceed with overwrite;
     otherwise abort the run without touching `input/patent.md`.

2. **Identify** — extract patent identifier (publication/application number) +
   title; echo both in the entry report.

3. **Workspace decision** (`handoff/`)
   - Empty ⇒ fresh run.
   - Non-empty, same patent (per `run-manifest.md` / confirm-file `patent:` field)
     and incomplete ⇒ **RESUME** from on-disk state (name the stage).
   - Non-empty, different patent ⇒ evacuate whole `handoff/` tree to
     `runs/<old-run_id>/handoff-abandoned/` and re-create empty stage dirs.
   - **All fresh-run cases:** delete any leftover `understand-confirmed.md`
     (a confirm never survives a new run).

4. **Figures identity** — read `input/figures/figures-manifest.md` header
   `patent:`. Mismatch with current patent ⇒ clear `input/figures/`,
   `input/figures-work/`, `input/figures-raw/` and note it. Manifest missing but
   `fig-*.png` present ⇒ stale (clear). Stale definition:
   `patent-figures-clean` SKILL.md.

5. **Write `handoff/run-manifest.md`** (format frozen; RUN-012 consumes):

   ```markdown
   # run-manifest

   - **run_id**: intel-us20250266395
   - **patent**: US20250266395A1
   - **patent_sha256**: <sha256 of input/patent.md>
   - **profile**: publish
   - **started**: 2026-07-10
   ```

   `run_id` syntax: glossary. Compute sha256 of `input/patent.md`. `essay_id` ≡ `run_id`.
   Prefer appending a short `-<topic>` keyword (e.g. `-backend-hbm`) so the id stays
   scannable as the `essays/` corpus grows — bare `<assignee>-us<number>` ids blur
   together at scale.

6. **Backlog preflight** (META-BACKLOG-01) — read
   `meta/improvement-proposals/README.md` status index; report count of pending
   `recommended-apply` proposals + oldest one's date. If any targets a
   gate/checker used by this run, warn that the run will hit a known defect.

7. **Entry report** (mandatory, one short block): patent id + title, `run_id`,
   workspace decision (fresh / resume / evacuated), cleared artifacts, backlog
   count.

### 0. Figures (optional) — `patent-figures-clean` / figures-prep

If no `input/figures/fig-*.png` but raw source exists → run figures stage. Bootstrap
step 4 has already cleared stale figures, so a surviving `fig-*.png` set is
identity-valid for the current patent; never skip on presence alone before bootstrap.

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
2. **Comprehension check (P2, keyed grading)** — runs only when `--comprehension-check`
   resolves **on** (per Parameters defaults) **and** not `--yes`. Reuses the
   STOP/CONFIRM protocol; does not invent a parallel mechanism. Bank:
   `handoff/00-understand/comprehension-quiz.md` (worker-produced; IF-2). Design:
   `docs/architecture/comprehension-loop.md` §4.2–4.3 / IF-1 / IF-4.

   **Per item (in bank order), each its own ASK→STOP turn:**
   1. **ASK** — RENDER the item's `question:` + `options:` inline (Korean stays
      Korean). STOP (end the turn; wait for the Owner).
   2. **GRADE** — compare the Owner's reply against `key` (mechanical, decidable).
      - **Correct** → advance to the next item.
      - **Incorrect** → **TEACH**: render the item's `rationale:` (study-pack span
        the answer rests on; positive framing only — never name a defensive
        writing behavior), then re-ASK a *paraphrased* form of the same item once.
   3. **Second miss (non-claim-scope aspects):** log as an explanation-prior
      ("this aspect did not land") in `comprehension-notes.md` and advance.
      Does **not** fail the Owner for problem / benefits / boundary.

   **PASS predicate (§4.3 / IF-1 `demonstrated`):** every mandatory aspect
   (`problem` | `claim-scope` | `benefits` | `boundary`) has at least one item
   answered correctly on the first or second try.

   **General opt-out:** at any non-claim-scope turn the Owner may say they will
   "confirm without the quiz" → set `comprehension: self-asserted` and stop
   asking remaining general items. **The general opt-out does NOT cover claim
   scope** — the claim-scope item must still be answered (or risk-accepted).

   **Claim-scope HARD STOP (§4.3, locked):** a **second miss** on the
   `aspect: claim-scope` item does **NOT** advance. The checkpoint STOPs and
   offers exactly two ways forward:
   - **(a)** re-read the claim-scope card (study pack §2b) and answer again, or
   - **(b)** explicitly accept the risk — recorded **verbatim** in the confirm
     `notes:` as `claim-scope risk accepted by owner`, and
     `comprehension: risk-accepted`.

   **`--yes` / flag off:** skip the loop entirely;
   `comprehension: skipped-unattended`. Do not write `comprehension-notes.md`.

   **After the loop (when it ran):** write
   `handoff/00-understand/comprehension-notes.md` (template shape) from the
   dialogue. Always include the **IF-4 claim-scope framing** section — a
   **positive** seed: the precise claimed-vs-described contrast to lead with,
   phrased affirmatively (whether demonstrated first try, taught-then-correct,
   or risk-accepted). Never name a defensive behavior (§5.1). Then proceed to
   the main ASK/RECORD; RECORD sets `comprehension:` per step 5.
3. **ASK** — utter the stage contract `question:` verbatim:
   > Can you restate Problem, Solution (incl. claim scope), and Benefits without
   > reopening the full patent? If yes, confirm. If no, edit open-questions or
   > request re-run of understand.
4. **STOP** — hard on `publish` / `understand-only` (end turn; no design, no Task/Skill
   for downstream, no confirm-file write this turn). Soft on `draft` / `wire` (RENDER
   and ASK still mandatory; may continue same turn with "soft checkpoint: continuing;
   reply to override").
5. **RECORD** — only after Owner's explicit affirmative in a later turn, write
   `handoff/00-understand/understand-confirmed.md` (`by: owner`, quote utterance in
   `notes:`). Set `comprehension:` to exactly one of (IF-1 frozen value set):
   - `demonstrated` — every mandatory aspect correct within two tries
   - `self-asserted` — Owner used the general opt-out ("confirm without the quiz");
     NOT available for claim scope
   - `skipped-unattended` — `--yes` or `--comprehension-check off`
   - `risk-accepted` — claim-scope item missed twice and Owner accepted the risk;
     `notes:` **MUST** then contain the verbatim string
     `claim-scope risk accepted by owner`

   **`--yes` only** writes without Owner utterance (`by: orchestrator-yes-flag`,
   `comprehension: skipped-unattended`). Stage worker never writes this file.
6. **RESUME** — valid confirm file for the current patent (see protocol validity) ⇒
   skip to design without re-asking; else RENDER→ASK→STOP again.

**Forbidden on hard checkpoints:** invoking design (or any next stage) in the same turn
as ASK; writing the confirm file without an Owner utterance (except `--yes`).

**Owner interaction records** (adjacent to this checkpoint; does not alter the protocol):

- Owner answers given at the checkpoint are appended by the orchestrator to
  `handoff/00-understand/open-questions.md` as
  `**Owner answer (YYYY-MM-DD):** …` blocks.
- A re-run of understand invalidates: delete `understand-confirmed.md` and regenerate
  the 01-design compat copies; the checkpoint must then be passed again.

Profile **`understand-only`**: after hard confirm, stop; do not design.

### 2. Design — `thesis-architect` / design-architect

Only after understand. Entry confirm: VALID confirm file, or recorded `--yes`, or
(profile `owner_confirm: soft`) RENDER+ASK performed this run with a soft-checkpoint note
in the run report — soft never writes a confirm file (`contracts/stages/design.yaml`
`entry_requires.confirm`). Consumes frozen `00-understand/` (and 01-design compat copies).
Must **not** recreate invention-summary from scratch. Surfaces title-lead candidates for
Owner override (`design_title_lead` soft checkpoint on every profile: RENDER candidates +
ASK per stage contract; STOP waived). May update briefing section ⑤ only (promo link)
with a Revision note. Cascade pauses that need an Owner decision use the
**OWNER_QUESTION relay** (below).

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
4. What ships on cap: the **LAST draft** only (never pick among earlier rounds by score).
5. Downstream after a cap-accepted ship: `self_audit` and later stages still run on
   `publish`.

### 5. Self-audit (publish)

≥2 adversarial-reader + grounding-verifier + one extra `adversarial-reader` fork run
checklist-FREE (the "cold reader"; same agent type, casual-scroller prompt only — contracted
in `contracts/stages/self_audit.yaml`); multi-vote; fix via revision mode; normalize deltas
to ledger. Cap 3 dry-loop iterations.

### 6. Polish (publish) — `prose-polish`

Surface-only 윤문; zero-new gate findings.

**Two-step drift check (AUD-W7):**

1. Polish worker returns a changed-sentence list and marks `drift-check PENDING` in its
   final message (worker does **not** spawn the verifier).
2. Orchestrator forks `grounding-verifier` on old/new pairs. Any `MEANING-CHANGED` **or**
   `PROTECTED-TOUCHED` ⇒ re-fork polish to revert that sentence; re-run gates as needed.

### 7. Verify

```
python3 .claude/skills/_shared/scripts/check_run.py --handoff handoff \
  --threshold <threshold> --self-audit <on|off> \
  --acceptance <single-clean|double-clean> --owner-confirm <required|yes-flag|off>
```

Profile → flags (`contracts/stages/verify.yaml`):

| Profile | `--acceptance` | `--owner-confirm` |
|---------|----------------|-------------------|
| `publish` | `double-clean` | `required` (`--yes` run ⇒ `yes-flag`) |
| `draft` / `wire` | `single-clean` | `off` |

`--require-understand` is on by default; disable it only to re-verify a legacy
`essays/` archive. Must PASS before archive. Never edit artifacts to satisfy it.

### 8. Archive

`id` ≡ `run_id` (glossary / `handoff/run-manifest.md`). Contract: `contracts/stages/archive.yaml`.

- `runs/<id>/` — full round evidence  
- `essays/<id>/` — shelf (assemble all of the following)

**Assemble (imperative):**

1. Copy `handoff/03-edit/essay-final.md` → `essays/<id>/essay-final.md`.
2. Copy from understand: `owner-study-pack.md`, `owner-briefing.md` → `essays/<id>/`.
3. Snapshot `input/patent.md` → `essays/<id>/patent.md` (sha256 must match run-manifest).
4. Place figures under `essays/<id>/figures/` and into `publication-package/` as needed.
5. Copy `handoff/02-compose/publication.md` → `essays/<id>/publication-package/publication.md`.
6. Author `essays/<id>/publication-package/posting-checklist.md` (title, cover alt, body alts, paste source).
7. **Cover (required):** generate `essays/<id>/publication-package/cover-5x2.png` via
   `python tools/make_header.py ... --out essays/<id>/publication-package/cover-5x2.png`
   (see `tools/header-style.md`; `make_header.py` is the contracted producer).
8. Copy score-history, gate-result, README; leave `promo/` for the promo stage.
9. Copy `handoff/02-compose/thesis-trace.md` → `essays/<id>/thesis-trace.md` (promo reads it).
10. **Slim archive:** the shelf carries the final artifacts + `thesis-trace.md` only. Do NOT
    copy the working `handoff/` tree into `essays/<id>/` — rejected thesis-candidates and
    pre-final drafts read as canonical to a fresh-context worker. The full round-by-round
    evidence stays in `runs/<id>/` (per-run, not tracked).

### 9. Promo (publish) — `promo-composer`

Post-archive; never edits essay; safe-claims grounding.

### 10. Retro — `pipeline-retro`

Propose-only; surface top proposal one line.

## Worker-raised questions (OWNER_QUESTION relay)

Any forked worker that needs an Owner decision ends its final message with:

```
OWNER_QUESTION: <question>
FILES: <paths>
DEFAULT: <answer>    # optional
```

The orchestrator treats this as a checkpoint instance of the Owner checkpoint protocol:

1. **RENDER** — the worker's named files (content inline) + the question text.
2. **ASK** — the question (and options if the worker supplied them).
3. **STOP** — hard/soft per checkpoint instance × profile (see table above) and `--yes`.
4. After Owner reply, re-invoke the worker with the answer.
5. **`--yes` rule:** if the worker supplied a `DEFAULT:` line, proceed with that answer
   and record the fact in the run report. If no `DEFAULT:` line is present, **abort the
   run with a report** — unattended runs never guess.

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
