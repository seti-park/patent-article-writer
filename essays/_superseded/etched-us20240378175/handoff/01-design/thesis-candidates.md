# Thesis Candidates

> Single-spine default applied (no multi-spine override keyword in the invocation).
> Edition: pending-application analysis — every claims anchor below is SOUGHT scope, and
> every candidate must be able to land the edition's required verdict: what this document
> IS to an investor today (asset-in-formation), never fence strength.

## Candidate 1: The origin document — the memory half, in writing, two years early

**Statement**: Etched's first-ever patent filing — May 2023, both co-founders as the
inventors — already puts the memory-side half of the company's no-middlemen architecture
in writing, claiming memory channels hardwired to array columns "without any switching
element"; three years on, that document is still an asset-in-formation: pending after a
final rejection, still being paid for, and already pledged with the rest of the stack as
venture-debt collateral.

**Framing**: origin-document reading — hold the July 2026 shipping-now narrative up
against the company's earliest filing and price what the filing actually is today.

**Evidence required**:
- Filing metadata (date, co-founder inventorship, first-filing status)
- Claim 39 family text (switchless hardwiring) + the spec's switch-is-typical contrast
- The thread's CSM pillar (company-claimed) as the narrative side of the friction
- Prosecution record (label sentence) + collateral facts (portfolio scope)

**Evidence available in invention-summary**:
- ✓ Metadata + timeline (filing 2023-05-10; Uberti + Zhu; earliest filing)
- ✓ Claims anchor (claim 39; `[0016]` q-0016-1; `[0043]`-`[0045]` q-0043-1/q-0044-1/q-0045-1)
- ✓ Problem anchor (`[0018]` q-0018-1, q-0018-2)
- ✓ Effect anchor (`[0045]` q-0045-2; `[0040]` q-0040-1; `[0057]` q-0057-1)
- ✓ External facts (fact-check-log: prosecution-record, tp-lien-1/2, etched-thread-2026-07, prior-essay-wiring-half)

**Structural tension**: the company sells finished racks and a memory philosophy in a July
2026 thread; the document where that philosophy was first written down is dated May 2023,
authored by both founders — and is still being argued with an examiner. Roadmap on paper
vs product on stage.

**Risks**:
- The rejection record can drag the verdict toward safe-harbor hedging (guarded by
  closing_posture: firm and the one-anti-hype-guard budget).
- The collateral beat can drift into patent-specific over-reading (guarded by the
  portfolio-scope discipline in fact-check-log and the handoff traps).

**Grounding (4-axis — draft, locked in Step 4)**:
- Claims anchor: claim 39 (SOUGHT) — "a separate memory device comprising a plurality of
  channels, wherein each of the plurality of channels is hardwired to respective one or
  more columns in the systolic array without any switching element"; echoed for claims 7/8
  (HBMs hardwired) and framed by claim 1's combined-array package
- Problem anchor: `[0018]` "it is unreasonable to expect a single chip to interface with
  100s of GB of memory used to store parameters and intermediate computation values"
- Effect anchor: `[0045]` "which can save space and power" (switch deleted) + `[0040]`
  ">1 TB/s" + `[0057]` "98% or greater utilization"
- Baseline-difference anchor: industry practice per the spec itself — HBM behind a
  switch/crossbar (`[0043]`) — plus the external record: the company's granted trio
  contains the wiring half but NOT this memory half (prior-essay-wiring-half), and the
  thread's CSM pillar is company-claimed narrative, not granted scope (etched-thread-2026-07)

**Q7 hook pattern (draft, hard-gated in Step 5)**:
- corporate-narrative-friction
- anchor: Etched's July 2026 thread presents the no-memory-middlemen philosophy (CSM) as
  shipping-now technology ("racks ship summer 2026", "$1B+ contracts" — company-claimed)
  vs the origin document that first claimed the switchless-memory idea in May 2023 and is
  still a pending, once-finally-rejected application — the narrative is ahead of the
  property right

**Adversarial defense (draft, locked in Step 6)**:
- Strongest objection: the memory-half "echo" rests on claim scope this applicant has
  failed to obtain for three years in a crowded examiner-cited field — if claims narrow or
  die, the "philosophy in writing" is just a disclosure, and the asset framing collapses.
- Mitigation: the verdict already prices this — the essay values the document as a dated,
  authored roadmap plus a live prosecution bet, explicitly NOT as a fence; the label
  sentence carries the rejection record; the claim-39 specificity is presented as the
  likeliest survivor, as drafted.

---

## Candidate 2: One array from many chips — the impossibility read

**Statement**: The application's answer to "how can nine separate chips act as one giant
math engine without a coordinator?" is to delete coordination itself — identical tiles, a
fixed top-down/left-right dataflow, no runtime instructions, and memory hardwired to the
columns it feeds.

**Framing**: mechanism-first explainer — resolve the reader's disbelief, then note what it
implies about the company's bet.

**Evidence required**:
- Combined-array mechanism (one-logical-array, chip-to-chip connections)
- Preset-loop / no-runtime-instructions design
- Utilization + bandwidth numbers

**Evidence available in invention-summary**:
- ✓ Mechanism (`[0019]` q-0019-1; `[0028]` q-0028-1; `[0027]` q-0027-1)
- ✓ Problem (`[0003]`, `[0018]`)
- ✓ Effect (`[0057]` q-0057-1; `[0040]` q-0040-1)
- ✓ Baseline (single-chip 128×128 ceiling `[0018]`; switched HBM practice `[0043]`)

**Structural tension**: the reader's intuition says chips joined by links need software
coordination and pay latency for it; the filing's answer is an architecture with nothing
to coordinate.

**Risks**:
- Lands a mechanism explainer, not the edition's required investor verdict — the strongest
  external evidence in this run (liens, prosecution record, thread friction) would hang
  off the spine instead of carrying it.
- The impossibility question is partially answered by prior art the examiner has already
  cited (multi-node acceleration is a crowded field) — the hook's "surely impossible"
  premise is weaker than it looks.

**Grounding (4-axis — draft, locked in Step 4)**:
- Claims anchor: claim 1 (SOUGHT) — chip-to-chip connections forming "a larger, combined
  systolic array"; claim 26's grid-like arrangement
- Problem anchor: `[0003]` FLOPs limited by array size; `[0018]` 128×128 ceiling
- Effect anchor: `[0057]` 98%+ utilization; `[0028]` host sees one large array
- Baseline-difference anchor: single-chip 128×128 industry practice (`[0018]`) + switched
  memory access (`[0043]`); external side thin — the crowded examiner-cited field actually
  CUTS AGAINST the impossibility premise

**Q7 hook pattern (draft, hard-gated in Step 5)**:
- technical-impossibility
- anchor: reader's "many chips can't just act as one array — who coordinates them?" →
  resolved by `[0027]` preset loop + `[0028]` one-logical-array + `[0044]` hardwired memory

**Adversarial defense (draft, locked in Step 6)**:
- Strongest objection: the examiner-cited field shows multi-chip/multi-node ML
  acceleration is established practice, so the "impossible" framing overstates novelty.
- Mitigation: would require reframing the hook from "impossible" to "done differently" —
  which dissolves the hook itself.

**Rejection reason**: Q7 anchor is structurally weak — the impossibility premise is
contradicted by the crowded examiner-cited field this run must itself report (the steelman
would eat the hook). And the frame cannot land the edition's required verdict (document-
as-asset): the load-bearing external facts would dangle. The mechanism material survives
as the middle sections (§one-big-array, §division-of-labor) of Candidate 1's essay.

---

## Candidate 3: The collateral story — patents as the bankable asset

**Statement**: The most concrete financial fact about Etched's patents today is not who
they exclude but what they secure — the whole stack, this pending application included,
has been pledged twice to the same venture lender.

**Framing**: money-first read — start from the reel/frame records and work back to the
documents.

**Evidence required**:
- Both TriplePoint liens with reel/frame cites
- Grant-vs-lien timing
- Portfolio composition (incl. rejected applications)

**Evidence available in invention-summary**:
- ✗ Claims anchor — the thesis does not rest on any claim text of THIS application
- ✓ External facts (fact-check-log: tp-lien-1-2024, tp-lien-2-2025, grant-lien-timing)
- ✗ Effect anchor — no invention effect carries the thesis

**Structural tension**: "$800m raised" and "$1B+ contracts" on stage; a blanket security
interest over every patent asset in the registry.

**Risks**:
- Violates the run's hard collateral discipline if the lien is read as patent-specific
  signal about this application (the pledged pool contains two rejected applications).
- 4-axis failure: claims and effect axes cannot be anchored — the patent becomes a prop.

**Grounding (4-axis — draft, locked in Step 4)**:
- Claims anchor: ✗ absent (thesis is about the portfolio, not claim content)
- Problem anchor: ✗ absent from the specification (the "problem" is financial, not the
  spec's)
- Effect anchor: ✗ absent
- Baseline-difference anchor: ✓ venture-debt norms vs the double lien (external only)

**Q7 hook pattern (draft, hard-gated in Step 5)**:
- corporate-narrative-friction
- anchor: "$800m raised" narrative vs the whole IP stack pledged as loan collateral

**Adversarial defense (draft, locked in Step 6)**:
- Strongest objection: blanket IP liens are ROUTINE in venture debt — reading signal into
  a standard security package is over-reading by construction.
- Mitigation: none available that preserves the thesis — the discipline note in
  essay-context makes exactly this objection.

**Rejection reason**: fails 4-axis grounding (Rule 1 — claims, problem, and effect axes
all unanchored: 1/4). It also collides head-on with the run's portfolio-scope discipline:
the liens carry zero patent-specific selectivity, so a spine built on them over-reads by
construction. Demoted to ONE paragraph — the investor beat inside Candidate 1's
asset-status section, in the honest both-directions frame (bankable asset class /
creditor's reach).

---

## Comparison

| Dimension | Candidate 1 | Candidate 2 | Candidate 3 |
|-----------|-------------|-------------|-------------|
| Evidence completeness | Full | Full (patent side) / thin (external) | External only |
| Audience appeal | High (origin story + money stakes) | Medium (explainer) | Medium (money angle, but over-read risk) |
| Architectural depth | High | High | Low |
| Defensive strength | High (steelman priced into the verdict) | Low (steelman eats the hook) | Low (discipline note IS the objection) |
| 4-axis grounding | 4/4 | 4/4 (Axis 4 external side weak) | 1/4 (no claims, no problem, no effect) |
| Q7 hook | corporate-narrative-friction | technical-impossibility (premise undercut by examiner field) | corporate-narrative-friction |
| Lands the edition's verdict (document-as-asset) | Yes | No | No (and breaches collateral discipline as spine) |

## Recommendation

Candidate 1 — the only candidate that is fully grounded on all four axes AND lands the
edition's required verdict (what the origin document is worth as an asset today); its Q7
friction is specific and datable (May 2023 filing + 2026-05 prosecution record vs July
2026 thread), and its steelman survives without eating the hook.

## SETI selection

- **Decision**: Select Candidate 1 (auto-selected per single-spine default and the
  orchestrator's auto-select-and-surface instruction; this list is surfaced for human
  override).
- **Notes**: Candidate 2's mechanism material is carried into Candidate 1's middle
  sections; Candidate 3 is demoted to the single collateral paragraph in the asset-status
  section under the portfolio-scope discipline. Proceed to spine lock (Step 8).
