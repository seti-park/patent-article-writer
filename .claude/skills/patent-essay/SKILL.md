---
name: patent-essay
description: >
  Orchestrator / entry point for the patent-essay system. Given an English patent (+ raw or
  cleaned figures), runs Phase 0 Figures → Phase 1 Design → Phase 2 Compose → Phase 3 Edit,
  with every phase in an ISOLATED agent context (context: fork), a Compose↔Edit loop with
  double-clean acceptance and a mechanical run-completeness check, then a post-acceptance
  self-audit, a Phase 4 promo pack against the archive, and pipeline-retro. Use when asked
  to turn a patent into a finished English essay end to end.
argument-hint: "[patent path | text | number]  [--threshold pass|revise-recommended] [--max-iter N] [--mode essay|wire] [--self-audit on|off]"
allowed-tools: Read, Write, Edit, Grep, Glob, Bash, Task, Skill, WebFetch, WebSearch
---

# Patent Essay — Orchestrator

You own the LOOP POLICY and arbitration; every phase's domain work runs in its own forked
agent context. Keep the main thread lean: parameters, gate outputs, loop state, and the
one-line reports each agent returns. All content travels through handoff files on disk. The
five north-star goals and the goal→check matrix live in `_shared/references/scoring-rubric.md`.

## Inputs (per run)

- `input/patent.md` — the English patent (or whatever `$ARGUMENTS` names).
- `input/figures/fig-NN.png` — cleaned figures; OR `input/figures-raw/` — a raw drop
  (zip / TIFF / mixed) that Phase 0 will clean.
- `input/essay-context.md` — optional per-run framing (audience override, edition, guards).

## Parameters

- `--threshold pass|revise-recommended` — minimum editorial assessment accepted. Default
  `pass`; never relaxable to `revise-required`.
- `--max-iter N` — max REVISION rounds (default 4). Confirmation reviews (below) do not
  count against this cap.
- `--mode essay|wire` — deliverable mode (default essay).
- `--self-audit on|off` — post-acceptance self-audit (default on; `off` only for wire runs,
  and `check_run.py` must then be invoked with `--self-audit off`).
- `--max-selfaudit-iter N` — self-audit loop-until-dry cap (default 3).

## Model allocation

- **Main session (this orchestrator)**: the strongest model available — it holds loop
  policy, arbitrates composer-vs-reviewer conflicts, and makes the accept/revise calls.
- **design-architect / essay-composer / editorial-reviewer / adversarial-reader /
  promo-composer**:
  `model: inherit` — design, prose, and editorial judgment are the hard parts; they run on
  the session model in clean, isolated contexts.
- **grounding-verifier / figures-prep**: `model: sonnet` — retrieval-shaped verification and
  mechanical image work; a cheaper model with a tight contract.

## Pipeline

### Phase 0 — Figures (conditional; skill: `patent-figures-clean`, agent: figures-prep)

If `input/figures/` has no `fig-*.png` but a raw source exists (`input/figures-raw/` or a
path in `$ARGUMENTS`), invoke the `patent-figures-clean` skill. It returns a figure
inventory + figures-index list and writes `input/figures/figures-manifest.md`. If figures
are already clean, skip.

### Phase 1 — Design (skill: `thesis-architect`, agent: design-architect, voice-off)

Invoke `thesis-architect`. It writes the `handoff/01-design/` bundle (invention-summary with
Quotable spans + Claim scope map, owner-briefing (Korean, per Step 2b +
`_shared/references/owner-briefing-schema.md`), thesis-spine with `closing_posture`,
thesis-candidates, title-lead-candidates (5 energy-register pairs + `recommended:`),
figure-selection with cover candidate, figure-rationale, fact-check-log, search-log,
phase2-handoff-notes) and
auto-selects the recommended single-spine candidate. Also ensure
`handoff/01-design/figures-index.txt` exists (from the manifest or `input/figures/`).

On return: surface the candidate list in one line (human can override), AND surface the five
title-lead candidates (register + title each) alongside — the human may override the pick;
default = Phase 1's `recommended:` pick. Record the selected register/pair in one line; it
travels to Phase 2 with the compose invocation. Surface the Korean owner-briefing
(`handoff/01-design/owner-briefing.md`) to the owner alongside the title-lead candidates: the
run's two human moments travel together. Then run the
early grounding gate — a Phase-1 quote fabrication must die here, not in round 3:

```
python .claude/skills/_shared/scripts/gate_quotes.py handoff/01-design/invention-summary.md \
  --invention-summary handoff/01-design/invention-summary.md --patent input/patent.md

python .claude/skills/_shared/scripts/gate_quotes.py handoff/01-design/owner-briefing.md \
  --invention-summary handoff/01-design/owner-briefing.md --patent input/patent.md
```

(The second invocation verifies the briefing: its `근거 (verbatim)` span lines parse as
Quotable-span lines, so the same gate covers it with zero code changes.) Any QUOTE-001 in
either file → send Phase 1 back once with the failing quotes named; fix-at-source before
Phase 2, same as invention-summary failures.

### Phase 2 — Compose (skill: `essay-en-composer`, agent: essay-composer, voice-on)

Invoke `essay-en-composer`, passing the selected title-lead pair (register) from Phase 1. It
reads `handoff/01-design/` (never the raw patent) and writes
`handoff/02-compose/` (essay-draft with `closing_posture` frontmatter, publication via
`strip_publication.py`, figures-rationale, thesis-trace with the ≤ 3 declared signature
lines).

### Phase 3 — Edit loop (skill: `editorial-review`, agent: editorial-reviewer, voice-fenced)

Per round N (starting N=1):

1. **Gates** (mechanical, before trusting any review):

   ```
   python .claude/skills/_shared/scripts/run_gates.py \
     --draft handoff/02-compose/essay-draft.md \
     --invention-summary handoff/01-design/invention-summary.md \
     --figures handoff/01-design/figures-index.txt \
     --figure-selection handoff/01-design/figure-selection.md \
     --patent input/patent.md --mode <essay|wire> --json
   ```

   Save the JSON to `handoff/03-edit/gate-result.round-N.json`. `gate_surface`
   (SURF-001..004, goal 5) runs inside `run_gates.py` like the rest — it is warn-only, so no
   loop-policy change: read its warns and surface them to the reviewer/revision prompts as
   goal-5 signals.
2. **Review**: invoke `editorial-review` — every invocation forks a FRESH
   editorial-reviewer with no memory of prior rounds. Tell it the round number and (N>1)
   point it at the prior edit-log + revision-response. It writes
   `handoff/03-edit/edit-log.round-N.md` (+ canonical `edit-log.md`), findings with
   `finding_id`s per `feedback-format.md`.
3. **Round verdict**:

   ```
   CLEAN(N) ⇔ gates all pass
              AND assessment acceptable per --threshold
              AND grounding hard-gate holds (no pass-3 high/critical; no gate_anchors or
                  gate_quotes fail)
              AND goal-2 hard-gate holds (no FIGUSE-001; no pass-3 coverage high)
              AND verdict hard-gate holds (no gate_hedge fail; no 6G high under a declared
                  firm closing)
   ```

**Acceptance = double-clean.** A single clean round is a hypothesis, not a verdict — the
documented failure mode is a self-graded round-1 `pass`. On the first CLEAN(N), run one
**confirmation round**: a fresh review (round N+1, no revision in between; re-use round N's
gate result or re-run). CLEAN(N+1) too → accept. Findings → back to the revision loop
(confirmation rounds don't count against `--max-iter`).

**While not accepted and revision rounds < max-iter**: invoke `essay-en-composer` in
revision mode with round N's edit-log + failing gate check_ids. It dispositions every
medium+ finding into `handoff/02-compose/revision-response.round-N.md` (per
`revision-mode.md`), revises in place, and the loop re-runs gates + a fresh review as round
N+1.

**Cap**: at `--max-iter` without double-clean, you may promote the best round ONLY by
writing an explicit `CAP HIT` line into `handoff/03-edit/score-history.md` and surfacing
every unresolved finding to the user. Never promote silently.

On acceptance, promote the accepted draft to `handoff/03-edit/essay-final.md` and write
`score-history.md` (one row per round: assessment, gate result, verdict, note).

## Self-audit (post-acceptance, auto)

Fresh eyes on the accepted essay, per round (up to `--max-selfaudit-iter`):

1. Spawn IN PARALLEL via Task: **2× adversarial-reader** (one per persona: impatient
   investor, skeptical pro-subject reader; separate output files, blind to each other),
   **1× grounding-verifier** (full anchor-by-anchor fidelity table on essay-final.md), and
   **1× cold reader** (adversarial-reader agent type, checklist-FREE prompt: a casual
   scroller persona — do NOT hand it the pass-7 checklist or any rubric; it reads
   essay-final.md once and reports ONLY (a) where it stopped reading, (b) what it felt,
   (c) the one thing it would repeat to a friend; separate output file, blind like the
   others).
2. **Multi-vote**: apply a finding when readers agree (majority), OR when a grounding
   finding is verified against the source, OR when it is a 6G over-hedge finding verified
   against the body's evidence — over-hedge is first-class here, symmetric with overreach.
   Cold-reader input maps to goal-5 findings: a cold-reader stop-point corroborated by ANY
   rubric reader's finding (same location or same cause) = apply; its repeat-to-a-friend
   sentence is checked against the `reader_sentence` (a miss is a goal-5 signal, not an
   auto-finding). **Exception — early drag auto-escalates:** a cold-reader stop-point or
   drag report located in the lead or before the first `payload: tech` section (thesis-spine
   trace tags) is a medium goal-5 finding on its own, no corroboration needed — the class
   `procedure-overweight-lead` shipped precisely because early-position drag was treated
   as taste (doctrine: `_shared/references/reader-energy.md` §6). Log other split /
   taste-only findings and uncorroborated stop-points to `revision-notes.md` as
   considered-not-applied.
3. **Apply** accepted findings via `essay-en-composer` in revision mode against
   `essay-final.md` (grounding fix priority binds; fix upstream Phase-1 artifacts too when a
   finding traces there). Log every applied edit as a `## delta` block in
   `handoff/03-edit/revision-notes.md` (schema: `handoff-template/03-edit/revision-notes.md`),
   then re-run the gates on the final.
4. **Loop until dry**: repeat until a round applies nothing at medium+. If a round applies
   nothing at all, write the explicit line `self-audit: no unresolved findings` into
   revision-notes.md. Self-audit can only ADD findings — never relax a gate or the bar.

Normalize the deltas afterwards:

```
python meta/normalize_revision_notes.py --notes handoff/03-edit/revision-notes.md \
  --essay-id <essay-id> --origin self-post-accept --append meta/findings-ledger.jsonl
```

## Phase 3.7 Polish — 윤문 (after self-audit DRY, before check_run/archive)

Spawn the `prose-polish` agent (fork, `model: inherit` — LOAD-BEARING, owner pen rule
2026-07-05: the polish is written by the session's strongest model) on the accepted,
self-audit-DRY essay. It is the final plain-language pass for the general reader:
sentence splitting, plain word choice, grounded glosses — with every fact, number,
`[dddd]` anchor, quote, verb of certainty, and declared signature line preserved
(signature lines byte-identical). Contract (`prose-polish/SKILL.md`): every edit logged
in `handoff/03-edit/polish-notes.md`; gates re-run with zero NEW findings (warns
included) or the edit reverts; changed sentences drift-verified by a
grounding-verifier-class instrument (pinned cheap; verdicts MEANING-CHANGED /
PROTECTED-TOUCHED force reverts); `draft_version` bumped; publication re-stripped.
Polish never reopens the loop — a factual defect it notices routes to the
human-post-accept channel, and the sentence stays unpolished.

## Run-completeness check (mandatory before archive)

```
python .claude/skills/_shared/scripts/check_run.py --handoff handoff \
  --threshold <threshold> --self-audit <on|off>
```

It mechanically verifies the loop's shape: contiguous round artifacts, a disposition for
every medium+ finding, no silently dropped finding_ids, double-clean (or explicit CAP HIT)
acceptance, self-audit evidence, owner-briefing presence (RUN-008). If it FAILS, do the
missing work — never edit artifacts to satisfy the checker. Its verdict goes in the final
report.

## Archive + promo + meta-loop

1. **Archive** to `runs/<essay-id>/`: all `edit-log.round-*.md`, `gate-result.round-*.json`,
   `revision-response.round-*.md`, `score-history.md`, `revision-notes.md`, the final
   `run_gates.py --json` output as `gate-result.json`, and the check_run verdict.
2. **Tracked deliverable** (committed): `essays/<essay-id>/` with `essay-final.md`,
   `figures/`, `gate-result.json`, `score-history.md`, `edit-log.md`, `README.md`,
   `owner-briefing.md` (copied from `handoff/01-design/`), `patent.md` (the run's exact
   `input/patent.md` snapshot, so every `[dddd]` anchor in the archive resolves without
   re-fetching), and the full `handoff/` phase tree — the canonical layout, per the
   2026-06-26 retro L7. If this archive supersedes an earlier `essays/<id>/` for the same
   patent, move the superseded dir to `essays/_superseded/` in the same commit and banner
   its README — the essays/ root holds only current deliverables (index:
   `essays/README.md`).
3. **Phase 4 promo (skill: `promo-composer`, agent: promo-composer; default-on for essay
   mode, skippable on request)**: spawn it (fork, `model: inherit` — LOAD-BEARING, owner
   decision 2026-07-05: the posting copy must be composed by the session's strongest
   model, never a pinned-cheap one) against the fresh `essays/<essay-id>/` archive.
   Output contract: `essays/<essay-id>/promo/promo-pack.md` (Korean long-form post
   400-800자 + English thread 3-5 tweets; bold-selection rule: promo leads with the
   boldest supportable claim, insurance ≤1 status clause per deliverable, process
   narration 0 — the article hedges, the promo points). Grounding rule: every factual
   phrase traces to `essay-final.md`/`publication.md` or `owner-briefing.md`; no new
   factual claims. Promo never edits the essay; promo findings never reopen the loop.
4. **Meta-loop**: invoke `pipeline-retro` (forked) with the run's artifacts. Propose-only;
   surface the top proposal in one line.

## Output (final report to the user)

- The final essay (`handoff/03-edit/essay-final.md`).
- The Korean owner briefing + the promo pack, called out for the owner
  (`essays/<essay-id>/owner-briefing.md`, `essays/<essay-id>/promo/promo-pack.md`).
- SCORE HISTORY: round → assessment → gate result (failing check_ids) → verdict → note,
  including confirmation rounds and self-audit rounds.
- The `check_run.py` verdict line.
- One line on any new `pipeline-retro` proposal.
- If capped: the CAP HIT statement + the unresolved findings, prominently.

## Optional: `/goal` outer net

```
/goal the patent-essay run is complete: check_run.py exits 0 (double-clean acceptance or an
explicit CAP HIT, dispositions for every medium+ finding, self-audit evidence present), all
gates green including gate_quotes and gate_hedge, and the SCORE HISTORY shows the final
accepted round
```
