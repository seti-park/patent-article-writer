```yaml
review_id: openai-us20260147536-editorial-review-2
draft_source: handoff/02-compose/essay-draft.md
draft_version_reviewed: 2
review_round: 2
review_timestamp: 2026-07-09T00:00:00Z
posture_applied: measured   # 3-tier posture = measured; edition declares closing_posture: firm,
                            # so 6G/6H/6I escalate to HIGH if violated. Checked below — all clean,
                            # no firm-closing escalation triggered.
closing_posture_declared: firm
gates_precomputed: PASS (0 fails). Warn signals weighed below: FIGUSE-002 x2 (FIG.38/FIG.45),
                   LONGSENT-001 x8 (incl. a 72-word flag), DUPE-001 x2, STRUCT-004 (4 triads).
reviewer_note: |
  Fresh round-2 reviewer, no memory of composing or of round 1. This draft is figure-enabled
  (draft_version 1 -> 2): four figures were integrated (FIG. 4 header, FIG. 1 + FIG. 3 in §2,
  FIG. 43 in §4) plus two prose cross-references (FIG. 38, FIG. 45). Figures were NEVER reviewed
  before (round 1 was text-only), so the figure integration is treated as brand-new material and
  scrutinized on its own terms (pass-3 grounding + pass-6/pass-5 surface). Re-review protocol
  followed: every round-1 finding_id (r1-F1..r1-F6) is ruled on FIRST, then the 7 passes hunt new
  findings.
overall_assessment: revise-recommended   # 1 medium (r2-F1) + 2 low. No high, no critical.

# ===========================================================================
# PART A — CARRIED FINDING RULINGS (round-1 dispositions verified in draft v2)
# All six round-1 dispositions were disposed 'applied'. Each verified below.
# ===========================================================================

carried_findings:

  - finding_id: r1-F1
    round1_severity: medium
    disposition_claimed: applied (split §2 alignment paragraph at "...before the sum [0104].")
    ruling: LANDED — accept
    verification: |
      §2 now breaks at the declared seam. ¶4 (line 42) ends "...on a consistent footing before
      the sum [0104]." (analogy + bit-shift + max-exponent search, 3 sentences, ~85 words). ¶5
      (line 44) begins "The numbers stay small by design:" (worked FP8xFP6 example + INT35/INT5
      + FP22 dequant, 3 sentences, ~75 words). Each half now renders ~6-7 mobile lines, both
      UNDER the pass-5 5C 8-line wall (the round-1 estimate of 4-5 lines was optimistic — ¶4
      absorbed the analogy + the FIG.38 clause — but the density wall the finding targeted is
      resolved). No neighbor regressed; no new 8-sentence paragraph created.

  - finding_id: r1-F2
    round1_severity: medium
    disposition_claimed: applied (split §3 densest para after "64 by 64 half adders"; broke the
                         ~48-word machinery sentence into two)
    ruling: LANDED — accept (with one precise note, non-reopening)
    verification: |
      §3 paragraph split landed: ¶3 (line 54) = named-machinery specifics (4 sentences, ends
      "...example 32-by-32 array [0183]."); ¶4 (line 56) = "That is the distinction the skeptical
      read misses..." affirmative-core return. The ~48-word machinery sentence was lightened, but
      landed as ONE sentence joined by a semicolon ("The named machinery starts with a shift
      calculation and select decoding unit that works out each product's shift [0200]; that unit
      is the one piece independent claim 20 pulls up into itself...") plus a following sentence,
      i.e. a semicolon-join rather than the two full sentences the disposition described. The
      readability goal is met (the triple-clause list is broken); the residue is one Tier-2
      semicolon (see pass-1 scoped_to). Density finding resolved — not re-asserted.

  - finding_id: r1-F3
    round1_severity: low
    disposition_claimed: applied (§1 ¶2 "written down to the individual memory cell" ->
                         "written to the bitcell")
    ruling: LANDED — accept
    verification: |
      §1 ¶2 (line 21) now reads "...the math engine was already on file, written to the bitcell."
      The verbatim depth-motif "down to the individual memory cell" now appears exactly twice —
      §1 ¶1 (line 19) and §6 (line 83) — the intended lead->closing bookend. Gate DUPE-001 x2
      confirmed and deliberate. The adjacent-lead verbatim repeat the finding targeted is gone.

  - finding_id: r1-F4
    round1_severity: low
    disposition_claimed: applied (shift-calc + select-decoding unit stated as folded into
                         independent claim 20, not dependent-only)
    ruling: LANDED — accept
    verification: |
      §3 ¶3 (line 54): "...that unit is the one piece independent claim 20 pulls up into itself,
      alongside the multiply-align-add triad." Matches invention-summary Claim scope map exactly
      (claim 20 = triad + shift-calculation and select decoding unit). Register-sizing (claim 3,
      [0202]) and log-mux tree (claims 6-9, [0206]) remain correctly grouped under "The dependent
      claims add the rest". Precision fix in the safe direction; no hedge introduced; no
      contradiction with §3 ¶2's "claims 1 and 20 seek the multiply-align-add triad".

  - finding_id: r1-F5
    round1_severity: low
    disposition_claimed: applied ("do not carry" -> "rarely carry" clock margins and scan modes)
    ruling: LANDED — accept
    verification: |
      §5 ¶3 (line 79): "Concept filings rarely carry clock margins and scan modes. Documents
      written toward manufacture do, and this one reads like engineering rather than positioning."
      Categorical narrowed; the evidential landing is untouched; jurisdiction fence honored
      (claim narrowed, verdict NOT hedged).

  - finding_id: r1-F6
    round1_severity: low
    disposition_claimed: applied ("about" added to §1 ¶1; §1 ¶2 and §6 inherit the approximation)
    ruling: LANDED — accept. (§6 consistency question ruled separately as r2-F3, low.)
    verification: |
      §1 ¶1 (line 19): "on 13 October 2025, about eleven months later". The other two uses stayed
      bare — §1 ¶2 (line 21) "Eleven months before OpenAI announced its own chip" and §6 (line 83)
      "priority date eleven months older than the announcement". The round-1 finding's own
      recommendation explicitly permitted the later uses to "inherit the approximation once
      established", so the disposition is consistent with what was accepted. The orchestrator's
      consistency question (should §6 match?) is ruled as a NEW low note — see r2-F3.

# ===========================================================================
# PART B — NEW ROUND-2 FINDINGS (figure integration is the new surface)
# ===========================================================================

findings:

  - finding_id: r2-F1
    pass: pass-5-reader-perspective   # cross-pass with pass-6 6H cover-caption clause; goal-2 figure review
    location: "Header / cover — the FIG. 4 caption block (line 15), the text directly under the cover image and above §1."
    severity: medium
    severity_under_default_posture: medium
    finding: |
      The cover caption is the densest text in the essay and sits at the highest-traffic surface
      (the X card / cover, the reader's first content beat). It runs ~86 words across five
      sentences and carries a heavy inventory of numerals and reference numbers: "at most 22
      here, an integer that fits in 5 bits", "the column adder tree (426)", "outputs a 35-bit
      integer per column", "claim 1's align-then-integer-accumulate step", plus the [0199]/[0011]/
      [0145] anchor cluster. This is the source of the LONGSENT-001 72-word flag: the caption was
      split into real sentences (longest is ~37 words), but the gate's sentence-splitter merges a
      ~70-word run across "...by that amount. A two's-complement step..." (single-capital A read
      as an initial) and the "(426)"/"35-bit" runs — so the "72-word sentence" is partly a
      splitter artifact, but the underlying density it points at is real. Grounding is CLEAN (every
      claim traces: Emax=22/INT5 [0199], adder tree 426 integer format [0011], INT35 out [0145];
      nothing overclaims beyond FIG. 4's drawing per the manifest). This is purely a cover-surface
      density / attention-budget concern, not an accuracy one. The reference number "(426)" in
      particular is pure inventory for the target retail reader — it adds nothing a cover caption
      needs and taxes the one caption meant to INVITE. Not defensive-open (6H clean: the caption
      leads with the discovery — "the align-once core, drawn as circuitry" — and no verdict-
      insurance fact precedes it), so this is not a 6H finding; it is a pass-5 cover-caption
      density finding.
    recommendation: |
      Trim the cover caption toward invitation without touching the header_composite design intent
      (it may stay detailed). Concrete, cheap edits: (a) drop the "(426)" reference number — a
      cover reader does not need part numbers; (b) compress the shift-calculation sentence so the
      cover leads faster to the payoff. One workable shape: "FIG. 4: the align-once core, drawn as
      circuitry. Each product's mantissa is shifted onto the block's largest exponent (at most 22
      here, a 5-bit integer [0199]), a two's-complement step lets negatives ride the same path, and
      the column adder tree sums the aligned mantissas as plain integers [0011], one 35-bit result
      per column [0145]. This is claim 1's align-then-integer-accumulate step, made literal." Keep
      the thesis-tie last sentence verbatim. No mechanism claim changes; the grounding chain is
      preserved.
    quote: "The column adder tree (426) then sums the aligned mantissas in the integer domain [0011] and outputs a 35-bit integer per column [0145]."

  - finding_id: r2-F2
    pass: pass-5-reader-perspective   # goal-2 figure review; assesses gate FIGUSE-002 x2
    location: "§2 ¶4 (line 42) 'FIG. 38 shows it as physical circuitry'; §5 ¶3 (line 79) 'FIG. 45 draws one such scan-wired double bitcell'."
    severity: low
    severity_under_default_posture: low
    finding: |
      Assessment of the two FIGUSE-002 value-add cross-references, per the orchestrator's request
      to judge value-add vs clutter. Both are ACCURATE against the manifest (FIG. 38 = the
      physical column-cell realization of FIG. 4's functional block: adder tree 426 + fp2int +
      bitcell layout; FIG. 45 = a scan-wired double bitcell). But BOTH point to figures the reader
      cannot see — neither FIG. 38 nor FIG. 45 is placed in the article. For the target retail
      reader, "FIG. 38 shows it..." / "FIG. 45 draws one such..." is a pointer to an absent visual
      (mild "where is that?" friction), and the composer's own revision-response records that these
      cross-references exist substantially to clear a gate_figure_use ORPHAN artifact (the Phase-1
      figure-selection.md prose tokenizes "FIG. 38/42" and "FIG. 45/46" as selected). Net: FIG. 38
      earns marginal thematic value — the functional-vs-physical duality reinforces the essay's
      depth thesis ("they drew it both as a block and as real circuits"); FIG. 45 is thinner (a
      bare scan pointer). Two of the three prose semicolons in the essay graft these figure
      pointers onto the preceding sentence (lines 42, 79), which is where the joins read slightly
      mechanical.
    recommendation: |
      Acceptable to ship as-is: the alternative (dropping the tokens) re-triggers the FIGUSE-001
      hard-fail orphan, and force-placing FIG. 38/45 as captions violates the design's tight-count
      intent. Preferred durable fix is UPSTREAM and already flagged by the composer in
      figures-rationale.md: design-architect should reword the unselected-figure discussion in
      figure-selection.md so "FIG. 38/42" / "FIG. 45/46" do not tokenize as selected (e.g. "sheets
      38 and 42"), after which these two clauses can be softened to describe the circuit without an
      un-shown figure number ("the patent also draws it as physical circuitry" / "the document even
      draws the scan-wired bitcell"). No round-2 revision required of the composer; this is a
      note-and-route to the upstream lane.
    quote: "FIG. 4 draws that back end as a functional block, and FIG. 38 shows it as physical circuitry."

  - finding_id: r2-F3
    pass: pass-3-fact-paraphrase   # date-arithmetic precision consistency (extends r1-F6)
    location: "§1 ¶2 (line 21) 'Eleven months before'; §6 ¶1 (line 83) 'eleven months older' — vs §1 ¶1's hedged 'about eleven months later'."
    severity: low
    severity_under_default_posture: low
    finding: |
      The orchestrator's flagged consistency question. r1-F6 added "about" to §1 ¶1 only; §1 ¶2
      opens flat ("Eleven months before...") and §6 restates flat ("eleven months older"). The
      true gap is ~10 months 21 days (2024-11-22 -> 2025-10-13); fact-check-log instructs "about
      eleven months". Ruling: ACCEPTABLE, no verdict impact, for two independent reasons. (1) §1 ¶2
      is ADJACENT to ¶1, so the "about" just established carries — exactly the inherit the round-1
      finding endorsed. (2) §6 itself states the RAW dates two sentences later ("The announcement
      is from October 2025. The engineering is dated November 2024."), so the reader can verify the
      ~11-month gap directly; the flat "eleven months older" is not presenting an unverifiable
      rounded figure. The load-bearing hook is thus transparently sourced, not overstated.
    recommendation: |
      No action required. Optional uniformity touch only if the composer wants it: soften §1 ¶2's
      sentence-initial "Eleven months before" to "Nearly eleven months before" (its position at the
      top of ¶2 makes the flat figure most prominent there). This is a precision nicety on date
      arithmetic, NOT a hedge on the verdict — jurisdiction fence honored.
    related_fact_entry: openai-broadcom-10gw-2025-10-13

# ===========================================================================
# PART C — CLEAN PASSES (falsifiable scoped_to — what was actually checked)
# ===========================================================================

  - pass: pass-1-voice-anti-ai
    finding: "no findings"
    scoped_to: |
      1B mechanical (v2 delta focus — the four figure captions + the r1-F1/r1-F2 split spans are
      the new prose): greped connective prose (quotes/blockquotes excluded) for the full Tier-1
      banned list (delve/leverage/navigate/crucial/underscore/enhance/robust/seamless/showcase/
      intricate/pivotal/testament/groundbreaking/interplay etc.) and rhetorical patterns
      (not-just-X-but-Y, despite-the-challenges, copula avoidance represents/constitutes/
      serves-as/stands-as, section-summaries, sentence-initial Additionally/Moreover/Furthermore,
      "it is worth noting", elegant variation): ZERO hits in the essay's own prose, including all
      new caption text ("align-once core", "one-pass datapath", "double-bitcell cell",
      "scan-wired double bitcell" — technical compounds, not tells). Note: the patent source
      paragraphs contain "crucial" (q-0104-1) and "leverage" — the composer correctly did NOT lift
      them into prose; the essay's [0104] usage is a clean paraphrase ("puts every contribution on
      a consistent footing"). Semicolons: 3 prose semicolons join independent clauses (lines 42,
      54, 79) plus one parallel-list caption (line 27, FIG. 1). Three is NOT a cluster in a ~1450-
      word essay; the false-positive guard covers isolated/deliberate use, so no pass-1 finding —
      but the two figure-pointer joins (42, 79) are the slightly-mechanical residue cross-referenced
      under r2-F2, and the line-54 semicolon is the r1-F2 sentence-break residue. 1A cadence:
      paragraph lengths 2-6 sentences (essay 3-7 band; frame sections tighter by design); one
      load-bearing bold anchor only ("Align once, and the whole accumulation becomes integer
      arithmetic." — signature line 1, present once, byte-exact); no bold/bullet overuse, no emoji,
      no ALL-CAPS. Both declared signature lines byte-identical and present exactly once.

  - pass: pass-2-redundancy
    finding: "no new findings (carried r1-F3 low bookend accepted; figure captions add no redundancy)"
    scoped_to: |
      2A claim repetition: core verdict in §1 + §6 (acceptable lead/closing bookend); "down to the
      individual memory cell" motif now 2x (r1-F3, bookend, deliberate). "35-bit integer" appears
      in the FIG. 4 caption (line 15) AND §2 ¶5 (line 44) — caption<->prose overlap on different
      surfaces, composer deliberately varied the verb ("outputs" vs "hands out") to kill the
      verbatim echo; acceptable, not flagged. STRUCT-004 (4 triads) re-assessed for v2: all four
      track real content — "line up the points... add the digits... place the point once" and "One
      alignment, one integer sum, one conversion back" are the genuine 3-step mechanism; "process,
      voltage, and temperature corners" is the standard PVT term; the FIG. 4 caption's shift/
      two's-complement/adder-tree ordering follows the datapath — content-driven enumeration, not
      AI rule-of-three padding; not flagged. Declared signature lines (2) exempt and uncounted.
      2B/2C: after the r1-F1 and r1-F2 splits, no essay paragraph reaches 8 sentences or a
      single-idea 150-word wall (max is §3 ¶3 at 4 sentences post-split); figure captions are not
      body paragraphs.

  - pass: pass-3-fact-paraphrase
    finding: "verbatim + external + FIGURE-CAPTION grounding verified (one low precision note r2-F3)"
    scoped_to: |
      NEW figure-caption grounding (goal 2) — every caption claim checked against BOTH the
      figures-manifest (does the drawing show it?) and the [dddd] anchors (invention-summary
      Quotable spans):
        FIG. 4 header [0199][0011][0145]: shift-calc subtracts product exponent from block's
          largest = Emax-E (manifest "per-row shift calculation (Emax-E)"); Emax<=22/INT5 = q-0199-1;
          adder tree 426 integer-format = q-0011-3 + ref-table 426; 35-bit out = INT35 q-0145-1;
          "claim 1's align-then-integer-accumulate step" = claim-1 (b)+(c). No overclaim beyond the
          drawing. CLEAN.
        FIG. 1 [0006][0142][0145]: input buffer 102, CIM macro 101 (32x32 per manifest), mode
          decoding 110 sets format = q-0006-1, dequant 106 -> FP22 = q-0145-1. All elements are in
          the FIG.1 drawing (manifest). Mode decoding unit is description-not-claim, but the caption
          only describes the datapath figure; §3 carries the claim-scope discipline. CLEAN.
        FIG. 3 [0011]: "one column cell, where a single primitive product is made" = q-0011-1 +
          manifest "Column cell (Col 0, Row 0) detail". Short by design (body_figure_prose_covers_
          fully). CLEAN, no overclaim.
        FIG. 43 [0012][0015]: double-bitcell 4303, BC0/BC1 share bit lines / separate write-
          wordlines (manifest "BC0/BC1 per column, BL0-BL31 bit lines, ww10/ww11 write-word-lines");
          parallel bank load/feed = q-0012-1 + q-0015-1. Structure grounded in the drawing; the
          function is anchored to [0012]/[0015]. The scheme is description/aspect (claims 11-19
          canceled) and §4 prose correctly narrates it as unclaimed ("the document describes, in its
          summary passages rather than in the claims it is seeking"); the caption stays neutral.
          CLEAN.
      Re-verified verbatim byte-exact against input/patent.md (spans unchanged by the figure edit):
      [0005] conversion-step (line 31), [0011] both claim spans (36-38), [0147] pipelined-VMM (62),
      [0154] 100%-utilization + 256-VMM (71/67), [0118] scan-test roles (79), [0006] no-separate-
      pipelines (50), [0199] Emax=22 (15/44). Paraphrase anchors faithful: [0133], [0130], [0141],
      [0104], [0145], [0183] (64x64), [0002], [0012]/[0015], [0234]/[0262]/[0289]. Round-1 edits
      re-checked: r1-F4 claim-20 fold matches scope map; r1-F5 "rarely" preserves meaning; r1-F6
      "about" consistent with fact-check-log. External facts trace to fact-check-log and appear in
      # Sources: 10GW/2025-10-13, Jalapeno 2026-06-24 + end-2026 window (all "company-claimed"),
      Allegrucci Apple/Rain June-2024 (labeled press-reported, bound stated), OCP MX 2023-09 seven
      signatories. "Five inventors" — sixth-name trap avoided; # Sources patent entry lists exactly
      five. Claim scope uses "seek to protect"/"sought" throughout; pending never shown as granted.

  - pass: pass-4-logic-causality
    finding: "no new findings (carried r1-F5 low accepted)"
    scoped_to: |
      4A thesis-section alignment incl. the four placed figures: FIG. 4 (header) makes Axis 1
      visual; FIG. 1 + FIG. 3 (§2) carry Axis 1/Axis 2; FIG. 43 (§4) carries Axis 3 (double-
      buffering feeds the product-per-cycle effect). Placements match figures-rationale.md exactly
      (FIG.1 after §2 ¶1; FIG.3 after the [0011] blockquote; FIG.43 after the double-buffering
      para). No caption advances an out-of-spine claim. 4B causality: the central inference stays
      EVIDENTIARY ("the filing is primary evidence that 'OpenAI-designed' is literal engineering"),
      not causal — no claim that the patent caused the announcement; no correlation->causation
      drift introduced by the figures. Confounders still bounded (Rain/Allegrucci lineage §5;
      production/roadmap scoped out §6). The FIG. 4 caption's "claim 1's ... step, made literal"
      describes claim content, not grant status — no pending overreach. 4C arc: lead tension set
      and resolved at close; implication thesis-specific.

  - pass: pass-6-lead-conclusion-format
    finding: "no findings"
    scoped_to: |
      6A lead anchor: §1 ¶1 lands the discovery beat declaratively and puts patent+mechanism on the
      table by sentence 2; two-sided call by lead end (§1 ¶2). 6H DEFENSIVE-OPEN (firm posture,
      high-if-violated): ¶1 opens on discovery; the "pending application" insurance label sits in
      ¶2 AFTER the beat; and the NEW cover element (FIG. 4 caption) carries NO verdict-insurance
      fact and leads with the discovery framing ("the align-once core"), so it does not defensive-
      open the piece — its density is a pass-5 concern (r2-F1), not a 6H one. CLEAN. 6G OVER-HEDGE
      (firm posture, high-if-violated): §6 verdict leads with the CALL ("'OpenAI-designed' is
      literal engineering, and this filing is the primary evidence"); exactly ONE anti-hype guard,
      THIS-patent-specific ("nothing connects these circuits to Jalapeno... no source shows this
      macro running in silicon"), no generic truism; no false equivalence, no re-listed caveats, no
      safe-harbor boilerplate; firm landing on signature line 2. Symmetric check: no OVERREACH
      either (Pass 3 clean, scope stays "sought"). CLEAN. 6B frame closure: firm -> closing-forward-
      watching-event (end-2026 Jalapeno deployment; examination fate of claims 1/20), matches
      thesis-spine, NOT open-question. 6C Sources: "# Sources" once; 4 enum categories (Patents/
      Official statements/News & media/Technical specs); 5 entries across 4 categories -> subgrouped,
      all-or-nothing satisfied; no Papers so 6D N/A. 6E: em-dash 0 (gate-confirmed), all [dddd]
      4-digit, one # Sources. 6F title 63 chars, no em-dash/colon separator. 6I attention-budget:
      prosecution/status confined to the single pricing section §5 + one lead clause + §6 recap; no
      spend-motif spread; the figure integration added no procedure narration.

  - pass: pass-7-adversarial-reader
    finding: "no findings"
    scoped_to: |
      Read as impatient investor + skeptical pro-subject reader; each check decomposed yes/no.
      (1) Hook: §1 ¶1 lands the discovery register declaratively, call by lead end — PASS (the new
      cover caption precedes ¶1 visually but carries no deferred question / no insurance; its
      density is r2-F1, not a hook-deferral).
      (2) Header-as-claim: all six ## headers are assertions; header-only skim reconstructs the arc
      — PASS (unchanged; figures did not touch headers).
      (3) Steelman present + not overweight: strongest THIS-patent counter conceded compactly in §3
      ¶1-2 (headline features outside the claim set; MX is prior standardized art — "A skeptic can
      fairly call the core a known technique, implemented"); the affirmative return (§3 ¶3-4:
      claimed circuit specifics + primary-source depth) carries >= the concession's attention after
      the r1-F2 split; net-new (pending caveat spent in §5, not re-spent); no spend/procedure motif
      inside the beat — PASS, neither steelman-absent nor steelman-overweight.
      (4) Meta posturing: none; "none is guessed at here", "The registry facts, stated once", "The
      bounds priced in the previous section" are functional/bridge phrasing (exempt) — PASS.
      (5) Jargon as signpost: mechanism terms glossed functionally (FP8/6/4, mantissa/exponent,
      VMM, primitive product, CIM); the §3 three named blocks each get a one-clause gloss; caption
      reference numbers are conventional figure signposts (the cover "(426)" is inventory, noted in
      r2-F1) — PASS, no jargon-overdepth.
      (6) Stub/rhythm: no section markedly short (lead ~156w, §2 ~440w incl. captions, §3 ~320w,
      §4 ~233w, §5 ~250w, §6 ~190w); figure captions do not create stubs — PASS.
      (7) Thesis not over-restated: core verdict asserted in §1 + §6 (2 sections) + exempt
      signature lines — <=3 — PASS.

  - pass: pass-5-reader-perspective
    finding: "one medium (r2-F1 cover-caption density) + one low (r2-F2 un-shown figure pointers)"
    scoped_to: |
      5A engagement: r1-F1 and r1-F2 resolved the two round-1 density walls (§2 alignment para, §3
      machinery para) — both now split, each half under the 8-line wall. The remaining pass-5
      concern is the NEW cover caption (r2-F1). 5B stake clarity: every section feeds the verdict
      the investor came for (money thread intact); closing reads standalone. 5C mobile rendering:
      no body paragraph exceeds ~8 lines post-split; the densest text is the FIG. 4 cover caption
      (r2-F1). LONGSENT-001 x8 assessed: the 72-word flag is the FIG. 4 caption body (splitter
      artifact of ~3 real sentences; underlying density real -> r2-F1); the other seven are dense-
      but-information-bearing patent-mechanism sentences (§2 ¶1 von-Neumann, §4 ¶2 double-buffer
      "described not claimed", Allegrucci background, FIG. 1 caption datapath list) that carry
      claim/mechanism logic and fall under the deliverable-voice patent-domain exception — none is
      egregiously compressible without dropping load-bearing qualifiers. Figure value-add (goal 2):
      the four SELECTED figures (4,1,3,43) are referenced substantively, not token-dropped (FIG. 3
      is short BY DESIGN — body_figure_prose_covers_fully); the two CROSS-REFERENCED figures
      (38,45) point to un-shown drawings -> r2-F2.
```
