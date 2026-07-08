---
proposal_id: 2026-07-05-figuse-selection-scope-promote
created: 2026-07-05T19:30:00Z
status: recommended-apply
lever: gate-strengthen
goal: "2"
root_cause_stage: gate
root_cause_artifact: _shared/scripts/gate_figure_use.py (selected set parsed from the WHOLE figure-selection.md, incl. NOT-selected / acknowledged-pair rows)
recurrence_count: 5
confidence: high
triggering_findings:
  - essay_id: 045-agility-638-last-mile-moat, pattern_tag: figuse-selection-scope-overread (proposal 2026-06-24, status proposed)
  - essay_id: etched-us12361091, pattern_tag: figure-selection-parse-overreach (proposal 2026-07-03, status watch; false FIGUSE orphans on figs 2/3/8/10/13, composer round-1 self-check)
  - essay_id: etched-us20240378175-r2, pattern_tag: figure-selection-parse-overreach (composer-cited prior workaround: FIG. 4 prose mention to satisfy the gate)
  - essay_id: intel-us20250266395, pattern_tag: figure-selection-parse-overreach (figures-rationale.md family-break note + FIG. 9/10 prose pointers on [0057]/[0058])
  - essay_id: intel-us20260191095-backend-hbm, pattern_tag: figure-selection-parse-overreach (5th essay; gate FIGUSE-001-failed non-selected packaging-variant figs 2-7, orchestrator reworded them to word form at the Phase-1 artifact; routed here by score-history)
supersedes: [2026-06-24-figuse-selection-scope, 2026-07-03-figure-use-selection-scope]
---

## Problem — now crosses RECUR_THRESHOLD (promote the two standing `watch` proposals)

`gate_figure_use` builds its **selected** set by regex-scanning the *entire* text of
`handoff/01-design/figure-selection.md`. But that file, by design, documents the figures the
design deliberately **dropped** as well as the ones it chose — in a "Reviewed but NOT selected"
table and/or a "Paired-figure relationships (acknowledged)" section that **name the dropped
figures again**. Because `_figure_numbers(selection_text)` reads all of it, every dropped figure
is treated as "selected" and then becomes a `FIGUSE-001` **orphan** unless the prose mentions it
anyway. Verified against the live gate today: `gate_figure_use.py:64` still reads
`selected = _figure_numbers(selection_text)` — the fix is **not applied**.

The per-run cost is a **workaround the gate should not require**: composers add a throwaway
one-sentence prose pointer to each dropped figure purely to keep the selected-set parse happy.
This run's `handoff/02-compose/figures-rationale.md` documents it verbatim:

> "§4 covers them in one prose sentence with figure-number pointers on `[0057]`/`[0058]`, which
> **also satisfies `gate_figure_use`'s selected-set parse of `figure-selection.md` (the gate reads
> every figure number in that file, including the acknowledged-pair rows — same resolution as the
> etched-us20240378175-r2 run's FIG. 4 prose mention)**."

That is the composer explicitly naming a **cross-run recurring mitigation**. The class is now
seen in **four essays**: 045-agility (proposal 2026-06-24, `proposed`), etched-us12361091
(proposal 2026-07-03, `watch`), etched-us20240378175-r2 (the workaround the composer cites), and
intel-us20250266395 (this run). Two of those runs are one dropped-figure-absent-from-prose away
from a **spurious goal-2 hard FAIL**. RECUR_THRESHOLD (3) is crossed → this consolidates the two
standing `watch`/`proposed` proposals and promotes them to **`recommended-apply`**.

This run's `figure-selection.md` also shows why the fix must be **section-name-agnostic**: the
dropped figures here live under `## Paired-figure relationships (acknowledged)` (FIG. 9, 10,
2A/2B, 3A/3B, 4A/4B, 6A/6B, 12-15), *not* under a `## Reviewed but NOT selected` heading. The
scoping must key off the **selected** heading and stop at the next H2, whatever the dropped
section is called.

## Proposed change (exact diff)

Apply the diff already drafted and mechanically verified in
`2026-06-24-figuse-selection-scope.md` — scope the **selected** set to the `## Selected figures`
section only, up to the next `## ` heading; the `used` set still scans the whole draft. When the
`## Selected figures` heading is absent (legacy / bare-list inputs, fixtures, the `test_gates.py`
`SELECTION` constant) it falls back to whole-text parsing, so the change is a **strict refinement
with full backward compatibility**. Restated for `.claude/skills/_shared/scripts/gate_figure_use.py`:

```diff
 GATE_ID = "figure_use"
 FIG_RE = re.compile(r"\bfig(?:ure|\.|-)?\s*0*(\d+)\b", re.IGNORECASE)
+# The selected set must come ONLY from the "## Selected figures" section, not from any
+# later section ("Reviewed but NOT selected", "Paired-figure relationships (acknowledged)",
+# "Figure relationships") that also names the dropped figures.
+# Ledger: figuse-selection-scope-overread / figure-selection-parse-overreach (runs 045,
+# etched-us12361091, etched-us20240378175-r2, intel-us20250266395).
+_SEL_HEADING_RE = re.compile(r"^##\s+Selected figures\s*$", re.IGNORECASE | re.MULTILINE)
+_NEXT_H2_RE = re.compile(r"^##\s+", re.MULTILINE)
+
+
+def _selected_region(text):
+    """Substring from the '## Selected figures' heading to the next '## ' heading.
+    If that heading is absent (legacy/bare-list selection), return the whole text so
+    behavior is unchanged for un-sectioned inputs. Section-name-agnostic for the
+    dropped-figure region: it stops at ANY next H2, whatever it is called."""
+    if not text:
+        return text or ""
+    m = _SEL_HEADING_RE.search(text)
+    if not m:
+        return text
+    start = m.end()
+    nxt = _NEXT_H2_RE.search(text, start)
+    return text[start:nxt.start()] if nxt else text[start:]
```

```diff
-    selected = _figure_numbers(selection_text)
+    # Only "## Selected figures" defines the selected set; later sections name dropped
+    # figures and must not be counted as selected (else they false-orphan).
+    selected = _figure_numbers(_selected_region(selection_text))
     used = _figure_numbers(draft_text)
```

Ship with the two `TestFigureUse` cases from `2026-06-24-figuse-selection-scope.md`
(`test_dropped_figures_in_reviewed_section_not_orphaned`,
`test_orphan_still_fails_within_selected_section`) **plus** a new fixture built from this run's
live `figure-selection.md` (selected = {1, 5, 7, 8, 11}; the acknowledged-pair section names
9/10/2/3/4/6/12-15) asserting `selected == {1,5,7,8,11}` and no `FIGUSE-001` when 9/10 are absent
from the draft. FIG. 5A+5B is a single unit (`fig-05AB.png`) — confirm the `FIG_RE` panel handling
resolves it to `{5}` (cross-check with the panel-suffix class, `2026-06-11-figure-token-panel-suffix.md`).

## Why this lever

- The defect lives in the gate script's parse scope (`root_cause_stage: gate`); no reference edit
  changes how the script reads the file. Section-scoping is the minimal mechanical fix.
- **Mechanically safe / strict refinement** — verified 2026-06-24: run-045 live file {1,2,3,4,5}→{1,4,5};
  handoff template {1,2}→{1,2}; both fixtures + the `test_gates.py` `SELECTION` constant identical
  both ways (no `## Selected figures` heading → whole-text fallback), so `figure-orphan` still emits
  `FIGUSE-001` and every existing gate test stays green.
- **Not a reference-edit:** the "mention the dropped figure in prose anyway" trick is exactly the
  per-run cost this retires — a figure the design **dropped** should be allowed to be absent from
  prose without a spurious goal-2 hard fail, and without composers hand-crafting throwaway pointers.
- Promotion is now earned: 4 distinct essays, RECUR_THRESHOLD crossed, exact diff pre-verified.
  `cascade` is not a concern — `gate_figure_use` has **never** been patched for this class (both
  prior records are `watch`/`proposed`, never applied), so this is a first application, not a cascade.

## Regression expectation

Run `python meta/regression.py` before applying. Expected after:

- `python .claude/skills/_shared/scripts/test_gates.py`: all existing cases unchanged (whole-text
  fallback preserves no-heading inputs) + 2 new `TestFigureUse` cases + the intel fixture case pass.
- `python meta/regression.py`: `figure-orphan` fixture still emits `FIGUSE-001` (bare-list selection,
  no `## Selected figures` heading → whole-text fallback → selected {1,2,3} as today); `clean-baseline`
  still passes with no FIGUSE findings.
- Observable next-run criterion: a `figure-selection.md` that drops a figure can omit it from prose
  without a spurious `FIGUSE-001`; a genuine orphan **inside** `## Selected figures` still fails; and
  no composer needs a "prose covers the dropped figure" pointer to satisfy the gate.

## Amendment (2026-07-06, intel-us20260191095-backend-hbm) — 5th corroboration, still unapplied

The class recurred a **fifth** time. `gate_figure_use` FIGUSE-001-failed the non-selected
packaging-variant figures **2-7** as orphans (they are named in token form in the run's
`figure-selection.md`); the draft correctly uses only the 4 selected FIG-1 panels. The
orchestrator's workaround this run was a **new variant** — rewording the non-selected figure
mentions in the Phase-1 artifact to **word form** ("figures two through six", "figures three and
four", "figures five and six") so the gate's regex selected-set reads `{1}`. `score-history.md`
routes it here explicitly: *"Systemic gate limitation (scope selected-set to the explicit
selection table) routed to pipeline-retro (propose-only)."*

Across the five essays the composer/orchestrator has now used **three different** mitigation
forms for the same gate defect — a throwaway prose pointer (etched-us20240378175-r2,
intel-us20250266395), a Footnotes not-placed audit (etched-us12361091), and word-form rewording
(this run). That the workaround keeps mutating is itself evidence the fix belongs in the gate,
not in per-run authoring discipline. The diff above (section-scope the selected set to
`## Selected figures`, whole-text fallback) is unchanged and still the right fix; this run adds
no new requirement, only weight. **The gate script remains unpatched** — recommendation stands
at `recommended-apply`.
