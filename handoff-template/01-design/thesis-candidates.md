<!--
  TEMPLATE: handoff/01-design/thesis-candidates.md
  Produced by: thesis-architect (Phase 1 Design, Step 3 — candidate generation)
  Schema source: thesis-architect/references/thesis-candidate-presentation.md

  2-4 candidates. Each carries a frame + draft 4-axis grounding (locked in Step 4)
  + draft Q7 hook (hard-gated in Step 5) + draft adversarial defense (Step 6).
  Rejected candidates MUST record a rejection reason. Example: Tesla RCM / 70ms.
-->

# Thesis Candidates

## Candidate 1: The architectural pre-commitment

**Statement**: Tesla's RCM patent reveals an architectural decision made months before the public announcement that retroactively explains the 70-millisecond claim.

**Framing**: investigative reframe — let the filing date reorder the public narrative.

**Evidence required**:
- Patent filing/publication timeline
- Vision-path claim language
- Quantified pre-impact lead time

**Evidence available in invention-summary**:
- ✓ Timeline (filing 2024-10-23, publication 2026-04-23)
- ✓ Claims anchor (`[0016]` vision-path)
- ✓ Quantitative effect (`[0024]` 70ms)

**Structural tension**: the public "70ms is unprecedented" announcement, then the patent that was already on file explaining how.

**Risks**:
- Reader may read the timeline as coincidence rather than pre-commitment.

**Grounding (4-axis — draft, locked in Step 4)**:
- Claims anchor: 청구항 1 (b) — "the vision sensor providing pre-impact prediction to the airbag controller"
- Problem anchor: `[0014]` "conventional accelerometer-based systems respond only after the collision has begun"
- Effect anchor: `[0024]` "approximately 70 milliseconds before traditional accelerometer-based systems"
- Baseline-difference anchor: Bosch ~10ms accelerometer vs ~70ms vision-path lead

**Q7 hook pattern (draft, hard-gated in Step 5)**:
- corporate-narrative-friction
- anchor: Tesla 公식 발표가 patent publication 보다 11개월 후 → narrative friction

**Adversarial defense (draft, locked in Step 6)**:
- Strongest objection: 70ms could be measured against a non-comparable baseline.
- Mitigation: §3 cites both baselines and shows apples-to-apples.

---

## Candidate 2: Optical beats electrical

**Statement**: Tesla's airbag controller commits to deployment from a photon-based prediction faster than any accelerometer can register the crash.

**Framing**: technical-impossibility reframe — answer the reader's "how can optical be faster than electrical?"

**Evidence required**:
- Vision-path mechanism
- Latency comparison

**Evidence available in invention-summary**:
- ✓ Mechanism (`[0017]` predictive input)
- ✓ Effect (`[0024]` 70ms)
- ✗ Independent external baseline for the optical-vs-electrical latency framing (needs more context research)

**Structural tension**: reader assumes electrical sensing is fastest; the patent inverts it via prediction-before-impact.

**Risks**:
- Conflates "prediction lead time" with "sensor latency" — could mislead a technical reader.

**Grounding (4-axis — draft, locked in Step 4)**:
- Claims anchor: 청구항 1 (b) vision-path limitation
- Problem anchor: `[0014]` accelerometer responds after collision begins
- Effect anchor: `[0024]` 70ms lead
- Baseline-difference anchor: ✗ baseline not yet externally anchored (3/4)

**Q7 hook pattern (draft, hard-gated in Step 5)**:
- technical-impossibility
- anchor: reader's "how can an optical input beat an electrical one?" is the entry point

**Adversarial defense (draft, locked in Step 6)**:
- Strongest objection: prediction lead time is not the same axis as raw sensor latency.
- Mitigation: would require an explicit definitional section.

**Rejection reason**: Axis 4 (baseline-difference) only 3/4 anchored — no external baseline for the optical-vs-electrical framing; risk of conflating prediction lead with sensor latency. Reframed into Candidate 1's apples-to-apples baseline treatment instead.

---

## Comparison

| Dimension | Candidate 1 | Candidate 2 |
|-----------|-------------|-------------|
| Evidence completeness | Full | Partial |
| Audience appeal | High | High |
| Architectural depth | High | Medium |
| Defensive strength | High | Medium |
| 4-axis grounding | 4/4 | 3/4 (no baseline) |
| Q7 hook | corporate-narrative-friction | technical-impossibility |
| Hook accessibility | High | High |

## Recommendation

<!-- Single line. SETI decides per references/thesis-candidate-presentation.md
     selection options (Select N / Combine / Revise / Reject all). -->
Candidate 1 — strongest 4-axis grounding (Bosch baseline well documented in context research) and the clearest hook (Tesla's announcement timing is specific and recent).

## SETI selection

- **Decision**: Select Candidate 1
- **Notes**: proceed to spine lock (Step 8) with Candidate 1's grounding + hook + defense.
