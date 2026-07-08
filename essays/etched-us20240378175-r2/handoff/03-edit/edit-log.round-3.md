# Edit Log — Round 3 (r2 re-run, reader-first architecture)

```yaml
review_id: etched-0378175-memory-in-writing-r2-editorial-review-3
draft_source: handoff/02-compose/essay-draft.md (draft_version 3)
publication_source: handoff/02-compose/publication.md
review_timestamp: 2026-07-04T13:45:00Z
review_round: 3
reviewer_context: fresh (no memory of rounds 1-2; round-1/2 artifacts read as inputs per re-review protocol)
carried_findings: r2-F1 (medium), r2-F2 (low) — ruled below BEFORE new-finding hunt; r1-F1..r1-F12 lifecycle re-confirmed on v3
gate_result_read: handoff/03-edit/gate-result.round-3.json (14/14 PASS, zero findings incl. warns)
posture_applied: measured
closing_posture_declared: firm
title_lead_register: discovery (human-selected pair; executed title verified byte-identical to the selected candidate in title-lead-candidates.md, 59 chars / 11 words)
overall_assessment: pass

findings:

  # ---- carried-finding rulings are in the disposition/lifecycle sections below ----
  # ---- (r2-F1 closed-verified, r2-F2 closed-verified; no re-assertions) ----

  # ---- NEW findings, round 3 ----

  - finding_id: r3-F1
    pass: pass-5-reader-perspective
    location: "§6 (An Asset in Formation) ¶2, last sentence"
    severity: low
    severity_under_default_posture: low
    finding: |
      Revision-introduced clarity wrinkle (side effect of the r2-F1 fix, which is otherwise
      correct and verified): "the examiner's cited art" is now the draft's one unglossed
      term of art. "Art" in the prior-art sense sits at the reader profile's LOWEST literacy
      area (filing-process detail; rule 1: every term of art gets a one-clause gloss on
      first use), and this is its only occurrence — first use, in the verdict section. The
      referent IS supplied one section earlier (§5 ¶2 "The examiner has assembled eight
      references against this application, drawn from... a crowded field"), which mostly
      carries the meaning by back-reference; that is why this is low, not medium. Same
      defect class and severity as r1-F12 (unglossed "continuation", low). The sentence's
      grounding is sound (see r2-F1 ruling); this is vocabulary only.
    recommendation: |
      Optional. If touched, swap the noun, keep everything else byte-identical — the
      round-2 log's own option (b) noun works and was already judged supportable:
      "That question gets decided against the examiner's citations, nowhere else."
      (or "...against what the examiner cites, nowhere else"). Do NOT add a gloss clause
      to the verdict, do not soften "nowhere else", do not touch signature line 3, and do
      not reintroduce the venue phrase (the composer's reason for avoiding "at the patent
      office" here is sound). Accepting the current text with a context-suffices argument
      is also a legitimate disposition.
    quote: "That question gets decided against the examiner's cited art, nowhere else."

  # ---- passes with no findings (scope proven) ----

  - pass: pass-1-voice-anti-ai
    finding: "no findings"
    scoped_to: |
      Mechanical grep re-run from scratch on draft_version 3 (script on record): all 39
      banned_terms.txt entries + the full pass-1 word list + judgment-tier cluster terms
      (actually/align/unlock/seamless/robust/realm etc.) — zero hits; em-dash, en-dash,
      ellipsis-char — zero; exclamation marks — the single "!" in the file is the markdown
      image-embed syntax "![FIG. 5...]", not prose; Latin abbreviations, emoji — zero;
      not-just-X-but-Y, despite-challenges, copula-avoidance (serves as / stands as /
      represents / constitutes), vague attribution, puffery ("remarkable/extraordinary/
      unprecedented"), section-summary openers, sentence-initial Additionally/Furthermore/
      Moreover, "turns out" — zero. Bold audit: exactly one span, the declared signature
      line 2 (the essay's single inline bold thesis anchor). Semicolon audit: 4 flagged
      lines — FIG. 2/3/6 caption inventories and §3 ¶7 where the semicolon sits INSIDE the
      verbatim pitch quote ("each memory layer adds latency; the best layer is no layer");
      none clause-joining body prose. Announcement-colons re-judged: quote lead-ins, the
      "Translated:" translate-then-quote device (reader-profile rule 3), and §5 ¶4's
      parallel record enumeration (complete clauses before each colon) — no
      incomplete-clause colon tells. Sentence-initial "And" (§1 ¶3, §2 ¶1, §5 ¶4) and the
      "Now the pricing." fragment judged deliberate cadence within deliverable-voice-rules.
      Document/filing/application alternation is patent register, not elegant variation.
      The two v2→v3 clause swaps ("cited art", "beyond it") re-checked for introduced
      tells: none. Signature lines style-exempt and not sanded.

  - pass: pass-2-redundancy
    finding: "no findings"
    scoped_to: |
      Claim-repetition census re-run on v3. r2-F2's "past + rejection" echo is dead: §5 ¶4
      sentence 4 now reads "through a rejection and beyond it"; "beyond" appears exactly
      once in the whole draft (grep), so the smoothing introduced no replacement echo; the
      registry-exact landing "defended past a final rejection" (sentence 6) is untouched.
      Motif audit fresh: paying/spending recurrences (§1 ¶3 varied pair per r1-F1, §5 ¶1/¶4,
      §6 ¶1; §5 header and signature line 3 exempt surface) each add a new evidence layer —
      acceptable bridges per 2A; three-years motif (¶1 surface + §1 ¶3 status + §2 ¶1
      transition + §3 ¶7 echo-dating; signature line 1 exempt) unchanged from the r1-F3
      accepted ruling; "says yes" appears once outside signature line 1 (§6 ¶1), which is
      lead→closing recap, explicitly acceptable. "eight references" now appears exactly
      once (§5 ¶2) — the r2-F1 secondary point (verdict re-list) is cleared. 2B tightening
      sweep found no ≥25% cuttable sentence; 2C: every paragraph within the 3-7 sentence
      band (the two 2-sentence quote-follower units in §2 read as quote-integrated cadence,
      consistent with rounds 1-2); no 8+ sentence paragraph (max 7).

  - pass: pass-3-fact-paraphrase
    finding: "no findings"
    scoped_to: |
      All 25 patent-text quote spans re-byte-checked from scratch against input/patent.md
      (NBSP-normalized only), independent of gate_quotes: all clean substrings, including
      the [0045] split-quote bridging the source's "220and" run-on outside quotation marks
      and the [0040] quote ending before "215in". All 4 external quoted spans ("$1B+
      contracts", "$800m raised", "the best layer is no layer", the full pitch line)
      verified verbatim against fact-check-log rows. All 38 anchor tokens / 26 unique
      [dddd] anchors 4-digit and resolving to invention-summary spans/rows. Paraphrase
      audit on every anchored non-quoted sentence: claim-39 translation vs [0016]
      ("respective one or more columns" → "its own column or columns" — faithful); claim 15
      via [0014]; claims 11-13 vs the claim scope map (sidecar / attention work / negative
      rule, quoting [0051]'s description twin); [0021] weights-from-top + may-be-constants
      + tensor-from-left (re-verified against patent [0021] directly); [0024] two
      computations; [0013]/[0028] package claim + host-sees-one-array; [0038] 100×400;
      [0037] "may not be needed" concession; [0039]/[0040] memory economy; [0027]
      preset-loop with description-only label in prose; FIG. 7 semantics [0053]/[0055]/
      [0056]/[0057] all description-labeled in prose AND caption, "lone stall at layer
      normalization (Time B)" re-verified against patent [0057] ("This is shown at Time B
      where the array stalls"). Essay-own comparisons re-done: 128×128 = 16,384 ≈ "roughly
      sixteen thousand multipliers"; 1 TB/s = 5 GB per 5 ms ≈ "a feature film's worth of
      data every five thousandths of a second". TPU sentence unchanged from the verified
      r1-F4 fix and consistent with fact tpu-mxu-128x128 (floating-point scope excludes the
      8-bit 256×256 first-gen TPU; Trillium 256×256). External-fact discipline: thread
      figures "the company's own claim / the company says" on every use; CSM press-labeled;
      lien-1/lien-2 with effective (not recordation) dates and exact reel/frames
      067204/0877 / 071792/0869; lien-1 pool honesty (two later-rejected compiler
      applications named); grant-lien timing dates-only with "Any motive read into them is
      inference."; family-us-only as a labeled observation; examiner-art-8refs exact in §5
      ("Intel, IBM and Rambus among the assignees" — "among" honest vs the row's
      Intel/IBM/Rambus/ETRI); LVI absence with the 18-month caveat; tier-5 sohu-linkage
      unused (grep: no Sohu string). Register discipline: application-era verbs on every
      claim statement ("asks for / claims / seeks the arrangement / as drafted" ×3);
      "granted" appears 4×, every instance about the actually-granted wiring
      half / trio, never this application; zero enforceability language (enforce*/infring*
      grep: 0); "claims will grant" is the guard's future conditional, not grant-era scope
      language. The r2-F1 replacement clause verified as grounded (see disposition ruling).
      Figure truth re-checked with own eyes on all six placed figures + unplaced FIG. 4
      (see verification notes); the FIG. 6 manifest 605/610 defect did NOT leak.

  - pass: pass-4-logic-causality
    finding: "no findings"
    scoped_to: |
      Spine→section trace re-walked on v3 against thesis-spine.md: all four axes carried
      where mapped (Axis 1 §3 + lead gloss; Axis 2 §2/§3; Axis 3 §3; Axis 4 §1/§2/§3/§5);
      no out-of-spine claims; rejected candidates 2 and 3 not revived (§2 stays
      context-scale, §4 stays description-labeled mechanism color). Causality audit fresh:
      grant-lien timing dates-only + labeled inference; drafting-deliberateness attributed
      to the applicant's election (an act the record shows: claim 39 is an independent
      claim); "That switch is the layer this filing exists to delete" grounded in
      [0043]-[0045]; "not the first time" matches the choice-point record (non-finals
      2024-11/2025-07 before the final rejection); the CSM echo stays an echo ("Whether the
      racks the company says are shipping practice these claims is invisible from the
      patent record"); the RCE gloss ("a fee paid to keep arguing after the examiner has
      said no with finality") is an accurate mechanism statement, not motive attribution.
      The r2-F1 fix removed round 2's one countable forward-exhaustive claim; its
      replacement ("cited art") is forward-open and no longer falsifiable by the docket it
      points at (4B re-checked). Lead tension resolves in the closing (stage-vs-office
      frame closure); 4C arc: lead sets the gap, §2-§4 anchor the mechanism, §5 prices it,
      §6 lands the spine's exact two-sided call with residual risk = Acceptance mapped to a
      binary test — conformant.

  - pass: pass-5-reader-perspective
    finding: "one finding (r3-F1 above); everything else verified"
    scoped_to: |
      Engagement curve re-read fresh as the profile reader: discovery beat at word one;
      money stakes by ¶2-¶3; every mechanism section surfaces back to the bet (§2 →
      wiring-half/memory-half stake; §3 → CSM echo + bold anchor; §4 → "architecture bet in
      its purest form" and the budgeted-idle-cycles landing feeding §5's record-of-behavior
      turn); §2 ¶2's "a detail that matters later" promise pays off in §3 ¶3 (constants →
      hardwiring permissible). Jargon gloss census on v3: systolic array, HBM, independent
      claim, RCE, security interest, blanket lien, PCT, continuation, weight-stationary,
      layer normalization, transformer/self-attention all one-claused; the single gap is
      the revision-introduced "cited art" (r3-F1, low); "reads on" (§5 ¶2) re-judged — the
      surrounding breadth language carries it, consistent with two prior rounds. Mobile 5C
      re-measured on v3 (words / est. lines @12wpl): the marginal set is unchanged text
      accepted in rounds 1-2 with reasons that still hold — §2 ¶1 (143w) and §3 ¶6 (147w)
      quote-integrated structures (posture-lens demotion); §3 ¶7 (~122w, 7 sentences,
      quote-integrated) band edge; §1 ¶3 (105w), §4 ¶3 (113w, quote-integrated), §5 ¶4
      (103w), §5 ¶5 (109w, lien/label cohesion the both-or-neither rule wants), §6 ¶3
      (105w, the closing's internally signposted binary test) all 8.6-9.4 estimated lines
      at 12 wpl, i.e. ≤8 at the typography's 13-15 wpl upper band — measured and accepted,
      no text changed this round. Stake clarity: §6 reads standalone. No density wall
      (quotes/captions break every mechanism run).

  - pass: pass-6-lead-conclusion-format
    finding: "no findings (6G/6H both PASS under firm)"
    scoped_to: |
      6A lead anchor: discovery beat sentence 1; patent + filing date sentence 2; thesis by
      ¶1's end. 6B frame closure: stage-vs-office returns in §6 ¶2-¶3; residual risk
      Acceptance → closing-binary-test + docket watch pointer (firm-conformant; not an open
      question). 6C Sources: three enum categories (Patents 2, News & media 2, Technical
      specs 2), six entries, subgrouped all-or-nothing. 6D N/A (no Papers). 6E re-verified
      independently of gate-result.round-3.json: zero em-dashes; all anchors 4-digit,
      resolving; banned grep clean; publication.md byte-identical to draft body minus
      frontmatter/footnotes (programmatic diff: True); no footnote defs in publication.md;
      exactly one "# Sources". 6F title: colon-free, em-dash-free, 59 chars. 6G under firm,
      BOTH directions: the call leads ("The verdict is firm. This document is the real
      origin of Etched's memory story.") and is not qualifier-led; exactly ONE anti-hype
      guard, this-application-specific ("Racks shipping this summer, if they ship, are not
      evidence that these claims will grant. That question gets decided against the
      examiner's cited art, nowhere else." — the "if they ship" conditional prices a
      company-claimed fact inside the one guard, not a second hedge); no safe-harbor
      boilerplate (no "guarantee", no "time will tell"); §6 ¶1's "It is not yet the asset
      itself... can shrink or die" is the spine's own two-sided call, stated once with no
      §5 re-list (no dates, no reel/frames, no reference count — the "eight" now lives only
      in §5); no over-hedge stacking; no overreach — "real origin" / "authentically the
      founders' own" carried by earliest-filing + inventorship + the granted record's
      memory-half absence, with §5 ¶3 separating authorship from originality ("The patent
      office decides whether early also meant original."). 6H: no insurance fact precedes
      the discovery beat in title, cover caption, ¶1, or headers; ¶1 order = beat → filing
      facts → stage date → priced last (signature line 1); first-two-lines test passes
      (beat starts at word one); cover caption discovery-shaped, 5 numeral tokens
      (510/520/515/2026/2023) within the ≤6 budget; no gap-framed headers. Surface
      jurisdiction respected: title/headers/¶1/signature lines byte-identical to the
      verified v2 surface (composer's surface confirmation independently spot-checked by
      exact-string counts); no style sanding recommended anywhere on the surface.

  - pass: pass-7-adversarial-reader
    finding: "no findings"
    scoped_to: |
      Decomposed checklist re-run fresh on v3 with quoted evidence, both personas
      (impatient investor per reader-profile; skeptical pro-subject reader); table below.
      Steelman is the THIS-application objection at full strength (eight examiner-cited
      references / crowded field; claim-1 breadth "usually the first casualty"; claim-39
      no-switch possibly routine for weight-stationary designs), conceded then refined by
      the record of behavior; no generic patent truism anywhere (grep "guarantee": zero).
      Non-exempt verdict assertions in exactly 3 sections (§1 ¶3, §5 ¶4, §6 ¶1); the three
      declared signature lines present as exact strings, once each, excluded from the
      count. No stub (section words ~274/477/735/449/571/237; the short closer is the
      conventional landing). No reader instruction / self-reference; "offered as an
      observation" and "with its label attached" are edition-mandated evidence labels;
      "The verdict is firm." re-evaluated fresh: the call's frame, not meta. Jargon
      signpost check contributed r3-F1 (logged under pass-5 as the owning pass).
```

## Disposition-verification table (round-2 → draft_version 3)

| ID | r2 severity | Disposition claimed | Verified in draft? | Evidence (current text) | Ruling |
|---|---|---|---|---|---|
| r2-F1 | medium | applied (narrow — spine's own guard phrasing; reviewer's option (a) venue clause deliberately not used) | YES | §6 ¶2 last sentence now reads: "That question gets decided against the examiner's cited art, nowhere else." Old sentence ("...the examiner's eight references, nowhere else.") grep: zero. "eight references" now appears exactly once, in §5 ¶2, dated by §5 ¶1's "As of the May 2026 record" — the secondary 6G re-list point is cleared by the same edit. Sentence stays declarative, 11 words → 11 words, ¶ stays 3 sentences; §6 ¶1 (verdict call) and ¶3 (binary test + signature line 3) byte-identical to v2. | closed-verified |
| r2-F2 | low | applied (reviewer's primary variant) | YES | §5 ¶4 sentence 4: "And the spending is repeated: examination has been paid for through a rejection and beyond it." Colon device kept; sentence 6 ("...defended past a final rejection...") untouched as instructed; "beyond" appears exactly once in the draft (no replacement echo); ¶4 stays 6 sentences; registry truth unchanged. | closed-verified |

**Merits ruling on the r2-F1 execution choice** (composer chose the orchestrator-named
clause over the round-2 reviewer's fuller option (a)): ACCEPTED on the merits. (1) The
defect was a forward-exhaustive COUNT ("eight ... nowhere else") that the open RCE record
could falsify; "the examiner's cited art" is forward-open — it covers the eight references
of record and whatever RCE prosecution adds — while keeping "nowhere else" doing its
stage-exclusion work, so the sentence is now supportable as written. It is also the design
bundle's own guard phrasing (thesis-spine closing posture: "the examiner-cited field is
where that gets decided"; same in essay-context.md). (2) The venue-avoidance reasoning is
sound: §6 ¶1 already carries "until the patent office says yes" and the declared signature
line 3 lands on "At the patent office, ..." two sentences later — inserting option (a)'s
"at the patent office" into ¶2 would put the venue phrase three times in a 237-word
section and pre-echo the protected landing line. Reordering insurance against a declared
signature line is exactly what the surface fence exists to prevent. (3) Residual cost of
the chosen noun: "art" is an unglossed term of art for this reader — logged as new low
r3-F1 (vocabulary), not as a re-assertion, because r2-F1's grounding defect is fixed.

**Surface confirmation cross-check (independent):** title (59 chars, byte-identical to the
selected candidate), cover caption, §1 ¶1 (exact-string count 1 for the v2 opening
sentence), all six section headers, the three signature lines (exact-string count = 1
each), §6 ¶1 and ¶3 all verified present unchanged; the only v2→v3 body deltas found are
the two dispositioned clauses (§5 ¶4 "beyond it", §6 ¶2 "cited art"), matching the
composer's exactly-three-changed-lines claim (third = frontmatter draft_version). All 12
round-1 fix spans re-greped on v3 and still present (see lifecycle); residue greps
("exactly 128", "second time", "twice-defended", "TechCrunch, July 2026", "two years"):
all zero.

## Finding-id lifecycle (rounds 1-2 → round 3)

- **r1-F1..r1-F12** — closed in round 2 (11 fixes verified + 1 no-action accepted).
  Re-confirmed on v3: every round-1 fix span persists byte-identical (mechanical
  exact-string checks: r1-F1 §1 ¶3 varied pair; r1-F2 "One more registry note, offered as
  an observation."; r1-F3 accepted bridge unchanged; r1-F4 TPU floating-point/v5p/Trillium
  sentence; r1-F5 "It claims a package holding many small chips"; r1-F6 "not the first
  time" + "defended past a final rejection"; r1-F7 "before the company had a product to
  sell"; r1-F8 "(TechCrunch)" ×2 with zero dated residue; r1-F9 "[0016], [0044]" composite;
  r1-F10 "redraws the same design"; r1-F11 §5 ¶2/¶3 split intact (80w/47w); r1-F12
  continuation gloss). **Remain closed; no regression.**
- **r2-F1** — closed-verified this round (fix landed; merits of the execution choice
  accepted; secondary 6G point cleared). **Closed.**
- **r2-F2** — closed-verified this round (echo dead, no replacement echo). **Closed.**
- **Re-asserted:** none. **Dropped silently:** none.
- **New this round:** r3-F1 (low, pass-5 — revision-introduced unglossed term of art
  "cited art" in §6 ¶2; adjacent to the r2-F1 fix, logged as new rather than reopening
  r2-F1 because r2-F1's grounding defect is fixed).

## Per-pass verdicts

| Pass | Verdict | Notes |
|---|---|---|
| 1 voice + anti-AI | clean | full grep suite re-run on v3: zero banned hits; one bold span (declared anchor); semicolons only in captions + inside the verbatim pitch quote; the two revision clauses introduced no tells |
| 2 redundancy | clean | r2-F2 echo verified dead with no replacement ("beyond" unique); "eight references" once; motifs unchanged from accepted rulings; no 8+ sentence paragraph |
| 3 fact + paraphrase | clean | 25 patent quotes + 4 external quotes byte-verified from scratch; 26 unique anchors resolve; register/attribution/collateral/label discipline verified; both r2 fixes grounded |
| 4 logic + causality | clean | spine trace intact on v3; labeled-inference discipline holds; the round-2 forward-exhaustive claim is gone; closing maps Acceptance → binary test |
| 5 reader perspective | 1 low | r3-F1 "cited art" unglossed (r1-F12 defect class); marginal mobile paragraphs re-measured, unchanged text, accepted with reasons |
| 6 lead/closing + format | clean | 6G clean both directions under firm (one this-application guard; no boilerplate; no qualifier-led call; no §5 re-list; no overreach); 6H PASS (beat first everywhere on the surface); mechanicals re-verified independently of gates; publication identity proven |
| 7 adversarial reader | clean | checklist below; both personas; steelman at full strength, this-application |

### Pass-7 checklist (verdict, evidence)

1. **Hook check** — PASS. ¶1 sentence 1 lands the discovery beat declaratively, nothing
   queues ahead: "Three years before Etched pitched 'the best layer is no layer' as its
   memory philosophy on stage, both of its co-founders had signed that idea into the
   company's very first patent filing." Insurance arrives only in ¶1's final signature
   sentence ("...still hasn't said yes to it."). Second half: the full two-sided call lands
   by the lead's end — §1 ¶3 "The filing proves authorship... And Etched has paid at every
   step since... What the filing is not, yet, is the property itself... down to the
   borrowing secured against the patent stack this filing belongs to."
2. **Header-as-claim** — PASS. Skim skeleton: the pitch has a paper trail → one giant array
   stitched from identical chips → the memory claims delete the switch → math that forgets,
   a sidecar that remembers → Etched keeps paying to own it → an asset in formation. The
   argument reconstructs from headers alone; none gap-framed.
3. **Steelman** — PASS. §5 ¶2-¶3 concede at full strength: "The bear case is genuinely
   strong, and it is already on file. The examiner has assembled eight references...
   Claim 1, as drafted, reads on more or less any multi-chip systolic-array package...
   Even claim 39's distinctive absence... could yet be judged routine for weight-stationary
   designs..." — then ¶4 refines with the record of behavior. THIS-application objection;
   no truism spent anywhere.
4. **No meta posturing** — PASS. "offered as an observation" / "with its label attached"
   are edition-mandated evidence labels (exempt functional scope devices); "The verdict is
   firm." is the call's frame, not a reader instruction; zero essay-self-reference.
5. **Jargon as signpost** — PASS with one gap: all terms of art one-claused except the
   revision-introduced "cited art" (r3-F1, low; §5's reference inventory mostly carries
   it). No doctrinal deep-dives (no UCIe/interposer/GT-s in prose).
6. **No stub / rhythm break** — PASS. Section words ~274/477/735/449/571/237; the short
   closer is the conventional landing and closes the frame.
7. **Thesis not over-restated** — PASS. Non-exempt verdict assertions in exactly 3
   sections (§1 ¶3, §5 ¶4, §6 ¶1); the 3 declared signature lines verified present as
   exact strings (1 occurrence each) and excluded from the count.

## Verification notes (falsifiable record, round 3)

- **Quote byte-checks re-run from scratch** — all 25 patent-text quotes verified as clean
  substrings of input/patent.md directly (NBSP normalization only), including the [0045]
  split around "220and" and the [0040] cut before "215in"; the 4 thread quotes verified
  against fact-check-log verbatims. 38 anchor tokens / 26 unique, all 4-digit, all
  resolving to invention-summary rows.
- **Figure truth re-checked with own eyes (all seven files)** — fig-05.png: two memory
  chips 505A/B, four channels 510A-D, wires 520, four columns 515A-D inside tile 220 / IC
  215, nothing else in the path — cover caption and §3 walk exact. fig-06.png: 605A-D
  (auxiliary circuitry) INSIDE ICs 615A-D beside tiles 220; 610A-D as small boxes OUTSIDE,
  coupled to the 605s; dashed 650 encloses only the tiles — the Phase-0 manifest's swapped
  605/610 line did NOT leak into the caption. fig-01/02/03/07 captions image-verified
  (FIG. 2 nine labeled ICs 215A-I; FIG. 3 six memory chips 305A-F; FIG. 7 Time B stall
  band matching patent [0057] "This is shown at Time B where the array stalls"). fig-04
  checked: 2×3 grid (unequal rows/columns) — the §3 one-clause acknowledgment is accurate;
  FIG. 4 correctly unplaced per the locked pair-break.
- **Publication integrity** — programmatic check: publication.md == essay-draft.md minus
  frontmatter and the # Footnotes block (True); no footnote definitions; exactly one
  "# Sources".
- **v2→v3 delta audit** — the composer's "exactly three changed lines" claim independently
  supported: both dispositioned clauses present, old wordings grep-zero, and every v2 span
  quoted in the round-2 log (fix spans, surface strings, signature lines, §6 ¶1/¶3) found
  byte-identical in v3. thesis-trace §6 parenthetical synced to the applied wording
  (bookkeeping, checked).
- **Edition discipline re-verified on v3** — application-era verbs on every claim
  statement; exactly ONE dated prosecution label sentence (§5 ¶1: pending + examination
  continuing + final rejection 23 October 2025 + RCE 24 April 2026 — the brief's required
  content, dates only here); §5 ¶4's "defended past a final rejection" is the sanctioned
  date-free steelman reference (phase2-handoff-notes allowance); both-or-neither satisfied
  (label + liens in §5); liens portfolio-scope with effective dates + reel/frames, blanket
  discipline stated in terms, creditor symmetry, timing-as-inference; US-only labeled
  observation; LVI absence with the 18-month caveat; tier-5 fact unused; description-only
  labels on the preset loop and all FIG. 7 material in prose AND caption; no
  enforceability language.
- **Three-years audit** — "three years" ×5 all correct against 2023-05-10 → July 2026;
  "two years" residue zero; "this summer" = summer 2026 consistent; grants 15 July 2025 +
  lien effective 18 July 2025 = "three days later" correct.
- **Gate cross-check** — gate-result.round-3.json (14/14, zero findings incl. warns)
  consistent with all independent re-verification above.

## Overall assessment

**pass** — zero critical, zero high, zero medium, one low (r3-F1).

Disposition verification: **both round-2 findings closed** (r2-F1 medium: fix verified in
text, execution choice accepted on the merits; r2-F2 low: fix verified, no replacement
echo). All twelve round-1 ids remain closed with fix spans persisting byte-identical in
v3. No id dropped, none re-asserted.

One-line rationale: draft_version 3 is grounding-clean against patent.md and the fact log
(every quote and anchor re-verified from scratch), verdict-symmetric under the firm
posture (6G: call leads, one this-application guard, no boilerplate, no overreach),
hook-first on the whole surface (6H), and steelman-complete; the only remaining item is a
single low-severity vocabulary gloss ("cited art") introduced by an otherwise-correct fix,
which does not affect the assessment and may be applied or reasoned-accepted without a
structural edit.

**This IS a clean round** (no medium+ findings): it is the FIRST clean round — rounds 1
and 2 were revise-recommended — so double-clean is NOT yet reached. Expected next: round 4
confirmation review by a fresh reviewer (no revision required for acceptance; if the
composer optionally applies r3-F1, round 4 additionally verifies that one-clause
disposition). No hard-gate trigger at any point this round: no pass-3 high/critical,
gates 14/14, verdict and lead conform to the declared firm posture.
