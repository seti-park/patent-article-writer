# Thesis Spine

## Selected thesis

**One-line spine**:
> Etched's "Tensor parallel group" patent substantiates the interconnect half of its
> Cluster-Scale Memory story - a switchless topology in which every chip reaches every
> other chip through at most one intermediate chip - and conspicuously not the memory-pool
> half.

The essay's verdict is two-sided and firm: the "proprietary ultra-low-latency
interconnect" leg of CSM has granted, checkable substance in claims 1/8/9/11/14/18; the
"shared low-latency memory pool" leg (and everything LVI) has none in this filing, and the
essay says both plainly.

## 4-axis grounding

### Axis 1 — Claims anchor
> Claim 1 - "a plurality of communication channels to directly communicatively couple
> every processing device in the first set of the plurality of processing devices with
> every processing device in the second set of the plurality of processing devices without
> communicatively coupling any of the plurality of processing devices in the same set of
> the plurality of processing devices" (q-0386-1, verbatim in claim 1) and the wherein
> clause "through at most one other of the plurality of processing devices" (q-0387-1,
> verbatim in claim 1). Reinforced by claims 8/9/11 (two channel subsets with exclusive
> sub-operation traffic, overlapping-time execution, reduction + gather) and by
> independents 14 (system of groups) and 18 (four-group dual-channel-family wiring).
> Scope discipline per invention-summary.md §Claim scope map (claims 1/14: four or more
> per set; claim 18: two or more per set with the group structure).

### Axis 2 — Problem anchor
> `[0026]` "In some circumstances, a data switch that allows sharing of data amongst
> different processing device may be expensive to include in a system that performs
> tensor operations." Secondary: `[0313]` feedforward computations at four times model
> depth inflate processing time or required bandwidth.

### Axis 3 — Effect anchor
> `[0124]` "the fixed topology ... may be used to reduce data sharing between the
> processing devices A0-A7 and thereby help to reduce a processing time for the tensor
> operations performed by a tensor parallel group 700 ." Supporting: `[0130]` fewer
> connections vs a point-to-point scheme (q-0130-2); `[0168]` same amount of data per
> device and per channel; `[0250]` reduced processing time or bandwidth for AI models.

### Axis 4 — Baseline-difference anchor
> Two-level baseline, both documented:
> (a) Engineering baseline (patent-internal, the only verifiable one in this
> environment - search-log L2): any-to-any sharing via a networking/data switch
> (`[0032]`, `[0026]`) or a full point-to-point mesh (`[0130]`) vs the claimed bipartite
> fixed topology - switchless, degree-uniform, at most one intermediate device, 16
> channels vs 28 full-mesh on 8 devices (derived figure, flagged as derived).
> (b) Narrative baseline: Etched's stealth-exit CSM claims (fact-check-log
> `etched-csm-thread-2026-07`, official company statement, content company-claimed) vs
> what the granted claims lock (topology only; no memory, latency, or HBM/SRAM
> limitation) - the friction the essay adjudicates.

## Q7 hook pattern (hard gate)

- [x] `corporate-narrative-friction` - anchor: Etched stealth-exit thread (2026-07):
  "shared low-latency memory pool across the entire scale-up domain" over a "proprietary
  ultra-low-latency, high-bandwidth interconnect" vs US 12,361,091 B1 (granted
  2025-07-15): the claims lock a switchless bipartite chip topology and contain no
  memory-pool, latency, or HBM/SRAM limitation. The friction is binary and checkable at
  the claim level: the interconnect leg has granted substance; the memory leg does not,
  in this filing. (Narrative event: specific, dated company statement. Friction:
  claim-text presence/absence, verifiable against the document.)
- [ ] `technical-impossibility` (held as a secondary in-body hook: "any-to-any needs a
  switch or a wire per pair - this has neither" - resolved in section 3; not the entry
  point.)

## Adversarial defense

**Strongest objection**: Claim 1 recites a wiring pattern - two sets of four-plus chips,
every cross-set pair directly linked - that the description itself says can run over
ordinary PCIe, SPI, ethernet, or UCIe links `[0134]`, with no latency figure, no
bandwidth magnitude, and no memory limitation anywhere in the granted claims. A
topology-only claim over standard link technologies is a thin moat for a "proprietary
ultra-low-latency interconnect", so the thesis's claim that the patent "substantiates"
even the interconnect leg of CSM overstates what was granted. (Category 1 claim-scope
attack on THIS patent's claim text; sharpened by Category 3: the patent's stated win is
fewer connections and reduced data sharing `[0130]`, `[0124]` - a cost/bandwidth story -
while the thread's adjective is latency.)

**Mitigation**: The essay's verdict is split-level and states its own boundary as part of
the call. Section 3 credits the patent only with what the claims lock: switch removal
with reachability preserved (at most one intermediate device, q-0387-1), degree- and
bandwidth-uniform channels (claims 3-5), and - the part that is not textbook graph
shape - the operation binding of claims 8/9/11/18/23, where reduce and gather traffic get
disjoint channel families that run simultaneously. Section 6 then concedes the objection
at full strength (standard links, no latency number, description-level AI tie) and
refines: structure is what a granted apparatus claim CAN lock, the latency adjective was
never claimable as such, and the checkable fence the company now owns is exactly the
wiring discipline its CSM math needs (`[0060]`-`[0061]` bandwidth-minimization, `[0168]`
balanced channels). The essay never credits latency numbers, the memory pool, HBM/SRAM,
or LVI to this filing.

**Residual risk**: Acknowledged - the claims are silent on link technology and latency
figures, and whether Etched's shipped racks embody claim 1's topology is not knowable
from the filing. Consumed once in the limits/boundary section (section 6), and mapped
under the firm posture to a closing-binary-test: the company says first racks ship summer
2026 (company-claimed, fact `etched-lvi-biz-thread-2026-07`); rack-level disclosures or
teardowns will show whether the scale-up domain is a switch fabric or the claimed
direct-wired bipartite pattern.

**Steelman beat**: Section 6 opens by conceding, at full strength, that what was granted
is a wiring diagram implementable over ordinary links - no latency number, no memory
claim, standard buses named in the spec `[0134]` - and that the memory half of CSM plus
all of LVI have no substance in this filing. It then refines: apparatus claims lock
structure, and this structure (cross-set-only direct wiring + at-most-one-intermediate
reachability + segregated simultaneous collectives) is the non-generic, inference-shaped
part of the interconnect story, now fenced through 2044 and extended internationally.
Generic "patents don't guarantee products" framing is banned as the steelman; the
concession is claim-text-specific. (Carried into phase2-handoff-notes §d as a
concede-then-refine instruction.)

## Closing posture

closing_posture: firm

Verdict edition default (essay-context.md mandates it). Lead the closing with the call:
the interconnect leg of CSM is substantiated by this grant; the memory leg is not, and
LVI is untouched by it. Exactly one patent-specific anti-hype guard (the LVI/HBM-SRAM
absence, with the 18-month unpublished-filings window noted once). The Acknowledged
residual maps to closing-binary-test (racks ship summer 2026 → topology becomes
inspectable), never to an open-question close.

## Single-spine declaration

- [x] Single-spine (default)
- [ ] Multi-spine (override - record SETI authorization)

## Spine → section trace

| Section | Spine element carried | Primary anchors |
|---|---|---|
| 1-lead | Q7 hook: thread's CSM claims vs what the 2025 grant actually locks (friction, verdict promised) | fact `etched-csm-thread-2026-07` (framing; no patent quote spent here) |
| 2-grant | What this document is: structure patent of the same-day trio (903 method / 091 wiring / 262 umbrella), sole inventor, 266-day exam, PCT + continuation commitment signal | metadata; fact `etched-family-trio-wips`; Examples-family mapping (invention-summary §Prior-art) |
| 3-wiring | Axis 1 + Axis 2: claim 1's structure via FIGS. 7A-7C; two sets, cross-set-only channels, at most one intermediate device; switch and full-mesh foils; secondary technical-impossibility resolution | `[0386]`, `[0387]`, `[0126]`, `[0128]`, `[0129]`, `[0130]`, `[0026]`, `[0032]` |
| 4-traffic | Claims 8/9/11/18: two channel families, exclusive sub-operation traffic, reduce + gather simultaneously; balanced links; the p=4/q=2 math | `[0140]`, `[0142]`, `[0168]`, `[0061]`, `[0135]`-`[0139]` |
| 5-workload | Axis 3 payoff: what the wiring is shaped for - transformer decoding, MLP at 4x depth, the never-gather-a-tensor invariant (the honest kernel of "the pool is the cluster") | `[0251]`, `[0258]`, `[0313]`, `[0278]`, `[0267]`, `[0121]` |
| 6-boundary | Steelman beat (concede-then-refine) + the memory-leg absence: memory 630 described-never-claimed; standard links `[0134]`; LVI/HBM-SRAM not in this filing (single anti-hype guard); claim-scope map discipline | `[0119]`, `[0134]`, `[0133]`, Claim scope map; fact `etched-lvi-biz-thread-2026-07` |
| 7-verdict | Firm two-sided call + closing-binary-test falsifier (summer 2026 racks) | (framing; recap anchors only) |

<!--
  Feedback-loop note: none required - Step 9 figure mapping confirmed the section trace
  (FIGS. 7A/7B/7C as one unit in sections 3-4; FIG. 6 carries section 6's memory-boundary
  beat) without forcing a spine revision.
-->
