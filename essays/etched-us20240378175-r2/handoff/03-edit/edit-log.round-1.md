# Edit Log — Round 1 (r2 re-run, reader-first architecture)

```yaml
review_id: etched-0378175-memory-in-writing-r2-editorial-review-1
draft_source: handoff/02-compose/essay-draft.md
publication_source: handoff/02-compose/publication.md
review_timestamp: 2026-07-04T00:00:00Z
review_round: 1
carried_findings: none (round 1; no prior edit-log or revision-response exists)
posture_applied: measured
closing_posture_declared: firm
title_lead_register: discovery (human-selected; executed pair verified against handoff/01-design/title-lead-candidates.md)
overall_assessment: revise-recommended

findings:

  # ---- pass 2 — redundancy + compression ----

  - finding_id: r1-F1
    pass: pass-2-redundancy
    location: "§1 (The Pitch Has a Paper Trail) ¶3; echoes in §5 ¶3 and §6 ¶1"
    severity: low
    severity_under_default_posture: low
    finding: |
      The paying/spending motif is the spine's second axis and most of its recurrences earn
      their place, but §1 ¶3 states it twice inside one paragraph: "Etched has kept paying,
      from the filing fee through the examination it is still in" and, three sentences later,
      "remains a bet the company keeps paying to convert into an asset". Cross-section, the
      §5 ¶3 "the spending is repeated" and §6 ¶1 "defended with repeated spending" are close
      verbal kin. (§5 header and signature line 3 are protected surface and were NOT counted.)
    recommendation: |
      Optional trim: vary the first §1 ¶3 instance, for example "And Etched has paid at every
      step since, from the filing fee through the examination it is still in", keeping the
      paragraph's closing "keeps paying to convert into an asset" (the spine's own phrase).
      No change to §5/§6 required.
    quote: "And Etched has kept paying, from the filing fee through the examination it is still in, to turn that language into property."

  - finding_id: r1-F2
    pass: pass-2-redundancy
    location: "§5 (Etched Keeps Paying to Own It) ¶6, first sentence"
    severity: low
    severity_under_default_posture: low
    finding: |
      "One more registry observation, offered as an observation." repeats "observation"
      within the required labeling device. The label itself is mandated by the edition brief
      (labeled observation) and must stay; the word echo is the only defect.
    recommendation: |
      "One more registry note, offered as an observation." (keeps the mandatory label,
      kills the echo).
    quote: "One more registry observation, offered as an observation."

  - finding_id: r1-F3
    pass: pass-2-redundancy
    location: "three-years motif: §1 ¶1 (surface + signature line 1), §1 ¶3, §2 ¶1, §3 ¶7"
    severity: low
    severity_under_default_posture: low
    finding: |
      The three-year gap (the thesis number) recurs in three body locations beyond the lead
      surface: "Three years in" (§1 ¶3), "Strip away three years of product story" (§2 ¶1),
      "Three years after these paragraphs were filed" (§3 ¶7). Each recurrence does contextual
      work (status, transition, echo dating), so this is acceptable-bridge repetition flagged
      for awareness per 2A, not a defect. Signature line 1's occurrence is exempt and was not
      counted.
    recommendation: |
      No action required. If the composer wants to thin the motif, §2 ¶1 survives as "Strip
      away the product story and the document asks for something easy to picture."

  # ---- pass 3 — claim adequacy + fact verification + paraphrase mutation ----

  - finding_id: r1-F4
    pass: pass-3-fact-paraphrase
    location: "§2 (One Giant Array, Stitched From Identical Chips) ¶1, TPU sentence"
    severity: medium
    severity_under_default_posture: medium
    finding: |
      "Google's TPU ran its matrix unit at exactly 128×128 through the v5p generation" drops
      the qualifier the design bundle's own evidence recorded. search-log.md row 3 captures
      the source as "On most TPU generations up through v5p, the MXU is a 128x128 systolic
      array" ("most", not all); fact-check-log tpu-mxu-128x128 already loosened this to
      "generations through v5p", and the draft hardened it further with "exactly ... through
      the v5p generation". The universal sweep is contradicted by the essay's own first
      Technical specs source: the cited "first Tensor Processing Unit" blog describes the
      original TPU's 256×256 matrix unit (8-bit, not floating point). Dropped-qualifier drift
      that changes scope; classified medium rather than high because the slip is peripheral
      to the thesis (the [0018] industry-ceiling point survives every corrected phrasing
      untouched) and the fix is one clause. Flagging the classification tension explicitly
      for the arbiter rather than auto-escalating.
    recommendation: |
      Narrow the claim to what the sources support. Either restore the qualifier and the
      floating-point scope of the [0018] quote it echoes: "Google's TPU ran its
      floating-point matrix units at 128×128 on generations through v5p, and moved to
      256×256 with Trillium" (the first TPU's 256×256 unit was 8-bit, so the floating-point
      framing is exact), or bound the generations: "from v2 through v5p". Do not add a hedge;
      the sentence stays declarative once narrowed.
    quote: "Google's TPU ran its matrix unit at exactly 128×128 through the v5p generation, and moved to 256×256 with Trillium (Google Cloud TPU documentation)."
    related_fact_entry: tpu-mxu-128x128

  - finding_id: r1-F5
    pass: pass-3-fact-paraphrase
    location: "§2 ¶1, first claims sentence"
    severity: medium
    severity_under_default_posture: medium
    finding: |
      "It claims a package holding many identical chips" puts an embodiment detail under the
      "claims" verb. No claim as drafted requires identical ICs; identicality is [0028]'s
      "In one embodiment, the ICs 215 are all identical." (quoted with the correct register
      three paragraphs later). In a sought-only edition whose controlling discipline is
      claim-register accuracy, the claims verb must not govern description-preference
      content. Direction is narrowing (under-claiming), so no reader is misled about scope
      breadth, but the register conflation is exactly what this edition polices. The §2
      header ("... Stitched From Identical Chips") may stand: it describes the document's
      design story, is embodiment-true, and headers are energy surface, not claim-scope
      statements.
    recommendation: |
      Move "identical" out of the claims clause. For example: "It claims a package holding
      many small chips, each carrying its own modest math array, joined to its neighbors so
      that the whole package computes as one enormous array [0013], [0028]." The
      interchangeability beat already lands verbatim in ¶3 ("The chips are deliberately
      interchangeable: 'In one embodiment, the ICs 215 are all identical.' [0028]").
    quote: "It claims a package holding many identical chips, each carrying its own modest math array, joined to its neighbors so that the whole package computes as one enormous array [0013], [0028]."

  - finding_id: r1-F6
    pass: pass-3-fact-paraphrase
    location: "§5 ¶1 last sentence; §5 ¶3 (\"twice-defended\")"
    severity: medium
    severity_under_default_posture: medium
    finding: |
      "It is the second time the company has chosen to keep spending on this document rather
      than let it lapse" attaches a precise count the registry record undercuts. The bundle's
      prosecution-record fact lists non-final actions 2024-11 and 2025-07 before the final
      rejection; each office action answered is itself a choose-to-spend-or-lapse moment, so
      the RCE is at least the third such choice, not the second. The spine's "twice-made
      spending decision" framed two PHASES (prosecution through final rejection, then the
      RCE); the draft turned phases into a countable event index. A skeptical reader with the
      public file wrapper counts three or more. Same defect in ¶3's "twice-defended". Cross-
      references pass-4B (countable causal-adjacent claim stronger than its evidence).
    recommendation: |
      Narrow the count out or make it exact. Cleanest: "It is not the first time the company
      has chosen to keep spending on this document rather than let it lapse." In ¶3, replace
      "twice-defended" with "repeatedly defended" or "defended past a final rejection"
      (both registry-exact). §6 ¶1's "defended with repeated spending" is already correct;
      leave it.
    quote: "It is the second time the company has chosen to keep spending on this document rather than let it lapse."
    related_fact_entry: prosecution-record

  - finding_id: r1-F7
    pass: pass-3-fact-paraphrase
    location: "§1 ¶3, second sentence"
    severity: medium
    severity_under_default_posture: medium
    finding: |
      "the memory half of Etched's architecture story was in claim language before the
      company had a product name" asserts an external timeline fact (when Etched acquired a
      product name) that has no fact-check-log entry and no source in # Sources. The phrase
      is inherited from Phase 1's insider lead sketch, not from a logged fact. The bundle
      DOES support the adjacent, stronger-for-the-thesis variant: the thread fact has first
      racks shipping summer 2026, so "before there was anything to sell" (§6's own phrasing)
      is record-supported.
    recommendation: |
      Re-anchor to the supported variant: "was in claim language before the company had a
      product to sell" or reuse §6's "before there was anything to sell". Alternatively, log
      the product-name date as a fact with a source in revision; absent that, the unlogged
      claim should not survive.
    quote: "The filing proves authorship: the memory half of Etched's architecture story was in claim language before the company had a product name."

  - finding_id: r1-F8
    pass: pass-3-fact-paraphrase
    location: "§1 ¶2 and §3 ¶7, the \"(TechCrunch, July 2026)\" parentheticals"
    severity: low
    severity_under_default_posture: low
    finding: |
      The inline attributions date TechCrunch's piece to July 2026; the # Sources block and
      the URL date the same article 30 June 2026. The month label "July 2026" for the THREAD
      follows the brief (essay-context and fact thread-claims-2026-07 both call it the July
      2026 thread), but attaching that month to TechCrunch specifically creates a checkable
      inconsistency inside the essay.
    recommendation: |
      Either date the source exactly, "(TechCrunch, 30 June 2026)", or drop the date from the
      parentheticals, "(TechCrunch)", keeping "July 2026" only where it labels the thread per
      the brief. The three-years arithmetic is unaffected either way.
    quote: "every figure the company's own claim (TechCrunch, July 2026)"
    related_fact_entry: thread-claims-2026-07

  - finding_id: r1-F9
    pass: pass-3-fact-paraphrase
    location: "§1 ¶1, second sentence (lead surface; factual anchoring in scope)"
    severity: low
    severity_under_default_posture: low
    finding: |
      "asks for memory channels wired straight into the columns of a giant multi-chip math
      array, no switch in between [0016]" is true of the application as a whole, but the
      single cited anchor [0016] (claim 39's twin) does not carry "giant multi-chip": claim
      39 recites one IC, and the draft itself later trades on exactly that ("it does not
      require the multi-chip package at all"). The multi-chip half of the composite rides on
      [0013] (and [0044]'s column extending through all ICs). Anchoring precision only; no
      factual error at document level, and no style change to the lead is proposed.
    recommendation: |
      Cite the composite honestly: "[0013], [0016]" (or "[0016], [0044]"). No wording change
      needed.
    quote: "US 2024/0378175 A1, filed 10 May 2023, asks for memory channels wired straight into the columns of a giant multi-chip math array, no switch in between [0016]."

  - finding_id: r1-F10
    pass: pass-3-fact-paraphrase
    location: "§3 ¶6, FIG. 4 clause"
    severity: low
    severity_under_default_posture: low
    finding: |
      "a sibling sheet, FIG. 4, redraws the same package with unequal rows and columns" —
      verified against the sheet: FIG. 4 is package 401, a distinct embodiment from FIG. 3's
      package 301 (six ICs versus nine, per [0041]). "The same package" overstates; the same
      DESIGN redrawn is what the record supports.
    recommendation: |
      "a sibling sheet, FIG. 4, redraws the same design with unequal rows and columns" (or
      "shows the unequal-grid variant of the same package idea").
    quote: "and a sibling sheet, FIG. 4, redraws the same package with unequal rows and columns"

  # ---- pass 5 — reader perspective + paragraph readability ----

  - finding_id: r1-F11
    pass: pass-5-reader-perspective
    location: "§5 ¶2 (the bear-case paragraph)"
    severity: medium
    severity_under_default_posture: medium
    finding: |
      127 words in one paragraph with no quote relief renders at roughly 9 to 11 lines on
      mobile (5C threshold: more than 8). It is the steelman, the paragraph a skeptical
      reader most needs to absorb, and it currently reads as a wall. The other long
      paragraphs (§2 ¶1 at 143 words, §3 ¶6 at 147 words) are quote-integrated structures
      and take the posture lens demotion to low; see the no-findings note below.
    recommendation: |
      Split after "...usually the first casualty of examination." Two paragraphs: the
      examiner's record and the breadth risk (sentences 1-4), then claim 39's routine-risk
      and the "early versus original" landing (sentences 5-7). No content change.
    quote: "The bear case is genuinely strong, and it is already on file. [...] The patent office decides whether early also meant original."

  - finding_id: r1-F12
    pass: pass-5-reader-perspective
    location: "§5 ¶6"
    severity: low
    severity_under_default_posture: low
    finding: |
      "no continuation" is the draft's one unglossed term of art. PCT gets its one-clause
      gloss ("the treaty route for filing abroad"); continuation gets none. The "family tree
      is thinner" metaphor partially carries the meaning, which is why this is low rather
      than medium, but the reader profile puts filing-process detail at the reader's lowest
      literacy.
    recommendation: |
      One clause: "and no continuation, the follow-on filing that keeps a patent family
      growing, while the granted trio got both treatments."
    quote: "with no international counterpart under the PCT, the treaty route for filing abroad, and no continuation, while the granted trio got both treatments"

  # ---- passes with no findings (scope proven) ----

  - pass: pass-1-voice-anti-ai
    finding: "no findings"
    scoped_to: |
      Full-text grep of the tier-1 banned list, plain-word swaps, and judgment-tier clusters
      (zero hits); em-dash/en-dash/ellipsis scan (zero); copula-avoidance, not-just-X-but-Y,
      despite-challenges, vague attribution, puffery, section-summary and elegant-variation
      patterns (none); bold budget (exactly one span, the declared signature anchor);
      semicolon audit (all instances inside figure-caption inventories, a verbatim pitch
      quote, or the stripped footnote; none clause-joining body prose); sentence-initial
      "And" and the "Now the pricing." fragment judged deliberate cadence within
      deliverable-voice-rules. Announcement-colon uses are quote lead-ins, enumerations, or
      the translate-then-quote device. Signature lines style-exempt and not sanded.

  - pass: pass-4-logic-causality
    finding: "no findings"
    scoped_to: |
      Spine-to-section trace verified against thesis-spine.md (all four axes carried where
      mapped; no out-of-spine claims; rejected candidates 2 and 3 not revived; §2 held to
      context scale). Causality audit: grant-lien timing stated dates-only with motive
      explicitly labeled inference; drafting-deliberateness attributed to the applicant's
      election; "exists to delete" grounded in [0043]-[0045]; no correlation-to-causation
      drift, no reverse-causation exposure load-bearing for the thesis. The one countable
      overstatement found (the "second time" index) is logged under pass-3 as r1-F6 with a
      4B cross-reference. Lead tension resolves in the closing (stage versus office frame
      closure verified).

  - pass: pass-6-lead-conclusion-format
    finding: "no findings"
    scoped_to: |
      6A lead anchor (tension in sentence 1, patent on the table in sentence 2, thesis by
      ¶1's end); 6B frame closure (closing returns to stage-versus-office; residual risk
      Acceptance maps to closing-binary-test plus docket watch pointer, firm-posture
      conformant); 6C Sources (three enum categories, all-or-nothing subgrouping, six
      entries); 6D N/A (no Papers); 6E mechanical (zero em-dashes; all 37 anchors 4-digit
      and present in invention-summary; banned grep clean; footnotes stripped from
      publication.md; exactly one "# Sources"); 6F title em-dash free, 59 chars, 11 words;
      6G verdict confidence BOTH directions under firm posture (call leads: "The verdict is
      firm. This document is the real origin..."; exactly ONE anti-hype guard and it is
      this-application-specific: racks shipping are not evidence the claims will grant,
      decided against the examiner's eight references; no safe-harbor boilerplate, no
      qualifier-led verdict, no caveat re-listing: the §6 limits clause is a one-breath
      reference to §5, not a re-list; no overreach: "real origin" and "authentically the
      founders' own" are carried by the earliest-filing + inventorship + wiring-half-absence
      record, and §5 separates authorship from originality explicitly); 6H defensive-open
      (see verification notes: PASS, discovery beat first everywhere on the surface).
      "The verdict is firm." evaluated and accepted as the call's frame, not meta
      self-reference.

  - pass: pass-7-adversarial-reader
    finding: "no findings"
    scoped_to: |
      Decomposed checklist run with quoted evidence, both personas (impatient investor,
      skeptical pro-subject reader); see per-pass verdicts table below. Steelman is a
      THIS-application objection at full strength; header-only skim reconstructs the
      argument; thesis restated in exactly 3 non-exempt sections; no stub; no reader
      instruction; jargon gloss coverage complete except "continuation" (logged as r1-F12
      under pass-5).
```

## Per-pass verdicts

| Pass | Verdict | Notes |
|---|---|---|
| 1 voice + anti-AI | clean | zero banned hits; one bold span (declared anchor); cadence within rules |
| 2 redundancy | 3 low | paying-motif double in §1 ¶3; "observation" echo; three-years awareness (acceptable bridges) |
| 3 fact + paraphrase | 4 medium, 3 low | TPU qualifier drop (r1-F4); claims/embodiment register (r1-F5); "second time" undercount (r1-F6); unlogged product-name claim (r1-F7); date-consistency, composite anchor, FIG. 4 wording lows |
| 4 logic + causality | clean | spine trace intact; labeled-inference discipline exemplary; r1-F6 cross-noted |
| 5 reader perspective | 1 medium, 1 low | §5 ¶2 mobile wall (split); "continuation" gloss |
| 6 lead/closing + format | clean | 6G clean both directions under firm; 6H PASS; mechanicals re-verified independently of gates |
| 7 adversarial reader | clean | checklist below |

### Pass-7 checklist (verdict, evidence)

1. **Hook check** — PASS. ¶1 sentence 1 lands the discovery beat declaratively, nothing queues ahead of it: "Three years before Etched pitched 'the best layer is no layer' as its memory philosophy on stage, both of its co-founders had signed that idea into the company's very first patent filing." Insurance arrives only in ¶1's last sentence ("...still hasn't said yes to it", the declared signature line). Full two-sided call lands by the lead's end: §1 ¶3 "The filing proves authorship... And Etched has kept paying... What the filing is not, yet, is the property itself... down to the borrowing secured against the patent stack this filing belongs to."
2. **Header-as-claim** — PASS. Skim skeleton: paper trail → one giant array from identical chips → memory claims delete the switch → math that forgets, sidecar remembers → Etched keeps paying to own it → an asset in formation. The argument reconstructs from headers alone.
3. **Steelman** — PASS. §5 ¶2 concedes at full strength ("The bear case is genuinely strong, and it is already on file... eight references... claim 1... reads on more or less any multi-chip systolic-array package... Even claim 39's distinctive absence... could yet be judged routine for weight-stationary designs"), then refines (¶3, record of behavior). THIS-application objection, not a truism; no generic patent truism spent anywhere.
4. **No meta posturing** — PASS. "offered as an observation" and "with its label attached" are edition-mandated functional labels (labeled-observation/inference requirements), exempt. "The verdict is firm." is the call's frame, not a reader instruction.
5. **Jargon as signpost** — PASS with one gap: systolic array, HBM, independent claim, RCE, security interest, PCT, weight-stationary, layer normalization all get one-clause glosses; "continuation" does not (r1-F12, low).
6. **No stub/rhythm break** — PASS. Section words 271/477/737/449/555/237; the short closer is conventional and lands the frame.
7. **Thesis not over-restated** — PASS. Non-exempt verdict assertions in exactly 3 sections (§1 ¶3, §5 ¶3, §6 ¶1); the three declared signature lines verified as exact strings in the draft and excluded from the count.

## Verification notes (falsifiable record)

- **Three-years consistency (composer's declared deviation 1) — VERIFIED CORRECT.** Filed
  2023-05-10 (patent.md, invention-summary); stage thread July 2026 (fact
  thread-claims-2026-07; TechCrunch URL 2026-06-30). Gap = 3 years 2 months; every temporal
  expression audited: "Three years before" (¶1), "three years older" (signature 1),
  "Three years in" (§1 ¶3), "three years of product story" (§2 ¶1), "Three years after these
  paragraphs were filed" (§3 ¶7), cover caption "July 2026 / dated May 2023", "this summer"
  (§6, = summer 2026), grants 15 July 2025 + lien effective 18 July 2025 = "three days
  later" (correct). Zero "two years" strings remain. The design bundle's "two years" was
  internally contradictory (spine one-liner said both "two years before" and "three years of
  examination later"); the deviation is accuracy-first and endorsed. Residue: the bundle's
  reader_sentence still says "two years" — a Phase-1 artifact, not a draft defect.
- **6H defensive-open — PASS.** No insurance fact precedes the discovery beat in the title,
  cover caption, ¶1, or headers; ¶1's order is beat → filing facts → stage date → priced
  last. First-two-lines test passes (beat starts at word one). Cover caption is
  discovery-shaped, 3 reference numerals (510/520/515), within the ≤6 budget even counting
  year tokens.
- **FIG. 6 manifest defect — CHECKED WITH OWN EYES.** fig-06.png shows 605A-D INSIDE ICs
  615A-D beside tiles 220, and 610A-D as small boxes OUTSIDE the ICs, coupled to the 605s;
  dashed 650 boundary encloses only the 220 tiles. The draft caption follows the spec-correct
  labels; the manifest's swapped line did NOT leak. FIG. 1/2/3/4/5/7 captions and the §3
  FIG. 5 walk (two memory chips, four channels, four columns) also verified against the
  images; FIG. 7's Time B stall matches [0057].
- **Quote byte-checks — ALL 25 patent-text quotes verified** as substrings of both
  invention-summary rows and patent.md under gate_quotes' sanctioned normalization (the
  patent file uses NBSP before reference numerals; wording identical). The [0045] "220and"
  run-on correctly avoided by clean-substring quoting. Thread quotes ("the best layer is no
  layer", "$1B+ contracts", "$800m raised", the full pitch line) verified verbatim against
  fact-check-log. All 37 [dddd] anchors present in invention-summary.
- **Edition discipline — VERIFIED.** Application-era verbs throughout (asks for / claims /
  seeks / as drafted); no enforceability language; exactly ONE dated prosecution label
  sentence (§5 ¶1) and both-or-neither satisfied (label + liens in the same section);
  collateral kept portfolio-scope with reel/frames 067204/0877 and 071792/0869, effective
  (not recordation) dates, blanket-lien discipline stated in terms ("Both liens are blanket,
  selecting nothing and saying nothing about any single filing's worth"); tier-5
  third-party-sohu-linkage not used; LVI absence carried with the 18-month caveat;
  description-only labels on the preset loop and all FIG. 7 material, in prose AND caption.
- **Composer deviations 2-5 (thesis-trace) — reviewed and accepted**: [0021] in §2 (needed
  by the FIG. 1 walk, anchor valid); FIG. 4 prose clause (grounded in the variant-pair row;
  wording low-flagged as r1-F10); wiring-half continuity as one reference at §2's end;
  prosecution-label discipline as executed.

## Overall assessment

**revise-recommended** — zero critical, zero high, five medium (r1-F4, r1-F5, r1-F6, r1-F7,
r1-F11), seven low. One-line rationale: the draft's grounding spine, verdict symmetry (6G),
and hook-first surface (6H) are clean under the firm posture, but four precision slips
(a dropped source qualifier on the TPU fact, one claim/embodiment register blur, one
undercounted prosecution index, one unlogged external claim) and one mobile-wall paragraph
sit exactly where this essay's registry-grade credibility lives and should be fixed before
publication. No hard-gate trigger: no pass-3 high/critical, gates all pass, verdict and lead
conform to the firm posture.
