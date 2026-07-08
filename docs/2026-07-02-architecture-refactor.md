# 2026-07-02 architecture refactor — isolation, symmetric verdicts, Phase 0

One coordinated refactor addressing the three operator-reported failure modes, plus the
backlog of validated improvement proposals. Everything below is applied and regression-tested
(`meta/regression.py` PASS: 88 gate tests + 4 fixtures).

## Pain point 1 — "The edit loop sometimes waves drafts through"

Root causes found: (a) the reviewer ran in the SAME context as the composer (no
`.claude/agents/` existed — "fresh context" was an instruction, not a mechanism), so a
round-1 self-graded `pass` ended the loop (see `essays/agility-us12560948/score-history.md`);
(b) "revision mode" was referenced by the orchestrator but never defined — nothing forced a
finding-by-finding response; (c) promotion at max-iter was silent.

Fixes:

- **Physical context isolation.** `.claude/agents/` added; phase skills now carry
  `context: fork` + `agent:` so every review round is a genuinely fresh
  `editorial-reviewer` with no memory of prior approvals.
- **Double-clean acceptance.** A clean round triggers a confirmation round by a second
  independent reviewer; only two consecutive cleans accept (confirmation rounds don't count
  against `--max-iter`).
- **Finding lifecycle.** Findings carry `finding_id`s; the composer's new revision mode
  (`essay-en-composer/references/revision-mode.md`) dispositions every medium+ finding
  (`applied` / argued `rejected`) into `revision-response.round-N.md`; the next reviewer must
  rule on every carried id (re-review protocol in `editorial-review/SKILL.md`).
- **Mechanical enforcement.** `_shared/scripts/check_run.py` (RUN-001..007) proves the loop's
  shape — contiguous round artifacts, disposition coverage, no dropped ids, double-clean or
  an explicit `CAP HIT` — and must pass before archiving.

## Pain point 2 — "Conclusions collapse into safe-harbor boilerplate"

Root causes found: (a) rubric asymmetry — passes 3/4 punish overreach, nothing punished
over-hedge (diagnosed in `2026-06-24-conclusion-over-hedge-check.md`, previously unapplied);
(b) pass-6 6B and section-blueprint both mapped `Acknowledged` residual risk →
`closing-open-question` — the rubric itself steered verdict editions into open-question
closings; (c) the steelman requirement accepted generic patent truisms, whose "rebuttal" is
inherently a hedge; (d) the anti-hedge guard existed only as a manual per-run
essay-context.md instruction.

Fixes (four structural layers):

1. **Design**: `thesis-spine.md` declares `closing_posture: firm` by DEFAULT for
   verdict/investor editions (thesis-architect Step 8); `Acknowledged` residual maps to
   forward-watching / binary-test closings, never open-question. Generic-truism ban in
   `adversarial-defense.md` (a category truism is a weak-man, not a steelman).
2. **Compose**: section-blueprint closing directive — the call leads, exactly ONE
   patent-specific anti-hype guard, limits referenced (not re-listed) from the verdict;
   `closing_posture` copied into the draft frontmatter.
3. **Edit**: pass-6 **6G** over-hedge guard (mirror of pass-3/4) + the **jurisdiction fence**
   in `editorial-review/SKILL.md`: grounding passes may never recommend hedging — the fix
   priority is anchor → narrow → label → cut. Pass-7's steelman check rejects truisms.
4. **Gate**: `gate_hedge.py` (HEDGE-001 boilerplate, HEDGE-002 qualifier-led verdict,
   HEDGE-003 hedge density) — hard-fails under `closing_posture: firm`; verified zero false
   positives on the known-good archived essay.

## Pain point 3 — "Figure preprocessing should live in the pipeline"

- New Phase 0 skill **`patent-figures-clean`** (+ `figures-prep` agent, `model: sonnet`):
  raw zip/TIFF drop in `input/figures-raw/` → extract, PNG-convert, white-trim
  (`ImageChops.difference` — the retro's PIL gotcha, encoded), size-cap, agent VISION naming
  pass (never trust source filenames), panel crop/rotate, mandatory label↔filename
  verification loop, and `figures-manifest.md`. Mechanical layer:
  `patent-figures-clean/scripts/clean_figures.py` (Pillow — the repo's only non-stdlib dep,
  Phase 0 only). The orchestrator invokes it automatically when `input/figures/` is empty.
  Note: the private patent-essay-pipeline repo's skill was inaccessible (404), so this is a
  clean rebuild against this repo's conventions; diff against the original if desired.

## Grounding chain completed

`gate_quotes.py`: every invention-summary Quotable span / Quote anchor table row must be
verbatim-present in `input/patent.md` (allowed normalizations from
`quote-anchor-conventions.md` + whitespace collapse). Previously the
invention-summary→patent link was pass-3 judgment only — a fabricated span passed every
gate. Now: draft→summary (`gate_anchors`) and summary→patent (`gate_quotes`) are both
mechanical, and the orchestrator runs the quote gate at the END OF PHASE 1 so fabrications
die before composition. New `grounding-verifier` agent (sonnet) does the judgment half
(misreads, scope drift) with a fidelity-only jurisdiction.

## Audience pinned

`_shared/references/reader-profile.md`: curious retail investor, technical comprehension
between advanced high school and early undergraduate, reading for the investment thread.
Replaces pass-5's old "tech-industry analyst" assumption; wired into the composer, pass-5,
pass-7's impatient-investor persona, and the self-audit readers. Per-run override via
`input/essay-context.md`.

## Model allocation (decision + rationale)

Main session: strongest model (Fable 5). Judgment agents (`design-architect`,
`essay-composer`, `editorial-reviewer`, `adversarial-reader`): `model: inherit`. Mechanical
agents (`grounding-verifier`, `figures-prep`): `model: sonnet`. The advisor pattern (Sonnet
main + Fable advisor) was rejected: the final prose can only be as good as the model that
holds the pen and the full context; an advisor sees neither.

## Previously-proposed fixes applied (with regression)

- `2026-06-11-figure-token-panel-suffix` — FIG_RE/FIGREF_RE panel letters (3rd recurrence).
- `2026-06-26-gate-structure-sentence-band-align` — STRUCT-001 warns at ≥8 sentences.
- `2026-06-26-publication-line-wrap` — convention + `strip_publication.py` paragraph rejoin.
- `2026-06-11-claim-scope-lock-map` — Claim scope map (locked/open/pinned) in the
  invention-summary schema + trap-wording rule (field-validated on the 2026-06-24 run).
- `2026-06-26-figure-selection-cover-and-phase` — cover-candidate tag + phase-map keyframes.
- Retro L7 — `essays/<essay-id>/` documented as the tracked-deliverable layout.

## Verification

- `python meta/regression.py` — PASS (88 tests incl. new gates/strip/check_run suites;
  fixtures: clean-baseline, figure-orphan, + new fabricated-quote, hedged-verdict).
- `gate_hedge` sanity-checked against `essays/agility-us12560948/essay-final.md`: PASS,
  zero findings (no false positives on a known-good firm verdict).
- New/changed Python compiles clean; everything except Phase 0's Pillow is stdlib.

## Not done (deliberately)

- `tools/compose_figure_sequence.py` (retro L6 cover-composition tool) — recommended build,
  out of this refactor's scope.
- Phase-4 `promo-composer` port — unchanged, preserved in `docs/source-prompts/`.
- Hooks (auto-gate on draft change) — worth adding once the new loop settles; see retro
  "Hooks worth adding".
