# Edit Log — Round 2 (r2 re-run, reader-first architecture)

```yaml
review_id: etched-0378175-memory-in-writing-r2-editorial-review-2
draft_source: handoff/02-compose/essay-draft.md (draft_version 2)
publication_source: handoff/02-compose/publication.md
review_timestamp: 2026-07-04T13:15:00Z
review_round: 2
reviewer_context: fresh (no memory of round 1; round-1 artifacts read as inputs per re-review protocol)
carried_findings: r1-F1..r1-F12 (5 medium, 7 low) — all ruled below BEFORE new-finding hunt
gate_result_read: handoff/03-edit/gate-result.round-2.json (14/14 PASS, zero findings incl. warns)
posture_applied: measured
closing_posture_declared: firm
title_lead_register: discovery (human-selected pair; executed title verified byte-identical to the selected candidate, 59 chars / 11 words)
overall_assessment: revise-recommended

findings:

  # ---- carried-finding rulings are in the lifecycle section below (none re-asserted) ----

  # ---- NEW findings, round 2 ----

  - finding_id: r2-F1
    pass: pass-3-fact-paraphrase
    location: "§6 (An Asset in Formation) ¶2, last sentence"
    severity: medium
    severity_under_default_posture: medium
    finding: |
      "That question gets decided against the examiner's eight references, nowhere else"
      turns a dated registry snapshot into the closed universe of a future decision. The
      count of eight is registry-true as of the May 2026 record (fact examiner-art-8refs,
      anchored in §5 ¶1's "As of the May 2026 record"), but the same record says
      examination is CONTINUING after an RCE with a third non-final action issuing — the
      reference set is open, and RCE prosecution routinely adds art. "Eight ... nowhere
      else" is a forward-exhaustive countable claim the record does not support; it can be
      falsified by the very docket §6 ¶3 tells the reader to watch. Same defect class as
      r1-F6 (a precise count stronger than its registry evidence), sitting in the verdict
      section where this essay's registry-grade credibility is most exposed. Secondary:
      re-citing the "eight" figure here also re-lists a §5 detail inside the verdict (6G
      prefers state-once-then-reference); one fix clears both. The design bundle's own
      guard phrasing is already the narrow version ("the examiner-cited field is where
      that gets decided" — essay-context.md, thesis-spine closing posture).
    recommendation: |
      Narrow the claim; do not hedge it and do not soften "nowhere else" (the stage-vs-
      office punch is the guard working). Options, best first:
      (a) "That question gets decided at the patent office, against the examiner's cited
          art, nowhere else." (venue carries "nowhere else"; count dropped)
      (b) "That question gets decided against the examiner's citations, nowhere else."
      (c) Keep the count but date it — weakest option, adds a clause the verdict does not
          need. The sentence stays declarative in every variant.
    quote: "That question gets decided against the examiner's eight references, nowhere else."
    related_fact_entry: examiner-art-8refs

  - finding_id: r2-F2
    pass: pass-2-redundancy
    location: "§5 (Etched Keeps Paying to Own It) ¶4, sentences 4 and 6"
    severity: low
    severity_under_default_posture: low
    finding: |
      Revision-introduced echo (a side effect of the r1-F6 fix, which is otherwise
      correct): sentence 4 now reads "examination has been paid for through a rejection
      and past it" and sentence 6 lands on "defended past a final rejection" — the same
      fact (spending continued past the final rejection) with a shared "past + rejection"
      core, twice inside one paragraph, two sentences apart. The composer's note shows the
      wording was chosen to avoid a repeated/repeatedly stack; the trade bought a
      rejection/past stack instead. Minor; the landing sentence is the paragraph's summary
      device and should keep "defended past a final rejection" (registry-exact).
    recommendation: |
      Optional. Vary sentence 4, keeping the colon device: "And the spending is repeated:
      examination has been paid for through a rejection and beyond it." (or "...through
      one rejection and after it"). Leave sentence 6 untouched.
    quote: "And the spending is repeated: examination has been paid for through a rejection and past it. [...] A signed, dated statement of the architecture, defended past a final rejection, is evidence about the company, whatever the office eventually says about the field."

  # ---- passes with no findings (scope proven) ----

  - pass: pass-1-voice-anti-ai
    finding: "no findings"
    scoped_to: |
      Mechanical grep re-run on draft_version 2 (falsifiable, commands on record): tier-1
      banned words + plain-word-swap gated terms — zero hits; em-dash/en-dash/ellipsis —
      zero; exclamation marks, Latin abbreviations, emoji — zero; not-just-X-but-Y,
      despite-challenges, copula-avoidance (serves as/stands as/represents/constitutes),
      vague attribution, puffery, section-summary openers, Furthermore/Moreover/sentence-
      initial-Additionally — zero. Bold audit: exactly one span, the declared signature
      line 2 (thesis anchor). Semicolon audit: 5 hits — FIG. 2/3/6 caption inventories,
      the verbatim pitch quote ("each memory layer adds latency; the best layer is no
      layer"), and the footnote stripped from publication.md; none clause-joining body
      prose. Sentence-initial "And" (4×) and the "Now the pricing." fragment judged
      deliberate cadence within deliverable-voice-rules. Announcement-colons are quote
      lead-ins, the "Translated:" translate-then-quote device (reader-profile rule 3), or
      the §5 ¶4 parallel record enumeration (complete clauses before each colon).
      "Document/filing/application" alternation checked against the elegant-variation rule:
      natural patent register, not epithet renaming. Revision deltas (r1-F4 TPU sentence,
      r1-F5 clause, r1-F6 rephrase, r1-F12 gloss split) re-checked for introduced tells:
      none. Signature lines style-exempt and not sanded.

  - pass: pass-3-fact-paraphrase
    finding: "one finding (r2-F1 above); everything else verified"
    scoped_to: |
      All 26 patent-text quote spans byte-checked directly against input/patent.md and
      invention-summary rows (independent of gate_quotes): all clean substrings, incl. the
      [0045] split-quote that correctly bridges the source's "220and" run-on outside
      quotation marks, and the [0040] quote ending before the "215in" run-on. All 26
      distinct [dddd] anchors resolve to invention-summary spans/rows; paraphrase checks on
      every anchored non-quoted sentence (claim-39 translation vs claim text; claim 15 via
      [0014]; claims 11-13 vs claim text; [0021]/[0024]/[0038]/[0039] mechanism
      paraphrases; [0037] concession) — no drift, no fact introduction. Register
      discipline: application-era verbs on every claim statement ("asks for / claims /
      seeks / as drafted"); grant-era language appears only for the actually-granted
      12,361,091 wiring half; no enforceability language. External facts: thread figures
      attributed "the company's own claim / the company says" on every use; CSM expansion
      press-labeled; lien-1/lien-2 with effective (not recordation) dates and reel/frames
      exact; grant-lien timing dates-only with inference labeled; family-us-only labeled
      observation; examiner-art-8refs exact in §5 (the §6 reuse is r2-F1); LVI absence with
      the 18-month caveat; tier-5 sohu-linkage unused. Essay-own comparisons verified
      arithmetic: 128×128 ≈ "roughly sixteen thousand multipliers" (16,384); 1 TB/s ≈ "a
      feature film's worth of data every five thousandths of a second" (5 GB per 5 ms).
      TPU sentence re-verified against fact tpu-mxu-128x128 and both logged sources
      (floating-point scope correctly excludes the 8-bit 256×256 first-gen TPU; Trillium
      256×256 exact). FIG. 5/6 captions and the §3 FIG. 5 walk re-verified against the
      images with own eyes: fig-06.png shows 605A-D INSIDE ICs 615A-D beside 220 tiles,
      610A-D outside coupled to the 605s, dashed 650 enclosing only the tiles — the
      manifest's swapped 605/610 line did NOT leak; fig-05.png shows 2 memory chips, 4
      channels, 4 columns, wires only. FIG. 1/2/3/7 captions also image-verified (FIG. 3:
      six memory chips 305A-F across the top; FIG. 7 stall band at Time B per [0057]).

  - pass: pass-4-logic-causality
    finding: "no findings"
    scoped_to: |
      Spine→section trace re-walked on draft_version 2: all four axes carried where mapped
      (Axis 1 §3 + lead gloss; Axis 2 §2/§3; Axis 3 §3; Axis 4 §1/§2/§3/§5); no
      out-of-spine claims; rejected candidates 2 and 3 not revived (§2 stays context-scale;
      §4 stays description-labeled mechanism color). Causality audit: grant-lien timing
      dates-only + labeled inference; drafting-deliberateness attributed to the applicant's
      election (an act the record shows); "exists to delete" grounded in [0043]-[0045];
      "not the first time" now matches the choice-point record (r1-F6 fix verified); no
      correlation→causation drift; the CSM echo stays an echo ("Whether the racks ...
      practice these claims is invisible from the patent record"). Lead tension resolves in
      the closing (stage-vs-office frame closure). The one countable-claim defect found
      this round is logged under pass-3 as r2-F1 (4B cross-reference: a forward claim
      stronger than its evidence).

  - pass: pass-5-reader-perspective
    finding: "no findings"
    scoped_to: |
      Engagement curve re-read as the profile reader: hook in sentence 1, money stakes by
      ¶2, every mechanism section surfaces back to the bet (§2 → wiring-half/memory-half
      stakes; §3 → CSM echo; §4 → "architecture bet in its purest form" + budgeted-idle-
      cycles landing feeding §5's record-of-behavior). Jargon gloss coverage now complete:
      systolic array, HBM, independent claim, RCE, security interest, blanket lien, PCT,
      continuation (r1-F12 fix verified), weight-stationary, layer normalization,
      transformer all one-claused; no deep-dives (UCIe/interposer/GT-s absent from prose).
      Mobile 5C re-measured post-split: §5 ¶2 now 80 words (~6.7 lines) and ¶3 47 words
      (~3.9 lines) — the r1-F11 wall is cleared with zero content change. Remaining
      marginal overruns measured and accepted: §2 ¶1 (~140 w) and §3 ¶6 (~135 w) are
      quote-integrated structures (posture-lens demotion, consistent with round 1); §5 ¶4
      (103 w, ~8.6 lines) and ¶5 (109 w, ~9.1 lines) are marginal on a 12-words-per-line
      estimate, internally signposted, and unchanged text round 1 reviewed — splitting ¶5
      would orphan the lien/label cohesion the both-or-neither rule wants. §3 ¶7 (116 w,
      7 sentences, quote-integrated) checked and accepted at the band edge. Stake clarity:
      closing paragraph reads standalone.

  - pass: pass-6-lead-conclusion-format
    finding: "no findings (r2-F1's verdict-precision defect is a pass-3 grounding item; 6G/6H both PASS)"
    scoped_to: |
      6A lead anchor (discovery beat sentence 1; patent + filing date sentence 2; thesis by
      ¶1's end). 6B frame closure (stage-vs-office returns in §6; residual risk Acceptance
      → closing-binary-test + docket watch pointer, firm-conformant). 6C Sources: three
      enum categories (Patents 2, News & media 2, Technical specs 2), six entries,
      subgrouped all-or-nothing. 6D N/A (no Papers). 6E re-verified independently of
      gate-result.round-2.json: zero em-dashes; all 26 anchors 4-digit and resolving;
      banned grep clean; publication.md byte-identical to draft body minus
      frontmatter/footnotes (programmatic diff, True) with no footnote defs; exactly one
      "# Sources". 6F title: colon-free, em-dash-free, 59 chars. 6G under firm posture,
      BOTH directions: call leads ("The verdict is firm. This document is the real origin
      of Etched's memory story."); not qualifier-led; exactly ONE anti-hype guard and it is
      this-application-specific (racks are not evidence the claims will grant); no
      safe-harbor boilerplate; the §6 "can shrink or die" clause is the call's own second
      half per the spine's two-sided shape, not a caveat re-list (no dates or references
      re-narrated — except the "eight references" number, handled under r2-F1 as the
      grounding fix); no overreach: "real origin" / "authentically the founders' own" carried
      by earliest-filing + inventorship + wiring-half-absence, with §5 ¶3 separating
      authorship from originality. 6H: no insurance fact precedes the discovery beat in
      title, cover caption, ¶1, or headers; ¶1 order = beat → filing facts → stage date →
      priced last (the signature line); first-two-lines test passes (beat starts at word
      one); cover caption discovery-shaped, 5 numeral tokens (510/520/515/2026/2023) ≤ 6
      budget; no gap-framed headers.

  - pass: pass-7-adversarial-reader
    finding: "no findings"
    scoped_to: |
      Decomposed checklist re-run fresh with quoted evidence, both personas; see table
      below. Steelman is the THIS-application objection at full strength (eight references,
      claim-1 breadth, claim-39 routine-risk for weight-stationary designs), then refined
      by the record of behavior; no generic patent truism anywhere. Header-only skim
      reconstructs the argument. Non-exempt verdict assertions in exactly 3 sections
      (§1 ¶3, §5 ¶4, §6 ¶1); the three declared signature lines verified present as exact
      strings (1 occurrence each) and excluded from the count. No stub (§6 at 237 words is
      the conventional closer and lands the frame). No reader instruction; "offered as an
      observation" / "with its label attached" are edition-mandated evidence labels;
      "The verdict is firm." re-evaluated fresh and accepted as the call's frame. Jargon
      signposts hold under the impatient-investor read; the only ungrounded-jargon
      candidate, PCIe, appears solely as a FIG. 2 caption inventory label (below finding
      threshold).
```

## Disposition-verification table (round-1 → draft_version 2)

| ID | r1 severity | Disposition claimed | Verified in draft? | Evidence (current text) | Ruling |
|---|---|---|---|---|---|
| r1-F1 | low | applied | YES | §1 ¶3: "And Etched has paid at every step since, from the filing fee through the examination it is still in, to turn that language into property." Paragraph closer "keeps paying to convert into an asset" retained. | closed-verified |
| r1-F2 | low | applied | YES | §5 ¶7: "One more registry note, offered as an observation." Echo dead; mandatory label intact. | closed-verified |
| r1-F3 | low | no action (per reviewer's primary recommendation) | YES | §2 ¶1 still opens "Strip away three years of product story..." — acceptable-bridge repetition stands; optional thinning declined with reasoning (motif churn). | closed-accepted |
| r1-F4 | medium | applied (narrow, option a) | YES | §2 ¶1: "Google's TPU ran its floating-point matrix units at 128×128 on generations through v5p, and moved to 256×256 with Trillium (Google Cloud TPU documentation)." Matches fact tpu-mxu-128x128; "exactly ... through the v5p generation" hardener gone; floating-point scope correctly excludes the 8-bit 256×256 first-gen TPU (the essay's own first Technical specs source); sentence stays declarative, no hedge. Residue grep for "exactly 128": zero. | closed-verified |
| r1-F5 | medium | applied (narrow) | YES | §2 ¶1: "It claims a package holding many small chips, each carrying its own modest math array... [0013], [0028]." "Identical" no longer under the claims verb; [0028] still carries host-sees-one-array (q-0028-1); identicality lands 3 paragraphs later on the embodiment register ("In one embodiment, the ICs 215 are all identical." [0028]); §2 header stands per the r1 carve-out ("small/modest" is [0001]/[0028]-grounded "smaller" framing, checked). | closed-verified |
| r1-F6 | medium | applied (narrow, de-precision) | YES | §5 ¶1: "It is not the first time the company has chosen to keep spending on this document rather than let it lapse." §5 ¶4: "A signed, dated statement of the architecture, defended past a final rejection, is evidence about the company..." Both registry-exact against prosecution-record (non-finals 2024-11/2025-07 before the final rejection → "not the first time" true; RCE = spend past final rejection). "second time"/"twice-defended" residue grep: zero. §6 ¶1 "defended with repeated spending" untouched per the r1 instruction; "twice pledged" separately verified against the two liens. The "signed, dated" inversion avoids a DUPE 5-gram with §6 as the composer argued (checked). Side effect: a new low-grade "past + rejection" echo inside ¶4 → logged as r2-F2, not a re-assertion. | closed-verified |
| r1-F7 | medium | applied (anchor) | YES | §1 ¶3: "was in claim language before the company had a product to sell." — the r1 recommendation's first option verbatim, riding fact thread-claims-2026-07 (first racks summer 2026); the unlogged "product name" claim is gone (residue grep zero). The non-verbatim variant vs §6's "before there was anything to sell" is deliberate DUPE avoidance; same record support, accepted. | closed-verified |
| r1-F8 | low | applied (option 2) | YES | Both parentheticals now "(TechCrunch)" (§1 ¶2, §3 ¶7); "TechCrunch, July 2026" residue zero; "July 2026" remains only as the thread/stage label per the brief; exact article date (30 June 2026) lives in # Sources. | closed-verified |
| r1-F9 | low | applied | YES | §1 ¶1: "...no switch in between [0016], [0044]." Composite honestly cited ([0016] no-switch channel-to-column; [0044] column through all ICs); zero wording change to the lead surface; thesis-trace §1 anchor list synced (checked). | closed-verified |
| r1-F10 | low | applied | YES | §3 ¶6: "a sibling sheet, FIG. 4, redraws the same design with unequal rows and columns" — "design" not "package" (FIG. 4 = package 401, distinct embodiment per [0041]); figures-rationale + thesis-trace deviation 3 synced (checked). | closed-verified |
| r1-F11 | medium | applied (structural split) | YES | §5 ¶2 now ends "...usually the first casualty of examination." (80 words, ~6.7 mobile lines); new ¶3 "Even claim 39's distinctive absence... whether early also meant original." (47 words, ~3.9 lines). Content byte-preserved across the split; §5 re-counted at 7 paragraphs, all 3-7 sentences; no figure tokens in §5, figure set/positions unchanged; downstream renumbering consistent with the composer's recount. Neighbor regression check: ¶4-¶7 text unchanged. | closed-verified |
| r1-F12 | low | applied (+ sentence split for length) | YES | §5 ¶7: "This application is US-only, with no international counterpart under the PCT, the treaty route for filing abroad. It has no continuation either, the follow-on filing that keeps a patent family growing, while the granted trio got both treatments." Gloss present; both sentences inside the length band; paragraph 4 sentences. | closed-verified |

**Surface confirmation cross-check:** title, cover caption, all six headers, the three
signature lines (exact-string count = 1 each), and §6 verified against the composer's
byte-identical claim; the only lead-surface delta is the r1-F9 citation token, as declared.

## Finding-id lifecycle (round 1 → round 2)

- **Closed, fix verified in text:** r1-F1, r1-F2, r1-F4, r1-F5, r1-F6, r1-F7, r1-F8,
  r1-F9, r1-F10, r1-F11, r1-F12 (11 of 12).
- **Closed, no-action accepted:** r1-F3 (the round-1 recommendation itself was "no action
  required"; the declined optional thinning is reasoned and accepted).
- **Re-asserted:** none. **Dropped silently:** none.
- **New this round:** r2-F1 (medium, pass-3), r2-F2 (low, pass-2 — revision-introduced
  echo adjacent to the r1-F6 fix, logged as new rather than reopening r1-F6 because the
  r1-F6 defect itself is fixed).

## Per-pass verdicts

| Pass | Verdict | Notes |
|---|---|---|
| 1 voice + anti-AI | clean | greps re-run on v2: zero banned hits; one bold span (declared anchor); semicolons all in captions/quote/footnote; revision deltas introduced no tells |
| 2 redundancy | 1 low | r2-F2 "past + rejection" echo inside §5 ¶4 (side effect of r1-F6 fix); paying-motif and three-years motif re-checked, still acceptable bridges |
| 3 fact + paraphrase | 1 medium | r2-F1 forward-exhaustive "eight references, nowhere else" in the verdict; all 26 quotes byte-verified vs patent.md; all r1 grounding fixes landed |
| 4 logic + causality | clean | spine trace intact on v2; labeled-inference discipline holds; r2-F1 cross-noted (4B: claim stronger than evidence) |
| 5 reader perspective | clean | r1-F11 wall cleared (80w/47w); r1-F12 gloss verified; marginal mobile overruns measured and accepted with reasons |
| 6 lead/closing + format | clean | 6G clean both directions under firm; 6H PASS (beat first everywhere on the surface); mechanicals re-verified independently of gates; publication.md identity proven |
| 7 adversarial reader | clean | checklist below; both personas |

### Pass-7 checklist (verdict, evidence)

1. **Hook check** — PASS. ¶1 sentence 1 lands the discovery beat declaratively, nothing
   queues ahead: "Three years before Etched pitched 'the best layer is no layer' as its
   memory philosophy on stage, both of its co-founders had signed that idea into the
   company's very first patent filing." Insurance arrives only in ¶1's final signature
   sentence. Second half verified: the full two-sided call lands by the lead's end (§1 ¶3:
   authorship + "has paid at every step" VERSUS "not, yet, the property itself" + the
   collateral preview clause).
2. **Header-as-claim** — PASS. Skim skeleton: pitch has a paper trail → one giant array
   from identical chips → memory claims delete the switch → math that forgets, sidecar
   remembers → Etched keeps paying to own it → an asset in formation. Argument
   reconstructs from headers alone; none gap-framed.
3. **Steelman** — PASS. §5 ¶2-¶3 concede at full strength ("The bear case is genuinely
   strong, and it is already on file... eight references... reads on more or less any
   multi-chip systolic-array package... could yet be judged routine for weight-stationary
   designs"), then ¶4 refines with the record of behavior. THIS-application objection; no
   truism spent anywhere.
4. **No meta posturing** — PASS. Edition-mandated evidence labels exempt; "The verdict is
   firm." accepted as the call's frame, not a reader instruction; zero "this essay"
   self-reference.
5. **Jargon as signpost** — PASS. All terms of art one-claused (continuation now included
   per r1-F12); no doctrinal deep-dives.
6. **No stub / rhythm break** — PASS. Section words ~274/477/735/449/571/237; the short
   closer is conventional and lands the frame.
7. **Thesis not over-restated** — PASS. Non-exempt verdict assertions in exactly 3
   sections (§1 ¶3, §5 ¶4, §6 ¶1); the 3 declared signature lines are present as exact
   strings and exempt.

## Verification notes (falsifiable record, round 2)

- **Quote byte-checks re-run from scratch** — all 26 patent-text quotes verified as clean
  substrings of input/patent.md directly (not only via invention-summary), including the
  [0045] split around "220and" and the [0040] cut before "215in". Thread quotes verified
  against fact-check-log verbatims.
- **Figure truth re-checked with own eyes** — fig-05.png and fig-06.png re-read; FIG. 6
  caption follows the spec-correct labels (605 aux inside ICs 615; 610 memory outside;
  650 encloses only tiles); the Phase-0 manifest defect did not leak. FIG. 1/2/3/7
  captions image-verified; FIG. 4 correctly unplaced with one honest prose clause.
- **Publication integrity** — programmatic check: publication.md == essay-draft.md minus
  frontmatter and footnotes (True); no footnote definitions in publication.md.
- **Mobile/structure metrics** — §5 paragraph metrics measured (words/sentences/estimated
  lines) post-split; every paragraph in the document within the 3-7 sentence band (the two
  2-sentence quote-follower units in §2 read as quote-integrated cadence, accepted).
- **Edition discipline re-verified on v2** — application-era verbs throughout; exactly ONE
  dated prosecution label sentence (§5 ¶1); both-or-neither satisfied (label + liens in
  §5); effective dates + reel/frames exact; blanket-lien discipline in terms; tier-5 fact
  unused; LVI absence with the 18-month caveat; description-only labels on the preset loop
  and all FIG. 7 material in prose AND caption.
- **Register/three-years audit** — "three years" consistent everywhere (2023-05-10 →
  July 2026 thread); zero "two years" residue; grants 15 July 2025 + lien effective
  18 July 2025 = "three days later" correct.

## Overall assessment

**revise-recommended** — zero critical, zero high, one medium (r2-F1), one low (r2-F2).

Disposition verification: **all 12 round-1 findings closed** (11 fixes verified in the
current text with quotes above; 1 no-action accepted); no id dropped, none re-asserted;
the low sweep did not regress any neighbor except the minor ¶-internal echo logged as
r2-F2.

One-line rationale: draft_version 2 is grounding-clean, verdict-symmetric (6G), and
hook-first (6H) under the firm posture, and every round-1 finding landed as described;
the one remaining medium is a single forward-exhaustive count in the verdict's anti-hype
guard ("eight references, nowhere else") that the open RCE record cannot support — a
one-clause narrow (the spine's own phrasing) with no hedging and no change to the call.

**Not a clean round**: one medium finding stands, so this round does NOT count toward
double-clean. Expected next: composer revision-mode disposition on r2-F1 (r2-F2 optional),
then a fresh round-3 review. No hard-gate trigger: r2-F1 is pass-3 medium (not
high/critical), gates are 14/14 PASS, and the verdict/lead conform to the firm posture.
