# Revision response — post-acceptance self-audit, round 2

draft_version: 5  <!-- the version this revision produced; revises the round-1 output v4 -->

Sources for this revision: the four round-2 self-audit reports (readerA, readerB, grounding,
coldreader — quoted evidence only), fact-check-log.md, thesis-trace.md (signature-line
declarations), thesis-spine.md, essay-context.md. input/patent.md not read (source fence
held). Grounding report: ZERO findings (69/69 rows SUPPORTED) — context only, nothing to
disposition. Orchestrator multi-vote rulings adopted as noted per finding. Surgical round:
two mediums + cheap lows only.

## sa2B-F1 (medium) — verdict wording "authentically the founders' own" ambiguous between authorship and originality

- disposition: applied (orchestrator multi-vote accepted; grounding-class verified)
- change: Bound to authorship per reader B's own fix direction, one-word-scale narrow:
  "The no-switch idea is authentically the founders' own, written into claim language
  before there was anything to sell." → "The no-switch idea is authentically the founders'
  own writing, in claim language before there was anything to sell." — "own writing" claims
  authorship (proven: named inventors, dated filing) and no longer floats toward
  originality, which the essay's own §5 expressly leaves open ("The patent office decides
  whether early also meant original."). Register stays firm and declarative; no qualifier
  added (not a hedge — a narrower claim). Harmonizes with §5's "The founders wrote it down
  early" and the title's "in Writing". Rest of the verdict paragraph byte-identical.
- location: §6 ¶1, sentence 3

## sa2B-F2 (medium) — exhaustive founder-count implication ("both of its co-founders" / "the two founders" / "both founders")

- disposition: applied (orchestrator multi-vote accepted; grounding-class verified), all
  three spans, count-safe phrasing per the orchestrator's fix directions
- change:
  1. §1 ¶1 (hook sentence): "both of its co-founders had signed that idea" → "two of its
     co-founders had signed that idea" — one word; the discovery beat (founders signing the
     idea into the first filing, three years early) and the sentence rhythm are intact;
     "two of its co-founders" no longer asserts the company has exactly two.
  2. §1 ¶2: "the architecture's authors, Gavin Uberti and Christopher Zhu, the two
     founders, as its inventors" → "the architecture's authors, co-founders Gavin Uberti
     and Christopher Zhu, as its inventors" — title-style "co-founders X and Y" asserts
     only that the two named inventors are co-founders.
  3. §5 ¶4: "10 May 2023, both founders." → "10 May 2023, co-founders Uberti and Zhu." —
     the orchestrator's exact suggestion; adds surname recall at the payoff, count-safe.
  The supported fact (essay-context: the two inventors ARE co-founders) is asserted
  everywhere; the unsupported exhaustive count is asserted nowhere. Thesis untouched.
- upstream fix (revision-mode "fix at the source"): thesis-spine.md carried the same
  phrasing in three spots (Q7 hook "by both co-founders"; Mitigation "(2023-05-10, both
  co-founders)"; §2 trace row "(first filing, both co-founders)") — corrected in place to
  "co-founders Uberti and Zhu" with a one-line erratum (origin: sa2B-F2). Root phrasing is
  input/essay-context.md line "both co-founders (Uberti, Zhu) are the inventors"
  (user-owned input, NOT edited) — flagged for the orchestrator / meta-loop.
- location: §1 ¶1 s1; §1 ¶2 last sentence; §5 ¶4 s2

## sa2B-F3 (low) — [0027] "in one embodiment" qualifier dropped

- disposition: applied (orchestrator sweep item)
- change: Labeled like the [0028] treatment (§2's "In a version the filing describes"):
  "The combined array "does not take instructions at runtime..." [0027]." → "In one
  version it describes, the combined array "does not take instructions at runtime..."
  [0027]." — pronoun "it" = the filing (subject of the preceding sentence), avoiding a
  byte-identical echo of §2's label formula. Quote and anchor untouched; the
  description-not-claim sentence that follows still does its separate job. Sentence count
  unchanged (4).
- location: §4 ¶1 s2

## sa2A-F1 (low) — "The public version" collides with the application's own publication event

- disposition: applied (orchestrator sweep item; reader A's own first suggestion)
- change: "The public version arrived in late June 2026" → "The public pitch arrived in
  late June 2026" — the noun now binds only to the thread pitch, so a date-checking reader
  cannot bind it to the Sources line's "published 2024-11-14". Signature line 1 ("The
  written version is three years older...") byte-identical; the pitch/filing contrast
  survives the loss of the version/version parallel.
- location: §1 ¶1 s3

## sa2A-F2 (low) — three un-glossed terms of art (tensor / TPU / queries)

- disposition: applied, all three (orchestrator sweep item; (c) doubles as the cold-reader
  [0055] touch)
- change:
  (a) "The tensor being processed streams in from the left [0021]." → "The data being
  processed, the tensor, streams in from the left [0021]." — reader A's own shape minus
  the em-dashes: plain words first, term named by apposition. (The round-2 cold reader
  independently self-glossed the same word as "numbers" — corroborated gap.)
  (b) "Google's TPU ran its floating-point matrix units at 128×128..." → "Google's
  in-house AI chip, the TPU, ran its floating-point matrix units at 128×128..." —
  functional one-clause gloss (beats expanding the acronym for this reader); fact
  tpu-mxu-128x128 unchanged, gloss restates the cited Google TPU documentation's own
  framing, so no new fact-check-log row needed. The gloss pushed the host sentence to 39
  words (v4 gate result had zero typography findings — self-introduced LONGSENT-001 warn),
  so the sentence was split at its colon: "That ceiling is concrete, and industry-wide.
  Google's in-house AI chip, the TPU, ran..." — both halves under the 35-word threshold;
  §2 ¶1 goes 6 → 7 sentences (STRUCT-001 band is ≥8; gate clean).
  (c) "One attention step alone, computing the queries, means..." → "One attention step
  alone, computing what the filing calls query values, means..." — [0055]'s own vocabulary
  ("to calculate the query values"); the term is now an attributed artifact of the filing,
  not assumed reader knowledge. A semantic gloss of queries (what they do in attention)
  would be an external ML fact beyond the run's evidence — naming attribution is the
  fence-compliant version of A's "gloss or trim" (trim was blocked: dropping "computing
  the queries" would un-scope the three-passes claim that reader A's own sample D verified
  as correctly scoped to the query computation).
- location: §2 ¶2 s3; §2 ¶1 s5; §4 ¶5 s1

## sa2A-F3 (low) — forward-promise "a detail that matters later"

- disposition: applied (reversal of the round-1 sa1A-F05 rejection, reasons recorded)
- change: Clause cut: "...and the filing notes they may be constants, a detail that
  matters later [0021]." → "...and the filing notes they may be constants [0021]." The §3
  payoff ("because the weights parked in those channels are constants that always go to
  the same columns [0045], [0035]") lands without the IOU, as reader A predicted.
- why the reversal: round 1 rejected on "peer concurrence did not arrive" + reader B's
  counter-vote; round 2 is the second independent reader-A instance to flag it, this time
  unconditionally, and no round-2 reader defended it. Two flags vs one stale defense, the
  fix is a five-word deletion, and the essay is left with zero self-reference. Sentence
  count unchanged (clause-level cut).
- location: §2 ¶2 s2

## sa2A-F4 (low) — "signed ... statement" triple echo in the final stretch

- disposition: applied, partially (varied the third instance only)
- change: Not VOID (the three spans are not declared signature lines — checked
  thesis-trace.md ## Signature lines). §6 ¶3 "the earliest signed statement of the bet" →
  "the earliest signed record of the bet". The §5 ¶4 introduction ("A signed, dated
  statement of the architecture...") and the §6 ¶1 verdict core ("a dated, signed
  statement of the memory idea it pitches, not an exclusive right to it") are kept as a
  deliberate two-beat callback — the verdict's precise legal contrast should not be
  reworded for echo, and two instances is a callback, not an echo. Triple broken at the
  cheapest, least load-bearing site.
- location: §6 ¶3 s2

## sa2A-F5 (low) — "Intel, IBM and Rambus among the assignees" exceeds the run brief's tiered list

- disposition: considered-not-applied (verification path satisfied — the anchor exists)
- justification: Reader A's fix direction was "verify the three names against the
  fact-check log / citation record (anchor), or cut the clause". Verified:
  fact-check-log.md `examiner-art-8refs` carries "assignees include Intel, IBM, Rambus,
  ETRI" (tier-1, registry-extract) — the brief's fact 3 omits the names but the log, the
  composer's sanctioned external-fact source, carries them. The round-2 grounding verifier
  independently reached the same verdict (E10 SUPPORTED, "among the assignees" correctly
  non-exhaustive with ETRI omitted without overclaiming). A read only the brief, not the
  log — the gap was in A's visibility, not the essay's grounding. No edit.

## sa2B-F4 (low) — §2 header carries the identical-chips embodiment as headline

- disposition: considered-not-applied
- justification: Reader B's own fix line is "none required if the body scoping is judged
  sufficient" — the body scopes it within the section ("In a version the filing
  describes..."), B bounded the harm, and the header was kept per the round-1 in-loop
  ruling (sa1B-F4 disposition: "not reopened"). Headers are also sanded surface
  (reader-energy.md) absent a factual defect the body fails to correct.

## sa2B-F5 (low) — wiring-half continuity runs two sentences vs the brief's "one clause"

- disposition: considered-not-applied
- justification: Declared composer deviation 4 in thesis-trace.md; reader B recorded it
  "independently for the multi-vote; no reader harm found" and conditioned the fix on the
  budget being enforced, which no round has enforced. The second sentence carries the
  pairs-with-does-not-repeat contract from the brief (the granted record never wrote the
  memory half down) — compressing it into the first sentence would trade a load-bearing
  absence claim for a budget technicality.

## sa2B-F6 (low) — Sources line credits Google Patents for dates the WIPS/DOCDB export supplied

- disposition: considered-not-applied (flagged as a cheap available fix if the
  orchestrator wants Sources-block provenance precision)
- justification: Outside the orchestrator's round-2 sweep list. Substantively: the Sources
  line names the record systems themselves ("USPTO assignment, prosecution and citation
  records") as the source with Google Patents as the reader-followable access path; a
  "DOCDB/WIPS registry export (2026-07-02)" is an internal artifact a reader cannot
  follow, and the full provenance chain (export date, corroboration split) is already on
  the record in fact-check-log.md `prosecution-record`. X Articles Sources favor
  followable links. If applied later, the fix is one appended clause on Sources line 2.

## Cold reader — [0055] schedule sentence drag (second consecutive cold round)

- disposition: applied in part (light naming touch); structural drag
  considered-not-applied with the recurrence noted
- change: The cheap touch that exists without losing the anchor is the sa2A-F2(c) edit
  above — "computing the queries" → "computing what the filing calls query values" —
  which removes the sentence's first stall (insider vocabulary the reader feels expected
  to know). Anchor [0055] and the verbatim quote untouched.
- recurrence note: second cold round in a row to drag on §4's scheduling half. The round-1
  corroborated fix already restructured the paragraph problem→answer→stall→payoff; the
  residual drag is the content itself (utilization homework), which is deliberate:
  description-only material the section exists to carry, rescued in-text by the
  bet-seriousness landing reader A's O-2 independently credited ("budgeted its idle
  cycles"). Cutting deeper would remove the demonstration that the giant array can be kept
  busy — a goal-2 coverage loss to buy a goal-5 point already half-rescued. If a third
  cold round drags here, the structural option (trimming the 98%-utilization sentence into
  the stall sentence) is the next candidate — flagged for the meta-loop.

## Cold reader — "registry note" paragraph drag (single occurrence)

- disposition: considered-not-applied (judged cheaply per the orchestrator)
- justification: Single-reader, single-round, and the reader "got through it" — the
  paragraph is already the short form (4 sentences) with both mandated one-clause glosses
  (PCT, continuation) and the edition-required observation label, and it ends on the
  plain-words payoff ("The filing's family tree is thinner than the trio's"). The
  checklist readers verified the same paragraph approvingly (A sample G; B's external-fact
  fencing table). The glaze is inherent to registry content the edition mandates; no
  cheap touch exists that keeps the label and the glosses. Same logic as the round-1
  reel/frame ruling (registry checkability is the point).

## Grounding report (round 2)

- Zero findings; 69/69 rows SUPPORTED. Nothing to disposition. The three
  lowest-confidence-SUPPORTED notes (R1, C6, R5) request no action and none was taken.

## Volunteered changes (beyond findings)

- None. Every edit above traces to a round-2 finding_id or the corroborated cold-reader
  drag point. Bookkeeping: draft_version 4 → 5; essay-draft.md synced byte-identical to
  essay-final.md; publication.md regenerated via strip pipeline; thesis-spine.md erratum
  (sa2B-F2 upstream); revision-notes.md round-2 delta blocks appended. thesis-trace.md
  unchanged — no declared signature line moved, no anchor set or figure placement moved
  (word_actual drift from clause edits is within the recorded ±20% bands). fact-check-log
  unchanged — no new external fact introduced (the TPU gloss restates the already-logged
  source's framing).

## Recount after structural edits

- One structural edit this round: the §2 ¶1 TPU sentence split at its colon (warn-avoiding
  companion to the sa2A-F2(b) gloss). Post-split recount of every edited/neighboring
  paragraph: §1 ¶1: 4; §1 ¶2: 3; §2 ¶1: 7 (was 6; band is 3-7, STRUCT-001 warns at ≥8);
  §2 ¶2: 4; §4 ¶1: 4; §4 ¶5: 5; §5 ¶4: 6; §6 ¶1: 7; §6 ¶3: 6. All other edits are
  clause-level in place with v4 sentence counts unchanged. Figure tokens re-checked:
  FIG. 1/2/3/5/6/7 all still referenced in prose/captions; FIG. 4 still prose-only per
  the locked pair-break; fig-05 header embed untouched.

## Byte-stability confirmation (title / signature lines / verdict call)

- Title: byte-identical.
- Signature lines 1-3 (thesis-trace declarations): all three byte-identical.
- Verdict call: "The verdict is firm. This document is the real origin of Etched's memory
  story." byte-identical; the §6 ¶2 anti-hype guard byte-identical. Two §6 spans
  legitimately touched by findings: ¶1 s3 (sa2B-F1, the finding's own target) and ¶3
  "signed statement"→"signed record" (sa2A-F4). Nothing else in §6 moved.
