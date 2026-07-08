# Self-audit round 2 — Reader B (skeptical pro-subject reader)

- essay: handoff/03-edit/essay-final.md (draft_version 4, closing_posture: firm)
- persona: AI-infrastructure practitioner (systolic arrays, TPU pods, wafer-scale, HBM);
  application-vs-grant discipline; hunting overclaim AND unearned hedging symmetrically
- sources read: essay-final.md, input/patent.md (full claims 1-42 + spec paras),
  input/essay-context.md, input/figures/fig-02.png, fig-05.png
- isolation: no edit-log, no revision-response/notes, no score-history, no prior selfaudit
  reports read

## Checklist verdicts (evidence-forced)

| # | Check | Verdict | Evidence | Severity |
|---|---|---|---|---|
| 1 | BLUF lead-altitude | yes (pass) | para 1: "Three years on, that document is still not an asset." — declarative verdict, no deferred question | — |
| 2 | Header-as-claim | yes (pass) | all seven `##` headers are assertions; header-only skim reconstructs the argument ("The Narrative Is Three Years Ahead of the Property Right" → "What Exists Today Is a Rejection, a Pledge, and Ongoing Spend" → "A Dated Roadmap the Company Keeps Funding, Not Yet a Fence"). No header overpromises relative to its section's evidence. | — |
| 3 | Steelman present + correct | yes (pass) | "The strongest objection to the whole origin-document framing lands here, and it deserves full strength. What is in writing is claim scope Etched has sought and failed to obtain for three years... The broad combined-array claims, claim 1 and claim 26 as drafted, sit closest to that art... Three years of prosecution have produced no enforceable claim at all... a disclosure is not a moat." — THIS-application objection (examiner-cited field + claim 1/26 breadth + zero enforceable claims), conceded at full strength, then refined in the verdict ("survives contact and changes nothing about the date") without dilution. Not a generic patent truism. Nothing material missing that the source fence permits (external prior-art naming is out of scope); not overcorrected. | — |
| 4 | No meta posturing | yes (pass) | closest span, "The filing is still where the checking starts.", is a functional scope statement, not reader-instruction | — |
| 5 | Jargon as signpost | yes (pass) | HBM, UCIe, RCE ("a paid restart"), final rejection ("the examiner's formal no"), security interest ("a lender's collateral claim"), independent claims ("the ones that stand on their own") all glossed in-line, none deep-dived past the insight | — |
| 6 | No stub / rhythm break | yes (pass) | no section markedly shorter than siblings | — |
| 7 | Thesis not over-restated | marginal NO | the core "pending ≠ asset" verdict is asserted in 4 sections: lede ("still not an asset"), founders section ("A patent application is not a patent"), status section ("what is this document, as a thing an investor can price"), verdict section ("a roadmap in formation rather than a fence") | low (F6) |
| 6G | Over-hedge symmetric check | no over-hedge found (pass) | verdict leads the call ("the verdict is firm. This document is the origin record of Etched's architecture bet"), exactly ONE patent-specific guard ("broad claim 1... likeliest to shrink or die"), no safe-harbor boilerplate, no qualifier-led verdict. The precision labels ("a bibliographic observation... proves nothing by itself about intent"; "an inference, not a record") are brief-mandated discipline labels attached to evidence, not dodges attached to the verdict; the conclusion is NOT safer than the body's evidence. | — |

## Deep claim audit (claims 1/15/26/39 + dependents vs CLAIMS text)

- **Claim 39 / [0016]:** essay quote verbatim-matches [0016]; claim 39 text confirmed
  ("hardwired to respective one or more columns... without any switching element").
  Essay's translation ("bonded, permanently, to its own column or columns... nothing can
  reroute it") is a fair reading of the no-switching-element limitation plus [0045]'s
  channel-isolation consequence. One nit → F3.
- **Independent-claim count:** "the application's four independent claims" — verified:
  1, 15, 26, 39. Correct.
- **Claims 7/8:** claim 7 = HBMs hardwired to respective columns without switching element;
  claim 8 = multiple HBMs per topmost-row IC. Essay compresses both into one clause → F4.
- **Claim 15 / [0014]:** essay's per-claim wording accurate ("coupled to the ICs forming
  the top row, store the model's weights") — note claim 15 itself carries no switchless
  limitation; framing nit → F5.
- **Claims 11-13 / [0051]:** accurate; [0051] quote verbatim; "the two never contend for
  the same store" is fair for claim 13's "do not communicate with" as drafted.
- **AI-limitation statement:** "The broad combined-array claims carry no AI limitation as
  drafted, and neither does claim 39's memory interface" — verified: claims 1, 26, 39
  contain no AI language (claims 6, 40 add it; claim 15 is the AI-accelerator independent
  and the essay pins "broad combined-array claims" to 1 and 26 explicitly). Correct.
- **Application-era language:** consistent throughout ("as drafted", "Etched is seeking",
  "asks for"). No instance of sought-scope stated as owned; "does not yet own anything in
  it" is the operative verdict verb. PASS.
- **No enforceability language:** confirmed; "no enforceable claim at all" is about the
  absence of enforceability, which is the permitted direction.

## Mechanism honesty (vs spec + figures)

- Combined array "appears to be one large array" [0028] — verbatim, correct.
- Directionality: weights top-down [0021]/[0022], data left-to-right — essay and FIG. 1
  caption correct; row-scaling-without-memory point matches [0039].
- Top-row memory feed: FIG. 2 caption ("Memory chips (210A to 210C) sit only on the top
  row", ICs 215A-215I, host 205 over PCIe 240) verified against the actual fig-02.png
  drawing. Correct.
- FIG. 5 caption (505A/505B above IC 215, channels 510A-D, wires 520, columns 515A-D,
  array 220) verified against fig-05.png. Correct.
- Time A/B pipelining: Time A (new computation entering while previous drains) matches
  [0056]; Time B layer-norm stall matches [0057]. Anchor nit → F7. 98% framing nit → F2.
- One essay-voice endorsement of a 2023 spec premise that a 2026 practitioner would
  contest → F1 (the medium).

## External-fact fencing

- Collateral discipline: PASS — "Both liens are blanket over the portfolio at signing,
  with no selectivity about any single filing, so they say nothing about this application
  in particular"; both-ways frame present; reel/frames match the brief.
- ONE prosecution label sentence: PASS — the label sentence carries pending + final
  rejection + RCE + 2026-05 record; no office-action chronology anywhere; later mentions
  ("paid restart... back in front of the examiner") reuse the already-labeled facts
  interpretively, adding no new record content.
- Motive-as-inference: PASS — "reading them as a lender sweeping fresh assets into its
  collateral is an inference, not a record"; three-days interval stated as dates.
- Thread facts: every use carries "the company says" / "the company's own account". PASS.

## Grounding spot-check (5+ samples, essay anchor vs patent.md)

1. [0013] block quote — verbatim match. PASS
2. [0018] "it is unreasonable to expect a single chip to interface with 100s of GB..." —
   verbatim. PASS
3. [0043] "a switch (or some kind of switching element such as a crossbar) is typically
   used..." — verbatim. PASS
4. [0045] "hardwiring the memory chips 505 to the columns 515 is permissible" + "which can
   save space and power" — verbatim. PASS
5. [0040] "can enable the memory chips 305 to transmit more than 1 TB/s of data to each of
   the ICs" — verbatim; essay's gloss preserves "topmost row" as "top-row chip". PASS
6. [0047] both quotes, [0021] "may be constants", [0044] "can be directly wired (or
   hardwired) to a particular column", [0002], [0028], [0057] — all verbatim. PASS
7. Pinned values: 128×128 ("top out at" = "at most"), 32 GT/s ("up to" is the patent's own
   words inside the quote), >1 TB/s, 98%-or-greater — none misdescribed as exact/bounds. PASS

## Findings

### sa2B-F1 — adopted-premise stated in essay voice — MEDIUM
- check: mechanism honesty / technical overclaim (pro-subject)
- verdict: NO (fails)
- evidence: "Hundreds of gigabytes is the working size of a modern model's parameters,
  roughly a whole laptop's storage, and no single chip realistically interfaces with that
  much memory [0018]."
- problem: the second clause asserts, in the essay's own present-tense (2026) voice, the
  filing's May-2023 premise. To a practitioner this is contestable today: current
  accelerator packages ship with roughly 192-288 GB of directly-interfaced HBM, i.e.
  "100s of GB" on a single chip package is now ordinary. The block quote above it is
  properly attributed; the gloss sentence drops the attribution and endorses.
- fix (jurisdiction fence: label, not hedge): attribute the clause to the filing — e.g.
  "and, the filing argues, no single chip realistically interfaces with that much memory
  [0018]" — or recast as the filing's 2023 premise. Do NOT add a hedge to the verdict.

### sa2B-F2 — "puts the result at" strengthens a conditional — LOW
- check: mechanism honesty
- verdict: NO (minor)
- evidence: "the filing puts the result at '98% or greater utilization of the systolic
  array' [0057]" vs patent: "the stalled time may be small relative to the computation
  time and still result in a 98% or greater utilization"
- problem: [0057]'s number is inside a "may... still result in" conditional; "puts the
  result at" reads it as a stated result. Attribution to the filing is present, which caps
  severity.
- fix: "puts the achievable result at" or "claims the result can still be".

### sa2B-F3 — "mirrored word for word" is off by one word — LOW
- check: claim audit precision
- verdict: NO (nit)
- evidence: essay: "The claim language, mirrored word for word in the filing's own
  summary". Claim 39: "wherein each of the plurality of channels"; [0016]: "where each of
  the plurality of channels".
- problem: the mirror differs by "wherein"/"where". The quoted span itself is verbatim
  from [0016], so grounding passes; only the "word for word" flourish overstates.
- fix: "mirrored nearly word for word" or drop the flourish.

### sa2B-F4 — claims 7/8 compressed into one joint attribution — LOW
- check: claim audit
- verdict: NO (minor)
- evidence: "Claims 7 and 8, as drafted, put HBMs on that same switchless hardwiring,
  several of them per top-row chip."
- problem: "several of them per top-row chip" is claim 8's limitation only (claim 7
  requires hardwired HBMs, not multiplicity). Joint phrasing attributes claim 8's
  limitation to both.
- fix: "Claims 7 and 8, as drafted, put HBMs on that same switchless hardwiring — claim 8
  several of them per top-row chip."

### sa2B-F5 — claim 15 inside the "family around the idea" frame — LOW
- check: claim audit / framing
- verdict: NO (minor)
- evidence: "The claim set builds a family around the idea. Claims 7 and 8... Claim 15
  frames the system version, an AI accelerator whose memory chips, coupled to the ICs
  forming the top row, store the model's weights [0014]."
- problem: "the idea" in context is the switchless interface; claim 15 as drafted carries
  no no-switching-element limitation (its mirrors, claims 19/20, and the grid-package
  mirrors 32/33, do — and go unmentioned). The per-claim wording ("coupled") is accurate,
  so this is frame-level only. Citing 19/20 would make the "family" statement literally
  true and stronger.
- fix: either narrow "the idea" to the memory-fed top row for the claim-15 sentence, or
  add the 19/20 mirror in a clause.

### sa2B-F6 — core verdict asserted in 4 sections — LOW
- check: pass-7 #7 thesis-restatement-redundancy
- verdict: NO (marginal)
- evidence: "still not an asset" (lede) / "A patent application is not a patent" (founders
  section) / "as a thing an investor can price" (status section) / "a roadmap in formation
  rather than a fence" (verdict) — 4 sections vs the <=3 pass condition.
- mitigation: each restatement carries new content (definition, pricing, verdict), so this
  reads as spine, not padding. Candidate cut if any: the founders-section restatement
  could compress.

### sa2B-F7 — FIG. 7 caption anchors Time A content to [0057] only — LOW
- check: grounding / anchor precision
- verdict: NO (nit)
- evidence: caption: "...at Time A a new computation has already entered while the
  previous one drains. The only idle gap is the layer-normalization stall, marked at
  Time B [0057]." Time A content is [0056]; only [0057] is anchored.
- fix: add [0056] after the Time A clause.

## Findings not raised (checked and passed)

- Over-hedge: none — no recently-added precision label reads as a dodge; the
  "bibliographic observation" and "inference, not a record" labels are brief-mandated and
  attach to evidence, not to the call.
- Prosecution one-label budget: compliant (one record-bearing sentence; later mentions
  interpretive).
- "8 references... which is to say the field is crowded": the crowded-field reading is the
  brief's own sanctioned characterization (essay-context §External facts 3); not flagged.
- Grant/sought confusion: none found anywhere.

## Persona verdict

As a practitioner I came in expecting either TPU-envy overclaim or rejection-record
cowardice and found neither: the claim audit survives contact with the actual claims text,
the steelman is the real objection (claims 1/26 sit on crowded multi-node art and three
years of prosecution have produced nothing enforceable), and the firm close is earned
rather than hyped. The one sentence I'd attack is "no single chip realistically interfaces
with that much memory [0018]" — a May-2023 drafting premise spoken in the essay's own
2026 voice, in a year when 192-288 GB single-package HBM is catalog hardware; attribute it
to the filing and the essay is clean. (Runner-up target, "On claim structure alone, it is
the best candidate to survive in some form", survives because its basis is labeled and its
prediction is bounded.)

## Totals

- critical: 0
- high: 0
- medium: 1 (sa2B-F1)
- low: 6 (sa2B-F2..F7)
