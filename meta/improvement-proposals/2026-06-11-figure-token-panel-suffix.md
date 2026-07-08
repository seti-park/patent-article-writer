---
proposal_id: 2026-06-11-figure-token-panel-suffix
created: 2026-06-11T16:30:00Z
status: applied  # 2026-07-02 architecture refactor; 3rd recurrence (2026-06-26 retro) met the bar; regression PASS
lever: gate-promotion
goal: "2"
root_cause_stage: gate
root_cause_artifact: _shared/scripts/gate_figure_use.py FIG_RE + _shared/scripts/gate_anchors.py FIGREF_RE
recurrence_count: 2
confidence: high
triggering_findings:
  - essay_id: 2026-06-10-us12636684b1-deleted-dome, iter: 0, pattern_tag: figure-token-regex-blindspot
  - essay_id: 2026-06-11-us20260158546a1-both-and-steel, iter: 0, pattern_tag: figure-token-regex-blindspot
---

## Problem

A panel-suffixed figure token like "FIG. 4B" is invisible to both figure-token regexes
(`FIG_RE`, `FIGREF_RE`): the trailing letter removes the `\b` word boundary after the digits
(`\d+` cannot end at a digit→letter position), so a draft whose only reference to figure 4
is "FIG. 4B" is **falsely orphaned** — a spurious `FIGUSE-001` hard fail (goal-2 hard-gate)
— and the token also escapes `FIGREF-001` off-index checking. Verified mechanically against
the current regexes (2026-06-11).

Recurrence determination, as run-1 framed it ("candidate gate-strengthening **if it
recurs**"): the *failure* has not manifested, but the *class* recurred in **2 of 2 runs** as
a mandatory mitigation cost — both runs' `phase2-handoff-notes` had to spend a trap slot
(run 2: trap 3, across **16 lettered panel assets**) mandating the parseable form
"FIG. N (panel X)" and banning "FIG. 2A"-style sole references; the round-2 edit-log had to
re-verify "no letter-suffixed FIG tokens" by hand. Avoidance-by-convention is the mitigation
working — and also evidence the latent defect taxes every run and sits one forgotten token
away from a spurious hard FAIL. Count 2 < RECUR_THRESHOLD(3) → files at `watch`, with the
full diff + tests ready (gate-promotion must ship with tests) so a human can apply early.

## Proposed change (exact diff)

**File 1: `.claude/skills/_shared/scripts/gate_figure_use.py`**

```diff
 GATE_ID = "figure_use"
-# Matches "fig-07", "FIG. 7", "Figure 7", "Fig 7".
-FIG_RE = re.compile(r"\bfig(?:ure|\.|-)?\s*0*(\d+)\b", re.IGNORECASE)
+# Matches "fig-07", "FIG. 7", "Figure 7", "Fig 7", and panel-suffixed "FIG. 7C".
+# The optional single panel letter is needed because a trailing letter removes the
+# \b word boundary after the digits, making "FIG. 4B" invisible and falsely
+# orphaning figure 4 (ledger: figure-token-regex-blindspot, 2/2 runs).
+FIG_RE = re.compile(r"\bfig(?:ure|\.|-)?\s*0*(\d+)[a-z]?\b", re.IGNORECASE)
```

**File 2: `.claude/skills/_shared/scripts/gate_anchors.py`**

```diff
-FIGREF_RE = re.compile(r"\bfig(?:ure|\.)?\s*(\d+)\b", re.IGNORECASE)  # Figure 3 / Fig. 3 / Fig 3
+FIGREF_RE = re.compile(r"\bfig(?:ure|\.)?\s*(\d+)[a-z]?\b", re.IGNORECASE)  # Figure 3 / Fig. 3 / Fig 3 / FIG. 3B
```

**File 3: `.claude/skills/_shared/scripts/test_gates.py`**

```diff
     def test_no_selection_skips(self):
         r = gate_figure_use.check("Figure 1.\n", {})
         self.assertTrue(r["passed"])
         self.assertTrue(_has(r, "FIGUSE-000"))
+
+    def test_lettered_panel_token_counts_for_figure(self):
+        # "FIG. 3B" must count as a reference to figure 3 (no false orphan).
+        draft = "Figure 1, Fig. 2, and FIG. 3B all appear.\n"
+        r = gate_figure_use.check(draft, {"figure_selection_text": self.SELECTION})
+        self.assertTrue(r["passed"], r["findings"])
+        self.assertFalse(_has(r, "FIGUSE-001"))
```

and in `TestAnchors`:

```diff
     def test_figref_in_index_passes(self):
         draft = "Fig. 2 and Figure 3 are referenced.\n"
         ctx = {"invention_summary_text": "", "figures_index": [1, 2, 3]}
         r = gate_anchors.check(draft, ctx)
         self.assertTrue(r["passed"], r["findings"])
+
+    def test_lettered_figref_not_in_index_fails(self):
+        # Panel-suffixed off-index token must no longer escape FIGREF-001.
+        draft = "FIG. 7C shows the gear.\n"
+        ctx = {"invention_summary_text": "", "figures_index": [1, 2, 3]}
+        r = gate_anchors.check(draft, ctx)
+        self.assertFalse(r["passed"])
+        self.assertTrue(_has(r, "FIGREF-001"))
```

Known, accepted limits (verified): plural ranges ("FIGS. 3A-5") and multi-letter panels
("FIG. 4AB") still don't match — the handoff-notes guidance that quoted spans don't count as
the composer's own reference stays valid. The change is a strict superset of current
matches: re-running both regexes over all `meta/fixtures/` files and both archived
`runs/*/essay-final.md` yields identical figure sets (checked 2026-06-11).

## Why this lever

- The defect lives in the gate scripts themselves (`root_cause_stage: gate`); no reference
  edit can fix a regex. Mechanically safe per the verification above (superset; no new
  match on "config 9"-style words because the prefix still requires `fig`).
- If applied, the per-run trap-3 burden shrinks from load-bearing to stylistic: the prose
  form "FIG. N (panel X)" remains the *recommended* reader-facing convention, but a slipped
  "FIG. 7C" warns/fails correctly instead of silently orphaning or escaping the index check.
- Watch, not recommended-apply: the bar is 3 and the failure has never actually fired in a
  run. A third lettered-panel patent (or one actual spurious FIGUSE-001) promotes this.

## Regression expectation

- `python .claude/skills/_shared/scripts/test_gates.py`: all existing cases pass unchanged
  (superset property) + 2 new cases pass.
- `python meta/regression.py`: `figure-orphan` fixture must still emit `FIGUSE-001`
  (`must_contain_check_ids` intact — its draft has no lettered tokens for the orphaned
  figure); `clean-baseline` must still pass with no FIGUSE/FIGREF findings.
