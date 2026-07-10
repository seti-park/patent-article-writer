```yaml
review_id: openai-us20260147536-editorial-review-6
draft_source: handoff/02-compose/essay-draft.md
draft_version_reviewed: 4
review_round: 6
review_timestamp: 2026-07-09T00:00:00Z
posture_applied: measured   # 3-tier posture = measured; edition declares closing_posture: firm,
                            # so 6G/6H/6I escalate to HIGH if violated. Checked — no firm-closing
                            # violation. This is a CONFIRMATION round on the UNCHANGED draft v4.
closing_posture_declared: firm
gates_precomputed: PASS (0 fails). Warn signals weighed below: STRUCT-004 (4 triads),
                   DUPE-001 x2 (deliberate §1->§6 bookend), LONGSENT-001 x7. Only FIG. 1/3/4/43
                   tokens present.
reviewer_note: |
  CONFIRMATION round. Fresh round-6 reviewer, no memory of composing or of rounds 1-5, spawned to
  CONFIRM OR BREAK the candidate double-clean that round 5 opened (round 5 was the FIRST clean
  after round 4 legitimately broke the prior candidate double-clean by catching an inherited
  upstream claim-scope omission — claim 29). There has been NO revision since round 5 (draft v4
  unchanged), so this round exists only to test whether the round-5 clean holds under a fully
  independent re-derivation from source. The pipeline's documented failure mode is a rubber-stamp
  confirmation, and the last confirmation round (round 4) DID break on a re-derivation — so I did
  NOT trust rounds 4 or 5, or the composer's disposition. I re-derived everything from primary
  source:
    - INDEPENDENTLY ENUMERATED the entire published claim set from input/patent.md (### Claims,
      lines 505-525), reading each claim's opening clause, to confirm the complete
      independent-claim set is EXACTLY {1, 20, 29} and that no other independent claim to the
      core exists (see PART A / r4-F1 for the full enumeration). I did NOT rely on the
      invention-summary Claim scope map or on prior logs for this.
    - Re-byte-checked all 9 verbatim patent quotes (8 spans + the "(canceled)" registry fact)
      against input/patent.md at the cited paragraph — against source, not against prior logs.
    - Re-verified every load-bearing [dddd] anchor supports its own sentence, INCLUDING three
      §5 "tape-out depth" anchors ([0234]/[0262]/[0289]) and the §4 VMM anchor [0002] that the
      prior rounds' scoped_to did not explicitly enumerate.
    - Re-ran the mechanical pass-1 checks (em-dash, en-dash, banned-word grep, sentence-initial
      transitions) by script over the whole draft, not inherited from the gate line.
    - Re-derived the verdict proportionality (both directions), the lead hook, and the steelman
      from source; confirmed the firm posture holds with no over-hedge AND no overreach.
    - Re-checked the four figure captions against input/figures/figures-manifest.md for
      claim-beyond-drawing.
  RESULT: the clean HOLDS. Independent claim enumeration is {1, 20, 29}, complete and correct,
  and the essay now states exactly that (zero leftover "claims 1 and 20"). All quotes byte-exact,
  all anchors support their sentences, verdict firm-and-proportionate both ways, all four captions
  within their drawings. ZERO new medium+ findings across all 7 passes. This is a CLEAN round and
  the SECOND consecutive independent clean, so it COMPLETES the double-clean.
  Re-review protocol followed: N-1 = round 5. Every carried finding_id (r4-F1; r2-F1..F3;
  r1-F1..F6) is ruled in PART A before the new hunt. No id dropped; check_run.py id-continuity
  satisfied.
overall_assessment: pass   # 0 critical, 0 high, 0 medium, 0 low. Per feedback-format assessment
                           # table (No critical, No high, No medium) -> pass. Clean round.
                           # This is the SECOND consecutive independent clean after the round-4
                           # break; round 5 + round 6 = the two consecutive independent cleans the
                           # double-clean acceptance contract requires. Double-clean COMPLETE.

# ===========================================================================
# PART A — CARRIED FINDING RULINGS
# No revision occurred after round 5, so draft v4 is byte-identical to what round 5 reviewed.
# Every prior finding_id is carried and independently re-confirmed on the current draft — each
# spot-verified on the live text, none assumed from the prior log. Nothing closes silently.
# ===========================================================================

carried_findings:

  - finding_id: r4-F1
    pass: claim-adequacy   # pass-3 (claim adequacy) + pass-4 (thesis-section accuracy)
    prior_disposition: applied (round 4) -> ruled LANDED-accept (round 5)
    round6_ruling: STILL LANDED — accept. Re-verified against my OWN enumeration of
                   input/patent.md, NOT against the round-4/5 rulings or the disposition note.
    verification: |
      INDEPENDENT CLAIM ENUMERATION (re-derived from input/patent.md, ### Claims, lines 505-525,
      by reading each claim's opening clause — the exact test round 4 used to break the prior
      candidate double-clean):
        - Claim 1  (line 505): "A computing system comprising:" — self-contained, no "according
          to claim N". INDEPENDENT. Recites the full triad: (a) column cell -> primitive product
          in a floating point format; (b) functional block aligning mantissa bits BY SHIFTING;
          (c) adder tree outputting an accumulation value in an INTEGER format.
        - Claims 2-10 (lines 506-514): each opens "The computing system according to claim N"
          (2->1, 3->2, 4->3, 5->4, 6->3, 7->6, 8->6, 9->6, 10->1) — DEPENDENT.
        - Claims 11-19 (line 515): "(canceled)".
        - Claim 20 (line 516): "A system comprising:" — self-contained. INDEPENDENT. Triad +
          "the functional block comprises a shift calculation and select decoding unit ... to
          determine a shift value" folded into the independent claim.
        - Claims 21-28 (lines 517-524): each "The computing system according to claim 1/21/25"
          (21->1, 22->21, 23->21, 24->1, 25->1, 26->25, 27->1, 28->1) — DEPENDENT.
        - Claim 29 (line 525): "A computing system comprising: a compute-in-memory (CIM) macro
          configured to perform a vector matrix multiplication (VMM) operation ... a column cell
          ... a functional block ... the functional block comprising a shift register; and an
          adder tree ... in an integer format ...". Self-contained, no "according to claim N".
          INDEPENDENT. Full triad + a shift register folded into the functional block, CIM
          configured for a VMM. It is the LAST claim in the publication — no claims 30+.
      => The complete independent-claim set is EXACTLY {1, 20, 29}. CONFIRMED by my own read.
         No other claim opens independently; every claim 2-28 (minus canceled 11-19) is a
         "according to claim N" dependent. Claim 29 unambiguously recites the multiply-align-add
         triad. The essay's enumeration is COMPLETE and CORRECT (it says "1, 20, and 29" — the
         true set — with no over-claim to "three-plus").

      FOUR LOCI on draft v4 — each landed and each accurate against the claim text:
        (a) §2 ¶3 (line 34): "What independent claims 1, 20, and 29 seek to protect is a structure
            that pays that cost once." [0011] carries the triad. Correct.
        (b) §3 ¶2 (line 52): "independent claims 1, 20, and 29 seek the multiply-align-add triad,
            not the mode decoding unit and not the format switching [0011]." Correct — none of
            claims 1/20/29 recites a mode decoding unit or format switching (verified against the
            claim text: claim 1 bare triad; claim 20 adds only the shift-calc/select-decoding
            unit; claim 29 adds only a shift register + the VMM framing). The mode decoding unit
            is description material ([0006]/[0146]), not a claim element.
        (c) §3 ¶3 (line 54): "Claim 20 folds in a shift calculation and select decoding unit that
            works out each product's shift [0200], and claim 29 pulls in a shift register, each
            carried alongside the same multiply-align-add triad. The dependent claims add the
            specifics: the shift register sized by rule to the maximum exponent plus the mantissa
            bit count [0202], and a logarithmic multiplexer tree that does the shifting in stages
            [0206]." ALL ACCURATE:
              - claim 20 independently folds in the shift calculation and select decoding unit
                (line 516) — anchor [0200] describes the shift-value computation Emax - P_E
                (patent line 265). Correct.
              - claim 29 independently folds in a bare shift register (line 525). Correct.
              - the SIZING rule (bits = Emax + mantissa bit count) is a DEPENDENT specific
                (claim 3, line 507; anchor [0202], patent line 267: "a number of bits that equals
                Emax plus the number of mantissa bits (e.g., 7b+22b=29b)"). Correctly attributed.
              - the logarithmic multiplexer tree is a DEPENDENT specific (claim 6, line 510;
                anchor [0206], patent line 271: "a plurality of multiplexers 3972 formed as a
                logarithmic tree"). Correctly attributed.
            The previously-false round-1..3 framing ("that unit is the one piece independent
            claim 20 pulls up into itself ... dependent claims add the rest: shift registers") is
            GONE; the shift register is correctly shown folded into INDEPENDENT claim 29. No fact
            misstated. The "64 by 64 half adders" [0183] sentence is kept and correctly attributed
            to the description ([0183], patent line 247: "64x64 number of half adders and full
            adders can be saved" for the exponent-computation optimization over the 1x32 * 32x32
            VMM).
        (d) §6 ¶3 (line 87): "what examination leaves of claims 1, 20, and 29 will fix how much of
            the align-once, integer-accumulate engine OpenAI ends up owning." Correct; sought-*
            vocabulary ("ends up owning") preserved.
      MECHANICAL SWEEP: draft carries "1, 20, and 29" exactly 3x (lines 34/52/87) and "1 and 20"
      exactly 0x (scripted count). No leftover two-claim framing survives anywhere.

      VERDICT NOT HEDGED (jurisdiction fence honored). The r4-F1 correction is coverage-
      STRENGTHENING (a third independent claim to the same core), applied as an accurate-
      enumeration fix — no caveat/disclaimer/hedge added. §6 ¶1 still LEADS with the firm call;
      the single THIS-patent anti-hype guard (Jalapeño / no-silicon) unchanged and not re-listed;
      caveats referenced not re-stacked. gate_hedge PASS. 6G re-derived clean (PART C).

      NEIGHBOR REGRESSION (the r4-F1 §3 ¶3 rework was the only structural edit in the whole
      draft's history since round 4). Re-counted the band: §3 is four paragraphs (lines 50/52/
      54/56); ¶3 is 5 sentences / ~112 words (in the 3-7 band, < 150 words, no STRUCT-001
      exposure). r1-F2's ¶3/¶4 split preserved. No figure token, blockquote, or [dddd] anchor
      added or lost. Accept.

  # -------------------------------------------------------------------------
  # Older carried ids — re-confirmed STILL LANDED on the unchanged draft v4. Each spot-verified
  # on the live text this round (not assumed). None re-opened.
  # -------------------------------------------------------------------------

  - finding_id: r2-F1
    prior_disposition: applied (r2) -> LANDED (r3, r4, r5)
    round6_ruling: STILL LANDED — accept
    verification: |
      FIG. 4 header caption (line 15) is the trimmed 3-sentence / ~53-word cover caption, ZERO
      reference numerals (the "(426)" is gone), ending "This is claim 1's
      align-then-integer-accumulate step, made literal." Grounding re-checked in pass-3
      (Emax<=22/INT5 [0199]; adder tree integer [0011]; 35-bit [0145]); caption claims nothing
      beyond the FIG. 4 drawing per figures-manifest (adder tree 3880/3882/3884/426, per-row
      shift calculation Emax-E, 2's-complement shift).

  - finding_id: r2-F2
    prior_disposition: applied (r2) -> LANDED (r3, r4, r5)
    round6_ruling: STILL LANDED — accept
    verification: |
      Scripted figure-token count over draft v4 returns EXACTLY {FIG. 4 x2 (header image alt +
      caption), FIG. 1, FIG. 3, FIG. 43} — NO FIG. 38, NO FIG. 45 anywhere. gate_figure_use /
      FIGREF PASS (precomputed). The §2 ¶4 bit-shift sentence still ends at "Here the lining up is
      a bit shift." (line 42); §5 ¶3 still closes on the [0118] scan-test quote (line 79).

  - finding_id: r2-F3
    prior_disposition: applied (r2) -> LANDED (r3, r4, r5)
    round6_ruling: STILL LANDED — accept
    verification: |
      §6 ¶1 (line 83) reads "...priority date about eleven months older than the announcement..."
      — the "about" qualifier present, uniform with §1 ¶1 ("about eleven months later", line 19).
      Date-arithmetic precision, not a verdict hedge; surrounding call firm and untouched.

  - finding_id: r1-F1
    prior_disposition: applied (r1) -> LANDED (r2-r5)
    round6_ruling: STILL LANDED — accept
    verification: |
      §2 density split intact: line 42 ends "...on a consistent footing before the sum [0104].";
      line 44 opens a fresh paragraph "The numbers stay small by design...". No re-merge.

  - finding_id: r1-F2
    prior_disposition: applied (r1) -> LANDED (r2-r5)
    round6_ruling: STILL LANDED — accept (re-counted because §3 ¶3 was the r4-F1 edit locus). §3
                   remains four paragraphs (lines 50/52/54/56); the ¶3/¶4 split holds; ¶3 stays
                   in-band at 5 sentences / ~112 words.

  - finding_id: r1-F3
    prior_disposition: applied (r1) -> LANDED (r2-r5)
    round6_ruling: STILL LANDED — accept. §1 ¶2 (line 21) carries "the math engine was already on
                   file, written to the bitcell"; depth-motif de-duplication holds.

  - finding_id: r1-F4
    prior_disposition: applied (r1) -> LANDED (r2-r5); SUBSUMED-CORRECTLY by r4-F1
    round6_ruling: STILL LANDED — accept. r1-F4's landed fact (the shift-calc-and-select-decoding
                   unit is folded into INDEPENDENT claim 20, not dependent-only) is preserved in
                   the r4-F1 rework ("Claim 20 folds in a shift calculation and select decoding
                   unit ... [0200]", line 54). Not reverted.

  - finding_id: r1-F5
    prior_disposition: applied (r1) -> LANDED (r2-r5)
    round6_ruling: STILL LANDED — accept. §5 ¶3 (line 79): "Concept filings rarely carry clock
                   margins and scan modes." — "rarely" (not "do not") intact; verdict untouched.

  - finding_id: r1-F6
    prior_disposition: applied (r1) -> LANDED (r2-r5)
    round6_ruling: STILL LANDED — accept. §1 ¶1 (line 19) carries "about eleven months later";
                   uniform with the §6 recap.

# ===========================================================================
# PART B — NEW ROUND-6 FINDINGS
# ===========================================================================

findings: []   # No new critical/high/medium/low findings. See PART C for the falsifiable
               # scoped_to of each pass's independent re-derivation from source.

# ===========================================================================
# PART C — CLEAN PASSES (falsifiable scoped_to — exactly what was re-derived from source)
# ===========================================================================

clean_passes:

  - pass: pass-1-voice-anti-ai
    finding: "no findings"
    scoped_to: |
      1B MECHANICAL (scripted over the WHOLE draft this round, not inherited): em-dash "—" = 0,
      en-dash "–" = 0 (including blockquotes). Tier-1 banned list (delve/tapestry/vibrant/pivotal/
      crucial/fostering/underscore/meticulous/intricate/testament/garner/bolster/showcase/enhance/
      enduring/valuable/boasts/renowned/multifaceted/leverage/navigate/resonate/nestled/
      groundbreaking/interplay) + Tier-2 co-occurrence tells (seamless/robust/realm/utilise/
      facilitate/commence/deep dive/going forward/ring-fence) = ZERO hits. No sentence-initial
      Additionally/Moreover/Furthermore, and none mid-sentence in prose. SOURCE-CONTAMINATION
      guard re-checked on quoted paragraphs: patent [0154] (line 213) carries
      "crucial"/"leverage"/"Additionally"/"Furthermore", [0015] (line 72) carries "seamless",
      [0104] carries "crucial" — the composer imported NONE ([0154] lifts only the 100%-utilization
      span; [0015] lifts only "minimize compute stalls during updates"; [0104] paraphrased to
      "consistent footing"). The single "!" in the file is the FIG. 4 image-embed markdown
      `![...]` on line 13, not body prose — EXCLAIM-001 correctly does not fire. No copula
      avoidance (is/are throughout; no "serves as a/stands as a"). 1A CADENCE: exactly one
      load-bearing bold anchor (signature line 1, line 46) present once, byte-exact; signature
      line 2 (line 87) present once, byte-exact; no bold/emoji/ALL-CAPS overuse. §3 ¶3's two
      list-introducing colons follow COMPLETE clauses (legitimate elaboration, not "fragment:
      payoff" tell). No AI tell.

  - pass: pass-2-redundancy
    finding: "no findings"
    scoped_to: |
      2A: core verdict lands §1 ¶2 + §6 (lead/close bookend, not padding). DUPE-001 x2 = the
      deliberate "down to the individual memory cell" §1 (line 19) -> §6 (line 83) bookend
      (acceptable lead->close circle-back). No same-value-3x-without-new-context: "35-bit"/INT35
      recurs on distinct surfaces (cover caption vs §2 prose vs §4) each carrying new context.
      STRUCT-004 (4 triads) = decimal-addition analogy, "one alignment/one integer sum/one
      conversion back", PVT term of art, tape-out-depth enumeration — all content-driven, not
      rule-of-three padding. Declared signature lines exempt from echo/count rules. 2C: scripted
      max prose-paragraph sentence count = 6 (< 8, no STRUCT-001); densest body para §3 ¶3
      ~112 words (< 150). Figure captions are not body paragraphs.

  - pass: pass-3-fact-paraphrase
    finding: "no findings. All 9 verbatim quotes byte-exact; every anchor supports its sentence;
             four figure captions grounded; independent-claim enumeration complete and correct."
    scoped_to: |
      3A VERBATIM — re-byte-checked EACH patent quote against input/patent.md at the cited
      paragraph (against SOURCE, not prior logs):
        - [0005] conversion-step blockquote (draft 31-32) vs patent line 62: EXACT.
        - [0011] both claim spans (draft 36-37) vs patent line 68: EXACT.
        - [0006] "without requiring separate conversion pipelines or dedicated cores for each
          format" (draft 50) vs patent line 63: EXACT.
        - [0147] pipelined-VMM blockquote (draft 62-63) vs patent line 210: EXACT (patent bolds
          the reference number "**101**" as markdown emphasis; textual content identical).
        - [0015] "minimize compute stalls during updates" (draft 67) vs patent line 72: EXACT.
        - [0154] "In some embodiments, 100% utilization of the compute engine 100 may be
          possible." (draft 71) vs patent line 213: EXACT ("**100**" bolded in source only).
        - [0118] "serve both compute storage and scan-test roles" (draft 79) vs patent line 180:
          EXACT.
        - [0133] "reducing the von Neumann bottleneck" (draft 19 + 25) vs patent line 196: EXACT.
        - "(canceled)" for claims 11-19 (draft 75) vs patent line 515: EXACT registry fact.
      3A/3C ANCHOR SUPPORT (each [dddd] verified against the source paragraph, full sweep):
        - [0002] (draft §4 line 65, "the operation that dominates AI training and inference") vs
          patent line 58: [0002] positions matrix-vector multiplication as "a fundamental
          computational operation ... including ... machine learning" that composes into neural
          network layers; the "dominates AI training and inference" gloss is corroborated by
          [0004]/[0005] and matches the invention-summary's own "[0002][0004]" anchoring. Faithful,
          not overstated. (Prior rounds did not enumerate [0002]; re-checked and clean.)
        - [0130] FP8/FP6/FP4 activations vs FP6/FP4 weights (draft §2/§3) vs patent line 192:
          faithful. [0131] minimal-accuracy-loss (draft §2 ¶3) vs patent line 193: faithful.
        - [0133] math within memory array (draft §1) vs patent line 196: faithful.
        - [0139] synthesizable integer adder tree vs FP hardware (draft §2 ¶6) vs patent line 202
          ("synthesizable ... adder tree ... accumulates ... in the integer domain"): faithful.
        - [0141] blocks of 32 sharing one scaling factor (draft §3 ¶1) vs patent line 204:
          faithful. [0142] input buffer / streaming activations (draft §2 ¶2 + FIG. 1 caption) vs
          patent line 205: faithful. [0145] INT35+INT5 -> FP22 (draft §2 ¶5 + captions) vs patent
          line 208: faithful.
        - [0199] Emax=22 / INT5 for FP8xFP6 (draft §2 ¶2 + cover caption) vs patent line 264:
          faithful. [0200] shift value = Emax - P_E (draft §2 ¶3 + §3 ¶3) vs patent line 265:
          faithful. [0202] shift register bits = Emax + mantissa bits (draft §3 ¶3) vs patent
          line 267: faithful, correctly attributed to a DEPENDENT specific. [0206] logarithmic
          multiplexer tree (draft §3 ¶3) vs patent line 271: faithful, DEPENDENT specific.
        - [0183] "64 by 64 half adders and full adders ... 32-by-32 array" (draft §3 ¶3) vs patent
          line 247: faithful, correctly attributed to the description.
        - [0104] "consistent footing" (draft §2 ¶3) = [0104] "consistent scale" (banned "crucial"
          dropped): faithful. [0012] parallel write+VMM double bitcells (draft §4) vs patent
          line 69: faithful.
        - §5 tape-out-depth trio re-derived from source (prior rounds' scoped_to did not
          enumerate these): [0234] (patent line 299, "setup time with respect to the weight clock
          signal") supports "setup-time relations"; [0262] (patent line 312, "check timing and
          margin very carefully across many processes, voltages and temperatures (PVTs)") supports
          "timing checks across process, voltage, and temperature corners"; [0289] (patent
          line 339, "generating two non-overlapping clock signals") supports "non-overlapping
          clock generation" and "latch-level bitcell circuits". All three faithful and correctly
          grouped. No polarity/scope/certainty mutation in any span.
      FOUR FIGURE CAPTIONS re-checked against input/figures/figures-manifest.md (caption <= drawing):
        - FIG. 4 header (line 13-15): align-once core; mantissa shifts onto largest exponent
          (<=22, 5-bit int); column adder tree sums as integers; one 35-bit result per column;
          claim-1 tie — all within manifest FIG. 4 (adder tree 3880/3882/3884/426; Emax-E shift;
          2's-complement) + anchors [0199]/[0011]/[0145]. Nothing beyond the drawing. Clean.
        - FIG. 1 (line 27): input buffer / 32x32 CIM macro (101) / mode decoding (110) sets format
          / dequantization (106) -> FP22 — matches manifest FIG. 1 block diagram; "sets the
          numeric format" is an anchored gloss ([0006]); "converts to FP22 once" ([0142]/[0145]).
          Clean.
        - FIG. 3 (line 40): "one column cell, where a single primitive product is made" — matches
          manifest FIG. 3 (column cell Col 0/Row 0); [0011]. Clean.
        - FIG. 43 (line 69): "BC0 and BC1 share bit lines but have separate write-wordlines, so
          one bank loads the next weights while the other feeds the running computation" — the
          BC0/BC1-sharing-BL + separate-write-wordline structure is drawn (manifest FIG. 43:
          bitcell_double 4303, BL0-BL31, ww10/ww11); the function is anchored [0012]/[0015]. Clean.
      3B EXTERNAL: 10GW / 2025-10-13 (tier-1) -> Official statements; Jalapeño 2026-06-24 +
      end-2026 deployment window (tier-1, labeled "company-claimed") -> Official statements;
      Allegrucci ~17yr Apple / Rain head-of-hardware June-2024 (tier-3, labeled "Bloomberg
      reported", bound stated: "no document here says where any of the five sat on the provisional
      date") -> News & media; OCP MX 2023-09, seven signatories AMD/Arm/Intel/Meta/Microsoft/
      Nvidia/Qualcomm (tier-2) -> Technical specs. Every "(see Sources, X)" resolves to the correct
      category. "Five inventors" — sixth-inventor trap avoided (Sources lists five). Sought-*
      vocabulary intact ("seek to protect"/"seek"/"wants to own"/"ends up owning"); pending never
      shown as granted. Non-load-bearing rounding ("a year before" for the ~14-month MX->priority
      gap) understates the essay's OWN concession (harmless / conservative).
      CLAIM-SCOPE COMPLETENESS (the round-4 break point): independently enumerated all 29 claims
      from the patent; independent set = {1, 20, 29}, exactly what the essay states. COMPLETE and
      correct. No pass-3 miss remains.

  - pass: pass-4-logic-causality
    finding: "no findings"
    scoped_to: |
      4A thesis-section alignment: Axis 1 (triad) + Axis 2 (problem) -> §2; Axis 4 (baseline) +
      steelman -> §3; Axis 3 (effect) -> §4; pricing -> §5; verdict frame -> §1/§6 — all land, no
      out-of-spine claim; figure placements match figures-rationale.md. 4B causality: the central
      inference is EVIDENTIARY, not causal ("this filing is the primary evidence that
      'OpenAI-designed' is literal engineering"); the essay never claims the patent CAUSED the
      announcement, so no correlation->causation drift from the 11-month gap. Confounders bounded:
      Rain/Allegrucci lineage priced in §5 with its limit stated; production/silicon scoped out in
      §6 ("no source shows this macro running in silicon", "nothing connects these circuits to
      Jalapeño"). The double-buffering is explicitly narrated as unclaimed ("in its summary
      passages rather than in the claims it is seeking", §4) and design-intent not measurement
      ("These are design statements by an applicant, not measurements of silicon"). 4C arc: lead
      tension set §1, resolved §6; implication is this-filing-specific.

  - pass: pass-5-reader-perspective
    finding: "no findings"
    scoped_to: |
      5A engagement: density splits (r1-F1 §2, r1-F2 §3) and the trimmed cover caption (r2-F1)
      hold; no 3+ consecutive mechanism paragraphs without a surface. The §3 ¶3 claim machinery is
      translated for the target reader ("shift calculation and select decoding unit that works out
      each product's shift"; "shift register"), meeting the reader-profile "translate, then quote"
      rule; no unglossed legalese. 5B stake clarity (money thread): every section feeds the
      investor verdict — §2 -> "the part OpenAI wants to own", §3 -> "the thesis rests on the
      record", §4 -> design intent, §5 -> "reads like engineering rather than positioning", §6 ->
      the call; the close reads standalone. 5C mobile: densest para §3 ¶3 ~112w / 5 sentences,
      clean at /15 words-per-line; re-splitting would fragment the §3 payoff. LONGSENT-001 x7:
      information-bearing mechanism/claim/attribution sentences under the patent-domain
      long-clause exception; none breaks readability for the advanced-HS-to-early-undergrad reader.
      Quantitative claims land on a familiar scale (mantissa/exponent glossed; INT5/INT35 glossed).
      Four figures referenced substantively; no un-shown-figure pointers.

  - pass: pass-6-lead-conclusion-format
    finding: "no findings"
    scoped_to: |
      6A lead anchor: §1 ¶1 puts patent + mechanism on the table by sentence 2; full two-sided
      call by lead's end (§1 ¶2). 6B frame closure: corporate-narrative-friction lead closed in
      §6; firm posture -> closing-forward-watching-event (end-2026 Jalapeño; examination fate),
      matches spine. 6C Sources: "# Sources" once (line 89); 4 categories (Patents / Official
      statements / News & media / Technical specs), all within the 5-enum; 5 entries subgrouped
      under ## subheads (all-or-nothing satisfied); no Papers -> 6D N/A. 6E: em-dash 0
      (scripted), every [dddd] 4-digit and resolving, one # Sources. 6F title "OpenAI's Chip
      Patent Does Floating-Point Math on Integer Adders" — 63 chars (< 70, SURF-001 clean), no
      em-dash, no colon, Title Case. Title claim is substantively accurate (the ACCUMULATION of
      FP products runs on integer adders; the body immediately scopes multiply-as-FP), and it is
      protected energy-contract surface — not sanded.
      6G OVER-HEDGE (firm posture, HIGH-if-violated), re-derived from §6: the verdict LEADS with
      the call ("'OpenAI-designed' is literal engineering, and this filing is the primary
      evidence"), not a qualifier; exactly ONE anti-hype guard, THIS-patent-specific (Jalapeño /
      no-silicon), not a generic "patents don't guarantee production" truism; caveats REFERENCED
      not re-listed ("The bounds priced in the previous section ... do not reverse it"); no
      safe-harbor boilerplate; gate_hedge PASS. Symmetric OVERREACH check: scope stays
      "sought"/"ends up owning" (pending), Rain/Allegrucci confounder priced, silicon scoped out.
      Verdict evidence-proportionate in BOTH directions. The r4-F1 correction did NOT convert into
      a verdict hedge (it added a third independent claim, coverage-strengthening). CLEAN.
      6H DEFENSIVE-OPEN (firm posture): §1 ¶1 opens on the discovery beat; the "pending
      application" label sits in §1 ¶2 AFTER the beat; cover caption leads with "the align-once
      core". First-two-lines test passes. CLEAN. 6I ATTENTION-BUDGET: prosecution/status narration
      confined to §5 + one lead clause + §6 recap; no spend-motif spread; the §3 steelman carries
      no procedure narration. CLEAN.

  - pass: pass-7-adversarial-reader
    finding: "no findings"
    scoped_to: |
      Read cold as the impatient investor + the skeptical pro-subject reader; each check decomposed
      yes/no with a quoted span.
      (1) HOOK: §1 ¶1 lands the discovery register declaratively ("There is a published OpenAI
      patent that designs an AI chip down to the individual memory cell. The math runs inside the
      memory array itself..."); no deferred question, no verdict-insurance fact ahead of the beat;
      two-sided call by lead's end. PASS.
      (2) HEADER-AS-CLAIM: all six ## body headers are assertions; a header-only skim reconstructs
      the arc (on file before news -> multiply-FP/add-int -> described vs claimed -> result every
      cycle -> pending but tape-out-depth -> literal engineering, two dates); no gap-framed header
      buries the discovery. PASS.
      (3) STEELMAN present + THIS-patent + not overweight: §3 ¶1-2 concede compactly that the
      format-agility headline features are description-not-claims and that block-scaled/MX is prior
      standardized art ("A skeptic can fairly call the core a known technique, implemented") — a
      THIS-patent objection, not a generic truism; affirmative return (§3 ¶3-4: claimed circuit
      specifics + primary-source depth, "the thesis rests on the record") carries >= the
      concession; net-new (pending-status caveat spent in §5); no spend/procedure motif inside the
      beat. The r4-F1 correction does not weaken it (the concession is about format-agility being
      unclaimed, not about the count of independent claims) and strengthens the affirmative
      return. PASS.
      (4) META: "none is guessed at here", "The registry facts, stated once", "The bounds priced
      in the previous section" are functional scope/bridge phrasing (exempt). PASS.
      (5) JARGON as signpost: FP8/FP6/FP4, mantissa/exponent, VMM, primitive product, CIM,
      dequantization, shift register each carry a one-clause gloss; the §3 named claim blocks are
      signposted, not deep-dived. PASS.
      (6) STUB/rhythm: section word counts ~156/437/320/233/245/191 — frame sections (§1/§6)
      tighter by design; none markedly short. PASS.
      (7) THESIS not over-restated: full verdict asserted in §1 ¶2 + §6 (2 sections); §3/§5 carry
      supporting sub-claims; two declared signature lines exempt. <= 3. PASS.

# ===========================================================================
# ACCEPTANCE NOTE (for the orchestrator)
# ===========================================================================
# Round 6 is CLEAN (pass; 0 findings). It was run as a fresh-context CONFIRMATION with a full
# re-derivation from primary source — the independent-claim enumeration ({1, 20, 29}, complete
# and correct by my own read of input/patent.md), all 9 verbatim quotes byte-exact, every anchor
# supporting its sentence, the verdict firm-and-proportionate in both directions, and all four
# figure captions within their drawings. r4-F1 is verified LANDED and factually correct; no
# carried id was dropped.
#
# Round 5 was the FIRST clean after the round-4 break; round 6 is the SECOND consecutive
# independent clean. Rounds 5 + 6 therefore satisfy the double-clean acceptance contract. The
# draft (draft_version 4) may be promoted to essay-final.md, subject to check_run.py confirming
# the loop shape (contiguous round artifacts, disposition coverage, id continuity).
```

## 2026-07-10 post-accept revision (origin: owner-directed, drafted by Grok 4.5)
- EDIT 1 essay-final.md: gloss von Neumann bottleneck after [0133]
- EDIT 2 essay-final.md: first-use gloss on dot products
- EDIT 3 essay-final.md: FIG. 1 caption story-then-labels
- EDIT 4 essay-final.md: bit-width ceiling sizing so-what [0202]
- EDIT 5 essay-final.md: dequantization job-first with [0005]
- EDIT 6 essay-final.md: split synthesizable adder-tree sentence
- EDIT 7 essay-final.md: first-use gloss on independent claims
- EDIT 8 essay-final.md: gloss multiplexer tree and adders
- EDIT 9 owner-briefing.md: claim 29 independent-claim completeness
- EDIT 10 owner-briefing.md: section 3 scannable bullets
- EDIT 11 owner-briefing.md: INT35/INT5 plain-Korean gloss
- EDIT 12 edit-log.md: provenance append for this revision
