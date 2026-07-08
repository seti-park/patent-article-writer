# Edit Log — Round 1

```yaml
review_id: etched-us20240378175-editorial-review-1
draft_source: handoff/02-compose/essay-draft.md
publication_strip: handoff/02-compose/publication.md
review_timestamp: 2026-07-04T00:00:00Z
review_round: 1
posture_applied: measured
closing_posture_declared: firm
edition: pending-application (first of its kind; input/essay-context.md controls)
overall_assessment: revise-recommended
assessment_rationale: |
  No high or critical findings. Seven medium findings (fidelity blur on the latency
  rationale, a specialization overstatement against [0019], a self-reference cluster,
  thesis-formula over-restatement, mobile-length paragraphs, one unanchored Sources
  entry, one unglossed verdict-section term of art) plus three low. Edition compliance
  (application-era language, one label sentence, one-paragraph collateral beat,
  both-or-neither) verified clean. Verdict shape (6G) clean in BOTH directions.
  No hard-gate-relevant finding: no pass-3 high/critical grounding issue, no
  FIGUSE/coverage issue, no 6G high under the firm posture.

findings:

  - finding_id: r1-F1
    pass: pass-3-fact-paraphrase
    location: "§4 (The Application Claims a Memory Interface With No Switch in It), paragraph 2; echoed in §1 lead paragraph 1 ('the philosophy it wrote down')"
    severity: medium
    severity_under_default_posture: medium
    finding: |
      The sentence "the price is a layer of silicon, with its space, power, and latency,
      sitting between memory and math" folds "latency" into the switch's cost while the
      prose is walking through the filing's own reasoning. The filing books the deletion's
      gain as space and power only ("which can save space and power" [0045], q-0045-2);
      latency is nowhere in the application (verified against patent.md full text). Latency
      is the 2026 thread's vocabulary ("every layer between compute and memory costs
      latency" — company-claimed, correctly attributed in the lead). Blending the two blurs
      the exact source-vs-narrative line this pending-application edition exists to hold,
      and it is load-bearing: the essay's bridge is "the thread's latency philosophy = this
      claim language." A skeptical reader who opens the filing finds no latency rationale.
    recommendation: |
      Narrow or label — do not hedge. Cleanest fix strengthens the essay: keep the
      structural cost ("a layer of silicon, with its space and power, sitting between
      memory and math") and make the vocabulary gap explicit at the §4 bridge, e.g.
      "The filing books the gain as space and power; latency is the word the 2026 thread
      added." Then "this is that idea's earliest written form" reads as the structural
      idea (no middle layer), which the source fully supports.
    quote: "The switch buys flexibility. Any part of the chip can reach any region of the memory, and the price is a layer of silicon, with its space, power, and latency, sitting between memory and math."

  - finding_id: r1-F2
    pass: pass-4-logic-causality
    location: "§3 final paragraph ('worth building only in a world where one workload...'); §5 final paragraph ('None of this reads like a generic accelerator filing.')"
    severity: medium
    severity_under_default_posture: medium
    finding: |
      Both sentences overstate the document's specialization relative to its own text. The
      specification explicitly generalizes: "they are not limited to such and can be used
      for other applications (e.g., cryptography, DNA and protein sequencing, digital
      signal processing, and the like)" [0019], and [0026] repeats the crypto/DSP framing.
      Claim 39 itself — the essay's core — carries no AI or transformer limitation as
      drafted. The transformer-shape reading is well supported where the essay anchors it
      (claims 11-13's self-attention division, [0047], FIG. 7's transformer stages), but
      "only" and "none of this" claim more than the source; a pro-subject reader who opens
      the filing sees the generality clause immediately.
    recommendation: |
      Narrow the claim to what the anchors support, or pre-empt with labeled analysis.
      Example for §5: "The spec waves at cryptography and DNA sequencing, as filings do
      [0019], but the claim set's self-attention split and the timing chart are cut to a
      transformer" — this concedes the boilerplate breadth and makes the transformer-shape
      point sharper, not softer. For §3, replace "is worth building only in a world where"
      with a formulation tied to the preset-loop evidence, e.g. "is a machine you build
      when one workload deserves its own dedicated hardware" (the bet reading stays firm;
      the false exclusivity goes).

  - finding_id: r1-F3
    pass: pass-7-adversarial-reader
    location: "§2 paragraph 2 sentence 1; §6 paragraph 1 sentence 2; §7 paragraph 2 final sentence"
    severity: medium
    severity_under_default_posture: medium
    finding: |
      Essay-self-reference cluster (meta-reader-instruction class; below gate_meta's regex
      resolution but a pattern in aggregate — three instances of the essay narrating its
      own construction):
      (1) "One distinction carries all the weight in what follows." — "in what follows"
      names the essay as an object.
      (2) "That single sentence is the entire prosecution status, and both halves of it
      matter:" — points the reader at the essay's own sentence (and advertises the
      label-sentence budget, which is pipeline machinery, not insight).
      (3) "The rejection record and the blanket liens set out above scope this call
      without softening it." — "set out above" + commentary on the essay's own call.
    recommendation: |
      Rewrite all three without self-reference; the content survives intact:
      (1) "One distinction carries all the weight."
      (2) "Both halves of that record matter: the claims have been refused once, and the
      company is still spending money to pursue them."
      (3) "The rejection record and the blanket liens scope this call without softening it."

  - finding_id: r1-F4
    pass: pass-5-reader-perspective
    location: "§6 paragraph 2 (collateral beat, 197 words ≈ 16 mobile lines); secondarily §7 paragraph 2 (139 words) and §6 paragraph 3 (steelman, 131 words)"
    severity: medium
    severity_under_default_posture: medium
    finding: |
      5C mobile-rendering: the collateral paragraph runs 197 words (~16 lines on a 6"
      screen against the ≤8-line heuristic) with no integrated quote to earn the demotion.
      Constraint acknowledged: the edition contract REQUIRES the collateral beat to be ONE
      paragraph, so splitting is not an available fix — compression inside the paragraph
      is. §7 paragraph 2 (139 words) and the §6 steelman paragraph (131 words) also exceed
      the heuristic; the §3/§4 mechanism paragraphs of similar length are quote-integrated
      and demote to low under measured posture (not flagged).
    recommendation: |
      Compress the collateral paragraph in place toward ~150 words while keeping every
      contract element (both reel/frames, 3-day timing as dated fact, motive labeled
      inference, portfolio scope, both-ways frame). Candidate cuts: merge sentences 4-5
      ("The second and third of those grants had issued on 15 July 2025, three days
      earlier; reading that as a lender promptly sweeping fresh assets into its collateral
      is an inference — the registry gives dates, not motive."), and tighten the 41-word
      "cuts both ways" sentence. For §7 paragraph 2, r1-F5's cut of one date restatement
      does most of the work.

  - finding_id: r1-F5
    pass: pass-2-redundancy
    location: "Cross-section: §1 lead; §3 final sentence; §4 bold anchor + following paragraph; §5 final sentence; §7 paragraphs 1-3"
    severity: medium
    severity_under_default_posture: medium
    finding: |
      Pass-7 check 7 / pass-2 2A: the core thesis formula "the bet/philosophy was in
      writing in May 2023 (and is not yet property)" is asserted in five sections — §1
      ("has been in writing since 10 May 2023"), §3 ("In May 2023, two founders were
      already betting on that world in a patent filing"), §4 (bold anchor: "not a 2026
      slogan here... claim language Etched has been asking the patent office for since
      May 2023"), §5 ("the same specialization bet the company now sells as finished
      racks"), §7 (three times: "dated 10 May 2023", "the filing date stays 10 May 2023",
      "The philosophy was in writing by May 2023 either way"). The related "still paying /
      still spending / keeps funding" beat appears in §2, §6, §7, and the §7 header.
      Each section SHOULD feed the verdict (reader-profile rule 4) — the issue is the
      identical formula, not the tie-backs themselves.
    recommendation: |
      Keep the full formula in exactly three places: §1 lead, §4 bold anchor (the
      designated payoff), §7 verdict. Retool the §3 and §5 closers to point forward
      instead of restating (e.g. §3: "That inflexibility only pays off in one world — the
      one the memory half is built for."). Inside §7, cut one of the three date
      restatements (the cleanest: drop "dated 10 May 2023" from paragraph 1, since
      paragraph 2's "the filing date stays 10 May 2023" is the invariant list doing real
      work).

  - finding_id: r1-F6
    pass: pass-3-fact-paraphrase
    location: "# Sources > Patents, entry 2 (US 12,361,091 B1)"
    severity: medium
    severity_under_default_posture: medium
    finding: |
      Sub-pass 3B: the entry carries metadata anchored nowhere in this run's inputs — the
      title "Tensor parallel group", "priority 2024-10-22", and "inventors: Gavin Uberti".
      fact-check-log `prior-essay-wiring-half` covers only: granted, the wiring half,
      memory half absent from the granted record (internal-prior-run evidence level).
      `grant-lien-timing` anchors the 2025-07-15 issue date (second/third grants of the
      trio). Title, priority date, and sole-inventor attribution are unverifiable from the
      Phase-1 artifacts; the fact-check-log's edition note forbids silent upgrades.
    recommendation: |
      Trim the entry to anchored fields: "US 12,361,091 B1, Etched.ai, Inc., granted
      2025-07-15 (the 'wiring half'; companion analysis)." Alternatively, have Phase 1
      add the full bibliographic record to fact-check-log with its own evidence_level —
      but trimming is the round-2-safe fix.

  - finding_id: r1-F7
    pass: pass-5-reader-perspective
    location: "§7 paragraph 2: 'it is the likeliest of the four independents to survive in some form'"
    severity: medium
    severity_under_default_posture: medium
    finding: |
      "the four independents" lands in the verdict section unglossed, and the body never
      established that the application has four independent claims (1, 15, 26, 39) or what
      "independent" means. The reader has met claim 39, claims 7/8, claim 15, claim 1, and
      claim 26 separately, but the count-of-four and the term of art both appear here for
      the first time — a reader-profile rule 1 (jargon gloss) and rule 5 (prerequisite
      chain) miss at the exact sentence the verdict leans on.
    recommendation: |
      Either gloss in place ("the likeliest of the application's four standalone claims —
      the ones the other thirty-eight hang off — to survive in some form") or seed the
      count earlier where claim 1 and claim 26 are introduced (§6 steelman: "two of the
      application's four independent claims").

  - finding_id: r1-F8
    pass: pass-3-fact-paraphrase
    location: "§3, sentence after the [0018] blockquote"
    severity: low
    severity_under_default_posture: low
    finding: |
      The essay's own scale illustration (correctly footnote-labeled as such) is
      imprecise: "Hundreds of gigabytes... more than an entire high-end laptop's storage."
      High-end laptops ship with 1-2 TB; "hundreds of GB" is not reliably MORE than that.
      The §4 companion ("One terabyte per second is roughly a full laptop drive's contents
      moving every second") works; this one wobbles. Reader-profile rule 2 comparisons
      must themselves survive scrutiny.
    recommendation: |
      Soften the comparator to match: "roughly a whole laptop's storage" or "several
      hundred phones' worth of photos" — any comparison where hundreds of GB genuinely
      sits at or above the familiar scale.

  - finding_id: r1-F9
    pass: pass-1-voice-anti-ai
    location: "§2 ('In plain terms:'), §4 ('Translated first:', 'The bandwidth follows:')"
    severity: low
    severity_under_default_posture: low
    finding: |
      Tier-2 judgment list (announcement-colon pattern): three colon-led pivots, two of
      them fragment-led ("In plain terms:", "Translated first:"). No single instance is a
      violation; as a cluster it edges toward the AI transition fingerprint. No Tier-1
      banned words or patterns anywhere in the draft (verified by scan on top of the
      passing gate).
    recommendation: |
      Convert one or two to plain sentences: "In plain terms, many small math grids..." /
      "Translated first, each memory channel is bonded...". Keep "The bandwidth follows:"
      if only one survives — it follows a complete clause and reads most natural.

  - finding_id: r1-F10
    pass: pass-2-redundancy
    location: "Body-wide; worst instances: §1 paragraph 1 sentence 3 (38 words), §6 'What they do say cuts both ways...' (41 words)"
    severity: low
    severity_under_default_posture: low
    finding: |
      2B tightening. LONGSENT-001's 21 warns were sample-verified rather than trusted:
      12 are artifacts (heading-joins across '# Sources', caption text, footnote defs —
      the 50/56/78/101/160-word hits) and 9 are real body sentences at 36-41 words with
      quoted spans excluded. Most carry claim clauses or the mandated two-sided collateral
      frame and are within the "pressure, not a cap" rule; two are plain prose that can
      shed 25% without loss.
    recommendation: |
      Split the lead's third sentence after "loan collateral" ("...as loan collateral.
      Meanwhile the philosophy it wrote down is presented on stage as shipping hardware.").
      The 41-word both-ways sentence is also r1-F4's compression target — one edit serves
      both.

  - pass: pass-1-voice-anti-ai
    finding: "no further findings"
    scoped_to: |
      Full-body case-insensitive scan against the Tier-1 banned word list and banned
      rhetorical patterns (not-just-X-but-Y, despite-challenges, copula avoidance, vague
      attribution, puffery, section summaries, elegant variation): zero hits. Bold usage:
      exactly one load-bearing thesis anchor (§4), compliant with the restrained-bold
      rule. No emoji, no ALL-CAPS emphasis, no semicolon-joined clauses, no Latin
      abbreviations, no exclamation marks. Fragments ("Now the memory half.") read as
      deliberate cadence, within the false-positive guard.

  - pass: pass-3-fact-paraphrase
    finding: "no further findings"
    scoped_to: |
      All 16 distinct [dddd] anchors resolve to invention-summary entries. Every quoted
      span (13 inline + 5 blockquotes, incl. both claim mirrors q-0013-1 and q-0016-1)
      byte-compared against the Quote anchor table AND patent.md: verbatim, and none
      extended across the flagged run-on artifacts. External claims traced to fact-check
      -log IDs: tp-lien-1-2024, tp-lien-2-2025 (reel/frames exact), grant-lien-timing
      (dates exact, motive labeled inference), prosecution-record, examiner-cited-field
      (8 refs, clusters verbatim), family-us-only (labeled bibliographic),
      etched-thread-2026-07 ("the company says" attribution present at every use),
      prior-essay-wiring-half (one clause, §2). Derived comparisons footnote-labeled.
      No evidence_level silently upgraded.

  - pass: pass-4-logic-causality
    finding: "no further findings"
    scoped_to: |
      4A: all seven sections verified against thesis-spine.md's spine→section trace and
      thesis-trace.md; every spine element lands in its assigned section; no out-of-spine
      claim found beyond r1-F1/r1-F2's scoping issues. 4B: the 3-day lien timing is
      handled as correlation with motive explicitly labeled inference (the essay's own
      exemplary case); "worth building only..." ruled under r1-F2. 4C: lead tension
      (narrative ahead of property right) resolves in §7; closing-binary-test matches the
      spine's Acceptance residual under firm posture.

  - pass: pass-5-reader-perspective
    finding: "no further findings"
    scoped_to: |
      Jargon glosses verified present on first use: systolic array, HBM, UCIe,
      self-attention, transformer, security interest, RCE ("a paid restart"), final
      rejection ("the examiner's formal no"), tensor, weights. Claim language handled
      translate-then-quote (§4 exemplary; §2's plain-meaning lead-in sentence satisfies
      the rule's intent). Engagement curve: hook lands in lead sentence 1; each mechanism
      section surfaces to the money thread; no 3+ paragraph density wall. Stake clarity:
      closing paragraph stands alone. "reel/frame" unglossed judged self-evident from
      "That record sits at" (not flagged).

  - pass: pass-6-lead-conclusion-format
    finding: "no findings"
    scoped_to: |
      6A: lead paragraph 1 is a declarative verdict (BLUF holds); patent on the table by
      sentence 2. 6B: closing returns to the lead's stage-vs-paper frame ("The racks are
      shipping, the company says. The paper is still asking."); closing-binary-test
      matches Acceptance residual + firm posture per posture-lens. 6C: Sources block has
      2 enum categories (Patents, Official statements), subgrouped all-or-nothing, 6
      entries. 6D: no papers, n/a. 6E: 0 em-dashes; all inline cites 4-digit; footnote
      defs stripped from publication.md (verified); '# Sources' exactly once. 6F: title
      uses a period separator, no em-dash. 6G BOTH DIRECTIONS under declared firm
      posture: verdict leads with the call ("the verdict is firm. This document is the
      origin record..."; "a roadmap in formation rather than a fence"); exactly ONE
      patent-specific anti-hype guard (claim 1 breadth, per the spine's budget); limits
      referenced, not re-listed ("The rejection record and the blanket liens... scope
      this call"); no safe-harbor boilerplate, no qualifier-led verdict, no stacked
      hedges — and no overreach: no asset-language for the pending set ("does not yet own
      anything in it"), no enforceability claims. The special edition risks (rejection
      record dragging the verdict into hedging / overcorrection into asset overreach)
      were checked explicitly: neither is present.

  - pass: pass-7-adversarial-reader
    finding: "no further findings"
    scoped_to: |
      Checklist run with quoted evidence: (1) BLUF — PASS, "The memory half... has been
      in writing since 10 May 2023... that document is still not an asset." (2)
      Header-as-claim — PASS, all seven ## headers are assertions; header-only skim
      reconstructs the argument. (3) Steelman — PASS and strong: THIS-application
      objection (crowded examiner-cited field, claim 1/26 breadth, "Three years of
      prosecution have produced no enforceable claim at all"), conceded at full strength
      in §6, refined in §7; no generic patent truism used as steelman. (4) Meta — FLAGGED
      as r1-F3. (5) Jargon-depth — PASS, terms kept as signposts (no doctrinal
      deep-dives). (6) Stub/rhythm — PASS, no section markedly shorter than siblings
      (§1's 3-paragraph lead is proportionate). (7) Thesis restatement — FLAGGED as
      r1-F5 (formula in 5 sections).

gate_warn_adjudications:
  - check_id: DUPE-001 (x2, "the best layer is no layer", lead vs §4)
    ruling: accepted-intentional
    rationale: |
      Both uses are attributed to the company and the §4 use is the essay's payoff move
      (2026 slogan held against 2023 claim language) — the echo IS the thesis mechanism.
      Earns its place. Note: if r1-F1 is applied, the §4 bridge sentence changes shape
      but should keep the echo.
  - check_id: STRUCT-004 (2 triads)
    ruling: accepted-functional
    rationale: |
      "space, power, and latency" (§4 — dissolves anyway if r1-F1 is applied) and the §7
      invariant list ("the filing date stays..., the named inventors stay..., and the
      content stays...") are functional enumerations, not reflexive rule-of-three padding.
  - check_id: LONGSENT-001 (x21)
    ruling: sample-verified, partially-artifact
    rationale: |
      Independently recounted: 9 real body sentences at 35-41 words (quotes excluded);
      the 50+/78/101/160-word hits are heading-join, caption, and footnote artifacts of
      the gate's tokenizer. Real instances handled under r1-F10 (low) and r1-F4.

edition_compliance_audit:
  application_era_language: |
    PASS. Grant-era verbs absent for claim content ("the application claims", "as
    drafted", "Etched is seeking", "asks for" throughout; "not something claim 1
    requires as drafted" follows the scope map's own column vocabulary). "Enforceable"
    appears only in negations that ARE the edition's framing ("before anything becomes
    enforceable", "produced no enforceable claim at all" — both sanctioned by the
    spine's steelman text); no enforceability/infringement claims anywhere.
  label_sentence: |
    PASS. Exactly one prosecution-status sentence (§6 paragraph 1) carrying pending +
    final rejection + RCE + as-of-2026-05; no office-action chronology or dates in the
    body (chronology lives only in the footnote apparatus, stripped from publication.md).
    §6's restatement sentence flagged under r1-F3 for its self-reference, not as a
    second label. Steelman and closing references to the rejection/RCE are
    spine-authorized beats, not battle narrative.
  collateral_beat: |
    PASS on all six contract elements: ONE paragraph (§6 para 2); portfolio scope
    explicit ("blanket over the whole portfolio at signing, with no selectivity about
    any single filing, so they say nothing about this application in particular");
    both liens with reel/frames (067204/0877, 071792/0869); 3-day timing as dated fact
    with motive explicitly labeled inference; both-ways framing verbatim in spirit
    ("cuts both ways... banked as collateral... what a creditor reaches if things go
    wrong"); never presented as patent-specific importance. Lead and §7 references to
    the pledge stay portfolio-scoped ("alongside the rest of the company's patent
    stack", "with the rest of the stack") — thesis-level carriage, not beat expansion.
  both_or_neither: |
    PASS. Collateral cited AND rejection labeled, same section (§6), rejection first.
  figures: |
    PASS. All five selected figures placed (FIG. 5 header + 1/2/6/7 body); FIG. 3/4
    drop honored, their point carried via [0039] in §3. FIG. 6 caption verified against
    the actual drawing: 605A-D are auxiliary-circuitry blocks inside ICs 615A-D, 610A-D
    are the external local memory chips — the draft correctly followed the spec over
    the manifest's swapped one-liner. FIG. 5 caption numerals (505A/B, 510A-D, 515A-D,
    520, 215, 220) verified against the drawing. FIG. 2 caption matches the vision
    manifest (215A-I, 210A-C, 205, 240).
```
