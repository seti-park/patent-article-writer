# Reader-first architecture overhaul (2026-07-04)

**Motive.** The 2026-07-04 blindspot review of the etched-us20240378175 run found that the
pipeline's outputs are optimized for the declared rubric, and the rubric under-specifies the
reader: all four north-star goals measure accuracy, coverage, comprehension, and structural
soundness; none measures whether the reader leans in, keeps reading, or leaves armed with
something to say. The result is report-genre essays (verdict-insurance stacked into the
first paragraph, gap-framed headers, aphorisms sanded off by count rules) shipped to a
column-genre venue. The composer did not game the review; the spec got maximized. This
overhaul adds the missing axis and rebalances jurisdiction between accuracy and energy.

Evidence: blindspot findings B1–B6 (conversation, 2026-07-04); pass-7 item 1's BLUF rule;
v7 §1's disclaimer-stack (three defensive facts before the discovery beat); the two-pass
title compromise; sa-round echo rules cutting signature lines; zero feed-context checks.

## As-is → To-be at a glance

| # | As-is | To-be | Files |
|---|-------|-------|-------|
| T1 | 4 north-star goals (accuracy, figures, comprehension, structure/verdict) | **Goal 5: reader energy** — the reader leans in at the lead, keeps momentum, leaves armed with a repeatable sentence; traceability rows added | `_shared/references/scoring-rubric.md` |
| T2 | reader-profile = comprehension tier only | **Reader jobs** section: information / feeling / social jobs + the required **leaving-sentence** ("the one sentence the reader wants to say to someone after reading") as a per-run essay-context field | `_shared/references/reader-profile.md` |
| T3 | no energy doctrine | **New reference `reader-energy.md`**: energy registers (discovery / tension / contrarian / insider / stakes); discovery-first lead pattern; defensive-open definition; feed-context rules (title ≤ 70 chars, cover caption numeral budget, first-two-lines test); protected signature lines (≤3, declared) | `_shared/references/reader-energy.md` (new) |
| T4 | Phase 1 competes thesis candidates only; title chosen by composer from a pattern list | Phase 1 also emits **`title-lead-candidates.md`**: 5 title+lead pairs, one per energy register, all riding the same factual spine; orchestrator surfaces them (human may pick; default = recommended pick with rationale) | `thesis-architect/SKILL.md` |
| T5 | Lead directive: verdict (BLUF) in ¶1 | **Hook-first lead**: ¶1 delivers the discovery/tension beat; the full (two-sided) call lands by the END of the lead section. Verdict-insurance facts (status labels, liens) may not precede the discovery beat | `essay-en-composer/SKILL.md` (+ lead/closing directive refs) |
| T6 | Echo/count rules treat aphorisms as restatements | Composer declares up to 3 **signature lines** in thesis-trace; reviewers exempt them from echo counts (factual findings still apply) | composer + `editorial-review` refs |
| T7 | Pass 6 checks lead/close format; pass 7 item 1 = BLUF present | Pass 6 gains **6H defensive-open guard** (disclaimers stacked before the discovery beat = finding, symmetric with 6G); pass 7 item 1 redefined: hook in ¶1 AND call by lead's end; **surface jurisdiction** note: title/headers/lead style belong to the energy contract — style-sanding them is out of scope, energy violations are findings | `editorial-review/SKILL.md` + feedback refs |
| T8 | Self-audit = 2 rubric-derived personas + verifier | **+1 cold reader**: checklist-FREE persona (casual scroller); reports only where they stopped, what they felt, what they'd repeat to a friend. Multi-vote unchanged; cold-reader input feeds energy findings | `patent-essay/SKILL.md` |
| T9 | No mechanical surface checks | **New `gate_surface.py`** (warn-level): SURF-001 title > 70 chars; SURF-002 qualifier-led first body sentence (reuse gate_hedge lexicon); SURF-003 cover-caption reference-numeral density > 6; SURF-004 defensive-open pattern in the first two body sentences (status/lien/rejection lexicon before any discovery verb) | `_shared/scripts/gate_surface.py` (new) + `run_gates.py` + tests |
| T10 | check_run false-fails on confirmation rounds and `prior_severity:` notation; LONGSENT merges across structural boundaries | Apply the two **recommended-apply proposals**: confirmation-transition modeling + carried-ruling severity parsing; typography splitter breaks at frontmatter/heading/caption/bold boundaries | `check_run.py`, `gate_typography.py` + tests |

## Jurisdiction rule (the core of the rebalance)

- **Accuracy contract** (unchanged, binds the BODY): anchors, quotes, claim scope,
  attribution, evidence levels, hedge symmetry. Grounding fix priority anchor → narrow →
  label → cut. Nothing in this overhaul relaxes any accuracy gate.
- **Energy contract** (new, binds the SURFACE): title, cover caption, section headers, the
  lead's first paragraph, signature lines. Owned by the leaving-sentence + chosen energy
  register. Review may flag energy violations (defensive-open, gap-framed headers, buried
  discovery) and factual errors on the surface — but not sand its style for count rules.
- Conflicts resolve accuracy-first ONLY for factual defects; style/count conflicts resolve
  energy-first on the surface.

## Acceptance criteria for this overhaul

1. `python .claude/skills/_shared/scripts/test_gates.py` and `python meta/regression.py`
   PASS after T9/T10.
2. A full pipeline re-run on US 2024/0378175 A1 (essay-id `etched-us20240378175-r2`)
   completes to double-clean + self-audit (incl. cold reader) + check_run PASS **without
   the orchestrator hand-writing transition/continuity records** (T10 proves itself).
3. The r2 essay's ¶1 leads with the discovery beat; the leaving-sentence is deliverable
   from the title + lead alone; all v7 accuracy invariants still hold (spot-verified).
4. Side-by-side comparison (v7 vs r2) shipped to the author for the iterate-or-PR call.

## Out of scope (unchanged proposals remain propose-only)

Phase-0 OCR-first hybrid (2026-07-03 proposal; orthogonal to this axis), gate_figure_use
selection-scope fix (watch), external-fact evidence-scope template change (already honored
in practice by essay-context authorship).

## Leaving-sentence for the r2 run (author may override)

"Etched wrote the no-switch memory idea into its first patent filing in May 2023, two years
before the hype thread — the patent office just hasn't said yes yet."
