# Revision notes — etched-0378175-memory-in-writing-r2

> Post-acceptance self-audit deltas (round 1). All blocks below: **origin:
> self-post-accept** (normalize with `meta/normalize_revision_notes.py --origin
> self-post-accept`). The inner loop accepted draft_version 3 (double-clean, rounds 3-4);
> the self-audit round-1 reports (readerA, readerB, grounding, coldreader) produced
> draft_version 4 via composer revision mode
> (`handoff/02-compose/revision-response.selfaudit-round-1.md` holds the full
> dispositions). Classes without an attribution-table row are flagged inline per the
> template ("Unknown classes flag for a new attribution-table row").

## delta
class: unsourced-scene-detail
round: selfaudit-1
before: the 2026 pitch staged as a live event on five prose/caption surfaces ("pitched this on stage", "The stage version arrived", "the one thing the stage cannot do", "not the keynote but", cover caption "on stage")
after: venue narrowed to the record's actual object — the pitch / the stealth-exit thread ("pitched this ... in its stealth-exit thread", "The public version arrived", "the one thing the pitch cannot do", "not the thread but")
rationale: sa1A-F01+sa1B-F1 (converged medium/high): the run's only source for the 2026 moment is a thread (fact thread-claims-2026-07); no stage/keynote event exists in evidence — an upstream spine injection ("pitched it on stage") every inner-loop pass inherited; spine + title-lead-candidates errata added at the source. NEW CLASS — flag for attribution-table row (owner: design/thesis-spine; goal 1).

## delta
class: unsourced-scene-detail
round: selfaudit-1
before: signature line 3 "On stage the layer is already gone. At the patent office, Etched is still paying to own the deletion."
after: signature line 3 "In the pitch the layer is already gone. At the patent office, Etched is still paying to own the deletion."
rationale: factual accuracy overrides signature protection (reader-energy.md §5); two-clause architecture, parallel prepositional openings, and the byte-identical second sentence keep the landing's contrast punch; updated exact string declared in thesis-trace ## Signature lines.

## delta
class: source-date-mismatch
round: selfaudit-1
before: pitch dated "July 2026" (cover caption + §1 ¶1) while the essay's own Sources line dates the sole source "TechCrunch, Etched stealth-exit coverage (30 June 2026)"
after: both mentions read "late June 2026"; the thread's own "summer" wording for the racks claim kept; all "three years" arithmetic re-verified valid (May 2023 → June 2026)
rationale: sa1G-F1+sa1B-F5: coverage cannot predate its subject by a month; align the body to the logged source date rather than the fact-row's inherited month label. NEW CLASS — flag for attribution-table row (owner: design/fact-check-log date discipline; goal 1).

## delta
class: jargon-gloss-gap
round: selfaudit-1
before: "That question gets decided against the examiner's cited art, nowhere else." ("art" the draft's one unglossed term of art, first use in the verdict)
after: "That question gets decided against the examiner's citations, nowhere else."
rationale: r3-F1 (deferred inner-loop low): round-3 reviewer's option (b) noun swap — back-references §5's "eight references" in plain English with no gloss clause added to the verdict and "nowhere else" untouched.

## delta
class: reader-engagement-break
round: selfaudit-1
before: "Computing attention queries means the data 'passes through the systolic array three times' [0055]. Inputs for the next computation are fed in 'before the previous computation completes' [0056]." (cold reader's one real attention drop; reader A's slowest stretch)
after: "One attention step alone, computing the queries, means the data 'passes through the systolic array three times' [0055]. The answer is overlap: inputs for the next computation are fed in 'before the previous computation completes' [0056]."
rationale: corroborated drag point — lead with the plain-words why (one step = three trips) and name the answer (overlap) before the spec words, so the schedule paragraph reads problem→answer→stall→payoff; anchors and verbatim quotes kept; the cash-out landing untouched.

## delta
class: anchor-under-coverage
round: selfaudit-1
before: "pushing a transformer layer through in batches [0053]"
after: "pushing a transformer layer through in batches [0053], [0055]"
rationale: sa1A-F02: [0053] covers one row/one layer; batching is [0055] content — composite anchor matches invention-summary's own pipelining row.

## delta
class: option-embodiment-upgraded
round: selfaudit-1
before: "even with that stall the array holds 'a 98% or greater utilization' [0057]"
after: "even with that stall the array can still hold 'a 98% or greater utilization' [0057]"
rationale: sa1A-F03: q-0057-2 is a may-outcome ("may be small ... and still result in"), not a held state; "can still hold" restores the source's modality, keeps the number.

## delta
class: document-section-mislabel
round: selfaudit-1
before: "The background gives two reasons why anyone would bother." [0018]; "the background is candid about how the industry handles it" [0043]
after: "The filing gives two reasons why anyone would bother."; "the description is candid about how the industry handles it"
rationale: sa1A-F04: the Background section is [0002]-[0003]; [0018] and [0043] live in the detailed description — labels narrowed, anchors and quotes unchanged. NEW CLASS — flag for attribution-table row (owner: compose/citation-format; goal 1).

## delta
class: option-embodiment-upgraded
round: selfaudit-1
before: "The chips are deliberately interchangeable: 'In one embodiment, the ICs 215 are all identical.' [0028]"
after: "In a version the filing describes, the chips are all interchangeable: 'In one embodiment, the ICs 215 are all identical.' [0028]"
rationale: sa1B-F4: identicality is an embodiment sentence in no claim, and "deliberately" read intent into it — prose now carries the described-embodiment label itself; §2 header kept per the round-1 in-loop ruling.

## delta
class: evidence-scope-overreach
round: selfaudit-1
before: "The pitch and the claims describe the same absence"
after: "The pitch and the claims name the same absence"
rationale: sa1B-F3: a cluster-scale memory pillar and a package-internal channel-to-column hardwire are cousins, not an identity — one verb closes the gap, same energy, scope honest.

## delta
class: fact-introduced-beyond-spans
round: selfaudit-1
before: "about a feature film's worth of data every five thousandths of a second" rode the ">1 TB/s" [0040] sentence with no log entry for the assumed film-file size
after: essay text unchanged; fact-check-log gains a "Derived comparisons (essay-own arithmetic)" entry film-per-5ms (1 TB/s × 5 ms = 5 GB ≈ one HD feature film, origin sa1G-F2)
rationale: sa1G-F2, log option over cut: the analogy serves reader-profile's familiar-scale rule and both readers cleared the arithmetic; the derivation is now on the record. (An in-text "Call that ..." split was drafted then reverted — it tripped STRUCT-001's naive splitter on the paragraph's "FIG. 3 ... FIG. 4" tokens.)

## delta
class: evidence-scope-overreach
round: selfaudit-1
before: "FIG. 1 shows the shape, plus a property the later pitch leaned on:"
after: "FIG. 1 shows the shape, plus a property the description spells out:"
rationale: sa1G-F3: no logged thread fact claims the dual-computation property; connection narrowed to what [0024] itself states (q-0024-1 "can perform different operations ... simultaneously").

## delta
class: paraphrase-hedge-compression
round: selfaudit-1
before: "Transformers, the model family the document aims at [0003]"
after: "Transformers, the model family the document uses as its running example [0003]"
rationale: sa1G-F4: [0003] says "e.g., transformer models" as one example of many AI applications and [0019] extends scope further — "running example" is the verifier's own defensible narrow given [0047]-[0057]'s transformer focus.

## considered-not-applied

- **sa1A-F05** (low, forward-pointer "a detail that matters later"): single-reader taste;
  reader B judged the same clause functional cohesion, round-3 pass-5 verified the payoff
  lands in §3 ¶3, and reader A conditioned the fix on peer concurrence that did not arrive.
- **sa1A-F06** (low, FIG. 3 "six memory chips"): verified against fig-03.png before ruling —
  the drawing draws exactly six labeled chips (305A-F, ellipses marking room for more), so
  "FIG. 3 draws ... with six memory chips across the top" is literally true; reader B and
  the grounding verifier independently passed the same sentence. Not trivially wrong.
- **sa1B-F2** (low, "giant"/"enormous" claim-1 color): the reviewer's own leave-as-is option
  taken — the §5 steelman states the drafted floor at full strength and the grounding
  verifier passed both sentences (M1/M2 SUPPORTED).
- **Cold reader: claim-39 blockquote skim**: the translate-then-quote contract working as
  designed — the reader's own account says the bold line "told me what the quote meant
  anyway"; uncorroborated as a defect.
- **Cold reader: reel/frame numeral glaze**: edition-mandated registry precision
  (collateral discipline, both-or-neither rule); the surrounding sentences were read;
  uncorroborated as a defect.

---

> Post-acceptance self-audit deltas (round 2, dry-check follow-up). All blocks below:
> **origin: self-post-accept**. Round-2 reports (readerA, readerB, coldreader; grounding
> ZERO findings) produced draft_version 5 via composer revision mode
> (`handoff/02-compose/revision-response.selfaudit-round-2.md` holds the full
> dispositions). Surgical round: two mediums (multi-vote accepted) + cheap lows.

## delta
class: evidence-scope-overreach
round: selfaudit-2
before: verdict sentence "The no-switch idea is authentically the founders' own, written into claim language before there was anything to sell." ("own" ambiguous between authorship, proven, and originality, which §5 expressly leaves open)
after: "The no-switch idea is authentically the founders' own writing, in claim language before there was anything to sell." (bound to authorship; firm register kept, no qualifier added)
rationale: sa2B-F1 (medium, multi-vote accepted): read as originality the sentence asserts what the steelman concedes is undecided ("The patent office decides whether early also meant original") — one-word-scale narrow per reader B's fix direction, not a hedge.

## delta
class: unsupported-exhaustive-count
round: selfaudit-2
before: three spans implied the company has exactly two founders ("both of its co-founders" §1 ¶1; "Gavin Uberti and Christopher Zhu, the two founders" §1 ¶2; "10 May 2023, both founders" §5 ¶4)
after: count-safe phrasing on all three ("two of its co-founders"; "co-founders Gavin Uberti and Christopher Zhu"; "10 May 2023, co-founders Uberti and Zhu") — hook rhythm and discovery beat intact
rationale: sa2B-F2 (medium, multi-vote accepted): the fact base establishes only that the two inventors ARE co-founders, never an exhaustive founder count; upstream spine spans corrected in place with erratum (thesis-spine.md, origin sa2B-F2); root phrasing in input/essay-context.md (user-owned) flagged. NEW CLASS — flag for attribution-table row (owner: design/essay-context intake; goal 1).

## delta
class: option-embodiment-upgraded
round: selfaudit-2
before: "The combined array 'does not take instructions at runtime, and only executes instructions in a preset loop' [0027]." ([0027]'s "in one embodiment" qualifier dropped)
after: "In one version it describes, the combined array 'does not take instructions at runtime, and only executes instructions in a preset loop' [0027]."
rationale: sa2B-F3: same class as round 1's [0028] fix — the prose now carries the described-embodiment label itself, consistent with the care shown at [0028]; quote and anchor untouched.

## delta
class: ambiguous-referent
round: selfaudit-2
before: "The public version arrived in late June 2026" ("public version" collides with the application's own publication event, Sources "published 2024-11-14")
after: "The public pitch arrived in late June 2026" (noun binds only to the thread pitch; signature line 1 byte-identical)
rationale: sa2A-F1: a date-checking reader can bind "public version" to the patent publication and stumble on "The written version is three years older" — one-word binding fix, reader A's own suggestion. NEW CLASS — flag for attribution-table row (owner: compose; goal 3).

## delta
class: jargon-gloss-gap
round: selfaudit-2
before: three terms of art un-glossed on first use — "The tensor being processed streams in from the left"; "Google's TPU ran its floating-point matrix units"; "computing the queries" (§4 [0055] sentence, also the cold reader's recurring drag)
after: "The data being processed, the tensor, streams in from the left"; "Google's in-house AI chip, the TPU, ran its floating-point matrix units"; "computing what the filing calls query values"
rationale: sa2A-F2 (a/b/c) + cold-reader corroboration on (a) tensor and (c) the [0055] stall; (c) uses [0055]'s own "query values" vocabulary as naming attribution because a semantic gloss would exceed the run's evidence and a trim would un-scope the three-passes claim; (b)'s host sentence split at its colon to stay under the LONGSENT-001 threshold the gloss would otherwise cross (§2 ¶1 now 7 sentences, in band).

## delta
class: meta-forward-promise
round: selfaudit-2
before: "and the filing notes they may be constants, a detail that matters later [0021]" (the essay's only self-referential forward-promise)
after: "and the filing notes they may be constants [0021]" (the §3 payoff at [0045]/[0035] lands without the IOU)
rationale: sa2A-F3, reversing round 1's sa1A-F05 rejection: second independent reader-A instance to flag it, this round unconditionally, with no round-2 defense; five-word cut leaves the essay with zero self-reference. NEW CLASS — flag for attribution-table row (owner: compose; goal 4).

## delta
class: phrase-echo
round: selfaudit-2
before: triple "signed ... statement" construction in the final stretch (§5 ¶4, §6 ¶1, §6 ¶3)
after: third instance varied — "the earliest signed statement of the bet" → "the earliest signed record of the bet"; §5 introduction and §6 ¶1 verdict core kept as a deliberate two-beat callback
rationale: sa2A-F4 (not VOID — spans are not declared signature lines): break the triple at the least load-bearing site; the verdict's legal contrast ("a dated, signed statement ..., not an exclusive right to it") is not reworded for echo. NEW CLASS — flag for attribution-table row (owner: compose; goal 4).

## considered-not-applied (round 2)

- **sa2A-F5** (low, "Intel, IBM and Rambus among the assignees" beyond the brief's list):
  verification path satisfied — fact-check-log `examiner-art-8refs` carries "assignees
  include Intel, IBM, Rambus, ETRI" (tier-1, registry-extract); round-2 grounding E10
  independently verified the clause SUPPORTED and correctly non-exhaustive. The gap was
  reader A's visibility (blind protocol excluded the log), not the essay's grounding.
- **sa2B-F4** (low, §2 header carries the identical-chips embodiment): reader B's own
  "none required if the body scoping is judged sufficient" option taken — the body scopes
  it in-section; round-1 in-loop ruling kept the header; not reopened.
- **sa2B-F5** (low, wiring-half continuity two sentences vs "one clause"): declared
  composer deviation 4 in thesis-trace; B recorded it for the multi-vote only, "no reader
  harm found"; the second sentence carries the brief's pairs-with-does-not-repeat absence
  claim.
- **sa2B-F6** (low, Sources line credits Google Patents for WIPS/DOCDB-supplied dates):
  outside the orchestrator's round-2 sweep; the Sources line names the record systems with
  the reader-followable access path, and the full provenance chain is on the record in
  fact-check-log `prosecution-record`. Flagged as a cheap available fix (one appended
  clause) if Sources-block provenance precision is wanted.
- **Cold reader: §4 scheduling-half drag (STRUCTURAL residue; recurrence noted — second
  cold round in a row)**: the cheap touch that existed was applied (the [0055] naming
  attribution, see jargon-gloss-gap delta); the residual drag is the description-only
  utilization content the section exists to carry, rescued in-text by the bet-seriousness
  landing reader A's O-2 independently credited. Deeper cuts trade goal-2 coverage for a
  half-rescued goal-5 point. If a third cold round drags here, the next candidate is
  folding the 98%-utilization sentence into the stall sentence — meta-loop item.
- **Cold reader: "registry note" paragraph glaze (single occurrence)**: judged cheaply per
  the orchestrator — already the short form with both mandated glosses (PCT, continuation)
  and the edition-required observation label, ending on the plain-words payoff; checklist
  readers verified the same paragraph approvingly; no cheap touch keeps the label and the
  glosses. Same logic as round 1's reel/frame ruling.

## Self-audit closure (round 3, 2026-07-04)

self-audit: no unresolved findings at medium+ — round 3 applied nothing (readers A/B dry,
grounding verifier 0 findings across 70 rows, cold-reader repeat-test passed a third time).
DRY within the 3-round cap. Residual lows (sa3A-F1/F2 gloss gaps, sa3B-F1..F5) logged
considered-not-applied with reasons. Non-essay observations for the meta-loop: thesis-spine
one-liner retains a two/three-years slip (erratum'd, never propagated); fact-check-log
`lvi-absent-here` uses a non-canonical evidence_level string.
