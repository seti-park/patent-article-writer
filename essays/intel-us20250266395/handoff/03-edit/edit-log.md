# Edit Log — Round 4 (confirmation round for double-clean)

```yaml
review_id: intel-us20250266395-editorial-review-4
draft_source: handoff/02-compose/essay-draft.md
draft_version: 3   # unchanged since round 3 (no revision occurred; this is the confirmation review)
review_timestamp: 2026-07-05T00:00:00Z
review_round: 4
posture_applied: measured
closing_posture_declared: firm   # 6G/6H/6I evaluated at full strength
gate_precheck: handoff/03-edit/gate-result.round-4.json (all 14 gates PASS, zero findings/warns; nothing below re-litigates a gate)
overall_assessment: pass

reviewer_independence_note: |
  Fresh context, no commitment to prior rounds. Because a clean confirmation of an
  unchanged draft is exactly where rubber-stamping happens, this round did NOT take
  round 3's evidence on faith: every [dddd]-anchored quote was re-verified directly
  against input/patent.md by grep (not against round-3's transcriptions), the claim
  structure was re-read from the patent's own Claims section, all paragraph bands
  were recounted from scratch, both of round 3's explicitly re-measurable judgment
  calls were re-measured with independent numbers (rulings below), and the banned-
  word/pattern/em-dash/cite-format sweeps were re-run mechanically rather than
  trusted from the gate file.

# =====================================================================
# PART 1 — RE-REVIEW PROTOCOL: carried state from round 3
# =====================================================================
# Round 3 issued ZERO new findings (no r3-F<k> ids exist) and closed all four
# round-2 ids. There is therefore no open finding_id to rule on. Per the
# protocol's intent (no silent inheritance), this round instead (a) spot-
# re-verified the r1/r2 fix chain in draft v3 from the sources, and (b) ruled
# afresh on the two judgment calls round 3 recorded for falsification.

carried_state_verification:

  - scope: r1/r2 applied-fix chain, independently re-verified in v3
    ruling: all-intact
    evidence: |
      r1-F1: §2 reads "Then comes the half Intel's shipped bridge flow does not
      contain" (narrowed, not hedged) — present. r1-F2 + r2-F2: FIG. 8 caption
      attaches 882 to the solder bumps (re-checked against patent.md [0056]: "solder
      attached to the upper surface of the substrate 870/970 with solder bumps
      882/982"); FIG. 5A/5B caption reads "ball-pitch solder pads (526...)"
      (re-checked against [0048]: "ball pitch solder pads 526") — both correct.
      r1-F4: "The parallel Example paragraph is written broader [0138]. The claim
      as filed is not." — present; divergence labeled at the anchor. r1-F6: §6
      guard is the this-filing form ("It is one pending application, and nothing in
      it schedules a product.") and remains the ONLY guard in the verdict. r1-F9:
      dual anchor "[0060], [0061]" present. r1-F10: "the one stated-effect
      sentence" present. r1-F11: the EMIB-baseline contrast sentence in §1 ¶1 is
      unanchored; [0142] rides only the patent half. r1-F13: "rolling out ...
      from 2026" attaches the date to the rollout. r1-F14: exactly three
      functional attribution labels remain ("the industry's and this essay's",
      "every link this essay draws", "this essay's synthesis"). r1-F18: the
      wind-up sentence is gone; the Mahajan paragraph opens on the fact. r2-F3:
      §4 glass paragraph opens "There is a quiet glass thread here: the bridge
      itself may be silicon, organic, or glass [0033]." — self-reference clause
      gone. r2-F4: "are generic wafer-and-device boilerplate" with the universal
      ("every filing carries") cut. r2-F1: §3 bands recounted 5/4/3/5 and §5
      bands 6/4/4/6/3/3 — both splits intact, signature line 2 byte-identical
      ("Only an assembly that has already passed its test gets to spend a
      substrate.").

  - scope: r1-F12 rejection (claim-20 truncation premise), independently re-tested
    ruling: rejection-confirmed
    evidence: |
      Re-grepped input/patent.md myself: the final claims line is
      "**20**. The method of claim 19, wherein the substrate has a cavity and
      attaching the substrate to the multi-die bridge assembly includes placing
      the bridge component in the cavity." (file line 228). The round-1 premise
      (snapshot ends at claim 19) was wrong; §5's "one dependent claim away"
      sentence is fully supported by the snapshot itself, not only by [0144].

  - scope: "round-3 judgment call 1 — §4 two-sentence caption-adjacent paragraph"
    ruling: upheld-not-a-finding
    evidence: |
      Re-measured: the paragraph after the FIG. 7 caption ("In the cavity
      embodiments... / Even here the attach options stay open...") is 2 sentences,
      ~82 words, and both sentences carry verbatim-quote/anchor freight (the [0035]
      split quote; the [0057]/[0058] figure-family pointers the handoff notes
      sanction). Merge options re-tested: the preceding unit is a caption (not
      mergeable prose); merging forward into the 4-sentence claimed-structure
      paragraph produces a ~148-word quote-integrated wall spanning two distinct
      ideas (attach options vs claimed structure + effect), trading a soft cadence
      note for a real 2C/5C defect; the dense second sentence has no natural seam
      (three parallel attach options, one clause each). The 3-7 band is a soft 1A
      cadence rule, the draft already uses sanctioned sub-3-sentence staging units,
      and the quote-integrated demotion applies. Round 3's ruling stands on my
      independent measurement: deliberate rhythm, not compression damage; at most
      low, no action recommended.

  - scope: "round-3 judgment call 2 — §6 ¶2 mobile length"
    ruling: upheld-not-a-finding
    evidence: |
      Re-counted independently: exactly 98 words, 7 sentences, longest sentence 30
      words. At the 5C detection heuristic's strict bound (12 words/line) that is
      8.17 lines — nominally over the >8 flag line; at the reference's own stated
      typography range (12-15 w/l), the midpoint (13.5) gives 7.3 lines. The
      distinguishing precedent is r2-F1: the paragraphs flagged there (112/115
      words) exceeded 8 lines even at the midpoint typography (8.3+/8.5+); §6 ¶2
      does not — it crosses only at the narrowest bound. The underlying 5C failure
      condition is "renders > 8 lines on mobile", which is not clearly met, and the
      paragraph is seven short declaratives (the opposite of a text wall). The one
      available seam (after "watchable and binary.") would split the verdict's
      question from its answer and fragment the closing into 5/3/4-sentence
      shards for a 2-word overrun at the strictest reading. Round 3's noise-band
      ruling is consistent with round-2's own application of the threshold and
      stands. Not a finding.

carried_summary: |
  No open finding_id existed entering round 4 (round 3: pass, zero findings; all
  r2 ids closed there). The full r1/r2 fix chain was spot-re-verified in v3 from
  patent.md and the design artifacts — all intact, no regression. Both round-3
  re-measurable judgment calls were re-measured with independent numbers and
  upheld. No id re-asserted; nothing closes silently because nothing was open.

# =====================================================================
# PART 2 — FRESH 7-PASS REVIEW of draft v3 (fresh context; new findings
# would be r4-F<k> — none met the bar; every entry states what was checked)
# =====================================================================

findings:

  - pass: pass-1-voice-anti-ai
    finding: "no findings"
    scoped_to: |
      1B re-run mechanically by this reviewer (not inherited from gate output):
      case-insensitive grep of the full Tier-1 banned list plus the judgment-list
      cluster words (seamless/robust/realm/deep dive/going forward etc.) — 0 hits;
      banned-pattern grep (not-just/not-only, despite-the, serves as / stands as a
      / represents a / constitutes, in summary / to recap / in conclusion, worth
      noting, vague attributions, sentence-initial Additionally / Furthermore /
      Moreover) — 0 hits in prose. Em-dash grep: 0. Puffery: none ("unusually
      candid" in §4 ruled mild evaluative description of the background section,
      not puffery about the invention). Elegant variation: Intel is always Intel;
      filing/document/application alternation is common-noun use. Tier-2 tells
      tallied: exactly 2 clause-joining semicolons in ~2,240 words (§5 ¶1; FIG. 7
      caption) and the parenthetical "(source; see Sources)" convention — below
      cluster threshold; colon uses are quote-introduction or apposition, and the
      one announcement-colon ("That one step moves the dividing line:") is the
      sanctioned bold-anchor staging device carried since round 1. 1A cadence:
      every prose paragraph recounted — bands §1 5/4/4, §2 4/6/3 plus the two
      sanctioned 1-sentence staging lines, §3 5/4/3/5, §4 6/3/3/2/4/6, §5
      6/4/4/6/3/3, §6 5/7 — all within 3-7 except the sanctioned staging lines and
      the §4 two-sentence paragraph ruled above (Part 1). Single bold anchor (§2),
      Title Case headers uniform, no emoji, no ALL-CAPS, no exclamation marks.

  - pass: pass-2-redundancy
    finding: "no findings"
    scoped_to: |
      2A appearance map rebuilt from scratch for the order/test-gate motif: cover
      caption ("that ordering is the whole story"), §1 news-frame, §2 claim-text
      blockquotes, §3 economics walk, §5 scope re-pricing, §6 verdict — each
      recurrence adds a distinct evidence layer; the three signature lines
      declared in thesis-trace verified byte-intact at their stations (§1 ¶1 pair,
      §3 ¶3 close, §6 ¶1 close) and excluded from counts. "Pending application"
      appears exactly 3 times, in exactly the three sanctioned homes (lead
      two-sided-call clause, §5 pricing, §6 guard) — cross-checked against the
      spine's attention-budget row. KGD percentages appear once. "Fifteen months"
      appears twice (lead + closing recap bookend). Feb-2024/May-2025/Aug-2025
      dates each recur only with new context (bibliographic vs synthesis vs
      pricing). 2B: fresh tightening sweep found no >=25%-cuttable sentence; no
      filler phrases (in-order-to / due-to-the-fact / at-this-point absent). 2C:
      max paragraph 7 sentences (§6 ¶2); >150-word single-idea check hits only the
      §4 glass paragraph (~150 words) — quote-integrated ([0049]/[0138]/[0059]
      quotes with interpretation), demoted per the posture-lens heuristic; a split
      would orphan quote from interpretation. Consistent with three prior rounds;
      independently re-judged, not inherited.

  - pass: pass-3-fact-paraphrase
    finding: "no findings"
    scoped_to: |
      3A re-verified from the PATENT, not from prior logs: grep-matched every
      quoted span byte-level in input/patent.md — [0001] wish-list; both §2
      blockquotes against Example 21 [0142] (with the required "Example 21"
      attribution line; the Example/claim-19 wording delta is why the Example
      anchor is mandatory, and it is present); [0061]/[0062] test/attach spans
      (step numbers cleanly outside quotes); [0024] both problem quotes; the
      [0035] split quote (both halves verbatim-contiguous, "102" dropped by
      closing/reopening quotes); [0122] "directly bonded"; [0034] "in a range of
      1 to 10 microns"; [0025] "many substrates remain solder-attach components";
      [0049] "to provide structural stability"; [0138] glass range; [0059] SoC
      sentence; [0123] claim-2 span; [0142]/[0144] partials in §5. Claim-structure
      assertions re-read from the Claims section itself: claim 17 depends on
      no-cavity claim 16 (draft correct); no claim carries the 1-10 µm pitch
      (correct — the number lives only in [0025]/[0034] description); claim 2
      never says power/TSV/cavity (correct); claim 19 locks the order + test +
      attach-when-passes, claim 20 adds the cavity (correct); Examples 24/25
      ([0145]/[0146]) claim hybrid bonding and solder as separate dependent
      options (§2 "separately, as options" correct); FIG. 12-15 = four context
      sheets (§5 "last four drawing sheets" correct); "bridge slung underneath"
      matches the drawing orientation per [0032]/[0048] ("bottom" in the drawing).
      Sought-vocabulary discipline re-swept: "as filed", "asking for", "a lock
      Intel is asking for" — no owns/secured/locked-in-granted-sense anywhere.
      3B: external claims re-traced to fact-check-log IDs and # Sources; intervals
      recomputed (2024-02-20 → 2025-05 ≈ 15 months; → 2025-08-21 = 18 months);
      thirteen inventors recounted from the Sources entry (=13); KGD math
      recomputed (0.95^4=0.815→"about 81 percent", 0.95^20=0.358→"about 35
      percent"), labeled as industry+essay math both before and after use;
      120x120 mm sentence carries its single-outlet label per the log's tier-3
      note and its point rides the die-count logic §3 already taught (no naked
      magnitude); Mahajan used within the "mainline packaging organization" limit
      (§1 "packaging group", §5, §6 — same strength, never stronger); counterparts
      JP/KR/CN/DE tier-1; glass announcement Sept 2023 tier-1. EMIB fence
      re-swept sentence-by-sentence: no EMIB/EMIB-T statement carries a [dddd]
      anchor; the document-never-says-EMIB disclosure appears in both §4 and §5.
      §1's "A bridge die is a small piece of silicon" gloss checked against
      [0033]: it glosses the news-context (EMIB) object and §4 explicitly broadens
      to silicon/organic/glass on [0033] — gloss-then-refine, not a contradiction.
      3C: zero quoted-text mutations found. 3D: causal claims inventoried — see
      pass-4.

  - pass: pass-4-logic-causality
    finding: "no findings"
    scoped_to: |
      4A re-traced against thesis-spine's spine→section table: Axis 1 → §2
      (re-priced §5), Axis 2 → §4, Axis 3 → §3, Axis 4 → §4; every section
      advances (not merely mentions) its element; no out-of-spine claim found on a
      fresh read. 4B full causal inventory: "it explains why a flow ... reads like
      an economic decision" (mechanism shown — the compounding arithmetic — and
      double-labeled as industry's/essay's, not the patent's); "the more dies a
      package carries, the more it pays to test" (mechanism carried by the §3
      math); "fee money a company does not usually spend on ideas it considers
      dead" (hedged inference, "usually", tier-1 counterpart fact); "The paperwork
      moved first last time." (n=1 historical fact anchored via mahajan-intel-
      fellow, stated as history, not law); the after-EMIB-T link consistently
      framed as timeline+mechanism synthesis with "Intel has not connected the two
      documents" stated in §5 — the confounder (a big filer's routine breadth) is
      the steelman itself, addressed head-on. No correlation→causation drift, no
      reverse-causation exposure (the essay never claims the filing caused
      EMIB-T or vice versa), no enables-without-mechanism. 4C: lead tension
      resolves in §6; closing-binary-test matches the spine's Acknowledged
      residual risk under firm posture; the implication (test-gate economics +
      this family's prosecution as the tell) is this-patent-specific.

  - pass: pass-5-reader-perspective
    finding: "no findings"
    scoped_to: |
      Full cold read as the reader-profile investor. 5A: hook lands in ¶1
      sentence 1; no 3+ paragraph mechanism wall (§4's run is broken by two
      captions and the "Why rebuild the order at all?" pivot); §3 delivers the
      stake payoff early; closing lands on the thesis. 5B: "why does this matter"
      answerable after the lead (two-sided call), at each boundary (§2 what
      changed / §3 what it saves / §4 why bother / §5 what is asked vs owned),
      and §6 ¶2 reads standalone; the money thread feeds the verdict in every
      section. Jargon: bridge die, substrate ("board-like base"), TSV ("vertical
      metal shafts"), TGV, hybrid bonding ("no solder in between"), micron ("a
      millionth of a meter"), known-good die — each one-clause glossed on first
      use, then signposts. 5C mechanical recount of every paragraph at 12 w/l:
      all non-quote-integrated paragraphs ≤8 lines except §6 ¶2 at the boundary —
      re-measured and ruled in Part 1 (98 words = 8.17 lines strict / 7.3 at
      typography midpoint; failure condition "renders >8 lines" not clearly met;
      upheld not-a-finding). The four quote-integrated long paragraphs (§2 ¶3
      ~127w, §4 glass ¶ ~150w, §5 ¶1 ~127w, §5 concede ¶ ~130w) remain demoted to
      low per the posture-lens quote-integrated heuristic and the standing
      adjacency rationale — independently re-judged: each carries quote +
      interpretation that a split would orphan.

  - pass: pass-6-lead-conclusion-format
    finding: "no findings"
    scoped_to: |
      6A: ¶1 sentence 1 sets the tension; the patent is on the table by sentence
      1 and the two-sided call lands inside the lead (§1 ¶3 sentences 3-4). 6B:
      frame closure holds (fifteen-months/stage frame returns in §6 ¶1; "The
      paperwork moved first last time." closes the loop); closing-binary-test
      matches Acknowledged residual risk under firm posture — not open-question.
      6C: # Sources appears exactly once; exactly the 5 enum categories; 7
      entries; all-or-nothing subgrouping honored. 6D: no "First, et al."
      malformation (the thin ECTC bibliographic entry remains the accepted
      r1-F17 upstream item, not a draft defect). 6E re-run mechanically: em-dash
      0; every inline cite 4-digit [dddd]; banned re-grep 0; no footnote defs in
      publication.md (grep 0). 6F: title 54 chars, no em-dash, no colon. 6G under
      firm posture, checked SYMMETRICALLY: over-hedge side — the verdict leads
      with the call, exactly ONE anti-hype guard and it is this-filing-specific
      ("It is one pending application, and nothing in it schedules a product."),
      limits referenced not re-listed ("stand as written"), no qualifier-led
      sentence, no false equivalence, no category truism, hedge density low;
      overreach side — the call is a documentary claim ("writing down the
      assembly flow"), which the anchored record (claim 19's order + test, filed
      2024-02-20, Example-quoted) fully carries; the after-EMIB-T positioning is
      disclosed as synthesis and priced in §4/§5; "none of them moves the call"
      is proportionate because the limits attack a production claim the essay
      never makes; the falsifier is named in BOTH directions (disclosures/
      prosecution confirm vs examination-narrowing weakens). 6H: no insurance
      fact ahead of the ¶1 discovery beat; the first two lines earn the tap. 6I:
      procedure/pricing narration lives only in §5 (the one payload:pricing
      home) + one lead status clause + the §6 guard/recap; zero process narration
      in the lead; spend-motif budget re-counted ("fee money" once; "one filing
      among hundreds" family once, §5 + its own header; "more than paper" ruled
      binary-test framing inside the recap allowance, consistent with rounds
      1-3).

  - pass: pass-7-adversarial-reader
    finding: "no findings"
    scoped_to: |
      All 7 checks re-run with quoted evidence, both personas. (1) Hook: PASS —
      ¶1 opens declarative on the discovery beat ("Fifteen months before Intel
      put EMIB-T on a conference stage, a filing from its packaging group had
      already written down a different way to build the same kind of chip
      package."), no insurance ahead; the two-sided call lands by lead end ("It
      is also a pending application: a set of claims Intel is asking for, not a
      product it has scheduled."). (2) Header-as-claim: PASS — all six headers
      assert and the header-only skim reconstructs the argument end-to-end. (3)
      Steelman: PASS — THIS-patent claim-scope objection conceded at full
      strength in §5 (pitch description-only [0034]; hybrid bonding pitch-less in
      the apparatus claim [0122]; claim 2 silent on power/TSV/cavity [0123];
      claim 17 on the no-cavity branch; no claim holds the whole architecture;
      document never says EMIB) then refined via claim 19/20's locked order +
      test gate. Independently pressure-tested two further objections as the
      skeptical pro-subject reader: (a) "KGD testing is standard industry
      practice" — pre-rebutted: §3 attributes the KGD concept to industry and the
      essay stakes novelty on the claimed ORDER, with examination-narrowing named
      as the falsifier; (b) "other vendors already build chip-first bridge
      flows" — the draft never claims industry-wide uniqueness (r1-F1's narrowing
      scopes every uniqueness claim to Intel's shipped flow / the public EMIB-T
      story). No unrebutted strongest counter found. (4) Meta: PASS — the three
      remaining self-references are functional attribution labels required by
      the grounding rules; "Note whose yield that is." re-judged independently:
      a two-word-scale content pointer enforcing the [0035] scope boundary
      (functionally a scope disclaimer, exempt class), single instance — upheld.
      (5) Jargon: PASS — signposts throughout; the glass thread stays one
      paragraph; no doctrinal deep-dive. (6) Stub: PASS — §6 at ~196 words is a
      proportionate closing against 230-620-word siblings. (7) Restatement: PASS
      — the non-exempt core verdict is asserted in exactly 3 sections (§2 bold
      anchor, §5 refinement, §6 call); the cover caption's "that ordering is the
      whole story" is cover-surface framing, not a body section; the three
      declared signature lines are byte-intact and exempt.

double_clean_note: |
  Round 3 (independent reviewer): pass, zero findings. Round 4 (this reviewer,
  fresh context, unchanged draft v3): pass, zero findings, with the two carried
  judgment calls independently re-measured and upheld and the full quote/claim
  chain re-verified against the patent snapshot. This constitutes the second
  consecutive clean round; the double-clean acceptance call itself belongs to the
  orchestrator.
```
