# Self-audit round 1 — Reader B (skeptical pro-subject reader)

- **Persona:** AI-infrastructure practitioner (systolic arrays, TPU-class pods, wafer-scale,
  HBM integration); reads for technical overclaim AND unearned hedging; application-vs-grant
  discipline checked cold.
- **Target:** `handoff/03-edit/essay-final.md` (draft v3, posture measured, closing firm)
- **Sources read:** `input/patent.md` (claims 1-42 in full + [0001]-[0057]),
  `input/essay-context.md`, `handoff/01-design/invention-summary.md` (Claim scope map only,
  for locked/open/pinned verification). No edit-log, no revision-response, no other reader.
- **Rules honored:** evidence-forced; ADD-only; jurisdiction fence (fixes are
  anchor / narrow / label / cut — never hedge).

## Finding count

| severity | count |
|---|---|
| high | 0 |
| medium | 1 |
| low | 5 |

---

## Checklist results

### 1. BLUF — verdict YES (pass)

Para 1 leads with a declarative verdict, not a deferred question:

> "The memory half of Etched's architecture story has been in writing since 10 May 2023 …
> Three years on, that document is still not an asset."

No finding.

### 2. Overpromising headers — verdict MOSTLY NO; one flag (→ sa1B-F4, low)

Headers are assertions and the header-only skim reconstructs the argument
("The Narrative Is Three Years Ahead of the Property Right" → "… Rejection, a Pledge, and
Ongoing Spend" → "A Dated Roadmap … Not Yet a Fence"). One header overpromises hardware:
"The Rest of the **2023 Silicon** Is Already Transformer-Shaped" — there is no 2023 silicon;
what is transformer-shaped is a filing's disclosed design. See sa1B-F4.

### 3. Steelman — verdict PRESENT and mostly RIGHT; one refinement gap (→ sa1B-F1, medium)

Present at full strength, and it is a THIS-application objection, not a truism:

> "What is in writing is claim scope Etched has sought and failed to obtain for three years.
> The examination record lists 8 references, all examiner-cited … the field was already
> crowded when the founders filed. The examiner has said no once. The broad combined-array
> claims, claim 1 and claim 26 as drafted, sit closest to that art … Three years of
> prosecution have produced no enforceable claim at all. If the set narrows or dies, what
> remains is a disclosure with a date on it, and a disclosure is not a moat."

Conceded, then refined honestly ("The crowded-field objection survives contact and changes
nothing about the date") — the refinement pivots to invariants (filing date, inventors,
content) rather than pretending the objection loses. That is the correct shape.

The gap: the steelman's blast radius is quietly confined to claims 1/26, while the verdict
then promotes claim 39 to "the likeliest survivor" — but the final rejection the essay itself
reports ("the claims have been refused once") covered the set claim 39 sits in, and the only
novelty evidence offered for the switchless interface is the applicant's own background
characterization ([0043] "typically used"), which an examiner does not treat as a concession
about the art. A pro reader notices the survivor ranking is never tested against the same
crowded field the steelman deploys against claims 1/26. Captured as sa1B-F1.

### 4. Technical-claim audit (claims 1/15/26/39 + dependents 7/8/11-13) — verdict HOLDS with two local stretches

Checked every claim-scope statement against the claims text (patent.md lines 133-174) and
the Claim scope map (invention-summary.md, sought/open/pinned — no "locked" class exists;
Pins column is "none" for every row, and the essay pins no value as a claim bound).

| Essay statement | Claims text | Verdict |
|---|---|---|
| Blockquote of the claim-1 package concept, cited to [0013], glossed "many small math grids, on many chips, wired to each other until they act as one big grid" | Claim 1 / [0013] verbatim | HOLDS |
| "This is the interface the application claims, as drafted, in claim 39 [0016]" (header caption) | Claim 39 = IC + separate memory device, channels "hardwired to respective one or more columns … without any switching element" | HOLDS |
| "Claim 39 … In translation, each memory channel is bonded, permanently, to its own column of the array, and nothing can reroute it" | Claim says "respective **one or more columns**" — translation narrows to one column per channel; the verbatim quote with "one or more columns" follows two lines later | STRETCHES (minor; self-correcting) → sa1B-F6, low |
| "Claims 7 and 8, as drafted, put HBMs on that same switchless hardwiring, several of them per top-row chip" | Claim 7: HBMs "hardwired to respective columns … without any switching element"; claim 8: "multiple HBMs … each of the plurality of ICs in the topmost row" | HOLDS |
| "Claim 15 frames the system version, an AI accelerator whose memory chips, coupled to the ICs forming the top row, store the model's weights [0014]" | Claim 15 / [0014] verbatim | HOLDS |
| "Claims 11 to 13, as drafted, add auxiliary circuitry (605) … The **same claims** then draw a boundary the arrays cannot cross" | Only claim 13 recites "the local systolic arrays do not communicate with the local memory chips"; claims 11-12 do not draw the boundary | STRETCHES → sa1B-F2, low |
| "The broad combined-array claims carry no AI limitation as drafted, and neither does claim 39's memory interface" | Claims 1, 26, 39: no AI term; AI arrives in deps 6/12/31/40 and indep. 15 | HOLDS |
| "the application's four independent claims, the ones that stand on their own rather than adding to another" | Independents are exactly 1, 15, 26, 39 | HOLDS |
| "That is a description preference, not something claim 1 requires as drafted" (UCIe / 32 GT/s) | Claim 1 recites no connection technology; matches scope-map "Leaves open" column | HOLDS |
| "As drafted, it is the likeliest survivor among the application's four independent claims" | Not a claims-text fact at all — a prosecution-outcome prediction, stated flat in the verdict section | BREAKS as stated (unlabeled inference) → sa1B-F1, medium |

**Application-era language sweep:** verdict HOLDS everywhere. Every claim-content statement
carries "as drafted" / "asks for" / "the application claims" / "Etched is seeking"; the title
says "Still Pending"; "the honest verbs … are application-era verbs" is stated and then
practiced. The only "patent" used as owned property is the actually-granted US 12,361,091 B1.
No enforceability language anywhere (essay-context hard rule honored). No sought claim is
stated as owned — the closest approach is the survivor prediction (sa1B-F1), which is a
prognosis problem, not an ownership-verb problem.

### 5. Mechanism honesty — verdict HOLDS (one embodiment-elevation flag)

- **Combined-array story:** "Horizontal connections (230) and vertical connections (225) join
  neighboring tiles until they compute as one combined systolic array (250) [0019]" — matches
  [0019]/[0029]; "appears to be one large array" [0028] verbatim. HOLDS. (The essay does not
  assert row bidirectionality / column unidirectionality as claim requirements — correctly,
  since those live in deps 3-4/17-18/28-29 and [0029] "In one embodiment.")
- **Top-row memory feed:** "Model weights (110) … enter from the top row of cells (105)
  [0021]" — [0021] "The topmost row of DPUs 105 receive AI model weights 110." HOLDS.
  "adding more rows of chips adds compute without adding memory chips at the top [0039]" —
  [0039] verbatim concept ("without having to add more memory chips 305 at the top … data …
  is reused across the rows"). HOLDS.
- **Pipelining Time A/B:** caption "at Time A a new computation has already entered while the
  previous one drains" — [0056] (Time A: DPU 0 on MLP output layer while DPU Y still on
  hidden layer). "The only idle gap is the layer-normalization stall, marked at Time B
  [0057]" — [0057] (stall at Time B, X cycles). "98% or greater utilization" verbatim [0057],
  correctly conditioned ("Even with a stall for layer normalization"). HOLDS.
- **1 TB/s:** quoted with the spec's own conditions intact ("with several memory chips
  feeding each top-row chip, the arrangement 'can enable … more than 1 TB/s'") [0040]. HOLDS —
  not stated as a spec-guaranteed bound.
- **Flag:** "One more design choice defines the machine. The combined array 'does not take
  instructions at runtime…' [0027]" — [0027] says "**in one embodiment**, the systolic array
  250 does not take instructions at runtime," and no claim recites it. Elevating an
  embodiment sentence to "defines the machine" overstates commitment. → sa1B-F3, low.

### 6. External-fact fencing — verdict CLEAN (NONE)

- **Attribution:** "The company says its first racks ship in summer 2026, that it holds more
  than $1 billion in customer contracts against $800 million raised … Every number and claim
  in that thread is the company's own account." / "The racks are shipping, the company says."
  All thread facts attributed. NONE.
- **Collateral, portfolio scope:** both reel/frames present (067204/0877 eff. 2024-04-19;
  071792/0869 eff. 2025-07-18); the hard discipline sentence is verbatim-honored: "Both liens
  are blanket over the portfolio at signing, with no selectivity about any single filing, so
  they say nothing about this application in particular." Symmetric creditor framing present.
  NONE.
- **Timing fact vs motive inference:** "The dates are registry fact, and reading them as a
  lender sweeping fresh assets into its collateral is an inference, not a record." Cleanly
  separated. NONE.
- **Prosecution label:** exactly one label sentence carrying the required content ("pending,
  with examination continuing after a final rejection … and a request for continued
  examination", "As of the 2026-05 record"); later mentions ("The examiner has said no
  once", "The paid restart") add no chronology — no battle narrative. NONE.
- **Family observation:** labeled bibliographic, "proves nothing by itself about intent."
  NONE.

### 7. Grounding spot-checks (sections 3, 4, 5, 6 sampled) — 8/8 HOLD

1. [0018] "it is unreasonable to expect a single chip to interface with 100s of GB of
   memory used to store parameters and intermediate computation values" — verbatim. HOLDS.
2. [0018] "floating point systolic arrays with a size of 128×128" — verbatim ("most chips
   have, at most, …"; essay gloss "most chips top out at" is faithful). HOLDS.
3. [0002] "perform the same task with different data at different times" — verbatim (spec:
   "algorithms that typically perform…"; essay drops "typically" outside the quote marks —
   acceptable). HOLDS.
4. [0043] switch/crossbar quote — verbatim. HOLDS.
5. [0044] "can be directly wired (or hardwired) to a particular column" — verbatim; FIG. 5
   caption channel-to-column mapping (510A→515A … 510D→515D, chips 505A/505B, wires 520)
   matches [0044] exactly. HOLDS.
6. [0045] "hardwiring the memory chips 505 to the columns 515 is permissible" + "which can
   save space and power" — both verbatim. HOLDS.
7. [0047] both self-attention quotes — verbatim. HOLDS.
8. [0051] "In this embodiment, the local systolic arrays 220 do not have access to the local
   memory chips 610." — verbatim, and the essay keeps the spec's own "In this embodiment"
   inside the quote; the claim-side boundary is real (claim 13). HOLDS (attribution of the
   boundary to "the same claims" is sa1B-F2).

Pinned values: scope map pins none; essay pins none as claim bounds. Locked/open honored
(no "locked" class exists for this edition; every scope statement says sought/as-drafted).

### 8. Over-hedge symmetric check — verdict NONE

The verdict leads and is not qualifier-wrapped: "Hold the July 2026 thread against the May
2023 filing and the verdict is firm." The rejection record is used to scope the call, not to
dodge it ("The rejection record and the blanket liens scope this call without softening
it."). The only "may" attached to patent content is the spec's own ("may be constants"
[0021], quoted). Exactly one patent-specific anti-hype guard (claim 1 "likeliest to shrink
or die"). No safe-harbor boilerplate, no generic "patents don't guarantee products" anywhere.
No 6G finding.

---

## Findings (ADD-only)

### sa1B-F1 — medium — check 3/4 (steelman refinement + unlabeled inference in verdict)

- **Span:** "As drafted, it is the likeliest survivor among the application's four
  independent claims" (verdict section), read against "the claims have been refused once"
  (asset-status section) and "inverts the crossbar practice the specification itself calls
  typical [0043]."
- **Problem:** a prosecution-outcome prediction stated flat in the verdict. Claim 39 sits in
  the same finally-rejected set, and the essay's only novelty evidence for the switchless
  interface is the applicant's own background paragraph ([0043]) — an applicant
  characterization, not art. The design-side scope map itself is more careful: "likeliest of
  the four to survive **in some form**, though the 'without any switching element' negative
  limitation remains examinable." The essay dropped both qualifiers of scope, so the steelman
  implicitly walls claim 39 off from the objection it just conceded for claims 1/26.
- **Fix (per jurisdiction fence — label or narrow, never hedge):** label the ranking as the
  essay's structural inference (e.g., "on claim structure alone, the best candidate of the
  four to survive") or narrow to the comparative fact it actually is (most structurally
  specific of the four independents). Do NOT add outcome disclaimers — the firm verdict
  itself needs no softening.

### sa1B-F2 — low — check 4 (claim attribution, narrower-claim fix)

- **Span:** "Claims 11 to 13, as drafted, add auxiliary circuitry … **The same claims** then
  draw a boundary the arrays cannot cross."
- **Problem:** only claim 13 recites the no-communication boundary; claims 11-12 do not.
- **Fix:** narrow the attribution ("the last of them, claim 13, then draws a boundary…").

### sa1B-F3 — low — check 5 (embodiment elevated to defining feature, label fix)

- **Span:** "One more design choice defines the machine. The combined array 'does not take
  instructions at runtime, and only executes instructions in a preset loop' [0027]."
- **Problem:** [0027] qualifies this "in one embodiment," and no claim recites it; "defines
  the machine" states an unclaimed embodiment as the machine's essence.
- **Fix:** label ("In the described embodiment, the combined array…") — the investor point
  (single-workload commitment) survives intact.

### sa1B-F4 — low — check 2 (header-as-claim overpromise)

- **Span:** header "The Rest of the 2023 Silicon Is Already Transformer-Shaped".
- **Problem:** there is no 2023 silicon; the section is about a filing's disclosed design.
  For an essay whose whole thesis is "the narrative is ahead of the property right," a header
  that converts paper into silicon hands the skeptic a free quote-tweet.
- **Fix:** narrow the header ("The Rest of the 2023 Design…" / "…2023 Filing…").

### sa1B-F5 — low — check 7 (thesis-restatement-redundancy)

- **Spans:** title ("…Still Pending"), §1 ("still not an asset"), §2 ("A patent application
  is not a patent"), §4 bold ("It is claim language Etched has been asking the patent office
  for since May 2023"), §7 ("a roadmap in formation rather than a fence" / "The paper is
  still asking").
- **Problem:** the core verdict is asserted in ~5 sections; pass-7 pass condition is ≤ 3.
  Each restatement carries new material, so this is mild — but the §4 bold line and the §2
  distinction paragraph are the two most cuttable duplicates.
- **Fix:** cut or fold one restatement (candidate: the §4 bolded sentence's second half
  duplicates §2's point).

### sa1B-F6 — low — check 4 (translation narrower than claim, self-correcting)

- **Span:** "In translation, each memory channel is bonded, permanently, to **its own
  column** of the array" vs claim 39's "respective **one or more columns**."
- **Problem:** the plain-terms gloss narrows one-or-more columns to one; the verbatim quote
  two lines later corrects it, so the reader is not left misinformed.
- **Fix:** narrow the gloss ("its own column or columns").

---

## Persona verdict (check 9)

Survives my quote-tweet better than almost any patent-application essay I've read: the
application-era verb discipline is airtight, the collateral beat is portfolio-scoped exactly
as the record supports, and the steelman is a real THIS-application objection conceded at
full strength. The one sentence I'd attack is "As drafted, it is the likeliest survivor among
the application's four independent claims" — my quote-tweet writes itself: "the 'likeliest
survivor' was in the same claim set the examiner finally rejected, and the only novelty
evidence offered is the applicant's own background paragraph."
