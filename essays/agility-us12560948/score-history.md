# Score history — US 12,560,948 B2 investor moat article (formal pipeline)

Compose↔Edit inner loop. Threshold `pass`, posture `measured` + investor firm-closing guard,
max 4 iterations.

| Iter | Deterministic gates | Editorial assessment | Round result | Note |
|---|---|---|---|---|
| 1 | PASS (0 fail, 0 warn) | pass | **PASS** | clean on round 1; loop terminates |

Terminated at iteration 1 (cap 4), result PASS.

## Hard-gate checks
- Grounding hard-gate (goal 1): clear. No pass-3 high/critical; `gate_anchors` PASS.
- Goal-2 hard-gate: clear. No `FIGUSE-001`; figures 1/3/6 used; core-mechanism coverage present.

## Contrast with the prior ad-hoc run
The earlier non-pipeline article on this patent needed three review rounds: two for 8-sentence
paragraphs (one a regression introduced by a fix), and a third SETI catch for an over-hedged
conclusion. This formal run cleared in one round because the same defects were prevented upstream:
- Phase 1 `thesis-spine.md` pinned a firm-closing posture (overriding the default
  Acknowledged-risk mapping) and a claim-scope map (locked/open/pinned).
- Phase 2 drafted to the 3-7 sentence paragraph band and the firm verdict from the first draft.

The loop's value here was confirmation, not repair. The cost moved from the loop (expensive,
late) to the design hand-off (cheap, early), which is the intended division.
