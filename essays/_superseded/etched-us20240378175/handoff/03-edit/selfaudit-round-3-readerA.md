# Self-audit round 3 — Reader A (impatient investor)

- essay: handoff/03-edit/essay-final.md (draft_version 5, closing_posture: firm)
- persona: impatient investor (reader-profile tier; saw the Etched stealth-exit thread; 6 minutes; headers first, captions before body)
- pass: pass-7-adversarial-reader (checklist 1-9) + grounding spot-checks vs input/patent.md and the Phase-1 Claim scope map
- isolation honored: did NOT read edit-log*, revision-response*, revision-notes.md, score-history, or any prior selfaudit report

## Checklist results (evidence-forced)

### 1. BLUF lead-altitude — PASS
Para 1 under the first header is a declarative verdict, not a deferred question: "The memory
half of Etched's architecture story has been in writing since 10 May 2023 ... Three years on,
that document is still not an asset." The title itself is a claim ("...It Is Still Pending.").
No question-lead. Severity: none.

### 2. Header-as-claim — PASS
Header-only skim reconstructs the argument: "The Narrative Is Three Years Ahead of the
Property Right" → "Both Founders Put the Bet in Writing in May 2023" → "Many Small Arrays,
Presented to the Host as One" → "The Application Claims a Memory Interface With No Switch in
It" → "The Rest of the 2023 Design Is Already Transformer-Shaped" → "What Exists Today Is a
Rejection, a Pledge, and Ongoing Spend" → "A Dated Roadmap the Company Keeps Funding, Not Yet
a Fence." Every `##` is an assertion. Severity: none.

### 3. Steelman present — PASS (THIS-patent, full strength, then refined)
Quoted span: "What is in writing is claim scope Etched has sought and failed to obtain for
three years. ... The broad combined-array claims, claim 1 and claim 26 as drafted, sit
closest to that art and are exactly the kind of claims that shrink in it. Three years of
prosecution have produced no enforceable claim at all. If the set narrows or dies, what
remains is a disclosure with a date on it, and a disclosure is not a moat." This is a
THIS-application objection (crowded examiner-cited field + claim-1/26 breadth), not a generic
truism, and the verdict refines rather than retracts: "The crowded-field objection survives
contact and changes nothing about the date." Severity: none.

### 4. No meta posturing — PASS
No reader-instruction or essay-self-reference. "So the honest verbs for this document are
application-era verbs" functions as a scope disclaimer (exempt class). The single continuity
clause ("the subject of an earlier analysis") is within the brief's allowance. Severity: none.

### 5. Jargon as signpost — PASS overall, two low findings (sa3A-F1, sa3A-F2 below)
Glosses land at first body use: systolic array ("a grid of small calculating cells"), HBM
("the stacked memory chips AI accelerators use"), UCIe ("a chip-to-chip standard"), RCE ("a
paid restart that keeps the argument alive"), security interest ("a lender's collateral
claim"), continuation ("the follow-on application that would extend the family"), independent
claims ("the ones that stand on their own rather than adding to another"), layer
normalization ("a bookkeeping step that rescales values between stages"), self-attention
("the step where a model looks back over everything it has generated so far"). No
jargon-overdepth: FIG. 7 and UCIe each get one insight and move on.

### 6. No stub / rhythm break — PASS
Seven body sections, each 2-5 paragraphs; no section markedly shorter than siblings. The
figure captions are consistent in weight. Severity: none.

### 7. Thesis not over-restated — PASS (at the boundary)
The core verdict ("origin record; roadmap/asset-in-formation, not yet a fence") is asserted in
3 body sections: lead ("still not an asset"), section 2 ("A patent application is not a
patent"), closing ("a roadmap in formation rather than a fence"). Section 6 is evidence, not
verdict restatement. Counted at the <=3 limit; each recurrence carries new material
(collateral, rejection, falsifier). Severity: none.

### 8. Grounding spot-checks — 5 primary samples + 3 extras, ALL PASS

Verbatim quotes vs input/patent.md:

1. **[0016] / claim 39** — essay quote "a separate memory device comprising a plurality of
   channels where each of the plurality of channels is hardwired to respective one or more
   columns in the systolic array without any switching element" — verbatim at patent [0016]
   (line 78); claim 39 (line 171) matches with "wherein" phrasing, and the essay's "mirrored
   almost word for word in the filing's own summary" is accurate. PASS.
2. **[0018]** — "it is unreasonable to expect a single chip to interface with 100s of GB of
   memory used to store parameters and intermediate computation values" — verbatim (line 81);
   "floating point systolic arrays with a size of 128×128" verbatim, and the essay's "top out
   at" fairly renders the patent's "at most". PASS.
3. **[0043]** — "a switch (or some kind of switching element such as a crossbar) is typically
   used so that the device can access the entire memory of the HBM" — verbatim (line 106).
   PASS.
4. **[0044]/[0045]** — "can be directly wired (or hardwired) to a particular column",
   "hardwiring the memory chips 505 to the columns 515 is permissible", "which can save space
   and power" — all verbatim (lines 107-108); the FIG. 5 caption's channel→column mapping
   (510A-D → 515A-D) matches [0044] exactly. PASS.
5. **[0040]** — "can enable the memory chips 305 to transmit more than 1 TB/s of data to each
   of the ICs" — verbatim (line 103); essay's "into each top-row chip" matches the patent's
   "in the topmost row". PASS.

Extras: [0027] "does not take instructions at runtime, and only executes instructions in a
preset loop" verbatim (line 90); [0051] "In this embodiment, the local systolic arrays 220 do
not have access to the local memory chips 610." verbatim (line 114), and pinning it to claim
13 is claim-accurate ("do not communicate with the local memory chips", line 145); [0057]
"98% or greater utilization of the systolic array" verbatim (line 120). "Four independent
claims" = 1, 15, 26, 39 — correct. Claims 7/8 characterization matches lines 139-140.

**Claim scope map honored:** map is sought/open/pinned with NO locked class; essay uses
application-era verbs throughout ("asks for", "claims, as drafted", "is seeking"). UCIe/32
GT/s correctly held as "a description preference, not something claim 1 requires as drafted"
(map: claim 1 leaves-open). "The broad combined-array claims carry no AI limitation as
drafted, and neither does claim 39's memory interface" — verified: AI enters only via deps 6
and 40. Map pins column = none, and no description value (128×128, 32 GT/s, 1 TB/s) is
presented as a claim bound — each is quoted with the patent's own qualifier ("at most", "up
to", "more than"). Lien discipline honored ("blanket ... no selectivity about any single
filing"); motive reading of the 3-day grant→lien gap labeled "an inference, not a record".
PASS.

### 9. Persona verdict + symmetric over-hedge check — PASS, one low finding (sa3A-F4)

- **Over-hedge / pending-status-as-crutch:** NOT present. The call leads ("Hold the July 2026
  thread against the May 2023 filing and the verdict is firm"), and pending status is priced,
  not hidden behind: the essay still makes affirmative differential calls (claim 39 "the best
  candidate to survive in some form"; claim 1 "likeliest to shrink or die"), names a falsifier
  already on the docket, and closes hard ("The racks are shipping, the company says. The
  paper is still asking."). Exactly ONE patent-specific anti-hype guard ("The one guard the
  evidence forces is just as specific: broad claim 1 ..."). No safe-harbor boilerplate in the
  verdict; "a disclosure is not a moat" lives inside the steelman where it belongs. The
  conclusion is NOT safer than the body's evidence (6G clear).
- **Overreach:** none found; the survival call is basis-labeled ("On claim structure alone").
- **Stop-point:** none hard. Mild drag in the FIG. 2 paragraph (UCIe/32 GT/s detail) before
  the money thread returns in section 6, but the in-tech relevance flag ("That inflexibility
  is the investor-relevant fact") held me.
- **Leaving question:** "when will the examiner decide, and is a final rejection normal or
  fatal?" — the falsifier answers the what, not the when/how-typical (see sa3A-F4).
- **Share yes/no:** YES — the title claim is quotable and the close is screenshot-able.

## Findings

### sa3A-F1 — check 5 (jargon-as-signpost) — LOW
- verdict: no (one un-glossed unit)
- evidence: "a physical layer that 'supports up to 32 GT/s' [0030]"
- "GT/s" (gigatransfers per second) is the only unit in the essay with no gloss or scale
  anchor; the reader-profile tier reads it as noise. Everything nearby gets a comparison
  (100s of GB = "a whole laptop's storage"; 1 TB/s = "a full laptop drive's contents moving
  every second"). Fix: three-word gloss or cut the number (it is a description preference
  anyway, as the essay itself says).

### sa3A-F2 — check 5 / captions-first reading order — LOW
- verdict: no (terms of art hit cold in the header caption)
- evidence: header caption fig-05: "Two memory chips (505A, 505B) sit above one IC (215) ...
  a dedicated column (515A to 515D) of the chip's systolic array (220)"
- A captions-before-body reader meets "IC" and "systolic array" un-glossed before section 3
  defines them. The caption's plain framing ("No switch, no crossbar, nothing between memory
  and math") mostly rescues it. Fix option: "one IC (chip, 215)" in the caption.

### sa3A-F3 — check 9 / asymmetric basis-labeling of the two claim calls — LOW
- verdict: no (labeled analysis on one side only)
- evidence: survival call is labeled — "On claim structure alone, it is the best candidate to
  survive in some form" — but the shrink call is asserted bare: "broad claim 1, the plain
  combined-array package, sits closest to the examiner-cited multi-node art and is the part
  of this filing likeliest to shrink or die."
- Both are analysis derived from the same Claim scope map risk notes (which the map supports);
  only one carries its basis label. Fence-compliant fix: labeled analysis — mirror the basis
  ("on claim breadth alone" or "against the examiner-cited categories"). NOT a hedge; the
  call itself stays.

### sa3A-F4 — check 9 / persona calibration of "final rejection" — LOW
- verdict: no (lay reader may over-read the gloss as terminal)
- evidence: "a final rejection (the examiner's formal no) and a request for continued
  examination (a paid restart that keeps the argument alive)"
- "The examiner's formal no" invites the tier reader to hear "dead"; in prosecution a final
  rejection is a routine stage. The RCE gloss partially calibrates ("keeps the argument
  alive"), and the falsifier paragraph restores the two-way frame, so severity stays low.
  Any fix must live inside the existing single label sentence's glosses (edition budget:
  exactly one label sentence, no battle narrative) — e.g. gloss RCE as "the standard paid
  restart". Do not add a second status sentence.

## Totals

- critical: 0 · high: 0 · medium: 0 · low: 4
- Hard-gate-relevant categories (grounding, steelman, over-hedge/6G, BLUF, meta): all PASS.
- Round-3 dry-check assessment from this reader: no medium+ findings; nothing here blocks
  acceptance.
