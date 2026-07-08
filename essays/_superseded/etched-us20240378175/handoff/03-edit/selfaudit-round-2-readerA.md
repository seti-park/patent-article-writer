# Self-audit round 2 — Reader A (impatient investor)

- essay: handoff/03-edit/essay-final.md (draft_version 4, closing_posture: firm)
- persona: curious retail investor per `_shared/references/reader-profile.md`; saw the
  stealth-exit thread, 6 minutes, headers first, captions before body
- isolation honored: no edit-log, no revision-response/notes, no score-history, no prior
  self-audit reports read
- edition awareness: PENDING APPLICATION analysis; judged on keeping me oriented on
  pending status AND making me care

## Checklist results (evidence-forced)

### 1. BLUF lead-altitude — PASS
Verdict: yes. Para 1 is declarative and carries the call: "Three years on, that document
is still not an asset. It is a pending application, still being argued with a patent
examiner, and pledged alongside the rest of the company's patent stack as loan
collateral." Title is itself the thesis ("...It Is Still Pending."). No deferred question.
Severity: none.

### 2. Header-as-claim — PASS
Verdict: yes. Header-only skim reconstructs the argument: "The Narrative Is Three Years
Ahead of the Property Right" → "Both Founders Put the Bet in Writing in May 2023" →
"Many Small Arrays, Presented to the Host as One" → "The Application Claims a Memory
Interface With No Switch in It" → "The Rest of the 2023 Design Is Already
Transformer-Shaped" → "What Exists Today Is a Rejection, a Pledge, and Ongoing Spend" →
"A Dated Roadmap the Company Keeps Funding, Not Yet a Fence". Every header asserts;
the skim alone gives filing → mechanism → status → verdict. Severity: none.

### 3. Steelman present — PASS
Verdict: yes, and it is a THIS-application objection, not a truism: "What is in writing is
claim scope Etched has sought and failed to obtain for three years. The examination record
lists 8 references, all examiner-cited... The broad combined-array claims, claim 1 and
claim 26 as drafted, sit closest to that art and are exactly the kind of claims that
shrink in it. Three years of prosecution have produced no enforceable claim at all."
Conceded at full strength ("it deserves full strength"), then refined rather than waved
off: "The crowded-field objection survives contact and changes nothing about the date.
Three things stay true however prosecution ends..." Severity: none.

### 4. No meta posturing — PASS with one conditional finding (sa2A-F5, low)
Verdict: body clean. "Now the memory half. Start with what the filing itself calls
typical." is a transitional imperative, not reader-instruction; "the subject of an earlier
analysis" is the one licensed continuity clause. But the trailing "# Footnotes" block is
pipeline-internal meta with no inline referent anywhere in the body: no `[^thread-claims]`,
`[^prosecution-label]`, `[^fig-05-crop]` etc. marker appears in the text, and the notes
cite internal artifacts — "quote chain is thread → input/essay-context.md → essay per
fact-check-log `etched-thread-2026-07`", "per the run's label-sentence budget", "Phase 1
intentionally dropped fig-03 and fig-04", "per figure-selection.md cover note". If this
block survives to the X Articles upload verbatim, a retail reader hits fact-check-log IDs
and phase names — meta-leak plus homework. Finding sa2A-F5, severity **low** (conditional
on the publication path): verify `strip_publication.py`/upload strips the orphan footnote
block; if it does not, this is a cut.

### 5. Jargon as signpost — PASS with one finding (sa2A-F1, low)
Verdict: gloss discipline is unusually good — every load-bearing term gets its one-clause
gloss on first body use: "systolic array" ("a grid of small calculating cells"), HBM ("the
stacked memory chips AI accelerators use"), UCIe ("a chip-to-chip standard"), self-attention
("the step where a model looks back over everything it has generated so far"), final
rejection ("the examiner's formal no"), RCE ("a paid restart that keeps the argument
alive"), security interest ("a lender's collateral claim"), continuation ("the follow-on
application"), independent claims ("the ones that stand on their own"), layer normalization
("a bookkeeping step that rescales values between stages"). Numbers land on owned scales
(laptop storage for 100s of GB; laptop drive per second for 1 TB/s), correctly labeled as
the essay's own in the footnote.

Finding sa2A-F1, severity **low**: `jargon-overdepth`/density in one spot. The FIG. 2
composition paragraph stacks six reference numerals plus a quoted unit no retail reader
owns: "a physical layer that 'supports up to 32 GT/s' [0030]". GT/s is the only un-glossed
unit in the essay, and it sits in the densest paragraph (215, 201, 220, 230, 225, 250,
UCIe, 32 GT/s). The sentence itself then dismisses the detail ("That is a description
preference, not something claim 1 requires as drafted"), so the quoted rate is doing no
argumentative work. Fix: one-clause gloss or cut the rate and keep "high-speed". This
paragraph was my one skim point (see persona verdict).

### 6. No stub / rhythm break — PASS with one tic finding (sa2A-F6, low)
Verdict: no stub. Sections run 3-5 substantial paragraphs each; the two-sentence pivot
("The thread does not cite a patent filing. The filing is still where the checking
starts.") is a deliberate hinge, not a stub.

Finding sa2A-F6, severity **low**: rhythm tic, not stub. "as drafted" appears 9 times
(twice in one paragraph of section 2: "the claims in it can shrink or die... Etched is
seeking these claims, as drafted"; then FIG. 5 caption; "not something claim 1 requires as
drafted"; "Claim 39 of this application, as drafted"; "Claims 7 and 8, as drafted";
"Claims 11 to 13, as drafted"; "claim 1 and claim 26 as drafted"; "carry no AI limitation
as drafted"). The application-era discipline is required by the edition brief and must
stay; the RATE is the finding — by the fourth use it reads as scaffolding. Fix: cut 2-3
instances where the verb already carries pending status ("asks for", "is seeking", "the
application claims").

### 7. Thesis not over-restated — borderline PASS with one finding (sa2A-F7, low)
Verdict: the full verdict shape (roadmap-in-formation, not a fence) is landed in exactly
one section (the closer) plus its header — good. But the component "pending ≠ asset" frame
is asserted in four sections: S1 ("that document is still not an asset. It is a pending
application"), S2 ("A patent application is not a patent... One distinction carries all
the weight"), S6 ("So what is this document, as a thing an investor can price"), and the
closer. S2's distinction paragraph substantially repeats S1 para 1 for this reader; the
new work it does (the verb rule) is one clause, wrapped in a repeat. Finding sa2A-F7,
severity **low**: `thesis-restatement-redundancy`, mild — trim the S2 restatement to its
new content, keep the rest.

### 8. Grounding spot-check — 5+ samples, HOLDS/STRETCHES/BREAKS

Sampled sections: header caption + S3 (mechanism), S4 (memory/claim 39), S5
(transformer), S6/closer (external facts + claim structure). Every quoted span checked
verbatim against `input/patent.md`; claim-scope statements checked against claims 1-42.

| # | Essay span | Patent | Verdict |
|---|---|---|---|
| 1 | Claim 39 blockquote "a separate memory device comprising a plurality of channels where each of the plurality of channels is hardwired to respective one or more columns in the systolic array without any switching element" [0016] | [0016] verbatim, character-exact | **HOLDS** |
| 2 | "mirrored word for word in the filing's own summary" (claim 39 vs [0016]) | Claim 39 reads ", wherein each..."; [0016] reads " where each..." — one word + comma differ | **STRETCHES** (sa2A-F2, low) |
| 3 | "most chips top out at 'floating point systolic arrays with a size of 128×128'" + "it is unreasonable to expect a single chip to interface with 100s of GB of memory used to store parameters and intermediate computation values" [0018] | [0018] verbatim both | **HOLDS** |
| 4 | "Hundreds of gigabytes is the working size of a modern model's parameters... [0018]" | [0018] says the memory stores "parameters AND intermediate computation values"; the parameters-only gloss is essay-derived world knowledge under a [0018]-anchored sentence | **STRETCHES** (sa2A-F3, low) |
| 5 | "adding more rows of chips adds compute without adding memory chips at the top [0039]" | [0039]: "adding more rows of ICs 215 increases the compute power... without having to add more memory chips 305 at the top" (FIG. 3 point, honestly carried in prose per the dropped-figure note) | **HOLDS** |
| 6 | "'can enable the memory chips 305 to transmit more than 1 TB/s of data to each of the ICs' [0040]" with "several memory chips feeding each top-row chip" precondition | [0040] verbatim incl. the multiple-chips precondition; pinned value quoted as the filing's "can enable", not stated as a bound | **HOLDS** |
| 7 | "'does not take instructions at runtime, and only executes instructions in a preset loop' [0027]", scoped "In the embodiment the filing describes" | [0027] verbatim, embodiment scope honored | **HOLDS** |
| 8 | "Identical chips (215) tile a package (201)" | [0028]: "In one embodiment, the ICs 215 are all identical" — embodiment condition dropped in a paragraph otherwise describing the embodiment | **STRETCHES** (sa2A-F4, low) |
| 9 | Switch-is-typical blockquote [0043]; "'can be directly wired (or hardwired) to a particular column' [0044]"; "'hardwiring the memory chips 505 to the columns 515 is permissible' [0045]"; "'which can save space and power' [0045]"; header-caption channel→column mapping 510A-D → 515A-D [0044] | All verbatim / mapping matches [0044] exactly (515A↔510A/505A, 515B↔510B/505A, 515C↔510C/505B, 515D↔510D/505B) | **HOLDS** |
| 10 | "The 2023 filing books the gain as space and power [0045]. Latency is the word the 2026 thread added." | "latency" appears nowhere in the patent text; [0045] says "save space and power" — the contrast is grounded | **HOLDS** |
| 11 | Claims family: "Claims 7 and 8, as drafted, put HBMs on that same switchless hardwiring, several of them per top-row chip"; "Claim 15 frames the system version... memory chips, coupled to the ICs forming the top row, store the model's weights [0014]"; "Claims 11 to 13... auxiliary circuitry (605)... local memory chips (610)"; [0051] blockquote; "four independent claims" | Claims 7/8, 15/[0014], 11-13 match as described; [0051] blockquote verbatim; independents are exactly 1, 15, 26, 39 | **HOLDS** |
| 12 | "The broad combined-array claims carry no AI limitation as drafted, and neither does claim 39's memory interface" | Claims 1, 26, 39 recite no AI limitation (AI enters at dependents 6, 12, 31, 40 and independent 15) | **HOLDS** |
| 13 | External facts: lien 1 (2024-04-19, 067204/0877, four applications incl. two rejected compiler filings), lien 2 (2025-07-18, 071792/0869, incl. granted trio), grants 2025-07-15 "three days earlier" labeled inference, "8 references, all examiner-cited", one-sentence prosecution label "As of the 2026-05 record..." | All match essay-context.md tiers, evidence labels honored ("bibliographic observation", "an inference, not a record"), lien discipline honored ("blanket over the portfolio... say nothing about this application in particular") | **HOLDS** |

No BREAKS. Three mild STRETCHES, all low, all fixable by narrow/cut (jurisdiction fence
honored — no hedges recommended):

- **sa2A-F2** (low): "mirrored word for word" overstates textual identity by one word
  (wherein/where). Fix: narrow — "mirrored nearly word for word" or cut "word for word"
  ("mirrored in the filing's own summary").
- **sa2A-F3** (low): parameters-only gloss narrows [0018]'s "parameters and intermediate
  computation values". Fix: narrow the gloss ("a modern model's parameters and working
  values") or move the [0018] anchor so it covers only the paraphrase clause.
- **sa2A-F4** (low): "Identical chips" states an "In one embodiment" fact unconditionally.
  Fix: narrow ("identical chips, in the layout the filing describes") — cheap, since the
  sentence already opens "The application's answer is composition."

Claim-scope map check: nothing described as locked; sought/as-drafted language throughout;
"one or more columns" of claim 39 honored ("its own column or columns"); no enforceability
language ("no enforceable claim at all" and "before anything becomes enforceable" assert
non-enforceability, which is correct for a pending application).

### 9. Persona verdict + over-hedge symmetric check

**Stop-point:** none reached. One skim: the FIG. 2 composition paragraph (the six part
numbers + UCIe + 32 GT/s stretch — see sa2A-F1). I re-engaged at "One more choice marks
how single-minded the machine is meant to be" because it named the investor-relevant fact
in so many words.

**Pending-orientation:** never lost it. Title, S1, and every claim discussion kept the
"sought, not owned" frame live without ever using it to dodge the call (see below). The
cost of that orientation is the "as drafted" tic (sa2A-F6), not confusion.

**Leaving question:** "If claim 39 grants in some form, who does it actually block — does
anyone else wire HBM channels straight to array columns, or is a design-around trivial?"
That is a next-essay question, not a hole in this one; the essay's own falsifier ("The
paid restart has put the claims back in front of the examiner, and that process ends one
of two ways") is on the page.

**Share: YES.** The header image plus the kicker — "The racks are shipping, the company
says. The paper is still asking." — is the tweet.

**Over-hedge symmetric check (6G): PASS, no finding.**
- The call leads and is not qualifier-wrapped: "Hold the July 2026 thread against the May
  2023 filing and the verdict is firm. This document is the origin record of Etched's
  architecture bet... Priced today, it is a roadmap in formation rather than a fence."
- Exactly ONE anti-hype guard, patent-specific, and self-labeled as such: "The one guard
  the evidence forces is just as specific: broad claim 1... is the part of this filing
  likeliest to shrink or die."
- **Pending-status-as-crutch: ABSENT.** The closer does not retreat into "it's only an
  application, so who knows." It prices affirmatively (origin record + ongoing spend +
  collateralized + "does not yet own anything in it"), names a best-survivor claim with
  its basis labeled ("On claim structure alone, it is the best candidate to survive in
  some form"), and states three prosecution-independent facts ("the filing date stays 10
  May 2023, the named inventors stay the two founders, and the content stays the
  switchless channel-to-column interface, which no rejection can un-write").
- No generic patent truism appears anywhere as steelman or hedge; the required labels
  ("an inference, not a record", "proves nothing by itself about intent") are evidence
  discipline, not verdict softening — the conclusion is not safer than the body's
  evidence, it is exactly the body's evidence.

## Finding summary

| id | check | class | severity | verdict |
|---|---|---|---|---|
| sa2A-F1 | 5 | jargon-overdepth / density | low | un-glossed "32 GT/s" in the densest part-number paragraph; the rate does no work |
| sa2A-F2 | 8 | grounding-stretch | low | "mirrored word for word" — claim 39 vs [0016] differ by wherein/where; narrow or cut |
| sa2A-F3 | 8 | grounding-stretch | low | parameters-only gloss narrows [0018]'s "parameters and intermediate computation values"; narrow |
| sa2A-F4 | 8 | grounding-stretch | low | "Identical chips" drops [0028]'s "In one embodiment"; narrow |
| sa2A-F5 | 4 | meta-reader-instruction (conditional) | low | orphan Footnotes block cites fact-check-log/essay-context/Phase 1; confirm stripped before publication, else cut |
| sa2A-F6 | 6 | rhythm tic | low | "as drafted" x9; cut 2-3 where the verb already carries pending status |
| sa2A-F7 | 7 | thesis-restatement-redundancy | low | pending≠asset frame in 4 sections; S2 paragraph repeats S1 para 1 |

Counts: critical 0 · high 0 · medium 0 · low 7. No hard-gate implicated. Round is dry at
the medium+ bar from this reader.
