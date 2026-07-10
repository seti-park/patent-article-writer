```yaml
review_id: openai-us20260147536-editorial-review-3
draft_source: handoff/02-compose/essay-draft.md
draft_version_reviewed: 3
review_round: 3
review_timestamp: 2026-07-09T00:00:00Z
posture_applied: measured   # 3-tier posture = measured; edition declares closing_posture: firm,
                            # so 6G/6H/6I escalate to HIGH if violated. Checked below — no firm-
                            # closing escalation triggered.
closing_posture_declared: firm
gates_precomputed: PASS (0 fails). Warn signals weighed below: STRUCT-004 (4 triads),
                   DUPE-001 x2 (deliberate §1->§6 "down to the individual memory cell" bookend),
                   LONGSENT-001 x8 (incl. one 72-word flag in §2 ¶6 — the signature-line
                   paragraph, protected surface). Only FIG. 1/3/4/43 tokens remain (FIGUSE-002
                   cleared).
reviewer_note: |
  Fresh round-3 reviewer, no memory of composing or of rounds 1-2. This is the round where a
  clean result would be the FIRST clean of a double-clean acceptance, so grounding, the
  both-direction verdict proportionality, the lead hook, the steelman, and the four figure
  captions were re-scrutinized from the source rather than trusted from prior logs. Re-review
  protocol followed: every round-2 finding_id (r2-F1, r2-F2, r2-F3) is ruled on FIRST — each
  "applied" disposition verified in draft v3 with the fixed span quoted and neighbors re-counted
  — then the 7 passes hunt new findings. The round-1 edits (r1-F4/F5/F6) were already verified-
  landed and accepted in round 2; they were incidentally re-confirmed intact during pass-3
  grounding and are noted but not re-opened (N-1 = round 2 is the carried set).
overall_assessment: pass   # 0 critical, 0 high, 0 medium, 0 low new findings. All three round-2
                           # dispositions landed. This is the FIRST clean of a candidate
                           # double-clean acceptance — earned by re-derivation, not inherited.

# ===========================================================================
# PART A — CARRIED FINDING RULINGS (round-2 dispositions verified in draft v3)
# All three round-2 findings were disposed 'applied'. Each verified below by
# quoting the landed span and re-counting the affected paragraph bands.
# ===========================================================================

carried_findings:

  - finding_id: r2-F1
    round2_severity: medium
    disposition_claimed: applied (trim FIG. 4 cover caption ~86w/5 sentences -> 52w/3 sentences;
                         drop the "(426)" reference number and the shift-arithmetic narration;
                         keep the align-once/adder-tree core + anchors + claim-1 tie)
    ruling: LANDED — accept
    verification: |
      Draft v3 line 15 now reads, byte-for-byte the composer's proposed shape:
      "FIG. 4: the align-once core, drawn as circuitry. Each product's mantissa shifts onto the
      block's largest exponent (at most 22 here, a 5-bit integer [0199]), and the column adder
      tree sums the aligned mantissas as plain integers [0011], one 35-bit result per column
      [0145]. This is claim 1's align-then-integer-accumulate step, made literal."
      Word count ~53 across 3 sentences (was ~86 / 5). Grep of the whole draft confirms the
      "(426)" reference number, the "two's-complement" standalone sentence, and the
      "shift-calculation" narration are GONE (zero hits). The cover caption now carries ZERO
      reference numerals (SURF-003 cover-numeral budget fully cleared; the 72-word LONGSENT
      splitter artifact that r2-F1 diagnosed on the OLD caption is dissolved — the current
      72-word flag has MOVED to §2 ¶6, ruled separately in pass-5 scoped_to).
      Grounding preserved and re-verified against the invention-summary: Emax<=22 / INT5 =
      q-0199-1; adder tree sums in integer format = q-0011-3; one 35-bit result per column =
      INT35 q-0145-1; "claim 1's align-then-integer-accumulate step" = claim 1 (b)+(c). No claim
      beyond FIG. 4's drawing (manifest: per-row shift calc Emax-E, 2's-complement shift, feeding
      the column adder tree 426): the caption describes exactly the shift-onto-largest-exponent ->
      integer adder tree the sheet draws, and glosses the adder tree's INT35 output with its
      anchor. No grant-status overreach (describes claim CONTENT, not grant). No neighbor
      regressed: the caption is not a body paragraph and FIG. 4 remains referenced in the header
      image, so no orphan.

  - finding_id: r2-F2
    round2_severity: low
    disposition_claimed: applied (remove both prose cross-references to un-shown figures —
                         "; ... FIG. 38 shows it as physical circuitry" in §2 ¶4 and
                         "; FIG. 45 draws one such scan-wired double bitcell." in §5 ¶3;
                         keep the [0118] scan-test verbatim quote)
    ruling: LANDED — accept
    verification: |
      Grep of the draft for "FIG.?\s*\d+" returns exactly five hits, all in the intended set:
      line 13 (header image FIG. 4), line 15 (FIG. 4 caption), line 27 (FIG. 1 caption), line 40
      (FIG. 3 caption), line 69 (FIG. 43 caption). NO FIG. 38 and NO FIG. 45 anywhere in the
      draft — both prose cross-references are removed.
      §2 ¶4 (line 42) now ends the analogy sentence at "Here the lining up is a bit shift." and
      continues cleanly "The macro finds the largest exponent among the 32 products in a block
      ..." — the FIG. 4-as-functional-block / FIG. 38-as-circuitry clause is gone; 3 sentences,
      in the 3-7 band, no neighbor regressed.
      §5 ¶3 (line 79) keeps the [0118] verbatim quote intact ("serve both compute storage and
      scan-test roles" [0118]) and closes with a period before "Concept filings rarely carry
      clock margins and scan modes." — the FIG. 45 clause is gone; 5 sentences, in band.
      Both deletions also removed the two "slightly mechanical" prose semicolon joins the round-2
      reviewer noted; the draft's remaining semicolons are non-figure joins. No [dddd] anchor and
      no verbatim quote lost. gate_figure_use / FIGUSE cleared (FIGUSE-002 x2 gone, per the
      round-3 gate signal). The upstream figure-selection.md tokenization fix (so "FIG. 38/42" /
      "FIG. 45/46" no longer tokenize as selected) is what makes the removal orphan-safe; the
      orchestrator reports it landed, and gate_figure_use PASS confirms no orphan re-triggered.

  - finding_id: r2-F3
    round2_severity: low
    disposition_claimed: applied (§6 "priority date eleven months older" -> "priority date about
                         eleven months older", uniform with §1 ¶1's hedged "about eleven months
                         later"; date-arithmetic precision, verdict untouched)
    ruling: LANDED — accept
    verification: |
      Draft v3 line 83 reads: "...carrying an OpenAI-assigned priority date about eleven months
      older than the announcement that made the phrase famous." The "about" qualifier is present.
      Consistent with fact-check-log ("use ... 'about eleven months' for the gap"; true gap ~10
      months 21 days from 2024-11-22 to 2025-10-13). Jurisdiction fence honored: this is a
      precision qualifier on DATE ARITHMETIC, not a hedge on the verdict — the surrounding call
      ("'OpenAI-designed' is literal engineering, and this filing is the primary evidence") is
      untouched and firm, and §6 still states the raw dates two sentences later ("The announcement
      is from October 2025. The engineering is dated November 2024."), keeping the ~11-month gap
      reader-verifiable. gate_hedge firm-posture status unaffected (verified clean under 6G below).
      Standing sub-question (does §1 ¶2's flat "Eleven months before" now read inconsistently?):
      independently re-ruled ACCEPTABLE — §1 ¶2 is adjacent to ¶1's "about", so the just-
      established approximation carries (exactly the inherit the round-1 finding r1-F6 endorsed
      and round-2 accepted). Not re-opened. The only bare instance is §1 ¶2, and it is not
      load-bearing beyond the approximation ¶1 already set.

# Carried round-1 edits (r1-F4/F5/F6) — verified-landed and accepted in round 2; incidentally
# re-confirmed intact in draft v3 during pass-3 grounding, NOT re-opened (N-1 = round 2):
#   r1-F4: §3 ¶3 "that unit is the one piece independent claim 20 pulls up into itself" — matches
#          Claim scope map (claim 20 = triad + shift-calc-and-select-decoding unit). Intact.
#   r1-F5: §5 ¶3 "Concept filings rarely carry clock margins and scan modes." — categorical
#          narrowed, verdict firm. Intact.
#   r1-F6: §1 ¶1 "about eleven months later". Intact.

# ===========================================================================
# PART B — NEW ROUND-3 FINDINGS
# ===========================================================================

findings: []   # No new findings at any severity. Rigor statement: this is NOT a first-draft
               # clean — draft v3 has absorbed 9 findings across two revision rounds, and the
               # specific surfaces the orchestrator flagged (grounding byte-exactness, both-
               # direction verdict proportionality, lead hook, steelman weight, figure-caption
               # grounding) were each re-derived from source below, not inherited. The clean
               # result is earned; see the falsifiable scoped_to on every pass in PART C.

# ===========================================================================
# PART C — CLEAN PASSES (falsifiable scoped_to — exactly what was checked)
# ===========================================================================

  - pass: pass-1-voice-anti-ai
    finding: "no findings"
    scoped_to: |
      1B mechanical: greped the essay's connective prose (double-quoted spans and blockquotes
      excluded) for the full Tier-1 banned word list (delve/tapestry/vibrant/pivotal/crucial/
      fostering/underscore/meticulous/intricate/testament/garner/bolstered/showcase/enhance/
      enduring/valuable/boasts/renowned/multifaceted/leverage/navigate/resonate/nestled/
      groundbreaking/interplay) plus Tier-2 co-occurrence tells (seamless/robust/realm/utilise/
      facilitate/commence) and rhetorical patterns (not-just-X-but-Y, not-only-but,
      despite-the-, "it is worth noting", "in summary"/"to recap"/"in conclusion", copula
      avoidance "represents a"/"serves as a"/"stands as a", sentence-initial Additionally/
      Moreover/Furthermore, safe-harbor "remains to be seen"/"only time will tell"): ZERO hits
      in the essay's own prose (grep-confirmed). Source-contamination check: the patent
      paragraphs [0104] ("crucial", q-0104-1) and [0015] ("seamless") carry banned words; the
      composer correctly did NOT lift them — [0104] is paraphrased as "puts every contribution
      on a consistent footing", and [0015]'s "seamless switching" is not imported (only "minimize
      compute stalls during updates" is quoted). Em-dash grep (Pass 6 territory, cross-checked
      here): ZERO en/em dashes in the draft. Semicolons: after the r2-F2 removals, the remaining
      prose semicolons join independent clauses non-mechanically (e.g. the FIG. 1 parallel-list
      caption on line 27); not a cluster in a ~1450-word essay — false-positive guard covers
      deliberate use, no finding. 1A cadence: paragraph lengths 2-6 sentences (essay 3-7 band;
      §1/§6 frame sections tighter by design); exactly one load-bearing bold anchor
      ("Align once, and the whole accumulation becomes integer arithmetic." — signature line 1,
      byte-exact, present once); no bold/bullet overuse, no emoji, no ALL-CAPS emphasis. Both
      declared signature lines present exactly once and byte-identical to thesis-trace.md.

  - pass: pass-2-redundancy
    finding: "no findings"
    scoped_to: |
      2A claim repetition: the core verdict lands in §1 (¶2) + §6 — acceptable lead/closing
      bookend, not restatement padding. The "down to the individual memory cell" depth motif is
      DUPE-001 x2 — §1 ¶1 (line 19) and §6 (line 83) — the intended lead->closing bookend
      (§1 ¶2's adjacent-lead echo was already varied to "written to the bitcell" in r1-F3);
      deliberate, not flagged. "35-bit" appears in the FIG. 4 caption (line 15), §2 ¶5 (line 44),
      and §4 context — caption<->prose overlap on different surfaces with varied verbs ("sums ...
      one 35-bit result" vs "hands out a 35-bit integer"); not a same-value-3x-no-new-context
      violation. STRUCT-004 (4 triads) re-assessed for v3: (1) "line up the points ... add the
      digits ... place the point once" (line 42) = the genuine 3-step decimal-addition analogy;
      (2) "One alignment, one integer sum, one conversion back" (line 46) = the real 3-step
      mechanism; (3) "process, voltage, and temperature corners" (line 79) = the standard PVT
      term of art; (4) "latch-level bitcell circuits, non-overlapping clock generation, setup-time
      relations, and timing checks ..." (line 79) = a content-driven depth enumeration (4-item,
      not rule-of-three padding). All content-driven; not flagged. Declared signature lines (2)
      exempt and uncounted. 2B/2C: after the r1-F1 + r1-F2 splits and the r2-F1/F2 trims, no essay
      paragraph reaches 8 sentences or a single-idea 150-word wall; the densest body paragraph is
      §3 ¶3 (~104 words / 4 sentences, under 150, in the 3-7 band). Figure captions are not body
      paragraphs.

  - pass: pass-3-fact-paraphrase
    finding: "no findings — verbatim byte-exact, paraphrase faithful, figure captions grounded"
    scoped_to: |
      3A VERBATIM (re-checked byte-for-byte against input/patent.md AND invention-summary
      Quotable spans / Quote anchor table, since a clean grounding chain is the acceptance
      spine): [0133] "reducing the von Neumann bottleneck" (line 19) = q-0133-2 partial, exact;
      [0005] full conversion-step blockquote (lines 31-32) = q-0005-1, exact; [0011] both claim
      spans (lines 36-38) = q-0011-2 + q-0011-3, exact; [0006] "without requiring separate
      conversion pipelines or dedicated cores for each format" (line 50) = q-0006-2, exact;
      [0147] pipelined-VMM blockquote (lines 62-63) = q-0147-1, exact; [0015] "minimize compute
      stalls during updates" (line 67) = q-0015-1 partial, exact; [0154] "In some embodiments,
      100% utilization of the compute engine 100 may be possible." (line 71) = q-0154-3, exact;
      [0118] "serve both compute storage and scan-test roles" (line 79) = q-0118-1 partial, exact;
      claims "(canceled)" (line 75) = registry fact, exact. All figure-caption anchors re-verified:
      [0199] Emax<=22/INT5 (lines 15, 44) = q-0199-1, exact.
      3A/3C PARAPHRASE (no drift): [0142]/[0130] activation-stream / stationary-weight datapath
      faithful; [0131] "shrinking numbers ... speeds up deep learning with minimal accuracy loss"
      = q-0131-1 faithful; [0104] "consistent footing" = q-0104-1 "consistent scale" faithful
      (banned "crucial" dropped); [0145] INT35+INT5->FP22, "5-bit exponent" = INT5 (Layer 2 #6),
      grounded; [0141] shared-scale MX block, block size 32, faithful; [0139] "synthesizable
      integer adder tree rather than floating-point hardware" = Layer 3, exact-sense; [0183]
      "64 by 64 half adders and full adders" over the 32x32 array = q-0183-1 faithful; [0002] VMM
      dominates AI training/inference, faithful; [0012] parallel write+VMM double-bitcell,
      correctly narrated as description-not-claim; [0234]/[0262]/[0289] tape-out-depth list = Layer
      4, faithful. NO fact introduced beyond the Quotable spans; NO polarity/scope/certainty
      mutation. FOUR FIGURE CAPTIONS re-checked against BOTH the manifest (does the sheet draw it?)
      and anchors: FIG. 4 (no overclaim beyond the drawn shift-calc + adder tree 426); FIG. 1
      (input buffer/CIM 101 32x32/mode-decode 110/dequant 106 all in the FIG. 1 sheet; mode-decode
      is description but the caption only describes the datapath figure, claim discipline carried in
      §3); FIG. 3 (one column cell, short by design); FIG. 43 (BC0/BC1 share BL, separate write-
      wordlines — matches the sheet; function anchored [0012]/[0015]; caption stays neutral on the
      canceled-claim status). 3B EXTERNAL: 10GW/2025-10-13 (tier-1) -> Official statements; Jalapeño
      2026-06-24 + end-2026 window (tier-1, "company-claimed") -> Official statements; Allegrucci
      ~17yr Apple / Rain head-of-hardware June-2024 (tier-3, labeled press-reported, bound stated:
      "no document here says where any of the five sat on the provisional date") -> News & media;
      OCP MX 2023-09 seven signatories (tier-2) -> Technical specs. Every inline "(see Sources, X)"
      pointer resolves to the correct category. Sixth-inventor trap avoided ("Five inventors"; the
      # Sources patent entry lists exactly five). Claim scope uses "seek to protect" / "sought" /
      "wants to own" / "ends up owning" throughout — pending never shown as granted. Minor
      approximations noted and cleared as acceptable non-load-bearing rounding: "a year before"
      (line 52) for the ~14-month MX(2023-09)->priority(2024-11) gap (understates, weakens the
      essay's own concession, harmless); "ten gigawatts" spelled (fact-check-log "10 gigawatts",
      value identical).

  - pass: pass-4-logic-causality
    finding: "no findings"
    scoped_to: |
      4A thesis-section alignment: all four spine axes land and no section advances an out-of-spine
      claim — Axis 1 (claim-1 triad) + Axis 2 (problem) -> §2; Axis 4 (baseline) + steelman -> §3;
      Axis 3 (effect: product-per-cycle, double-buffered weights narrated as unclaimed) -> §4;
      pricing (registry facts once) -> §5; verdict frame -> §1/§6. Figure placements match
      figures-rationale.md (FIG. 1 after §2 ¶1; FIG. 3 after the [0011] blockquote; FIG. 43 after
      the double-buffering paragraph); no caption advances an out-of-spine claim. 4B causality: the
      central inference is EVIDENTIARY, not causal — "the filing is primary evidence that
      'OpenAI-designed' is literal ... engineering" and "The design record says the work started
      earlier"; the essay never claims the patent CAUSED the announcement, so no
      correlation->causation drift from the 11-month gap. Counterfactual/mechanism basis for the
      tape-out-depth inference is stated ("Concept filings rarely carry clock margins and scan
      modes. Documents written toward manufacture do"). Confounders bounded: Rain/Allegrucci lineage
      named and priced in §5; production/silicon scoped out in §6 ("no source shows this macro
      running in silicon", "nothing connects these circuits to Jalapeño"). 4C arc: lead tension
      (announcement vs priority date) set in §1 and resolved at close; the implication is thesis-
      specific (this filing's dated transistor-level depth), not a generic patent implication.

  - pass: pass-5-reader-perspective
    finding: "no findings"
    scoped_to: |
      5A engagement: r1-F1 and r1-F2 resolved the two round-1 density walls (both split, verified
      intact in v3); the r2-F1 caption trim removed the highest-traffic density point (the cover
      caption). No remaining density wall of 3+ consecutive mechanism paragraphs without surface.
      5B stake clarity (money thread, reader-profile rule 4): every section feeds the verdict the
      investor came for — §2 mechanism ties to "the part OpenAI wants to own", §3 scope ties to
      "the thesis rests on the record", §4 throughput to design intent, §5 depth to "reads like
      engineering rather than positioning", §6 the call; the closing reads standalone. 5C mobile
      rendering: re-counted the densest surviving paragraph, §3 ¶3 (line 54), ~104 words / 4
      sentences = ~8.7 lines at the /12 mobile heuristic, ~7 lines at /15 (X Articles typography is
      12-15 words/line) — BORDERLINE at /12, clean at /15; it is the post-r1-F2 split result already
      accepted in round 2, carries the load-bearing claim-scope resolution (named machinery ->
      dependent claims -> what they buy) as one logical unit, sits in the 3-7 sentence band and
      under 150 words, and re-splitting a paragraph already split once would fragment the §3 payoff.
      Judged ACCEPTABLE, not a 5C finding. LONGSENT-001 x8 assessed: the 72-word flag sits in §2 ¶6
      (line 46), the signature-line paragraph — a splitter artifact spanning the bold signature line
      ("Align once, and the whole accumulation becomes integer arithmetic.") and its neighbors; the
      signature line is protected surface (reader-energy §5) — not sanded, not counted; the non-
      signature sentence in that paragraph (~44 words, a causal claim on why the adder tree is
      integer) falls under the deliverable-voice patent-domain long-clause exception. The other
      seven LONGSENT flags are dense-but-information-bearing mechanism/claim/attribution sentences
      (§2 ¶1 von-Neumann gloss, §2 ¶5 dequant, §3 claim-scope, §4 ¶2 double-buffer "described not
      claimed", §5 Allegrucci attribution) — each carries a load-bearing gloss/qualifier and none is
      egregiously compressible; none breaks readability for the advanced-HS-to-early-undergrad
      reader. Figure value-add (goal 2): the four selected figures (4/1/3/43) are referenced
      substantively (FIG. 3 short by design, body_figure_prose_covers_fully); no un-shown-figure
      pointers remain after r2-F2.

  - pass: pass-6-lead-conclusion-format
    finding: "no findings"
    scoped_to: |
      6A lead anchor: §1 ¶1 puts the patent + mechanism on the table by sentence 2 (discovery beat
      declarative); the full two-sided call lands by the lead's end (§1 ¶2 — evidence side + pending-
      application pricing side). 6B frame closure: the corporate-narrative-friction lead is closed in
      §6 ("The chip story was told in 2025. The design record says the work started earlier..."); firm
      posture -> closing-forward-watching-event (end-2026 Jalapeño deployment; examination fate of
      claims 1/20), matches thesis-spine, NOT closing-open-question. 6C Sources: "# Sources" appears
      exactly once (line 89); 4 categories (Patents/Official statements/News & media/Technical specs),
      all inside the 5-enum; 5 entries across 4 categories -> subgrouped, all-or-nothing satisfied
      (every entry sits under a ## subheading); no Papers so 6D N/A. 6E: em-dash 0 (grep + gate
      confirmed), every [dddd] anchor 4-digit and resolving, one # Sources. 6F title: "OpenAI's Chip
      Patent Does Floating-Point Math on Integer Adders" — no em-dash, no colon, 63 chars (< 70,
      SURF-001 clean), Title Case. 6G OVER-HEDGE (firm posture, HIGH-if-violated) — re-derived: the
      §6 verdict LEADS with the call ("'OpenAI-designed' is literal engineering, and this filing is
      the primary evidence"), not a qualifier; exactly ONE anti-hype guard, and it is THIS-patent-
      specific ("nothing connects these circuits to Jalapeño ... no source shows this macro running
      in silicon"), never a generic "patents don't guarantee production" truism; caveats are
      REFERENCED not re-listed ("The bounds priced in the previous section scope that call, and they
      do not reverse it"); no false equivalence, no safe-harbor boilerplate. Symmetric check —
      OVERREACH: none; scope stays "sought"/"ends up owning" (pending), Pass 3 clean, the Rain/
      Allegrucci confounder is priced. Verdict is evidence-proportionate in BOTH directions. CLEAN.
      6H DEFENSIVE-OPEN (firm posture, HIGH-if-violated): §1 ¶1 opens on the discovery beat; the
      "pending application" insurance label sits in §1 ¶2 AFTER the beat; the cover caption (FIG. 4)
      carries no verdict-insurance fact and leads with discovery framing ("the align-once core") —
      no insurance stacked ahead of the payoff; first-two-lines test passes. CLEAN. 6I ATTENTION-
      BUDGET: prosecution/status narration confined to the single pricing section §5 plus one lead
      clause plus the §6 recap; no spend-motif spread across lead/body/closing; no procedure narration
      inside the steelman (SURF-007 clean). CLEAN.

  - pass: pass-7-adversarial-reader
    finding: "no findings"
    scoped_to: |
      Read cold as the impatient investor + the skeptical pro-subject reader; each check decomposed
      yes/no with a quoted span.
      (1) HOOK: §1 ¶1 lands the discovery register declaratively ("There is a published OpenAI patent
      that designs an AI chip down to the individual memory cell. The math runs inside the memory
      array itself...") — no deferred question, no verdict-insurance fact ahead of the beat; the full
      two-sided call lands by the lead's end (§1 ¶2). The cover caption precedes ¶1 visually but leads
      with discovery, not insurance. PASS.
      (2) HEADER-AS-CLAIM: all six ## headers are assertions and a header-only skim reconstructs the
      arc — on file before news / multiply-FP-add-int-convert-once / headline described but circuits
      claimed / result every cycle / pending but tape-out depth / literal engineering, two dates. No
      gap-framed header buries the discovery. PASS.
      (3) STEELMAN present + not overweight (THIS-patent): the strongest pro-subject counter is
      conceded compactly and specifically in §3 ¶1-2 — the format-agility headline features are
      description not claims, and block-scaled/MX is prior standardized art ("A skeptic can fairly
      call the core a known technique, implemented") — a THIS-patent objection, not a generic truism.
      Weighed the ratio: concession ~160 words (§3 ¶1-2) vs affirmative return ~210 words (§3 ¶3-4:
      claimed circuit specifics + primary-source depth + "the thesis rests on the record") — the
      affirmative core carries >= the concession. Net-new (the pending-status caveat is spent in §5,
      not re-spent here); no spend/procedure lexicon inside the beat. PASS — neither steelman-absent
      nor steelman-overweight.
      (4) META: no reader-instruction / essay-as-object; "none is guessed at here", "That stays
      labeled as background", "The registry facts, stated once", "The bounds priced in the previous
      section" are functional scope / bridge phrasing (exempt). PASS.
      (5) JARGON as signpost: FP8/FP6/FP4, mantissa/exponent, VMM, primitive product, CIM,
      dequantization each get a one-clause functional gloss; the §3 three named blocks (shift-calc
      unit, shift register, log-mux tree) are signposted, not deep-dived past the claim-specificity
      insight. PASS — no jargon-overdepth.
      (6) STUB/rhythm: section word counts ~156 / ~437 / ~320 / ~233 / ~245 / ~191 — §1 and §6 (frame)
      appropriately tighter than the mechanism body; no section markedly short. PASS.
      (7) THESIS not over-restated: the full core verdict is asserted in §1 (¶2) + §6 (2 sections);
      §3/§5 carry supporting sub-claims (scope resolution, depth evidence), not the verdict
      restatement; the two declared signature lines are exempt. <= 3. PASS.
```
