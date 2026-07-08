# Revision response — post-acceptance self-audit round 1

draft_version: 4  <!-- the version this revision produced (v3 -> v4) -->
inputs: selfaudit-round-1-grounding.md (sa1G-F1..F4), selfaudit-round-1-readerA.md
(sa1A-F1..F6), selfaudit-round-1-readerB.md (sa1B-F1..F6); carried lows from acceptance
(r3-F1, r4-F1, r4-F2, r4-F3 per score-history.md).
multi-vote convergences: thesis restatement (sa1A-F1 medium + sa1B-F5 low);
claim-39 gloss narrower than claim text (sa1A-F6 + sa1B-F6, both low).

## sa1G-F1 (medium — MISREAD anchor)

- disposition: applied
- change: Horizontal/vertical connection clause re-anchored: "(230) and vertical connections
  (225) [0029] join neighboring tiles until they compute as one combined systolic array
  (250) [0019]." — [0029] now carries the horizontal/vertical naming (its actual source),
  [0019] keeps only the generic joined-into-one-array clause it supports. [0029] is present
  in the invention-summary reference table (rows 225/230); gate_anchors PASS confirms.
- location: §3, composition paragraph

## sa1G-F2 (medium — unlogged external fact)

- disposition: applied
- change: Cut "open" from "UCIe, an open chip-to-chip standard" -> "UCIe, a chip-to-chip
  standard". The patent-anchored content ("supports up to 32 GT/s" [0030], description
  preference not a claim-1 requirement) stands unchanged; no fact-check-log entry added.
- location: §3, composition paragraph

## sa1A-F1 (medium) + sa1B-F5 (low) — thesis-restatement-redundancy

- disposition: applied
- change: The §4 standalone bolded paragraph (near-verbatim echo of title and §7,
  "not a 2026 slogan... claim language Etched has been asking... since May 2023") is gone as
  a thesis restatement. The section's single inline bold anchor is preserved (a planned spine
  element per thesis-trace, canon: inline-bold-thesis-anchor two-sentence parallel cadence)
  but re-targeted to §4's fresh beat and folded into the bridge paragraph: "**The 2023 filing
  books the gain as space and power [0045]. Latency is the word the 2026 thread added.**"
  Core verdict is now asserted in title + §1 + §2 + §7 = 3 sections, meeting the pass-7
  <= 3-sections condition. Also removes one "not X. It is Y" instance (see r4-F3 below).
- location: §4, bridge paragraph (former bold paragraph deleted; thesis-trace §4 updated)

## sa1A-F2 (medium — grounding, unsupported prior-event implication)

- disposition: applied
- change: "or the set narrows again or dies" -> narrowed by dropping "again" (the cited
  record shows refusals, not a documented narrowing). Follow-up: the fix made §7's phrase a
  verbatim 5-gram duplicate of §6's "If the set narrows or dies" (DUPE-001 warn,
  revision-induced-duplication class), so §7 was varied to "or the claims narrow or die" —
  same supported content, no echo. Verdict unchanged; this is a narrower claim, not a hedge.
- location: §7, closing paragraph

## sa1B-F1 (medium — survivor ranking stated flat in the verdict)

- disposition: applied
- change: "As drafted, it is the likeliest survivor among the application's four independent
  claims..." -> "On claim structure alone, it is the best candidate to survive in some form
  among the application's four independent claims, the ones that stand on their own rather
  than adding to another." This is the finding's label+narrow fix: the ranking is now
  explicitly the essay's structural inference ("on claim structure alone") and restores the
  scope map's own "in some form" qualifier. The map's second caveat (the negative limitation
  "remains examinable") was NOT imported: the verdict section carries exactly one anti-hype
  guard (claim 1) per the closing directive, and a second guard would trade a grounding
  finding for a hedge finding — jurisdiction fence respected. Verdict lead sentence
  ("...the verdict is firm.") untouched; gate_hedge PASS under closing_posture: firm.
- location: §7, claim-39 paragraph (thesis-trace §7 updated)

## sa1G-F3 (low — prosecution fact restated beyond the one-sentence budget)

- disposition: applied
- change: Cut "The examiner has said no once." from the steelman. The rejection already
  reaches the steelman through "sought and failed to obtain for three years" and "Three years
  of prosecution have produced no enforceable claim at all" (analytic reuse, no chronology,
  cleared by both readers); the §6 label sentence remains the fact's single carrier.
- location: §6, steelman paragraph

## sa1G-F4 (low — timing inference beyond the logged fact)

- disposition: applied
- change: "which is to say the field was already crowded when the founders filed" -> "which
  is to say the field is crowded". The at-time-of-filing relationship is not established by
  the logged `examiner-cited-field` fact (the 8 references' own dates are registry-external
  per the invention-summary Timeline note); the present-tense form asserts only what the
  record shows.
- location: §6, steelman paragraph

## sa1A-F3 (low — jargon-gloss gaps)

- disposition: applied (primary items), rejected (secondary items)
- change: (1) "layer normalization" glossed at first body use: "a bookkeeping step that
  rescales values between stages" (one clause, stops at the insight; the FIG. 7 caption use
  now inherits the body gloss). (2) FIG. 2 caption: "the host computer (205) connects over a
  standard PCIe link (240)" (minimal handle for the captions-first reader).
- rejected items + justification: "32 GT/s" sits inside a verbatim patent quote and any
  familiar-scale conversion would be a new derived comparison needing a footnote log entry
  for a value doing no argumentative work; "reel/frame" already functions as a citation and
  is glossed by context ("recorded at USPTO reel/frame..."); the header-caption cold terms
  ("systolic array (220)", "claim 39") are the header composite's topology-first role, and
  the skimmer's very next caption (FIG. 1, expanded under sa1A-F5) now explains what the
  array does. The reader's own report ranks these "secondary, below the flag line on their
  own".
- location: §5 pipelining paragraph; FIG. 2 caption

## sa1A-F4 (low — meta/process leak)

- disposition: applied (phrase); annex confirmed stripped
- change: "The claim language, mirrored in the citable summary, reads:" -> "The claim
  language, mirrored word for word in the filing's own summary, reads:" — reader-facing
  wording, same accurate framing ([0016] is the summary mirror of claim 39). The
  `# Footnotes` annex does NOT ship: strip_publication.py cuts at the `# Footnotes` heading
  (verified in the re-emitted publication.md), so the internal-artifact names never reach
  X Articles, exactly the conditional the reader stated. This also closes carried r3-F1.
- location: §4, claim-39 lead-in

## sa1A-F5 (low — FIG. 1 caption carries no claim)

- disposition: applied
- change: "*FIG. 1: a systolic array, logically.*" -> adds one compressed claim clause:
  "Weights (110) come down from the top [0021], data (115) comes in from the left, and every
  crossing of the two is a multiply-and-add." Worded to avoid a body n-gram echo (gate_dupe
  PASS); [0021] anchors the weights-from-top clause, 115-from-left is figure content
  (grounding sub-table 3 verified the image). caption_role stays prose_covers_fully;
  figures-rationale.md updated.
- location: FIG. 1 caption, §3

## sa1A-F6 + sa1B-F6 (low, 2 votes — translation narrower than claim text)

- disposition: applied (body translation), rejected (header caption)
- change: "bonded, permanently, to its own column of the array" -> "to its own column or
  columns of the array" — matches claim 39's "respective one or more columns"; the adjacent
  verbatim quote continues to carry the exact language.
- rejected item + justification: the header caption's "a dedicated column (515A to 515D)"
  describes FIG. 5's drawn topology, which IS one-to-one (grounding S1: verified
  element-for-element against the image and [0044]); the caption presents "the claimed core
  step as a drawing", i.e. one embodiment of claim 39, not the claim's outer bound. Widening
  it would make the caption false to the image.
- location: §4, translation sentence

## sa1B-F2 (low — boundary attributed to claims 11-13 collectively)

- disposition: applied
- change: "The same claims then draw a boundary..." -> "The last of them, claim 13, then
  draws a boundary the arrays cannot cross:" — the no-communication limitation is claim 13's
  alone.
- location: §5, claims 11-13 paragraph

## sa1B-F3 (low — embodiment elevated to defining feature)

- disposition: applied
- change: "One more design choice defines the machine. The combined array 'does not take
  instructions at runtime...'" -> "One more choice marks how single-minded the machine is
  meant to be. In the embodiment the filing describes, the combined array 'does not take
  instructions at runtime, and only executes instructions in a preset loop' [0027]." — the
  label fix: [0027]'s "in one embodiment" scope is now on the sentence; the investor point
  (single-workload commitment) is intact.
- location: §3, preset-loop paragraph

## sa1B-F4 (low — header converts paper into silicon)

- disposition: applied
- change: header "The Rest of the 2023 Silicon Is Already Transformer-Shaped" -> "The Rest
  of the 2023 Design Is Already Transformer-Shaped". Body uses of "silicon" ("splits the
  silicon", "the silicon split") stay: inside the section they read as the disclosed
  design's hardware division, and only the header was flagged as the quotable overpromise.
- location: §5 header (thesis-trace updated)

## Carried lows from acceptance (score-history: r3-F1, r4-F1, r4-F2, r4-F3)

- r3-F1 (citable-summary gloss): applied — closed by sa1A-F4 above.
- r4-F1 (continuation/family gloss): applied — "no continuation, the follow-on application
  that would extend the family" (§6, one clause).
- r4-F2 (founders epithet x3 in §7): applied — "signed by both founders" cut from §7
  paragraph 1 (the signature fact lives in §1/§2); §7 now carries the founders twice
  (invariants list; closing "co-founder-signed blueprint").
- r4-F3 ("not X. It is Y" figure x4): partially applied — the §4 bold cut (sa1A-F1) removes
  one instance; the remaining uses are §1 (the lead verdict) and §2 (the load-bearing
  application-vs-patent distinction), which stay by design. Neither adversarial reader
  re-raised the figure.

## Volunteered changes (beyond findings)

- §7 "or the set narrows or dies" -> "or the claims narrow or die" (dedupe of the phrase the
  sa1A-F2 fix would otherwise have duplicated from §6 — itemized under sa1A-F2).
- draft_version bumped 3 -> 4; publication.md re-emitted via strip pipeline;
  figures-rationale.md (FIG. 1, FIG. 2 caption records) and thesis-trace.md (§3 anchors +
  [0029], §4 bold note, §5 header, §7 survivor phrasing) updated to match.
- Nothing else moved.

## Recount after structural edits

- §4 bold-merge: bridge paragraph now 2 prose sentences + bold pair = 3 sentences; neighbors
  unchanged (claim-family paragraph 4).
- §6 steelman after two cuts: 6 sentences. §7 paragraph 1 after epithet cut: 4 sentences.
  §7 claim-39 paragraph: 4. §3 preset-loop paragraph: 5. All paragraphs within the 3-7 band;
  gate_structure PASS (STRUCT-001 none; the one STRUCT-004 warn is the pre-existing factual
  triad, warn-only by design).
- Figure tokens re-checked: fig-05 header + FIG. 1/2/5/6/7 body references all present;
  gate_figure_use PASS; no orphaned reference.

## Gate self-check (post-edit)

run_gates.py: 13/13 PASS (warns: 1 STRUCT-004 pre-existing triad; 2 DUPE-001 = the
company's own slogan "the best layer is no layer" quoted in §1 and §4, sanctioned repetition
present since round 1; 19 LONGSENT incl. known parser merge artifacts). gate_quotes,
gate_anchors, gate_hedge (closing_posture: firm) all clean.
