```yaml
review_id: openai-us20260147536-editorial-review-5
draft_source: handoff/02-compose/essay-draft.md
draft_version_reviewed: 4
review_round: 5
review_timestamp: 2026-07-09T00:00:00Z
posture_applied: measured   # 3-tier posture = measured; edition declares closing_posture: firm,
                            # so 6G/6H/6I escalate to HIGH if violated. Checked — no firm-closing
                            # violation. This round reviews the r4-F1 REVISION (draft v3 -> v4).
closing_posture_declared: firm
gates_precomputed: PASS (0 fails). Warn signals weighed below: STRUCT-004 (4 triads),
                   DUPE-001 x2 (deliberate §1->§6 bookend), LONGSENT-001 x7. Only FIG. 1/3/4/43
                   tokens present. (LONGSENT dropped 8->7 vs round 4: the §3 ¶3 rework retired
                   one long sentence; no new long sentence introduced.)
reviewer_note: |
  REVISION round. Fresh round-5 reviewer, no memory of composing or of rounds 1-4, spawned to
  review draft_version 4 — the revision that applied round-4's r4-F1 (claim-scope completeness:
  the core is claimed by THREE independent claims, 1, 20, AND 29). Round 4 BROKE a candidate
  double-clean by re-deriving the claim set from the patent and catching an upstream omission
  (claim 29) that rounds 1-3 had inherited from the invention-summary. The documented failure
  mode is a reviewer that rubber-stamps, so I did NOT trust round 4's clean OR the composer's
  disposition. I re-derived from source:
    - Re-byte-checked all 8 verbatim patent blockquotes against input/patent.md (not against
      prior logs).
    - Independently ENUMERATED the entire patent claim set (input/patent.md lines 505-525) to
      confirm the complete independent-claim set is exactly {1, 20, 29} and that claim 29 is
      genuinely independent (line 525: self-contained "A computing system comprising:", full
      triad + shift register in the functional block, CIM configured for VMM — no "according to
      claim N" dependency; it is the last claim, no 30+).
    - Verified all four r4-F1 loci landed correctly and re-anchored to the corrected
      invention-summary Claim scope map (which now carries claim 29 as a third independent row).
    - Re-verified every load-bearing [dddd] anchor in and around the reworked §3 ¶3
      ([0200]/[0202]/[0206]/[0183]) against the patent paragraphs.
    - Re-derived the verdict proportionality (both directions), the lead hook, and the steelman
      from source; confirmed the correction did NOT hedge the verdict.
    - Re-counted the §3 ¶3 paragraph band (the only structural edit this round) for neighbor
      regression.
  RESULT: r4-F1 LANDED and is factually correct; the verdict was NOT hedged by the correction
  (it STRENGTHENS the core coverage — a third independent shot at the same triad); zero new
  medium+ findings across all 7 passes. This is a CLEAN round. It is the FIRST clean round after
  the round-4 break, so it opens (does not complete) the double-clean; a further independent
  round is required to confirm.
  Re-review protocol followed: N-1 = round 4. r4-F1 (the one applied medium finding) is ruled
  first in PART A; all older carried ids (r1-F1..F6, r2-F1..F3) are re-confirmed still-landed on
  draft v4 (the only edits since round 4 were the four r4-F1 loci, so they are intact by
  construction and spot-verified). No id dropped.
overall_assessment: pass   # 0 critical, 0 high, 0 medium, 0 low. Per feedback-format assessment
                           # table (No critical, No high, No medium) -> pass. Clean round.
                           # Double-clean NOT yet complete: round 4 was revise-recommended, so
                           # round 5 is the first of the two consecutive independent cleans the
                           # acceptance contract requires.

# ===========================================================================
# PART A — CARRIED FINDING RULINGS
# r4-F1 was APPLIED (draft v3 -> v4). All older ids carried and re-confirmed. No id closes
# silently; check_run.py id-continuity satisfied.
# ===========================================================================

carried_findings:

  - finding_id: r4-F1
    pass: claim-adequacy   # pass-3 (claim adequacy) + pass-4 (thesis-section accuracy)
    prior_disposition: applied (round 4, revision-response.round-4.md)
    round5_ruling: LANDED — accept. Verified correct against input/patent.md, not just against
                   the disposition note.
    verification: |
      SOURCE RE-DERIVATION (independent). Enumerated all claims in input/patent.md:
        - Claim 1  (line 505): "A computing system comprising:" — INDEPENDENT, the triad.
        - Claims 2-10 (lines 506-514): "The computing system according to claim N" — dependent.
        - Claims 11-19 (line 515): "(canceled)".
        - Claim 20 (line 516): "A system comprising:" — INDEPENDENT, triad + shift calculation
          and select decoding unit folded in.
        - Claims 21-28 (lines 517-524): dependent (each "according to claim 1/21/25").
        - Claim 29 (line 525): "A computing system comprising: a compute-in-memory (CIM) macro
          configured to perform a vector matrix multiplication (VMM) operation ... a functional
          block ... the functional block comprising a shift register ..." — INDEPENDENT, full
          triad + shift register; the LAST claim (no 30+).
      => The complete independent-claim set is EXACTLY {1, 20, 29}. Confirmed. Claim 29 is
      unambiguously independent and recites the full multiply-align-add triad. The essay's new
      enumeration is therefore complete AND correct (no over-claim: it says "1, 20, and 29",
      which is the true set, not "three-plus").

      FOUR LOCI — each landed and each accurate:
        (a) §2 ¶3 (line 34): "What independent claims 1, 20, and 29 seek to protect is a
            structure that pays that cost once." [0011] supports the triad. Correct.
        (b) §3 ¶2 (line 52): "independent claims 1, 20, and 29 seek the multiply-align-add
            triad, not the mode decoding unit and not the format switching [0011]." Correct —
            none of claims 1/20/29 recites a mode decoding unit or format switching (verified
            against the claim text); the mode decoding unit is description material ([0146]/
            [0191]), not a claim element.
        (c) §3 ¶3 (line 54), the reworked "named machinery" paragraph:
              "The named machinery is pulled up into the independent claims themselves. Claim 20
              folds in a shift calculation and select decoding unit that works out each product's
              shift [0200], and claim 29 pulls in a shift register, each carried alongside the
              same multiply-align-add triad. The dependent claims add the specifics: the shift
              register sized by rule to the maximum exponent plus the mantissa bit count [0202],
              and a logarithmic multiplexer tree that does the shifting in stages [0206]."
            This is now ACCURATE and the previously-false "that unit is the one piece independent
            claim 20 pulls up into itself" framing is GONE:
              - claim 20 independently folds in the shift calculation and select decoding unit
                (verified line 516; anchor [0200] describes the shift-value computation, line 265)
              - claim 29 independently folds in a (bare) shift register (verified line 525)
              - the SIZING rule (bits = Emax + mantissa bit count) is a DEPENDENT specific
                (claim 3, line 507; anchor [0202], line 267: "a first shift register 3574 having
                a number of bits that equals Emax plus the number of mantissa bits ... 7b+22b=29b")
              - the logarithmic multiplexer tree is a DEPENDENT specific (claim 6, line 510;
                anchor [0206], line 271: "a plurality of multiplexers 3972 formed as a
                logarithmic tree").
            The subtlety is handled correctly: claim 29's shift register is bare in the
            independent claim; the sizing rule is genuinely a dependent-claim addition. No
            fact is misstated. The "64 by 64 half adders" [0183] sentence is kept verbatim and
            correctly attributed to the description ([0183], line 247: "64x64 number of half
            adders and full adders can be saved" for the 1x32 * 32x32 VMM / exponent-computation
            optimization).
        (d) §6 ¶3 (line 87): "what examination leaves of claims 1, 20, and 29 will fix how much
            of the align-once, integer-accumulate engine OpenAI ends up owning." Correct; the
            "ends up owning" sought-* vocabulary is preserved.
      NO leftover "claims 1 and 20" survives anywhere in the draft (independently grepped — the
      only "1, 20, and 29" hits are lines 34/52/87 and the §3 ¶3 "claim 20 / claim 29" split at
      line 54).

      VERDICT NOT HEDGED (jurisdiction fence honored). The correction is coverage-STRENGTHENING
      (a third independent claim to the same core), applied as an anchor/narrow enumeration fix.
      No caveat, disclaimer, or hedge was added. §6 ¶1 still LEADS with the firm call
      ("'OpenAI-designed' is literal engineering, and this filing is the primary evidence");
      the single THIS-patent anti-hype guard (Jalapeño / no-silicon, §6 ¶2) is unchanged and
      not re-listed; caveats are referenced not re-stacked ("The bounds priced in the previous
      section scope that call, and they do not reverse it"). gate_hedge PASS. 6G re-derived clean
      below.

      NEIGHBOR REGRESSION CHECK (the only structural edit this round was §3 ¶3). Re-counted the
      band: §3 ¶3 is now 5 sentences, ~112 words — inside the 3-7 band and < 150 words, no
      STRUCT-001 (8-sentence) exposure. r1-F2's density split (§3 into ¶3 + ¶4) is preserved;
      ¶1/¶2/¶4 are byte-unchanged. No figure token, blockquote, or [dddd] anchor added or lost
      by the rework (anchors in the reworked span — [0200]/[0202]/[0206]/[0183] — were already
      present and valid in v3). "folds in" vs "pulls in" verb variation avoids a mechanical
      back-to-back parallelism; not a pass-1 tell, not a new DUPE-001. Accept.

  # -------------------------------------------------------------------------
  # Older carried ids — re-confirmed STILL LANDED on draft v4. The only edits since round 4 were
  # the four r4-F1 loci above, so these fixes are intact by construction; each spot-verified on
  # the current draft (not assumed). None re-opened.
  # -------------------------------------------------------------------------

  - finding_id: r2-F1
    prior_disposition: applied (r2) -> LANDED (r3, r4)
    round5_ruling: STILL LANDED — accept
    verification: |
      FIG. 4 header caption (line 15) is the trimmed 3-sentence / ~53-word cover caption, zero
      reference numerals, ending "This is claim 1's align-then-integer-accumulate step, made
      literal." Grounding re-checked in pass-3 (Emax<=22/INT5 [0199]; adder tree integer [0011];
      35-bit [0145]); caption claims nothing beyond the FIG. 4 drawing (per figures-manifest:
      "adder tree 3880/3882/3884/426, per-row shift calculation Emax-E, 2's-complement shift").

  - finding_id: r2-F2
    prior_disposition: applied (r2) -> LANDED (r3, r4)
    round5_ruling: STILL LANDED — accept
    verification: |
      Independent grep of draft v4 returns figure tokens EXACTLY {FIG. 4 (header img + caption),
      FIG. 1, FIG. 3, FIG. 43} — no FIG. 38, no FIG. 45 anywhere. gate_figure_use / FIGREF PASS
      (precomputed). The §2 ¶4 bit-shift sentence still ends at "Here the lining up is a bit
      shift." (line 42); §5 ¶3 still closes on the [0118] scan-test quote (line 79).

  - finding_id: r2-F3
    prior_disposition: applied (r2) -> LANDED (r3, r4)
    round5_ruling: STILL LANDED — accept
    verification: |
      §6 ¶1 (line 83) reads "...priority date about eleven months older than the announcement..."
      — the "about" qualifier present, uniform with §1 ¶1. Date-arithmetic precision, not a
      verdict hedge; the surrounding call is firm and untouched.

  - finding_id: r1-F1
    prior_disposition: applied (r1) -> LANDED (r2-r4)
    round5_ruling: STILL LANDED — accept
    verification: |
      §2 density split intact: line 42 ends "...on a consistent footing before the sum [0104]."
      and line 44 opens a fresh paragraph "The numbers stay small by design...". No re-merge.

  - finding_id: r1-F2
    prior_disposition: applied (r1) -> LANDED (r2-r4)
    round5_ruling: STILL LANDED — accept (re-counted this round because §3 ¶3 was the r4-F1 edit
                   locus). §3 remains four paragraphs (¶1 line 50, ¶2 line 52, ¶3 line 54, ¶4
                   line 56); the ¶3/¶4 split from r1-F2 is preserved; ¶3 stays in-band at 5
                   sentences / ~112 words after the r4-F1 rework.

  - finding_id: r1-F3
    prior_disposition: applied (r1) -> LANDED (r2-r4)
    round5_ruling: STILL LANDED — accept. §1 ¶2 (line 21) carries "the math engine was already on
                   file, written to the bitcell"; the depth-motif de-duplication holds.

  - finding_id: r1-F4
    prior_disposition: applied (r1) -> LANDED (r2-r4)
    round5_ruling: STILL LANDED — accept, and now SUBSUMED-CORRECTLY by r4-F1. r1-F4 fixed the
                   essay to state the shift-calc-and-select-decoding unit is folded into
                   independent claim 20 (not dependent-only). The r4-F1 rework preserves that
                   fact ("Claim 20 folds in a shift calculation and select decoding unit ...
                   [0200]") while adding claim 29. r1-F4's landed fact is NOT reverted.

  - finding_id: r1-F5
    prior_disposition: applied (r1) -> LANDED (r2-r4)
    round5_ruling: STILL LANDED — accept. §5 ¶3 (line 79) reads "Concept filings rarely carry
                   clock margins and scan modes." — "rarely" (not "do not") intact; verdict
                   landing untouched.

  - finding_id: r1-F6
    prior_disposition: applied (r1) -> LANDED (r2-r4)
    round5_ruling: STILL LANDED — accept. §1 ¶1 (line 19) carries "about eleven months later";
                   uniform with the §6 recap.

# ===========================================================================
# PART B — NEW ROUND-5 FINDINGS
# ===========================================================================

findings: []   # No new medium/high/critical (or low) findings. See PART C for the falsifiable
               # scoped_to of each pass's independent re-derivation.

# ===========================================================================
# PART C — CLEAN PASSES (falsifiable scoped_to — exactly what was re-derived from source)
# ===========================================================================

clean_passes:

  - pass: pass-1-voice-anti-ai
    finding: "no findings"
    scoped_to: |
      1B MECHANICAL (re-run this round, not inherited): em-dash "—" = 0 across the whole draft
      (independently grepped: 0 occurrences, including blockquotes); en-dash 0. Tier-1 banned list
      (delve/leverage/navigate/crucial/pivotal/underscore/robust/seamless/showcase/enhance/
      groundbreaking/interplay/tapestry/meticulous/testament, etc.) = ZERO hits in prose.
      SOURCE-CONTAMINATION guard re-checked on the quoted paragraphs: patent [0154] (line 213)
      carries "crucial"/"leverage"/"Additionally"/"Furthermore" and [0015] (line 72) carries
      "seamless" and [0104] carries "crucial" — the composer imported NONE of them ([0154] lifts
      only "In some embodiments, 100% utilization of the compute engine 100 may be possible.";
      [0015] lifts only "minimize compute stalls during updates"; [0104] paraphrased to
      "consistent footing"). No sentence-initial Moreover/Furthermore/Additionally in prose. No
      copula avoidance (draft uses is/are throughout; no "serves as a/stands as a"). 1A CADENCE:
      one load-bearing bold anchor ("Align once, and the whole accumulation becomes integer
      arithmetic.", line 46) present once, byte-exact vs thesis-trace signature line 1; signature
      line 2 ("The design record says the work started earlier, and the record is the harder
      document to argue with.", line 87) present once, byte-exact. Reworked §3 ¶3 (line 54) uses
      two list-introducing colons ("add the specifics:" / "counts what such choices buy:") — both
      follow COMPLETE clauses (legitimate elaboration colons, not the "fragment: payoff" AI tell),
      and both pre-existed in v3; not a new cluster. No AI tell in the revision.

  - pass: pass-2-redundancy
    finding: "no findings"
    scoped_to: |
      2A: core verdict lands §1 ¶2 + §6 (lead/close bookend, not padding). DUPE-001 x2 = the
      deliberate "down to the individual memory cell" §1->§6 bookend; the r4-F1 rework introduced
      NO new repeated span (verb variation folds-in/pulls-in was chosen specifically to avoid a
      "claim NN folds in a shift..." parallelism). STRUCT-004 (4 triads) unchanged by the
      revision: decimal-addition analogy, "one alignment/one integer sum/one conversion back",
      PVT term of art, tape-out-depth enumeration — all content-driven. 2C: no essay paragraph
      reaches 8 sentences; the reworked §3 ¶3 is 5 sentences / ~112 words (< 150). Declared
      signature lines exempt from echo/count rules.

  - pass: pass-3-fact-paraphrase
    finding: "no findings (r4-F1 resolved; see PART A). All blockquotes byte-exact; all anchors
             support their sentences; four figure captions grounded."
    scoped_to: |
      3A VERBATIM — re-byte-checked EACH patent quote against input/patent.md at the cited
      paragraph (against source, not prior logs):
        - [0005] conversion-step blockquote (draft 31-32) vs patent line 62: EXACT.
        - [0011] both claim spans (draft 36-38) vs patent line 68: EXACT.
        - [0006] "without requiring separate conversion pipelines or dedicated cores for each
          format" (draft 50) vs patent line 63: EXACT.
        - [0147] pipelined-VMM blockquote (draft 62-63) vs patent line 210: EXACT.
        - [0015] "minimize compute stalls during updates" (draft 67) vs patent line 72: EXACT.
        - [0154] "In some embodiments, 100% utilization of the compute engine 100 may be
          possible." (draft 71) vs patent line 213: EXACT (patent bolds the reference number
          "100" as markdown emphasis; textual content identical).
        - [0118] "serve both compute storage and scan-test roles" (draft 79) vs patent line 180:
          EXACT.
        - [0133] "reducing the von Neumann bottleneck" (draft 19) vs patent line 196: EXACT.
        - "(canceled)" for claims 11-19 (draft 75) vs patent line 515: EXACT registry fact.
      3A/3C ANCHOR SUPPORT (each [dddd] supports its sentence; re-verified the loci touched or
      neighbored by r4-F1 plus a full sweep):
        - [0199] Emax=22/INT5 (draft §2 ¶2 + cover caption) vs patent line 264: faithful.
        - [0200] shift value = Emax - P_E (draft §2 ¶4 + §3 ¶3 "works out each product's shift")
          vs patent line 265: faithful; claim 20's added element (line 516) matches.
        - [0202] shift register bits = Emax + mantissa bit count (draft §3 ¶3) vs patent line 267
          ("7b+22b=29b"): faithful; correctly attributed to a DEPENDENT specific (claim 3).
        - [0206] logarithmic multiplexer tree (draft §3 ¶3) vs patent line 271: faithful;
          correctly attributed to a DEPENDENT specific (claim 6).
        - [0183] "64 by 64 half adders and full adders ... 32-by-32 array" (draft §3 ¶3) vs
          patent line 247: faithful; correctly attributed to the description.
        - [0139] synthesizable integer adder tree vs patent line 202; [0141] MX shared scaling /
          blocks of 32 vs patent line 204; [0130] FP8/FP6/FP4 vs FP6/FP4 vs patent line 192;
          [0142] input buffer vs patent line 205; [0145] INT35+INT5 -> FP22 vs patent line 208;
          [0104] "consistent footing" = "consistent scale" (banned "crucial" dropped); [0131]
          minimal-accuracy-loss vs patent line 193; [0012]/[0015] double-bitcell parallel
          write+VMM vs patent lines 69/72. No polarity/scope/certainty mutation in any span.
      FOUR FIGURE CAPTIONS re-checked against figures-manifest (drawings not re-opened this round;
      manifest + round-4 image reads used):
        - FIG. 4 (line 15): claims align-once core, shift onto largest exponent (<=22, 5-bit int),
          adder tree sums as integers, 35-bit result, claim-1 tie — all within the manifest
          drawing (adder tree 3880/3882/3884/426; Emax-E shift; 2's-complement) + anchors. Clean.
        - FIG. 1 (line 27): input buffer / 32x32 CIM macro (101) / mode decoding (110) /
          dequantization (106) -> FP22 — matches manifest FIG. 1 block diagram; "sets the numeric
          format" glossed from [0006]. Clean.
        - FIG. 3 (line 40): "one column cell, where a single primitive product is made" — matches
          manifest FIG. 3 (column cell Col 0/Row 0). Clean.
        - FIG. 43 (line 69): BC0/BC1 share bit lines, separate write-wordlines, one bank loads
          while the other feeds compute — matches manifest FIG. 43 (bitcell_double 4303, BL0-BL31,
          wwl0/wwl1); function anchored [0012]/[0015]. Clean.
      3B EXTERNAL: 10GW/2025-10-13 (tier-1) -> Official statements; Jalapeño 2026-06-24 + end-2026
      window (tier-1, "company-claimed") -> Official statements; Allegrucci ~17yr Apple / Rain
      head-of-hardware June-2024 (tier-3, labeled "Bloomberg reported", bound stated) -> News &
      media; OCP MX 2023-09 seven signatories (tier-2) -> Technical specs. Every "(see Sources,X)"
      resolves. "Five inventors" (sixth-inventor trap avoided). Sought-* vocabulary intact
      ("seek to protect"/"seek"/"wants to own"/"ends up owning"); pending never shown as granted.
      CLAIM-SCOPE COMPLETENESS (the round-4 break point): independently enumerated all 29 claims;
      independent set = {1, 20, 29}, exactly what the essay now states. COMPLETE and correct. No
      pass-3 miss remains.

  - pass: pass-4-logic-causality
    finding: "no findings"
    scoped_to: |
      4A thesis-section alignment: Axis 1 (triad) + Axis 2 (problem) -> §2; Axis 4 (baseline) +
      steelman -> §3; Axis 3 (effect) -> §4; pricing -> §5; verdict frame -> §1/§6 — all land, no
      out-of-spine claim. The r4-F1 rework STRENGTHENS Axis 4's affirmative return (a third
      independent shot at the core) without introducing an out-of-spine assertion. 4B causality:
      the central inference is EVIDENTIARY, not causal ("this filing is the primary evidence that
      'OpenAI-designed' is literal engineering"); the essay never claims the patent CAUSED the
      announcement, so no correlation->causation drift from the 11-month gap. Confounders bounded:
      Rain/Allegrucci lineage priced in §5 with its limit stated; production/silicon scoped out in
      §6 ("no source shows this macro running in silicon", "nothing connects these circuits to
      Jalapeño"). 4C arc: lead tension set §1, resolved §6; implication is this-filing-specific.

  - pass: pass-5-reader-perspective
    finding: "no findings"
    scoped_to: |
      5A engagement: density splits (r1-F1 §2, r1-F2 §3) and the trimmed cover caption (r2-F1)
      hold; no 3+ consecutive mechanism paragraphs without a surface. The reworked §3 ¶3 still
      translates the claim machinery for the target reader ("shift calculation and select decoding
      unit that works out each product's shift"; "shift register"), meeting the reader-profile
      "translate, then quote" rule; no unglossed legalese introduced. 5B stake clarity (money
      thread): every section still feeds the investor verdict — §3 resolves to "the thesis rests
      on the record". 5C mobile: densest para §3 ¶3 ~112 words / 5 sentences, clean at /15
      words-per-line; re-splitting would fragment the §3 payoff. LONGSENT-001 x7: none breaks
      readability for the advanced-HS-to-early-undergrad reader (patent-domain long-clause
      exception). Four figures referenced substantively; no un-shown-figure pointers.

  - pass: pass-6-lead-conclusion-format
    finding: "no findings"
    scoped_to: |
      6A lead anchor: §1 ¶1 puts patent + mechanism on the table by sentence 2; full two-sided
      call by lead's end (§1 ¶2). 6B frame closure: corporate-narrative-friction lead closed in
      §6; firm posture -> closing-forward-watching-event (end-2026 Jalapeño; examination fate).
      6C Sources: "# Sources" once (line 89); 4 categories (Patents / Official statements / News &
      media / Technical specs) all within the 5-enum; ## subgrouping all-or-nothing. 6E: em-dash
      0 (independently grepped), every [dddd] 4-digit and resolving, one # Sources. 6F title
      "OpenAI's Chip Patent Does Floating-Point Math on Integer Adders" — 63 chars (< 70), no
      em-dash/colon, Title Case.
      6G OVER-HEDGE (firm posture, HIGH-if-violated), re-derived from §6: the verdict LEADS with
      the call ("'OpenAI-designed' is literal engineering, and this filing is the primary
      evidence"), not a qualifier; exactly ONE anti-hype guard, THIS-patent-specific (Jalapeño /
      no-silicon), not a generic "patents don't guarantee production" truism; caveats REFERENCED
      not re-listed ("The bounds priced in the previous section ... do not reverse it"); no
      safe-harbor boilerplate; gate_hedge PASS. Symmetric OVERREACH check: scope stays
      "sought"/"ends up owning" (pending); Rain/Allegrucci confounder priced; silicon scoped out.
      Verdict evidence-proportionate in BOTH directions. CRITICAL for this round: the r4-F1
      correction did NOT convert into a verdict hedge — it added a third independent claim to the
      core (coverage-strengthening) and left the call untouched. CLEAN.
      6H DEFENSIVE-OPEN (firm posture): §1 ¶1 opens on the discovery beat; the "pending
      application" label sits in §1 ¶2 AFTER the beat; cover caption leads with "the align-once
      core". First-two-lines test passes. CLEAN. 6I ATTENTION-BUDGET: prosecution/status narration
      confined to §5 + one lead clause + §6 recap; no spend-motif spread; the §3 steelman carries
      no procedure narration. CLEAN.

  - pass: pass-7-adversarial-reader
    finding: "no findings"
    scoped_to: |
      Read cold as the impatient investor + the skeptical pro-subject reader; each check
      decomposed yes/no with a quoted span.
      (1) HOOK: §1 ¶1 lands the discovery register declaratively ("There is a published OpenAI
      patent that designs an AI chip down to the individual memory cell. The math runs inside the
      memory array itself..."); no deferred question, no verdict-insurance fact ahead of the beat;
      two-sided call by lead's end. PASS.
      (2) HEADER-AS-CLAIM: all six ## headers are assertions; a header-only skim reconstructs the
      arc; no gap-framed header buries the discovery. PASS.
      (3) STEELMAN present + THIS-patent + not overweight: §3 ¶1-2 concede compactly that the
      format-agility headline features are description-not-claims and that block-scaled/MX is prior
      standardized art ("A skeptic can fairly call the core a known technique, implemented") — a
      THIS-patent objection, not a generic truism; affirmative return (§3 ¶3-4: claimed circuit
      specifics + primary-source depth) carries >= the concession; net-new (pending-status caveat
      spent in §5). The r4-F1 correction (third independent claim) does not weaken the steelman —
      the concession is about format-agility being unclaimed, not about the count of independent
      claims — and it STRENGTHENS the affirmative return. PASS.
      (4) META: "none is guessed at here", "The registry facts, stated once", "The bounds priced
      in the previous section" are functional scope/bridge phrasing (exempt). PASS.
      (5) JARGON as signpost: FP8/FP6/FP4, mantissa/exponent, VMM, primitive product, CIM,
      dequantization, shift register each carry a one-clause gloss; the §3 named claim blocks are
      signposted, not deep-dived. PASS.
      (6) STUB/rhythm: frame sections (§1/§6) tighter by design; none markedly short. PASS.
      (7) THESIS not over-restated: full verdict asserted in §1 ¶2 + §6 (2 sections); §3/§5 carry
      supporting sub-claims; two declared signature lines exempt. <= 3. PASS.

# ===========================================================================
# ACCEPTANCE NOTE (for the orchestrator)
# ===========================================================================
# Round 5 is CLEAN (pass; 0 findings). r4-F1 is verified LANDED and factually correct; the
# verdict was NOT hedged by the correction. Because round 4 was revise-recommended (it broke the
# prior candidate double-clean), round 5 is the FIRST of the two consecutive independent clean
# rounds the double-clean acceptance contract requires. One further fresh-context round is needed
# to CONFIRM the double-clean before the draft may be promoted to essay-final.md.
```
