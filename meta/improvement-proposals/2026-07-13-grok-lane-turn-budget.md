---
proposal_id: 2026-07-13-grok-lane-turn-budget
created: 2026-07-13T12:20:00Z
status: watch
lever: reference-edit
goal: "all"
root_cause_stage: tooling
root_cause_artifact: patent-essay/references/compose-lane-grok.md (no turn-budget guidance) + _shared/scripts/cli_lane.py --max-turns default 16
recurrence_count: 2
confidence: medium
triggering_findings:
  - essay_id: tesla-wo2026148096-ladder-hoist, iter: 1, pattern_tag: lane-turn-budget-undersized (lane-substitution.round-1.json — "cli_lane exit 3 — grok CLI nonzero: Error: max turns reached", compose round 1, ~202KB prompt, died pre-draft → inherit)
  - essay_id: tesla-us20260196678-hemmed-tabless, pattern_tag: lane-turn-budget-undersized (ledger incident record — "grok compose round-0 needed --max-turns 48 (default-tier 16 insufficient at ~220KB prompts); 96 used for revision rounds at ~430KB")
---

## Problem

Second essay in a row where the grok compose lane's turn budget was the binding
constraint. Prior run the orchestrator discovered an escalation ladder in-run
(48 turns at ~220KB prompts, 96 at ~430KB — logged to the ledger as
`lane-turn-budget-undersized`); this run the compose lane died pre-draft with
`Error: max turns reached` (exit 3) on a ~202KB prompt
(`handoff/02-compose/lane-substitution.round-1.json`) and the whole compose + all
revision rounds fell back to inherit. The fallback chain worked as designed
(substitution recorded, run completed clean), but the run lost its cross-vendor
compose lane entirely to a budget knob.

Nothing owns this knowledge: `cli_lane.py` documents `--max-turns` only as a
"runaway-turn guard (default 16); NOT the isolation mechanism", and
`compose-lane-grok.md` contains no mention of turns or prompt-size budgeting — so the
prior run's discovered ladder never reached this run's invocation. There is also an
unexamined design question: every grok invoke is deliberately tool-less
(`--tools "" --no-subagents --disable-web-search`), so a compose call should be
close to single-shot — why a ~200KB prompt consumes >16 "turns" (vendor CLI
semantics: continuation/segment counting?) is not established, which caps confidence
at medium.

## Proposed change (exact diff)

**File: `patent-essay/references/compose-lane-grok.md`** — add under the invocation
section:

```markdown
+## Turn budget (required)
+
+`--max-turns` defaults to 16 — a runaway guard, not a working budget. Compose-class
+prompts exhaust it: field data is 48 turns needed at ~220KB and 96 at ~430KB
+(tesla-us20260196678), and a ~200KB compose prompt died pre-draft at a lower budget
+(tesla-wo2026148096). Invoke compose/revision rounds with `--max-turns 64` minimum;
+on `exit 3: max turns reached`, retry ONCE with the budget doubled before recording a
+lane substitution to inherit. Log the working value in the round's lane record so the
+next run inherits the calibration.
+
+Open question for the human applier: grok runs tool-less here, so compose should be
+near single-shot — if the CLI exposes a non-agentic/single-response mode, prefer it
+over turn-budget tuning and record the flag in this section.
```

**Optional companion (same class, separate decision):** `_shared/scripts/cli_lane.py`
could scale the default when the flag is omitted (`32 / 64 / 128` at
`<100KB / <300KB / >=300KB` prompt size). Held out of the primary diff: the
reference-edit alone removes the recurrence (orchestrators always pass the flag), and
silent auto-scaling changes behavior for all lanes, which wants its own test pass.

## Why this lever

The failure is operational knowledge that existed (prior run's ledger) but had no home
artifact, so it did not transfer. A reference-edit to the lane contract is the
cheapest durable fix and is exactly the "runbook note" lever the attribution table
already assigns to the `lane-*` incident family. A script change (auto-scaling or a
single-shot flag) may supersede it, but needs the vendor-CLI turn semantics answered
first — premature to hard-code.

## Regression expectation

No gate fixtures involved (`meta/regression.py` trivially green). Field check on the
next multi-vendor run: compose round-1 completes on the grok lane, or substitutes only
after one doubled-budget retry, with the working `--max-turns` recorded in the lane
record.
