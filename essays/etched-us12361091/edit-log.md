# Edit Log — Round 3 (confirmation round)

```yaml
review_id: etched-us12361091-editorial-review-3
draft_source: handoff/02-compose/essay-draft.md
publication_strip: handoff/02-compose/publication.md
review_timestamp: 2026-07-03T01:45:00Z
posture_applied: measured
closing_posture_declared: firm
overall_assessment: pass
round: 3
carried_findings: r2-F1, r2-F2, r2-F3 ruled below (re-review protocol step 2; no
  composer dispositions exist — round 2 was the first clean round and no revision was
  performed before this confirmation round, by design)
independence_note: >
  Full 7-pass review executed from scratch on draft_version 2 BEFORE consulting the
  round-1/round-2 logs. Two of round 2's three findings (r2-F2, r2-F3) were
  independently re-derived in this review before the round-2 log was opened —
  treated here as replication, not inheritance. All quoted-span byte checks, the
  claims-1-23 vocabulary sweeps, the figure inspections, and the paragraph counts
  below are this reviewer's own reruns, not trusted from prior rounds.

gate_context: >
  gate-result.round-3.json: all 13 gates PASS. Warns re-verified rather than trusted.
  1x STRUCT-004: the two 'A, B, and C' triads located and judged — "methods, topology,
  and AI-model computation" (§2, the spec's own three example families, verified at
  [0336]-[0337]/[0385]+) and "the same number of chips, the same number of channels,
  and channels of the same bandwidth" (§4, literally claims 3/4/5) — both are
  content-bearing factual enumerations, not reflexive rule-of-three. 7x LONGSENT-001
  decomposed by hand on publication.md: the 137w/109w/43w/38w hits are parser merge
  artifacts at frontmatter/heading/Sources/footnote boundaries (recomputed: the final
  body sentence is 15 words; the merge arithmetic checks); the 41w hit merges the 11w
  "None of its claims..." sentence across the §2 heading; the two real 37w survivors
  ("The stated payoff..." §3; the thin-moat sentence §6) are quote-integrated /
  claim-clause sentences permitted by deliverable-voice-rules ("a necessary causal or
  claim clause may run longer"). Independent mechanical re-checks this round: em-dash
  0, en-dash 0, exclamation 0, banned-term grep 0 hits, one semicolon (inside the
  thread's verbatim quote — exempt), all inline cites 4-digit, # Sources exactly once,
  no footnote defs in publication.md.

# ==================================================================
# PART 1 — CARRIED-FINDING RULINGS (r2-F1 .. r2-F3)
# No revision occurred after round 2 (confirmation round takes no
# revision), so there are no dispositions to verify. Each carried id
# is ruled on the merits against the current text. No id dropped.
# ==================================================================

carried_rulings:

  - finding_id: r2-F1
    round2_severity: low
    composer_disposition: none (no revision round occurred — by design)
    ruling: confirmed-still-present; finding independently re-validated; severity low (unchanged)
    evidence: |
      §4 ¶1 sentence 2 unchanged: "Each set subdivides into two groups of chips,
      labeled 712a through 712d, and the channels split with them into two families
      [0135]." Re-verified against patent.md this round: [0135] carries the
      four-group naming only; each-set-contains-two is [0136]; the two channel
      families are [0138]/[0139]. All three sub-claims true; citation compressed
      onto the range's first anchor. Round 2's gate-safety caution re-verified: the
      literal token [0136] is NOT in the Phase-1 handoff (gate_anchors would fail);
      the proposed gate-safe fix "[0135], [0138], [0139]" remains correct.
      Remains open as optional pre-publication polish; does not block.

  - finding_id: r2-F2
    round2_severity: low
    composer_disposition: none (no revision round occurred — by design)
    ruling: confirmed-still-present; independently re-derived this round before reading the round-2 log; severity low (unchanged)
    evidence: |
      Both instances unchanged: §4 ¶2 "the dense web of FIG. 7C is the two overlaid
      [0123]" and FIG. 7B caption "Added to FIG. 7A's links it gives the full
      FIG. 7C web [0123]". Re-verified: [0123] supports subgraphs-for-legibility and
      the union ("may include all the connections of FIGS. 7 A and 7 B") but never
      names FIG. 7C; the 7C-in-a-single-figure fact is [0125], which the header
      caption already cites correctly. [0125] is in the Phase-1 quote-anchor table —
      fix is gate-safe. Remains open as optional polish; does not block.

  - finding_id: r2-F3
    round2_severity: low
    composer_disposition: none (no revision round occurred — by design)
    ruling: confirmed-still-present; independently re-derived this round before reading the round-2 log; severity low (unchanged)
    evidence: |
      §5 ¶2 final sentence unchanged: "The description sizes the tensor parallel
      group around exactly that operation [0121]." Re-verified against [0121]: "may
      be based on the largest computation ... For example, ... the computations
      performed by the feedforward operations performed by a MLP layer" — an option
      offered as the lead example (with depth-based [0120] and sub-multiple [0121]
      alternatives adjacent), flattened to a definite act. The section frame ("None
      of this is claimed for AI"; "The intent lives one level down, in the
      description") keeps the drift off any verdict-relevant point. Round 2's
      recommended rewording remains apt. Remains open as optional polish; does not
      block.

# ==================================================================
# PART 2 — FRESH 7-PASS REVIEW (new findings, ids r3-*)
# ==================================================================

findings:

  # ----------------------------------------------------------------- LOW ----

  - finding_id: r3-F1
    pass: pass-3-fact-paraphrase
    location: "§5 'The Description Aims It at Transformer Decoding', paragraph 1, final-but-one sentence"
    severity: low
    severity_under_default_posture: low
    finding: |
      Anchor under-coverage, same class as r2-F1 (and fixed r1-F14/r1-F15), one
      residual instance neither prior round listed: "run normalization, then
      self-attention (QKV generation and attention computation), then projection,
      then an MLP [0252]". [0252] lists the four decoding layers (910/915/920/925)
      but never mentions QKV generation or the attention computation; those
      sub-blocks (916, 918) are described at [0254] ("The self-attention layer 915
      may include QKV generation 916 ... may also include performing the attention
      computation 918"). Content verified true against the patent and against
      fig-09A.png (which draws both sub-boxes directly below this sentence); only
      the citation is compressed.
    recommendation: |
      Gate-safe options ([0254] appears literally in the Phase-1 reference-number
      table rows for 915/916/918): extend the anchor set — "...then an MLP [0252],
      [0254]" — or drop the parenthetical and let FIG. 9A carry the sub-blocks it
      already draws. Do not reorder the layer list (verified correct against
      [0252]).
    quote: "run normalization, then self-attention (QKV generation and attention computation), then projection, then an MLP [0252]"

  - finding_id: r3-F2
    pass: pass-3-fact-paraphrase
    location: "FIG. 9A caption (§5, below paragraph 1)"
    severity: low
    severity_under_default_posture: low
    finding: |
      Anchor precision, same class as r2-F2: the caption "FIG. 9A: the
      decoding-layer loop the description maps onto the group [0251]" anchors the
      maps-onto-the-group claim to [0251], which only establishes what the model IS
      ("may be representative of a large language model or a transformer decoder").
      The mapping onto the tensor parallel group is [0252] ("a specific processing
      system, such as a tensor parallel group of FIG. 1 may be used to perform one
      or more of the operations of the decoding layers 905"). Caption content
      verified accurate against fig-09A.png (900 → 905: 910, 915 [916/918], 920,
      925 → 930).
    recommendation: |
      Cite both where the mapping is asserted: "...the description maps onto the
      group [0251], [0252]" — or keep [0251] and reword to what it supports ("the
      decoding-layer loop of the LLM the description has in mind [0251]"). [0252]
      is Phase-1-traceable (reference table + prior use in §5 body); gate-safe.
    quote: "*FIG. 9A: the decoding-layer loop the description maps onto the group [0251].*"

  - finding_id: r3-F3
    pass: pass-3-fact-paraphrase
    location: "§2 'A Structure Patent Etched Keeps Paying to Extend', paragraph 1, final sentence"
    severity: low
    severity_under_default_posture: low
    finding: |
      "It carries 23 claims, three of them independent, over 16 figures of one
      idea: how the chips of an AI cluster should be wired to each other" attaches
      the one-idea characterization to the 16 figures. True of the claims (all 23
      are wiring/topology — re-verified against the claims text this round); not
      true of the figures: FIGS. 3/4/5/8/10/11/12 are method flowcharts of the
      tile-movement/AI-model families, FIG. 9A/9B draw the AI model, FIG. 13 is
      computer boilerplate — figure territory the draft itself assigns to the spec's
      OTHER two example families two paragraphs later ("The specification enumerates
      three example families ... and the claims granted here track only the topology
      family"). A reader who opens the PDF sees flowcharts, not wiring, on 7 of 16
      sheets. Mild internal tension, self-corrected in-section; scene-setting color,
      not verdict-bearing — hence low, but it is the same checkable-absolute class
      that r1-F2 taught at high severity in a load-bearing position.
    recommendation: |
      Move the one-idea attribution from the figures to the claims (narrower claim,
      per fix priority): for example "It carries 23 claims, three of them
      independent, across 16 figures, and every claim pursues one idea: how the
      chips of an AI cluster should be wired to each other." No hedge needed; the
      claims-level statement is verified.
    quote: "It carries 23 claims, three of them independent, over 16 figures of one idea: how the chips of an AI cluster should be wired to each other."

  # ------------------------------------------------ NO-FINDINGS PASSES ----

  - pass: pass-1-voice-anti-ai
    finding: "no findings"
    scoped_to: |
      1B mechanical grep re-run by this reviewer on publication.md: full Tier-1
      banned list + govuk swaps + co-occurrence set (delve/leverage/crucial/
      enhance/robust/seamless/landscape/utilize/facilitate/commence/realm/
      game-changer, sentence-initial Additionally/Moreover/Furthermore, "worth
      noting", "In summary/In conclusion", represents-a/serves-as/stands-as/
      constitutes): zero hits outside verbatim quotes. Banned patterns: no
      not-just-X-but-Y, no despite-challenges, no vague attribution ("an informed
      reader should press" frames the steelman's strength, not an appeal to
      experts), no puffery, no section summaries, no elegant variation (Etched /
      "the company" and patent/filing/grant alternation is role-consistent).
      Formatting: exactly one bold span (§6 inline-bold thesis anchor — the
      sanctioned device), bullets only in Sources, no emoji, no ALL-CAPS beyond
      acronyms/part numbers, em-dash 0, en-dash 0, exclamation 0; one semicolon,
      inside the thread's quoted slogan (exempt). 1A cadence: paragraph bands
      recounted — all body paragraphs 3-7 sentences except the two sanctioned
      1-sentence beats (the §4 FIG.-pointer transition line, pre-dating round 1,
      and the §6 bold anchor); colon-pivot density recounted post-r1-F9 (~11 true
      pivots / ~1,700 words, max one non-quotation pivot per paragraph except §6
      ¶2's accepted list-colon + keeper pair); fragments ("Out of stealth after
      taping out its A0 silicon.", "Described, never claimed.") are deliberate
      cadence under the false-positive guard.

  - pass: pass-2-redundancy
    finding: "no findings"
    scoped_to: |
      2A census recounted from scratch: hop bound [0387] appears 4x in the
      sanctioned lead-setup / §3-primary (verbatim quote) / §6-single-carry
      ("A hop bound is, and claim 1 sets one") / §7-recap pattern — the r1-F8
      same-paragraph double remains fixed; [0386] rides the same 4-section pattern
      plus the header caption (caption is figure-reading, not claim restatement);
      [0124] spent exactly twice (§3 primary quote + §7 recap — the
      citation-priority map sanctions exactly this); [0168] three uses each doing
      distinct work (statement + counterfactual §4, fence arithmetic §6, recap §7);
      16-vs-28, p=4.35235/q=1.83809, $1B/$800m, "inside nine months", 12,288-class
      numbers each spent once; 4x-MLP twice on distinct anchors ([0258] compute,
      [0313] elements/bandwidth) doing different work. 2B: tightening candidates
      re-scanned — no "in order to"/filler-phrase hits; "actually" once,
      load-bearing (claims-vs-built distinction); "in effect" once, labeling
      analysis; the 37w survivors are claim-clause exempt. 2C: no paragraph
      exceeds 7 sentences (maxima at §3 ¶5, §4 ¶5, §5 ¶1, §7 ¶1 = 7); >150w
      single-idea: §3 ¶5 only (160w, two integrated verbatim quotes + derived-count
      disclosure — posture-lens quote-integrated demotion applies; standing
      noted-no-action from rounds 1-2 accepted on my own re-read: the paragraph is
      one arc, hop-cost → wire-count → stated payoff, and the [0124] quote must
      stay adjacent to the count it pays off).

  - pass: pass-3-fact-paraphrase
    finding: "no findings beyond r3-F1/F2/F3 and carried r2-F1/F2/F3"
    scoped_to: |
      Every double-quoted patent span byte-compared against input/patent.md by this
      reviewer: [0021], [0026], [0032]-derived paraphrase, [0386] blockquote,
      [0387], [0124], [0140] blockquote (incl. " 730 ." spacing), [0168], [0061],
      [0251], [0313], [0278] blockquote (incl. " 905 ." spacing), [0267], [0119],
      [0385] "two or more" — zero mutations. [0386]/[0387] re-confirmed verbatim
      inside granted claim 1 (blockquote attribution "claim 1, [0386]" correct).
      Claims-1-23 vocabulary sweeps re-run mechanically on the claims text: zero
      "memory", zero "latency", zero "AI/transformer/inference", bandwidth only as
      claim 5's equality — so §1's "None of its claims mention latency, a bandwidth
      magnitude, or memory", §5's "AI, transformers, and inference are absent from
      the claim language", and §6's claims-level absolutes all hold, including over
      the dependent claims (16/17/19/20/21) the Claim scope map does not row-list
      (checked directly: parallel-processing and channel-count limitations only).
      Claim-scope traps re-verified against the claims text: 1/14 four-or-more per
      set; 18 two-or-more + two-groups-per-set + dual-family exclusivity WITHOUT
      simultaneity (claim 9's limitation, correctly not attributed to 18); claim 11
      reduction-first/gather-second stated to claim order while gather-on-730 /
      reduction-on-740 is labeled the description's worked example [0140]; eight
      devices kept as FIG. 7 example ("the drawings' eight-chip example") with
      claim 13 nowhere upgraded; 16-vs-28 flagged as figure arithmetic in body and
      footnote; link technologies kept description options [0134]; separate dies
      and memory attachment kept permissive [0133]. Reduction/gather glosses
      verified against [0037] (sub-results shared and combined) and [0039] (data
      copied between devices). Figure record inspected directly: fig-07C.png (710a
      right = a1/a3/a5/a7, 710b left = a0/a2/a4/a6, 16 cross-set channels, none
      intra-column, families overlaid — header caption accurate, lowercase labels
      match the drawing), fig-07A.png (730: 712a↔712c, 712b↔712d — caption
      accurate), fig-07B.png (740 criss-cross: 712a↔712d, 712b↔712c — caption
      accurate), fig-06.png (host 602 / system 610 / 620a-620b / memory 630 box;
      caption uses the spec's text label per the handoff instruction), fig-09A.png
      (matches §5 and caption). External facts: every company number ($1B+, $800m,
      half-voltage, A0 tapeout, summer-2026 racks) carries company's-own-account /
      "the company says" attribution per fact-check-log discipline; thread quotes
      match the essay-context transcription; trio metadata (903 May-2025, 262
      same-day, PCT WO-2026 trio, 2026 continuations, October-2044 term) matches
      the tier-2 WIPS rows; "inside nine months" arithmetic re-verified (266 days);
      the 18-month unpublished-window statement is essay-context-sanctioned and
      stated once; no tier-4/5 anchor anywhere. Deliberately not flagged after
      examination: "balloons as the group grows" (arithmetic gloss of [0130]'s
      mesh contrast; quadratic pair-count is common knowledge and the specific
      16-vs-28 instance is disclosed as derived); "the ordinary buses commodity
      hardware already uses" (fair common-knowledge gloss of PCIe/ethernet);
      "a memory 630 whose role is to provide..." (the memory packages FORM memory
      630 per [0119]; attribution accurate).

  - pass: pass-4-logic-causality
    finding: "no findings"
    scoped_to: |
      4A: draft checked section-by-section against thesis-spine's spine→section
      trace — all seven sections carry their assigned elements on their assigned
      anchors; no out-of-spine section-level claim found; the four axes all land
      (claims [0386]/[0387]; problem [0026]/[0313]; effect [0124]/[0130]/[0168];
      baseline switch-vs-mesh foils + narrative friction). 4B causal sweep: "the
      split creates the real problem" (mechanism given, [0036]); "The families
      exist so two kinds of traffic never share a wire" (purpose carried by claims
      8/11 + [0140]); "Disjoint lanes make simultaneity cheap" (mechanism, claim 9
      + [0142]); "the equal traffic follows from the split the description
      prescribes" (conditionality preserved post-r1-F5, [0168]'s own
      counterfactual); "That is the filing pattern of a company fencing an
      architecture" (pattern-reading scoped to the pattern, on tier-2 facts,
      essay-context-sanctioned; confounders not required at this scoping);
      twelve-months-before stated as chronology, not cause; "Etched has, in
      effect, published the diagram" labeled analysis. 4C: lead tension (checkable
      split) → mechanism (§3-4) → aim (§5) → boundary (§6) → firm two-way verdict +
      closing-binary-test — arc closes on the lead's frame; residual-risk
      handling matches the spine (Acknowledged → binary test under firm, not
      open-question).

  - pass: pass-5-reader-perspective
    finding: "no findings"
    scoped_to: |
      Jargon budget audited term-by-term: tensor ("grids of numbers AI models
      multiply"), reduction, gather, systolic array ("grid of small processing
      elements that computes as data flows through it"), K4,4 (one labeled aside),
      MLP ("multi-layer perceptron block that follows attention"), HBM/SRAM
      ("stacked high-bandwidth memory paired with on-chip SRAM"), PCT ("extends
      each abroad"), continuation ("keeps each open at home") — all one-clause
      glossed on first use. Two borderline terms examined and accepted, consistent
      with (but re-judged independently of) round 2: "scale-up domain" enters
      inside the thread's verbatim quote and its §7 bare use is defined in
      apposition by the very next clause ("the wiring either matches claim 1's
      cross-set pattern [0386] or it does not") plus the Phase-1 audience note
      that the reader arrives from the thread holding CSM vocabulary; "apparatus
      claim" appears once, inside a sentence that IS its functional gloss
      ("Structure is what an apparatus claim can lock"). Numbers on familiar
      scales: 16-vs-28 wires, "inside nine months", 4-of-8-chips reading attached
      to the p/q decimals, $1B-vs-$800m plain. 5C mobile recount (words/12): >8-line
      paragraphs are §3 ¶1 (107w), §3 ¶5 (160w), §4 ¶5 (136w), §5 ¶1 (117w), §5 ¶2
      (97w), §6 ¶1 (128w) — every one a quote-integrated structure demoted per the
      posture-lens heuristic; §7 ¶1 (103w, ~8.6 lines, no integrated quote) carries
      rounds-1/2's noted-no-action ruling, accepted on my own read (it is the
      verdict paragraph; a split would fragment the call, and it is 6 tight
      sentences). Engagement: stake resurfaces §3 ¶2 ("a switch or a wire per
      pair... with neither"), §4 ¶1 ("stops being textbook"), §5 ¶1 ("None of this
      is claimed for AI"), §5 close ("It does not claim the store"); money thread
      feeds the verdict at §2 (commitment signal), §6 (the one caution), §7
      (binary test). Closing paragraph read in isolation: self-sufficient;
      bookending intact.

  - pass: pass-6-lead-conclusion-format
    finding: "no findings"
    scoped_to: |
      6A: sentence 1 news event, sentence 2 declarative half-verdict, sentence 3
      the other half — thesis + patent + stake inside three sentences. 6B: frame
      closure verified ("The thread sells a memory story. The granted record holds
      a wiring story."); Acknowledged residual under declared firm maps to the
      delivered closing-binary-test (summer-2026 racks → wiring matches claim 1 or
      it does not), not an open question. 6C: # Sources exactly once; categories
      Patents + Official statements (both in the 5-enum); 4 entries across 2
      categories → subgrouped, all-or-nothing satisfied. 6D: no Papers — n/a.
      6E re-run mechanically this round: em-dash 0 outside quotes; every inline
      cite 4-digit and Phase-1-resolvable; footnotes absent from publication.md;
      banned grep clean; # Sources once. 6F: title has no em-dash and no
      separator; Title Case consistent across all headers. 6G at full strength in
      BOTH directions under closing_posture: firm — the verdict leads with the
      call ("Hold the thread against the grant and the verdict is firm both
      ways"), no qualifier-led opening, zero safe-harbor boilerplate (no "patents
      don't guarantee", no "time will tell", no "remains to be seen"), exactly ONE
      patent-specific anti-hype guard (LVI/HBM-SRAM absence + the 18-month window,
      §6, stated once, flagged in-text as "the one caution the verdict carries"),
      limits REFERENCED from §7 ("The boundaries set out above scope that call.
      They do not soften it.") rather than re-listed; and no over-firm inversion:
      §7's recap clauses each trace to established anchors ([0387], [0142],
      [0168], [0124], [0386]), "it holds" is scoped by its own sentence to "the
      one you can check today" (granted substance, not product practice), and
      rack-practice is reserved for the binary test. gate_hedge PASS is consistent
      with this reading; "The claims cannot say what Etched actually built. The
      racks can." is the sanctioned binary-test setup, not a truism close.

  - pass: pass-7-adversarial-reader
    finding: "no findings"
    scoped_to: |
      1 BLUF: ¶1 sentence 2 is a declarative verdict — "Half of the loudest
      architecture claim in the thread already has a granted US patent standing
      behind it." — no deferred question. 2 Header-as-claim: all seven ## headers
      assert; the header-only skim reconstructs the argument (checkable half →
      structure patent being extended → switchless any-to-any → wiring schedules
      traffic → aimed at transformer decoding → no latency number, no memory claim
      → one leg substantiated, one absent). 3 Steelman: present, THIS-patent,
      full-strength ("Claim 1 recites a wiring pattern and nothing else... PCIe,
      SPI, ethernet, UCIe [0134]... A topology-only claim over standard link
      technologies is a thin moat"), then refined without un-conceding (structure
      is what the claim locks; the claims-8/9/11 binding is the non-generic part;
      hop bound claimable where the adjective is not); no generic patent truism
      appears as steelman or close. Also pressure-tested: the "K4,4 is textbook"
      objection is pre-empted (the essay never rests novelty on the bare shape —
      "where the shape stops being textbook" hands novelty to the channel-family
      binding); the fast-grant/no-citations angle is not adjudicated by the essay
      and nothing in the text leans on examination quality. 4 Meta: no
      reader-instruction / essay-self-reference; "The objection an informed reader
      should press" frames the objection, "The boundaries set out above" is the
      6G-sanctioned reference-not-relist; footnote provenance notes are functional.
      5 Jargon as signpost: no doctrinal deep-dive anywhere; p/q decimals spent
      once with the practical reading attached. 6 Stub/rhythm: section word-counts
      recounted — §7 (~190w) and §2 (~200w) are the short sections, both
      multi-paragraph and complete; no stub. 7 Thesis restatement census
      (recounted independently): the FULL two-sided verdict is asserted in §1 ¶1
      and §7; §5's closing pair ("claims the movement pattern... does not claim
      the store") is the honest-kernel beat's local landing and §6's topic
      sentences are leg-scoped boundary evidence in the designated limits section
      — strict census ≤ 3 sections even counting §5. Impatient-investor read:
      answer in ¶1, company numbers by ¶2, no unglossed blocker, money thread
      never drops for more than one section. Skeptical-pro read: the strongest
      objection is the one the essay itself presses hardest, and its rebuttal
      stands on claim text and the patent's own arithmetic.

# ==================================================================
# PART 3 — OVERALL
# ==================================================================

severity_census:
  critical: 0
  high: 0
  medium: 0
  low: 6   # carried r2-F1, r2-F2, r2-F3 (still open by design) + new r3-F1, r3-F2, r3-F3
```

**Overall assessment: pass** — independent full re-review of the unchanged draft_version 2
confirms round 2's clean verdict rather than inheriting it: every verbatim span, claims-level
absolute, claim-scope statement, figure caption, and external-fact attribution was re-verified
against the patent, the figures, and the design bundle from scratch, and the fresh sweep
surfaces only three new low-severity anchor-precision/wording items (r3-F1/F2/F3, two of them
the same citation-compression class as the carried r2-F1/F2), none medium+, none touching the
verdict, the steelman, the figure record, or any hard-gate dimension. The three carried round-2
lows remain open-by-design and, with the three new lows, are available to the composer as
optional pre-publication polish. This is the SECOND consecutive clean round from an independent
reviewer: double-clean acceptance is satisfied from this reviewer's side.

## Finding-id lifecycle (round-2 carried ids)

One ruling line per finding_id appearing in round 2's edit-log, recorded from this
round's own verification of draft_version 2 (RUN-004 id-continuity; no re-litigation).

- r1-F1: verified-standing in v2 draft: lead uses halves-of-CSM vocabulary; "pillar" reserved for LVI/CSM.
- r1-F2: verified-standing in v2 draft: memory-scenery narrowing with [0119]/[0133] absorbed; FIG. 6 caption absolute gone.
- r1-F3: verified-standing in v2 draft: fence scoped to "the patent's own cluster-scale arithmetic" [0168], [0061].
- r1-F4: verified-standing in v2 draft: "adjective was never claimable as such; a hop bound is [0387]".
- r1-F5: verified-standing in v2 draft: equal channels wired in; equal traffic follows the prescribed split [0168].
- r1-F6: verified-standing in v2 draft: binary test is match/no-match against claim 1's pattern [0386].
- r1-F7: verified-standing in v2 draft: §1 internal verdict double absent; ¶4 ends on the claims-absence sentence.
- r1-F8: verified-standing in v2 draft: [0387] census = lead/§3-primary/§6-single-carry/§7-recap; fence list has three elements.
- r1-F9: verified-standing in v2 draft: ~11 true colon pivots per ~1,700 words; accepted keeper deviation intact.
- r1-F10: verified-standing in v2 draft: §2 and §6 splits present; no >8-line non-quote-integrated paragraph beyond the noted-no-action verdict paragraph.
- r1-F11: verified-standing in v2 draft: "PCT ... extends each abroad" / "US continuation ... keeps each open at home".
- r1-F12: verified-standing in v2 draft: "inside nine months" carried; 266-day computation re-verified and footnoted.
- r1-F13: verified-standing in v2 draft: header caption anchors [0128], [0129] with [0125] on the overlay sentence; figure-checked.
- r1-F14: verified-standing in v2 draft: decoding handoff on [0259]; layer list on [0252] (adjacent new residual filed as r3-F1, not a regression).
- r1-F15: verified-standing in v2 draft: "[0168], [0178]" pairing present; [0178] re-read against patent.md.
- r1-F16: verified-standing in v2 draft: "and precision matters here" stage direction absent from §5 landing.
- r1-F17: verified-standing in v2 draft: "need not even hold ... may begin forwarding" modality intact per [0143].
- r2-F1: still-open-low at round 3 by design (confirmation round takes no revision); carried to self-audit.
- r2-F2: still-open-low at round 3 by design (confirmation round takes no revision); carried to self-audit.
- r2-F3: still-open-low at round 3 by design (confirmation round takes no revision); carried to self-audit.
