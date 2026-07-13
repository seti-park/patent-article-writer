---
proposal_id: 2026-07-13-lane-log-assessment-key
created: 2026-07-13T12:10:00Z
status: watch
lever: gate-promotion
goal: "all"
root_cause_stage: gate
root_cause_artifact: _shared/scripts/check_run.py ASSESS_RE vs patent-essay/references/review-lane-gpt.md required-output shape (+ cli_lane.py REVIEW_ASSESSMENT_TOKENS)
recurrence_count: 1
confidence: high
triggering_findings:
  - essay_id: tesla-wo2026148096-ladder-hoist, iter: 1-3, pattern_tag: checker-lane-assessment-key-mismatch (edit-log.round-{1,2,3}.gpt.md emit `assessment:`; orchestrator bridged via acceptance block each round)
  - essay_id: tesla-wo2026148096-ladder-hoist, source: essays README known-defect note ("check_run needed `overall_assessment:` in the orchestrator acceptance block (gpt-lane logs use `assessment:`)")
---

## Problem

Two halves of the same contract name the review verdict key differently:

- **Checker + canon:** `check_run.py` L157 `ASSESS_RE =
  re.compile(r"^\s*overall_assessment:\s*(\S+)", re.M)` — RUN-002 FAILs an edit-log
  with "no parsable overall_assessment". `editorial-review/references/feedback-format.md`
  L15 also specifies `overall_assessment:`.
- **Lane prompt + lane validator:** `patent-essay/references/review-lane-gpt.md`
  ("Reproduce the following shape **exactly**") requires the bare key
  `assessment: pass | revise-recommended | revise-required`, and
  `cli_lane.py --validate review` (REVIEW_ASSESSMENT_TOKENS, L67-71) checks the
  substring `"assessment: pass"` etc. — satisfied by either key, so the drift is
  invisible at capture time.

This run, all three gpt review-lane logs (`edit-log.round-{1,2,3}.gpt.md`) dutifully
emitted `assessment:` per their prompt; `ASSESS_RE` cannot parse that (anchored
`^\s*overall_assessment:`), so the orchestrator had to write `overall_assessment:`
into its prepended acceptance block in every canonical `edit-log.round-N.md` to keep
RUN-002/RUN-014 and double-clean acceptance working. The bridge is manual, undocumented
as a *requirement*, and a future orchestrator that promotes a lane log without the
acceptance-block key gets a false RUN-002 FAIL on a valid round — or, worse, an
unparsed `assessments={}` weakening RUN-005 acceptance reasoning. Deterministic on
every gpt-review round while the two templates disagree.

## Proposed change (exact diff)

**1. `_shared/scripts/check_run.py`** — accept the lane key as a fallback, canonical
key preferred (first match; acceptance blocks are prepended, so an orchestrator ruling
always wins):

```python
 ASSESS_RE = re.compile(r"^\s*overall_assessment:\s*(\S+)", re.M)
+ASSESS_LANE_RE = re.compile(r"^\s*assessment:\s*(\S+)", re.M)
```

and at the RUN-002 parse site (~L574):

```python
-        m = ASSESS_RE.search(text)
+        m = ASSESS_RE.search(text) or ASSESS_LANE_RE.search(text)
```

(`^\s*assessment:` cannot match an `overall_assessment:` line — the anchor sees
`overall_` first — so precedence is strict: canonical key, then lane key.)

**2. `patent-essay/references/review-lane-gpt.md`** — align the required shape to the
canon so new lane logs are self-contained:

```markdown
-a `round_type:` line, an `assessment:` token from
+a `round_type:` line, an `overall_assessment:` (or `assessment:`) token from
...
-assessment: pass | revise-recommended | revise-required
+overall_assessment: pass | revise-recommended | revise-required
```

(`cli_lane.py` REVIEW_ASSESSMENT_TOKENS need no change — substring matching already
accepts `overall_assessment: pass`; archived bare-`assessment:` logs stay valid via
the checker fallback.)

**3. Tests (`test_gates.py` check_run cases), shipped with the diff:**

- edit-log with only `assessment: pass` ⇒ parsed (no RUN-002), value `pass`;
- edit-log with acceptance block `overall_assessment: revise-recommended` above a lane
  `assessment: pass` ⇒ parsed value `revise-recommended` (orchestrator ruling wins);
- edit-log with neither ⇒ RUN-002 fail unchanged.

## Why this lever

The lane emitted exactly what its prompt demanded — no reference-edit to the lane
alone can fix a checker regex, and no checker edit alone removes the template
contradiction; the pair (checker fallback + template alignment) closes it from both
sides, like 2026-07-11-check-run-template-string-scoping did for CAP_HIT_RE.
Mechanically safe: the fallback only fires when the canonical key is absent, which
today is precisely the false-FAIL case.

## Regression expectation

check_run cases in `test_gates.py` + `meta/regression.py` green; this run's archived
handoff verifies PASS unchanged (acceptance blocks present), and the same handoff with
the acceptance-block `overall_assessment:` line removed goes from RUN-002 FAIL to
parsed via the lane key.
