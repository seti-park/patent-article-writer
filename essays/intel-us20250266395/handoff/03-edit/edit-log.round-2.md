# Edit Log — Round 2

```yaml
review_id: intel-us20250266395-editorial-review-2
draft_source: handoff/02-compose/essay-draft.md
draft_version: 2
review_timestamp: 2026-07-05T00:00:00Z
review_round: 2
posture_applied: measured
closing_posture_declared: firm   # 6G/6H/6I evaluated at full strength
gate_precheck: handoff/03-edit/gate-result.round-2.json (all 14 gates PASS, zero findings/warns; nothing below re-litigates a gate)
overall_assessment: revise-recommended

# =====================================================================
# PART 1 — RE-REVIEW PROTOCOL: rulings on every carried round-1 id
# (ruled BEFORE the fresh 7-pass hunt; no id closes silently)
# =====================================================================

carried_findings:

  - finding_id: r1-F1
    prior_severity: high
    disposition_claimed: applied
    ruling: verified-landed
    evidence: |
      §2 now reads "Then comes the half Intel's shipped bridge flow does not contain, the
      test-and-commit order:" — the universal negative ("no shipped bridge flow contains")
      is narrowed to the scope emib-chips-last-flow (tier-2) supports. Fix followed the
      grounding priority (narrow, not hedge); sentence force intact. CLOSED.

  - finding_id: r1-F2
    prior_severity: high
    disposition_claimed: applied
    ruling: verified-landed
    evidence: |
      FIG. 8 caption now reads "the dies land across the substrate top on solder bumps
      (882)" — numeral 882 attaches to the bumps, matching patent.md [0056] and the
      invention-summary reference row ("882/982 | solder bumps, dies to substrate top
      surface"). 872 (bridge) and 860 (underfill) unchanged and still correct. The
      volunteered figures-rationale.md "Caption (as written)" sync also landed (verified).
      CLOSED.

  - finding_id: r1-F3
    prior_severity: medium
    disposition_claimed: applied
    ruling: verified-landed
    evidence: |
      §2 ¶1 now reads "set two chips on a temporary carrier, mold them into one rigid
      piece" — "face-down" is gone. Independently re-verified: grep of input/patent.md
      returns 0 hits for "face-down". The upstream fix also landed: invention-summary.md
      Layer-2 step 1 now reads "Assemble a first IC die and a second IC die on a carrier
      with an adhesive/bond film (1102)" with no orientation claim, so a future recompose
      cannot reintroduce the drift. CLOSED.

  - finding_id: r1-F4
    prior_severity: medium
    disposition_claimed: applied
    ruling: verified-landed
    evidence: |
      §5 now reads "...hangs off the no-cavity inverted package of claim 16, not off the
      cavity packages described above. The parallel Example paragraph is written broader
      [0138]. The claim as filed is not." The Example/claim divergence is named at the
      anchor exactly as the Claim scope map instructs. Neighbor recount after the
      accompanying §5 split: the dissection paragraphs sit at 4 + 4 sentences, in band.
      No regression. CLOSED.

  - finding_id: r1-F5
    prior_severity: medium
    disposition_claimed: applied
    ruling: verified-landed
    evidence: |
      §1: "So read it two-sided from the start:" → "That cuts two ways. This is the most
      concrete piece of after-EMIB-T assembly thinking on the public record. It is also a
      pending application: ..." (declarative; two-sided call still lands inside the lead).
      §2: "Hold on to what just happened there:" → "That one step moves the dividing
      line:" staging the unchanged bold anchor as a claim. Both reader-instructions gone;
      pass-7 check 4 re-run on the full draft (see Part 2). CLOSED.

  - finding_id: r1-F6
    prior_severity: medium
    disposition_claimed: applied
    ruling: verified-landed
    evidence: |
      §6 guard now reads "It is one pending application, and nothing in it schedules a
      product." — this-filing-specific (the spine's own sanctioned wording), weight
      unchanged, still exactly ONE guard in the verdict, limits still referenced not
      re-listed. 6G re-checked under firm posture: call leads, no qualifier-led sentence,
      no false equivalence, hedge budget held. CLOSED.

  - finding_id: r1-F7
    prior_severity: medium
    disposition_claimed: applied
    ruling: verified-landed
    evidence: |
      Both splits landed at the recommended seams. §1 ¶2 breaks after "(Google Patents)."
      — bands now 5 / 4 / 4 sentences (~94 / ~80 / ~60 words); the two-sided call still
      lands inside the lead section (6A/6H unaffected). §4 EMIB paragraph breaks after
      "(IEEE ECTC paper; see Sources)." — 3 / 3 sentences. The two quote-integrated
      paragraphs the finding demoted to low (§2 ¶3, §4 glass ¶) were left intact per the
      quote-interpretation adjacency rationale — accepted. Minor note, not a finding:
      ¶2b now opens with the pronoun "It" whose antecedent ("The application in
      question") sits across the new break; antecedent is adjacent and unambiguous.
      CLOSED. (Two other paragraphs newly exceed the 5C mobile threshold on this round's
      recount — filed fresh as r2-F1, not a regression of this fix: neither was touched
      by it, and one got SHORTER via r1-F18.)

  - finding_id: r1-F8
    prior_severity: medium
    disposition_claimed: applied
    ruling: verified-landed
    evidence: |
      §5 ¶1 now reads "and its impressive numbers do not sit where the previous sections
      may have left the impression they do." — grammatical, and the self-reference is
      gone. The composer's refusal of the "are not in the claims" variant is CORRECT and
      noted with approval: claim 17 as filed carries an exact numeric range
      (20 µm-1.4 mm), so that variant would have traded grammar for a scope error.
      CLOSED.

  - finding_id: r1-F9
    prior_severity: low
    disposition_claimed: applied
    ruling: verified-landed
    evidence: |
      Dual anchor "[0060], [0061]" present on the plain-English method sentence;
      carrier/mold steps live in [0060] per the Layer-2 mechanism. CLOSED.

  - finding_id: r1-F10
    prior_severity: low
    disposition_claimed: applied
    ruling: verified-landed
    evidence: |
      "The payoff on offer is the one stated-effect sentence in the document" —
      "quantified" gone; the doubled-"stated" avoidance wording is factually identical.
      CLOSED.

  - finding_id: r1-F11
    prior_severity: low
    disposition_claimed: applied
    ruling: verified-landed
    evidence: |
      §1 ¶1 split so [0142] anchors only the patent half: "In the flow Intel ships
      today, the little bridge die is buried in the board, and the chips land on top."
      (unanchored, sourced in §4) then "The filed method bonds the bridge straight onto
      the chips first, then tests the whole cluster before a board ever enters the
      picture [0142]." No EMIB-baseline content rides a [dddd] anchor. CLOSED.

  - finding_id: r1-F12
    prior_severity: low
    disposition_claimed: rejected
    ruling: rejection-accepted
    evidence: |
      Independently re-verified against input/patent.md: the claims section's FINAL LINE
      is claim 20 — "The method of claim 19, wherein the substrate has a cavity and
      attaching the substrate to the multi-die bridge assembly includes placing the
      bridge component in the cavity." The round-1 finding's premise (snapshot truncates
      at claim 19) was factually wrong. Rejection accepted; finding closed as invalid.
      The draft's "one dependent claim away, 'placing the bridge component in the
      cavity' [0144]" is fully supported. CLOSED.

  - finding_id: r1-F13
    prior_severity: low
    disposition_claimed: applied
    ruling: verified-landed
    evidence: |
      "Intel has discussed rolling out EMIB packages up to roughly 120 by 120
      millimeters from 2026" — the time reference attaches to the rollout, matching
      emib-package-roadmap-120mm; single-outlet label retained. CLOSED.

  - finding_id: r1-F14
    prior_severity: low
    disposition_claimed: applied
    ruling: verified-landed
    evidence: |
      Both recastable self-references removed ("the cavity packages described above";
      the r1-F8 rewrite). The three functional attribution labels remain, correctly:
      "That math is the industry's and this essay's, not the patent's" (§3), "every link
      this essay draws to it rests on timeline and mechanism" (§4), "The after-EMIB-T
      reading is this essay's synthesis" (§5). CLOSED.

  - finding_id: r1-F15
    prior_severity: low
    disposition_claimed: rejected
    ruling: rejection-accepted
    evidence: |
      Rationale is sound and rule-grounded: the hair-width comparison is an external
      factual claim with no fact-check-log entry, and the composer's execution boundary
      forbids fact introduction in ALL modes, revision included. The finding's own
      mitigator (the draft deflates the number's claim status one clause later) stands.
      The upstream option (Phase 1 logs a tier-4 hair-width entry if wanted) is noted
      for the orchestrator; not re-asserted. CLOSED.

  - finding_id: r1-F17
    prior_severity: low
    disposition_claimed: rejected
    ruling: rejection-accepted
    evidence: |
      Rationale is sound: resolving the ECTC entry's real title/authors requires
      fetching the ieeexplore record, which no Phase-1 artifact carries, and the source
      fence forbids externally fetched material in revision. The upstream flag (enrich
      the fact-check-log bibliographic fields; Sources then updates mechanically)
      remains open as an orchestrator/Phase-1 action item — advisory, not a draft
      defect. CLOSED at the draft level.

  - finding_id: r1-F18
    prior_severity: low
    disposition_claimed: applied
    ruling: verified-landed
    evidence: |
      "And the names on it are not a side project." is cut; the Mahajan sentence opens
      the beat directly. Paragraph recounted: 6 sentences, in band. CLOSED.

carried_summary: |
  18/18 round-1 ids ruled. 15 applied dispositions verified landed with no neighbor
  regressions (paragraph bands recounted around every structural edit: §1 splits, §4
  split, §5 split, §5 cut). 3 rejections (r1-F12, r1-F15, r1-F17) accepted — r1-F12's
  rejection independently re-verified against the patent snapshot. No id re-asserted.

# =====================================================================
# PART 2 — FRESH 7-PASS REVIEW of draft v2 (new findings: r2-F<k>)
# =====================================================================

findings:

  # ---------- MEDIUM ----------

  - finding_id: r2-F1
    pass: pass-5-reader-perspective
    location: "§3, paragraph 2 (the KGD-arithmetic paragraph, 'The patent never puts a number...'); secondary: §5, paragraph 4 ('Price it accordingly...')"
    severity: medium
    severity_under_default_posture: medium
    finding: |
      5C mobile rendering, mechanical recount of draft v2: the KGD paragraph runs 115
      words ≈ 9.6 lines at 12 words/line (7 sentences), and the pricing paragraph runs
      112 words ≈ 9.3 lines (6 sentences) — both over the >8-line threshold. Neither
      qualifies for the quote-integrated demotion (no verbatim patent quote + [dddd]
      anchor structure; the KGD numbers are external industry math, the pricing facts
      are Google-Patents-labeled). Transparency note: both paragraphs stood at similar
      length in round 1 and were not flagged (round 1's applied bar was ~124+ words);
      this round applies the reference threshold as written. The KGD paragraph is the
      heavier case: it carries the essay's economic stake and ends on declared signature
      line 2, and a 9.6-line wall risks the skim right before that line. The four
      quote-integrated long paragraphs (§2 ¶3, §4 glass ¶, §5 ¶¶1/3) remain demoted to
      low per round 1 and are deliberately NOT re-raised (splitting them would orphan
      quote from interpretation).
    recommendation: |
      Split both at natural seams; no content changes, no signature-line contact.
      §3 ¶2: break after "One bad die can scrap the finished package." → 4 + 3
      sentences (~63 + ~52 words); signature line 2 stays the closing sentence of the
      second paragraph. §5 pricing ¶: break after "...ideas it considers dead (Google
      Patents)." → 3 + 3 sentences (status+counterparts / provenance+weight). Re-count
      neighbor bands after the splits.

  # ---------- LOW ----------

  - finding_id: r2-F2
    pass: pass-3-fact-paraphrase
    location: "§3, FIG. 5A/5B caption"
    severity: low
    severity_under_default_posture: low
    finding: |
      Caption precision against patent.md [0048]: the source reads "ball pitch solder
      pads 526 on the second surface ('bottom' in the drawing...) of the bridge
      component" — numeral 526 labels solder PADS at ball pitch; the caption calls them
      "solder balls (526, FIG. 5A)". Unlike r1-F2 this is not a part mis-attribution
      (the numeral sits on the right structure in the right place, bridge underside);
      the part noun drifted pads → balls. Low: a reader decoding the figure still finds
      the right feature; classification: accidental drift, caption-local, non-quoted.
    recommendation: |
      "The bridge's underside carries either solder pads (526, FIG. 5A) or hybrid-bond
      contacts (536, FIG. 5B)..." — one word; mirror into figures-rationale.md's
      "Caption (as written)" record as with r1-F2.
    quote: "The bridge's underside carries either solder balls (526, FIG. 5A) or hybrid-bond contacts (536, FIG. 5B)"

  - finding_id: r2-F3
    pass: pass-7-adversarial-reader
    location: "§4, glass paragraph, first sentence"
    severity: low
    severity_under_default_posture: low
    finding: |
      Check 4 (no meta posturing), residual after the r1-F5 fixes: "There is a quiet
      glass thread here, and it stays one paragraph". The clause "and it stays one
      paragraph" can only refer to the ESSAY's own allocation (in the patent, the glass
      material spans [0033]/[0049]/[0054]/[0138] — multiple paragraphs), so it is a
      judgment-tier essay-self-reference below gate_meta's lexicon. One clause, not a
      reading instruction; low.
    recommendation: |
      Cut the clause: "There is a quiet glass thread here: the bridge itself may be
      silicon, organic, or glass [0033]." Nothing else in the paragraph changes.
    quote: "There is a quiet glass thread here, and it stays one paragraph:"

  - finding_id: r2-F4
    pass: pass-3-fact-paraphrase
    location: "§5, paragraph 1, sentence 3"
    severity: low
    severity_under_default_posture: low
    finding: |
      Unanchored universal, decorative: "the generic wafer-and-device boilerplate every
      filing carries" asserts that EVERY filing carries these context sheets — no
      fact-check-log entry, and not literally true across filings. Same claim-class as
      r1-F1 but low, not high: it sits inside the steelman's concession voice as color,
      is not load-bearing for the thesis, and concedes AGAINST the essay's interest.
      Still checkably overbroad in the section built for claim-scope credibility.
    recommendation: |
      Narrow or cut the universal (never hedge): simplest is "...are generic
      wafer-and-device boilerplate." (drop "every filing carries"); alternatively
      "...the generic wafer-and-device boilerplate that pads out a filing of this
      kind."
    quote: "are the generic wafer-and-device boilerplate every filing carries"

  # ---------- NO-FINDINGS PASS ENTRIES ----------

  - pass: pass-1-voice-anti-ai
    finding: "no findings"
    scoped_to: |
      1A cadence re-judged on v2 against deliverable-voice-rules: all prose paragraphs
      3-7 sentences (max 7, §3 ¶2 and §6 ¶2); single bold thesis anchor unchanged in §2;
      Title Case headers consistent; the r1-F5/F7/F4 rewrite spans checked specifically
      for clipped-cadence regression — none ("That cuts two ways." and "The dissection
      cuts deeper still." read as deliberate short-beat pivots, not compression
      artifacts). 1B full banned-word grep re-run on v2: 0 hits (gate_banned concurs).
      Banned patterns: no not-just-X-but-Y, no despite-challenges, no copula avoidance
      (draft still favors is/sits/lives), no vague attribution (every external claim
      carries a named source label), no puffery, no section summaries, no elegant
      variation (filing/document/application alternation remains legitimate common-noun
      use). Tier-2 tells: one body semicolon (§5 through-via sentence) and
      quote-introducing colons — below cluster threshold, false-positive guard applied.
      Residual self-reference clause escalated as r2-F3 (pass-7 jurisdiction).

  - pass: pass-2-redundancy
    finding: "no findings"
    scoped_to: |
      2A claim-appearance map rebuilt on v2 for the order/test-gate motif (cover
      caption, §1, §2 blockquotes, §3 walk, §5 re-pricing, §6 recap): each recurrence
      still adds a new evidence layer; the three declared signature lines verified
      verbatim-intact in the draft and excluded from all counts per thesis-trace §5.
      §6's recap sentence ("Bond the bridge to the chips first, test the cluster while
      no board is committed...") sits adjacent to exempt signature line 3 — judged the
      sanctioned closing recap plus the aphoristic landing, not unearned repetition
      (gate_dupe concurs). KGD percentages appear once. 2B tightening sweep on v2: the
      r1-F18 cut landed; no remaining ≥25%-cuttable sentence found. 2C: no paragraph
      ≥8 sentences; >150-word check: only the §4 glass paragraph (~154 words incl.
      anchors) — quote-integrated, demoted per posture-lens heuristic, left intact per
      the round-1 adjacency rationale (mobile-length aspect consolidated under r2-F1's
      scope note, not double-filed).

  - pass: pass-3-fact-paraphrase
    finding: "no further findings"
    scoped_to: |
      3A: all 20 [dddd]-anchored spans in v2 re-verified against invention-summary
      Quotable spans / Quote anchor table; both §2 blockquotes byte-match q-0142-1/2
      with the Example-21 attribution the invention-summary note requires ("claim
      language as filed" + Example anchor). Split-quote handling at [0035] (omitting
      "102" by closing the quote) verified verbatim-contiguous. [0057]/[0058] use
      sanctioned by phase2-handoff-notes; [0060]+[0061] dual anchor correct; [0138]
      divergence now labeled (r1-F4). 3B: every external claim traced to a
      fact-check-log ID and to # Sources: 15-month timeline (Feb 2024 → May 2025 ✓),
      thirteen inventors (✓ counted), 18-month publication interval (✓), 0.95^4=0.815 →
      "about 81 percent" and 0.95^20=0.358 → "about 35 percent" (✓, labeled industry
      math), 120x120 mm roadmap (single-outlet label present per log note), counterparts
      JP/KR/CN/DE (tier-1), Mahajan (tier-2, used within its "mainline packaging
      organization" limit), glass announcement Sept 2023 (tier-1). EMIB fence re-swept:
      no EMIB/EMIB-T statement carries a [dddd] anchor; the document-never-says-EMIB
      disclosure appears in §4 and §5 as designed. 3C: no quoted-text mutations (gate
      concurs); caption drift filed as r2-F2; universal-color claim filed as r2-F4.
      3D: no new causal claims in the revised spans.

  - pass: pass-4-logic-causality
    finding: "no findings"
    scoped_to: |
      4A re-traced on v2 against the spine→section table: all four axes carried in
      their declared sections; no out-of-spine claim introduced by the revision
      (r1-F1's narrowing brought §2's baseline sentence INSIDE the anchored scope);
      sought-vocabulary discipline held ("as filed", "asking for", "a lock Intel is
      asking for"); claim-17/claim-16 dependency stated correctly with the Example
      divergence now labeled. 4B causal sweep on v2: "explains why" (mechanism shown,
      labeled industry arithmetic), "reads like an economic decision" (labeled
      analysis), "fee money a company does not usually spend" (hedged inference),
      "The paperwork moved first last time." (n=1 factual, not asserted as law) — all
      unchanged rulings; the EMIB-T link remains framed as timeline+mechanism synthesis
      with Intel-has-not-connected stated. 4C: lead tension (news narrative vs filed
      flow) still resolves in §6's order-of-operations verdict; closing-binary-test
      matches the spine's residual-risk mapping under firm posture.

  - pass: pass-5-reader-perspective
    finding: "no further findings"
    scoped_to: |
      5A: hook lands in sentence 1; post-split §1 reads faster; §4's mechanism run
      remains broken by two captions and the "Why rebuild the order at all?" /
      "Note whose yield that is" re-anchors; no 3+ paragraph density wall. 5B: stake
      re-answerable after the lead (two-sided call), at §3 (substrate economics), §5
      (what is asked vs owned), §6; closing paragraph reads standalone; money thread
      feeds the verdict in every section. Jargon glosses verified on v2: bridge die,
      substrate (r1-F16, landed), TSV, TGV, hybrid bonding, known-good die, micron —
      each one clause, then used freely; "the expensive part" epithet for the substrate
      judged defensible labeled-analysis color inside the industry-arithmetic frame
      (the paragraph's own math carries the point), not a naked-magnitude or accuracy
      defect. 5C mechanical recount performed on all of v2 — the two over-threshold
      non-quote-integrated paragraphs filed as r2-F1; the four quote-integrated ones
      stay demoted per posture-lens.

  - pass: pass-6-lead-conclusion-format
    finding: "no findings"
    scoped_to: |
      6A: thesis on the table by ¶1 sentence 3; patent in the lead. 6B: frame closure
      holds (fifteen-months/stage frame returns in §6; "The paperwork moved first last
      time." closes the loop); closing-binary-test, not open-question. 6C: five
      categories, all in enum, all-or-nothing subgrouping honored. 6D: no "First, et
      al." malformation (ECTC entry's missing bibliographic fields remains the accepted
      r1-F17 upstream item). 6E: em-dash 0, all cites 4-digit, banned re-grep clean,
      # Sources exactly once. 6F: title colon-free and em-dash-free, 52 chars. 6G under
      firm posture: verdict leads with the call; exactly ONE anti-hype guard, now
      this-filing-specific (r1-F6 verified); limits referenced not re-listed ("stand as
      written"); "none of them moves the call" is confidence the §5 refinement earned —
      no over-hedge, no overreach; falsifier present without qualifier-stacking. 6H: no
      insurance fact precedes the ¶1 discovery beat; first two lines earn the tap. 6I:
      procedure/pricing narration confined to §5 (single home) + one lead status clause
      + §6 recap clause; "more than paper" in §6 ruled binary-test framing within the
      recap allowance; spend-motif budget held (SURF-005/006 zero-warn concurs).

  - pass: pass-7-adversarial-reader
    finding: "no further findings"
    scoped_to: |
      Check 1 hook: PASS — ¶1 sentence 1 is the discovery beat, declarative, no
      insurance ahead; two-sided call lands by lead end ("It is also a pending
      application: a set of claims Intel is asking for, not a product it has
      scheduled."). Check 2 header-as-claim: PASS — all six headers assert; header-only
      skim still reconstructs the argument. Check 3 steelman: PASS — THIS-patent
      objection (claim-scope stitching: pitch in description [0034], purpose in
      description [0035], claim 17 on the no-cavity branch, no EMIB anywhere) conceded
      at full strength then refined via claim 19's locked order+test; not a generic
      truism (the generic guard is spent exactly once, in §6, per budget). Check 4
      meta: r1-F5 spans verified recast; one residual judgment-tier clause → r2-F3
      (low). Check 5 jargon: PASS — all terms glossed once and kept as signposts.
      Check 6 stub: PASS — §6 at ~196 words is the proportionate closing recap.
      Check 7 restatement: PASS — non-exempt core-verdict assertions in 3 sections
      (§2 bold anchor, §5 refinement, §6 call); three declared signature lines
      verbatim-intact and exempt.
```
