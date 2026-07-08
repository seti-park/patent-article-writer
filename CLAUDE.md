# Patent Essay System (Claude Code / web)

A skill-based pipeline that turns an **English patent** (+ figures, raw or cleaned) into a
finished **English essay** for X Articles, written for a **curious retail investor** (technical
comprehension between advanced high school and early undergraduate — see
`_shared/references/reader-profile.md`). Four phases — **Figures → Design → Compose → Edit** —
pass data through on-disk hand-off directories. Every phase runs in an **isolated agent
context** (`context: fork` + `.claude/agents/`), and an orchestrator runs the Compose↔Edit
quality loop to a **double-clean acceptance** verified by a mechanical run-completeness check.
After each essay a slower **meta-loop** (`pipeline-retro`) proposes improvements to the system
itself.

## North-star goals (acceptance criteria)

Every gate and editorial pass defends one of five goals; the full goal→check traceability
matrix is in `_shared/references/scoring-rubric.md`:

1. **Catch the patent's core accurately** — anchor chain + verbatim-quote gate, grounding.
2. **Use figures + specification sufficiently** — `gate_figure_use` + pass-3 coverage.
3. **Easy for the reader to understand** — reader-profile calibration, structure, pass-5/7.
4. **Well-structured (4a) and natural (4b)** — incl. the **verdict hard-gate**: conclusions
   must be evidence-proportionate in BOTH directions (no overreach, no safe-harbor hedging).
5. **Reader energy** — the reader leans in at the lead, keeps momentum, leaves armed with a
   repeatable sentence; binds the SURFACE only (`gate_surface` + pass-6 6H + pass-7 hook
   check + cold-reader self-audit; doctrine: `_shared/references/reader-energy.md`).

One **output contract** sits beside the rubric: the pipeline's understanding must reach TWO
humans. The READER leaves armed (goal 5); the OWNER (Korean publisher) receives the same
comprehension as the Korean **owner briefing** at Phase 1 (`gate_quotes`-verified, schema:
`_shared/references/owner-briefing-schema.md`) plus the **promo pack** at Phase 4. Not a
rubric goal: it is how the owner judges the essay, answers readers, and briefs a promo.

## How to run

```
/patent-essay <patent path | text | number>  [--threshold pass|revise-recommended] [--max-iter 4] [--mode essay|wire] [--self-audit on|off]
```

Inputs live under `input/`: `patent.md`, `figures/fig-NN.png` (cleaned) **or**
`figures-raw/` (zip / TIFF drop — Phase 0 cleans it), and optional `essay-context.md`
(per-run audience/edition overrides). The orchestrator runs Phase 0-3 plus the loop, the
post-acceptance self-audit, the Phase 3.7 윤문 polish (`prose-polish`), `check_run.py`,
archives to `runs/<essay-id>/` +
`essays/<essay-id>/`, then runs Phase 4 promo (default-on in essay mode) and the meta-loop,
and returns the final essay + owner briefing + promo pack + score history + check_run verdict.

**Model allocation** (the recommended setup): run the SESSION on the strongest model
available (Fable 5) — the main thread holds loop policy, arbitration, and acceptance calls,
and `model: inherit` agents (design / compose / review / self-audit readers / promo copy —
the promo posting copy is inherit BY OWNER DECISION, never pinned down) get that model
in clean contexts, which is where writing and editorial judgment quality comes from.
Mechanical agents pin cheaper models in their frontmatter (`grounding-verifier`,
`figures-prep`: `model: sonnet`). An "advisor" pattern (weak main model consulting a strong
one) is deliberately NOT used: prose and integration quality are bounded by the model that
holds the pen, not the one giving advice.

Individual phases can be run standalone: `/patent-figures-clean`, `/thesis-architect`,
`/essay-en-composer`, `/editorial-review`, `/prose-polish`, `/pipeline-retro`
(`/voice-canon-lookup` is an internal Phase-2 helper).

## Architecture

```
.claude/agents/          isolated contexts + model pinning (the fencing is PHYSICAL now)
  design-architect       P1 worker (inherit)    essay-composer     P2 worker (inherit)
  editorial-reviewer     P3 worker, fresh per round (inherit)
  adversarial-reader     self-audit personas, >=2 in parallel (inherit)
  promo-composer         P4 worker, post-archive (inherit)
  grounding-verifier     fidelity instrument (sonnet)   figures-prep  P0 worker (sonnet)
.claude/skills/
  patent-essay/          orchestrator: loop policy + arbitration ONLY (entry point; main context)
  patent-figures-clean/  P0 Figures — raw drop → cleaned fig-NN.png + vision-verified manifest
  thesis-architect/      P1 Design  — patent → invention-summary (+ Claim scope map) + owner-briefing
                         (KR, gate_quotes-verified) + thesis-spine (+ closing_posture) + figure plan
                         (+ cover candidate)   [fork: design-architect]
  essay-en-composer/     P2 Compose — blueprint → draft (+ revision mode w/ dispositions)
                                                                    [fork: essay-composer]
  voice-canon-lookup/    P2 internal helper — voice-canon corpus (runs inline in the composer)
  editorial-review/      P3 Edit    — 7-pass severity review incl. 6G over-hedge + 6I
                         attention-budget guards; finding_id lifecycle; re-review protocol
                                                            [fork: editorial-reviewer]
  prose-polish/          P3.7 Polish (윤문) — post-self-audit plain-language pass for the
                         general reader; surface-only jurisdiction, every edit logged +
                         drift-verified, gates re-run zero-new   [fork: prose-polish]
  promo-composer/        P4 Promote (post-archive): essays/<id>/ → promo/promo-pack.md (KR 장문
                         400-800자 + EN thread 3-5 tweets; bold-selection rule: promo leads
                         bold, the article hedges), grounded in essay-final/publication
                         + owner-briefing; never edits the essay   [fork: promo-composer]
  pipeline-retro/        meta-loop  — findings → ledger → propose-only proposals   [fork]
  _shared/
    references/          scoring-rubric (severity + matrix + double-clean acceptance) ·
                         reader-profile (audience contract + reader jobs) · reader-energy
                         (goal-5 surface doctrine) · deliverable-voice-rules ·
                         anti-ai-writing · caption-roles · working-dialogue-voice
    scripts/             14 deterministic gates (stdlib) + strip_publication.py +
                         check_run.py + banned_terms.txt + tests
    vendor/              humanizer + ai-check — REFERENCE ONLY, absorbed into anti-ai-writing
handoff/          01-design 02-compose 03-edit    runtime stage artifacts (gitignored)
handoff-template/ full-schema templates incl. revision-response.md + revision-notes.md
essays/<essay-id>/  the TRACKED deliverable: essay-final.md · owner-briefing.md · patent.md
                    (the run's input snapshot; anchors resolve offline) · figures/ ·
                    gate-result.json · score-history.md · edit-log.md · README.md ·
                    promo/promo-pack.md (P4) · full handoff/ phase tree
essays/_superseded/   replaced editions, moved on supersede (baseline/evidence; never a
                      grounding source)
runs/    <essay-id>/  per-run archive (round logs, gate results, dispositions)
meta/    findings-ledger.jsonl · attribution-table.md · improvement-proposals/ ·
         fixtures/ + regression.py  (the system's persistent memory — tracked)
input/   patent.md · figures/ · figures-raw/ · essay-context.md
docs/source-prompts/  original claude.ai skills, verbatim reference baseline
```

Data flows by **output contracts**: each phase's `SKILL.md` defines the exact files it writes
to `handoff/<phase>/`, and the next phase reads them — no chat copy-paste, no shared
conversation state. Context isolation is enforced by the harness (forked agents), not by
instructions: the reviewer physically cannot see the composer's reasoning, only its artifacts.

## Voice + source fencing (by agent, physical)

- **Design (voice-off, design-architect):** thesis-architect references only — no voice canon.
- **Compose (voice-on, essay-composer):** full voice stack + reader-profile; NEVER reads the
  raw patent (Quotable spans are the only patent source).
- **Edit (voice-fenced, editorial-reviewer):** `deliverable-voice-rules` + `anti-ai-writing`
  + `reader-profile` only — not voice-profile / caption-roles. Fresh instance per round.
- **Self-audit (adversarial-reader / grounding-verifier):** blind to each other; can only ADD
  findings; grounding recommendations are anchor/narrow/label/cut — never "add a hedge".

## Loop control (three tiers)

- **Inner loop (auto):** per round — gates (`run_gates.py`, now incl. `gate_quotes`
  invention-summary↔patent verbatim and `gate_hedge` verdict over-hedge) + a FRESH
  `editorial-review` (severity model, finding_ids). **Acceptance = double-clean**: two
  consecutive clean rounds from independent reviewers (a round-1 "pass" is a hypothesis, not
  a verdict). On FAIL: `essay-en-composer` revision mode — every medium+ finding gets an
  `applied`/`rejected` disposition in `revision-response.round-N.md` (revision-mode.md), and
  the next reviewer verifies each disposition landed. Hard-gates: grounding (pass-3
  high/critical, gate_anchors, gate_quotes), goal-2 (FIGUSE-001, coverage), **verdict**
  (gate_hedge fail / 6G high under firm closing). Max 4 revision rounds; at cap, ship the
  best round ONLY with an explicit `CAP HIT` in score-history + surfaced findings.
- **Run-completeness (auto):** `_shared/scripts/check_run.py` must pass before archiving —
  it mechanically proves the loop ran (contiguous round artifacts, disposition coverage, no
  dropped finding_ids, double-clean or CAP HIT, self-audit evidence). If it fails, do the
  missing work; never edit artifacts to satisfy it.
- **Self-audit (auto, post-acceptance):** ≥2 `adversarial-reader` agents (personas, blind,
  parallel) + 1 `grounding-verifier` + 1 checklist-free **cold reader** (casual scroller;
  stop-point / feelings / repeat-to-a-friend → goal-5 findings); multi-vote; over-hedge findings are first-class
  (symmetric with overreach); fixes via composer revision mode; `## delta` blocks in
  revision-notes.md; loop until dry (cap 3); normalized to the ledger as
  `origin: self-post-accept`.
- **Polish (auto, post-self-audit, 윤문):** one `prose-polish` pass before archiving —
  plain-language surface smoothing for the general reader; meaning/facts/anchors/quotes/
  signature lines preserved (drift-verified by a cheap instrument, gates re-run zero-new);
  every edit logged in `polish-notes.md` (`origin: polish`).
- **Meta-loop (`pipeline-retro`, propose-only):** normalizes inner-loop + self-audit +
  human-post-accept findings into `meta/findings-ledger.jsonl` (attribution-table keys),
  writes evidence-backed proposals. It never edits a skill — a human applies after
  `meta/regression.py` passes.

## Deterministic gates

`_shared/scripts/run_gates.py` runs fourteen mechanical checks (pass `--patent` for the
quote gate): `gate_emdash`, `gate_anchors` (incl. panel-letter figure tokens), **`gate_quotes`**
(every invention-summary Quotable span / Quote anchor row verbatim-present in patent.md — the
mechanical half of the grounding chain), `gate_sources`, `gate_banned`, `gate_structure`
(STRUCT-001 warns at ≥8 sentences, aligned to Pass 2C), `gate_figure_use`, `gate_meta`,
`gate_stub`, `gate_cashtag`, `gate_dupe`, `gate_typography`, **`gate_hedge`** (verdict-section
safe-harbor boilerplate / qualifier-led verdict / hedge density; hard-fails under the draft's
`closing_posture: firm`), and **`gate_surface`** (warn-only goal-5 feed checks: SURF-001 title
> 70 chars, SURF-002 qualifier-led first body sentence, SURF-003 cover-caption numeral
density > 6, SURF-004 defensive-open, SURF-005 lead procedure-narration sentences > 1,
SURF-006 spend-motif > 4 in prose — the attention-budget pair, doctrine in
`reader-energy.md` §6). Utilities: `strip_publication.py` (publication.md with one line per
paragraph) and `check_run.py` (loop shape). Run
`python .claude/skills/_shared/scripts/test_gates.py` for the suite, or
`python meta/regression.py` for tests + fixtures.

## The over-hedge defense (why conclusions stay firm)

The historical failure: passes 3/4 punished overreach, nothing punished over-hedge, and the
cheapest way to satisfy a grounding critic is to hedge — so conclusions ratcheted toward
"a patent doesn't guarantee production/stock gains" boilerplate. The defense is now
structural, at four layers: (1) `thesis-spine.md` declares `closing_posture: firm` by default
for verdict editions; (2) the composer's closing directive drafts the call first with ONE
patent-specific anti-hype guard; (3) editorial 6G + the jurisdiction fence (grounding passes
may never recommend hedging; fix priority = anchor → narrow → label → cut); (4) `gate_hedge`
hard-fails boilerplate/qualifier-led verdicts under a firm posture. The steelman must be a
THIS-patent objection — generic patent truisms are banned as steelmen and count as
`steelman-absent`.

## Customization

- **Audience** in `_shared/references/reader-profile.md` (per-run override via
  `input/essay-context.md`); **behavior** in `_shared/references/` (scoring-rubric,
  anti-ai-writing, deliverable-voice-rules) and each skill's `references/`; the banned-term
  list is mirrored to `_shared/scripts/banned_terms.txt`. The composition/hygiene canon is
  govuk-based plain English with patent-domain exceptions (claim language, terms of art, part
  numbers, verbatim quotes keep exact wording).
- **Grow the canon** via `pipeline-retro` proposals, applied by a human after
  `meta/regression.py`.
- **Originals** in `docs/source-prompts/` (incl. Phase-4 `promo-composer`, preserved for a
  future port). Keep each phase's output contract intact when porting.
