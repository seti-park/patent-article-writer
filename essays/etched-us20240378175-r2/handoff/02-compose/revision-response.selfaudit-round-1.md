# Revision response — post-acceptance self-audit, round 1

draft_version: 4  <!-- the version this revision produced; revises the ACCEPTED v3 -->

Sources for this revision: the four self-audit reports (readerA, readerB, grounding,
coldreader — quoted evidence only), fact-check-log.md, invention-summary.md quote-anchor
rows, edit-log.round-3.md (deferred r3-F1), and direct inspection of input/figures/fig-03.png.
input/patent.md not read (source fence held). Orchestrator multi-vote rulings adopted as
noted per finding.

## sa1A-F01 (medium) = sa1B-F1 (high) — unsupported venue: "on stage" / "keynote" / "stage version"

- disposition: applied (converged pair; grounding-verified against fact-check-log)
- change: All six occurrences narrowed to the venue the run's fact base records (the
  stealth-exit thread / the pitch), keeping the discovery register's energy:
  1. Cover caption: "Etched pitched this as its no-layer memory philosophy in its
     stealth-exit thread in late June 2026." (also carries the date fix, see sa1G-F1)
  2. §1 ¶1 s1: "on stage" dropped — "Three years before Etched pitched \"the best layer is
     no layer\" as its memory philosophy, both of its co-founders had signed that idea into
     the company's very first patent filing." Beat still starts at word one.
  3. §1 ¶1 s3: "The stage version arrived in July 2026" → "The public version arrived in
     late June 2026" (public/written parallel preserved against signature line 1).
  4. §6 ¶2: "The one thing the stage cannot do" → "The one thing the pitch cannot do"
     (reader B's own proposed fix; sentence shape kept).
  5. §6 ¶3: "The place to watch is not the keynote but" → "not the thread but" (the thread
     is the established, logged referent; docket contrast intact).
  6. Signature line 3 (factual accuracy overrides signature protection per
     reader-energy.md §5): "On stage the layer is already gone." → "In the pitch the layer
     is already gone." Second sentence ("At the patent office, Etched is still paying to
     own the deletion.") byte-identical; two-clause architecture, parallel prepositional
     openings, and present-tense contrast preserved. Updated exact string declared in
     thesis-trace.md ## Signature lines.
- upstream fix (revision-mode "fix at the source"): thesis-spine.md one-liner "pitched it
  on stage" corrected in place to "pitched it in its stealth-exit thread" with a one-line
  erratum (origin: sa1B-F1); matching erratum note added at the top of
  title-lead-candidates.md (candidates themselves preserved as written).
- bookkeeping: figures-rationale.md caption-as-written synced; thesis-trace deviation 6
  records the campaign.
- location: cover caption; §1 ¶1 (×2); §6 ¶2; §6 ¶3 (×2 incl. signature line 3)

## sa1G-F1 (medium) = sa1B-F5 (low) — pitch month "July 2026" contradicts the essay's own cited source (30 June 2026)

- disposition: applied
- change: Both dated mentions aligned to the logged source (TechCrunch coverage,
  30 June 2026): cover caption and §1 ¶1 now say "late June 2026". "First racks shipping
  in the summer" (§1 ¶2) and "Racks shipping this summer" (§6 ¶2) unchanged — that is the
  thread's own claim wording per fact `thread-claims-2026-07`. Three-years arithmetic
  re-checked after the change: 10 May 2023 → late June 2026 = 3 years + ~7 weeks, so every
  "three years" instance (§1 ¶1 ×2 incl. signature line 1, §1 ¶3, §2 ¶1, §3 ¶7) remains a
  fair round; none touched. No other "July 2026" instance exists in the draft (grep zero).
- location: cover caption; §1 ¶1 s3

## r3-F1 (low, deferred inner-loop) — unglossed "cited art" in the verdict guard

- disposition: applied
- change: Round-3 reviewer's option (b) noun swap, everything else byte-identical:
  "That question gets decided against the examiner's cited art, nowhere else." → "That
  question gets decided against the examiner's citations, nowhere else." Back-references
  §5 ¶2's "The examiner has assembled eight references" without a gloss clause in the
  verdict; "nowhere else" untouched; no venue phrase reintroduced; signature line 3
  untouched by this edit; sentence stays 10 words, declarative.
- location: §6 ¶2, last sentence

## Cold-reader drag point (§4 schedule paragraph) + reader A slowest-section note — corroborated pair

- disposition: applied
- change: §4 ¶5 lightened, anchors and verbatim quotes kept. Sentence 1 now leads with the
  plain-words why ("One attention step alone, computing the queries, means the data
  'passes through the systolic array three times' [0055]." — even one step is three trips,
  so keeping the array busy is real homework); sentence 2 names the answer before the spec
  words ("The answer is overlap: inputs for the next computation are fed in 'before the
  previous computation completes' [0056]." — supported by q-0056-1's to-achieve-efficiency
  framing). The paragraph now reads problem → answer → residual stall → payoff; the
  investor cash-out sentences ("A document that only wanted to impress ... budgeted its
  idle cycles.") that pulled the cold reader back are untouched. Sentence count unchanged
  (5); quotes remain substrings of q-0055-1/q-0056-1.
- location: §4 ¶5

## sa1A-F02 (low) — "in batches" carried by [0053] alone

- disposition: applied
- change: Composite anchor: "pushing a transformer layer through in batches [0053],
  [0055]" — [0053] carries the one-row/one-layer chart, [0055] the batching, matching
  invention-summary's own pipelining row (batches anchored `[0055]`+).
- location: §4 ¶4

## sa1A-F03 (low) — [0057]'s may-outcome rendered as held state

- disposition: applied
- change: "the array holds 'a 98% or greater utilization'" → "the array can still hold
  'a 98% or greater utilization'" — restores q-0057-2's modality ("may be small ... and
  still result in") while keeping the number and the quote.
- location: §4 ¶5, sentence 3

## sa1A-F04 (low) — "the background" mislabels detailed-description paragraphs

- disposition: applied
- change: Both labels narrowed per the finding's own suggestions: §2 "The background gives
  two reasons" → "The filing gives two reasons" ([0018] sits in the description); §3 "the
  background is candid" → "the description is candid" ([0043] likewise). Anchors and
  quotes unchanged.
- location: §2 ¶1 s3; §3 ¶1

## sa1B-F4 (low) — identical chips generalized from an embodiment ("deliberately interchangeable")

- disposition: applied
- change: §2 header kept per the round-1 in-loop ruling (not reopened). Body now labels
  identical-chips as the described embodiment and drops the intent-reading adverb: "The
  chips are deliberately interchangeable:" → "In a version the filing describes, the chips
  are all interchangeable:" — the prose label now mirrors the quote's own "In one
  embodiment" instead of asserting design intent as fact. Quote and follow-on sentence
  unchanged.
- location: §2 ¶5

## sa1B-F3 (low) — "describe the same absence" asserts identity on company framing

- disposition: applied
- change: Reader B's proposed verb: "The pitch and the claims name the same absence" —
  rhyme kept, identity claim narrowed; the rest of the sentence (including "this document
  is where the absence has a date") unchanged.
- location: §3 ¶7

## sa1G-F2 (low) — feature-film analogy assumes an unlogged file size

- disposition: applied (log option chosen over cut — the analogy serves reader-profile's
  familiar-scale rule and both readers cleared it as owned arithmetic)
- change: Logged in fact-check-log.md under a new "Derived comparisons (essay-own
  arithmetic)" section: film-per-5ms — 1 TB/s × 5 ms = 5 GB ≈ one HD feature-film file;
  origin sa1G-F2. Essay text unchanged: "by the description's own numbers" already scopes
  the patent's 1 TB/s figure, and the log entry now records the film conversion as the
  essay's own arithmetic. (A volunteered sentence-split marking the conversion in-text was
  drafted, then reverted: the naive STRUCT-001 splitter counts the sentence-final "FIG. 3
  ... FIG. 4 ..." tokens as boundaries, and the extra sentence pushed §3 ¶6 to a
  splitter-count of 8 — a warn round 3 did not have. The log alone satisfies the finding's
  fix options.)
- location: handoff/01-design/fact-check-log.md (essay text unchanged)

## sa1G-F3 (low) — "a property the later pitch leaned on" connects [0024] to the pitch without a logged source

- disposition: applied
- change: Narrowed to description-only framing per the verifier's fix class: "plus a
  property the later pitch leaned on:" → "plus a property the description spells out:" —
  [0024] states the dual-computation capability explicitly (q-0024-1 "can perform
  different operations ... simultaneously"); the unlogged pitch connection is gone.
- location: §2 ¶2 s4

## sa1G-F4 (low) — "the model family the document aims at" overstates [0003]'s "e.g." hedge

- disposition: applied
- change: Verifier's recommended narrow: "Transformers, the model family the document uses
  as its running example [0003]" — defensible per the verifier's own note that
  [0047]-[0057] are transformer-specific; the singular-aim assertion is gone.
- location: §4 ¶2 s1

## sa1A-F05 (low) — forward-pointer "a detail that matters later"

- disposition: rejected
- justification: Single-reader taste with an explicit counter-vote: reader B's pass-4 check
  judged the same clause "a three-word forward signpost, cohesion not posturing", and the
  round-3 pass-5 review verified the promise pays off in §3 ("§2 ¶2's 'a detail that
  matters later' promise pays off in §3 ¶3"). Reader A themselves marked it borderline and
  conditioned the fix on peer concurrence, which did not arrive. Multi-vote threshold not
  met; no factual defect.

## sa1A-F06 (low) — FIG. 3 "six memory chips" count

- disposition: rejected (verified before ruling, per the orchestrator's condition)
- justification: Re-inspected input/figures/fig-03.png directly this revision: the drawing
  shows exactly six labeled memory-chip boxes (305A-305F), two per top-row IC, with
  ellipsis dots between pairs. The essay sentence — "FIG. 3 draws the square-grid version
  with six memory chips across the top" — is a statement about what the drawing draws, and
  it draws six; the caption ("multiple memory chips (305) feed each top-row chip") already
  carries the open-ended reading. Reader B's independent image check reached the same
  verdict ("matches the six drawn boxes (ellipses permit more — not contradicted)"), as
  did the grounding verifier (FC4 SUPPORTED). Not trivially wrong; not applied.

## sa1B-F2 (low) — claim-1 translations wear the embodiment's magnitude ("giant"/"enormous")

- disposition: rejected
- justification: The reviewer's own fix line offers "or leave as-is; the §5 correction
  already exists" — the essay's steelman states the drafted floor at full strength
  ("Claim 1, as drafted, reads on more or less any multi-chip systolic-array package"),
  and the grounding verifier passed both sentences (M1/M2 SUPPORTED, "magnitude adjectives
  are the drawings'/description's"). Not in the orchestrator's apply or sweep lists.
  De-scaling ¶1's hook sentence would trade verified color for no grounding gain.

## Cold reader — claim-39 blockquote skim

- disposition: rejected (contract element)
- justification: The skim is the translate-then-quote device working as designed
  (reader-profile rule 3): the reader jumped to the bold line "which told me what the
  quote meant anyway" — the translation precedes the blockquote precisely so skipping the
  legal text costs nothing. Uncorroborated as a defect by any checklist reader.

## Cold reader — reel/frame numeral glaze

- disposition: rejected (contract element)
- justification: Reel/frame precision is edition-mandated collateral discipline
  (fact-check-log Notes; both-or-neither rule) and the cold reader kept reading the
  sentences around the numbers. Registry-checkability is the point of the parentheticals;
  uncorroborated by the checklist readers.

## Volunteered changes (beyond findings)

- None. Every edit above traces to a finding_id or the corroborated cold-reader drag
  point; bookkeeping syncs (thesis-trace signature-line declaration + deviation 6 +
  §6 guard parenthetical, figures-rationale caption record) follow revision-mode step 4.

## Recount after structural edits

- No structural edit survives into v4 (the one volunteered split was reverted, see
  sa1G-F2); every edited paragraph keeps its v3 sentence count (§1 ¶1: 4; §2 ¶1: 6;
  §2 ¶2: 4; §2 ¶5: 2 quote-follower unit unchanged; §3 ¶6: 5; §3 ¶7: 7, band edge as
  previously accepted; §4 ¶2: 4; §4 ¶4: 3; §4 ¶5: 5; §6 ¶2: 3; §6 ¶3: 6). Figure tokens
  re-checked: FIG. 1/2/3/5/6/7 all still referenced in prose/captions; FIG. 4 still
  prose-only per the locked pair-break; fig-05 embed untouched.
