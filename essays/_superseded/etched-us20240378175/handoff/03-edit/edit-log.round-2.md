# Edit Log — Round 2

```yaml
review_id: etched-us20240378175-editorial-review-2
draft_source: handoff/02-compose/essay-draft.md
publication_strip: handoff/02-compose/publication.md
review_timestamp: 2026-07-04T00:00:00Z
review_round: 2
draft_version_reviewed: 2
posture_applied: measured
closing_posture_declared: firm
edition: pending-application (input/essay-context.md controls)
overall_assessment: revise-recommended
assessment_rationale: |
  All ten round-1 dispositions verified landed (quoted below), with no neighbor
  regressions except one soft referent noted at low severity. One NEW medium finding:
  the FIG. 7 caption factually mis-describes the drawing and the spec (the stage
  sequence does not sit "between Time A and Time B"; Time B is the stall, Time A is
  the pipelining overlap, and B precedes A on the axis) — verified against the image
  and [0053]-[0057]. Two new lows. No high/critical; no hard-gate-relevant finding
  (grounding chain verbatim-verified incl. NBSP-normalization audit, FIGUSE clean,
  6G clean both directions under firm posture). Medium present -> revise-recommended.

# ------------------------------------------------------------------
# PART 1 — Re-review protocol: ruling on every carried round-1 finding
# ------------------------------------------------------------------

carried_finding_rulings:

  - finding_id: r1-F1
    prior_severity: medium
    disposition_claimed: applied
    ruling: verified-landed
    evidence: |
      §4 para 2 now reads "...the price is a layer of silicon, with its space and
      power, sitting between memory and math." (latency removed). §4 bridge now
      carries the explicit vocabulary line: "The filing books the gain as space and
      power [0045]. Latency is the word the 2026 thread added." Independently
      re-verified: `grep -i latenc` on input/patent.md returns ZERO hits — the
      filing never uses the word; the only latency claims in the essay remain
      company-attributed (§1 "The memory pillar carries the philosophy... Every
      number and claim in that thread is the company's own account"). Neighbor
      check: the "best layer is no layer" DUPE echo survives as adjudicated; the
      STRUCT-004 "space, power, and latency" triad dissolved as predicted (round-2
      gate shows only one remaining triad, ruled functional below).

  - finding_id: r1-F2
    prior_severity: medium
    disposition_claimed: applied (with composer source-fence flag)
    ruling: verified-landed; grounding-substitution accepted
    evidence: |
      §3 closer now: "That inflexibility is the investor-relevant fact: this is a
      machine you build when one workload, transformer inference, the running of
      already-trained models, deserves its own dedicated hardware." — the false
      "worth building only" exclusivity is gone; the bet reading stays firm. §5 now:
      "Not everything here is that committed. The broad combined-array claims carry
      no AI limitation as drafted, and neither does claim 39's memory interface,
      which is ordinary drafting breadth. Where the filing does commit, it commits
      along a transformer's seams..." — breadth conceded, transformer-shape narrowed
      to the anchored pieces (claims 11-13 / [0047] / FIG. 7).
      RULING ON THE SOURCE-FENCE FLAG: the composer grounded the breadth concession
      on the Claim scope map instead of the reviewer-suggested [0019] generality
      clause (no Quotable span exists for it). That grounding SUFFICES: the sentence
      is a negative statement about claim text, quotes nothing, and is fully
      verifiable from the map's "requires as drafted" columns — and this reviewer
      independently confirmed it against the claims themselves in patent.md (claims
      1, 26, and 39 carry no AI limitation; AI enters only via claim 15 and
      dependents 6/12/40). No upstream Phase-1 span is needed for the text as
      written; the composer's upstream_flag stands as optional, relevant only if a
      future revision wants [0019] quoted verbatim.

  - finding_id: r1-F3
    prior_severity: medium
    disposition_claimed: applied
    ruling: verified-landed (one soft-referent side effect, filed as r2-F3 low)
    evidence: |
      All three rewrites present verbatim: §2 "One distinction carries all the
      weight."; §6 "Both halves of that record matter: the claims have been refused
      once, and the company is still spending money to pursue them."; §7 "The
      rejection record and the blanket liens scope this call without softening it."
      Volunteered removals confirmed: §3 "the investor-relevant fact" (no "in this
      section"); §7 "That objection survives contact" (no "above"). Neighbor check:
      dropping "above" left a bare demonstrative whose antecedent sits one section
      and one paragraph back — noted as new low r2-F3, not a re-assertion.

  - finding_id: r1-F4
    prior_severity: medium
    disposition_claimed: applied (with accepted residuals)
    ruling: verified-landed; residuals accepted
    evidence: |
      Collateral paragraph (§6 para 2) recounted at 174 words (from 197), ONE
      paragraph held, all six contract elements intact (re-audited in the edition
      compliance block below); merged sentence present: "The dates are registry
      fact, and reading them as a lender sweeping fresh assets into its collateral
      is an inference, not a record."; both-ways sentence tightened to ~35 words.
      §7 split verified: "That objection survives contact... un-write." (2
      sentences) / "Within the sought set..." (4 sentences); no stub introduced
      (gate_stub passes; §7 rhythm reads intentional). Residuals ACCEPTED: the ~24
      words above the ~150 target are the contract elements themselves (two
      reel/frames + gloss + four dates + two-sided frame) and the edition's
      one-paragraph rule blocks a split; the §6 steelman at 131 words / 7 sentences
      stays under the 8-sentence line and any split would stub it.

  - finding_id: r1-F5
    prior_severity: medium
    disposition_claimed: applied
    ruling: verified-landed
    evidence: |
      The full thesis formula now appears in exactly three sections: §1 lead ("has
      been in writing since 10 May 2023"), §4 bold anchor ("claim language Etched
      has been asking the patent office for since May 2023"), §7 ("The philosophy
      was in writing by May 2023 either way"). §3 closer replaced with the forward
      pointer "And the design commits hardest on the memory side."; §5 closer with
      "The open question is not what this machine is for. It is what the document
      describing it is worth."; §7 para 1's "dated 10 May 2023" dropped (remaining
      "the May 2023 filing" is a frame pointer, and para 2's invariant-list date is
      doing real work, as the recommendation specified). Pass-7 check 7 now passes
      (verdict formula in 3 sections). Remaining "May 2023" density (7 mentions
      incl. §2 metadata and the §2 header) judged functional — the date IS the
      thesis object; not re-asserted.

  - finding_id: r1-F6
    prior_severity: medium
    disposition_claimed: applied
    ruling: verified-landed
    evidence: |
      Sources entry now: "US 12,361,091 B1, Etched.ai, Inc., granted 2025-07-15
      (the \"wiring half,\" subject of the companion analysis)." Every remaining
      field anchors: grant date 2025-07-15 via fact-check-log `grant-lien-timing`
      (the trio's second/third grants; 12,361,091 is among them), "wiring half" +
      companion framing via `prior-essay-wiring-half`. Title, priority date, and
      inventor attribution removed. No silent evidence_level upgrade remains.

  - finding_id: r1-F7
    prior_severity: medium
    disposition_claimed: applied
    ruling: verified-landed
    evidence: |
      §7 para 3 now: "As drafted, it is the likeliest survivor among the
      application's four independent claims, the ones that stand on their own
      rather than adding to another." Gloss carries both the count and the term of
      art in place. Independently verified against patent.md claims 1-42: exactly
      four independents (1, 15, 26, 39), matching the Claim scope map.

  - finding_id: r1-F8
    prior_severity: low
    disposition_claimed: applied
    ruling: verified-landed
    evidence: |
      §3: "Hundreds of gigabytes is the working size of a modern model's
      parameters, roughly a whole laptop's storage" — comparator now survives
      scrutiny; footnote label still accurate.

  - finding_id: r1-F9
    prior_severity: low
    disposition_claimed: applied
    ruling: verified-landed
    evidence: |
      §2: "In plain terms, that means many small math grids..."; §4: "In
      translation, each memory channel is bonded..."; "The bandwidth follows:" kept
      as the single surviving colon pivot, per the recommendation. No
      announcement-colon cluster remains.

  - finding_id: r1-F10
    prior_severity: low
    disposition_claimed: applied
    ruling: verified-landed
    evidence: |
      Lead sentence 3 split: "...pledged alongside the rest of the company's patent
      stack as loan collateral. Meanwhile the philosophy it wrote down is presented
      on stage as shipping hardware." Both-ways sentence recounted at ~35 words
      (from 41) under the r1-F4 edit.

# ------------------------------------------------------------------
# PART 2 — Fresh 7-pass review of draft_version 2 (new findings)
# ------------------------------------------------------------------

findings:

  - finding_id: r2-F1
    pass: pass-3-fact-paraphrase
    location: "§5, FIG. 7 caption (draft line 94 / publication line 84)"
    severity: medium
    severity_under_default_posture: medium
    finding: |
      The caption states the six pipeline stages "follow each other through the row
      between Time A and Time B." Checked against the drawing with fresh eyes and
      against [0053]-[0057]: (a) the stage sequence spans the figure's FULL time
      axis (0 to X), not the interval between the two labeled ticks — attention
      queries and keys sit BEFORE Time B on the chart; (b) the two ticks are
      specific marked instants, not interval bounds: Time A is where pipelining
      overlap is shown ("at Time A, the leftmost DPU... is performing the... output
      layer of the MLP, while the rightmost DPU... is still working on the...
      hidden layer", [0056]) and Time B is where the layer-normalization stall is
      shown ("This is shown at Time B where the array stalls", [0057]); (c) Time B
      precedes Time A on the axis, so "between Time A and Time B" also inverts
      chronology. The caption's second sentence ("The only idle gap is the
      layer-normalization stall [0057]") is supported; the interval claim is
      accidental drift a chart-reading reader will catch. The body sentence above
      the figure ("a new computation entering before the previous one drains") is
      accurate and unaffected.
    recommendation: |
      Re-anchor the caption to what the marks mean rather than treating them as
      bounds, e.g.: "FIG. 7: pipelining one array row. Attention queries, keys, and
      values, projection, and the MLP layers follow each other through the row; at
      Time A a new computation has already entered while the previous one drains,
      and the one idle gap is the layer-normalization stall at Time B [0057]."
      Keep [0057]; no new anchor needed.
    quote: "Attention queries, keys, and values, projection, and the MLP layers follow each other through the row between Time A and Time B. The only idle gap is the layer-normalization stall [0057]."

  - finding_id: r2-F2
    pass: pass-7-adversarial-reader
    location: "§4, final paragraph before the bold anchor"
    severity: low
    severity_under_default_posture: low
    finding: |
      "The header drawing, FIG. 5, is the whole argument in one picture" — the
      figure reference is functional, but "the header drawing" names the essay's
      own layout (meta-reader-instruction class, below gate_meta resolution;
      pre-existing text, outside r1-F3's scope). The sentence's payoff does not
      need the layout locator.
    recommendation: |
      "FIG. 5 is the whole argument in one picture: two boxes of memory, four
      columns of math, and only wires in between."
    quote: "The header drawing, FIG. 5, is the whole argument in one picture: two boxes of memory, four columns of math, and only wires in between."

  - finding_id: r2-F3
    pass: pass-5-reader-perspective
    location: "§7 paragraph 2, first sentence"
    severity: low
    severity_under_default_posture: low
    finding: |
      "That objection survives contact and changes nothing about the date." — the
      antecedent (the steelman objection closing §6) sits one section header and
      one full verdict paragraph back, and the intervening paragraph never mentions
      an objection. The r1-F3 volunteered edit correctly removed "above" but left a
      bare demonstrative; a mobile reader arriving from the verdict paragraph
      gropes for the referent for a beat. Content is intact — this is a
      referent-clarity polish, not a re-assertion of r1-F3.
    recommendation: |
      Name the referent once: "The crowded-field objection survives contact and
      changes nothing about the date." (or "The examiner's no survives contact...").
    quote: "That objection survives contact and changes nothing about the date."

  - pass: pass-1-voice-anti-ai
    finding: "no findings"
    scoped_to: |
      Full-body case-insensitive scan against the Tier-1 banned list and the Tier-2
      judgment list on draft_version 2: zero banned words, zero banned patterns
      (no not-just-X-but-Y, no copula avoidance, no vague attribution, no puffery,
      no section summaries, no elegant variation — filing/document/application/paper
      variation judged deliberate status-distinction, not brand-avoidance). Bold:
      exactly one load-bearing thesis anchor (§4). No emoji, no ALL-CAPS, no Latin
      abbreviations, no exclamation marks or semicolons in body prose (the only
      hits sit in footnote apparatus and image syntax). Announcement-colon cluster
      resolved by r1-F9; "The bandwidth follows:" is the single sanctioned survivor.

  - pass: pass-2-redundancy
    finding: "no findings"
    scoped_to: |
      2A: thesis-formula repetition re-verified at exactly three sections after
      r1-F5 (§1/§4/§7); "still paying/spending/funding" beat appears §2/§6/§7 +
      §7 header, each in a distinct evidentiary role (metadata, record, verdict) —
      not flagged. The two laptop-scale comparisons (§3 storage, §4 bandwidth)
      compare different quantities and share one footnote label. 2B: real 35-41
      word sentences re-sampled; all carry claim clauses, attribution lists, or
      mandated contract elements ("pressure, not a cap"). 2C: longest body
      paragraphs 174/135/133/131 words, all under 8 sentences; the two §3/§4
      mechanism paragraphs are quote-integrated (measured-posture demotion).

  - pass: pass-3-fact-paraphrase
    finding: "no further findings (r2-F1 above)"
    scoped_to: |
      All 19 distinct [dddd] anchors resolve to invention-summary.md entries
      (mechanically re-listed). Every double-quoted span byte-compared against BOTH
      the Quote anchor table and patent.md: verbatim, with one systematic
      non-semantic difference — patent.md uses non-breaking spaces before some
      reference numerals ("arrays\xa0220"); after NBSP->space normalization every
      span matches exactly, none extends across the flagged run-on artifacts
      ("105passes", "220and", "215in" etc.). Claim-content statements independently
      re-verified against patent.md claims 1-42: claims 7/8 (HBMs hardwired,
      multiple per top-row IC), 11-13 (auxiliary circuitry, local memory, arrays
      do-not-communicate boundary), 15 (AI accelerator, top-row memory chips), 39
      (channels hardwired, no switching element), four independents. External
      claims re-traced to fact-check-log IDs with reel/frames, dates, and the
      8-reference cluster wording exact; motive labeled inference; thread content
      "the company says" at every use; no evidence_level silently upgraded.
      Figure-caption accuracy checked against the actual drawings (see figures
      block below) — FIG. 7's caption is the one miss (r2-F1).

  - pass: pass-4-logic-causality
    finding: "no findings"
    scoped_to: |
      4A: all seven sections re-traced against thesis-spine.md's spine->section
      table on the revised draft; the two r1-F2 scoping overstatements are gone and
      no out-of-spine claim replaced them; the §5 breadth concession stays inside
      the Claim scope map. 4B: lien timing remains dates-plus-labeled-inference
      (the essay's own exemplary correlation handling); "a machine you build when"
      formulation no longer asserts exclusivity; no correlation->causation drift
      found. 4C: lead tension (narrative three years ahead of the property right)
      resolves in §7; concede(§6)->refine(§7) arc intact after the paragraph split;
      closing-binary-test (RCE outcome) matches the spine's Acceptance residual
      under firm posture.

  - pass: pass-5-reader-perspective
    finding: "no further findings (r2-F3 above)"
    scoped_to: |
      Glosses re-verified on first use (systolic array, HBM, UCIe, self-attention,
      security interest, final rejection, RCE, independent claims — the last added
      by r1-F7). Engagement curve on the revised draft: hook in lead sentence 1;
      the retooled §3/§5 forward-pointer closers improve section-boundary stake
      clarity; no 3+ paragraph density wall; closing paragraph stands alone.
      Mobile: collateral paragraph 174 words (~14 lines) accepted as the edition
      contract's floor (one-paragraph rule + six mandated elements); §7 split
      brought both verdict paragraphs under the heuristic; remaining long
      paragraphs are quote-integrated.

  - pass: pass-6-lead-conclusion-format
    finding: "no findings"
    scoped_to: |
      6A: lead paragraph 1 is a declarative verdict; the patent is on the table by
      sentence 1. 6B: closing returns to the lead's stage-vs-paper frame ("The
      racks are shipping, the company says. The paper is still asking.");
      closing-binary-test under firm posture per posture-lens. 6C: Sources = 2 enum
      categories (Patents, Official statements), 6 entries, all-or-nothing
      subgrouping correct for 4+/2+. 6D: no papers, n/a. 6E: 0 body em-dashes; all
      inline cites 4-digit; footnote defs stripped from publication.md (re-checked:
      publication ends at Sources); '# Sources' exactly once. 6F: title uses a
      period separator, no em-dash. 6G BOTH DIRECTIONS under declared firm posture:
      the call leads ("Hold the July 2026 thread against the May 2023 filing and
      the verdict is firm."); exactly ONE patent-specific anti-hype guard ("broad
      claim 1... likeliest to shrink or die"); limits referenced, not re-listed
      ("The rejection record and the blanket liens scope this call without
      softening it."); no safe-harbor boilerplate, no qualifier-led verdict, no
      stacked hedges (gate_hedge pass concurs). Overreach direction: no
      asset-language for the pending set ("does not yet own anything in it", "a
      roadmap in formation rather than a fence"); "enforceable" appears only in the
      edition's sanctioned negations; the binary-test close claims only what either
      outcome supports. The edition's special risk pair (rejection-record hedging
      vs asset-language overreach) checked explicitly: neither present.

  - pass: pass-7-adversarial-reader
    finding: "no further findings (r2-F2 above)"
    scoped_to: |
      Checklist with quoted evidence on draft_version 2: (1) BLUF — PASS ("The
      memory half of Etched's architecture story has been in writing since 10 May
      2023... that document is still not an asset."). (2) Header-as-claim — PASS,
      all seven ## headers assert; header-only skim reconstructs the argument
      including the verdict ("A Dated Roadmap the Company Keeps Funding, Not Yet a
      Fence"). (3) Steelman — PASS, THIS-application objection (crowded
      examiner-cited field, claims 1/26 breadth, "Three years of prosecution have
      produced no enforceable claim at all") conceded at full strength in §6,
      refined in §7; no generic truism. (4) Meta — one residual layout
      self-reference flagged as r2-F2 (low); the r1-F3 cluster is gone. (5)
      Jargon-depth — PASS, terms stay signposts. (6) Stub/rhythm — PASS, §7's
      2-sentence second paragraph reads as deliberate verdict cadence, sections
      balanced. (7) Thesis restatement — PASS after r1-F5 (3 sections).

gate_warn_adjudications:
  - check_id: DUPE-001 (x2, "the best layer is no layer", §1 vs §4)
    ruling: accepted-intentional (re-judged on merits, concurring with round 1)
    rationale: |
      Both uses are company-attributed and the §4 use is the payoff move — the 2026
      slogan held against the 2023 claim language. The echo IS the friction thesis;
      cutting either weakens the essay's one bold-anchor payoff.
  - check_id: STRUCT-004 (1 triad, line 94)
    ruling: accepted-functional
    rationale: |
      "multi-node ML acceleration, hybrid parallelism, and neural-network
      accelerator architectures" enumerates the fact-check-log's three
      examiner-citation clusters verbatim — a factual list, not reflexive
      rule-of-three. (Round 1's second triad dissolved with the r1-F1 fix, as
      predicted.)
  - check_id: LONGSENT-001 (x17)
    ruling: spot-verified, majority-artifact
    rationale: |
      Independently sampled: the 42/49/50/56/57/101/159-word hits are tokenizer
      joins across blockquotes, headings, captions, and footnote defs. Real body
      sentences run 36-41 words (label sentence with its two mandated glosses,
      attribution list, invariant list, binary-test close, both-ways contract
      sentence) — each carries a claim/contract clause within the "pressure, not a
      cap" rule. No new tightening finding.

edition_compliance_audit:
  application_era_language: |
    PASS. Grant-era verbs absent for claim content ("the application asks for",
    "as drafted", "Etched is seeking", "has been asking"); the one "requires" is
    the sanctioned negation "not something claim 1 requires as drafted" (scope-map
    column vocabulary). "Enforceable" appears only in the edition's own framing
    negations ("before anything becomes enforceable", "produced no enforceable
    claim at all"); no infringement/enforceability claims anywhere.
  label_sentence: |
    PASS. Exactly one prosecution label sentence (§6 para 1, "As of the 2026-05
    record, the application is pending, with examination continuing after a final
    rejection... and a request for continued examination...") carrying all
    mandated elements; no office-action chronology in the body; steelman/closing
    references to the rejection and RCE are spine-authorized beats.
  collateral_beat: |
    PASS on all six elements in ONE paragraph (§6 para 2, 174 words): portfolio
    scope ("blanket over the portfolio at signing, with no selectivity about any
    single filing, so they say nothing about this application in particular");
    both reel/frames (067204/0877, 071792/0869); timing as dated fact (grants
    15 July 2025, lien 18 July 2025) with motive explicitly labeled inference
    ("is an inference, not a record"); both-ways frame ("concrete enough to
    bank... what a creditor reaches if things go wrong"); never patent-specific.
  both_or_neither: |
    PASS. Rejection label sentence and collateral beat both in §6, rejection first.
  figures: |
    PASS with one caption finding (r2-F1). All five selected figures placed
    (FIG. 5 header + 1/2/6/7 body); FIG. 3/4 drop honored, their point carried via
    [0039]. FIG. 6 re-verified against the drawing WITH FRESH EYES this round:
    605A-D are the rounded blocks INSIDE ICs 615A-D (auxiliary circuitry) and
    610A-D are the small EXTERNAL chips wired only to the 605 blocks (local
    memory) — the draft caption is correct and the manifest one-liner's swap is
    confirmed wrong; round 1's override stands. FIG. 5 caption numerals (505A/B,
    510A-D, 515A-D, 520, 215, 220) re-verified against the drawing. FIG. 2 caption
    (215A-I, 220 tiles, 210A-C top row, 205 host, 240 PCIe, 225/230, 250)
    re-verified. FIG. 1 body description (weights 110 top-down into DPUs 105,
    previous tensor 115 from the left) re-verified. FIG. 7 caption is the one
    miss — see r2-F1.
```
