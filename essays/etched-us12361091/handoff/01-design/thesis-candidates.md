# Thesis Candidates

Single-spine default (no multi-spine override keyword in the invocation). All candidates
answer, or fail to answer, the question `input/essay-context.md` mandates: does this
granted patent substantiate a real, defensible piece of Etched's "Cluster-Scale Memory"
(CSM) claim? Land a clear verdict.

## Candidate 1: The wiring is the granted half

**Statement**: Etched's "Tensor parallel group" patent substantiates the interconnect half
of its Cluster-Scale Memory story - a switchless topology in which every chip reaches
every other chip through at most one intermediate chip - and conspicuously not the
memory-pool half.

**Framing**: verdict-first claims audit - hold the stealth-exit thread's CSM claim up
against what the granted claims actually lock, and split the story where the claims split
it.

**Evidence required**:
- The thread's CSM claims (interconnect + memory pool), attributable
- Granted claim text locking the topology (cross-set all-to-all, no in-set links, at most
  one intermediate device, channel-family traffic segregation)
- Absence evidence: no memory/latency/HBM-SRAM limitation anywhere in the claims
- Family context (trio division of labor) for the "structure patent" identity

**Evidence available in invention-summary**:
- ✓ Claim text (q-0386-1, q-0387-1 verbatim = claim 1 limitations; Claim scope map rows 1,
  8, 9, 11, 14, 18)
- ✓ Problem/effect spans (`[0026]`, `[0124]`, `[0130]`, `[0168]`)
- ✓ Absence evidence (Claim scope map "Leaves open" column; memory 630 described `[0119]`,
  never claimed; Examples-family mapping)
- ✓ Thread claims + family facts (fact-check-log `etched-csm-thread-2026-07`,
  `etched-family-trio-wips`)

**Structural tension**: the thread sells a memory story; the granted patent that exists is
a wiring story. The essay walks the reader from the claim they heard (CSM) to the claim
that was granted (topology), and lands the verdict that the two overlap on exactly one
leg.

**Risks**:
- Reader may hear "the memory half is unclaimed" as "the company lied" - the essay must
  hold the measured line: unpublished filings may exist (18-month window), and the
  interconnect leg is genuinely substantiated.
- The claim-scope thinness objection (see defense) must be conceded at full strength or an
  informed reader dismisses the verdict as patent-counting.

**Grounding (4-axis - draft, locked in Step 4)**:
- Claims anchor: claim 1 - "directly communicatively couple every processing device in the
  first set ... with every processing device in the second set ... without communicatively
  coupling any of the plurality of processing devices in the same set" + wherein clause
  "through at most one other of the plurality of processing devices" (q-0386-1, q-0387-1);
  reinforced by claims 8/9/11 (channel-family segregation, simultaneity, reduce/gather)
  and 14/18.
- Problem anchor: `[0026]` "a data switch that allows sharing of data amongst different
  processing device may be expensive to include in a system that performs tensor
  operations" (+ `[0313]` feedforward bandwidth pressure).
- Effect anchor: `[0124]` "reduce data sharing between the processing devices A0-A7 and
  thereby help to reduce a processing time"; `[0130]` fewer connections vs point-to-point;
  `[0168]` same amount of data per device and per channel.
- Baseline-difference anchor: two-level. Engineering baseline = the patent's own named
  alternatives (any-to-any networking/data switch `[0032]`/`[0026]`; full point-to-point
  mesh `[0130]`) vs the claimed bipartite fixed topology. Narrative baseline = Etched's
  CSM thread claims (fact `etched-csm-thread-2026-07`, company-claimed) vs what the
  granted claims lock. No live external baseline available (search-log L2).

**Q7 hook pattern (draft, hard-gated in Step 5)**:
- corporate-narrative-friction
- anchor: Etched stealth-exit thread (2026-07): "shared low-latency memory pool across the
  entire scale-up domain" over a "proprietary ultra-low-latency, high-bandwidth
  interconnect" vs US 12,361,091 B1 (granted 2025-07-15): claims lock a switchless
  bipartite chip topology and contain no memory-pool, latency, or HBM/SRAM limitation.
  Friction is binary and checkable at the claim level: the interconnect leg has granted
  substance; the memory leg does not, in this filing.

**Adversarial defense (draft, locked in Step 6)**:
- Strongest objection (Category 1, THIS-patent): claim 1 recites a wiring pattern the
  description says can run over ordinary PCIe/SPI/ethernet/UCIe links `[0134]`, with no
  latency, bandwidth-magnitude, or memory limitation anywhere in the granted claims - a
  topology-only claim cannot "substantiate" an ultra-low-latency memory-pool story.
- Mitigation: the verdict is split-level and says so - the essay credits the patent only
  with the structural mechanism (switch removal, at-most-one-intermediate bound,
  degree/bandwidth-uniform channels, claims 8-11's segregated simultaneous collectives)
  and expressly refuses to credit latency figures, the memory pool, HBM/SRAM, or LVI to
  this filing. The concession IS half the verdict.

**Q7 status**: PASS (corporate-narrative-friction; specific event, binary friction).
**4-axis status**: 4/4 anchored.

---

## Candidate 2: No switch, no n-squared wires - the two-hop trick

**Statement**: Etched's patent answers a wiring paradox - how eight chips can each reach
any other in at most one intermediate hop without a switch and without wiring all 28
pairs - by splitting them into two sets of four and wiring only across the split.

**Framing**: mechanism-first explainer - lead with the reader's "that shouldn't work"
intuition, resolve it with the bipartite construction, then note what it's for.

**Evidence required**:
- The reachability guarantee and its claim anchor
- The link-count arithmetic (16 vs 28)
- The switch-cost and full-mesh alternatives as foils

**Evidence available in invention-summary**:
- ✓ Claims anchor (q-0387-1 at-most-one-other; q-0386-1 cross-set coupling)
- ✓ Problem anchor (`[0026]` switch cost)
- ✓ Effect anchor (`[0130]` fewer connections; `[0124]` processing time)
- ✓ Baseline (patent-internal: switch `[0032]`, full mesh `[0130]`)

**Structural tension**: intuition says any-to-any needs a switch or n-squared wires; the
patent's graph gives any-to-any at degree 4 with a two-hop worst case.

**Risks**:
- Does not answer the essay-context's mandated question (CSM substantiation verdict); a
  mechanism explainer with no verdict fails the deliverable.
- The "paradox" softens for readers who know graph theory (bipartite graphs are
  textbook) - hook durability depends on audience.

**Grounding (4-axis - draft)**: 4/4 anchorable (same anchors as Candidate 1, minus the
narrative baseline).

**Q7 hook pattern (draft)**:
- technical-impossibility
- anchor: reader's "any-to-any communication needs a switch or a wire per pair - how do
  you get it with neither?" → claim 1's two-set construction resolves it.

**Adversarial defense (draft)**:
- Strongest objection: a complete-bipartite arrangement is a known network shape; the
  interesting part is the operation binding (claims 8-11), which this framing buries.
- Mitigation: would need to promote the channel-family material into the spine - at which
  point the essay still owes the CSM verdict it never set up.

**Rejection reason**: Fails the deliverable, not the gates - it answers "how does the
wiring work" when the context brief mandates "does the patent substantiate CSM; land a
clear verdict." Folded into Candidate 1 as the section-3 mechanism beat and as the
secondary hook inside the body (the two-hop resolution is still the essay's best
explainer moment).

---

## Candidate 3: Three patents, one machine - the commitment signal

**Statement**: The same-day trio (903 = how tiles move, 091 = how chips are wired, 262 =
the model-level umbrella), each extended by PCT and a continuation, shows Etched
systematically fencing a scale-up architecture rather than filing a one-off.

**Framing**: portfolio read - the filing pattern as evidence of intent.

**Evidence required**:
- Family bibliographic facts (dates, PCTs, continuations)
- The division-of-labor mapping
- Claim-level identity of 091 within the trio

**Evidence available in invention-summary**:
- ✓ Family facts (fact-check-log `etched-family-trio-wips`, tier-2)
- ✓ Patent-internal corroboration (Examples 1/2/3 families vs granted claims)
- ✗ Claims anchor for the THESIS: the thesis's load-bearing mechanism is a filing
  strategy, not a claim limitation - no claim element carries "systematic fencing"

**Structural tension**: one stealth thread, three simultaneous fences.

**Risks**:
- Axis 1 is structurally weak (portfolio intent is not in any claim).
- The context brief reserves the sibling deep-dive for a possible part-2 and caps siblings
  at one context paragraph here.

**Q7 hook pattern (draft)**: nearest fit is a timing/portfolio anomaly - a pattern v2
DROPPED (timing-anomaly). Reframing as corporate-narrative-friction produces a weaker
anchor than Candidate 1's (the friction would be "thread vs filing pattern", which is
corroboration, not friction).

**Rejection reason**: Q7 hard-gate failure risk (maps naturally to the deprecated
timing-anomaly pattern) + Axis 1 weakness (no claim limitation carries the thesis) +
context-brief scope cap on siblings. Kept as one context paragraph in section 2 of the
selected spine (commitment-signal fact, tier-2).

---

## Candidate 4: Balanced by construction

**Statement**: The patent's topology makes the collective operations of transformer
inference balanced by wiring rather than by scheduling - reduce and gather each own a
channel family, run simultaneously, and every link carries the same bytes.

**Framing**: engineering-elegance read - the wiring encodes the workload.

**Evidence required**:
- Channel-family claims (8, 9, 11, 18, 23)
- Balanced-data spans (`[0168]`, `[0178]`, `[0231]`)
- Workload tie (`[0251]`, `[0258]`, `[0278]`)

**Evidence available in invention-summary**:
- ✓ Claims anchor (claims 8/9/11/18/23; q-0140-1/2, q-0142-1)
- ✓ Problem anchor (`[0313]` feedforward pressure)
- ✓ Effect anchor (`[0168]` balanced data)
- ✗ Baseline-difference: needs an external reference for how collectives are scheduled on
  conventional fabrics to make "by construction vs by scheduling" concrete -
  environment-limited (search-log L2); patent-internal foils alone leave the contrast
  implied rather than anchored.

**Structural tension**: everyone else load-balances in software; this wiring cannot be
unbalanced.

**Risks**:
- "Collective operations", "all-reduce" vocabulary sits above the reader profile without a
  full explainer section.
- 3/4 axes fully anchored; Axis 4 depends on unverifiable external practice claims.
- No verdict on CSM - same deliverable failure as Candidate 2.

**Q7 hook pattern (draft)**:
- technical-impossibility ("keeping every link equally busy is a hard scheduling problem -
  here it falls out of the wiring") - reasonable, but the reader must first learn what
  collective traffic is; hook accessibility medium.

**Rejection reason**: Axis 4 not fully anchorable in this environment (3/4) + hook
accessibility medium for the retail reader profile + does not carry the mandated verdict.
Material survives as the section-4 traffic beat of the selected spine.

---

## Comparison

| Dimension | Candidate 1 | Candidate 2 | Candidate 3 | Candidate 4 |
|-----------|-------------|-------------|-------------|-------------|
| Evidence completeness | Full | Full | Partial (Axis 1 weak) | Partial (Axis 4 gap) |
| Answers mandated question (CSM verdict) | Yes | No | Partially | No |
| Audience appeal | High (readers arrive from the thread) | High | Medium | Medium |
| Architectural depth | High | Medium | Low | High |
| Defensive strength | High (steelman is half the verdict) | Medium | Low | Medium |
| 4-axis grounding | 4/4 | 4/4 | 2/4 (claims weak, effect n/a for portfolio intent) | 3/4 (no external baseline) |
| Q7 hook | corporate-narrative-friction | technical-impossibility | (maps to deprecated timing-anomaly) | technical-impossibility (accessibility medium) |
| Hook accessibility | High | High | n/a | Medium |

## Recommendation

Candidate 1 - it is the only candidate that lands the verdict `input/essay-context.md`
mandates, its 4-axis grounding is full with the friction hook anchored on a specific,
checkable event (thread claims vs granted claim text), and its strongest objection folds
into the verdict instead of undermining it. Candidates 2 and 4 survive as its mechanism
and traffic beats.

## SETI selection

- **Decision**: Select Candidate 1 (auto-selected by the Phase 1 design worker per the
  single-spine default and the run's "auto-select, surface, don't block" rule; the
  orchestrator may override by re-invoking with a different selection).
- **Notes**: proceeded to spine lock (Step 8) with Candidate 1's grounding + hook +
  defense. Candidates 2 and 4 are intentionally folded in as body beats (sections 3 and
  4 of the spine trace); Candidate 3 survives only as the one-paragraph family-context
  fact.
