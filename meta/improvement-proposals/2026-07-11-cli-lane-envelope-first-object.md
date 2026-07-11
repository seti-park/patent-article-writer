---
proposal_id: 2026-07-11-cli-lane-envelope-first-object
created: 2026-07-11T14:30:00Z
status: watch
lever: gate-promotion
goal: "all"
root_cause_stage: tooling
root_cause_artifact: _shared/scripts/cli_lane.py (grok JSON envelope parse, json.loads(proc.stdout))
recurrence_count: 1
confidence: high
triggering_findings:
  - essay_id: tesla-us20260196678-hemmed-tabless, pattern_tag: lane-envelope-trailing-data
---

## Problem

The grok lane parses the CLI's JSON envelope with a strict whole-buffer
`json.loads(proc.stdout)` (cli_lane.py ~line 311). Once this run (the first full
multi-vendor production run), grok emitted a **valid JSON envelope followed by trailing
data**; `json.loads` raised `Extra data` and the lane substituted with
`invalid-output` — although the envelope's `document` was intact and usable. Cost: one
avoidable substitution/fallback cycle. Single occurrence → watch.

## Proposed change (exact diff)

**File: `_shared/scripts/cli_lane.py`**

```python
-            try:
-                obj = json.loads(proc.stdout)
+            try:
+                obj, _end = json.JSONDecoder().raw_decode(proc.stdout.lstrip())
                 doc = (obj.get("structuredOutput") or {}).get("document")
                 if doc is None:
                     doc = json.loads(obj["text"])["document"]
                 content = doc
             except Exception as exc:
                 detail = "grok json envelope parse failed: %s" % repr(exc)
```

(First-object capture: identical behavior on clean envelopes; tolerant of trailing
bytes after the envelope; non-JSON garbage still substitutes as before. `obj` must be a
dict — `raw_decode` on a non-object raises or yields a non-dict whose `.get` fails into
the same except branch.)

**Test (`test_cli_lane.py`), shipped with the diff:**
- envelope + trailing junk (`'{"structuredOutput": {"document": "X"}}\nleftover'`) →
  parses, content == "X", no substitution;
- pure garbage stdout → still `invalid-output` substitution;
- clean envelope → unchanged behavior.

## Why this lever

Script-strengthening is the only lever for a parser robustness gap; the vendor CLI's
stdout hygiene is outside our control. Mechanically safe: strictly widens the accepted
input to a superset (first valid JSON object), never changes what a clean envelope
yields.

## Regression expectation

`test_cli_lane.py` full suite green + the three new cases; `meta/regression.py` green
(no gate fixtures involve cli_lane).
