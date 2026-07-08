# Attribution table — finding class → goal + owner stage/artifact + lever

The meta-loop's brain. `pipeline-retro` reads this to route each normalized finding to the
*stage and artifact that should have prevented it*, tag it with the north-star goal it
threatens, and pick the default improvement lever. Human-editable: when a new finding class
appears that isn't covered, add a row (that itself is a small reference-edit proposal).

Voice fencing is encoded here on purpose: Phase-3 voice findings route to
`anti-ai-writing.md` / `deliverable-voice-rules.md` or a Phase-2 voice-canon admission — never
to re-exposing `voice-profile.md` in Phase 3.

| Finding class (pattern_tag) | Source signal | Goal | Owner stage | Owner artifact | Default lever |
|---|---|---|---|---|---|
| `anchor-missing` | gate ANCHOR-001 / pass-3 | 1 | design | thesis-architect invention-summary / quote-anchor-conventions | reference-edit |
| `anchor-malformed` | gate ANCHOR-002 | 1 | compose | essay-en-composer/citation-format.md | reference-edit |
| `paraphrase-accidental-drift` | pass-3 3C | 1 | compose | essay-en-composer/citation-format.md | reference-edit |
| `paraphrase-substantive-change` | pass-3 3C | 1 | compose | execution-boundary.md (Plan⊥Execute) | reference-edit |
| `fact-introduced-beyond-spans` | pass-3 3A | 1 | compose | execution-boundary.md | reference-edit |
| `correlation-causation-drift` | pass-3 3D / pass-4 | 1 | compose | causal-reasoning awareness in section-blueprint | reference-edit |
| `figure-orphan` | gate FIGUSE-001 | 2 | compose | essay-en-composer/figure-rendering.md | reference-edit |
| `figure-offplan` | gate FIGUSE-002 | 2 | design/compose | figure-selection.md ↔ figures-rationale.md sync | reference-edit |
| `spec-undercoverage` | pass-3 coverage sub-check | 2 | design | invention-summary 4-layer / phase2-handoff-notes citation priority | reference-edit |
| `sources-enum-violation` | gate SOURCES-002 / pass-6 6C | 4a | compose | x-articles-format-en.md | reference-edit (or gate-promotion) |
| `sources-subgroup-violation` | gate SOURCES-003 / pass-6 6C | 4a | compose | x-articles-format-en.md | reference-edit |
| `lead-conclusion-weak` | pass-6 6A/6B | 4a | design/compose | thesis-spine arc / section-blueprint closing_directive | reference-edit |
| `conclusion-over-hedge` | gate HEDGE-001/002/003 / pass-6 6G (was: SETI catch only) | 4a | design + edit | thesis-spine closing_posture + section-blueprint closing directive + pass-6 6G | gate-promotion (done 2026-07-02) + reference-edit |
| `quote-fabrication` | gate QUOTE-001 (was: pass-3 judgment only) | 1 | design | invention-summary Quotable spans / quote-anchor-conventions verbatim discipline | gate-promotion (done 2026-07-02) |
| `loop-shape-violation` | check_run RUN-001..007 | all | orchestrator | patent-essay SKILL loop policy (round artifacts, dispositions, double-clean) | reference-edit |
| `paragraph-eight-sentence-slip` | gate STRUCT-001 vs pass-2C | 3 / 4a | gate | gate_structure.py threshold (>8 vs >=8) | gate-strengthen |
| `publication-hard-wrap` | publish render | 4a | compose | x-articles-format-en.md + strip-pipeline.md | reference-edit + pipeline |
| `figure-cover-undervalued` | SETI catch / design | 2 | design | invention-summary-schema Figure relationships + SKILL Step 9 | reference-edit |
| `figure-composition-tooling-gap` | cover build | 2 / 4a | tooling | tools/ (no figure-sequence helper) | new-tool |
| `section-thesis-misalignment` | pass-4 | 4a | design | thesis-spine spine→section trace | reference-edit |
| `reader-engagement-break` | pass-5 | 3 | compose | mode-spec posture / section-blueprint | rubric-tuning (posture) |
| `redundancy-bloat` | pass-2 | 3 | compose | section-blueprint word_target | reference-edit |
| `banned-word` | gate BANNED-001 / pass-1 1B | 4b | canon | anti-ai-writing.md → banned_terms.txt | gate-promotion |
| `banned-pattern-recurring` | pass-1 1B (judged) | 4b | canon | anti-ai-writing.md | gate-promotion (if mechanically safe) |
| `em-dash` | gate EMDASH-001 / pass-6 6E | 4b | compose | strip-pipeline.md | reference-edit |
| `voice-canon-cadence-drift` | pass-1 1A | 4b | compose | voice-canon entry (weak/missing) | voice-canon-admission |
| `voice-canon-structural-miss` | pass-1 1A | 4b | compose | voice-canon entry + section-blueprint | voice-canon-admission |
| `meta-reader-instruction` | gate META-001 / pass-1 / pass-7 | 4b | canon | anti-ai-writing.md → gate_meta | gate-promotion (done run 045) |
| `lead-thesis-deferral` | pass-6 6A / pass-7 / human-revision | 4a | design/compose | thesis-spine arc / section-blueprint lead block | reference-edit |
| `nonclaim-section-header` | pass-6 / pass-7 / human-revision | 4a | compose | section-blueprint header / x-articles-format-en | reference-edit |
| `jargon-overdepth` | pass-5 / pass-7 / human-revision | 3 | compose | deliverable-voice-rules.md | reference-edit |
| `steelman-absent` | pass-4 / pass-7 / human-revision | 1 | design | thesis-spine adversarial-defense → phase2-handoff-notes | reference-edit |
| `section-stub-imbalance` | gate STUB-001 / pass-5 / pass-7 | 4a | compose | section-blueprint word_target balance | reference-edit |
| `thesis-restatement-redundancy` | pass-2 / pass-7 | 3 | compose | section-blueprint (sub-mechanism of redundancy-bloat) | rubric-tuning |
| `revision-induced-duplication` | gate DUPE-001 / pass-2 | 4b | compose | essay-en-composer revision-mode re-scan | rubric-tuning |
| `venue-ticker-convention` | gate CASH-001 / pass-6 | 4a | compose | x-articles-format-en.md | reference-edit (done run 045) |
| `procedure-overweight-lead` | gate SURF-005/006 / pass-6 6I / cold-reader early-drag auto-escalation / human-revision | 5 | design + compose | thesis-spine payload tags + spine→section trace / section-blueprint attention budget + reader-energy.md §6 | reference-edit + gate-strengthen (done 2026-07-05) |
| `promo-safe-harbor-overweight` | human-revision (promo v1→v2 owner read; self-check: promo-format Final Checklist bold_selection line) | 5 | promo | promo-composer promo-format.md bold-selection rule + briefing-vocabulary-only reuse | reference-edit (done 2026-07-05, v3 contract) |
| `plain-language-gap` | human-revision (v6→v7 owner read; owned going forward by the Phase 3.7 prose-polish stage) | 3 | edit + architecture | pass-5 reader-perspective calibration + prose-polish SKILL (surface-only 윤문, drift-verified) | new-stage (done 2026-07-05) + rubric-tuning candidate for pass-5 |

## Recurrence ledger summary (auto-maintained by pipeline-retro)

`pipeline-retro` keeps a running count per class here so a human can see system health at a
glance. Counts are derived from `meta/findings-ledger.jsonl`; do not hand-edit the counts.

| pattern_tag | open | watch | proposed | resolved | escalated | patches applied |
|---|---|---|---|---|---|---|
| `redundancy-bloat` | 0 | 6 | 0 | 0 | 0 | 0 |
| `mobile-paragraph-wall` † | 0 | 1 | 4 | 0 | 0 | 0 |
| `external-fact-universalization` † | 0 | 0 | 3 | 0 | 0 | 0 |
| `fence-canon-verification-gap` † | 0 | 0 | 3 | 0 | 0 | 0 |
| `claim-scope-misattribution` † | 0 | 0 | 2 | 0 | 0 | 0 |
| `figure-token-regex-blindspot` † | 0 | 0 | 2 | 0 | 0 | 0 |
| `paraphrase-hedge-compression` † | 0 | 2 | 0 | 0 | 0 | 0 |
| `revision-induced-band-break` † | 0 | 2 | 0 | 0 | 0 | 0 |
| `sources-entry-template-drift` † | 0 | 2 | 0 | 0 | 0 | 0 |
| `banned-pattern-recurring` | 0 | 1 | 0 | 0 | 0 | 0 |
| `quote-notation-gap` † | 0 | 1 | 0 | 0 | 0 | 0 |
| `claim-vs-spec-citation-conflation` † | 0 | 1 | 0 | 0 | 0 | 0 |
| `figuse-selection-scope-overread` † | 0 | 0 | 1 | 0 | 0 | 0 |
| `source-tier-hedge-posture` † | 0 | 1 | 0 | 0 | 0 | 0 |
| `rule-of-three-warn` † | 0 | 1 | 0 | 0 | 0 | 0 |
| `source-pointer-style-drift` † | 0 | 1 | 0 | 0 | 0 | 0 |
| `figure-panel-context-bleed` † | 0 | 1 | 0 | 0 | 0 | 0 |
| `legal-posture-language-slip` † | 0 | 1 | 0 | 0 | 0 | 0 |
| `jargon-gloss-gap` † | 0 | 1 | 0 | 0 | 0 | 0 |
| `fact-introduced-beyond-spans` | 0 | 1 | 0 | 0 | 0 | 0 |
| `quoted-title-emdash-policy-gap` † | 0 | 1 | 0 | 0 | 0 | 0 |

Counts derived from the ledger as of run `045-agility-638-last-mile-moat` (third recorded
run). A class with a proposal on file shows its triggering records under `proposed` (the
proposal file under `meta/improvement-proposals/` lists the triggering finding ids and is the
append-only audit reference).

Cross-essay recurrence (present in 2+/3 essays): `claim-scope-misattribution` (HIGH +
grounding hard-gate breach in runs 1–2 — most damaging class in the system; **did NOT recur in
run 045**, whose grounding/claim pass was clean — the run-045 claim issue was a *citation
notation* mislabel, a different class, see below), `mobile-paragraph-wall` (walls in runs 1–2,
edge-of-band only in run 045), `external-fact-universalization`, `fence-canon-verification-gap`
(escalated low → medium; run-2 resolution field-tested the interrogative-🤔-host fix, no
recurrence in run 045), `redundancy-bloat` (now 3/3 — sanctioned-repetition-layering awareness
again in run 045), `revision-induced-band-break`, `paraphrase-hedge-compression`, and
`figure-token-regex-blindspot` (latent; avoided by convention all runs — recurring mitigation
cost, not failure).

New first-seen classes in run 045 (all `watch`/`proposed`, count 1): **`claim-vs-spec-citation-conflation`**
(the iter-1 MEDIUM — three verbatim CLAIM quotes carried a `[0144]` *spec-paragraph* bracket;
quote TEXT byte-exact, only the attribution LABEL wrong; distinct from `claim-scope-misattribution`,
which is claim *semantics*, and from `quote-notation-gap`, which was a missing "(emphasis added)";
resolved iter-2 by attributing claim quotes by claim in prose + correcting thesis-trace upstream),
**`figuse-selection-scope-overread`** (proposal on file — `gate_figure_use` reads the whole
selection file, so figures in the "Reviewed but NOT selected" section false-count as selected;
one dropped-figure-from-prose away from a spurious goal-2 hard FAIL), `source-tier-hedge-posture`
(a tier-4 source on a hedged non-load-bearing forward pointer — within bounds), and
`rule-of-three-warn` (STRUCT-004 on a factual customer triad — warn-only, behaving as designed).

RECUR_THRESHOLD=3 reached by record count: `external-fact-universalization`,
`fence-canon-verification-gap`, `mobile-paragraph-wall` (proposals on file,
recommended-apply) and `redundancy-bloat` (now at 6, still deliberately HELD at `watch`:
heterogeneous sub-mechanisms — anchor doubling, caption echo, sanctioned-layering awareness,
intensifier tics — no single mechanical rule covers them and the class has never cost a loop
iteration). 6 proposals on file as of 2026-06-24 (5 from `2026-06-11-*.md` + the new
`2026-06-24-figuse-selection-scope.md`). Do not hand-edit the counts.
† = new finding class with no row in the main table above; adding the missing rows is itself
a small reference-edit proposal per this table's header (human decision, still pending from
run 1).

## Self-audit channel — first dataset (origin: self-post-accept)

Run `2026-06-26-us12560948b2-investor-selfaudit` is the first dataset for a third finding
**origin**, alongside `inner-loop` (a pass should have caught it) and `human-post-accept` (only a
human caught it): **`self-post-accept`** — the self-audit loop caught it *adversarially, with no
human in the loop*, after the inner loop returned `pass` and all ten gates were green. Captured
via the same `## delta` channel (`meta/normalize_revision_notes.py --origin self-post-accept`).
This is the empirical answer to "can `/goal` self-check without a human": 15 findings caught and
resolved across three autonomous rounds, convergence verified by a third blind fresh-context pair
that traced two residual off-by-one anchors back to the Phase-1 invention-summary and fixed them at
the source.

Routing for the classes that channel surfaced (added so the ledger records resolve; mirrors the
levers already used for their cousins):

| Finding class (pattern_tag) | Source signal | Goal | Owner stage | Owner artifact | Default lever |
|---|---|---|---|---|---|
| `claim-scope-misattribution` | pass-7 G1 / fresh-context | 1 | design | thesis-architect invention-summary claim-scope map (locked/open/pinned) | reference-edit |
| `legal-posture-language-slip` | pass-7 / fresh-context | 1 | compose | deliverable-voice-rules.md legal register + fact-check-log | reference-edit |
| `prosecution-record-overstatement` | pass-7 G1 / fresh-context | 1 | compose | fact-check-log prosecution-record discipline | reference-edit |
| `figure-caption-scope-deferral` | pass-7 / fresh-context | 2 | compose | caption-roles.md scope-first ordering | reference-edit |
| `anchor-incomplete` | pass-7 G2 / fresh-context | 1 | compose | essay-en-composer/citation-format.md range anchors for multi-paragraph spans | reference-edit |
| `anchor-offbyone` | pass-7 G2 / fresh-context | 1 | design | thesis-architect invention-summary Quotable-spans paragraph labeling | reference-edit (fix at source) |

`nonclaim-section-header`, `lead-thesis-deferral`, `steelman-absent`, `meta-reader-instruction`,
`venue-ticker-convention`, and `revision-induced-duplication` are the run-045 human-revision
classes, now field-tested by the autonomous pass too (caught by `gate_dupe` / pass-7 without a
human). Their rows live with the run-045 dataset. See
`meta/improvement-proposals/2026-06-26-self-audit-origin-and-goal-acceptance.md`.
| `checker-confirmation-round-gap` | check_run RUN-001/RUN-004 false FAIL on spec-mandated no-revision confirmation rounds | all | gate | `_shared/scripts/check_run.py` round-transition model | gate-strengthen |
| `longsent-parser-merge-artifact` | gate LONGSENT-001 warn census (merges across frontmatter/heading/caption/bold boundaries) | 3 | gate | `_shared/scripts/gate_typography.py` sentence splitter | gate-strengthen |
| `figure-selection-parse-overreach` | gate_figure_use parsing figure tokens in NOT-selected rationale rows as selected | 2 | gate | `_shared/scripts/gate_figure_use.py` selection parsing | gate-strengthen |
| `evidence-scope-overreach` | self-audit grounding (absence-claim asserted beyond the run's evidence level) | 1 | design | essay-context template + fact-check-log `evidence_level` field | reference-edit |
| `anchor-pointer-offbyone` / `anchor-under-coverage` | pass-3 / self-audit grounding full table | 1 | compose | essay-en-composer/references/citation-format.md anchor-precision rule | reference-edit |
| `option-embodiment-upgraded` | pass-3 3C (description "may/for example" stated as definite practice) | 1 | compose | essay-en-composer/references/citation-format.md | reference-edit |
| `revision-added-text-drift` | round-N+1 mediums concentrated on round-N added sentences | 1 | compose | essay-en-composer/references/revision-mode.md (new-sentence self-check) | reference-edit |
| `checker-severity-parse-gap` | check_run RUN-003 false FAILs on `prior_severity:` carried-ruling notation | all | gate | `_shared/scripts/check_run.py` severity regex | gate-strengthen |
| `figure-manifest-mislabel` | manifest element-label swap surviving Phase-0 verification (files right, manifest wrong) | 2 | design | patent-figures-clean manifest verification loop | reference-edit (+ OCR cross-check) |
| `caption-anchor-clause-drift` | multi-clause figure captions riding one anchor across clause boundaries | 1 | compose | essay-en-composer figure-rendering caption-anchor discipline | reference-edit |
| `vocabulary-import-from-news` | present-day news vocabulary stated inside the filing's own reasoning | 1 | compose | citation-format.md source-era vocabulary discipline | reference-edit |
| `steelman-overweight` | pass-7 check 3 (two-sided, symmetric with `steelman-absent`) / gate_surface SURF-007 / human-post-accept | 4b | design + edit | adversarial-defense.md steelman-beat concede-and-return spec + pass-7 two-sided check + reader-energy.md §6 + gate_surface SURF-007 | multi (reference-edit + rubric-tuning + gate-strengthen) |

## Run intel-us20260191095-backend-hbm classes (added 2026-07-06)

New/adjacent classes surfaced by this run (routed here so the ledger records resolve). This
run accepted double-clean at round 3 (2 medium + 7 low inner-loop, both mediums fixed by
round 2) and closed a 2-round self-audit; no hard-gate breach. `claim-scope-misattribution`
remained the dominant class (4 this run; 15 across the ledger).

| Finding class (pattern_tag) | Source signal | Goal | Owner stage | Owner artifact | Default lever |
|---|---|---|---|---|---|
| `affirmative-core-contrastive-term-imprecision` | pass-4 (pivotal inference) / pass-2 restatement / self-audit — a `claim-scope-misattribution` sub-mechanism: the spine's affirmative core states the contrastive term ("X can carry it, where Y cannot") as a generic superset of the claim-supported narrow term ("front-end" vs "DRAM front-end"), and Compose inherits it | 1 | design | thesis-architect/references/adversarial-defense.md affirmative-core spec + thesis-spine Mitigation field (**proposal 2026-07-06-affirmative-core-contrastive-precision**, watch; residual of applied claim-scope-lock-map) | reference-edit |
| `term-collision-coherence` | self-audit round-2 medium — a settled-sense headline word ("direction") reused in a being-tested sense in the same high-stakes section; **introduced by a prior revision fix** (extends `revision-added-text-drift` from grounding to coherence) | 4a / 3 | compose | essay-en-composer/references/revision-mode.md new-sentence self-check (broaden to: a headline/load-bearing term keeps its established referent in added text) | reference-edit |
| `caveat-restatement-redundancy` | self-audit round-2 cold-reader last-section drag — a caveat/appositive distinction doubled inside one section; sub-mechanism of `redundancy-bloat` / `thesis-restatement-redundancy` | 3 | compose | essay-en-composer section-blueprint attention budget (reader-energy §6) | rubric-tuning (held at watch with redundancy-bloat) |
| `pending-application-status-precision` | pass-3 / title — "Patent" on a published application (highest-read surface) vs the body's scrupulous pending-vs-granted precision | 1 | design + compose | title-lead-candidates / x-articles-format-en (**proposal 2026-07-04-pending-application-edition**) | reference-edit |
| `checker-confirmation-overfire` | check_run RUN-000 — the confirmation-transition detector mislabeled a REAL revised transition (round 1→2, `revision-response.round-1.md` present) as a confirmation and SKIPPED RUN-003 disposition-coverage; misfired on loose "confirmation" markers that describe what a clean round *triggers next*. Inverse of the applied `2026-07-03-check-run-confirmation-round-model` (that fixed the model under-firing / false RUN-001 FAIL; this is over-firing / false RUN-003 skip). Latent this run (no false-pass; RUN-004 id-continuity still ran), structural masking risk | all | gate | _shared/scripts/check_run.py `_is_confirmation_transition` + the RUN-003 gate that trusts it without a revision-response veto (**proposal 2026-07-06-check-run-confirmation-transition-veto**) | gate-strengthen |

Recurrence note (this run): `figure-selection-parse-overreach` reached its **5th** essay
(gate false-orphaned non-selected figs 2-7; orchestrator reworded to word form) — corroborates
the standing `recommended-apply` proposal `2026-07-05-figuse-selection-scope-promote` (now
recurrence 5, still unapplied; `gate_figure_use.py` remains unpatched). `redundancy-bloat` /
`thesis-restatement-redundancy` again absorbed a large share of self-audit effort (4 deltas) —
still held at `watch` by design (heterogeneous sub-mechanisms, never cost a loop iteration).
`evidence-scope-overreach` paired across origins this run (inner-loop r1-F1 + self-post-accept
SA-delta-9, the same §6 proof-point seam caught twice).
