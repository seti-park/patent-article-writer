---
proposal_id: 2026-07-13-grounding-verifier-modifier-sweep
created: 2026-07-13T12:30:00Z
status: watch
lever: reference-edit
goal: "1"
root_cause_stage: edit
root_cause_artifact: .claude/agents/grounding-verifier.md (anchored-span verification procedure — no modifier-level enumeration step)
recurrence_count: 1
confidence: medium
triggering_findings:
  - essay_id: tesla-wo2026148096-ladder-hoist, source: grounding-check-round-1.md L61 vs grounding-check-round-2.md (round-1 verdicted the line-19 span, flagged "clamp-on" only, note said the rest "all check out" — "cordless" in the SAME span passed; round-2 caught "cordless" as OVERREACHED-BEYOND-ANCHOR ×3 → SA2-FIX-2), pattern_tag: verifier-modifier-sweep-incremental
  - essay_id: tesla-wo2026148096-ladder-hoist, source: grounding-check-round-1.md L73 vs grounding-check-round-3.md #41 (round-1 called the §5 tray elaboration "elaborated correctly later (line 67)"; rounds 1 AND 2 passed "electrical conduit"; round-3 caught it as PARAPHRASE-DRIFT → SA3-FIX-2), pattern_tag: verifier-modifier-sweep-incremental
---

## Problem

The self-audit grounding verifier catches invented **modifiers** only incrementally,
one per round, even inside spans it explicitly verdicts. This run had three invented
modifiers of the same shape — an adjective the source never states, attached to a
correctly-grounded noun:

- "clamp-on" (modules) — caught round 1;
- "cordless" (drill) — **missed round 1 inside an explicitly-verdicted row** (the
  round-1 table quoted the full line-19 sentence, flagged "clamp-on", and wrote
  "'three modules...drill...photovoltaic' all check out"); caught round 2 (3
  occurrences);
- "electrical" (conduit) — **missed rounds 1 and 2** (round 1 even endorsed the
  sentence: "elaborated correctly later (line 67)"); caught round 3.

Each catch was correct and each fix was cheap (drop the adjective), but the pattern
means single-sweep coverage of this defect class is roughly one instance per round —
the run only converged because the audit had three rounds for other reasons. All three
sweeps were the same lane (claude sonnet pin, fresh context per round), so what
eventually caught everything was fresh-context resampling, not procedure. A
same-shape defect that survives to publication is a goal-1 (accuracy) miss on exactly
the surface readers quote.

## Proposed change (exact diff)

**File: `.claude/agents/grounding-verifier.md`** — add one step to the anchored-span
procedure (wording to fit the file's existing step list):

```markdown
+**Modifier sweep (per anchored span):** before writing the row's verdict, enumerate
+every adjective/qualifier attached to a source-derived noun in the span (e.g.
+"cordless drill", "electrical conduit", "clamp-on modules") and check each ONE
+token at a time against the source span. An unsourced modifier is
+PARAPHRASE-DRIFT / OVERREACH even when every other element of the sentence is
+grounded — a row is not GROUNDED until its modifiers are. Field basis: three
+invented modifiers in one run, each caught a round late because the noun checked
+out (tesla-wo2026148096 rounds 1-3).
```

No diff required at watch status beyond the hypothesis above; if the class recurs, the
stronger levers to evaluate are (a) cross-vendor verifier alternation between audit
rounds (the gpt verifier lane already exists for the inner loop) or (b) a same-lane
double-sweep on round 1 only — both cost a lane invocation, so they need a second
essay's evidence first.

## Why this lever

The misses happened inside rows the verifier explicitly examined, so this is a
procedure gap (attention allocation within a span), not a coverage gap between spans —
the cheapest fix is making the modifier check an enumerated step in the verifier's own
reference, which is how the same agent's caption/anchor disciplines are already
encoded. Rubric or lane-topology changes are premature at recurrence 1.

## Regression expectation

No mechanical gates involved (`meta/regression.py` trivially green). Field check on
the next audited run: zero invented-modifier findings surfacing for the first time in
round 2 or later (all instances either caught in round 1 or absent).
