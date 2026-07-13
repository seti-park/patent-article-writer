---
proposal_id: 2026-07-13-figures-index-filename-parse
created: 2026-07-13T12:00:00Z
status: watch
lever: gate-promotion
goal: "2"
root_cause_stage: gate
root_cause_artifact: _shared/scripts/gate_anchors.py + _shared/scripts/run_gates.py (_parse_figures_file, duplicated) vs patent-understand SKILL figures-index provisioning
recurrence_count: 1
confidence: high
triggering_findings:
  - essay_id: tesla-wo2026148096-ladder-hoist, source: grounding-check-round-1.md L29-40, pattern_tag: gate-figures-index-format-mismatch
  - essay_id: tesla-wo2026148096-ladder-hoist, source: grounding-check-round-2.md L23-25 + round-3 L20 (workaround repeated), pattern_tag: gate-figures-index-format-mismatch
  - essay_id: tesla-wo2026148096-ladder-hoist, source: essays README known-defect note ("numeric temp list workaround used throughout")
---

## Problem

`--figures` on `gate_anchors.py` / `run_gates.py` crashes with
`ValueError: invalid literal for int() with base 10: 'fig-01A.png'` on the
`figures-index.txt` the pipeline actually ships. `_parse_figures_file` (duplicated
verbatim in both scripts) does `int(tok)` on every comma/whitespace token; the run's
`handoff/01-design/figures-index.txt` is filename-per-line (`fig-01A.png` …
`fig-08C.png`).

The format split is contract-level: `contracts/stages/figures.yaml` L25 and
`patent-figures-clean/SKILL.md` L77-79 say "one integer per line", but
`patent-understand/SKILL.md` L145 says "Ensure `handoff/01-design/figures-index.txt`
exists **from `input/figures/` listing**" — a listing of `input/figures/` is filenames,
which is what understand produced this run (the figures stage was skipped; figures
survived bootstrap). `thesis-architect/SKILL.md` L140 ("Ensure `figures-index.txt`
exists") states no format at all.

Cost this run: **every** worker that ran the anchors gate hand-derived a numeric temp
list (`fig-01A/1B→1 … fig-08A/B/C→8 ⇒ 1,2,3,4,5,6,7,8`) — grounding verifier rounds
1, 2, and 3 each documented the derivation (`--figures /tmp/.../figures-index-ints.txt`
/ "temp file containing 1,2,3,4,5,6,7,8"), and the review-loop `run_gates` invocations
rounds 1-3 supplied a figures context too (no FIGREF-000 "skipped" warn in any
`gate-result.round-N.json`). Deterministic on every future run provisioned by the
understand path. Threatens goal 2 indirectly: a worker that skips the workaround
loses figure-reference checking entirely (FIGREF-000 downgrade).

## Proposed change (exact diff)

**Files: `_shared/scripts/gate_anchors.py` and `_shared/scripts/run_gates.py`**
(same helper in both; patch both copies):

```python
 def _parse_figures_file(path):
-    """Parse a figures file: one integer per line, or comma-separated."""
+    """Parse a figures file: integers (line/comma separated) or canonical
+    fig-NN[panel].png filenames (one per line), as the pipeline ships them."""
     with open(path, "r", encoding="utf-8") as fh:
         raw = fh.read()
     nums = []
     for tok in re.split(r"[,\s]+", raw.strip()):
-        if tok:
-            nums.append(int(tok))
-    return nums
+        if not tok:
+            continue
+        m = re.match(r"(?:fig-)?0*(\d+)[A-Za-z]?(?:\.png)?$", tok, re.I)
+        if m is None:
+            raise ValueError("unrecognized figures-index token: %r" % tok)
+        nums.append(int(m.group(1)))
+    return sorted(set(nums))
```

Plain integers parse exactly as before (`12` → 12); `fig-08A.png` → 8; panel siblings
dedupe (`fig-01A`/`fig-01B` → one 1, harmless — `figref` consumes the list as a set);
garbage still raises. **Test (`test_gates.py`), shipped with the diff:**

- filename-per-line file (this run's 12 names) ⇒ `[1, 2, 3, 4, 5, 6, 7, 8]`;
- `"1,2,3"` and one-int-per-line ⇒ unchanged results;
- `"not-a-fig.txt"` ⇒ `ValueError`.

## Why this lever

The mismatch is between a parser and the artifact the pipeline actually produces;
only widening the parser fixes all consumers at once (verifier rounds, review-loop
gates, scoring-rubric's documented invocation). The alternative reference-edit
(rewrite patent-understand L145 to emit integers) still leaves filename lists in
every existing run directory, discards panel information, and keeps the file
human-opaque; parser widening is strictly compatible with both contract formats.
Mechanically safe: accepted input becomes a superset; unrecognized tokens still fail
loudly.

## Regression expectation

`test_gates.py` full suite + the three new cases green; `meta/regression.py` green.
This run's `handoff/01-design/figures-index.txt` passed raw to
`gate_anchors.py --figures` yields the same PASS the temp-list workaround produced.
