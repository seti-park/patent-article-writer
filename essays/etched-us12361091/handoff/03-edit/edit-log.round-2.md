# Edit Log — Round 2

```yaml
review_id: etched-us12361091-editorial-review-2
draft_source: handoff/02-compose/essay-draft.md
publication_strip: handoff/02-compose/publication.md
review_timestamp: 2026-07-02T23:40:00Z
posture_applied: measured
closing_posture_declared: firm
overall_assessment: pass
round: 2
carried_findings: r1-F1..r1-F17 ruled below (re-review protocol step 2 before new hunting)

gate_context: >
  gate-result.round-2.json: all 13 gates PASS. Warns re-verified rather than trusted:
  1x STRUCT-004 — the two triads ("Split ... / Wire ... / Run no wire ..." = claim 1's
  three requirements as imperatives; "methods, topology, and AI-model computation" =
  the spec's own example families) are content-bearing factual enumerations, not
  reflexive rule-of-three. 7x LONGSENT-001 decomposed by hand: frontmatter merge (38w),
  heading merge (41w = the 11w "None of its claims..." sentence + the §2 heading + the
  22w document-identity sentence — arithmetic checks exactly), Sources-block merge
  (137w), footnote merges (109w, 43w), and two real 34-37w sentences ("The stated
  payoff..." and the thin-moat sentence) that are quote-integrated claim-clause
  sentences permitted by deliverable-voice-rules ("a necessary causal or claim clause
  may run longer"). Round-1's warn attribution remains accurate on the round-2 output;
  warn count fell 9 -> 7 consistent with the r1-F7 cut and r1-F9 splits.

# ==================================================================
# PART 1 — CARRIED-FINDING RULINGS (r1-F1 .. r1-F17)
# Every disposition verified against the CURRENT draft text; quotes are
# from draft_version 2. No id dropped.
# ==================================================================

carried_rulings:

  - finding_id: r1-F1
    round1_severity: high
    composer_disposition: applied
    ruling: verified-landed
    evidence: |
      §1 ¶1 now reads "Half of the loudest architecture claim in the thread already
      has a granted US patent standing behind it. The other half, the shared memory
      pool that gives Cluster-Scale Memory its name, has no granted substance in the
      filings you can read today." — halves vocabulary owns the CSM split. §1 ¶3 now
      reads "Low-Voltage Inference is the power pillar. Cluster-Scale Memory, or CSM,
      is the one that pulled readers in" — "pillar" reserved for LVI/CSM, so §6 ¶5's
      "The thread's other pillar" (LVI) reads against a clean definition. Title, ¶1,
      and §7 scope now agree (patent backs the interconnect half of CSM only). BLUF
      stays declarative; no re-parse forced at ¶3. No neighbor regression: ¶1 and ¶3
      are each 4 sentences.

  - finding_id: r1-F2
    round1_severity: high
    composer_disposition: applied
    ruling: verified-landed
    evidence: |
      §6 ¶3 now reads "The memory half has no equivalent fence anywhere in the claims.
      In the description, memory is scenery. FIG. 6 shows ... a memory 630 whose role
      is to 'provide tensors and other data to the tensor parallel groups 620 for
      processing' [0119]. The description also lets each chip couple to memory
      devices, shared among the chips or not, and no claim picks that option up
      [0133]. Described, never claimed." The false document-wide absolute is gone;
      the absolute now lives at claims level, which I re-verified independently:
      the granted claims 1-23 contain zero occurrences of "memory" and zero of
      "latency" (mechanical grep of the claims text). [0133]'s shared-or-not wording
      is absorbed with permissive modality intact ("lets ... couple"), i.e. no
      option-to-lock drift introduced by the fix. Spillover fix confirmed: FIG. 6
      caption now reads "box 630, the memory that feeds the tensor parallel groups,
      described in one embodiment figure and never claimed [0119]" — the caption's
      old "the patent's only memory" absolute is gone. Memory-leg verdict untouched.

  - finding_id: r1-F3
    round1_severity: high
    composer_disposition: applied
    ruling: verified-landed
    evidence: |
      §6 ¶2 now reads "...and the whole fence is the wiring discipline the patent's
      own cluster-scale arithmetic runs on [0168], [0061]." The any-CSM-story
      necessity claim is gone; scope is the patent's own design, per the spine
      mitigation wording. The §3 switched-fabric foil no longer contradicts it, and
      the thin-moat concession one paragraph earlier stays conceded. Firmness kept
      (no hedge added). [0168]/[0061] carry exactly this (balance-by-split + the
      p/q optimum) — anchors now match claim scope.

  - finding_id: r1-F4
    round1_severity: medium
    composer_disposition: applied
    ruling: verified-landed
    evidence: |
      §6 ¶2 now reads "The thread's adjective was never claimable as such. A hop
      bound is, and claim 1 sets one: at most one device between any two chips, ever
      [0387]." The false apparatus-claim generalization is gone; the spine's narrower
      adjective claim is restored and the bound is tied to claim 1 (verified: the
      wherein clause is claim-1 text).

  - finding_id: r1-F5
    round1_severity: medium
    composer_disposition: applied
    ruling: verified-landed
    evidence: |
      §4 final paragraph now ends "No link runs hot. The equal channels are wired in,
      and the equal traffic follows from the split the description prescribes
      [0168]." The software-independence overclaim is gone; structure (channels)
      vs prescribed split (traffic) are correctly separated. Anchor precision
      re-verified: [0168] itself carries the unequal-split counterfactual ("had the
      first and second tensors been split in unequal tiles..."), so the single
      anchor covers the conditioned claim as now written.

  - finding_id: r1-F6
    round1_severity: medium
    composer_disposition: applied
    ruling: verified-landed
    evidence: |
      §7 ¶2 now reads "When they do, the scale-up domain becomes inspectable: the
      wiring either matches claim 1's cross-set pattern [0386] or it does not."
      Strictly binary (match/no-match against the claim); the excluded-middle pair
      is gone; closing-binary-test posture preserved under firm.

  - finding_id: r1-F7
    round1_severity: medium
    composer_disposition: applied
    ruling: verified-landed
    evidence: |
      "Held against each other, the two documents split the CSM story cleanly in
      two." is absent from the draft; §1 ¶4 now lands on "None of its claims mention
      latency, a bandwidth magnitude, or memory." The §1-internal double is gone.
      Residual restatement census on the current draft: the FULL two-sided verdict
      appears in §1 ¶1 and §7 only; §5's "It does not claim the store." and §6 ¶3's
      topic sentence carry only the memory-leg boundary inside their local scope
      (round-1's earn-their-place ruling re-affirmed on fresh read). Pass-7 check 7
      satisfied.

  - finding_id: r1-F8
    round1_severity: medium
    composer_disposition: applied
    ruling: verified-landed
    evidence: |
      §6 ¶2's fence list is now three elements: "cross-set-only direct channels
      [0386], degree- and bandwidth-uniform links (claims 3 to 5), and reduce and
      gather running simultaneously on disjoint channel families (claims 8, 9, 11)"
      — the [0387] list item is gone, and the hop bound is stated once in §6 (the
      "A hop bound is..." punchline). Body-wide [0387] census: §1 setup, §3 primary
      (verbatim quote), §6 single carry, §7 recap — the sanctioned pattern.

  - finding_id: r1-F9
    round1_severity: medium
    composer_disposition: applied (with one argued in-finding deviation)
    ruling: verified-landed; deviation ACCEPTED on the merits
    evidence: |
      All seven listed conversions confirmed in the current text (§2 period split at
      "own text. The specification enumerates"; §3 "(In graph-theory terms, this
      is...)"; §3 "The wire count stays modest. The eight-chip drawing gets by
      with..."; §4 "Disjoint lanes make simultaneity cheap. Claim 9 has..."; §4
      "Claim 11 names the pair, a reduction and a gather."; §6 r1-F2 rewrite removed
      the rectangle pivot; §6 "...narrower than the description's framing. The
      specification's summary covers..."). Independent recount on publication.md:
      20 colons in body prose, 9 of them quotation/blockquote lead-ins, ~11 true
      pivots in ~1,700 words (one per ~155 words, down from one per ~77). The
      fingerprint density is broken.
      Deviation judged: keeping "Uniformity is claimed as structure too:" in §4 ¶5 —
      converting it would push the paragraph to 8 sentences (Pass 2C high / the
      recount rule), and the paragraph's only other colon is the [0061] quotation
      lead-in, so the finding's stated per-paragraph target is met there. §6 ¶2's
      two non-quotation colons are the fence-list enumeration colon (a genuine list
      introduction, not an announcement pivot) and the hop-bound pivot the round-1
      finding named as a keeper. Deviation accepted; residual density is voice-clean
      under anti-ai-writing's cluster standard.

  - finding_id: r1-F10
    round1_severity: medium
    composer_disposition: applied
    ruling: verified-landed
    evidence: |
      §2 ¶2 split at the recommended seam — "It did not file alone... the model-level
      execution those moves add up to." (48w, ~4.0 mobile lines) | "The division of
      labor is visible... not filing a one-off." (82w, ~6.8 lines). §6 tail split at
      "...that the thread folds into CSM." (56w) | "The company says its math
      blocks..." (59w). Post-split band recount across the whole draft: all body
      paragraphs sit at 3-7 sentences (the three sub-3-sentence lines — the K4,4
      labeled aside, the FIG. 7A/7B pointer line, and the [0278] blockquote lead-in —
      pre-date round 1 and are transition/aside beats, not new stubs). No figure
      reference orphaned; marginal §6 ¶2 / §7 ¶1 remain noted-no-action as round 1
      ruled.

  - finding_id: r1-F11
    round1_severity: low
    composer_disposition: applied
    ruling: verified-landed
    evidence: |
      §2 ¶3: "Etched is paying to keep all three alive: a PCT filing extends each
      abroad, and a US continuation, published in 2026, keeps each open at home."
      Continuation no longer filed under the beyond-US umbrella; both instruments
      get correct one-clause functional glosses.

  - finding_id: r1-F12
    round1_severity: low
    composer_disposition: applied
    ruling: verified-landed
    evidence: |
      §2 ¶1: "filed 22 October 2024 and granted 15 July 2025, inside nine months"
      (arithmetic verified: 266 days ≈ 8.7 months); the 266-day computation moved to
      [^derived-counts] with attribution intact. No unanchored pendency baseline
      added.

  - finding_id: r1-F13
    round1_severity: low
    composer_disposition: applied
    ruling: verified-landed
    evidence: |
      Header caption now anchors the cross-pair + no-wire-inside sentence to
      "[0128], [0129]" and keeps [0125] on the families-overlaid sentence. Caption
      content re-verified against fig-07C.png: 710a right (a1, a3, a5, a7), 710b
      left (a0, a2, a4, a6), 16 cross-set channels, none within a column — accurate.

  - finding_id: r1-F14
    round1_severity: low
    composer_disposition: applied
    ruling: verified-landed
    evidence: |
      §5 ¶1: "...then projection, then an MLP [0252]. From there the work hands off
      to decoding, the token pick [0259]." Decoding 930 no longer attributed to what
      the 905 layers "run"; [0259] verified as the correct anchor ("After the
      operations of the decoding layers 905 are completed, the AI model 900 may
      perform decoding 930").

  - finding_id: r1-F15
    round1_severity: low
    composer_disposition: applied
    ruling: verified-landed
    evidence: |
      §4 ¶5: "...and the same amount crosses each channel [0168], [0178]." — the
      first-family mirror anchor is present ([0178] verified: "a same amount of data
      may be shared across each of the first communication channels 730").

  - finding_id: r1-F16
    round1_severity: low
    composer_disposition: applied
    ruling: verified-landed
    evidence: |
      §5 final paragraph: "This is the closest the filing comes to the thread's
      memory idea." — the "and precision matters here" stage direction is gone.

  - finding_id: r1-F17
    round1_severity: low
    composer_disposition: applied
    ruling: verified-landed
    evidence: |
      §3 ¶5: "The relay need not even hold the message, since an intermediate chip
      may begin forwarding data before it has finished receiving it [0143]." —
      capability modality restored ([0143] "may also be configured to transmit a
      portion of data to be received before all data is received"); the since-clause
      form avoids adding a colon pivot, consistent with r1-F9.

# ==================================================================
# PART 2 — FRESH 7-PASS REVIEW OF THE CURRENT DRAFT (new findings)
# ==================================================================

findings:

  # ----------------------------------------------------------------- LOW ----

  - finding_id: r2-F1
    pass: pass-3-fact-paraphrase
    location: "§4 'The Wiring Schedules the Traffic', paragraph 1, sentence 2"
    severity: low
    severity_under_default_posture: low
    finding: |
      Anchor under-coverage (same class as fixed r1-F15): "Each set subdivides into
      two groups of chips, labeled 712a through 712d, and the channels split with
      them into two families [0135]" carries three sub-claims on the range's first
      anchor only. [0135] supports the four-group naming; the each-set-contains-two
      fact is [0136] ("the first group ... and the second group ... may be formed
      from the first set 710a ..."), and the two-families fact is [0138]/[0139]
      (cited only in the following sentences). Phase 1's own support for this step
      is the range [0135]-[0139]. All three sub-claims are TRUE against the patent
      (verified), and claim 18's structure statement in §6 locks the two-groups-per-
      set fact independently; only the citation is compressed.
    recommendation: |
      Extend the anchor set to what the sentence actually spans, staying inside the
      Phase-1 anchor inventory (note: the literal token [0136] is not in the Phase-1
      handoff, so do NOT introduce it without a Phase-1 extraction — gate_anchors
      would fail). Gate-safe fix: "...and the channels split with them into two
      families [0135], [0138], [0139]." Alternatively reword the lead clause to what
      [0135] states ("The chips subdivide further into four groups, labeled 712a
      through 712d [0135]") and let the adjacent pairing sentences + captions carry
      set membership, which they already do.
    quote: "Each set subdivides into two groups of chips, labeled 712a through 712d, and the channels split with them into two families [0135]."

  - finding_id: r2-F2
    pass: pass-3-fact-paraphrase
    location: "§4 paragraph 2 (FIG. 7A/7B pointer line) and FIG. 7B caption, final sentence"
    severity: low
    severity_under_default_posture: low
    finding: |
      Anchor precision (same class as fixed r1-F13, two residual instances): the
      FIG.-7C-is-the-union identification rides [0123] alone in "the dense web of
      FIG. 7C is the two overlaid [0123]" and in the FIG. 7B caption "Added to
      FIG. 7A's links it gives the full FIG. 7C web [0123]". [0123] supports
      7A+7B-as-subgraphs and the union ("may include all the connections of FIGS.
      7A and 7B") but never mentions FIG. 7C; the 7C-in-a-single-figure fact is
      [0125] (already used, correctly, in the header caption). Content verified
      accurate against the figures; only the pointer is one paragraph off.
    recommendation: |
      Cite both where FIG. 7C is named: "...the dense web of FIG. 7C is the two
      overlaid [0123], [0125]" (and likewise in the FIG. 7B caption), or move the 7C
      clauses onto [0125] and leave [0123] on the separated-for-legibility clause it
      supports. [0125] is in the Phase-1 quote-anchor table; no extraction needed.
    quote: "FIG. 7A and FIG. 7B draw one family each, separated purely for legibility, and the dense web of FIG. 7C is the two overlaid [0123]."

  - finding_id: r2-F3
    pass: pass-3-fact-paraphrase
    location: "§5 'The Description Aims It at Transformer Decoding', paragraph 2, final sentence"
    severity: low
    severity_under_default_posture: low
    finding: |
      Option-to-act modality drift (same class as fixed r1-F17, weaker instance):
      "The description sizes the tensor parallel group around exactly that operation
      [0121]" states as the description's definite act what [0121] offers as its
      lead example among alternatives ("the size of the tensor parallel groups 620
      MAY be based on the largest computation ... For example, ... the computations
      performed by the feedforward operations performed by a MLP layer"; a
      sub-multiple sizing alternative follows in the same paragraph). The section's
      framing is honest (description-level intent, opened by "None of this is
      claimed for AI"), and the sentence misleads no verdict-relevant point — but
      the modality clip is the drift class the handoff notes fence.
    recommendation: |
      Restore example/option status without hedging the section's point, for
      example: "The description's sizing example builds the tensor parallel group
      around exactly that operation [0121]." (Keeps "exactly that operation" — the
      pointing is accurate — and returns the act to the description's worked
      example.)
    quote: "The description sizes the tensor parallel group around exactly that operation [0121]."

  # ------------------------------------------------ NO-FINDINGS PASSES ----

  - pass: pass-1-voice-anti-ai
    finding: "no findings"
    scoped_to: |
      Banned-word grep re-run on publication.md (full Tier-1 list + govuk swaps +
      co-occurrence set: delve/leverage/crucial/robust/seamless/landscape/utilize/
      facilitate etc.): zero hits. Banned patterns: no not-just-X-but-Y, no
      despite-challenges, no copula avoidance (represents/constitutes/serves-as:
      zero), no vague attributions, no puffery, no section summaries, no elegant
      variation (Etched/"the company" and patent/filing/grant alternation is
      register-normal and role-consistent). Formatting: exactly one bold span (the
      sanctioned §6 thesis anchor), no bullets outside Sources, no emoji, no
      ALL-CAPS beyond acronyms (FIGS/SRAM), no exclamation marks, no Latin
      abbreviations, no em-dash, one semicolon and it sits inside the thread's
      verbatim quote. Colon-pivot density re-verified post-r1-F9 (~11 true pivots /
      ~1,700 words, max one non-quotation pivot per paragraph except §6 ¶2's
      list-colon + named-keeper pair — accepted under the r1-F9 ruling above).
      Fragments ("Out of stealth after taping out its A0 silicon.", "Described,
      never claimed.") read as deliberate inventory/landing cadence — false-positive
      guard applies.

  - pass: pass-2-redundancy
    finding: "no findings"
    scoped_to: |
      2A claim-repetition sweep on the revised draft: hop bound now 4 statements in
      the sanctioned lead/primary/§6-single/recap pattern (r1-F8 verified); [0124]
      spent twice (primary + verdict recap — the citation-priority map allows
      exactly this); [0168] carries distinct work per use (statement+counterfactual
      in §4, fence arithmetic in §6, recap in §7); 16-vs-28, p=4.35235, $1B/$800m,
      "inside nine months", 4x MLP each spent once (4x twice with distinct anchors
      [0258]/[0313] doing different work — accepted round 1, re-affirmed). The
      "checkable/check" motif (header, lead, §2 opener, verdict, landing) is the
      thesis's operating word in five distinct roles — deliberate repetition,
      not claim redundancy. 2B: the two 34-37w survivors are quote-integrated
      claim-clause sentences (exemption applies). 2C: no paragraph exceeds 7
      sentences (max 7 at §3 ¶5, §4 ¶5, §5 ¶1, §7 ¶1); >150w single-idea: only
      §3 ¶5 (160w, quote-integrated, demoted per posture lens — carried
      noted-no-action).

  - pass: pass-3-fact-paraphrase
    finding: "no findings beyond r2-F1/F2/F3"
    scoped_to: |
      Every double-quoted patent span in the draft byte-checked against
      input/patent.md by script: [0021], [0026], [0386], [0387], [0124], [0140]
      blockquote (incl. " 730 ." spacing), [0168], [0061], [0251], [0313], [0278]
      blockquote (incl. " 905 ." spacing), [0267], [0119], [0385] — zero mutations.
      [0386]/[0387] independently confirmed verbatim inside granted claim 1 (the
      blockquote's "claim 1" attribution is correct). Claims-level absolutes
      re-verified mechanically: claims 1-23 contain zero "memory", zero "latency",
      and bandwidth only as claim 5's equality — so "None of its claims mention
      latency, a bandwidth magnitude, or memory" (§1), "No granted claim recites a
      latency figure or a bandwidth magnitude" (§6), and "none of them mentions
      memory" (§6) all hold. Claim-scope traps re-verified against the claims text:
      1/14 four-or-more per set; claim 18 two-or-more + two-groups-per-set +
      dual-family exclusivity, WITHOUT simultaneity attributed (claim 9's
      limitation); claim-11 reduction/gather stated without physical-family lock
      while gather-on-730/reduction-on-740 is labeled the description's worked
      example [0140]; eight devices / 16-vs-28 flagged as figure arithmetic in body
      + footnote; link technologies kept description options; equal-not-high
      bandwidth stated explicitly. Figure check: fig-07C.png inspected — header
      caption accurate (sets, sides, 16 channels, no intra-column wire, both
      families). External facts: all company numbers ($1B, $800m, half-voltage,
      summer-2026 racks) carry the-company-says/company's-own-account attribution;
      thread quotes byte-match input/essay-context.md transcription; trio
      metadata (903 May-2025, 262 same-day, PCT + 2026 continuations, 2044 term)
      matches fact-check-log tier-2 rows; "inside nine months" arithmetic verified;
      18-month unpublished-window statement is essay-context-sanctioned; no tier-4/5
      anchor anywhere. [0026]'s "may be expensive" rendered as "the filing calls
      'expensive to include...'" judged acceptable attribution of the patent's own
      foil motivation (quote verbatim-contiguous; patent drafting modality, not a
      substantive hedge being clipped) — reviewed and deliberately not flagged.

  - pass: pass-4-logic-causality
    finding: "no findings"
    scoped_to: |
      4A: thesis-trace (draft_version 2) checked against thesis-spine's
      spine->section trace — all seven sections carry their assigned elements; the
      two revision-added anchors ([0178] §4, [0259] §5) are in-spine; no
      out-of-spine section-level claim found in the revised text; r1-F1/F3/F5/F6
      fixes verified to pull the previously drifting sentences back inside the
      spine. 4B: causal sweep — "The families exist so two kinds of traffic never
      share a wire" (purpose supported by claims 8/9 structure + [0140]); "Disjoint
      lanes make simultaneity cheap" (mechanism given, claim 9/[0142]); "That is the
      filing pattern of a company fencing an architecture" (pattern-reading on
      tier-2 facts, evidence-proportionate); twelve-months-before stated as
      sequence, not cause; "in effect, published the diagram" labeled analysis. 4C:
      lead tension (checkable split) resolved by §7; closing matches the spine's
      Acknowledged-residual -> closing-binary-test mapping under firm; no section
      surprises the lead's setup.

  - pass: pass-5-reader-perspective
    finding: "no findings"
    scoped_to: |
      Jargon budget: tensor, reduction, gather, systolic array, K4,4 (labeled
      aside), MLP, HBM/SRAM, PCT ("extends each abroad"), continuation ("keeps each
      open at home") all glossed one-clause on first use; "scale-up domain" enters
      inside the thread's verbatim quote and recurs in §7 where the apposition
      ("the wiring...") carries it — accepted per the Phase-1 audience note that
      the reader arrives from the thread already holding CSM vocabulary. 5C mobile
      recount post-splits: former offenders §2 ¶2 and §6 ¶6 now 4.0/6.8 and
      4.7/4.9 lines; remaining >8-line paragraphs (§3 ¶1/¶5, §4 ¶5, §5 ¶1/¶2, §6
      ¶1) are quote-integrated structures demoted per the posture-lens heuristic;
      §7 ¶1 at ~8.6 lines carries round-1's noted-no-action ruling (verdict
      paragraph; splitting would fragment the call). Engagement curve: stake
      resurfaces §3 ¶2 ("a switch or a wire per pair"), §4 ¶1 ("stops being
      textbook"), §5 ¶1 ("None of this is claimed for AI"), §5 close ("It does not
      claim the store"); money thread feeds the verdict in §2 (commitment), §6
      (caution), §7 (binary test). Closing readable in isolation; bookending
      intact.

  - pass: pass-6-lead-conclusion-format
    finding: "no findings"
    scoped_to: |
      6A: lead sentence 1 = news event, sentence 2 = declarative half-verdict,
      sentence 3 = the other half — thesis + patent + stake inside three sentences
      (r1-F1 fix verified scope-true). 6B: frame closure — the lead's
      thread-vs-grant friction returns in §7 ("The thread sells a memory story. The
      granted record holds a wiring story."); Acknowledged residual under declared
      firm maps to the delivered closing-binary-test, not an open question. 6C:
      # Sources exactly once; categories Patents + Official statements (both in
      enum); 4 entries across 2 categories -> subgrouped, all-or-nothing satisfied.
      6D: no Papers — n/a. 6E: em-dash 0 outside quotes; all inline cites 4-digit
      and Phase-1-resolvable (gate_anchors/gate_quotes PASS + my independent
      spot-set); footnotes stripped from publication.md; banned grep clean;
      # Sources once. 6F: title uses no separator. 6G at full strength BOTH
      directions under closing_posture: firm — verdict leads with the call ("Hold
      the thread against the grant and the verdict is firm both ways"), no
      qualifier-led opening, zero safe-harbor boilerplate (no "patents don't
      guarantee...", no "time will tell"), exactly ONE patent-specific anti-hype
      guard (LVI/HBM-SRAM absence + 18-month window, §6, stated once), limits
      referenced from §7 ("The boundaries set out above scope that call. They do
      not soften it.") not re-listed, and no over-firm inversion: every §7 recap
      clause traces to established claims/anchors, and rack-practice is explicitly
      reserved for the binary test rather than asserted. gate_hedge PASS is
      consistent with this reading.

  - pass: pass-7-adversarial-reader
    finding: "no findings"
    scoped_to: |
      1 BLUF: ¶1 sentence 2 is a declarative verdict ("Half of the loudest
      architecture claim ... already has a granted US patent standing behind it.")
      — no deferred question. 2 Header-as-claim: all seven ## headers are
      assertions; header-only skim reconstructs the argument (checkable half ->
      structure patent being extended -> switchless reachability -> wiring
      schedules traffic -> aimed at transformer decoding -> no latency/memory
      claim -> one leg substantiated, one absent). 3 Steelman: present,
      THIS-patent-specific, conceded at full strength (§6 ¶1: topology-only claim,
      standard links [0134], no latency figure, equal-not-high bandwidth, wins are
      cost/bandwidth while the thread's adjective is latency), then refined without
      un-conceding (post-r1-F3 text verified); no generic patent truism anywhere;
      the validity-flavored "K4,4 is textbook" objection is pre-empted by the essay
      never resting novelty on the bare shape ("where the shape stops being
      textbook" -> claims 8/9/11 binding). 4 Meta: no reader-instruction or
      essay-self-reference ("The objection an informed reader should press" frames
      the objection's strength, not the reader's behavior; provenance parentheticals
      are functional scope notes — exempt); the r1-F16 instance is gone. 5 Jargon
      as signpost: no doctrinal deep-dive; K4,4 one line; p/q decimals spent once
      with the practical reading attached. 6 Stub/rhythm: §7 186w / §2 192w, both
      multi-paragraph and content-complete; no section markedly under its siblings'
      job. 7 Thesis restatement: full verdict in §1 + §7 (= 2 sections); §5/§6
      instances are leg-scoped local boundary work (census under r1-F7 ruling).
      Impatient-investor read: answer in ¶1, numbers by ¶2, no un-glossed blocker,
      the money thread never drops for more than one section. Skeptical-pro read:
      the strongest objection is the one the essay itself presses hardest, and its
      rebuttal now stands entirely on claim text and the patent's own arithmetic.

# ==================================================================
# PART 3 — OVERALL
# ==================================================================

severity_census:
  critical: 0
  high: 0
  medium: 0
  low: 3   # r2-F1, r2-F2, r2-F3 (all pass-3 anchor-precision/modality polish)
```

**Overall assessment: pass** — all 17 round-1 dispositions verified landed in the text (r1-F9's argued deviation accepted on the merits: the kept colon avoids an 8-sentence paragraph and the finding's per-paragraph target is met); the three round-1 highs are fixed without hedging the verdict, and the fresh 7-pass sweep of draft_version 2 surfaces only three low-severity anchor-precision/modality polish items (r2-F1/F2/F3), none publication-blocking and none touching the verdict, the steelman, or the figure record. Under the double-clean rule this is the FIRST clean round: acceptance requires an independent round-3 confirmation, and r2-F1/F2/F3 are available to the composer as optional polish before it.
