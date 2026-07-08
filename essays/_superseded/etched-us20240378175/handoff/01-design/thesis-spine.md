# Thesis Spine

> **Edition guard:** pending application. Every claims anchor below is SOUGHT scope —
> application-era language only ("the application claims", "as drafted", "Etched is
> seeking"). No enforceability language anywhere in the essay: nothing here can be
> infringed until (unless) it grants.

## Selected thesis

**One-line spine**:
> Etched's first-ever patent filing — May 2023, both co-founders as the inventors —
> already puts the memory-side half of the company's no-middlemen architecture in
> writing, claiming memory channels hardwired to array columns "without any switching
> element"; three years on it is still an asset-in-formation: pending after a final
> rejection, still being paid for, and already pledged with the rest of the stack as
> venture-debt collateral.

## 4-axis grounding

### Axis 1 — Claims anchor
> Claim 39 (SOUGHT, not locked) — "a separate memory device comprising a plurality of
> channels, wherein each of the plurality of channels is hardwired to respective one or
> more columns in the systolic array without any switching element" (mirrored verbatim in
> the citable summary paragraph `[0016]`, q-0016-1). Reinforced by claims 7/8 (HBMs
> hardwired to columns; multiple HBMs per top-row IC) and framed by claim 1's combined-
> array package (q-0013-1). Scope classes per the Claim scope map: claim 1 sought-broad /
> claim 26 sought-structured / claim 15 sought-system / claim 39 sought-memory-interface.

### Axis 2 — Problem anchor
> `[0018]` "it is unreasonable to expect a single chip to interface with 100s of GB of
> memory used to store parameters and intermediate computation values" (q-0018-2), with
> the compute-side ceiling `[0018]` "Currently, most chips have, at most, floating point
> systolic arrays with a size of 128×128." (q-0018-1)

### Axis 3 — Effect anchor
> `[0045]` deleting the switching element "which can save space and power" (q-0045-2),
> plus the quantitative effects: `[0040]` ">1 TB/s" weight bandwidth per top-row IC
> (q-0040-1) and `[0057]` "98% or greater utilization" (q-0057-1).

### Axis 4 — Baseline-difference anchor
> Industry baseline: HBM access mediated by a switching element — the spec itself states
> the norm, `[0043]` "a switch (or some kind of switching element such as a crossbar) is
> typically used" (q-0043-1) — vs the application's switchless channel-to-column
> hardwiring. External difference: the company's GRANTED record (trio incl. US 12,361,091
> B1) carries the wiring half but not this memory half (fact-check-log:
> prior-essay-wiring-half), and the thread's CSM memory philosophy is company-claimed
> narrative, not granted scope (fact-check-log: etched-thread-2026-07)
> (industry-practice + granted-vs-pending record comparison).

## Q7 hook pattern (hard gate)

- [x] `corporate-narrative-friction` — anchor: Etched's July 2026 thread sells the
  no-memory-middlemen philosophy (CSM) as shipping-now technology ("racks ship summer
  2026", "$1B+ contracts" — all company-claimed) vs the origin document that first put
  the switchless-memory idea in writing in May 2023 and is, as of the 2026-05 record,
  still a pending application continuing after a final rejection — the narrative is ahead
  of the property right.
- [ ] `technical-impossibility`

## Adversarial defense

**Strongest objection** (Category 1, claim scope — layer-confusion priority input): The
thesis calls this filing "the memory half of the architecture in writing", but what is in
writing is claim scope Etched has SOUGHT and failed to obtain for three years — the set
has drawn a final rejection in a crowded, examiner-cited field (8 references: multi-node
ML acceleration, hybrid parallelism, NN accelerator architectures), and the broad
combined-array claims (1/26) are exactly the kind most likely to shrink. If the claims
narrow or die, the "philosophy in writing" is a disclosure with a date on it, not a
property right — and the asset framing the verdict rests on collapses.

**Mitigation**: The verdict prices this in rather than dodging it. The essay's asset-
status section (§6) separates what is already true regardless of prosecution outcome —
the disclosure's date (2023-05-10), its authorship (both co-founders), and its content
(the switchless memory interface, claim 39 family) — from what only a grant would create
(exclusive rights). The claim-scope map's vocabulary carries the distinction: sought-broad
claim 1 is flagged as the likeliest casualty, while sought-memory-interface claim 39 is
presented, as drafted, as the most structurally specific and likeliest survivor. The label
sentence puts the rejection record in the reader's hands in the same section that cites
the collateral facts (both-or-neither).

**Residual risk**: Acceptance — the RCE's outcome is a watchable binary test: the third
non-final action (issuing as of 2026-05) leads either to allowed claims (the memory half
starts becoming a property right) or to further narrowing/abandonment (it remains a dated
disclosure). Under firm posture this maps to closing-binary-test, not closing-open-question.

**Steelman beat**: §6/§7 concedes at full strength: "the examiner has said no once
already, in a field crowded with multi-node acceleration art — the broad claims may never
grant, and three years of prosecution have not yet produced a single enforceable claim."
Then refines: the filing's investor value today was never the fence — it is the dated,
co-founder-authored proof that the memory-side architecture bet predates the funding and
the hype, plus a live, still-funded prosecution bet whose most specific piece (claim 39's
switchless channel-to-column hardwiring) is the part built to survive. (Generic-truism ban
honored: the objection attacks THIS application's prosecution record, examiner field, and
claim breadth — not "patents don't guarantee products".)

## Closing posture

closing_posture: firm
<!-- Edition default for verdict/investor editions, confirmed by essay-context.md
     ("closing_posture: firm — the call leads and is not qualifier-wrapped"). Call shape:
     origin document + memory-half philosophy in writing + company still paying to push
     it (RCE) + whole stack banked as collateral, VERSUS not yet an asset (pending,
     finally rejected once, claims can shrink). Exactly ONE patent-specific anti-hype
     guard (claim 1's breadth is the part likeliest to shrink). The Acceptance residual
     maps to closing-binary-test (the RCE outcome), never closing-open-question. -->

## Single-spine declaration

- [x] Single-spine (default)
- [ ] Multi-spine (override — record SETI authorization)

## Spine → section trace

| Section | Spine element carried | Primary anchors |
|---|---|---|
| 1-lead | Q7 hook — thread's shipping-now CSM narrative vs the May 2023 origin filing (friction) | (framing; thread facts attributed "the company says" — fact-check-log: etched-thread-2026-07) |
| 2-origin-document | What this document is: earliest filing, both co-founders, the "splittable math arrays" subject; ONE clause of continuity with the wiring-half essay allowed | Metadata; `[0013]` q-0013-1; `[0019]` q-0019-1 |
| 3-one-big-array | Mechanism: chips composed into one logical array; preset loop, no runtime instructions; host sees one array | `[0019]`, `[0027]` q-0027-1, `[0028]` q-0028-1, `[0030]` q-0030-1/2, `[0018]` q-0018-1/2; FIG. 1, FIG. 2 |
| 4-memory-half | Axis 1 core: claim 39 family — switch-is-typical baseline, then switchless hardwiring; HBM deps 7/8; Axis 3 effects | `[0016]` q-0016-1, `[0043]` q-0043-1, `[0044]` q-0044-1, `[0045]` q-0045-1/2, `[0040]` q-0040-1; FIG. 5 |
| 5-division-of-labor | Transformer-shaped split: auxiliary circuitry + local memory the arrays never touch (claims 11-13, sought); pipelining to 98% | `[0047]` q-0047-1/2, `[0051]` q-0051-1, `[0057]` q-0057-1; FIG. 6, FIG. 7 |
| 6-asset-status | Prosecution label sentence (ONE sentence) + collateral beat (portfolio scope, both liens, reel/frames, timing correlation-only) + US-only family observation; steelman concession begins here | fact-check-log: prosecution-record, tp-lien-1-2024, tp-lien-2-2025, grant-lien-timing, family-us-only, examiner-cited-field |
| 7-verdict | Firm call: roadmap-not-fence, asset-in-formation the company keeps funding and has banked; steelman refine + closing-binary-test (RCE outcome); ONE anti-hype guard (claim 1 breadth likeliest to shrink) | (framing; Axis anchors recapped, no new evidence) |
