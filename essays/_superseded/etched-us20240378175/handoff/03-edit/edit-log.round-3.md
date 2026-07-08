# Edit Log — Round 3

```yaml
review_id: etched-us20240378175-editorial-review-3
draft_source: handoff/02-compose/essay-draft.md
publication_strip: handoff/02-compose/publication.md
review_timestamp: 2026-07-04T00:00:00Z
review_round: 3
draft_version_reviewed: 3
posture_applied: measured
closing_posture_declared: firm
edition: pending-application (input/essay-context.md controls)
overall_assessment: pass
assessment_rationale: |
  All three round-2 dispositions verified landed — r2-F1 (FIG. 7 caption) verified
  AGAINST THE DRAWING ITSELF and against [0053]-[0057] in patent.md, not just against
  the revision-response text. All ten round-1 fixes re-confirmed still standing in
  draft_version 3 (composer reported §7 paragraphs 1/3/4 byte-identical to v2;
  independently spot-confirmed). Full fresh 7-pass review on v3 run against the
  design bundle, patent.md claims 1-42, the fact-check-log, and all five figure
  images: zero critical, zero high, zero medium; ONE new low (r3-F1, a gloss-clarity
  polish on "the citable summary" in §4). Per the assessment rules (no critical, no
  high, no medium), this round is PASS. Because a clean call must be falsifiable,
  the no-findings entries below record exactly what was re-checked, and the draft
  was re-read against pass-5 (reader-profile calibration) and pass-7 (adversarial
  personas) a second time before signing: the residue found on that second read is
  r3-F1 and nothing at medium or above. This is the FIRST clean round; double-clean
  acceptance still requires an independent round-4 confirmation.

# ------------------------------------------------------------------
# PART 1 — Re-review protocol: ruling on every carried round-2 finding
# ------------------------------------------------------------------

carried_finding_rulings:

  - finding_id: r2-F1
    prior_severity: medium
    disposition_claimed: applied
    ruling: verified-landed (verified against fig-07.png directly + [0056]/[0057])
    evidence: |
      Current caption (draft line 94): "FIG. 7: pipelining one array row. Attention
      queries, keys, and values, projection, and the MLP layers follow each other
      through the row, and at Time A a new computation has already entered while the
      previous one drains. The only idle gap is the layer-normalization stall, marked
      at Time B [0057]."
      Independent image inspection this round: the time axis runs 0 to X with Y-axis
      "Operation of DPU i"; the six legend stages (Attention: Queries / Keys / Values,
      Projection, MLP: Hidden Layer, MLP: Output Layer) span the FULL axis; the tick
      "Time B" sits LEFT of X/2 adjacent to the hatched stall band, and "Time A" sits
      RIGHT of X/2 where the dense band ends and the MLP output-layer lines overlap
      the draining hidden-layer lines. Spec cross-check: [0056] "at Time A, the
      leftmost DPU... is performing the computation associated with the output layer
      of the MLP, while the rightmost DPU... is still working on the previous
      computation, the MLP hidden layer" = the caption's "a new computation has
      already entered while the previous one drains"; [0057] "This is shown at Time B
      where the array stalls" (layer normalization) = "the layer-normalization stall,
      marked at Time B". The old interval-bounds error ("between Time A and Time B")
      and its chronology inversion are gone. The composer's semicolon-split
      equivalence edit is semantically identical to the round-2 recommendation and
      keeps body prose semicolon-free. Neighbor check: the body sentence above the
      figure is unchanged and accurate; the surviving quote "98% or greater
      utilization of the systolic array" [0057] re-verified verbatim in patent.md;
      figures-rationale.md sync noted (volunteered change, consistent).

  - finding_id: r2-F2
    prior_severity: low
    disposition_claimed: applied
    ruling: verified-landed
    evidence: |
      §4 (draft line 73) now reads "FIG. 5 is the whole argument in one picture: two
      boxes of memory, four columns of math, and only wires in between." The layout
      self-reference ("The header drawing") is gone; the FIG. 5 figure token survives
      (round-3 gate_figure_use passes); no other meta/self-reference introduced.

  - finding_id: r2-F3
    prior_severity: low
    disposition_claimed: applied
    ruling: verified-landed
    evidence: |
      §7 paragraph 2 sentence 1 (draft line 110) now reads "The crowded-field
      objection survives contact and changes nothing about the date." The referent is
      named once and correctly (the §6 steelman IS the crowded-field objection: "the
      field was already crowded when the founders filed"). Neighbor check: no
      duplication cluster created (two total "crowded" uses, §6 statement + §7
      referent name); §7 verdict wording, the single anti-hype guard, and the
      binary-test close are unchanged (paragraphs 1/3/4 confirmed unchanged).

# ------------------------------------------------------------------
# PART 2 — Finding-id lifecycle: continuity ruling on every id from rounds 1-2
# ------------------------------------------------------------------

finding_id_lifecycle:
  - {finding_id: r1-F1, status: closed-verified (round 2), re-checked-in-v3: standing — §4 "with its space and power" + bridge "The filing books the gain as space and power [0045]. Latency is the word the 2026 thread added." both present}
  - {finding_id: r1-F2, status: closed-verified (round 2, grounding-substitution accepted), re-checked-in-v3: standing — §3 "a machine you build when one workload... deserves its own dedicated hardware"; §5 "Not everything here is that committed..." breadth concession intact and re-confirmed against claims 1/26/39 (no AI limitation as drafted)}
  - {finding_id: r1-F3, status: closed-verified (round 2), re-checked-in-v3: standing — all three self-reference rewrites present; the follow-on referent issue was r2-F3, now closed}
  - {finding_id: r1-F4, status: closed-verified (round 2, residuals accepted), re-checked-in-v3: standing — collateral paragraph re-counted at 174 words, ONE paragraph, all six contract elements present; steelman 131 words / 7 sentences}
  - {finding_id: r1-F5, status: closed-verified (round 2), re-checked-in-v3: standing — full thesis formula in exactly three sections (§1 lead, §4 bold anchor, §7); §3/§5 forward-pointer closers intact; "May 2023" density 7 mentions, functional (the date is the thesis object)}
  - {finding_id: r1-F6, status: closed-verified (round 2), re-checked-in-v3: standing — Sources entry for US 12,361,091 B1 carries only anchored fields (grant date, "wiring half", companion framing)}
  - {finding_id: r1-F7, status: closed-verified (round 2), re-checked-in-v3: standing — independent-claims gloss in §7 para 3; four independents re-verified against patent.md claims (1, 15, 26, 39)}
  - {finding_id: r1-F8, status: closed-verified (round 2), re-checked-in-v3: standing — "roughly a whole laptop's storage" comparator}
  - {finding_id: r1-F9, status: closed-verified (round 2), re-checked-in-v3: standing — "In plain terms, that means..." / "In translation, each memory channel..."; "The bandwidth follows:" is the single surviving colon pivot}
  - {finding_id: r1-F10, status: closed-verified (round 2), re-checked-in-v3: standing — lead sentence split at "loan collateral. Meanwhile..."}
  - {finding_id: r2-F1, status: closed-verified this round (see carried ruling above)}
  - {finding_id: r2-F2, status: closed-verified this round (see carried ruling above)}
  - {finding_id: r2-F3, status: closed-verified this round (see carried ruling above)}

# ------------------------------------------------------------------
# PART 3 — Fresh 7-pass review of draft_version 3 (new findings)
# ------------------------------------------------------------------

findings:

  - finding_id: r3-F1
    pass: pass-5-reader-perspective
    location: "§4, sentence introducing the [0016] blockquote (draft line 66)"
    severity: low
    severity_under_default_posture: low
    finding: |
      "The claim language, mirrored in the citable summary, reads:" — "the citable
      summary" is unglossed insider phrasing. It is doing real work (it explains
      honestly why the anchor is [0016], the application's Summary paragraph that
      mirrors claim 39 near-verbatim, rather than the claim itself), but the target
      reader has no way to know what "the citable summary" is or why a claim would be
      "mirrored" there. Reader-profile rule 1 (one-clause gloss on first use). The
      quote chain itself is accurate: [0016] text verified verbatim; it differs from
      claim 39 only by "where"/"wherein", so "mirrored" is precise.
    recommendation: |
      Gloss in place, e.g.: "The claim language, repeated word for word in the
      application's own summary section, reads:" (keeps the [0016] anchor honest and
      tells the reader what they are looking at). No anchor change needed.
    quote: "The claim language, mirrored in the citable summary, reads:"

  - pass: pass-1-voice-anti-ai
    finding: "no findings"
    scoped_to: |
      Independent full-body scan on v3 (own script, not gate output): zero Tier-1
      banned words (delve/tapestry/.../interplay list plus plain-English hard bans),
      zero abstract "landscape", zero sentence-initial "Additionally". Banned
      patterns: no not-just-X-but-Y, no despite-challenges, no copula avoidance
      (represents/constitutes/serves-as: zero hits), no vague attribution, no
      puffery, no section summaries, no "worth noting". Tier-2 judgment sweep: no
      AI-vocabulary co-occurrence cluster (actually/robust/seamless/unlock/key etc.:
      only "keys" as the FIG. 7 legend term), no transition fingerprint, no
      manufactured-discovery pivots; "The bandwidth follows:" remains the single
      sanctioned colon pivot; 0 em-dashes; no semicolons in body prose; no filler
      phrases ("in order to", "due to the fact": zero). Bold: exactly one
      load-bearing thesis anchor (§4). No emoji, ALL-CAPS, Latin abbreviations, or
      exclamation marks. Document-name variation (filing/document/application/paper)
      re-judged deliberate status-work, not elegant variation.

  - pass: pass-2-redundancy
    finding: "no findings"
    scoped_to: |
      2A on v3: thesis formula confirmed at exactly three sections (§1/§4/§7); the
      "still paying/spending/funding" beat sits in §2 (metadata), §6 (record), §7
      (verdict + header) each in a distinct evidentiary role — re-judged acceptable;
      DUPE-001's "best layer is no layer" echo re-adjudicated below. 2B: real long
      sentences re-sampled at 36-41 words, each carrying a claim clause, mandated
      contract elements, or an attribution list ("pressure, not a cap"). 2C:
      paragraph maxima re-counted 174/135/133/131 words, all ≤7 sentences; the two
      long §3/§4 mechanism paragraphs are quote-integrated (measured-posture
      demotion); the 174-word collateral paragraph is the edition contract's floor
      (one-paragraph rule + six mandated elements), carried from the accepted r1-F4
      residual.

  - pass: pass-3-fact-paraphrase
    finding: "no findings"
    scoped_to: |
      Re-verified from sources this round, not inherited: every double-quoted span
      byte-located in patent.md ([0002] "perform the same task...", [0013] and
      [0016] blockquotes, [0018] x2 incl. "128×128", [0021] "may be constants",
      [0027], [0028], [0030] "supports up to 32 GT/s", [0040] ">1 TB/s" span stopping
      before the "215in" artifact, [0043] blockquote, [0044], [0045] x2, [0047] x2,
      [0051] blockquote, [0057]) — all verbatim, none extended across the flagged
      run-on artifacts. All 19 [dddd] anchors resolve to invention-summary entries.
      Claim-content statements re-verified directly against patent.md claims 1-42:
      four independents (1/15/26/39); claims 7/8 HBMs hardwired switchless, multiple
      per top-row IC (claim 8); claims 11-13 auxiliary circuitry + local memory +
      claim 13's do-not-communicate boundary; claim 15 AI-accelerator system with
      top-row memory chips storing weights ([0014] mirror); claim 39's "where"
      variant in [0016] correctly presented as the summary mirror. External claims
      re-traced to fact-check-log: both reel/frames exact (067204/0877, 071792/0869),
      lien dates and scope wording within the log's claims, grant-lien 3-day interval
      as dated fact with motive explicitly labeled inference, prosecution label
      matches `prosecution-record`, 8 examiner-cited references with the three
      cluster names verbatim from the log, family-us-only carried as a labeled
      bibliographic observation, thread facts "the company says" at every use,
      wiring-half continuity held to one clause (§2). No evidence_level silently
      upgraded; derived comparisons footnote-labeled. Figure captions verified
      against all five images with my own eyes this round (see figures block).

  - pass: pass-4-logic-causality
    finding: "no findings"
    scoped_to: |
      4A: all seven sections re-traced against thesis-spine.md's spine→section
      table; every spine element lands in its assigned section; no out-of-spine
      claim (the §5 breadth concession stays inside the Claim scope map's columns;
      independently re-confirmed against the claims). 4B: the one timing correlation
      (grants 15 July / lien 18 July) is handled dates-first with the motive reading
      explicitly labeled inference; "The workload is what makes this thinkable" has
      its mechanism on the page ([0021] constants → columns always fed the same
      slice); "no program counter... no scheduler" reads as translation of the
      adjacent [0027] quote, not a new mechanism claim; no correlation→causation
      drift found. 4C: lead tension (narrative three years ahead of the property
      right) resolves in §7; concede(§6)→refine(§7) steelman arc intact;
      closing-binary-test (RCE outcome) matches the spine's Acceptance residual
      under the declared firm posture.

  - pass: pass-5-reader-perspective
    finding: "no further findings (r3-F1 above)"
    scoped_to: |
      Second full read as the reader-profile investor. Glosses re-verified on first
      use: systolic array, transformer, weights, previous tensor, HBM, UCIe,
      self-attention, inference ("the running of already-trained models"), security
      interest, final rejection, RCE, independent claims; "reel/frame" carried as
      self-evident from context (round-1 adjudication, concur); "layer
      normalization" used as an opaque stage name whose insight (the one stall,
      ≥98% anyway) survives without a doctrinal gloss — signpost, not deep-dive.
      Quantitative claims carry familiar-scale comparisons where load-bearing (100s
      of GB → laptop storage; 1 TB/s → laptop drive per second); 32 GT/s is color,
      not load-bearing. Engagement curve: hook in lead sentence 1; no 3+ paragraph
      density wall (each mechanism paragraph surfaces to the money thread); §3/§5
      forward-pointer closers hold section-boundary stake; closing paragraph stands
      alone. Mobile: worst paragraph 174 words (~14 lines) is the edition-contract
      floor, accepted; all others ≤135 words.

  - pass: pass-6-lead-conclusion-format
    finding: "no findings"
    scoped_to: |
      6A: lead paragraph 1 is a declarative verdict; patent on the table in sentence
      1. 6B: closing returns to the lead's stage-vs-paper frame ("The racks are
      shipping, the company says. The paper is still asking."); closing-binary-test
      under firm posture matches the spine's Acceptance residual. 6C: Sources = 2
      enum categories (Patents, Official statements), 6 entries, all-or-nothing
      subgrouping correct for 4+/2+. 6D: no papers, n/a. 6E: 0 body em-dashes; all
      inline cites 4-digit; publication.md re-checked to end at Sources with no
      footnote defs; "# Sources" exactly once. 6F: title uses a period separator, no
      em-dash, Title Case consistent. 6G BOTH DIRECTIONS under declared firm
      posture — over-hedge: the call leads ("Hold the July 2026 thread against the
      May 2023 filing and the verdict is firm."), no qualifier-led verdict, no
      safe-harbor boilerplate (no "patents don't guarantee..." anywhere), exactly
      ONE patent-specific anti-hype guard (claim 1 breadth likeliest to shrink),
      limits referenced not re-listed ("The rejection record and the blanket liens
      scope this call without softening it."); gate_hedge round-3 pass concurs.
      Overreach: no asset/enforceability language for the pending set ("does not
      yet own anything in it", "a roadmap in formation rather than a fence");
      "likeliest survivor" stays inside the scope map's prosecution-risk note and
      is bounded "As drafted"; the binary-test close claims only what either
      outcome supports. The edition's specific risk pair (rejection-record hedging
      vs asset-language overreach) checked explicitly: neither present.

  - pass: pass-7-adversarial-reader
    finding: "no findings"
    scoped_to: |
      Checklist with quoted evidence on v3, read as both personas: (1) BLUF — PASS
      ("The memory half of Etched's architecture story has been in writing since 10
      May 2023... that document is still not an asset."). (2) Header-as-claim —
      PASS: all seven ## headers assert; a header-only skim reconstructs setup →
      mechanism → memory claim → transformer shape → record → verdict. (3) Steelman
      — PASS, THIS-application objection at full strength ("The examination record
      lists 8 references... the field was already crowded when the founders filed.
      The examiner has said no once... Three years of prosecution have produced no
      enforceable claim at all.") conceded in §6, refined in §7; no generic patent
      truism. (4) Meta — PASS: the r2-F2 layout self-reference is gone; remaining
      document-references ("this document", "the paper") name the patent
      application, not the essay; no reader instruction. (5) Jargon-depth — PASS,
      terms stay signposts (no doctrinal prosecution or claim-construction
      deep-dive). (6) Stub/rhythm — PASS, no section markedly shorter than
      siblings; §7's 2-sentence second paragraph reads as deliberate verdict
      cadence (concurring with round 2). (7) Thesis restatement — PASS, core
      verdict formula asserted in exactly 3 sections. Impatient-investor irritation
      scan: the one residue is the unglossed "citable summary" (filed as r3-F1).

gate_warn_adjudications:
  - check_id: STRUCT-004 (1 triad, line 94)
    ruling: accepted-functional
    rationale: |
      Line 94 is the revised FIG. 7 caption; "Attention queries, keys, and values,
      projection, and the MLP layers" enumerates the drawing's own six legend
      stages in legend order — a factual figure-reading list, not reflexive
      rule-of-three. (The §6 examiner-cluster list remains a verbatim enumeration
      of the fact-check-log's three citation clusters, same ruling as rounds 1-2.)
  - check_id: DUPE-001 (x2, "the best layer is no layer", §1 vs §4)
    ruling: accepted-intentional (re-judged on merits, third independent concurrence)
    rationale: |
      Both uses are company-attributed and the §4 use is the essay's payoff move —
      the 2026 slogan held against the 2023 claim language. The echo IS the
      friction thesis; cutting either weakens the single bold-anchor payoff.
  - check_id: LONGSENT-001 (x17)
    ruling: spot-verified, majority-artifact
    rationale: |
      Independently sampled this round: the 50/56/57/101/159-word hits are
      tokenizer joins across headings, blockquote attributions, captions, and
      footnote defs (e.g. the 159-word "sentence" is the Sources block; the 50-word
      "The filing is still where the checking starts. ##..." is a heading join).
      Real body sentences run 36-41 words and each carries a claim clause, the
      mandated collateral contract elements, an attribution list, or the
      binary-test close — within "pressure, not a cap". No new tightening finding.

edition_compliance_audit:
  application_era_language: |
    PASS. Claim content carried in application-era verbs throughout ("the
    application asks for", "as drafted", "Etched is seeking", "has been asking");
    the one "requires" is the sanctioned negation ("not something claim 1 requires
    as drafted"); "enforceable" appears only in the edition's own framing negations
    ("before anything becomes enforceable", "produced no enforceable claim at
    all"); no infringement/enforceability claims anywhere; no description
    preference presented as claim-required (UCIe explicitly flagged as preference);
    no specification number presented as a claim limitation.
  label_sentence: |
    PASS. Exactly one prosecution label sentence (§6 para 1: pending + examination
    continuing + final rejection + RCE + as-of-2026-05), with both mandated glosses;
    no office-action chronology in the body (chronology lives only in the stripped
    footnote apparatus); lead's "still being argued with a patent examiner" and the
    §6/§7 rejection/RCE beats are spine-authorized thesis carriage, not a second
    label (concurring with rounds 1-2).
  collateral_beat: |
    PASS on all six elements in ONE paragraph (§6 para 2, 174 words): portfolio
    scope with zero selectivity stated ("blanket over the portfolio at signing...
    say nothing about this application in particular"); both reel/frames; timing as
    dated fact with motive explicitly labeled inference; both-ways frame ("concrete
    enough to bank... what a creditor reaches if things go wrong"); never
    patent-specific. Lead/§7 references stay portfolio-scoped ("alongside the rest
    of the company's patent stack", "with the rest of the stack").
  both_or_neither: |
    PASS. Rejection label sentence and collateral beat both in §6, rejection first.
  figures: |
    PASS, all verified against the image files with my own eyes this round. FIG. 5
    header caption numerals (505A/B, 510A-D, 515A-D, 520, 215, 220) match the
    drawing. FIG. 1 body description (weights 110 into top row of DPUs 105,
    previous tensor 115 from the left) matches. FIG. 2 caption (215A-I, 220 tiles,
    210A-C top row only, host 205, PCIe 240, 225/230, 250) matches. FIG. 6
    re-verified independently: 605A-D are the rounded blocks INSIDE ICs 615A-D
    (auxiliary circuitry) and 610A-D are the small EXTERNAL chips wired only to the
    605 blocks (local memory) — the draft caption is correct; the manifest
    one-liner's 605/610 swap is confirmed wrong for the third consecutive round.
    FIG. 7 caption now matches the drawing and [0056]/[0057] (r2-F1 closed). All
    five selected figures placed (FIG. 5 header + 1/2/6/7 body); FIG. 3/4 drop
    honored, their point carried via [0039] in §3.
```
