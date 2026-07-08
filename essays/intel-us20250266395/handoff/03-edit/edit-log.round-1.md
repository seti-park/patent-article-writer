# Edit Log — Round 1

```yaml
review_id: intel-us20250266395-editorial-review-1
draft_source: handoff/02-compose/essay-draft.md
review_timestamp: 2026-07-05T00:00:00Z
review_round: 1
posture_applied: measured
closing_posture_declared: firm   # 6G/6H/6I evaluated at full strength
gate_precheck: handoff/03-edit/gate-result.round-1.json (all 14 gates PASS; nothing below re-litigates a gate)
overall_assessment: revise-required

findings:

  # ---------- HIGH ----------

  - finding_id: r1-F1
    pass: pass-3-fact-paraphrase
    location: "§2 (The Bridge Changes Sides), sentence introducing the second blockquote: 'Then comes the half no shipped bridge flow contains, the test-and-commit order:'"
    severity: high
    severity_under_default_posture: high
    finding: |
      Universal external claim with no fact-check-log entry. "No shipped bridge flow contains
      [a test-and-commit order]" asserts a negative across the entire industry's shipped bridge
      flows. The log supports only the narrower claim: Intel's shipped EMIB flow embeds the
      bridge in the substrate first and attaches chips last (emib-chips-last-flow, tier-2).
      Nothing verifies the absence of pre-substrate cluster testing in every shipped bridge
      flow anywhere (e.g., non-Intel bridge integrations are unexamined). The sentence is
      load-bearing: it frames the test gate as industry-unique rather than EMIB-flow-unique.
    recommendation: |
      Narrow the claim to what the anchor supports (fix priority: narrow, not hedge):
      "Then comes the half Intel's shipped bridge flow does not contain, the test-and-commit
      order:" (rests on emib-chips-last-flow). The force of the sentence survives intact;
      §5's parallel formulation already does this correctly ("exactly the piece the public
      EMIB-T story does not have").
    quote: "Then comes the half no shipped bridge flow contains, the test-and-commit order:"
    related_fact_entry: emib-chips-last-flow

  - finding_id: r1-F2
    pass: pass-3-fact-paraphrase
    location: "§4, FIG. 8 caption"
    severity: high
    severity_under_default_posture: high
    finding: |
      Reference-numeral mis-attribution, verified against patent.md [0056]: "The IC 1 and IC 2
      are solder attached to the upper surface of the substrate 870/970 with solder bumps
      882/982." Numeral 882 labels the SOLDER BUMPS, not the dies (invention-summary reference
      table agrees: "882/982 | solder bumps, dies to substrate top surface"). The caption reads
      "the dies (882) land across the substrate top", assigning 882 to the dies. A reader
      decoding the figure against the caption misidentifies the part; captions are goal-2
      trust surface and this is checkable by anyone with the document. (872 for the bridge and
      860 for the underfill in the same caption are correct.)
    recommendation: |
      Reword so 882 attaches to the bumps: "the dies land across the substrate top on solder
      bumps (882)". One-clause fix; no other caption in the draft has this defect (526/536 in
      the FIG. 5A/5B caption and 701/702/704 in FIG. 7 all verify against [0048]/[0052]-[0055]).
    quote: "the dies (882) land across the substrate top"

  # ---------- MEDIUM ----------

  - finding_id: r1-F3
    pass: pass-3-fact-paraphrase
    location: "§2, paragraph 1, the plain-English translation of the method claim"
    severity: medium
    severity_under_default_posture: medium
    finding: |
      Paraphrase adds a detail the source does not state. "Set two chips face-down on a
      temporary carrier" — neither [0060] ("assembling a first integrated circuit (IC) die and
      a second IC die on a carrier with an adhesive or bond film"), nor [0061], nor claim 19
      as filed says anything about die orientation; "face-down" appears nowhere in patent.md
      (grep-verified). It is a plausible engineering inference from the figures, but it sits
      inside the sentence presented as the plain-English rendering of THE spine claim, where
      invented specifics are most costly. Classification: accidental drift (added detail),
      not substantive change (order-of-operations meaning is preserved).
    recommendation: |
      Cut "face-down": "set two chips on a temporary carrier, mold them into one rigid piece..."
      Nothing in the sentence's job needs the orientation.
    quote: "set two chips face-down on a temporary carrier"

  - finding_id: r1-F4
    pass: pass-3-fact-paraphrase
    location: "§5, paragraph 2, claim-17 sentence anchored [0138]"
    severity: medium
    severity_under_default_posture: medium
    finding: |
      Correct statement, self-undermining anchor. The sentence says claim 17 "hangs off the
      no-cavity inverted package of claim 16, not off the cavity packages" — TRUE per the
      claims text (claim 17: "The semiconductor package of claim 16...") and the Claim scope
      map. But the anchor shown is [0138], whose Example 17 text reads "any one of Examples
      12-16" — the BROADER form. A skeptical reader who checks the anchor finds text that
      appears to contradict the sentence, in the exact section built to establish claim-scope
      credibility. The scope map and phase2-handoff-notes flag precisely this divergence
      ("Example 17 is written broader than the claim; attribute breadth to the Example, not
      the claim").
    recommendation: |
      Better anchor / labeled divergence (fix priority: anchor first): keep the sentence and
      make the divergence explicit, e.g. "...not off the cavity packages this filing's cavity
      sections describe (the parallel Example paragraph is written broader [0138]; the claim
      as filed is not)." Alternatively drop the [0138] anchor from this sentence (the claim
      text itself carries no paragraph anchor) and leave [0138] to §4's Example-attributed use,
      which is already correct.
    quote: "The glass-and-TGV claim, claim 17 as filed, hangs off the no-cavity inverted package of claim 16, not off the cavity packages this essay has been drawing [0138]."

  - finding_id: r1-F5
    pass: pass-7-adversarial-reader
    location: "§1 paragraph 2 ('So read it two-sided from the start:') and §2 ('Hold on to what just happened there:')"
    severity: medium
    severity_under_default_posture: medium
    finding: |
      Check 4 (no meta posturing): FAIL on two spans. Both are reader-instructions — telling
      the reader how to read/what to notice — the judgment-tier form of the banned pattern
      ("read it the way an examiner would", "notice how") that gate_meta's lexicon does not
      catch. "So read it two-sided from the start" instructs the reading posture; "Hold on to
      what just happened there" stages the bold thesis anchor instead of letting it land.
      (Functional attribution labels like "that math is the industry's and this essay's" are
      exempt and NOT flagged here.)
    recommendation: |
      Recast declaratively, preserving the two-sided call and the anchor. §1: "The record is
      two-sided from the start: this is the most concrete piece of after-EMIB-T assembly
      thinking on the public record. It is also a pending application: ..." §2: replace the
      stage direction with a claim, e.g. "That one step moves the dividing line: **the bridge
      stops being part of the board and becomes part of the chip cluster.**"
    quote: "So read it two-sided from the start: ... / Hold on to what just happened there:"

  - finding_id: r1-F6
    pass: pass-6-lead-conclusion-format
    location: "§6 (verdict), paragraph 2, first sentence — the anti-hype guard"
    severity: medium
    severity_under_default_posture: medium
    finding: |
      6G guard-specificity breach (NOT an over-hedged close). The verdict structure complies
      with the firm posture: call first, exactly one guard, limits referenced not re-listed
      ("The limits priced in the previous section stand as written"), closing-binary-test
      landed. But the one guard is phrased as a category truism: "a patent application
      schedules no product" is true of every application ever filed. 6G's hedge budget
      requires the single guard to be specific to THIS patent; the spine's own closing
      directive authorized the this-patent form ("nothing here schedules a product").
      Severity note: kept at medium rather than firm-posture high because the close is not
      over-hedged — the defect is one clause's genericity, and the fix moves no confidence.
    recommendation: |
      Re-point the guard at this filing without changing its weight: "It is one pending
      application, and nothing in it schedules a product." (Do NOT add any further caveat;
      the budget stays at one.)
    quote: "It is one pending application, and a patent application schedules no product."

  - finding_id: r1-F7
    pass: pass-5-reader-perspective
    location: "§1 paragraph 2 (~133 words); §4 EMIB-comparison paragraph (~124 words); also §2 paragraph 3 (~137 words) and §4 glass paragraph (~130 words)"
    severity: medium
    severity_under_default_posture: medium
    finding: |
      5C mobile rendering: four paragraphs exceed the >8-mobile-line threshold (~96 words at
      12 words/line); §1 ¶2 renders ~11 lines on a phone — and it is the lead paragraph that
      must carry the two-sided call. §2 ¶3 and the §4 glass paragraph carry inline verbatim
      quotes + anchors, so the quote-integrated demotion applies to them (treat as low); §1 ¶2
      and the §4 EMIB paragraph contain no patent verbatim and stay at medium.
    recommendation: |
      Split at natural seams; no content changes needed. §1 ¶2: break after "(Google Patents)."
      — gloss+EMIB-T context in one paragraph, the filing + two-sided call in the next (the
      call still lands inside the lead section, so 6A/6H are unaffected). §4 EMIB paragraph:
      break after "(IEEE ECTC paper; see Sources)." — caution + shipped-EMIB flow, then
      EMIB-T + this filing's inversion.

  - finding_id: r1-F8
    pass: pass-5-reader-perspective
    location: "§5, paragraph 1, second sentence"
    severity: medium
    severity_under_default_posture: medium
    finding: |
      Comprehension stumble at the steelman's opening. "its impressive numbers are not where
      this essay may have made them feel" is grammatically broken (numbers are not WHERE
      ... made them FEEL); the reader stalls exactly where the essay needs maximum
      credibility (conceding the objection at full strength). Doubles as an essay-self-
      reference that is not a functional attribution label.
    recommendation: |
      Rewrite plainly, e.g.: "and its impressive numbers do not sit where the previous
      sections may have left the impression they do." Or more direct: "and its impressive
      numbers are not in the claims." The next three sentences already deliver the specifics.
    quote: "its impressive numbers are not where this essay may have made them feel"

  # ---------- LOW ----------

  - finding_id: r1-F9
    pass: pass-3-fact-paraphrase
    location: "§2, paragraph 1, plain-English method sentence, anchor [0061]"
    severity: low
    severity_under_default_posture: low
    finding: |
      Anchor scope: the carrier step (1102) and mold step (1104) live in [0060]; [0061] covers
      only carrier-detach (1106), bridge attach (1108), and test (1110). The sentence's first
      half is anchored one paragraph off. Content is fully in-source; precision only.
    recommendation: |
      Cite both: "...and bond a bridge across the two chips [0060], [0061]" — or move the
      anchor split to match the clauses. ([0060] is within the Phase-1 Layer-2 mechanism span.)

  - finding_id: r1-F10
    pass: pass-3-fact-paraphrase
    location: "§4, claimed-structure paragraph: 'the one quantified-effect sentence in the document'"
    severity: low
    severity_under_default_posture: low
    finding: |
      "[Q]uantified" overstates: [0035]'s effect sentence ("reduces the number of substrate
      routing layers and can improve product yield") contains no quantity. Design artifacts
      call it the only stated yield/effect sentence, not a quantified one. The verbatim quote
      beside it limits the damage, but the label is checkably wrong.
    recommendation: |
      "the one stated-effect sentence in the document" or "the closest thing to a promised
      payoff in the document".

  - finding_id: r1-F11
    pass: pass-3-fact-paraphrase
    location: "§1, paragraph 1, sentence 2"
    severity: low
    severity_under_default_posture: low
    finding: |
      Attribution hygiene at the EMIB fence: "Instead of burying the little bridge die in the
      board and landing the chips on top, the filed method bonds the bridge straight onto the
      chips first [0142]." The contrast clause describes the external EMIB baseline
      (emib-chips-last-flow) but rides a sentence closed by a patent anchor; the patent itself
      never describes the buried-bridge/chips-on-top flow. The fence's letter holds (no EMIB
      term on a [dddd] anchor) and ¶2 sources the baseline properly, but a strict reader could
      attribute the baseline to [0142].
    recommendation: |
      Split so the anchor covers only the patent half: "...the filed method bonds the bridge
      straight onto the chips first, then tests the whole cluster before a board ever enters
      the picture [0142]." with the "instead of burying..." contrast as its own unanchored
      clause/sentence.

  - finding_id: r1-F12
    pass: pass-3-fact-paraphrase
    location: "§5, paragraph 3: 'with the cavity seating one dependent claim away'"
    severity: low
    severity_under_default_posture: low
    finding: |
      The provided patent.md claims section ends at claim 19 (file truncates there); claim 20's
      existence and dependency are verified only via the Example 23 mirror [0144] and the
      Phase-1 Claim scope map. Almost certainly correct, but the run's offline-resolvable
      snapshot cannot show a claim 20.
    recommendation: |
      Confirm claim-20 numbering against the Google Patents record (already tier-1 in Sources),
      or attribute via the Example ("one dependent example away, 'placing the bridge component
      in the cavity' [0144]"). Flag to Phase 0/1: patent.md snapshot may be truncated after
      claim 19.

  - finding_id: r1-F13
    pass: pass-3-fact-paraphrase
    location: "§3, paragraph 3, first fact sentence"
    severity: low
    severity_under_default_posture: low
    finding: |
      "From 2026, Intel has discussed EMIB packages up to roughly 120 by 120 millimeters"
      garbles the log entry (emib-package-roadmap-120mm: Intel AIMS TO ROLL OUT such packages
      from 2026). As written, "From 2026" attaches to "has discussed" (when the discussing
      happened) instead of to the rollout. Weaker-than-source direction, single-outlet label
      present — accuracy of the time reference only.
    recommendation: |
      "Intel has discussed rolling out EMIB packages up to roughly 120 by 120 millimeters from
      2026, carrying as many as twelve HBM memory stacks..."
    related_fact_entry: emib-package-roadmap-120mm

  - finding_id: r1-F14
    pass: pass-1-voice-anti-ai
    location: "essay-wide: five 'this essay' self-references (§3 x1, §4 x1, §5 x3)"
    severity: low
    severity_under_default_posture: low
    finding: |
      Self-reference density. Three instances are functional attribution labels required by
      the grounding rules and exempt ("That math is the industry's and this essay's", "every
      link this essay draws to it rests on timeline and mechanism", "The after-EMIB-T reading
      is this essay's synthesis"). Two are recastable shorthand: "the cavity packages this
      essay has been drawing" and the r1-F8 clause. Not a META-001 pattern; polish.
    recommendation: |
      "the cavity packages described above" for the first; r1-F8's rewrite absorbs the second.
      Leave the three attribution labels alone.

  - finding_id: r1-F15
    pass: pass-5-reader-perspective
    location: "§2, paragraph 3, pitch sentence"
    severity: low
    severity_under_default_posture: low
    finding: |
      Reader-profile rule 2: "1 to 10 microns" gets a definition ("a millionth of a meter")
      but no familiar-scale comparison; a retail reader cannot weigh the magnitude. Minor
      because the draft deliberately deflates the number's claim status a clause later.
    recommendation: |
      Optional one-clause comparison, clearly the essay's: "a human hair is about 70 microns
      across" — keeps the source values verbatim.

  - finding_id: r1-F16
    pass: pass-5-reader-perspective
    location: "§1-§3, first uses of 'substrate'"
    severity: low
    severity_under_default_posture: low
    finding: |
      "Substrate" is never explicitly glossed; the board↔substrate equivalence is left to
      inference ("burying the little bridge die in the board" ¶1 → "package substrate" ¶2 →
      "a board ever enters the picture"). Every other term of art (bridge die, TSV, TGV,
      hybrid bonding, known-good die, cavity) gets its one-clause gloss.
    recommendation: |
      One clause at first §1 use, e.g. "the package substrate, the board-like base the whole
      package is built on". Then use freely.

  - finding_id: r1-F17
    pass: pass-6-lead-conclusion-format
    location: "# Sources, Papers subgroup"
    severity: low
    severity_under_default_posture: low
    finding: |
      Entry quality (enum and subgrouping are compliant; not a 6C/6D fail): "IEEE ECTC 2025,
      EMIB-T conference paper" carries neither authors nor the actual paper title — it is the
      tier-2 backstop for the EMIB-T claims and should be findable from the entry alone. The
      Mahajan IEEE EPS biography is not a paper (categorization follows fact-check-log;
      acceptable, noting for the record).
    recommendation: |
      Resolve the ECTC entry to its real title (and "Last, First, et al." authors if 3+) from
      the ieeexplore record already linked.

  - finding_id: r1-F18
    pass: pass-2-redundancy
    location: "§5, paragraph 4: 'And the names on it are not a side project.'"
    severity: low
    severity_under_default_posture: low
    finding: |
      Loose metonymy (names are not a project); the next sentence carries the actual content.
      The sentence can be cut or tightened with zero information loss.
    recommendation: |
      Cut it (the Mahajan sentence lands harder without the wind-up), or "And the names on it
      are not side-project names."

  # ---------- NO-FINDINGS PASS ENTRIES ----------

  - pass: pass-1-voice-anti-ai
    finding: "no further findings"
    scoped_to: |
      1A cadence judged against deliverable-voice-rules (3-7 sentence paragraphs: verified per
      paragraph, max 7 incl. signature lines; single bold thesis anchor in §2 only; Title Case
      headers consistent). 1B: full banned-word grep re-run (0 hits), banned patterns checked
      (no not-just-X-but-Y; no copula avoidance — draft favors is/sits/lives; no vague
      attribution — external claims all carry named sources; no puffery; no section summaries;
      no elegant variation — filing/document/application alternation judged legitimate common
      nouns, not renamed subjects). Tier-2 tells: one body semicolon (§5 through-via sentence)
      and several announcement-colons, all introducing quotes/translations — below cluster
      threshold, false-positive guard applied. Reader-instruction spans escalated as r1-F5;
      self-reference as r1-F14.

  - pass: pass-2-redundancy
    finding: "no further findings"
    scoped_to: |
      2A: claim-appearance map built for the order/test-gate motif (caption, §1, §2 quotes, §3
      walk, §5 re-pricing, §6 recap) — each recurrence adds a new evidence layer (quote →
      economics → claim scope → verdict); declared signature lines 1-3 excluded from counts
      per thesis-trace; lead→closing recap acceptable. KGD percentages appear once. 2B:
      tightening sweep found only r1-F18. 2C: no paragraph ≥8 sentences (max 7); no >150-word
      paragraph (max ~137, flagged instead under 5C as r1-F7).

  - pass: pass-4-logic-causality
    finding: "no findings"
    scoped_to: |
      4A: all six sections traced against thesis-spine spine→section table; all 4 axes carried
      where declared (Axis 1 §2/§5, Axis 2+4 §4, Axis 3 §3); no out-of-spine claim found
      (the §2 universal-baseline sentence is ruled a pass-3 grounding defect, r1-F1, not a new
      spine element). Sought-vocabulary discipline held throughout ("as filed", "asking for",
      "Every 'locks' above is a lock Intel is asking for"). 4B: causal-language sweep —
      "explains why" (KGD math, mechanism shown and labeled as industry arithmetic), "reads
      like an economic decision" (labeled analysis), "fee money a company does not usually
      spend" (hedged inference, defensible), "The paperwork moved first last time" (factual
      n=1 statement, not asserted as a law). No correlation→causation drift: the EMIB-T link
      is consistently framed as timeline+mechanism synthesis, stated twice explicitly. 4C: arc
      closes — lead tension (news narrative vs filed flow) resolved by §6's order-of-operations
      verdict; closing matches spine's closing-binary-test mapping under Acknowledged residual
      risk + firm posture.

  - pass: pass-5-reader-perspective
    finding: "no further findings"
    scoped_to: |
      5A: hook lands in sentence 1; no 3+ paragraph density wall (§4's mechanism run is broken
      by two captions and re-anchored by "Why rebuild the order at all?" and "Note whose yield
      that is"); closing lands on the thesis, not a new claim. 5B: stake stated at lead end
      (two-sided call), at §3 (substrate economics), §5 (what is actually owned-as-asked), §6;
      closing paragraph reads standalone. Money thread feeds the verdict in every section.
      5C findings consolidated as r1-F7.

  - pass: pass-6-lead-conclusion-format
    finding: "no further findings"
    scoped_to: |
      6A: thesis on the table by sentence 2 of ¶1. 6B: frame closure verified (fifteen-months
      /stage frame returns in §6; closing-binary-test matches spine residual-risk mapping under
      firm posture — not closing-open-question). 6C: 5 categories, all in enum, all-or-nothing
      subgrouping honored. 6D: r1-F17 (entry quality, not the "First, et al." failure form).
      6E: em-dash 0, all inline cites 4-digit, banned-word re-grep clean, # Sources exactly
      once. 6F: title has no em-dash, 51 chars. 6G: verdict leads with the call, limits
      referenced not re-listed, no qualifier-led sentences, no false equivalence; single-guard
      budget respected in count — guard specificity breach filed as r1-F6. 6H: no insurance
      fact precedes the ¶1 discovery beat; first two lines are the discovery. 6I: lead carries
      exactly one status clause (sanctioned); procedure/pricing narration confined to §5
      (single home); §6's "more than paper"/"paperwork moved first" ruled binary-test framing
      and positive-polarity closer, not insurance stacking — spend-motif budget judged held
      (consistent with SURF-005/006 zero-warn).

  - pass: pass-7-adversarial-reader
    finding: "no further findings"
    scoped_to: |
      Check 1 hook: PASS — ¶1 sentence 1 is the discovery beat ("Fifteen months before Intel
      put EMIB-T on a conference stage, a filing from its packaging group had already written
      down a different way..."), declarative, no insurance ahead of it; two-sided call lands
      by lead end ("It is also a pending application: a set of claims Intel is asking for,
      not a product it has scheduled."). Check 2 header-as-claim: PASS — all six headers are
      assertions; header-only skim reconstructs the argument (next flow on file → bridge
      changes sides → test before substrate → power through floor → one claim matters →
      the claim is an order of operations). Check 3 steelman: PASS — THIS-patent objection
      (claim-scope stitching: pitch in description, purpose in description, claim 17 on the
      no-cavity branch, no EMIB anywhere) conceded at full strength ("Now the objection, at
      full strength... No single claim contains the full architecture narrated above."), then
      refined (claim 19 locks the order + test gate); NOT the generic patents-truism. Check 4
      meta: FAIL → r1-F5. Check 5 jargon: PASS — bridge die, TSV, TGV, hybrid bonding, KGD,
      cavity each get one-clause glosses and stay signposts (substrate gap filed as low
      r1-F16). Check 6 stub: PASS — §6 at ~196 words is the closing recap, proportionate; no
      body stub (gate_stub concurs). Check 7 restatement: PASS — non-exempt core-verdict
      assertions in 3 sections (§2 bold anchor, §5 refinement, §6 call); the three declared
      signature lines excluded per thesis-trace.
```
