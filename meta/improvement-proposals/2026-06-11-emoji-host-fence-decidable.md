---
proposal_id: 2026-06-11-emoji-host-fence-decidable
created: 2026-06-11T16:30:00Z
status: recommended-apply
lever: reference-edit
goal: "4b"
root_cause_stage: canon
root_cause_artifact: _shared/references/anti-ai-writing.md (emoji allowance conditioned on a canon pattern not visible inside the Phase-3 fence)
recurrence_count: 3
confidence: high
triggering_findings:
  - essay_id: 2026-06-10-us12636684b1-deleted-dome, iter: 1, pattern_tag: fence-canon-verification-gap
  - essay_id: 2026-06-10-us12636684b1-deleted-dome, iter: 2, pattern_tag: fence-canon-verification-gap
  - essay_id: 2026-06-11-us20260158546a1-both-and-steel, iter: 1, pattern_tag: fence-canon-verification-gap
---

## Problem

The anti-ai-writing emoji allowance — "**emoji** (only 🤔 at a `closing-open-question`
ending)" — has a qualifying condition the Phase-3 editor **cannot decide inside the voice
fence**: when the essay lands on a declarative aphorism (a real voice-canon pattern,
`closing-aphoristic-landing-circuit-contract`), only the canon entries say whether 🤔 is
sanctioned, and the fence (deliberately) hides the canon from Phase 3.

3 ledger records, 2 distinct instances, **2 of 2 essays**, escalating low → medium:

- Run 1 (low, carried iters 1→2): essay-end 🤔 on a blended closing; editor could not verify
  the cited canon entries and punted to SETI both rounds.
- Run 2 (medium, F7): 🤔 on a declarative landing again undecidable; **resolved by the
  composer re-hosting the emoji on a genuine open question** ("Can a die keep what the
  printer draws? 🤔") so anti-ai-writing's rule alone decides, no canon access needed. The
  composer wrote an explicit precedent note for pipeline-retro — *"prefer interrogative 🤔
  hosts because declarative-aphorism + 🤔 is not verifiable under the Phase-3 fence"* — and
  the round-2 editor endorsed it. That precedent currently lives only in a per-run
  `thesis-trace.md` and evaporates next run unless codified.

Record count 3 = RECUR_THRESHOLD, cross-essay 2/2, and the fix is field-tested (run 2 v2
passed with it) → `recommended-apply`, confidence high.

## Proposed change (exact diff)

**File: `.claude/skills/_shared/references/anti-ai-writing.md`** — make the allowance
self-contained (fence-decidable):

```diff
 - **Boldface overuse** (also `STRUCT-002`); **inline-header vertical lists**; **Title Case in
-  body headings** where sentence case is the house style; **emoji** (only 🤔 at a
-  `closing-open-question` ending).
+  body headings** where sentence case is the house style; **emoji** (only 🤔 at a
+  `closing-open-question` ending, and the sentence hosting 🤔 must itself be that open
+  question — interrogative, ending in "?". A declarative/aphoristic host does not qualify,
+  even where a voice-canon entry sanctions the cadence: no canon entry is visible inside
+  the Phase-3 fence, so the allowance must be decidable from this rule alone. Composers:
+  when a closing hybrid offers both, put 🤔 on the question, not the aphorism).
```

## Why this lever

- This is run-1's own recommendation ("restate the qualifying condition mechanically in
  anti-ai-writing.md … both fence-visible") executed with run-2's validated wording.
- **Voice fence preserved exactly as the attribution table requires**: the Phase-3 voice
  finding routes to the anti-ai canon — `voice-profile.md` and the canon entries stay
  invisible to Phase 3. The alternative (re-exposing canon entries to the editor) is the
  forbidden direction; the other alternative (a Phase-2 canon-conformance declaration the
  editor must trust) weakens the review's independence.
- Trade-off, stated openly: this constrains the canon-sanctioned declarative-aphorism + 🤔
  ending (`circuit-contract`) at essay-end. The canon entry remains valid for cadence; only
  the 🤔 attachment now requires an interrogative host. Run 2 demonstrated the cost is ~zero
  (the hybrid re-host read *better* and passed).
- Not gate-promotion: 🤔-followed-by-"?" is regexable, but the "closing" position and the
  one-emoji budget are already enforced by pass-1 review; a gate would duplicate a judged
  rule for one emoji. Revisit if a third instance appears after applying.

## Regression expectation

Documentation-only change. `python .claude/skills/_shared/scripts/test_gates.py` and
`python meta/regression.py` unchanged green. Success criterion: zero
`fence-canon-verification-gap` findings in the next run's pass-1; the editor can decide the
emoji allowance without a SETI escalation in either round.
