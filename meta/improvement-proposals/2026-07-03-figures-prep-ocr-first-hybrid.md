---
proposal_id: 2026-07-03-figures-prep-ocr-first-hybrid
created: 2026-07-03T00:20:00Z
status: watch  # recurrence 1, but user-seeded priority; pilot recommended on next run
lever: reference-edit (+ new script step in patent-figures-clean)
goal: "2 (indirect: cost/latency of Phase 0)"
root_cause_artifact: patent-figures-clean/SKILL.md process order (vision-first)
recurrence_count: 1
confidence: medium-high (this run's evidence is clean but single)
triggering_findings:
  - essay_id: etched-us12361091, Phase-0 run stats: 16 uniform machine-set sheets, ~15 min, ~255k tokens, 97 tool uses, 0 exception cases
---

## Problem

Phase 0 is vision-first: the agent Reads every staged sheet to name it, again after
geometry fixes, and again in the final verification loop. On clean US-grant sheet sets
(the common case: machine-set "Sheet N of M" headers + typeset "FIG. N" labels, one figure
per sheet) all of that judgment is deterministic. etched-us12361091: 16/16 sheets needed
zero judgment beyond label reading, yet consumed ~255k subagent tokens / ~15 minutes.

## Proposed change

Add an OCR-first pass to `patent-figures-clean/scripts/clean_figures.py` (tesseract, or
pure-Python fallback) BEFORE the vision naming pass:

1. `ocr-triage`: per staged sheet, OCR at 0/90/180/270; pick orientation by best OCR score;
   extract `Sheet (\d+) of (\d+)` (ordering) and all `FIG\.?\s*\d+[A-Z]?` labels (naming).
2. Deterministic checks: sheet numbers contiguous 1..M; label set == the set declared by
   patent.md's BRIEF DESCRIPTION OF THE DRAWINGS; exactly one label group per sheet.
3. All checks green -> auto-name map; the vision agent's role reduces to the EXISTING final
   verification loop (label<->filename spot-check, which stays mandatory — a wrong figure
   name silently poisons FIGREF/FIGUSE downstream).
4. Any check amber (mixed sheets, unreadable labels, set mismatch) -> fall back to the
   current vision-first flow for the affected sheets only.

Fixture: this run's input/figures-raw/ 16-sheet set (copy to meta/fixtures/) as the clean-set
regression case; the agility multi-panel set as the amber case.

## Amendment (2026-07-04, etched-us20240378175)

New evidence class: the vision pass named all 7 files correctly but wrote a WRONG manifest
line (FIG. 6's 605/610 element labels swapped vs spec [0051]); four independent reviewers
had to override the manifest against the image throughout the run. Element-label <-> spec
cross-checking is exactly what a deterministic pass does better (the spec text pairs each
numeral with its name). Recurrence for Phase-0 output defects: 2 runs (cost evidence run 1,
correctness evidence run 2). Also: 7-sheet run took ~4 min/119k tokens (vs 15 min/255k for
16 sheets) — cost scales with sheet count; OCR pass would flatten it.
