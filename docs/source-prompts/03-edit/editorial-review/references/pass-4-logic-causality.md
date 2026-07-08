# Pass 4 — Logical alignment + causality

Combines thesis-section alignment check (v1 partial Pass 5) with the causal-reasoning framework (already an editorial-review reference in v1).

## Two sub-passes

### 4A — Thesis-section 정렬

Cross-check `handoff/02-compose/thesis-trace.md` against the actual draft:

1. For each spine element in `handoff/01-design/thesis-spine.md`, locate the section(s) that carry it.
2. Verify the section's prose actually advances that element (not just mentions it).
3. Verify no section advances a claim outside the spine.

Common failures:

| Failure | Description | Severity |
|---|---|---|
| Spine element absent from any section | Supporting point 2 was supposed to land in §3 but the section drifted to a different claim | high |
| Section advances out-of-spine claim | §4 introduces a new mechanism not in the spine | high (Plan ⊥ Execute violation) |
| Spine element under-evidenced | Section mentions the point but doesn't anchor it with `[XXXX]` or external fact | medium |
| Section header misnames | §3 title says "Architecture" but content is "Implication" | low |

### 4B — Causal claim quality

For every causal claim in the draft, apply the `references/causal-reasoning.md` framework:

**인과 (causation)** — X → Y; mechanism explained; counterfactual ("if not X, not Y") holds.

**상관 (correlation)** — X and Y co-occur; no mechanism explained; counterfactual untested.

**우연 (coincidence)** — X and Y co-occur once; no mechanism; no pattern.

Common drifts:

| Drift | Description | Severity |
|---|---|---|
| Correlation → causation | "Tesla filed the patent, then the cell line launched, so the patent caused the line" — missing mechanism | high |
| Coincidence → correlation | "Both Tesla and SpaceX filed similar patents in Q1" — sample size of 1 | medium |
| Causation buried | The mechanism IS in the source but the prose only states the correlation | medium (rewrite) |
| Causation overstated | "X drives Y entirely" when source supports "X contributes to Y" | high |

### 4C — Thesis arc coherence

Read the draft front-to-back as a reader. The arc should:

1. Set up the thesis tension in the lead.
2. Anchor the tension in patent evidence (mechanism section).
3. Show the implication (implication section).
4. Land the thesis with closing posture (forward_pointer / wider_framing / thesis_recap).

Coherence failures:

- Lead's tension never resolved by closing.
- Mechanism section makes claims the lead didn't set up (reader surprised).
- Implication is generic (could apply to any patent — not this thesis-specific).
- Closing landing doesn't match the spine's adversarial defense residual_risk posture.

## Severity calibration per posture

| Sub-check | aggressive | measured | conservative |
|---|---|---|---|
| 4A spine element absent | high | high | high |
| 4A out-of-spine claim | high | high | critical |
| 4A under-evidenced | medium | medium | high |
| 4B correlation → causation | high | high | critical |
| 4B causation overstated | high | high | high |
| 4C lead tension unresolved | high | high | high |
| 4C generic implication | medium | medium | high |

## Output finding template

```yaml
- pass: pass-4-logic-causality
  location: §3, paragraph 1
  severity: high
  severity_under_default_posture: high
  finding: |
    Sentence "Tesla's patent filing 11 months before the announcement caused
    the public framing" asserts causation from temporal sequence alone.
    invention-summary.md doesn't support a causal mechanism; the timing is
    correlation only.
  recommendation: |
    Reframe as: "Tesla's filing predates the announcement by 11 months, which
    suggests the public framing was constructed retroactively." Avoid "caused".
```

## Cross-pass interactions

- Pass 4A failures often share location with Pass 2 redundancy (out-of-spine claim is also typically restated 2-3 times to feel grounded).
- Pass 4B failures cross-reference Pass 3 (a paraphrase mutation can simultaneously be a causation drift).
- Pass 4C closing failure often correlates with Pass 6 closing posture mismatch.
