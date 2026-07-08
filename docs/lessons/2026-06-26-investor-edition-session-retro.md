# Session retro — investor-edition run on US 12,560,948 B2 (2026-06-26)

A consolidated handoff of the lessons from one full arc: an ad-hoc investor article, then a
formal-pipeline rewrite, then a long figure/cover-composition pass. It maps each lesson to a
concrete repo change (skill / reference / gate / tool / hook / CLAUDE.md) and a lever, and points
to the propose-only files where the change is staged. Propose-only discipline holds: nothing here
edits a skill or gate directly; a human applies after `meta/regression.py`.

## The arc in one paragraph

The ad-hoc (pre-pipeline) draft passed all six gates yet needed three SETI catches to ship
(8-sentence paragraphs the gate let through, a revision that re-introduced one, and an over-hedged
verdict). The formal-pipeline rewrite, with those lessons pinned into `thesis-spine.md`
(firm-closing posture + claim-scope map) and drafted to the paragraph band, cleared the Edit loop
in one round. Then a long tail of work to build the FIG. 5 cover surfaced a separate cluster of
figure/tooling gaps. The through-line: the cheap place to fix a defect is the design hand-off, not
the late loop, and several recurring costs are mechanical gaps the system can close.

## Lessons → improvements

### L1. The rubric gates overreach, not over-hedge (goal 4a; edit + design)
- **Observed:** the ad-hoc verdict led with "qualified yes", set moat and limits as equal weights
  ("limits are equally real"), and re-listed caveats. All six passes are blind to it; only a human
  caught it. Passes 3/4 defend against claiming too much; nothing defends against concluding too
  little.
- **Improvement:** (a) add a pass-6 `6G` over-hedge sub-check + an investor/verdict firm-closing
  default in `posture-lens.md` (reference-edit); (b) have `thesis-architect` *default* a
  firm-closing posture for verdict/investor editions, so Compose drafts it firm from the start
  (this is what made the pipeline rewrite pass in one round).
- **Status:** proposed — `meta/improvement-proposals/2026-06-24-conclusion-over-hedge-check.md`.
  Extend that proposal to cover the thesis-architect default.

### L2. 8-sentence paragraphs slip the gate (goal 3/4a; edit)
- **Observed:** `gate_structure` STRUCT-001 warns at `> 8` sentences (i.e. 9+), but editorial
  Pass 2C flags `>= 8` as high. Exactly-8-sentence paragraphs pass the gate and fail the editor.
  The ad-hoc run hit this three times, once as a *regression a fix introduced* (splitting one long
  paragraph pushed an adjacent one to 8).
- **Improvement:** (a) align the gate to the editor: STRUCT-001 warns at `>= 8` (one-line constant
  change + a test) so the mechanical layer matches Pass 2C; (b) a recount-after-split discipline
  note in editorial-review / composer revision-mode (a split/merge can move a neighbor across the
  band — re-count every paragraph after any structural edit).
- **Status:** NEW — `meta/improvement-proposals/2026-06-26-gate-structure-sentence-band-align.md`.
  Complements the existing `2026-06-11-gate-structure-word-wall.md` (word-count walls); together
  they make paragraph length fully mechanical.

### L3. Hard-wrapped publication renders ragged (goal 4a; compose)
- **Observed:** the draft was hard-wrapped at ~95 columns; in X Articles (and any renderer that
  honors single newlines) the mid-sentence breaks show as ragged line breaks. Publication markdown
  wants one line per paragraph.
- **Improvement:** (a) state the convention in `x-articles-format-en.md` (publication.md = one line
  per paragraph, blank line between); (b) add a paragraph-rejoin step to the strip pipeline so it
  normalizes hard wraps mechanically (the pipeline already strips frontmatter/footnotes).
- **Status:** NEW — `meta/improvement-proposals/2026-06-26-publication-line-wrap.md`.

### L4. Lettered figure panels are invisible to the figure regex (goal 2; gate) — 3rd recurrence
- **Observed:** `FIG. 5A` does not parse in `FIG_RE` / `FIGREF_RE` (the trailing letter removes the
  word boundary after the digit), so a draft that referenced only lettered panels would falsely
  orphan figure 5. This run carried a bare `FIG. 5` token to work around it — the same mitigation
  cost the ledger logged on runs 1 and 2. This is the third occurrence.
- **Improvement:** extend `FIG_RE` / `FIGREF_RE` with an optional panel-letter suffix, shipped with
  `test_gates.py` cases; keep `FIG. N (panel X)` as the stylistically preferred prose form.
- **Status:** proposed — `meta/improvement-proposals/2026-06-11-figure-token-panel-suffix.md`.
  Recurrence count is now 3 → recommend promoting from `watch` to apply.

### L5. Figure selection under-weights visual/cover value and sequence-to-phase mapping (goal 2; design)
- **Observed:** the FIG. 5 kneel sequence — the filing's most striking visual and the most literal
  picture of the claimed step (lowering the center-of-gravity) — was nearly dropped for economy.
  When it was used, frames were first chosen by visual spacing, not by the patent's own four-phase
  decomposition ([0046]-[0047]). The patent *defines* the core movement set; the figure plan should
  inherit that, not improvise it.
- **Improvement:** add to `thesis-architect` figure-selection guidance: (a) a **cover-candidate**
  tag identifying the single most visually compelling figure for the 5:2 header, separate from the
  argument-economy selection; (b) for multi-panel sequences, map selected keyframes to the patent's
  own phase paragraphs (cite the paragraph that enumerates the phases) rather than to visual
  spacing; (c) do not drop a sequence that *depicts the claimed core step* purely for economy.
- **Status:** NEW — `meta/improvement-proposals/2026-06-26-figure-selection-cover-and-phase.md`.

### L6. Cover/figure composition is undocumented and untooled (goal 2/4a; tooling)
- **Observed:** building the FIG. 5 cover took many iterations: ground-line alignment across
  heterogeneous source sheets, uniform captions (replacing varied source labels), even spacing, and
  the 5:2 cover aspect — all re-derived from scratch. A real time-sink was a PIL gotcha:
  `Image.getbbox()` trims **black** borders, not white, so white-background trims were silent
  no-ops; the fix is `ImageChops.difference` against white.
- **Improvement:** (a) a reusable `tools/compose_figure_sequence.py` that crops panels from a
  multi-panel composite, detects and aligns the ground line, renders uniform captions, spaces
  evenly, and emits at the 5:2 cover spec; (b) a short `docs/figure-composition.md` (or a section in
  `tools/header-style.md`) recording the 5:2 spec, baseline-alignment, uniform-caption, even-spacing,
  and the white-trim gotcha; (c) a one-line pointer in CLAUDE.md so future runs reuse it.
- **Status:** NEW — recommended build (new-tool). Spec is in this retro; ready to implement on
  request. The composition logic from this session can seed it directly.

### L7. The tracked-deliverable location was improvised (structure)
- **Observed:** `handoff/` and `runs/` payloads are gitignored (per-run ephemera), so the committed
  deliverable needed a tracked home. This run used `essays/<essay-id>/` with the full phase tree
  (`handoff/01-design`, `02-compose`, `03-edit`) plus `essay-final.md`, `gate-result.json`,
  `score-history.md`, `edit-log.md`, and `figures/`. Good pattern, but undocumented.
- **Improvement:** document `essays/<essay-id>/` as the canonical tracked-deliverable location and
  its layout in CLAUDE.md (Architecture / "How to run"), so it is standard, not improvised.
- **Status:** NEW — CLAUDE.md edit (small).

### L8. Prevent upstream, not repair in loop (meta-principle; validated)
- **Observed:** ad-hoc run = 3 review rounds; formal run with the same lessons pinned into
  `thesis-spine.md` = 1 round. The loop's job became confirmation, not repair. This field-tests
  `claim-scope-lock-map` (applying the map manually prevented the misattribution class) and the
  over-hedge proposal (the pinned firm-closing posture held).
- **Improvement:** promote the validated propose-only files (claim-scope-lock-map at minimum), and
  bias `thesis-architect` toward carrying *more* pre-commitments (posture, claim-scope map,
  cover-figure choice) into the spine, where they are cheap.

## Hooks worth adding

- **Auto-gate on draft change / pre-commit.** A `Stop` or pre-commit hook that runs
  `python .claude/skills/_shared/scripts/test_gates.py` and, when an `essay-draft.md` /
  `essay-final.md` is in the working tree, `run_gates.py` against it, surfacing any fail. This
  catches gate regressions (and, once L2 lands, the 8-sentence case) without a manual run — the
  ad-hoc run's defects would have been flagged automatically. Configure in `.claude/settings.json`.
- **Web-session readiness.** The `session-start-hook` skill already exists for ensuring
  python/tests run in web sessions; keep it covering `test_gates.py` + `meta/regression.py`.

## CLAUDE.md edits worth making

- Document `essays/<essay-id>/` as the tracked-deliverable location + layout (L7).
- Add a one-line pointer to the figure/cover spec (5:2) and the composition tool (L6) under
  Customization / the figures note.
- Note the publication line-wrap convention (L3) where the strip pipeline is described.

## Already-captured / recurrence bumps (no new file needed)

- `figure-token-regex-blindspot` → 3rd occurrence this run; existing proposal should be applied.
- `conclusion-over-hedge` → proposal on file; extend to the thesis-architect default.
- `claim-scope-misattribution` + `external-fact-universalization` → both **did not recur** this run
  with the maps applied, which is positive evidence for promoting their proposals.

## Index of proposals referenced

| Lever | File | New / existing |
|---|---|---|
| reference-edit | `2026-06-24-conclusion-over-hedge-check.md` | existing (extend) |
| gate-strengthen | `2026-06-26-gate-structure-sentence-band-align.md` | NEW |
| reference-edit + pipeline | `2026-06-26-publication-line-wrap.md` | NEW |
| gate-strengthen | `2026-06-11-figure-token-panel-suffix.md` | existing (apply; 3rd recurrence) |
| reference-edit | `2026-06-26-figure-selection-cover-and-phase.md` | NEW |
| new-tool | `tools/compose_figure_sequence.py` + `docs/figure-composition.md` | recommended build |
| claude.md-edit | `essays/<id>/` layout + figure/cover + line-wrap pointers | recommended |
