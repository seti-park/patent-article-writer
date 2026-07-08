---
proposal_id: 2026-07-03-figure-use-selection-scope
created: 2026-07-03T00:20:00Z
status: watch
lever: gate-strengthen
goal: "2"
root_cause_artifact: _shared/scripts/gate_figure_use.py figure-selection.md parsing
recurrence_count: 1
confidence: high (mechanically reproduced in-run)
triggering_findings:
  - essay_id: etched-us12361091, composer round-1 gate self-check: false FIGUSE orphans on figures 2/3/8/10/13
---

## Problem

gate_figure_use derives the "selected set" from every figure token in figure-selection.md —
including tokens inside the NOT-selected rationale rows (the audit trail of what was
considered and rejected). Phase-1's honest rejection documentation therefore inflates the
selected set and false-orphans unplaced figures. This run worked around it with a truthful
not-placed audit in the draft's # Footnotes (stripped from publication), which is a
side-channel the gate shouldn't require.

## Proposed change

Scope the parser to the selected-figures table/section only (figure-selection.md has a
stable "selected" table and a separate rationale section; parse the former, ignore the
latter), or honor an explicit `<!-- gate: not-selected -->` fence. Ship with a fixture
mirroring this run's figure-selection.md. Remove the footnote-audit workaround note from
essay templates once applied.
