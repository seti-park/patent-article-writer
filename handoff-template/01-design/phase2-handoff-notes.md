<!--
  TEMPLATE: handoff/01-design/phase2-handoff-notes.md
  Produced by: thesis-architect (Phase 1 Design, Step 11 — Phase 2 handoff notes)
  Schema source: thesis-architect/SKILL.md Step 11

  Phase 2 entry instructions. Captures:
    (a) audience reframe decision (if any)
    (b) citation priority mapping (which Quotable span → which essay section first)
    (c) framing trace (core reasons rejected candidates were rejected)
    (d) traps Phase 2 must avoid
    (e) open questions for Phase 2 (items awaiting a SETI decision)

  Example content: Tesla RCM / 70ms patent.
-->

# Phase 2 Handoff Notes

## (a) Audience reframe decision

<!-- Any decision about who the essay addresses and at what assumed-knowledge level.
     "None" is a valid answer. -->
Audience held at the default: technically literate generalist who follows the EV /
autonomy beat but is not an airbag-systems engineer. No reframe. The optical-vs-
electrical intuition (technical-impossibility) is available as a secondary hook but
the locked spine leads with corporate-narrative-friction.

## (b) Citation priority mapping

<!-- Which invention-summary Quotable span is used FIRST in which section. Helps
     Phase 2 avoid spending a strong anchor in the wrong place. -->
| Quotable span | Primary section | Role |
|---|---|---|
| `[0016]` (vision-path claim) | 2-architecture | claim anchor, used first |
| `[0017]` (predictive input) | 2-architecture | mechanism support |
| `[0014]` (accelerometer responds after) | 3-baseline | problem framing |
| `[0024]` (~70ms lead) | 3-baseline, then 4-implication | quantitative payoff — reserve for the baseline comparison, do not spend in the lead |
| `[0029]` (<0.1% false-positive) | 4-implication | bounds the claim |

## (c) Framing trace (rejected candidates)

<!-- One line per rejected candidate from thesis-candidates.md: the core reason,
     so Phase 2 does not accidentally drift back into a rejected frame. -->
- Candidate 2 ("optical beats electrical") rejected: Axis 4 only 3/4 anchored and it
  risks conflating prediction lead time with raw sensor latency. Phase 2 must NOT
  reframe the essay around sensor-latency comparison.

## (d) Traps to avoid

<!-- Concrete things Phase 2 must not do — paraphrase risks, apples-to-oranges
     comparisons, em-dash temptations, frames that reopen rejected candidates. -->
- Do not present the ~70ms figure as a sensor-latency number — it is a deployment-
  decision lead time. Keep the Bosch ~10ms vs ~70ms comparison apples-to-apples
  (both are pre-deployment-decision latencies).
- Do not spend `[0024]` in the lead; the announcement-vs-filing friction carries §1.
- Em-dash is banned in essay body (deliverable voice); patent verbatim quotes keep
  their em-dashes.

## (e) Open questions for Phase 2 (awaiting SETI)

<!-- Items the composer should confirm before/while drafting. Empty list is valid. -->
- Title pattern: spine fits both Pattern 3 (multi-clause reversal) and Pattern 1
  (declarative reversal). SETI to pick at compose time.
- Whether to surface the secondary technical-impossibility hook inside §2 or leave
  it implicit. Default: leave implicit.
