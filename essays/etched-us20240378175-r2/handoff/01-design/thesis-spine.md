# Thesis Spine

## Selected thesis

**One-line spine**:
> Etched's very first patent filing put the no-switch memory half of its architecture in claim language in May 2023, two years before the company pitched it in its stealth-exit thread; three years of examination later it is still a bet the company keeps paying to convert into an asset, not the asset itself.

*Erratum (self-audit round 1, origin: sa1B-F1): "pitched it on stage" corrected in place to "pitched it in its stealth-exit thread" — no stage/keynote event exists in the run's fact base; the pitch venue on record is the stealth-exit thread (fact `thread-claims-2026-07`, TechCrunch coverage dated 30 June 2026).*

*Erratum (self-audit round 2, origin: sa2B-F2): three "both co-founders" spans (Q7 hook, Mitigation, §2 trace row) corrected in place to count-safe "co-founders Uberti and Zhu" — the run's fact base (patent front-matter; essay-context "both co-founders (Uberti, Zhu) are the inventors") establishes that the two inventors ARE co-founders, never that the company has exactly two founders; "both" invited the exhaustive-count reading. Root phrasing lives in input/essay-context.md (user-owned, not edited) — meta-loop item.*

Edition contract (controlling): PENDING APPLICATION. All claim content is SOUGHT, not
locked; application-era language only ("the application claims / Etched is seeking / as
drafted"). The verdict is about what the document IS (origin filing, memory-half philosophy
in writing, asset-in-formation) — never about fence strength, never enforceability.

## 4-axis grounding

### Axis 1 — Claims anchor
> Claim 39 (sought, independent) — "a separate memory device comprising a plurality of channels, wherein each of the plurality of channels is hardwired to respective one or more columns in the systolic array without any switching element" — reinforced by claims 7/19/32 (HBMs "hardwired to respective columns in the local systolic arrays without any switching element", sought) and claim 15 (memory chips storing weights "coupled to the plurality of ICs forming a top row", sought). Description twin for [xxxx]-anchored citation: `[0016]` (q-0016-1). Claim 39 notably does NOT require multi-chip: the memory idea is claimed as a stand-alone invention.

### Axis 2 — Problem anchor
> `[0018]` "One of which, notably, is that it is unreasonable to expect a single chip to interface with 100s of GB of memory used to store parameters and intermediate computation values." + `[0043]` "a switch (or some kind of switching element such as a crossbar) is typically used so that the device can access the entire memory of the HBM"

### Axis 3 — Effect anchor
> `[0045]` "This avoids having to add a switching element between the local systolic array 220and the memory chips 505, which can save space and power." (run-on "220and" is the source's own text) + `[0039]` adding rows of ICs adds compute without adding memory chips (weights reused down the rows)

### Axis 4 — Baseline-difference anchor
> Corporate narrative baseline: Etched's July 2026 stealth-exit thread presents the no-layer memory philosophy (CSM pillar) as shipping-hardware fact, with "$1B+ contracts" / "$800m raised" / racks shipping summer 2026 — all company-claimed (fact `thread-claims-2026-07`); the published wiring-half analysis found the memory half absent from the GRANTED record (fact `wiring-half-essay`). Registry difference: the same philosophy has been in claim language since 2023-05-10 and is still SOUGHT (final rejection 2025-10-23; RCE 2026-04-24 — fact `prosecution-record`). Industry-practice difference: conventional accelerators keep a switching layer between HBM and compute (`[0043]`, in-document) and live in the ~128×128-per-chip array world (`[0018]`; external instance: TPU MXU, fact `tpu-mxu-128x128`).

## Q7 hook pattern (hard gate)

- [x] `corporate-narrative-friction` — anchor: July 2026 thread (CSM "no memory layer" pillar sold as shipping hardware; $1B+ contracts, racks this summer — company-claimed) vs the USPTO record (the same idea claim-drafted 2023-05-10 by co-founders Uberti and Zhu, final-rejected 2025-10-23, kept alive by a paid RCE, still sought as of 2026-05). The friction is binary and checkable: the philosophy ships on stage while its ownership is still being argued.
- [ ] `technical-impossibility`

## Adversarial defense

**Strongest objection**: Authorship without ownership. The examiner has already assembled 8
references against this application (multi-node ML acceleration, hybrid parallelism, NN
accelerator architectures — Intel, IBM, Rambus, ETRI among the assignees) and issued a final
rejection. The breadth that makes the filing quotable is exactly what makes it shrinkable:
claim 1 reads on any multi-chip systolic-array package, and claim 39's no-switch hardwiring
may yet be found routine for weight-stationary designs. So "the memory half was in writing
by May 2023" proves the founders wrote it down early — it does not prove Etched will ever
own it, and an essay that trades on the claim language is trading on the part of the record
most likely to change.

**Mitigation**: The essay makes the objection load-bearing instead of rebutting it. §5
states it at full strength (crowded examiner-cited field; final rejection already taken;
claim 1's breadth the most likely casualty), then refines with what the record proves
regardless of outcome: dated, signed authorship of the memory-half architecture (2023-05-10,
co-founders Uberti and Zhu); a stand-alone independent claim (39), not a buried embodiment — the
company paid to claim the memory idea as its own invention; and a twice-made spending
decision to keep it alive (prosecution through final rejection, then an RCE). The verdict
prices the document as an asset-in-formation on exactly this two-sided record.

**Residual risk**: Acceptance — falsifiable by prosecution outcome: if the memory-side
claims (39-42, 7/19/32) grant materially intact, the memory half becomes an owned asset;
if they die or narrow to ornament, the filing stays a dated roadmap. The closing maps this
to a binary test / forward watching event (next office-action response on the record),
per firm-posture rules — never an open question.

**Steelman beat**: §5 concedes the objection at full strength (the examiner may be right
that this is a crowded field's routine idea; the breadth is the shrinkable part), then
refines with the authorship + independent-claim-status + continued-spend record. The generic
"patents don't guarantee products/stock prices" truism is banned as the steelman; the limits
section may spend ONE sentence on category limits, no more.

## Closing posture

closing_posture: firm  # verdict edition default + explicit essay-context directive; carried into the draft frontmatter for gate_hedge

Firm does not mean bullish. The call shape (from the brief, on this evidence): origin
document + memory-half philosophy in writing + the company still paying to push it (RCE
after final rejection) + the whole stack banked as collateral, VERSUS not yet an asset
(pending, rejected once, claims can shrink). The call leads; it is not qualifier-wrapped.
Exactly ONE patent-specific anti-hype guard (recommended: the shipping product is not
evidence the claims will grant — the examiner-cited field is where that gets decided).
Residual `Acceptance` maps to closing-binary-test / closing-forward-watching-event.

## Single-spine declaration

- [x] Single-spine (default)
- [ ] Multi-spine (override — record SETI authorization)

## Spine → section trace

| Section | Spine element carried | Primary anchors |
|---|---|---|
| 1-lead | Q7 hook + discovery beat (register per title-lead-candidates.md); full two-sided call lands by end of lead | `[0016]` (claim-39 twin); facts: thread-claims-2026-07, prosecution-record (label sentence) |
| 2-origin-array | What the filing is: one combined array from many identical chips; host sees one array; splittable; origin facts (first filing, co-founders Uberti and Zhu); one clause of wiring-half continuity | `[0013]`, `[0018]`, `[0019]`, `[0024]`, `[0028]`, `[0038]`; FIG. 1 + FIG. 2 |
| 3-memory-half | Axis 1/2/3: the no-switch memory claims; FIG. 5 walk; weights-from-top; add-rows-without-memory; the CSM echo (two years earlier, company-claimed attribution) | `[0016]`, `[0043]`, `[0044]`, `[0045]`, `[0035]`, `[0039]`, `[0040]`; FIG. 5 + FIG. 3 |
| 4-division-of-labor | Supporting mechanism: preset loop, auxiliary circuitry + private memory (claims 11-13, sought), FIG. 7 pipelining (description-only status flagged) | `[0027]`, `[0047]`, `[0048]`, `[0051]`, `[0053]`, `[0055]`, `[0056]`, `[0057]`; FIG. 6 + FIG. 7 |
| 5-asset | Axis 4 + adversarial mitigation: what the document is worth today — prosecution label sentence (the ONE), collateral facts (portfolio scope, reel/frames, both-or-neither), US-only family observation, steelman beat | facts: lien-1, lien-2, grant-lien-timing, prosecution-record, examiner-art-8refs, family-us-only |
| 6-closing | Firm verdict: asset-in-formation call + ONE anti-hype guard + binary test (prosecution outcome on the memory-side claims) | (framing; recap anchors only) |

<!--
  > Revision note — none. Step 9 figure mapping confirmed the spine's figure dependencies
  (FIG. 5 cover; FIG. 4 dropped as unselected variant) without changing spine content.
-->
