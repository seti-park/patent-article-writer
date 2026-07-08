# Essay context — US 2024/0378175 A1 (Etched.ai, "Multi-chip systolic arrays") — PENDING APPLICATION

Framing brief for the patent-essay pipeline. Read by Phase 1 (audience reframe) and carried
through Phase 2/3. Where it conflicts with anything else, this brief controls.

## Edition: pending-application analysis (FIRST OF ITS KIND for this pipeline)

This is a PATENT APPLICATION, not a grant. That changes the claim discipline everywhere:

- There are NO locked claims. Every entry in the Claim scope map is **sought**, not locked;
  the claims may narrow or die before grant. Never use grant-era language ("the patent
  locks/requires/fences") for claim content — use application-era language ("the
  application claims / Etched is seeking / as drafted").
- The verdict therefore cannot be about fence strength. It lands on what this document IS:
  the company's origin filing and the memory-side half of its architecture philosophy in
  writing, plus what its treatment (portfolio collateral, continued prosecution spend)
  says about the company — an asset-in-formation, a roadmap rather than a fence.
- **Prosecution status: exactly ONE label sentence in the essay, no battle narrative**
  (user decision). The sentence must carry: pending; examination continuing after a final
  rejection and a request for continued examination (as of the 2026-05 record). This label
  is REQUIRED — an investor essay that cites the collateral fact while omitting the
  rejection record would be one-sided evidence selection; both or neither.

## Audience and deliverable

- **Audience:** default reader-profile (curious retail investor; advanced high school –
  early undergraduate). No override.
- **News moment:** same as the prior run — Etched's July 2026 stealth-exit thread (LVI +
  CSM claims, "$1B+ contracts", "$800m raised", racks ship summer 2026; all company-claimed,
  attribute as such). This essay is a standalone follow-up to the published analysis of
  granted US 12,361,091 B1 ("the wiring half"); one clause of continuity is allowed, no
  dependence on having read it.
- **Question to answer:** Etched's very first patent filing describes stitching chips into
  one giant systolic array and hardwiring memory to it without switches. What does this
  origin document reveal about the architecture bet, and what is it worth to an investor
  today as an asset? Land a clear verdict.
- **Deliverable:** one standalone English analytical article (X Articles long-form).

## The spine material (Phase 1 decides, but these are the load-bearing facts)

- **Origin:** filed 2023-05-10, the company's earliest filing; both co-founders (Uberti,
  Zhu) are the inventors. The thread's "splittable math arrays" is this document's subject.
- **Claim 39 family (the memory-side echo):** a separate memory device whose channels are
  "hardwired to respective one or more columns in the systolic array without any switching
  element"; claim 7 puts HBMs hardwired to columns; claim 15 streams weights from memory
  chips into the top row. This is the "each memory layer adds latency; the best layer is no
  layer" philosophy of the thread's CSM pillar, written two years earlier — but pending,
  not granted. Pairs with (does not repeat) the published wiring-half essay's verdict that
  the memory half was absent from the GRANTED record.
- **Also present:** claims 11-13 auxiliary/self-attention circuitry with local memory the
  systolic arrays never touch (the transformer-ASIC division of labor); FIG. 7 pipelining.

## External facts (tiered; fact-check-log must carry evidence_level per fact)

1. **Venture-debt collateral (the investor beat, PORTFOLIO scope only):**
   - 1st security interest: TriplePoint Capital LLC, effective 2024-04-19, USPTO reel/frame
     067204/0877 — covers the four 2023-era applications (all Etched IP existing then),
     including the two later-rejected compiler applications. Source: DOCDB legal events via
     WIPS export 2026-07-02. evidence_level: registry-extract.
   - 2nd security interest: TriplePoint Capital LLC, effective 2025-07-18, reel/frame
     071792/0869 — covers the portfolio INCLUDING the granted trio (US 12,306,903 /
     12,361,091 / 12,361,262). Source: user-verified against USPTO assignment records,
     2026-07-03. evidence_level: registry-verified. Phase 1 should cite the reel/frame.
   - **Timing detail (usable, correlation only):** the trio's second and third grants
     issued 2025-07-15; the second lien is effective 2025-07-18 — three days later. State
     the dates; label any motive reading as inference.
   - **DISCIPLINE (hard):** the liens are blanket over the portfolio at each signing date —
     they carry ZERO patent-specific selectivity. Never present the lien as evidence that
     THIS application is individually important (the same pool contains two rejected
     applications). The honest frame: Etched's entire patent stack, crown jewels included,
     is pledged as venture-debt collateral — IP is the company's bankable asset class, and
     symmetrically, the encumbered pool is what a creditor reaches if things go wrong.
2. **Prosecution record (label-sentence only, see Edition):** non-final actions 2024-11 and
   2025-07; final rejection mailed 2025-10-23; RCE docketed 2026-04-24; third non-final
   action issuing as of 2026-05. Source: DOCDB via WIPS export 2026-07-02.
   evidence_level: registry-extract.
3. **Examiner-cited art context (optional, one clause):** 8 unique references, all
   examiner-cited (multi-node ML acceleration, hybrid parallelism, NN accelerator
   architectures) — a crowded field. Source: USPTO/Google Patents citation record.
   evidence_level: registry-extract.
4. **Thread claims:** company-claimed only, attribute as "the company says".
5. **Family:** US-only, no PCT, no continuation (WIPS export 2026-07-02;
   evidence_level: bibliographic) — contrast with the granted trio's PCT+continuation
   treatment is allowed as a labeled observation.

## Scope boundaries (anti-hype guard material)

- LVI (voltage, VRMs, cold plates) is nowhere in THIS filing either (full-text verified —
  zero voltage/power-delivery content). Same 18-month-unpublished-window caveat applies to
  what may exist unseen.
- Absence claims about OTHER filings need their own evidence level; this run has full text
  for THIS application only (plus the prior run's full text of US 12,361,091 B1).
- No enforceability language anywhere: nothing here can be infringed until (unless) it
  grants.

## Posture and closing discipline

- **Posture: measured.** Full accuracy bar; claim-scope (sought!) and external-fact
  discipline as above.
- **closing_posture: firm.** Firm does not mean bullish — it means the call leads and is
  not qualifier-wrapped. The call shape available on this evidence: origin document + the
  memory-half philosophy in writing + the company still paying to push it + the whole
  stack banked as collateral, VERSUS not yet an asset (pending, rejected once, claims can
  shrink). Exactly ONE patent-specific anti-hype guard; steelman must be a THIS-application
  objection (e.g., the crowded examiner-cited field, or the breadth of claim 1 being the
  part most likely to shrink), not a generic patent truism.

## Figures available

- `input/figures-raw/` carries 7 drawing sheets (Safari-1..7.PNG, browser exports; names
  meaningless — Phase 0 names by vision). The application declares FIG. 1-7, one per sheet
  expected: 1 systolic array basics; 2 package with combined array; 3-4 multi-chip array
  variants; 5 hardwired external memory chips; 6 local memory chips; 7 pipelining.

## Reader-first fields (2026-07-04 architecture, r2 run)

- **reader_sentence** (the one sentence the reader wants to say to someone after reading):
  "Etched wrote the no-switch memory idea into its first patent filing in May 2023, two
  years before the hype thread — the patent office just hasn't said yes yet."
- Title + lead must deliver this sentence's energy; the discovery beat leads ¶1, and
  verdict-insurance facts (pending status, liens, rejection) never precede it. The full
  two-sided call still lands by the end of the lead section, and every accuracy rule in
  this brief (label-sentence budget, both-or-neither, portfolio-scope collateral,
  application-era language) is unchanged.
- Energy-register default if the human does not pick: Phase 1's `recommended:` from
  title-lead-candidates.md.
