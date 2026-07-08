# Edit Log — Round 4 (r2 re-run, reader-first architecture) — CONFIRMATION ROUND

```yaml
review_id: etched-0378175-memory-in-writing-r2-editorial-review-4
draft_source: handoff/02-compose/essay-draft.md (draft_version 3 — unchanged since round 3)
publication_source: handoff/02-compose/publication.md
review_timestamp: 2026-07-04T14:05:00Z
review_round: 4
round_type: confirmation
reviewer_context: fresh (no memory of rounds 1-3; own findings formed on the draft, figures, patent, and design bundle BEFORE prior-round logs were opened; rounds 1-3 artifacts then read per re-review protocol)
no_revision_since: round 3 (by design — confirmation rounds take no revision; no revision-response.round-3.md exists, correctly)
draft_identity_check: frontmatter draft_version 3; every v3 span quoted in the round-3 log found byte-identical; all round-1/2 fix spans persist exact-count-1 (table below); residue greps all zero
carried_findings: r1-F1..r1-F12 (closed rounds 2-3), r2-F1 (closed round 3), r2-F2 (closed round 3), r3-F1 (low, OPEN by design) — every id ruled in the lifecycle section below
gate_result_read: handoff/03-edit/gate-result.round-4.json (14/14 PASS, zero findings incl. warns) — consistent with this round's independent re-verification
posture_applied: measured
closing_posture_declared: firm
title_lead_register: discovery (human-selected pair; executed title re-verified byte-identical to the selected candidate in title-lead-candidates.md, 59 chars / 11 words)
overall_assessment: pass

findings:

  # ---- NEW findings, round 4: NONE. No r4-* ids issued. ----
  # Round 3's pass was treated as a hypothesis and tested from scratch: full 7-pass review
  # at full strength on the identical draft, with independent byte-checks, image checks,
  # greps, and paragraph measurements (evidence in scoped_to blocks and the verification
  # notes). The one open item remains r3-F1 (low, carried — ruled in the lifecycle section,
  # not re-issued under a new id).

  - pass: pass-1-voice-anti-ai
    finding: "no findings"
    scoped_to: |
      Mechanical grep battery re-run from scratch on draft_version 3 (own script, commands
      on record): full tier-1 banned list + plain-word-swap gated terms + judgment-tier
      cluster terms (actually / align with / unlock / seamless / robust / realm /
      landscape-abstract etc.) — zero hits; em-dash, en-dash, ellipsis character — zero in
      body (patent.md's own 5 em-dashes confirmed not imported); exclamation marks — the
      single "!" is the markdown image-embed token "![FIG. 5...", not prose; Latin
      abbreviations, emoji, ALL-CAPS emphasis (non-acronym) — zero. Pattern sweep:
      not-just-X-but-Y, despite-challenges, copula avoidance (serves as / stands as /
      represents a / constitutes), vague attribution, puffery
      (remarkable/extraordinary/unprecedented), section summaries, sentence-initial
      Additionally/Furthermore/Moreover, "turns out", "in order to", "due to the fact" —
      zero. Bold audit: exactly one span, the declared signature line 2 (the essay's single
      inline bold thesis anchor). Semicolon audit: hits only in the FIG. 2/3/6 caption
      inventories, inside the verbatim pitch quote ("each memory layer adds latency; the
      best layer is no layer"), and in the footnote stripped from publication.md — none
      clause-joining body prose. Colon audit: every mid-sentence colon follows a complete
      clause (quote lead-ins, "Translated:" translate-then-quote device, §5 ¶4 record
      enumeration, "That last filing is a purchase:") — no incomplete-clause fragment
      tells. "Now the pricing." fragment and sentence-initial "And" judged deliberate
      cadence within deliverable-voice-rules; document/filing/application alternation is
      patent register, not elegant variation. Signature lines style-exempt, not sanded.

  - pass: pass-2-redundancy
    finding: "no findings"
    scoped_to: |
      Independent claim-repetition census on v3. Non-exempt verdict assertions appear in
      exactly 3 sections (§1 ¶3 "remains a bet the company keeps paying to convert into an
      asset"; §5 ¶4 record-of-behavior refinement; §6 ¶1 verdict) — within budget; the
      three declared signature lines verified present exactly once each (exact-string
      count = 1) and excluded per surface jurisdiction. Motif audit fresh: the three-years
      motif (¶1 opener, §1 ¶3 status, §2 ¶1 transition, §3 ¶7 echo-dating; signature
      line 1 exempt) — each instance anchors a different time relation; acceptable-bridge
      repetition, consistent with the r1-F3 accepted ruling. Paying/spending recurrences
      (§1 ¶3 varied pair, §5 ¶1/¶4, §6 ¶1; §5 header + signature line 3 exempt) each add a
      new evidence layer. "10 May 2023" full date appears twice in body (¶1 discovery
      beat; §5 ¶4 authorship refinement) — new context both times. Echo checks: "beyond"
      appears exactly once (r2-F2's fix introduced no replacement echo); "eight
      references" exactly once (§5 ¶2); "says yes" once outside signature line 1 (§6 ¶1
      lead→closing recap, acceptable). 2B sweep found no ≥25%-cuttable sentence (the prose
      is compressed; "One more registry note, offered as an observation." is the
      edition-mandated label, kept). 2C: no paragraph ≥8 sentences (max 7); no paragraph
      >150 words (max 147).

  - pass: pass-3-fact-paraphrase
    finding: "no findings"
    scoped_to: |
      All quote spans re-byte-checked from scratch, independently of gate_quotes and of
      prior rounds: every double-quoted patent span and all three blockquotes are exact
      substrings of invention-summary.md Quotable spans / Quote anchor rows, and exact
      substrings of input/patent.md after normalizing the USPTO NBSP-before-numeral
      artifact (patent.md carries 731 U+00A0 characters; wording identical — verified at
      byte level). The [0045] split-quote correctly bridges the source's "220and" run-on
      OUTSIDE quotation marks; the preserved-typo discipline holds. All 4 external quoted
      spans ("$1B+ contracts", "$800m raised", "the best layer is no layer", the full
      pitch line) verified verbatim against fact-check-log rows. All 26 unique [dddd]
      anchors 4-digit, well-formed, resolving to invention-summary rows. Paraphrase audit
      on every anchored non-quoted sentence: claim-39 translation vs [0016] ("respective
      one or more columns" → "its own column or columns" — faithful); claim 15 via
      [0014]; claims 11-13 vs the claim scope map (sidecar / attention work / negative
      rule, [0051] description twin, "As drafted" label present); [0021]
      weights-from-top + may-be-constants + tensor-from-left (checked against patent
      [0021] directly); [0038] 100×400/400×100; [0037] "may not be needed" concession;
      [0039]/[0040] memory economy; [0027] preset loop with description-only label;
      FIG. 7 semantics [0053]/[0055]/[0056]/[0057] description-labeled in prose AND
      caption, "lone stall at layer normalization (Time B)" re-verified against patent
      [0057] ("This is shown at Time B where the array stalls"); §3 ¶3's
      column-reads-only-its-own-channel trade statement checked against [0043]-[0045] and
      the invention-summary's own Layer-2/Layer-3 reading — faithful. Essay-own
      comparisons re-computed: 128×128 = 16,384 ≈ "roughly sixteen thousand multipliers";
      1 TB/s × 5 ms = 5 GB ≈ "a feature film's worth of data every five thousandths of a
      second"; both clearly the essay's, source values verbatim. TPU sentence verified
      against fact tpu-mxu-128x128 (floating-point scope correctly excludes the 8-bit
      256×256 first-gen TPU; "generations through v5p"; Trillium 256×256 exact).
      Sought-only register: application-era verbs on every claim statement ("asks for /
      It claims / seeks / As drafted" — grep for locks/fences/protects/infring*/enforce*:
      zero); "granted" (5×) and "grants" (1×) refer only to the actually-granted wiring
      half / trio, never this application; "not an exclusive right to it" is the negated
      insurance clause, correct; "claims will grant" is the guard's future conditional.
      External-fact discipline: thread figures company-attributed on every use ("in the
      company's telling" ¶1, "every figure the company's own claim" ¶2, "the company
      says" / "the company calls" §3, "if they ship" conditional inside the §6 guard);
      CSM expansion press-labeled; lien-1/lien-2 portfolio-scope with EFFECTIVE dates and
      exact reel/frames 067204/0877 (19 April 2024) / 071792/0869 (18 July 2025); lien-1
      pool honesty (two later-rejected compiler applications named); blanket discipline
      in terms ("Both liens are blanket, selecting nothing..."); grant-lien timing
      dates-only ("The dates are facts. Any motive read into them is inference.");
      family-us-only as a labeled observation with PCT + continuation glosses; LVI
      absence scoped to THIS filing with the 18-month caveat; tier-5 sohu-linkage unused
      (grep zero). Exactly ONE dated prosecution label sentence (§5 ¶1: pending + final
      rejection 23 October 2025 + RCE 24 April 2026, "As of the May 2026 record");
      both-or-neither satisfied (label + liens in §5). Figure truth re-checked with own
      eyes on all seven image files (see verification notes); the Phase-0 manifest's
      swapped FIG. 6 605/610 line did NOT leak into caption or prose.

  - pass: pass-4-logic-causality
    finding: "no findings"
    scoped_to: |
      Spine→section trace re-walked against thesis-spine.md on the unchanged draft: all
      four axes carried where mapped (Axis 1 §3 + lead gloss; Axis 2 §2/§3; Axis 3 §3;
      Axis 4 §1/§2/§3/§5); every section advances its declared element; no out-of-spine
      claims; rejected candidates 2 and 3 not revived (§2 stays context-scale; §4 stays
      description-labeled mechanism color). Causality audit fresh: "That switch is the
      layer this filing exists to delete" grounded in [0043]-[0045] + claim 39's negative
      limitation; "adding rows of chips adds compute without adding a single memory chip"
      carries its mechanism (weights reused down rows, [0039]) — causation with
      mechanism, not correlation; "The filing proves authorship" carried by the signed
      inventorship record, with §5 ¶3 explicitly separating authorship from originality
      ("The patent office decides whether early also meant original."); grant-lien timing
      kept dates-only with motive labeled inference; the RCE gloss ("a fee paid to keep
      arguing after the examiner has said no with finality") is mechanism, not motive;
      "not the first time" matches the choice-point record (non-finals 2024-11/2025-07
      answered before the final rejection); the CSM echo stays an echo, never an equation
      ("Whether the racks the company says are shipping practice these claims is
      invisible from the patent record"); routine-filing confounder addressed via the
      RCE-after-final specificity + stand-alone-independent-claim election. 4C arc: lead
      sets the stage-vs-office gap, §2-§4 anchor the mechanism, §5 prices it, §6 lands
      the spine's exact two-sided call; residual risk Acceptance → closing-binary-test +
      docket watch pointer, conformant with the firm posture.

  - pass: pass-5-reader-perspective
    finding: "no findings (carried r3-F1 remains open — ruled in the lifecycle section)"
    scoped_to: |
      Engagement curve read fresh as the profile reader (curious retail investor,
      advanced-HS-to-early-undergrad): discovery beat at word one; stakes ("what is this
      document worth") explicit by ¶2-¶3; every mechanism section surfaces back to the
      bet (§2 → the wiring-half/memory-half stake at section end; §3 → CSM echo + the
      bold anchor; §4 → "the architecture bet in its purest form" and the
      budgeted-idle-cycles landing feeding §5's record-of-behavior turn); §2 ¶2's "a
      detail that matters later" promise pays off in §3 ¶3. Jargon gloss census re-run:
      systolic array, HBM, independent claim, RCE, security interest, blanket lien, PCT,
      continuation, weight-stationary, layer normalization, transformer/self-attention
      all one-claused; the single gap remains the carried r3-F1 "cited art" (§6 ¶2) —
      independently re-judged LOW: the §5 ¶2 steelman inventory ("The examiner has
      assembled eight references against this application, drawn from...") supplies the
      referent one section earlier by back-reference. Mobile 5C re-measured
      independently (words / est. lines at 12-15 wpl): §2 ¶1 143w, §3 ¶6 147w, §3 ¶7
      122w are the heaviest and all are quote-integrated structures (verbatim quote +
      narrative anchor + citation as one unit) → posture-lens demotion applies (measured
      + quote-integrated → low); §1 ¶3 105w, §4 ¶3 113w, §5 ¶4 103w, §5 ¶5 109w (lien
      cohesion the both-or-neither rule wants), §6 ¶3 105w all ≤8 lines at the
      typography's 13-15 wpl band. Same set, same reasons, as the rounds-1-3 accepted
      rulings — measured independently BEFORE reading those logs; concur, no text change
      required. No density wall (a quote or caption breaks every mechanism run); §6
      reads standalone (stake clarity bookended).

  - pass: pass-6-lead-conclusion-format
    finding: "no findings (6G and 6H both PASS under the declared firm posture)"
    scoped_to: |
      6A: discovery beat sentence 1; patent number + filing date + the ask in sentence 2;
      thesis by ¶1's end; full two-sided call by §1 ¶3. 6B: closing returns to the
      stage-vs-office frame (§6 ¶2-¶3); residual risk Acceptance → closing-binary-test +
      forward watching event ("the application's public docket, and the company's next
      response on it") — firm-conformant, not an open question. 6C: # Sources exactly
      once; three enum categories (Patents 2, News & media 2, Technical specs 2), six
      entries, all-or-nothing subgrouping correct (4+ entries across 2+ categories →
      subgrouped). 6D: N/A (no Papers). 6E re-verified independently of the gate JSON:
      zero em-dashes; all anchors 4-digit and resolving; banned grep clean; footnote defs
      absent from publication.md; publication.md == draft body minus frontmatter +
      Footnotes (programmatic normalize-diff: True). 6F: title colon-free, em-dash-free,
      59 chars / 11 words. 6G under firm, BOTH directions — over-hedge: the call leads
      ("The verdict is firm. This document is the real origin of Etched's memory
      story."), not qualifier-led; exactly ONE anti-hype guard and it is
      this-application-specific ("Racks shipping this summer, if they ship, are not
      evidence that these claims will grant. That question gets decided against the
      examiner's cited art, nowhere else."); no safe-harbor boilerplate (no "patents
      don't guarantee", no "only time will tell" — grep "guarantee": zero); §6 ¶1's
      "not yet the asset itself... can shrink or die" is the spine's own two-sided call
      stated once, with zero §5 re-list (no dates, no reel/frames, no reference count in
      §6); no stacked hedges. Overreach: "real origin" / "authentically the founders'
      own" carried by earliest-filing + signed inventorship + the granted record's
      memory-half absence, with §5 separating authorship from originality; the binary
      test's upside branch stays conditional on grant. 6H: no verdict-insurance fact
      precedes the discovery beat in title, cover caption, ¶1, or headers; ¶1 order =
      beat → filing facts → stage date → priced last (signature line 1);
      first-two-lines test passes (beat starts at word one); cover caption
      discovery-shaped with 3 reference numerals (510/520/515), within the ≤6 budget;
      no gap-framed headers. Surface jurisdiction respected throughout: no style
      recommendation touches title, headers, ¶1, or the three declared signature lines.

  - pass: pass-7-adversarial-reader
    finding: "no findings"
    scoped_to: |
      Decomposed checklist re-run fresh with quoted evidence, both personas (impatient
      investor per reader-profile.md; skeptical pro-subject reader) — full table below.
      Steelman is the THIS-application objection at full strength (eight examiner-cited
      references / crowded field; claim-1 breadth "usually the first casualty"; claim 39
      possibly routine for weight-stationary designs), conceded ("The bear case is
      genuinely strong, and it is already on file.") then refined by the record of
      behavior; no generic patent truism anywhere. Skeptic's second-order objections all
      pre-answered in text: lien selectivity ("Both liens are blanket, selecting
      nothing"), product-practices-claims equation (explicitly disclaimed), LVI absence
      (18-month caveat), stale-snapshot risk (registry facts self-dated "As of the May
      2026 record"). Impatient-investor scan: verdict-in-miniature lands in ¶3; no
      un-glossed jargon except the carried r3-F1 low; no filler; the §4 mechanism color
      is the highest-skim-risk stretch but is short (449w), image-anchored, and lands on
      the section's strongest two sentences. "The verdict is firm." re-evaluated fresh:
      the call's frame, not meta posturing; "offered as an observation" / "with its
      label attached" are edition-mandated evidence labels (functional, exempt).
```

## Carried-finding lifecycle (rounds 1-3 → round 4, no revision in between)

Confirmation-round duty: no dispositions exist to verify (no revision occurred, correctly);
the ruling below is (a) independent re-verification that every closed finding's fix still
stands in the unchanged draft, and (b) an independent ruling on the one open id.

| ID | Severity | State entering round 4 | Independent re-verification (this round) | Ruling |
|---|---|---|---|---|
| r1-F1 | low | closed (r2, re-confirmed r3) | Fix span exact-count-1: "And Etched has paid at every step since..." + closing "keeps paying to convert into an asset" intact | remains closed |
| r1-F2 | low | closed | "One more registry note, offered as an observation." exact-count-1; "registry observation" residue 0 | remains closed |
| r1-F3 | low | closed (no-action accepted) | Three-years motif re-censused independently; same acceptable-bridge judgment reached fresh | remains closed |
| r1-F4 | medium | closed | TPU sentence exact-count-1 in the narrowed form ("floating-point... through v5p... Trillium"); "exactly 128" residue 0; fact-conformant | remains closed |
| r1-F5 | medium | closed | "It claims a package holding many small chips" exact-count-1; identicality lives only in the verbatim [0028] quote ¶3 | remains closed |
| r1-F6 | medium | closed | "It is not the first time..." exact-count-1; "second time"/"twice-defended" residue 0; "defended past a final rejection" exact-count-1 | remains closed |
| r1-F7 | medium | closed | "before the company had a product to sell" exact-count-1; "product name" residue 0 | remains closed |
| r1-F8 | low | closed | "(TechCrunch)" undated ×2; "TechCrunch, July 2026" residue 0 | remains closed |
| r1-F9 | low | closed | Composite cite "no switch in between [0016], [0044]" exact-count-1 | remains closed |
| r1-F10 | low | closed | "redraws the same design with unequal rows and columns" exact-count-1; checked against fig-04.png (package 401, distinct embodiment) — wording remains the supportable one | remains closed |
| r1-F11 | medium | closed | §5 ¶2/¶3 split intact (80w / 47w by independent count) | remains closed |
| r1-F12 | low | closed | Continuation gloss "the follow-on filing that keeps a patent family growing" exact-count-1 | remains closed |
| r2-F1 | medium | closed-verified (r3) | "That question gets decided against the examiner's cited art, nowhere else." exact-count-1; old wording residue 0; "eight references" exactly once, in §5, dated by ¶1. Merits of the narrow-not-hedge execution independently ACCEPTED: "cited art" is forward-open against the RCE record while "nowhere else" keeps the stage-exclusion punch; grounding fix priority (narrow) correctly applied, no hedge added | remains closed |
| r2-F2 | low | closed-verified (r3) | "through a rejection and beyond it" exact-count-1; "beyond" unique in draft (no replacement echo); landing sentence untouched | remains closed |
| r3-F1 | low | OPEN (by design — no revision between rounds 3 and 4) | "the examiner's cited art" present unchanged in §6 ¶2 (its only occurrence). Independently re-judged: severity LOW confirmed — "art" is the draft's one unglossed term of art, first use in the verdict, but the §5 ¶2 steelman inventory supplies the referent one section earlier by back-reference, and every fix route that adds a gloss clause to the verdict is worse than the defect (6G hedge-budget pressure; signature-line 3 pre-echo risk per the round-3 merits ruling). Round 3's recommendation menu stands, including reasoned acceptance | remains OPEN (low) — deferred to post-acceptance self-audit per confirmation-round policy; does not affect assessment (lows never do) and does not block double-clean |

**No id dropped silently. No id re-asserted. No new ids issued this round.**

## Per-pass verdicts

| Pass | Verdict | Notes |
|---|---|---|
| 1 voice + anti-AI | clean | full grep battery re-run from scratch: zero banned hits; one bold span (declared anchor); semicolons only in captions + verbatim quote + stripped footnote; no colon/fragment tells |
| 2 redundancy | clean | verdict in exactly 3 non-exempt sections; motifs re-censused and accepted; "beyond"/"eight references" unique; no 8+ sentence or >150w paragraph |
| 3 fact + paraphrase | clean | every quote span byte-verified from scratch vs invention-summary AND NBSP-normalized patent.md; 26 anchors resolve; sought-only register, attribution, collateral, label, and figure-truth discipline all hold; zero drift, zero fact introduction |
| 4 logic + causality | clean | spine trace intact; every causal claim carries its mechanism or its inference label; echo-not-equation discipline holds; arc closes on the binary test |
| 5 reader perspective | clean (1 carried low open) | r3-F1 "cited art" re-judged low, remains open by design; mobile set independently re-measured, quote-integrated demotion concurred; money thread structural in every section |
| 6 lead/closing + format | clean | 6G PASS both directions under firm (call leads; ONE this-application guard; no boilerplate; no re-list; no overreach); 6H PASS (beat first everywhere on the surface); mechanicals re-verified independently of the gate JSON |
| 7 adversarial reader | clean | checklist below with quoted evidence; steelman at full strength and this-application; both personas run |

### Pass-7 checklist (verdict, evidence)

1. **Hook check** — PASS. ¶1 sentence 1 lands the discovery beat declaratively, nothing
   queued ahead: "Three years before Etched pitched 'the best layer is no layer' as its
   memory philosophy on stage, both of its co-founders had signed that idea into the
   company's very first patent filing." Insurance arrives only in ¶1's final signature
   sentence ("...still hasn't said yes to it."). Second half: the full two-sided call
   lands by the lead's end — §1 ¶3 "The filing proves authorship... What the filing is
   not, yet, is the property itself... down to the borrowing secured against the patent
   stack this filing belongs to."
2. **Header-as-claim** — PASS. Skim skeleton: the pitch has a paper trail → one giant
   array stitched from identical chips → the memory claims delete the switch → math that
   forgets, a sidecar that remembers → Etched keeps paying to own it → an asset in
   formation. The argument reconstructs from headers alone; none gap-framed; none
   inventory-shaped.
3. **Steelman present** — PASS. §5 ¶2-¶3: "The bear case is genuinely strong, and it is
   already on file. The examiner has assembled eight references against this
   application... Claim 1, as drafted, reads on more or less any multi-chip
   systolic-array package... Even claim 39's distinctive absence... could yet be judged
   routine for weight-stationary designs..." — conceded at full strength, then refined
   (¶4, the record of behavior). THIS-application objection; grep "guarantee": zero.
4. **No meta posturing** — PASS. Zero reader-instruction / essay-self-reference. "The
   verdict is firm." is the call's frame; "offered as an observation" / "with its label
   attached" are edition-mandated evidence labels (functional scope devices, exempt).
5. **Jargon as signpost** — PASS with the one carried gap: all terms of art one-claused
   except "cited art" (r3-F1, low, open by design; §5's reference inventory carries it).
   No doctrinal deep-dives (no UCIe / interposer / GT/s in prose).
6. **No stub / rhythm break** — PASS. Section words ~274/477/735/449/571/237; the short
   closer is the conventional landing and closes the frame.
7. **Thesis not over-restated** — PASS. Non-exempt verdict assertions in exactly 3
   sections (§1 ¶3, §5 ¶4, §6 ¶1); the three declared signature lines verified present
   as exact strings, once each, excluded from the count.

## Verification notes (falsifiable record, round 4)

- **Independence protocol.** All findings-hunting (passes 1-7, byte-checks, image checks,
  greps, paragraph measurements) was completed on the draft + design bundle + patent +
  figures BEFORE opening edit-log.round-1/2/3.md or the revision responses; prior logs
  were then read to execute the carried-id lifecycle ruling. Convergent results (the same
  mobile set, the same r3-F1 judgment, the same clean pass verdicts) are therefore
  independent confirmations, not inherited ones.
- **Quote byte-checks re-run from scratch** — every double-quoted patent span and all
  three blockquotes are exact substrings of invention-summary rows AND of patent.md after
  NBSP normalization (the patent file carries 731 U+00A0 characters before reference
  numerals — the only difference; verified at byte level with a diff on the [0028] span).
  External quotes verified against fact-check-log verbatims. 26 unique anchors, all
  4-digit, all resolving; no malformed cite tokens.
- **Figure truth re-checked with own eyes (all seven files)** — fig-05.png: two memory
  chips 505A/B, four channels 510A-D, wires 520, four columns 515A-D inside tile 220 / IC
  215, nothing else in the path — cover caption and the §3 walk exact. fig-06.png: 605A-D
  (auxiliary circuitry) INSIDE ICs 615A-D beside tiles 220; 610A-D as small boxes OUTSIDE
  the ICs, coupled to the 605s; dashed 650 encloses only the tiles — the caption follows
  the spec-correct labels; the Phase-0 manifest's swapped 605/610 line did NOT leak.
  fig-01.png: two multiplications sharing one DPU grid (caption exact). fig-02.png: nine
  labeled ICs 215A-I, tiles 220A-I, memory chips 210A-C on the top row, host 205 over
  PCIe 240 (caption exact). fig-03.png: six memory chips 305A-F, two per top-row IC
  (prose "six memory chips across the top" and caption exact). fig-07.png: timeline with
  Time B stall band — matches patent [0057] "This is shown at Time B where the array
  stalls". FIG. 4 correctly unplaced (locked pair-break); its one prose clause remains
  the supportable "same design" wording.
- **Draft identity + fix persistence** — frontmatter draft_version 3; no
  revision-response.round-3.md exists (correct for a confirmation round); all 14 fix
  spans from rounds 1-2 and all 3 signature lines present at exact-string count 1; all 11
  residue greps zero ("exactly 128", "second time", "twice-defended", "TechCrunch, July
  2026", "two years", "product name", "eight references, nowhere else", "rejection and
  past it", "One more registry observation", "Sohu/sohu"). Publication integrity:
  publication.md == essay-draft.md minus frontmatter and # Footnotes (programmatic
  normalize-diff: True); no footnote defs in publication.md; exactly one "# Sources".
- **Edition discipline re-verified end-to-end** — sought-only claim language everywhere;
  exactly ONE dated prosecution label sentence (§5 ¶1); both-or-neither satisfied in §5;
  liens portfolio-scope with effective dates + reel/frames + blanket discipline +
  creditor symmetry; timing-as-inference labeling; US-only labeled observation;
  LVI absence with the 18-month caveat; description-only labels on the preset loop and
  all FIG. 7 material in prose AND caption; zero enforceability language; three-years
  arithmetic correct at every occurrence (2023-05-10 → July 2026; grants 15 July 2025 →
  lien effective 18 July 2025 = "three days later").
- **Gate cross-check** — gate-result.round-4.json (14/14 PASS, zero findings incl.
  warns) consistent with every independent re-check above.

## Overall assessment

**pass** — zero critical, zero high, zero medium, zero new low; one carried low (r3-F1)
remains open by design.

One-line rationale: an independent full-strength re-review of the unchanged
draft_version 3 — quotes re-byte-checked against the patent, figures re-read against the
images, register/attribution/collateral/label discipline re-audited, 6G/6H re-judged in
both directions under the firm posture, and the pass-7 checklist re-run with evidence —
reproduces round 3's result from scratch and surfaces nothing at any severity beyond the
already-logged r3-F1 (low, vocabulary, deferred to self-audit).

**Double-clean is REACHED from this reviewer's side**: round 3 (first clean round,
independent reviewer) + round 4 (this confirmation round, fresh reviewer, zero medium+
findings on the identical draft) = two consecutive clean rounds from independent
reviewers. No hard-gate trigger at any point: no pass-3 high/critical, gates 14/14,
verdict and lead conform to the declared firm posture. r3-F1 (low) travels to the
post-acceptance self-audit under its existing id.
