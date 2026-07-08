# Edit Log — Round 4 (confirmation round: independent full review of the unrevised v3 draft)

```yaml
review_id: etched-us20240378175-editorial-review-4
draft_source: handoff/02-compose/essay-draft.md
publication_strip: handoff/02-compose/publication.md
review_timestamp: 2026-07-04T00:00:00Z
review_round: 4
round_type: confirmation (no revision since round 3; revision-response.round-3.md is an orchestrator transition record)
draft_version_reviewed: 3
posture_applied: measured
closing_posture_declared: firm
edition: pending-application (input/essay-context.md controls)
overall_assessment: pass
assessment_rationale: |
  Independent full 7-pass review of draft_version 3, treating round 3's pass as a
  hypothesis. Everything was re-derived from the sources, not inherited: every quoted
  span re-located in patent.md (byte-level; the three initial grep misses traced to the
  markdown conversion's non-breaking spaces around reference numerals, U+00A0 — texts
  identical after NBSP normalization); every claim-content statement re-checked against
  the actual claims 1-42 at the end of patent.md; all five placed figures re-read with
  my own eyes (FIG. 6's 605/610 assignment re-confirmed against the drawing: 605A-D are
  the blocks INSIDE ICs 615A-D, 610A-D the external chips — the draft caption is right,
  the manifest one-liner is wrong, fourth consecutive independent confirmation); the
  gate-result.round-4 warn profile re-judged on merits, not inherited. Because a clean
  confirmation must be falsifiable, I hunted specifically in the places rounds 1-3 did
  not flag: the §6 family sentence, the §7 verdict paragraph's internal repetition, and
  the essay's recurring two-sentence contrast figure. That hunt produced THREE new lows
  (r4-F1 unglossed "continuation"/"family" terms of art; r4-F2 founders-authorship
  stated three times inside §7; r4-F3 the "not X. It is Y" cadence figure used four
  times) and nothing at medium or above. One carried low stays open by design (r3-F1,
  deferred to self-audit; deferral accepted). Zero critical, zero high, zero medium:
  per the assessment rules this round is PASS — the second consecutive clean round from
  an independent reviewer. Double-clean is achieved from this side. The open lows
  (r3-F1, r4-F1, r4-F2, r4-F3) do not block acceptance and should travel to the
  post-acceptance self-audit queue.

# ------------------------------------------------------------------
# PART 1 — Re-review protocol: ruling on the carried round-3 state
# ------------------------------------------------------------------

carried_finding_rulings:

  - finding_id: r3-F1
    prior_severity: low
    disposition_claimed: deferred (orchestrator transition record; confirmation round takes no revision)
    ruling: deferral-accepted; finding independently re-confirmed, stays OPEN at low
    evidence: |
      Independent concurrence: I flagged the same span on my own fresh pass-5/pass-7
      read BEFORE opening round 3's log. §4 (draft line 66): "The claim language,
      mirrored in the citable summary, reads:" — "the citable summary" is unglossed
      insider phrasing; the target reader cannot know it means the application's own
      Summary section ([0016]), which mirrors claim 39 near-verbatim (sole difference
      "where"/"wherein", re-verified this round against claim 39's text). The quote
      chain itself is accurate; this is purely a gloss-clarity polish. Round 3's
      recommendation stands ("repeated word for word in the application's own summary
      section"). Low does not block double-clean; deferral to self-audit revision mode
      is a legitimate disposition, not a silent drop.

# ------------------------------------------------------------------
# PART 2 — Finding-id lifecycle: ruling on every id mentioned in round 3's log
# (no revision occurred, so the ruling is: does each closure still stand in v3?
#  Each was independently spot-verified in the current draft, not inherited.)
# ------------------------------------------------------------------

finding_id_lifecycle:
  - {finding_id: r1-F1, status: closed-verified (round 2), round-4 ruling: standing — §4 "with its space and power" and the bridge "The filing books the gain as space and power [0045]. Latency is the word the 2026 thread added." both present (draft lines 64, 77); independently re-verified `grep -ci latenc` on input/patent.md = 0, and the draft's only "latency" uses are company-attributed (lines 21, 77)}
  - {finding_id: r1-F2, status: closed-verified (round 2, grounding-substitution accepted), round-4 ruling: standing — §3 "a machine you build when one workload, transformer inference... deserves its own dedicated hardware" (line 55); §5 "Not everything here is that committed. The broad combined-array claims carry no AI limitation as drafted, and neither does claim 39's memory interface" (line 96); independently re-confirmed against the claims text: claims 1, 26, 39 carry no AI limitation as drafted (AI enters via claim 15 and dependents 6/12/40); the round-2 acceptance of the scope-map grounding is CONCURRED with}
  - {finding_id: r1-F3, status: closed-verified (round 2), round-4 ruling: standing — all three rewrites present verbatim ("One distinction carries all the weight." line 29; "Both halves of that record matter:..." line 100; "The rejection record and the blanket liens scope this call without softening it." line 112); my own pass-7 meta sweep of v3 found no essay-self-reference cluster}
  - {finding_id: r1-F4, status: closed-verified (round 2, residuals accepted), round-4 ruling: standing — collateral beat is ONE paragraph (line 102), independently re-counted at 7 sentences / ~174 words with all six contract elements; residual acceptance concurred (the length floor is the edition contract itself)}
  - {finding_id: r1-F5, status: closed-verified (round 2), round-4 ruling: standing — full thesis formula in exactly three sections (§1 line 19, §4 bold anchor line 75, §7 line 114); §3/§5 forward-pointer closers intact ("And the design commits hardest on the memory side." / "It is what the document describing it is worth."); my independent pass-7 check 7 count concurs (≤3)}
  - {finding_id: r1-F6, status: closed-verified (round 2), round-4 ruling: standing — Sources entry (line 121) carries only anchored fields: "US 12,361,091 B1, Etched.ai, Inc., granted 2025-07-15 (the \"wiring half,\" subject of the companion analysis)"; no unanchored title/priority/inventor fields; no silent evidence_level upgrade found anywhere in Sources}
  - {finding_id: r1-F7, status: closed-verified (round 2), round-4 ruling: standing — §7 line 112: "the likeliest survivor among the application's four independent claims, the ones that stand on their own rather than adding to another"; independently re-verified against patent.md claims: exactly four independents (1, 15, 26, 39)}
  - {finding_id: r1-F8, status: closed-verified (round 2), round-4 ruling: standing — §3 line 49: "roughly a whole laptop's storage"; comparator survives scrutiny; footnote label accurate}
  - {finding_id: r1-F9, status: closed-verified (round 2), round-4 ruling: standing — "In plain terms, that means..." (line 36), "In translation, each memory channel..." (line 66), and "The bandwidth follows:" as the single surviving colon pivot (line 71); no announcement-colon cluster in v3}
  - {finding_id: r1-F10, status: closed-verified (round 2), round-4 ruling: standing — lead split present: "...as loan collateral. Meanwhile the philosophy it wrote down is presented on stage as shipping hardware." (line 19)}
  - {finding_id: r2-F1, status: closed-verified (round 3), round-4 ruling: standing, independently re-verified against fig-07.png AND [0055]-[0057] — the caption's two factual claims both check: "at Time A a new computation has already entered while the previous one drains" = [0056] (leftmost DPU on MLP output layer while rightmost still on hidden layer; Time A tick sits right of X/2 on the drawing where the overlap is shown), and "the layer-normalization stall, marked at Time B [0057]" = [0057] "This is shown at Time B where the array stalls"; the six stage names match the drawing's legend verbatim; the old interval-bounds error is gone}
  - {finding_id: r2-F2, status: closed-verified (round 3), round-4 ruling: standing — §4 line 73 reads "FIG. 5 is the whole argument in one picture:..."; no layout self-reference ("header drawing") anywhere in v3}
  - {finding_id: r2-F3, status: closed-verified (round 3), round-4 ruling: standing — §7 line 110 names the referent: "The crowded-field objection survives contact and changes nothing about the date."; exactly two "crowded" uses body-wide (§6 statement, §7 referent), no duplication cluster}
  - {finding_id: r3-F1, status: OPEN at low (deferred to self-audit) — see carried ruling above}

# ------------------------------------------------------------------
# PART 3 — Fresh 7-pass review of draft_version 3 (new findings, r4-*)
# ------------------------------------------------------------------

findings:

  - finding_id: r4-F1
    pass: pass-5-reader-perspective
    location: "§6 paragraph 1, final two sentences (draft line 100)"
    severity: low
    severity_under_default_posture: low
    finding: |
      "The filing's family is US-only, with no international filing and no
      continuation." — two terms of art reach the reader with no gloss. "PCT" was
      correctly translated to "international filing", but "continuation" is left bare
      (the retail reader has no way to know it means a follow-on application that
      extends the same disclosure), and "family" gets no first-use clause either.
      Reader-profile rule 1 (one-clause gloss on first use). Mitigation that keeps this
      at low rather than medium: the investment point is carried by the NEXT sentence
      ("it contrasts with the broader treatment given the company's granted patents"),
      so the reader who skips the terms still receives the observation's meaning, and
      the observation is explicitly labeled bibliographic-only. Every other term of art
      in the essay is glossed; this is the one remaining gap.
    recommendation: |
      Gloss in place without lengthening the labeled-observation discipline, e.g.:
      "The filing's family, the set of related applications built on it, is US-only:
      no international filing, and no continuation, the follow-on filing that would
      extend it." Or fold both into the contrast: "...no international filing and no
      follow-on continuation filing." No anchor change needed (family-us-only,
      evidence_level bibliographic, already labeled).
    quote: "The filing's family is US-only, with no international filing and no continuation."

  - finding_id: r4-F2
    pass: pass-2-redundancy
    location: "§7 (verdict section): paragraph 1, paragraph 2, and paragraph 4"
    severity: low
    severity_under_default_posture: low
    finding: |
      2A within-section repetition: the founders-authorship fact appears three times
      inside the verdict section alone — "signed by both founders" (para 1, line 108),
      "the named inventors stay the two founders" (para 2, line 110), "a dated,
      co-founder-signed blueprint" (para 4, line 114) — on top of §1's "signed by both
      co-founders" and §2's establishing statement (five body mentions total). Para 2's
      instance is load-bearing (it is the invariant list, the steelman refinement's
      spine) and stays. Paras 1 and 4 both re-assert it as an epithet within four
      paragraphs of each other. Below the 2A medium bar because the wording varies and
      each instance is short, but the verdict section would land cleaner shedding one.
    recommendation: |
      Cut ONE of the two epithet instances, keeping the para-2 invariant list intact.
      Cleanest: para 1 "signed by both founders, with the transformer-shaped division
      of labor drawn beside it" -> "with the transformer-shaped division of labor drawn
      beside it" (authorship then lands exactly twice in §7: the invariant list and the
      closing epithet). Alternatively drop "co-founder-signed" from para 4's "a dated,
      co-founder-signed blueprint".
    quote: "signed by both founders ... the named inventors stay the two founders ... a dated, co-founder-signed blueprint"

  - finding_id: r4-F3
    pass: pass-1-voice-anti-ai
    location: "cross-section cadence: §1 para 1 (line 19), §2 para 2 (line 29), §4 bold anchor (line 75), §5 closer (line 96)"
    severity: low
    severity_under_default_posture: low
    finding: |
      Tier-2 judgment (cadence fingerprint, not a banned pattern): the same
      two-sentence contrast template — negated noun, full stop, "It is" + corrected
      noun — carries four separate turning points: "that document is still not an
      asset. It is a pending application..."; "A patent application is not a patent.
      It is the scope a company is asking for..."; "...is not a 2026 slogan here. It
      is claim language..."; "The open question is not what this machine is for. It is
      what the document describing it is worth." Each instance is individually strong
      and none is an AI tell in isolation (the false-positive guard protects deliberate
      repetition); four uses of the identical figure across seven sections makes the
      device visible on a single read and slightly dulls the §4 bold anchor, which is
      the instance that most deserves the shape. This is the kind of taste-level
      pattern the multi-vote rule exists for: filed at low for the self-audit readers
      to vote on rather than asserted as a defect.
    recommendation: |
      If two or more self-audit readers concur, vary ONE instance, preferably §5's
      closer (the least load-bearing), e.g.: "The open question is not what this
      machine is for, but what the document describing it is worth." or recast as
      "What this machine is for was never the question. What the document describing
      it is worth is." Do not touch the §4 bold anchor (designated payoff) or §2
      (the edition's teaching sentence).
    quote: "The open question is not what this machine is for. It is what the document describing it is worth."

  - pass: pass-1-voice-anti-ai
    finding: "no further findings (r4-F3 above)"
    scoped_to: |
      Independent full-body scan on v3 with my own greps, run against the draft file
      (not the gate output): zero Tier-1 banned words (full delve/.../interplay list,
      plain-English hard bans utilise/facilitate/commence/deep-dive/going-forward),
      zero abstract "landscape", zero sentence-initial "Additionally", zero
      Furthermore/Moreover. Banned patterns: no not-just-X-but-Y (the four "not X. It
      is Y" contrasts are two-sentence figures, not the negative-parallelism
      construction — filed separately as r4-F3 cadence, not as the banned pattern), no
      despite-challenges, no copula avoidance (represents/constitutes/serves-as: zero),
      no vague attributions, no puffery (remarkable/extraordinary/unprecedented: zero),
      no section summaries, no filler announcements ("worth noting": zero), no elegant
      variation (filing/document/application/paper re-judged independently: each swap
      tracks the essay's status argument — "document" when neutral, "application" when
      the pending status is the point, "paper" in the closing antithesis — deliberate
      status-work, concur with rounds 1-3). Tier-2: no AI-vocabulary co-occurrence
      cluster; "The bandwidth follows:" is the single colon pivot and follows a
      complete clause; no semicolons in body prose (hits live only in the stripped
      footnote apparatus); 0 em-dashes; no Latin abbreviations, exclamation marks,
      emoji, or ALL-CAPS emphasis (HBM/UCIe/PCIe/RCE/FIG are acronyms/part tokens).
      Bold: exactly one load-bearing thesis anchor (§4). Fragments ("Now the memory
      half.") are deliberate cadence within the false-positive guard.

  - pass: pass-2-redundancy
    finding: "no further findings (r4-F2 above)"
    scoped_to: |
      2A re-derived from scratch: thesis formula appears in exactly three sections
      (§1/§4/§7); "the best layer is no layer" echo (§1 vs §4) re-adjudicated on merits
      in the gate block below; "still paying/spending/funding" beat sits in §2
      (teaching), §6 (record), §7 (verdict) in distinct evidentiary roles; the two
      laptop comparisons compare different quantities (storage vs bandwidth); date
      density re-checked: "May 2023"/"10 May 2023" mentions are the thesis object
      (concur with round 2's adjudication). The founders beat is the one 2A residue
      (r4-F2). 2B: real body sentences re-sampled at 36-41 words; each carries a claim
      clause, a mandated contract element (label sentence with two glosses, both-ways
      collateral frame), an attribution list, or the binary-test close — within
      "pressure, not a cap"; no sentence found that sheds 25% without losing mandated
      content. 2C: paragraph maxima independently re-counted — collateral 7 sentences
      / ~174 words (edition-contract floor, accepted), §3 composition paragraph 7
      sentences (at the limit, quote-integrated), §4 workload paragraph 5 sentences,
      steelman 7 sentences; nothing at 8+.

  - pass: pass-3-fact-paraphrase
    finding: "no findings"
    scoped_to: |
      Re-verified from sources this round, nothing inherited. (3A) Every double-quoted
      span and all four blockquotes byte-located in patent.md: [0002], [0013]
      blockquote, [0016] blockquote (also compared against claim 39 itself: sole
      difference "where"/"wherein" — the draft's "mirrored" framing is precise),
      [0018] x2 (incl. 128×128), [0021], [0027], [0028], [0030], [0040], [0043]
      blockquote, [0044], [0045] x2, [0047] x2, [0051] blockquote, [0057]. Three
      initial exact-match misses were investigated to root cause: patent.md carries
      non-breaking spaces (U+00A0) around some reference numerals ("chips 505");
      after NBSP normalization every span is verbatim, and no quote extends across the
      flagged run-on artifacts ("105passes", "215in", "220and"). All 19 [dddd] anchors
      resolve to invention-summary entries. (claims) Re-verified against patent.md
      claims 1-42 directly: four independents (1/15/26/39); claims 7/8 = HBMs
      hardwired to columns without any switching element, multiple per topmost-row IC;
      claims 11-13 = auxiliary circuitry + local memory chips + claim 13's
      do-not-communicate boundary (the §5 framing "the same claims then draw a
      boundary" is carried by claim 13 and the [0051] embodiment quote — accurate as
      drafted); claim 15 = AI accelerator with top-row memory chips storing weights
      ([0014] mirror); claims 1/26/39 carry no AI limitation ("ordinary drafting
      breadth" is fair). [0051]'s continuation ("in other examples, the local systolic
      arrays 220 may also have access") was checked against the draft's "the two never
      contend for the same store [0051]" — the draft scopes this to claims 11-13 as
      drafted and the blockquote itself carries "In this embodiment", so no
      overstatement. (3B) External claims re-traced to fact-check-log: reel/frames
      067204/0877 and 071792/0869 exact; lien dates 2024-04-19 / 2025-07-18 exact;
      grant date 2025-07-15 and the three-day interval as dated fact with motive
      explicitly labeled inference; "four applications then on file... two
      since-rejected compiler filings" within tp-lien-1-2024's wording; prosecution
      label matches prosecution-record; 8 examiner-cited references with cluster names
      from the log (NN expanded to "neural-network" — faithful); family-us-only
      labeled bibliographic; thread facts "the company says" at every use ($1B+
      contracts, $800 million, summer-2026 racks, LVI/CSM, latency philosophy);
      wiring-half continuity held to one clause (§2); both derived laptop comparisons
      footnote-labeled as the essay's own. No evidence_level silently upgraded.
      (3D) Causal claims: "The workload is what makes this thinkable" has its
      mechanism on the page ([0021] constants + [0045] same-columns); "so a bigger
      grid does more math per clock tick" follows [0003]/[0018]; "adding more rows
      adds compute without adding memory chips" is [0039] verbatim-adjacent ("data...
      is reused across the rows" -> "weight data is reused as it falls down the
      rows" — faithful).

  - pass: pass-4-logic-causality
    finding: "no findings"
    scoped_to: |
      4A: all seven sections independently re-traced against thesis-spine.md's
      spine->section table; every spine element lands in its assigned section (Q7
      friction hook §1; origin metadata + application-vs-grant teaching §2; mechanism
      + preset-loop bet §3; claim-39 family + baseline-then-inversion + effects §4;
      claims 11-13 split + 98% pipelining §5; label sentence + collateral +
      steelman concession §6; firm call + refine + binary test §7); no out-of-spine
      claim found; the §5 breadth concession stays inside the Claim scope map's
      columns. 4B: the one timing correlation (grants 15 July / lien 18 July) is
      handled dates-first with the motive reading explicitly labeled inference —
      exemplary correlation discipline; "no program counter to redirect and no
      scheduler to negotiate with" is translation of the adjacent [0027] quote, not a
      new mechanism claim; no correlation->causation drift, no reverse-causation
      exposure (the essay never claims the filing caused the product), no
      indirect-evidence-direct-claim mismatch (the verdict prices the document, not
      the company's intent). 4C: lead tension (narrative three years ahead of the
      property right) resolves in §7; concede(§6)->refine(§7) steelman arc intact;
      closing-binary-test (RCE outcome) matches the spine's Acceptance residual under
      the declared firm posture; the implication is THIS-document-specific, not
      generic.

  - pass: pass-5-reader-perspective
    finding: "no further findings (r4-F1 above; r3-F1 carried)"
    scoped_to: |
      Full read as the reader-profile investor, hunting deliberately where prior
      rounds had not flagged. Glosses re-verified on first use: systolic array,
      transformer, model weights, previous tensor, HBM, UCIe, self-attention,
      inference ("the running of already-trained models"), security interest, final
      rejection ("the examiner's formal no"), RCE ("a paid restart that keeps the
      argument alive"), independent claims; the two residues are "the citable
      summary" (r3-F1, open) and "family"/"continuation" (r4-F1, new). Quantitative
      claims carry familiar-scale comparisons where load-bearing (100s of GB ->
      laptop storage; 1 TB/s -> laptop drive per second); 32 GT/s is color, not
      load-bearing, and is explicitly de-weighted ("a description preference").
      Engagement curve: hook lands in lead sentence 1; no 3+ paragraph density wall
      (each mechanism paragraph surfaces to the money thread: "That inflexibility is
      the investor-relevant fact...", "The open question is... what the document...
      is worth"); §6's "So what is this document, as a thing an investor can price"
      re-anchors the stake before the record dump. Closing paragraph read in
      isolation: stands alone (names the restart, both outcomes, and the
      narrative-vs-paper frame without needing §1). Mobile: worst paragraph ~174
      words (edition-contract floor, accepted per r1-F4 residual); all others ≤~135
      words. "As of the 2026-05 record" phrasing checked and cleared: it mirrors the
      edition contract's own mandated wording for the label sentence.

  - pass: pass-6-lead-conclusion-format
    finding: "no findings"
    scoped_to: |
      6A: lead paragraph 1 is a declarative verdict ("Three years on, that document
      is still not an asset."); the patent filing is on the table in sentence 1;
      thesis fully set by paragraph 1. 6B: closing returns to the lead's
      stage-vs-paper frame ("The racks are shipping, the company says. The paper is
      still asking."); closing-binary-test under the declared firm posture matches
      the spine's Acceptance residual (RCE outcome as watchable falsifier); NOT a
      closing-open-question. 6C: Sources = 2 enum categories (Patents, Official
      statements), 6 entries across 2 categories -> subgrouped, all-or-nothing
      honored, no out-of-enum label. 6D: no papers, n/a. 6E: 0 body em-dashes
      (independent grep); all inline cites 4-digit zero-padded; publication.md
      re-diffed against the draft body this round — identical except frontmatter and
      the stripped footnote block (no footnote defs in publication.md); "# Sources"
      exactly once. 6F: title uses period separators, no em-dash, no colon needed,
      Title Case consistent. 6G BOTH DIRECTIONS under declared firm posture —
      over-hedge: the call leads ("Hold the July 2026 thread against the May 2023
      filing and the verdict is firm."); no qualifier-led verdict; no safe-harbor
      boilerplate anywhere (no "patents don't guarantee...", no "time will tell");
      exactly ONE patent-specific anti-hype guard ("broad claim 1... likeliest to
      shrink or die"); limits referenced, not re-listed ("The rejection record and
      the blanket liens scope this call without softening it."); gate_hedge
      round-4 pass concurs. Overreach: no asset/enforceability language for the
      pending set ("does not yet own anything in it"; "a roadmap in formation rather
      than a fence"); "likeliest survivor" is bounded "As drafted", carries its
      reason on the page (inverts the [0043] baseline), and stays inside the scope
      map's prosecution-risk note; the binary-test close claims only what either
      outcome supports. The edition's specific risk pair (rejection-record hedging
      vs asset-language overreach) checked explicitly: neither present.

  - pass: pass-7-adversarial-reader
    finding: "no further findings (r4-F2/r4-F3 surfaced on this pass's read, filed under their home passes)"
    scoped_to: |
      Checklist with quoted evidence on v3, both personas, fresh eyes: (1) BLUF —
      PASS ("The memory half of Etched's architecture story has been in writing
      since 10 May 2023... Three years on, that document is still not an asset.").
      (2) Header-as-claim — PASS: all seven ## headers assert; header-only skim
      reconstructs friction -> origin -> mechanism -> memory claim -> transformer
      shape -> record -> verdict. (3) Steelman — PASS: THIS-application objection
      conceded at full strength in §6 ("The examination record lists 8 references...
      the field was already crowded when the founders filed. The examiner has said
      no once... Three years of prosecution have produced no enforceable claim at
      all.") and refined, not dodged, in §7; no generic patent truism stands in for
      it. (4) Meta — PASS: no reader instruction, no essay-self-reference
      ("this document"/"the paper" name the patent application, not the essay;
      "the verdict is firm" examined and cleared — it asserts a property of the
      call the paragraph then delivers, functional analytic register, not stage
      direction). (5) Jargon-depth — PASS: terms stay signposts; no prosecution-law
      or claim-construction deep-dive; layer normalization used as an opaque stage
      name whose insight survives (concur with round 3). (6) Stub/rhythm — PASS:
      no section markedly shorter than siblings; the lead's 2-sentence hinge
      paragraph and §7's 2-sentence second paragraph read as deliberate cadence.
      (7) Thesis restatement — PASS: core verdict formula in exactly 3 sections
      (§1/§4/§7). Impatient-investor irritation scan residue: the unglossed
      "continuation" (r4-F1) and the fourth "not X. It is Y" (r4-F3) — filed above.

gate_warn_adjudications:
  - check_id: STRUCT-004 (1 triad, line 94)
    ruling: accepted-functional (independent re-judgment, concurring)
    rationale: |
      The FIG. 7 caption's "Attention queries, keys, and values, projection, and the
      MLP layers" enumerates the drawing's own legend stages in legend order —
      verified against fig-07.png this round (legend reads Attention: Queries / Keys /
      Values, Projection, MLP: Hidden Layer, MLP: Output Layer). A factual
      figure-reading list, not reflexive rule-of-three.
  - check_id: DUPE-001 (x2, "the best layer is no layer", §1 vs §4)
    ruling: accepted-intentional (independent re-judgment on merits, fourth concurrence)
    rationale: |
      Both uses are company-attributed and the §4 use is the essay's payoff: holding
      the 2026 slogan against the 2023 claim language IS the friction thesis — the
      verbatim echo is the argument's mechanism, and the essay explicitly prices the
      vocabulary gap two sentences later ("Latency is the word the 2026 thread
      added."). Cutting either occurrence would weaken the single bold-anchor payoff.
  - check_id: LONGSENT-001 (x17)
    ruling: spot-verified, majority-artifact (independent re-sampling)
    rationale: |
      Re-sampled against the actual draft text: the 49/50/54/56/57/101/159-word hits
      are tokenizer joins across headings, blockquote attributions, captions, and
      footnote defs (the 159-word "sentence" is the Sources block; the 54-word hit
      joins the bold anchor to the next paragraph). Real body sentences top out at
      36-41 words and each carries a claim clause, a mandated contract element, an
      attribution list, or the binary-test close — within the "pressure, not a cap"
      rule with the claim-clause exception. No tightening finding survives the
      mandated-content test.

edition_compliance_audit:
  application_era_language: |
    PASS. Claim content carried in application-era verbs throughout ("the
    application asks for / claims", "as drafted", "Etched is seeking", "has been
    asking"); the one "requires" is the sanctioned negation ("not something claim 1
    requires as drafted"); "enforceable" appears only in the edition's own framing
    negations ("before anything becomes enforceable", "produced no enforceable claim
    at all"); no infringement language; UCIe explicitly labeled a description
    preference; no specification number presented as a claim limitation (128×128,
    100s of GB, 32 GT/s, 1 TB/s, 98% all attributed to the filing's description).
  label_sentence: |
    PASS. Exactly ONE prosecution label sentence (§6 para 1) carrying all mandated
    elements (pending; examination continuing after a final rejection and an RCE; as
    of the 2026-05 record) with both glosses inline; no office-action chronology in
    the body; the lead's "still being argued with a patent examiner" and the
    §6-steelman/§7 rejection-RCE beats are spine-authorized thesis carriage, not a
    second label (independent concurrence with rounds 1-3).
  collateral_beat: |
    PASS on all six elements in ONE paragraph (§6 para 2): portfolio scope with zero
    selectivity stated ("blanket over the portfolio at signing... say nothing about
    this application in particular"); both reel/frames exact; timing as dated fact
    with motive explicitly labeled inference; both-ways frame ("concrete enough to
    bank... what a creditor reaches if things go wrong"); never presented as
    THIS-application evidence. Lead and §7 references stay portfolio-scoped
    ("alongside the rest of the company's patent stack", "with the rest of the
    stack").
  both_or_neither: |
    PASS. Rejection label sentence and collateral beat both in §6, rejection first.
  figures: |
    PASS, all five placed figures re-verified against the image files with my own
    eyes this round. FIG. 5 header caption numerals (505A/B, 510A-D, 515A-D, 520,
    215, 220) match the drawing exactly. FIG. 1 body description (weights 110 into
    the top row of DPUs 105, previous tensor 115 from the left) matches. FIG. 2
    caption (ICs 215A-215I, 220 tiles, memory chips 210A-210C top row only, host
    205, PCIe 240, 230 horizontal / 225 vertical, array 250) matches. FIG. 6
    re-verified independently: 605A-D are the rounded blocks INSIDE ICs 615A-D
    (auxiliary circuitry) and 610A-D are the small EXTERNAL chips wired only to the
    605 blocks (local memory chips) — the draft caption is correct; the manifest
    one-liner's 605/610 swap is confirmed wrong for the fourth consecutive
    independent round (trust the drawing, not the manifest). FIG. 7 caption matches
    the drawing and [0055]-[0057] (six legend stages verbatim; Time A overlap; Time
    B stall). FIG. 3/4 drop honored (their point travels via [0039] in §3; neither
    appears in the body); placement matches figure-selection.md (fig-05 header +
    1/2/6/7 body in section order 3/3/5/5).

double_clean_status: |
  Round 3 (reviewer instance 3): pass. Round 4 (this reviewer, independent, no
  revision in between): pass. Two consecutive clean rounds from independent
  reviewers on the identical draft — double-clean acceptance is satisfied from the
  editorial side. Open low-severity queue for the post-acceptance self-audit:
  r3-F1 (citable-summary gloss), r4-F1 (continuation/family gloss), r4-F2 (§7
  founders repetition), r4-F3 (contrast-figure cadence, multi-vote requested).
```
