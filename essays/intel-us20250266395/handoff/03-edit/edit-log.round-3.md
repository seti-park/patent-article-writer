# Edit Log — Round 3

```yaml
review_id: intel-us20250266395-editorial-review-3
draft_source: handoff/02-compose/essay-draft.md
draft_version: 3
review_timestamp: 2026-07-05T00:00:00Z
review_round: 3
posture_applied: measured
closing_posture_declared: firm   # 6G/6H/6I evaluated at full strength
gate_precheck: handoff/03-edit/gate-result.round-3.json (all 14 gates PASS, zero findings/warns; nothing below re-litigates a gate)
overall_assessment: pass

# =====================================================================
# PART 1 — RE-REVIEW PROTOCOL: rulings on every carried round-2 id
# (ruled BEFORE the fresh 7-pass hunt; no id closes silently)
# =====================================================================

carried_findings:

  - finding_id: r2-F1
    prior_severity: medium
    disposition_claimed: applied
    ruling: verified-landed
    evidence: |
      Both splits landed at the named seams, split-only. §3 KGD paragraph now breaks
      after "One bad die can scrap the finished package." → 4 sentences (~63 words),
      and the follow-on paragraph ("That math is the industry's and this essay's, not
      the patent's. ... Only an assembly that has already passed its test gets to
      spend a substrate.") is 3 sentences (~52 words) with declared signature line 2
      byte-identical as its closing sentence. §5 pricing paragraph breaks after
      "...ideas it considers dead (Google Patents)." → "Price it accordingly. ..."
      3 sentences, then the Mahajan/provenance paragraph at 3 sentences. Neighbor
      bands recounted on v3: §3 = 5/4/3/5 sentences (matches the response); §5 =
      6/4/4/6/3/3 sentences — the revision-response's recount listed "6/4/4/3/3",
      omitting the untouched 6-sentence concede paragraph ("Concede all of that...")
      from its list. Bookkeeping omission in the response only, NOT a draft
      regression: every §5 paragraph is in the 3-7 band and the concede paragraph is
      byte-level untouched by the split. No paragraph in the draft now exceeds the
      5C >8-mobile-line threshold except the four quote-integrated paragraphs
      deliberately demoted since round 1 (see Part 2, pass-5 scope). CLOSED.

  - finding_id: r2-F2
    prior_severity: low
    disposition_claimed: applied
    ruling: verified-landed
    evidence: |
      §3 caption now reads "The bridge's underside carries either ball-pitch solder
      pads (526, FIG. 5A) or hybrid-bond contacts (536, FIG. 5B)". Independently
      re-verified against patent.md [0048]: "ball pitch solder pads 526 on the second
      surface ('bottom' in the drawing...) of the bridge component" — noun now
      matches source; 536 (HB contacts) unchanged and correct. The mirror into
      figures-rationale.md "Caption (as written)" landed (r2-F2 note present in that
      file). Upstream Phase-1 figure-rationale.md fix confirmed applied at source per
      the orchestrator's briefing. CLOSED.

  - finding_id: r2-F3
    prior_severity: low
    disposition_claimed: applied
    ruling: verified-landed
    evidence: |
      §4 glass paragraph now opens "There is a quiet glass thread here: the bridge
      itself may be silicon, organic, or glass [0033]." — the essay-self-reference
      clause ("and it stays one paragraph") is gone; [0033] anchor intact; paragraph
      still 6 sentences, no neighbor disturbed. Pass-7 check 4 re-run on all of v3
      (see Part 2): no residual essay-self-reference above the functional-label
      exemption. CLOSED.

  - finding_id: r2-F4
    prior_severity: low
    disposition_claimed: applied
    ruling: verified-landed
    evidence: |
      §5 ¶1 sentence 3 now reads "Its last four drawing sheets, beginning at FIG. 12,
      are generic wafer-and-device boilerplate, and its impressive numbers do not sit
      where..." — the unanchored universal ("every filing carries") is cut, not
      hedged, per the finding's simplest variant. Concession color and the FIG. 12
      pointer survive; ¶ stays 6 sentences. CLOSED.

carried_summary: |
  4/4 round-2 ids ruled, all applied dispositions verified landed in draft v3 with no
  neighbor regressions (paragraph bands recounted around both r2-F1 splits; signature
  line 2 verified byte-identical; figure tokens all present). One transparency note on
  r2-F1: the revision-response's §5 band list omitted one untouched paragraph — a
  response-side bookkeeping slip with zero draft impact. Round-1 chain spot-checked
  (r1-F1 narrowed baseline sentence, r1-F2 FIG. 8 caption numerals, r1-F6 single §6
  guard): all still intact in v3. No id re-asserted.

# =====================================================================
# PART 2 — FRESH 7-PASS REVIEW of draft v3 (fresh context, no commitment
# to prior rounds; new findings would be r3-F<k> — none met the bar)
# =====================================================================

findings:

  - pass: pass-1-voice-anti-ai
    finding: "no findings"
    scoped_to: |
      1B full banned-word/pattern sweep re-run on v3 prose (gate_banned concurs at 0):
      no banned vocabulary, no not-just-X-but-Y, no despite-challenges, no copula
      avoidance (draft consistently uses is/sits/lives), no vague attribution (every
      external claim carries a named source label), no puffery, no section summaries,
      no sentence-initial Additionally, no elegant variation (Intel is always Intel;
      filing/document/application alternation is common-noun use). Tier-2 tells: one
      body semicolon (§5 "never says power, TSV, or cavity; it locks in only") and
      quote-introducing colons — single instances, below cluster threshold,
      false-positive guard applied (consistent with rounds 1-2). 1A cadence: single
      bold thesis anchor (§2), Title Case headers uniform, no emoji, no ALL-CAPS.
      Paragraph bands: all prose paragraphs 3-7 sentences EXCEPT (a) the two
      one-sentence quote-staging lines in §2 ("Then comes the half..." / "That one
      step moves the dividing line:") — the sanctioned blockquote-staging + bold-
      anchor device, accepted in rounds 1-2, and (b) the 2-sentence §4 paragraph
      after the FIG. 7 caption ("In the cavity embodiments... / Even here the attach
      options stay open..."). I counted (b) honestly at 2 sentences (prior rounds'
      blanket "all 3-7" claim was imprecise there) and ruled it NOT a finding under
      the false-positive guard: it is caption-adjacent interpretation carrying the
      [0035] split quote plus the three attach options; merging it into the following
      4-sentence paragraph would create a ~165-word quote-integrated wall (worse
      under 5C), and splitting its dense second sentence has no natural seam. Judged
      deliberate rhythm, not compression damage. No action recommended.

  - pass: pass-2-redundancy
    finding: "no findings"
    scoped_to: |
      2A claim-appearance map rebuilt on v3: order/test-gate motif appears at cover
      caption, §1, §2 blockquotes, §3 walk, §5 refinement, §6 recap — each recurrence
      adds a new evidence layer (news frame → claim text → economics → scope pricing
      → verdict); the three declared signature lines verified byte-intact in v3
      (§1 ¶1 pair, §3 ¶3 close, §6 ¶1 close) and excluded from all counts per
      thesis-trace §Signature-lines. KGD percentages appear exactly once. "Fifteen
      months" appears twice (lead + closing recap — sanctioned bookend). February
      2024 / May 2025 dates each appear twice with distinct context (bibliographic vs
      timeline synthesis). 2B: no ≥25%-cuttable sentence found on a fresh sweep; no
      filler phrases ("in order to", "due to the fact that" absent). 2C: no paragraph
      ≥8 sentences (max 7, §6 ¶2); >150-word single-idea check: only the §4 glass
      paragraph (~150 words) — quote-integrated ([0049]/[0138]/[0059] quotes with
      interpretation), demotion per posture-lens heuristic carried from round 1,
      splitting would orphan quote from interpretation.

  - pass: pass-3-fact-paraphrase
    finding: "no findings"
    scoped_to: |
      3A: all [dddd]-anchored spans in v3 re-verified against input/patent.md
      directly (not only against invention-summary): [0001] wish-list quote verbatim
      (patent.md line "[0001] There is an ongoing push to improve bump density,
      power efficiency, speed and bandwidth..."); both §2 blockquotes byte-match
      Example 21 [0142] with the required Example attribution line; §3 quotes match
      [0061]/[0062] (leading "At 1110,"/"At 1112," cleanly omitted outside the
      quotes); §4 [0024] both quotes, [0035] split quote (the "102" omission handled
      by closing/reopening quotes — both halves verbatim-contiguous), [0123] claim-2
      language, [0035] effect sentence, [0049] "to provide structural stability",
      [0138] glass range, [0059] SoC sentence; §5 re-uses of [0034]/[0122]/[0123]/
      [0035]/[0142]/[0144] all verbatim. Claim-structure assertions independently
      re-verified against the patent's Claims section: claim 17 hangs off no-cavity
      claim 16 (draft §5 correct); no claim carries the 1-10 µm pitch (correct);
      claim 2/[0123] never says power/TSV/cavity (correct); claim 19 order + test +
      when-passes and claim 20 cavity seating (correct); Examples 24/25 [0145]/[0146]
      claim hybrid bonding and solder as separate options (§2 "claims hybrid bonding
      and solder separately, as options" correct). Sought-vocabulary discipline held
      throughout ("as filed", "asking for", "a lock Intel is asking for"). 3B: every
      external claim traced to a fact-check-log ID and # Sources: 15-month and
      18-month intervals recomputed (2024-02-20 → 2025-05 ≈ 15 mo; → 2025-08-21 =
      18 mo ✓); thirteen inventors recounted from the Sources entry (13 ✓); KGD math
      recomputed (0.95^4 = 0.815 → "about 81 percent", 0.95^20 = 0.358 → "about 35
      percent" ✓, labeled industry math, never the patent's); 120x120 mm roadmap
      carries its single-outlet label per the log's tier-3 note; counterparts
      JP/KR/CN/DE (tier-1); Mahajan used within its "mainline packaging organization"
      limit; glass announcement Sept 2023 (tier-1). EMIB fence re-swept on v3: the
      patent never uses EMIB/EMIB-T, and no EMIB/EMIB-T sentence in the draft carries
      a [dddd] anchor — all ride named-source labels; the document-never-says-EMIB
      disclosure appears in §4 and §5. Figure captions re-checked against the
      reference-number table: FIG. 5A/5B (526 pads / 536 HB contacts, post-r2-F2 ✓),
      FIG. 7 (701/702/704 ✓), FIG. 8 (872/882/860 ✓), cover FIG. 11 flow ✓. 3C: no
      quoted-text mutations (gate_quotes concurs); no accidental-drift paraphrase
      found this round. 3D: no new causal claims in v3's changed spans (the four
      r2 edits are two splits, one clause cut, one noun swap, one universal cut).

  - pass: pass-4-logic-causality
    finding: "no findings"
    scoped_to: |
      4A re-traced against thesis-spine's spine→section table on v3: Axis 1 → §2
      (re-priced §5), Axis 2 → §4, Axis 3 → §3, Axis 4 → §4; no out-of-spine claim;
      the four r2 edits introduced no new claims (two were pure splits). 4B causal
      sweep: "it explains why a flow... reads like an economic decision" (mechanism
      shown, labeled as industry's + essay's math); "fee money a company does not
      usually spend on ideas it considers dead" (hedged inference, "usually");
      "The paperwork moved first last time." (n=1 fact — Mahajan's silicon-bridge
      patents preceding EMIB is the anchored antecedent — stated as history, not
      law); the after-EMIB-T link framed throughout as timeline+mechanism synthesis
      with "Intel has not connected the two documents" stated in §5. No
      correlation→causation drift, no overstated causation. 4C: lead tension
      (EMIB-T stage narrative vs the filed inverted flow) set in ¶1, resolved in
      §6's order-of-operations verdict; closing-binary-test matches the spine's
      Acknowledged residual risk under firm posture (never open-question); the
      implication is this-patent-specific (test-gate economics + this family's
      prosecution), not generic.

  - pass: pass-5-reader-perspective
    finding: "no findings"
    scoped_to: |
      Full cold read as the reader-profile investor. 5A: hook lands in ¶1 sentence 1;
      no 3+ paragraph density wall (§4's mechanism run is broken by two captions and
      the "Why rebuild the order at all?" / "Note whose yield that is" re-anchors —
      the latter ruled a content-pointing beat, not reader-instruction, consistent
      with round 2); closing lands on the thesis, not a new claim. 5B: "why does
      this matter" answerable after the lead (two-sided call), at every boundary
      (§2 what changed / §3 what it saves / §4 why bother / §5 what is owned vs
      asked), and the §6 close reads standalone; money thread feeds the verdict in
      every section. Jargon: bridge die, substrate ("board-like base"), TSV
      ("vertical metal shafts"), TGV, hybrid bonding ("no solder in between"),
      micron ("a millionth of a meter"), known-good die — each glossed one clause on
      first use, then used as signposts. 5C mechanical recount on all of v3 at 12
      words/line: post-split §3 and §5 paragraphs all ≤8 lines; the four
      quote-integrated paragraphs (§2 ¶3 ~127w, §4 glass ¶ ~150w, §5 ¶1 ~127w, §5
      concede ¶ ~130w) remain over-threshold and remain demoted to low per the
      posture-lens quote-integrated heuristic and the rounds-1/2 adjacency rationale
      (splitting orphans quote from interpretation) — deliberately not re-raised.
      Transparency measurement: §6 ¶2 counts 98 words ≈ 8.2 lines at the strict
      12-w/l bound (7.3 at the reference's 13.5 midpoint) — within the heuristic's
      own noise band, and the paragraph is seven short declarative sentences (max 30
      words), not a density wall; splitting the verdict paragraph would trade the
      landing rhythm against a 2%-over heuristic. Ruled not a finding; recorded here
      so round 4 can falsify the call.

  - pass: pass-6-lead-conclusion-format
    finding: "no findings"
    scoped_to: |
      6A: ¶1 sentence 1 sets the tension, patent on the table by sentence 3, full
      two-sided call lands inside the lead (§1 ¶3). 6B: frame closure holds — the
      fifteen-months/stage frame returns in §6 ¶1 and "The paperwork moved first
      last time." closes the loop; closing-binary-test matches Acknowledged residual
      risk under declared firm posture. 6C: # Sources has exactly the 5 enum
      categories, 7 entries, all-or-nothing subgrouping honored. 6D: no "First, et
      al." malformation (the ECTC entry's thin bibliographic fields remain the
      accepted r1-F17 upstream item, not a draft defect). 6E: em-dash 0, all inline
      cites 4-digit [dddd], banned re-grep clean, # Sources exactly once, no footnote
      defs. 6F: title has no em-dash and no colon; 54 chars (≤70). 6G under firm
      posture: the verdict leads with the call ("This filing is Intel's mainline
      packaging organization writing down the assembly flow that comes after the one
      it is currently selling."); exactly ONE anti-hype guard and it is
      this-filing-specific ("It is one pending application, and nothing in it
      schedules a product."); limits referenced, not re-listed ("stand as written");
      no qualifier-led sentence, no false equivalence, no category truism; symmetric
      check for overreach: the call is conditioned by a named binary falsifier in
      BOTH directions (ECTC-class disclosures / prosecution vs examination narrowing
      away from the test step) and the after-EMIB-T synthesis is disclosed and
      priced in §4/§5 — evidence-proportionate both ways. 6H: no insurance fact
      precedes the ¶1 discovery beat; the first two lines earn the tap. 6I:
      procedure/pricing narration confined to §5 (the one payload:pricing home) plus
      one lead status clause (§1 ¶3) and the §6 guard/recap clause; no process
      narration in the lead; spend-motif budget held ("fee money" once; "one filing
      among hundreds" family once, in §5; SURF-005/006 zero-warn concurs).

  - pass: pass-7-adversarial-reader
    finding: "no findings"
    scoped_to: |
      All 7 checks run with quoted evidence on v3. (1) Hook: PASS — ¶1 opens on the
      declarative discovery beat ("Fifteen months before Intel put EMIB-T on a
      conference stage, a filing from its packaging group had already written down a
      different way to build the same kind of chip package."), no insurance ahead of
      it; two-sided call lands by lead end ("It is also a pending application: a set
      of claims Intel is asking for, not a product it has scheduled."). (2)
      Header-as-claim: PASS — all six headers assert; the header-only skim
      reconstructs the argument (filed next flow → bridge changes sides → test
      before substrate → power through floor → one claim matters → the claim is an
      order of operations). (3) Steelman: PASS — THIS-patent objection conceded at
      full strength in §5 (claim-scope stitching: pitch description-only [0034],
      purpose description-only [0035], claim 17 on the no-cavity branch, no claim
      holds the full architecture, document never says EMIB) then refined via claim
      19/20's locked order + test gate; independently pressure-tested a second
      objection ("pre-assembly testing is standard KGD practice") — the essay
      already attributes the KGD concept to industry (§3) and stakes novelty on the
      ORDER, with examination-narrows-the-test-step named as the falsifier, so the
      objection finds no unrebutted purchase. (4) Meta: PASS — the three remaining
      self-references are functional attribution labels ("this essay's synthesis",
      "the industry's and this essay's, not the patent's"), exempt by rule; "Note
      whose yield that is." rules as a content pointer at the [0035] scope boundary,
      one instance. (5) Jargon: PASS — terms stay signposts; the glass thread stays
      one paragraph without doctrinal deep-dive. (6) Stub: PASS — §6 at ~196 words
      is the proportionate closing against 230-620-word siblings; no section
      markedly short. (7) Restatement: PASS — non-exempt core-verdict assertions in
      exactly 3 sections (§2 bold anchor, §5 refinement, §6 call); the three
      declared signature lines byte-intact and exempt.
```
