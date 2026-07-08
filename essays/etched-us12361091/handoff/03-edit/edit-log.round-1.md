# Edit Log — Round 1

```yaml
review_id: etched-us12361091-editorial-review-1
draft_source: handoff/02-compose/essay-draft.md
publication_strip: handoff/02-compose/publication.md
review_timestamp: 2026-07-02T21:05:00Z
posture_applied: measured
closing_posture_declared: firm
overall_assessment: revise-required
round: 1
carried_findings: none (round 1 — no prior round; re-review protocol n/a)

gate_context: >
  gate-result.round-1.json: all 13 gates PASS. Warns: 1x STRUCT-004 (two triads),
  9x LONGSENT-001. LONGSENT sample VERIFIED rather than trusted: the 44w / 54w /
  137w / 109w / 43w hits are parser merge artifacts at heading/caption/footnote
  boundaries (headings and caption markers lack terminal punctuation, so the
  splitter concatenates across them); the remaining 37-40w hits are real sentences
  but are quote-integrated or claim-enumeration sentences permitted by
  deliverable-voice-rules ("a necessary causal or claim clause may run longer").
  The composer's footnote attribution is accurate. Both STRUCT-004 triads
  ("methods, topology, and AI-model computation"; "normalization, then
  self-attention..., then projection, then an MLP") are content-bearing factual
  enumerations, not reflexive rule-of-three.

findings:

  # ---------------------------------------------------------------- HIGH ----

  - finding_id: r1-F1
    pass: pass-4-logic-causality
    location: "§1 'The Memory Story Has a Checkable Half', paragraph 1, sentences 2-3 (cross-ref pass-6 6A)"
    severity: high
    severity_under_default_posture: high
    finding: |
      The lead's BLUF mis-scopes the verdict and contradicts the essay's own
      pillar definition two paragraphs later. Paragraph 1: "One of the thread's
      two architecture pillars already has a granted US patent standing behind
      it. The other pillar, the shared memory pool that gives Cluster-Scale
      Memory its name..." — here the "two pillars" are the interconnect and the
      memory pool (the two legs OF CSM). Paragraph 3 then defines the thread's
      two pillars as LVI and CSM ("The architecture case rests on two pillars.
      Low-Voltage Inference is the power half. Cluster-Scale Memory... is the
      half that pulled readers in."), and §6 uses "The thread's other pillar"
      correctly for LVI. Read with paragraph 3's definition, paragraph 1 claims
      a FULL pillar (CSM) has a granted patent standing behind it — but the
      spine, the title ("the Wiring Half of Its Memory Story"), and §7's verdict
      all say the patent substantiates only the interconnect LEG of CSM. The
      essay's most prominent claim overstates its own conclusion and forces a
      re-parse at paragraph 3.
    recommendation: |
      Recast paragraph 1 in halves-of-the-memory-claim vocabulary and reserve
      "pillar" for LVI/CSM (as §6 already does). For example: "Half of the
      loudest architecture claim in the thread already has a granted US patent
      standing behind it. The other half, the shared pool that gives
      Cluster-Scale Memory its name, has no granted substance in the filings
      you can read today." Keeps the declarative BLUF and the firm split; fixes
      the scope.
    quote: "One of the thread's two architecture pillars already has a granted US patent standing behind it."

  - finding_id: r1-F2
    pass: pass-3-fact-paraphrase
    location: "§6 'No Latency Number, No Memory Claim', paragraph 3, sentence 2"
    severity: high
    severity_under_default_posture: high
    finding: |
      "The only memory in the patent is a labeled rectangle: FIG. 6 shows... a
      memory 630" is a checkable absolute about the document that the document
      contradicts. Memory appears in the description beyond box 630: [0133]
      (cited by the draft in this very section for the dies point) says each
      chip "may be coupled to one or more memory devices that are shared or are
      not shared among the processing devices A0-A7" — the spec's closest
      textual approach to a shared-memory idea; the Examples families recite
      "one or more memory devices configured to store a plurality of tensors"
      ([0373], [0432]); FIG. 13 shows memory 1312 (boilerplate). A skeptical
      reader with the patent open finds [0133] in minutes, and the essay's
      credibility rests on exactly this kind of claim-text precision. The
      CLAIMS-level absolute remains true (no granted claim recites memory —
      verified against claims 1-23) and fully carries the verdict.
    recommendation: |
      Narrow the absolute to where it is true, per fix priority (narrower
      claim, better anchor). Options: (a) "Memory appears nowhere in the
      claims. In the description it is scenery: a box 630 feeding the groups
      [0119], and optional per-chip memory devices, 'shared or... not shared'
      [0133] — described, never claimed." — explicitly absorbing [0133]
      strengthens the steelman handling rather than softening the verdict; or
      (b) scope the sentence to the system drawings: "the only memory the
      invention's own architecture drawing gives a role is a labeled
      rectangle". Do NOT hedge the memory-leg verdict itself; it is correct.
    quote: "The only memory in the patent is a labeled rectangle: FIG. 6 shows a host, two tensor parallel groups, and a memory 630"

  - finding_id: r1-F3
    pass: pass-3-fact-paraphrase
    location: "§6 'No Latency Number, No Memory Claim', paragraph 2 (refine beat), sentence 3 (cross-ref pass-4 4B: necessity overstated)"
    severity: high
    severity_under_default_posture: high
    finding: |
      "...the balanced-channel arithmetic the description builds on it [0168],
      [0061] is the wiring discipline any cluster-scale memory story would have
      to run on" introduces a necessity claim the anchors do not carry.
      [0168]/[0061] support that THIS design's balance comes from the split
      arithmetic; they say nothing about what any cluster-scale memory story
      requires. The essay's own §3 concedes that switched fabrics deliver
      any-to-any sharing ([0032]) — that is, a memory-pool story can run on a
      switch — so the sentence also contradicts the essay's own foil framing,
      and it partially un-concedes the steelman ("thin moat") granted one
      paragraph earlier by implying every CSM implementation needs what this
      patent fences. Spine's mitigation states the defensible version: the
      fence "is exactly the wiring discipline ITS CSM math needs".
    recommendation: |
      Narrow the claim to the patent's own story (spine wording), keeping the
      firmness: "...is the wiring discipline the patent's own cluster-scale
      arithmetic runs on [0061], [0168]" or "...the wiring discipline Etched's
      described CSM math needs". No hedge; just scope the necessity to this
      design.
    quote: "the wiring discipline any cluster-scale memory story would have to run on"

  # -------------------------------------------------------------- MEDIUM ----

  - finding_id: r1-F4
    pass: pass-3-fact-paraphrase
    location: "§6 'No Latency Number, No Memory Claim', paragraph 2, sentences 4-5"
    severity: medium
    severity_under_default_posture: medium
    finding: |
      "A latency figure was never going to sit in an apparatus claim." is a
      categorical statement about patent practice that is false in general —
      apparatus claims can and do recite quantitative functional limitations
      (e.g. "configured to respond within X ns"). The spine's version was
      narrower and correct: "the latency ADJECTIVE was never claimable as
      such". The composer's adjective→figure swap turned a defensible point
      into a contestable generalization inside the essay's key rebuttal; a
      patent-literate reader dings it. The follow-on "A hop bound can, and it
      does" is fine.
    recommendation: |
      Restore the spine's narrower claim or tie the impossibility to THIS
      claim set: for example "The thread's adjective was never claimable as
      such, and a latency number would have needed a claimed link technology
      to bind — the claims leave that open [0134]. A hop bound needs neither,
      and claim 1 sets one [0387]."
    quote: "A latency figure was never going to sit in an apparatus claim. A hop bound can, and it does"

  - finding_id: r1-F5
    pass: pass-4-logic-causality
    location: "§4 'The Wiring Schedules the Traffic', final paragraph, last two sentences"
    severity: medium
    severity_under_default_posture: medium
    finding: |
      "No link runs hot, and nothing about that depends on scheduling
      software. It is wired in." overstates what the structure locks. The
      paragraph's own first sentence says the balance comes from tensors being
      "pre-cut", and [0168] explicitly conditions the property: "had the first
      and second tensors been split in unequal tiles, different amounts of
      data may be shared". What is wired in is channel-count/bandwidth
      UNIFORMITY (claims 3-5); the equal traffic additionally requires the
      equal split the description prescribes. The punchline claims
      software-independence that the anchor's own counterfactual denies.
    recommendation: |
      Narrow the punchline to what structure locks vs what the split supplies:
      for example "No link runs hot. The equal channels are wired in (claims 3
      to 5); the equal traffic follows from the split the description
      prescribes [0168]." Keeps the beat, drops the overclaim.
    quote: "No link runs hot, and nothing about that depends on scheduling software. It is wired in."

  - finding_id: r1-F6
    pass: pass-4-logic-causality
    location: "§7 'One Leg Substantiated, One Leg Absent', paragraph 2, sentence 4"
    severity: medium
    severity_under_default_posture: medium
    finding: |
      The closing binary test presents an excluded middle: "either the chips
      hang off a switch fabric, or they are wired chip to chip in claim 1's
      cross-set pattern [0386]". The essay's own §3 named a third shape (full
      point-to-point mesh, [0130]), and other direct-wired topologies (rings,
      tori) are standard in scale-up domains. If teardowns show direct wiring
      in some non-claim-1 pattern, both stated branches are false. The
      falsifier itself is genuinely binary — the hardware either embodies
      claim 1's pattern or it does not — but the sentence as written is not.
    recommendation: |
      Recast the test as match/no-match against the claim: for example "When
      they do, the scale-up domain becomes inspectable: the wiring either
      matches claim 1's cross-set pattern [0386] or it does not." (Optionally
      keep the switch fabric as the named alternative the thread itself
      denies.) Preserves the closing-binary-test posture.
    quote: "either the chips hang off a switch fabric, or they are wired chip to chip in claim 1's cross-set pattern [0386]"

  - finding_id: r1-F7
    pass: pass-7-adversarial-reader
    location: "§1 paragraphs 1 and 4; §5 final paragraph; §6 paragraph 3; §7 paragraph 1 (finding class: thesis-restatement-redundancy)"
    severity: medium
    severity_under_default_posture: medium
    finding: |
      The core split-verdict (wiring substantiated / memory absent) is
      asserted in 4 sections — over the <=3 bar — and twice within the lead
      itself: §1 ¶1 "That split is the story..." and §1 ¶4 "Held against each
      other, the two documents split the CSM story cleanly in two."; §5 "It
      does not claim the store."; §6 "The memory half has no equivalent fence
      anywhere in the claims."; §7 "the verdict is firm both ways". §5's and
      §6's instances each do local boundary work and earn their place; the
      §1-internal double does not — ¶4's closer restates ¶1's landing without
      a new evidence layer.
    recommendation: |
      Cut or fold §1 ¶4's "Held against each other, the two documents split
      the CSM story cleanly in two." — the paragraph's preceding sentence
      ("None of its claims mention latency, a bandwidth magnitude, or
      memory.") already lands the contrast, and ¶1 owns the split statement.
    quote: "Held against each other, the two documents split the CSM story cleanly in two."

  - finding_id: r1-F8
    pass: pass-2-redundancy
    location: "§6 paragraph 2 (fence list AND 'A hop bound' sentence); also §1 ¶4, §3 ¶5, §7 ¶1"
    severity: medium
    severity_under_default_posture: medium
    finding: |
      2A claim repetition: the at-most-one-intermediate hop bound [0387] is
      stated five times across four sections — §1 ("through at most one chip
      in between"), §3 (verbatim quote + gloss, sanctioned), §6 twice
      (fence-list item "the at-most-one-intermediate guarantee [0387]" and,
      two sentences later, "A hop bound can, and it does: at most one device
      between any two chips, ever [0387]"), §7 (recap, sanctioned). Lead
      setup, §3 primary statement, and §7 recap are acceptable repetition; the
      same-paragraph double inside §6 is not — same fact, same anchor, no new
      evidence layer.
    recommendation: |
      Carry the hop bound once in §6. Cleanest: drop "the
      at-most-one-intermediate guarantee [0387]," from the fence list (the "A
      hop bound can, and it does" punchline restates it at full strength two
      sentences later), leaving the list with three elements.
    quote: "the at-most-one-intermediate guarantee [0387], ... A hop bound can, and it does: at most one device between any two chips, ever [0387]."

  - finding_id: r1-F9
    pass: pass-1-voice-anti-ai
    location: "body-wide; densest in §4 and §6 (cadence pattern, Tier-2 judgment list)"
    severity: medium
    severity_under_default_posture: medium
    finding: |
      Colon-pivot construction ("complete clause: elaboration") appears ~22
      times in ~1,700 words of body prose (excluding captions and blockquote
      lead-ins) — roughly one per 77 words, in nearly every paragraph.
      Individually each is grammatical (not the banned incomplete-clause
      form), but at this density the identical pivot rhythm becomes a
      structural fingerprint (anti-ai-writing Tier-2: announcement-colon /
      punctuation tells are cluster-flagged). Examples: "Disjoint lanes make
      simultaneity cheap: claim 9...", "Uniformity is claimed as structure
      too: each device...", "The only memory in the patent is a labeled
      rectangle: FIG. 6...", "has granted, checkable substance: a group
      wired...".
    recommendation: |
      Break up roughly a third — keep the strongest pivots (the claim-1
      lead-in, "A hop bound can, and it does:"), convert the weakest to
      periods or reshaped sentences (for example "Uniformity is claimed as
      structure too. Each device couples to..."). Target: no more than one
      colon pivot per paragraph.

  - finding_id: r1-F10
    pass: pass-5-reader-perspective
    location: "§2 paragraph 2 ('It did not file alone...', 130 words) and §6 paragraph 6 ('The thread's other pillar...', 115 words)"
    severity: medium
    severity_under_default_posture: medium
    finding: |
      5C mobile rendering: two paragraphs with no integrated verbatim quote
      exceed the 8-line mobile heuristic — §2 ¶2 at 130 words (~11 lines,
      seven sentences: trio + division of labor + PCT/continuation + term +
      fencing verdict) and §6 ¶6 at 115 words (~10 lines: LVI absence +
      cold plates + HBM/SRAM + voltage + 18-month window + close). Marginal:
      §6 ¶2 (104w) and §7 ¶1 (103w) at ~8.6 lines. The heavier §3/§4/§5
      paragraphs (158w/129w/128w) are quote-integrated structures and demote
      to low under the posture lens; noted, no action required.
    recommendation: |
      Split the two flagged paragraphs at their natural seams: §2 ¶2 after
      "...the model-level execution those moves add up to." (trio identity |
      commitment signal); §6 ¶6 after "...that the thread folds into CSM."
      (what is absent | what that absence means today).

  # ----------------------------------------------------------------- LOW ----

  - finding_id: r1-F11
    pass: pass-3-fact-paraphrase
    location: "§2 paragraph 2, sentence 6"
    severity: low
    severity_under_default_posture: low
    finding: |
      "Etched is paying to keep all three alive beyond the United States:
      each carries a PCT international filing and a US continuation published
      in 2026" files the US continuation under the beyond-US umbrella. A
      continuation is a domestic instrument (keeps prosecution open at home);
      only the PCT extends abroad. Also the reader profile asks filing-process
      terms to be functionally unpacked — the PCT gets one from "beyond the
      United States", the continuation gets a wrong one.
    recommendation: |
      Split the gloss: for example "Etched is paying to keep all three alive
      and growing: a PCT filing to extend each abroad, a US continuation to
      keep each open at home, and this one's expected term runs to October
      2044."
    quote: "keep all three alive beyond the United States: each carries a PCT international filing and a US continuation published in 2026"

  - finding_id: r1-F12
    pass: pass-5-reader-perspective
    location: "§2 paragraph 1, sentence 1"
    severity: low
    severity_under_default_posture: low
    finding: |
      "granted 15 July 2025, 266 days later" is a naked magnitude for the
      profile reader — nothing in the essay says whether 266 days is fast or
      slow, so the number does no work (Phase 1's "unusually fast" note was
      not carried, and no external pendency baseline is in the fact log to
      anchor one).
    recommendation: |
      Either translate the unit so the reader owns the scale ("granted 15
      July 2025, inside nine months" — arithmetic, same class as the flagged
      16-vs-28 count) or cut the clause. Do not add an unanchored
      "fast for the art unit" comparison; no verified baseline exists in the
      fact-check log.
    quote: "filed 22 October 2024 and granted 15 July 2025, 266 days later"

  - finding_id: r1-F13
    pass: pass-3-fact-paraphrase
    location: "header caption (FIG. 7C), sentence 3"
    severity: low
    severity_under_default_posture: low
    finding: |
      Anchor precision: the caption anchors "Every chip in one column is
      wired straight to every chip in the other, 16 channels in all, and no
      wire runs inside a column" to [0125], but [0125] only says FIG. 7C
      shows all connections in a single figure. The no-wires-within-a-set
      fact is [0128]; the every-cross-pair fact is [0129]; 16 is figure
      arithmetic (flagged as derived in the body, and the caption content is
      verified accurate against fig-07C.png, including 710a right / 710b
      left and the drawing's lowercase a0-a7 labels).
    recommendation: |
      Re-anchor the sentence to [0128] (or [0128]-[0129]); keep [0125] for
      the "both families overlaid in one drawing" sentence if desired.
    quote: "no wire runs inside a column [0125]"

  - finding_id: r1-F14
    pass: pass-3-fact-paraphrase
    location: "§5 paragraph 1, final sentence"
    severity: low
    severity_under_default_posture: low
    finding: |
      "Its decoding layers... run normalization, then self-attention...,
      then projection, then an MLP, and finally decoding [0252]" — [0252]
      lists the decoding layers 905 as normalization, self-attention,
      projection, MLP; the decoding (token-selection) block 930 sits OUTSIDE
      the 905 loop in FIG. 9A and is described at [0259]. Attributing
      "finally decoding" to what the decoding layers "run", on the [0252]
      anchor, is a small structural inaccuracy.
    recommendation: |
      Either "...then an MLP [0252], then hand off to decoding, the token
      pick [0259]" or drop "and finally decoding" (FIG. 9A's caption already
      shows the flow).
    quote: "run normalization, then self-attention (QKV generation and attention computation), then projection, then an MLP, and finally decoding [0252]"

  - finding_id: r1-F15
    pass: pass-3-fact-paraphrase
    location: "§4 final paragraph, sentence 2"
    severity: low
    severity_under_default_posture: low
    finding: |
      "...and the same amount crosses each channel [0168]" generalizes to
      both channel families on an anchor that covers only the second family
      ([0168]: "a same amount of data may be shared across each of the
      second communication channels 740"). The generalization is TRUE — the
      first family's mirror statement is [0178] — but the single anchor
      under-covers the claim as written.
    recommendation: |
      Cite both: "...and the same amount crosses each channel [0168],
      [0178]." ([0178] is in the Phase-1 anchor set.)
    quote: "and the same amount crosses each channel [0168]"

  - finding_id: r1-F16
    pass: pass-7-adversarial-reader
    location: "§5 final paragraph, sentence 2 (finding class: meta-reader-instruction, borderline)"
    severity: low
    severity_under_default_posture: low
    finding: |
      "This is the closest the filing comes to the thread's memory idea, and
      precision matters here." — the second clause is the essay narrating its
      own carefulness (self-reference-lite). Not gated (META-001 exempts
      functional framing) and the first clause is doing real work; the
      "precision matters here" aside is stage direction the following two
      sentences make redundant.
    recommendation: |
      Cut "and precision matters here" — the store/movement distinction that
      follows IS the precision.
    quote: "This is the closest the filing comes to the thread's memory idea, and precision matters here."

  - finding_id: r1-F17
    pass: pass-3-fact-paraphrase
    location: "§3 paragraph 5, sentence 4"
    severity: low
    severity_under_default_posture: low
    finding: |
      "The relay does not even hold the message" states as definite what
      [0143] frames as an optional embodiment capability ("may also be
      configured to transmit a portion of data to be received before all
      data is received"); cut-through forwarding is not claimed anywhere.
      The modality survives in the since-clause ("may begin forwarding"), so
      meaning is partially preserved, but the lead clause upgrades an option
      to a property — the option→lock drift class the handoff notes fence.
    recommendation: |
      "The relay need not even hold the message: an intermediate chip may
      begin forwarding data before it has finished receiving it [0143]."
    quote: "The relay does not even hold the message, since an intermediate chip may begin forwarding data before it has finished receiving it [0143]."

  # ------------------------------------------------ NO-FINDINGS PASSES ----

  - pass: pass-6-lead-conclusion-format
    finding: "no findings"
    scoped_to: |
      6A: lead's first three sentences anchor thesis + patent + stake (the ¶1
      scope defect is filed as r1-F1 under pass-4; the BLUF structure itself
      passes). 6B: frame closure verified — corporate-narrative-friction lead
      returns in §7 ("The thread sells a memory story. The granted record
      holds a wiring story."); residual_risk 'Acknowledged' under declared
      firm posture maps to closing-binary-test, and §7 delivers one
      (summer-2026 racks → topology inspectable), not an open-question close.
      6C: # Sources present exactly once; 2 categories (Patents, Official
      statements), both in the 5-enum; 4 entries across 2 categories →
      subgrouping required and all-or-nothing satisfied. 6D: no Papers
      category — n/a. 6E: em-dash count 0 outside quotes; all inline cites
      4-digit [dddd] and present in the Phase-1 anchor set (gate_anchors /
      gate_quotes PASS independently confirmed on spot-checks: [0386]/[0387]
      verbatim in claim 1; [0140] and [0278] blockquotes byte-identical
      including the " 730 ." / " 905 ." spacing quirks; [0021], [0026],
      [0061], [0119], [0124], [0251], [0267], [0313]-subspans verbatim);
      footnotes stripped from publication.md; banned-words grep clean.
      6F: title uses no em-dash and no separator. 6G checked in BOTH
      directions at full strength under closing_posture: firm — the verdict
      leads with the call ("Hold the thread against the grant and the verdict
      is firm both ways"), no qualifier-led verdict, no safe-harbor
      boilerplate ("patents don't guarantee...", "time will tell" absent),
      exactly one patent-specific anti-hype guard (LVI/HBM-SRAM absence with
      the 18-month window, stated once in §6), limits REFERENCED from §7
      ("The boundaries set out above scope that call. They do not soften
      it.") not re-listed, and no over-firm inversion in §7 itself — the
      verdict's confidence is proportionate to the body (the §6-body
      overreach instances are filed under r1-F2/F3/F4, not verdict-section
      defects). gate_hedge PASS is consistent with this reading.

pass_scope_notes: |
  pass-1 (scope beyond r1-F9): banned-word grep re-run clean on
  publication.md (delve/leverage/crucial/landscape/etc. zero hits); no
  banned rhetorical patterns (no not-just-X-but-Y, no copula avoidance
  outside verbatim quotes, no vague attribution, no puffery, no section
  summaries, no elegant variation — Etched/"the company" and patent/filing/
  grant variation is register-normal); banned formatting clean (exactly one
  bold span = the sanctioned §6 thesis anchor; bullets only in Sources; no
  emoji; no ALL-CAPS beyond acronyms/part numbers); semicolons in body
  prose: zero (the one semicolon lives inside the thread's verbatim quote);
  fragments ("It is wired in.", "Reduce and gather stop taking turns.") read
  as deliberate cadence, protected by the false-positive guard.
  pass-2 (scope beyond r1-F8): claim-repetition sweep on all numeric values
  (16/28 stated once + one footnote; p=4.35235 spent once; $1B/$800m once;
  266 days once; 4x MLP twice with distinct anchors [0258]/[0313] doing
  different work — accepted); 2B tightening candidates limited to the
  33-word "The patent's own stated wins..." contrast sentence (kept:
  claim-logic clause exemption); 2C: no paragraph exceeds 7 sentences
  (max 7 at §2 ¶2, §6 ¶6, §7 ¶1); >150-word single-idea: only §3 ¶5 (158w,
  quote-integrated, demoted per posture lens — split optionally with
  r1-F10's mobile work).
  pass-3 (scope beyond findings): every [dddd] anchor in the draft exists in
  invention-summary.md quotable spans / quote-anchor table / anchored
  sections; all verbatim quoted spans byte-checked against patent.md (see
  6G scope list) — zero mutations found; claim-scope traps verified
  respected: claims 1/14 stated four-or-more per set, claim 18 two-or-more
  with the four-group dual-family structure and WITHOUT simultaneity
  attributed, [0385] "two or more" used only as the labeled narrowing
  exhibit in §6, eight devices / 4 links per chip / 16-vs-28 presented as
  worked example + derived arithmetic, link technologies kept as
  description options, bandwidth equality (claim 5) never upgraded to
  magnitude, gather-on-730/reduction-on-740 labeled as the description's
  example while claim 11's reduction/gather lock is stated without family
  mapping; external facts: all company numbers carry the-company-says
  attribution; thread quotes match input/essay-context.md transcription
  verbatim; trio metadata matches fact-check-log (903 May-2025 grant, 262
  same-day grant, 2044 expiry); 266-day computation verified correct; the
  18-month unpublished-window statement is essay-context-sanctioned and
  accurately phrased; no tier-4/5 anchors used anywhere.
  pass-4 (scope beyond findings): thesis-trace section mapping verified
  against thesis-spine spine→section trace — all seven sections carry their
  assigned elements, all four axes land, no out-of-spine section-level
  claims beyond the flagged sentences; causal-chain sweep: §2's "filing
  pattern of a company fencing an architecture" is evidence-proportionate
  pattern-reading on tier-2 facts; no correlation→causation drift in the
  twelve-months-before chronology (stated as sequence, not cause); §7's
  "in effect, published the diagram" is labeled analysis.
  pass-5 (scope beyond r1-F10/F12): jargon budget verified — tensor,
  reduction, gather, systolic array, K4,4, MLP, HBM/SRAM all get one-clause
  glosses on first use; no prerequisite chains (each section re-grounds its
  vocabulary); engagement curve holds (stake resurfaces at §3 ¶2 "a switch
  or a wire per pair", §4 ¶1 "stops being textbook", §5 ¶1 "None of this is
  claimed for AI", §5 close ties to the verdict); §4 ¶1's reference-number
  density (712a-d/730/740) accepted because FIGS. 7A/7B captions sit
  adjacent and repeat the pairings; closing readable in isolation
  (bookending intact).
  pass-7 (scope beyond r1-F7/F16): BLUF present (¶1 declarative verdict —
  scope defect filed as r1-F1); all seven ## headers are claims and a
  header-only skim reconstructs the argument; steelman PRESENT and
  THIS-patent-specific (§6 ¶1: topology-only claim over standard links
  [0134], no latency figure, no memory limitation — conceded at full
  strength, then refined without generic patent truisms); no
  reader-instruction meta beyond the flagged borderline clause; jargon kept
  as signposts (no doctrinal deep-dives); no stub sections (§2 192w / §7
  194w are the two short sections, both multi-paragraph and
  content-complete; verdict sections run short by design); impatient-investor
  read: the answer arrives in ¶1 and the money thread never drops for more
  than one section; skeptical-pro read: the strongest objection is the one
  the essay presses, and after r1-F2/F3 corrections its rebuttal stands on
  claim text alone.
```

**Overall assessment: revise-required** — three high findings: the lead's pillar framing overstates the verdict's scope against the essay's own definitions (r1-F1), and two §6 grounding overreaches assert checkable absolutes the patent text contradicts or exceeds (r1-F2 "only memory in the patent", r1-F3 "any cluster-scale memory story"); all three have narrow, firmness-preserving fixes, and the verdict section itself is clean under 6G in both directions.
