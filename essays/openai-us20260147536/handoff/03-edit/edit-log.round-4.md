```yaml
review_id: openai-us20260147536-editorial-review-4
draft_source: handoff/02-compose/essay-draft.md
draft_version_reviewed: 3
review_round: 4
review_timestamp: 2026-07-09T00:00:00Z
posture_applied: measured   # 3-tier posture = measured; edition declares closing_posture: firm,
                            # so 6G/6H/6I escalate to HIGH if violated. Checked — no firm-closing
                            # violation. The one new finding is a claim-ACCURACY gap (pass-3),
                            # not a verdict-hedge/overreach issue.
closing_posture_declared: firm
gates_precomputed: PASS (0 fails). Warn signals weighed below: STRUCT-004 (4 triads),
                   DUPE-001 x2 (deliberate §1->§6 bookend), LONGSENT-001 x8. Only FIG. 1/3/4/43
                   tokens present.
reviewer_note: |
  CONFIRMATION round. Fresh round-4 reviewer, no memory of composing or of rounds 1-3, spawned
  to CONFIRM OR BREAK the candidate double-clean that round 3 opened. There has been NO revision
  since round 3 (draft v3 unchanged), so this round exists only to test whether the round-3 clean
  holds under an independent re-derivation from source. The pipeline's documented failure mode is
  a rubber-stamp confirmation, so I did NOT trust round 3: I re-byte-checked every blockquote
  against input/patent.md, re-walked the claim scope against the patent's actual claim set, opened
  and read the four figure images to check caption grounding, and re-derived the verdict
  proportionality, the lead hook, and the steelman from source.
  RESULT: the clean does NOT hold. Re-deriving the claim scope from the patent surfaced a claim-
  accuracy gap that rounds 1-3 inherited from the upstream invention-summary and did not catch:
  the patent has THREE independent claims to the core (1, 20, AND 29), but the essay (and the
  invention-summary Claim scope map it is grounded on) names only 1 and 20. One MEDIUM finding
  (r4-F1). Double-clean BROKEN.
  Re-review protocol followed: N-1 = round 3 (findings: []); all prior finding_ids
  (r1-F1..F6, r2-F1..F3) are carried and ruled in PART A before the new hunt. No id dropped.
overall_assessment: revise-recommended   # 0 critical, 0 high, 1 medium (r4-F1), 0 low.
                                         # Per feedback-format assessment table: No critical,
                                         # No high, Yes medium -> revise-recommended. This is NOT
                                         # a clean round; the candidate double-clean is broken.

# ===========================================================================
# PART A — CARRIED FINDING RULINGS
# No revision occurred after round 3, so draft v3 is byte-identical to what round 3 reviewed.
# All prior finding_ids are carried forward and independently re-confirmed on the unchanged
# draft (nothing closes silently; check_run.py id-continuity satisfied).
# ===========================================================================

carried_findings:

  - finding_id: r2-F1
    prior_disposition: applied (round 2) -> ruled LANDED-accept (round 3)
    round4_ruling: STILL LANDED — accept (re-confirmed independently on unchanged draft)
    verification: |
      Draft v3 line 15 carries the trimmed 3-sentence FIG. 4 cover caption
      ("FIG. 4: the align-once core, drawn as circuitry. ... This is claim 1's
      align-then-integer-accumulate step, made literal."). Word count ~53 / 3 sentences.
      Zero reference numerals in the caption (the "(426)" is gone). No revision since round 3,
      so the fix is intact by construction; re-read to confirm, not assumed. Grounding re-checked
      against source in pass-3 below (Emax<=22/INT5=q-0199-1; adder tree integer=q-0011-3;
      35-bit=INT35 q-0145-1; and the FIG. 4 image itself draws INT35 out + Shift Calc (EMax-E) +
      INT5(22) + Adder Tree 426 — caption claims nothing beyond the drawing).

  - finding_id: r2-F2
    prior_disposition: applied (round 2) -> ruled LANDED-accept (round 3)
    round4_ruling: STILL LANDED — accept (re-confirmed)
    verification: |
      Independent grep of draft v3 for figure tokens returns exactly FIG. 4 (header image),
      FIG. 4 (caption), FIG. 1, FIG. 3, FIG. 43 — five hits, no FIG. 38 and no FIG. 45 anywhere.
      §2 ¶4 (line 42) ends the analogy at "Here the lining up is a bit shift." and continues into
      the max-exponent sentence; §5 ¶3 (line 79) keeps the [0118] scan-test verbatim quote and
      closes before "Concept filings rarely carry clock margins and scan modes." No [dddd] anchor
      or blockquote lost. gate_figure_use / FIGREF PASS confirmed (precomputed gates).

  - finding_id: r2-F3
    prior_disposition: applied (round 2) -> ruled LANDED-accept (round 3)
    round4_ruling: STILL LANDED — accept (re-confirmed)
    verification: |
      Draft v3 line 83 reads "...priority date about eleven months older than the announcement..."
      The "about" qualifier is present, uniform with §1 ¶1. Jurisdiction fence honored: this is a
      date-arithmetic precision qualifier, not a verdict hedge — the surrounding call
      ("'OpenAI-designed' is literal engineering, and this filing is the primary evidence") is
      firm and untouched; §6 still states the raw dates two sentences later. gate_hedge firm-posture
      unaffected (6G re-derived clean below).

  # Round-1 finding_ids (r1-F1 split §2 density wall; r1-F2 split §3 dense para; r1-F3 §1 ¶2
  # "written to the bitcell"; r1-F4 §3 claim-20 fold-in precision; r1-F5 §5 "rarely carry";
  # r1-F6 §1 ¶1 "about eleven months") — all verified-landed and accepted in rounds 2-3, and
  # incidentally re-confirmed intact during this round's pass-3 grounding walk. NOT re-opened.
  #
  # NOTE on r1-F4: r1-F4 tightened the essay's statement that claim 20 (not just dependent
  # claims) folds in the shift-calculation-and-select-decoding unit. That fix is still correct as
  # far as it goes — but re-deriving the WHOLE independent-claim set from the patent this round
  # shows the same §3 sentence is now INCOMPLETE for a different reason (claim 29). That is a NEW
  # finding (r4-F1), not a regression of r1-F4; r1-F4's landed text is not reverted.

# ===========================================================================
# PART B — NEW ROUND-4 FINDINGS
# ===========================================================================

findings:

  - finding_id: r4-F1
    pass: claim-adequacy   # pass-3 (claim adequacy + fact verification); also touches pass-4
                           # (thesis-section accuracy). NOT a verdict-hedge finding.
    location: |
      §3 ¶2 (line 52: "independent claims 1 and 20 seek the multiply-align-add triad");
      §3 ¶3 (line 54: "that unit is the one piece independent claim 20 pulls up into itself...
      The dependent claims add the rest: shift registers...");
      §2 ¶3 (line 34: "What independent claims 1 and 20 seek to protect...");
      §6 ¶3 (line 87: "what examination leaves of claims 1 and 20 will fix how much of the
      align-once, integer-accumulate engine OpenAI ends up owning").
    severity: medium
    severity_under_default_posture: medium
    finding: |
      The essay treats claims 1 and 20 as the complete set of independent claims to the core
      align-once / integer-accumulate structure. Re-deriving the claim set directly from
      input/patent.md (claims listing, lines 505-525) shows there are THREE independent claims,
      not two:
        - Claim 1  (line 505): "A computing system comprising:" — the multiply-align-add triad.
        - Claim 20 (line 516): "A system comprising:" — the triad + a shift calculation and
          select decoding unit folded in.
        - Claim 29 (line 525): "A computing system comprising:" — the triad + "the functional
          block comprising a shift register" folded in.
      Claim 29 is unambiguously independent (self-contained "A computing system comprising:",
      no "according to claim N" dependency) and recites the full triad verbatim. It is the LAST
      claim in the publication (no claims 30+). The upstream invention-summary Claim scope map
      (handoff/01-design/invention-summary.md) lists only claims 1 and 20 as independent and its
      table stops at claim 28 — it omits claim 29 entirely. The composer faithfully followed that
      grounding artifact, so the ROOT CAUSE is upstream in the design phase; but the incomplete
      fact reaches publication in the essay, which is what this pass judges (north-star goal 1:
      catch the patent's core accurately).

      Two concrete inaccuracies follow from the omission:
        (a) §3 ¶3's structural story — "that unit [shift-calc-and-select-decoding] is the one
            piece independent claim 20 pulls up into itself ... The dependent claims add the
            rest: shift registers..." — is wrong on the shift register: a shift register is
            folded up into INDEPENDENT claim 29, not only added by a dependent claim (claim 3).
            So claim 20 is not "the one piece" that an independent claim promotes.
        (b) §6 ¶3's investor-facing watch-list — "what examination leaves of claims 1 and 20 will
            fix how much ... OpenAI ends up owning" — understates the robustness of OpenAI's core
            coverage. If claims 1 and 20 were both amended or rejected but 29 survived, OpenAI
            would still hold an independent claim to the core triad. For the reader whose job is
            to gauge "how much of the engine OpenAI ends up owning," a third independent shot at
            the same core is materially relevant.

      Severity note (why medium, not high): the essay is LITERALLY TRUE — claims 1 and 20 ARE
      independent — and the direction of the error is CONSERVATIVE (it understates OpenAI's
      coverage, it does not overreach). The verdict itself ("literal engineering; primary
      evidence") is unaffected and, if anything, under-supported by the omission. So it is a
      quality/accuracy gap, not a publication-blocking mislead-to-a-false-conclusion. But it is
      more than polish: it is a wrong factual claim about the patent's claim structure sitting in
      the two most load-bearing places (the §3 claim-scope resolution and the §6 verdict
      watch-list), so it routes to revision.
    recommendation: |
      Correct the claim-scope fact to the accurate independent-claim set (anchor/narrow fix —
      this STRENGTHENS the thesis; do NOT hedge the verdict). Suggested, minimal:
        - §3 ¶2 / §2 ¶3: "independent claims 1, 20, and 29" (or "the three independent claims")
          instead of "independent claims 1 and 20".
        - §3 ¶3: fix the fold-in story so it does not claim claim 20 is "the one piece" an
          independent claim promotes — e.g., note that claim 20 folds in the shift-calculation
          and select-decoding unit while claim 29 independently folds in a shift register, with
          the remaining specifics (register sizing, log-mux tree) left to the dependent claims.
        - §6 ¶3: "what examination leaves of claims 1, 20, and 29" (or "of the independent
          claims").
      Jurisdiction fence: the fix is to make the claim-scope statement accurate, never to add a
      caveat/disclaimer to the verdict. Keep the sought-* vocabulary ("seek", "ends up owning").
      UPSTREAM: this cannot be cleanly re-anchored unless the invention-summary Claim scope map
      is corrected to add claim 29 as a third independent claim — flag to the orchestrator so the
      design artifact (the composer's grounding source) is fixed alongside the essay; otherwise a
      composer edit would be un-anchorable to its own grounding file.
    quote: "independent claims 1 and 20 seek the multiply-align-add triad, not the mode decoding unit and not the format switching [0011]."

# ===========================================================================
# PART C — CLEAN PASSES (falsifiable scoped_to — exactly what was re-derived from source)
# ===========================================================================

  - pass: pass-1-voice-anti-ai
    finding: "no findings"
    scoped_to: |
      1B MECHANICAL (independently re-run this round, not inherited): scripted count over the whole
      draft — em-dash "—" = 0, en-dash "–" = 0; Tier-1 banned list (delve/tapestry/vibrant/pivotal/
      crucial/fostering/underscore/meticulous/intricate/testament/garner/bolster/showcase/enhance/
      enduring/boasts/renowned/multifaceted/leverage/navigate/resonate/nestled/groundbreaking/
      interplay) plus Tier-2 co-occurrence tells (seamless/robust/realm/utilise/facilitate/commence)
      and sentence-initial Moreover/Furthermore/Additionally = ZERO hits across the entire document
      (including blockquotes). Source-contamination guard: patent [0104] carries "crucial" (q-0104-1)
      and [0015] carries "seamless" — the composer did NOT import either ([0104] paraphrased to
      "consistent footing", only "minimize compute stalls during updates" lifted from [0015]).
      1A CADENCE: paragraph lengths 2-6 sentences; exactly one load-bearing bold anchor
      ("Align once, and the whole accumulation becomes integer arithmetic.", signature line 1,
      present once, byte-exact vs thesis-trace); both declared signature lines present once and
      byte-identical; no bold/emoji/ALL-CAPS overuse. Remaining prose semicolons (e.g. §3 ¶3 line 54,
      FIG. 1 caption line 27) join independent clauses non-mechanically; not a cluster. No AI tell.

  - pass: pass-2-redundancy
    finding: "no findings"
    scoped_to: |
      2A: core verdict lands §1 ¶2 + §6 (lead/close bookend, not padding). DUPE-001 x2 = the
      deliberate "down to the individual memory cell" §1->§6 bookend. "35-bit" recurs in the FIG. 4
      caption + §2 ¶6 + §4 with varied verbs on different surfaces (caption vs prose) — not
      same-value-3x-no-new-context. STRUCT-004 (4 triads) re-assessed: decimal-addition analogy,
      "one alignment/one integer sum/one conversion back", PVT term of art, and the tape-out-depth
      enumeration are all content-driven, not rule-of-three padding. Declared signature lines exempt.
      2C: no essay paragraph reaches 8 sentences; densest body para §3 ¶3 ~104w/4 sentences (< 150w,
      3-7 band). Figure captions are not body paragraphs.

  - pass: pass-3-fact-paraphrase
    finding: "ONE finding (r4-F1, claim-scope completeness). Verbatim quotes byte-exact; external
             facts sourced; figure captions grounded."
    scoped_to: |
      3A VERBATIM — re-byte-checked EACH blockquote/inline patent quote against input/patent.md at
      the cited paragraph (not against prior logs):
        - [0005] conversion-step blockquote (draft lines 31-32) vs patent [0005] (line 62): EXACT.
        - [0011] both claim spans (draft lines 36-38) vs patent [0011] (line 68): EXACT.
        - [0006] "without requiring separate conversion pipelines or dedicated cores for each
          format" (line 50) vs patent [0006] (line 63): EXACT.
        - [0147] pipelined-VMM blockquote (lines 62-63) vs patent [0147] (line 210): EXACT
          ("CIM macro 101 operates in a pipelined fashion, returning a VMM product (i.e., a vector
          of dot products) every cycle").
        - [0015] "minimize compute stalls during updates" (line 67) vs patent [0015] (line 72): EXACT.
        - [0154] "In some embodiments, 100% utilization of the compute engine 100 may be possible."
          (line 71) vs patent [0154] (line 213): EXACT.
        - [0118] "serve both compute storage and scan-test roles" (line 79) vs patent [0118]
          (line 180): EXACT.
        - [0133] "reducing the von Neumann bottleneck" (line 19) vs patent [0133] (line 196): EXACT.
        - "(canceled)" for claims 11-19 (line 75) vs patent (line 515): EXACT registry fact.
      3A/3C PARAPHRASE (no drift): [0142]/[0130] streaming-activation/stationary-weight datapath
      faithful (patent lines 205/203); [0131] "shrinking numbers ... minimal accuracy loss" faithful
      (patent line 193); [0104] "consistent footing" = "consistent scale" faithful, banned "crucial"
      dropped; [0139] "synthesizable integer adder tree rather than floating-point hardware" faithful
      (patent line 202: "synthesizable ... adder tree ... accumulates ... in the integer domain");
      [0183] "64 by 64 half adders and full adders ... 32-by-32 array" faithful (patent line 247,
      exponent-computation optimization over the 1x32 * 32x32 VMM); [0199]/[0200] Emax=22/INT5 and
      per-product shift = Emax - P_E faithful (patent lines 264/265); [0145] INT35+INT5 -> FP22
      faithful (patent line 208). No polarity/scope/certainty mutation in any span.
      FOUR FIGURE CAPTIONS — opened and read each cleaned image and checked caption <= drawing:
        - FIG. 4 (fig-04.png): image draws Adder Tree Col 0, Rows 0-31, Shift Calculation (EMax-E)
          3882, INT5(22) Emax, Shift>>+2's Complement 3884, Adder Tree 426, INT35 out. Caption
          ("align-once core ... shifts onto the block's largest exponent (at most 22, a 5-bit
          integer) ... column adder tree sums ... as plain integers, one 35-bit result per column")
          claims nothing beyond the drawing. Clean.
        - FIG. 1 (fig-01.png): draws Input Buffer 102, 32x32 Digital Compute-in-Memory Macro 101,
          Weight/Act inputs, Mode Decoding 110, Dequantization 106, FP22 Output. Caption matches;
          "sets the numeric format" is an anchored gloss ([0006] q-0006-1). Clean.
        - FIG. 3 (fig-03.png): draws one column cell 220 (Col 0/Row 0), SIGN/EXPONENTS/MANTISSA ->
          Exponent Handling + Mantissa Handling producing a primitive product. Caption ("one column
          cell, where a single primitive product is made") matches; short by design. Clean.
        - FIG. 43 (fig-43.png): draws bitcell_double 4303, BC0/BC1 sharing BL (BL0/BL31) with
          separate write-wordlines wwl0/wwl1. Caption ("BC0 and BC1 share bit lines but have
          separate write-wordlines, so one bank loads the next weights while the other feeds the
          running computation") matches the drawn structure; the function is anchored [0012]/[0015].
          Clean (caption stays neutral on the canceled-claim status).
      3B EXTERNAL: 10GW/2025-10-13 (tier-1) -> Official statements; Jalapeño 2026-06-24 + end-2026
      window (tier-1, "company-claimed") -> Official statements; Allegrucci ~17yr Apple / Rain
      head-of-hardware June-2024 (tier-3, labeled press-reported, bound stated) -> News & media;
      OCP MX 2023-09 seven signatories (tier-2) -> Technical specs. Every "(see Sources, X)" resolves
      to the correct category. Sixth-inventor trap avoided ("Five inventors"; Sources lists five).
      Sought-* vocabulary intact ("seek to protect"/"seek"/"wants to own"/"ends up owning"); pending
      never shown as granted. Non-load-bearing rounding cleared: "a year before" for the ~14-month
      MX(2023-09)->priority(2024-11) gap understates (weakens the essay's own concession — harmless);
      "ten gigawatts" = fact-check "10 gigawatts".
      THE ONE GAP: the independent-claim ENUMERATION is incomplete vs the patent's actual claim set
      (claim 29 is a third independent claim) — logged as r4-F1. This is the only pass-3 miss.

  - pass: pass-4-logic-causality
    finding: "no findings beyond r4-F1's §3/§6 loci"
    scoped_to: |
      4A thesis-section alignment: Axis 1 (triad) + Axis 2 (problem) -> §2; Axis 4 (baseline) +
      steelman -> §3; Axis 3 (effect) -> §4; pricing -> §5; verdict frame -> §1/§6 — all land, no
      out-of-spine claim. Figure placements match figures-rationale.md. 4B causality: the central
      inference is EVIDENTIARY, not causal — "the filing is primary evidence that 'OpenAI-designed'
      is literal engineering"; the essay never claims the patent CAUSED the announcement, so no
      correlation->causation drift from the 11-month gap. Confounders bounded: Rain/Allegrucci
      lineage priced in §5 with its limit stated; production/silicon scoped out in §6 ("no source
      shows this macro running in silicon", "nothing connects these circuits to Jalapeño"). 4C arc:
      lead tension set in §1, resolved at close; implication is this-filing-specific. The only logic
      touchpoint is r4-F1's §3 fold-in story (claim 20 is not "the one piece" an independent claim
      promotes — claim 29 promotes a shift register); ruled under r4-F1, not double-counted here.

  - pass: pass-5-reader-perspective
    finding: "no findings"
    scoped_to: |
      5A engagement: r1-F1/r1-F2 density walls stayed split; r2-F1 removed the highest-traffic
      density point (cover caption). No 3+ consecutive mechanism paragraphs without surface. 5B stake
      clarity (reader-profile money thread): every section feeds the investor verdict — §2 -> "the
      part OpenAI wants to own", §3 -> "the thesis rests on the record", §4 -> design intent, §5 ->
      "reads like engineering rather than positioning", §6 -> the call; close reads standalone.
      5C mobile: densest para §3 ¶3 ~104w/4 sentences ~ borderline at /12, clean at /15 words-per-line;
      already accepted post-r1-F2; re-splitting would fragment the §3 payoff. LONGSENT-001 x8: the
      72-word flag sits in the §2 ¶6 signature-line paragraph (protected surface — not sanded, not
      counted); the other seven are information-bearing mechanism/claim/attribution sentences under
      the patent-domain long-clause exception; none breaks readability for the advanced-HS-to-early-
      undergrad reader. Figure value-add (goal 2): four figures referenced substantively; no
      un-shown-figure pointers after r2-F2.

  - pass: pass-6-lead-conclusion-format
    finding: "no findings"
    scoped_to: |
      6A lead anchor: §1 ¶1 puts patent + mechanism on the table by sentence 2; full two-sided call
      by lead's end (§1 ¶2). 6B frame closure: corporate-narrative-friction lead closed in §6; firm
      posture -> closing-forward-watching-event (end-2026 Jalapeño; examination fate), matches spine.
      6C Sources: "# Sources" appears once (line 89); 4 categories all within the 5-enum; 5 entries
      subgrouped under ## subheads (all-or-nothing satisfied); no Papers -> 6D N/A. 6E: em-dash 0,
      every [dddd] 4-digit and resolving, one # Sources. 6F title: "OpenAI's Chip Patent Does
      Floating-Point Math on Integer Adders" — 63 chars (< 70, SURF-001 clean), no em-dash/colon,
      Title Case.
      6G OVER-HEDGE (firm posture, HIGH-if-violated) — re-derived from the §6 text: the verdict LEADS
      with the call ("'OpenAI-designed' is literal engineering, and this filing is the primary
      evidence"), not a qualifier; exactly ONE anti-hype guard and it is THIS-patent-specific
      ("nothing connects these circuits to Jalapeño ... no source shows this macro running in
      silicon"), not a generic "patents don't guarantee production" truism; caveats REFERENCED not
      re-listed ("The bounds priced in the previous section scope that call, and they do not reverse
      it"); no safe-harbor boilerplate; gate_hedge PASS. Symmetric OVERREACH check: scope stays
      "sought"/"ends up owning" (pending), the Rain/Allegrucci confounder is priced, silicon scoped
      out. Verdict evidence-proportionate in BOTH directions. NOTE: r4-F1 (claim 29 omission) does
      NOT push the verdict either way — it is a completeness gap whose correction STRENGTHENS the
      core coverage; it is filed under pass-3, and the jurisdiction fence forbids converting it into
      a verdict hedge. CLEAN.
      6H DEFENSIVE-OPEN (firm posture): §1 ¶1 opens on the discovery beat; the "pending application"
      label sits in §1 ¶2 AFTER the beat; the cover caption leads with "the align-once core", no
      verdict-insurance fact ahead of the payoff. First-two-lines test passes. CLEAN.
      6I ATTENTION-BUDGET: prosecution/status narration confined to §5 + one lead clause + §6 recap;
      no spend-motif spread; no procedure narration inside the steelman. CLEAN.

  - pass: pass-7-adversarial-reader
    finding: "no findings"
    scoped_to: |
      Read cold as the impatient investor + the skeptical pro-subject reader; each check decomposed
      yes/no with a quoted span.
      (1) HOOK: §1 ¶1 lands the discovery register declaratively ("There is a published OpenAI patent
      that designs an AI chip down to the individual memory cell. The math runs inside the memory
      array itself..."); no deferred question, no verdict-insurance fact ahead of the beat; full
      two-sided call by lead's end. PASS.
      (2) HEADER-AS-CLAIM: all six ## headers are assertions; a header-only skim reconstructs the arc;
      no gap-framed header buries the discovery. PASS.
      (3) STEELMAN present + THIS-patent + not overweight: §3 ¶1-2 concede compactly that the
      format-agility headline features are description-not-claims and that block-scaled/MX is prior
      standardized art ("A skeptic can fairly call the core a known technique, implemented") — a
      THIS-patent objection, not a generic truism; affirmative return (§3 ¶3-4: claimed circuit
      specifics + primary-source depth) carries >= the concession; net-new (pending-status caveat
      spent in §5). PASS. [Independent-of-r4-F1: the steelman does not rely on the claim count, so
      r4-F1 does not weaken it; correcting claim 29 would only strengthen the affirmative return.]
      (4) META: "none is guessed at here", "The registry facts, stated once", "The bounds priced in
      the previous section" are functional scope/bridge phrasing (exempt). PASS.
      (5) JARGON as signpost: FP8/FP6/FP4, mantissa/exponent, VMM, primitive product, CIM,
      dequantization each carry a one-clause gloss; the §3 named blocks are signposted, not
      deep-dived. PASS.
      (6) STUB/rhythm: section word counts ~156/437/320/233/245/191 — frame sections tighter by
      design; none markedly short. PASS.
      (7) THESIS not over-restated: full verdict asserted in §1 ¶2 + §6 (2 sections); §3/§5 carry
      supporting sub-claims; two declared signature lines exempt. <= 3. PASS.
```
