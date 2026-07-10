```yaml
review_id: openai-us20260147536-editorial-review-1
draft_source: handoff/02-compose/essay-draft.md
review_round: 1
review_timestamp: 2026-07-09T00:00:00Z
posture_applied: measured   # 3-tier posture = measured; edition is a firm-closing verdict
                            # (closing_posture: firm) so 6G/6H/6I escalate to high IF violated.
                            # Both checked and clean, so no firm-closing escalation was triggered.
closing_posture_declared: firm
gates_precomputed: PASS (0 fails); warn signals DUPE-001, LONGSENT-001 x7, STRUCT-004 weighed below
overall_assessment: revise-recommended

# ---------------------------------------------------------------------------
# REAL FINDINGS (medium first, then low)
# ---------------------------------------------------------------------------

findings:
  - finding_id: r1-F1
    pass: pass-5-reader-perspective
    location: "§2 (Multiply in Floating Point...), paragraph 4 — 'The alignment is the move you already know...' through '...converts the result to FP22, a wider floating-point format, in one step [0141] [0145].'"
    severity: medium
    severity_under_default_posture: medium
    finding: |
      The single densest mechanism paragraph in the essay: ~125 words across 5 sentences,
      carrying the analogy + bit-shift + max-exponent search + the worked FP8xFP6 example
      (22 -> 5-bit) + the INT35/INT5 output + the FP22 dequantization, all in one block.
      On X Articles mobile typography (~12 words/line) this renders ~10 lines, over the
      pass-5 5C >8-line wall threshold. For the target reader (advanced-HS to early-undergrad),
      the alignment analogy and the numeric worked-example are two separable comprehension
      beats fused into one wall. Grounding is clean (all anchors verified); this is purely a
      mobile-rendering / density-pacing concern, not an accuracy one.
    recommendation: |
      Split into two paragraphs. Natural seam: end paragraph A at "...before the sum [0104]."
      (analogy + what the shift does), start paragraph B at "The numbers stay small by
      design:" (the worked example + INT35/INT5 + FP22 output). Each half then renders
      ~4-5 mobile lines. No wording change to the mechanism required.

  - finding_id: r1-F2
    pass: pass-5-reader-perspective   # cross-pass with pass-2 2C (paragraph earn) and pass-2 2B (sentence length)
    location: "§3 (The Headline Features Are Described...), paragraph 3 — 'The claim set answers with specificity...' through '...the thesis rests on the record.'"
    severity: medium
    severity_under_default_posture: medium
    finding: |
      The essay's densest paragraph: 7 sentences, ~155 words (over the 150-word 2C earn
      threshold), and it carries at least two distinct ideas tangled together — (a) the
      specific named machinery the dependent claims add, and (b) the MX-is-a-format /
      circuits-are-claimed distinction plus the return to the affirmative core. It also
      contains the essay's longest connective sentence (~48 words: "The sought dependent
      claims wrap the triad in named machinery: a shift calculation and select decoding unit
      that works out each product's shift [0200], shift registers sized by rule to the maximum
      exponent plus the mantissa bit count [0202], and a logarithmic multiplexer tree that
      does the shifting in stages [0206]."), a triple-clause list naming three circuit blocks
      the target reader meets for the first time. On mobile this paragraph is ~13 lines.
      Each named block does get a one-clause functional gloss (good practice per reader-profile
      rule 1), so this is a density/pacing finding, not a jargon-overdepth or grounding one.
    recommendation: |
      Split after the "64 by 64 half adders" sentence: paragraph A = the named-machinery
      specifics (claim-set answers with specificity + the three blocks + adders-saved),
      paragraph B = "That is the distinction the skeptical read misses..." through the
      affirmative-core return. Optionally break the ~48-word machinery sentence into two
      (e.g. lead with the shift-calc unit, then a second sentence for the register-sizing rule
      and the log-mux tree). This is the one spot a scrolling investor is most likely to stall.

  - finding_id: r1-F3
    pass: pass-2-redundancy
    location: "'down to the individual memory cell' — §1 ¶1 ('designs an AI chip down to the individual memory cell'), §1 ¶2 ('written down to the individual memory cell'), §6 ('specified down to the individual memory cell'). Gate signal DUPE-001."
    severity: low
    severity_under_default_posture: low
    finding: |
      Assessed the gate's DUPE-001 warn. The phrase is a deliberate depth-motif carrying the
      thesis's evidentiary core (transistor-level design). It is NOT a declared signature line
      (thesis-trace declares only two, neither is this), so echo/count rules apply. Two of the
      three uses are defensible: the §1 -> §6 pairing is the acceptable lead-to-closing recap
      (pass-2 2A). The genuine echo is §1 ¶1 and §1 ¶2 repeating the exact phrase in adjacent
      paragraphs of the lead — a tight verbatim repeat that reads as an editing artifact rather
      than intended cadence.
    recommendation: |
      Vary the §1 ¶2 instance only (e.g. "specified to the transistor" / "written to the
      bitcell"), so the motif lands three times across the arc rather than twice in one breath.
      Keep the §1 ¶1 introduction and the §6 recap. Do not sand it to zero — the motif is
      load-bearing.
    quote: "written down to the individual memory cell"

  - finding_id: r1-F4
    pass: pass-3-fact-paraphrase   # claim-adequacy / claim-scope precision
    location: "§3, sentence 'The sought dependent claims wrap the triad in named machinery: a shift calculation and select decoding unit...'"
    severity: low
    severity_under_default_posture: low
    finding: |
      The shift-calculation-and-select-decoding unit is grouped under "the sought dependent
      claims." Per invention-summary.md Claim scope map, that unit is in dependent claim 2 AND
      is "folded into the independent claim" 20 ("claim 20 (independent): Same triad as claim 1
      plus the shift calculation and select decoding unit"). The essay elsewhere tells the
      reader claims 1 and 20 seek only "the multiply-align-add triad," so a reader would infer
      the shift-calc unit is dependent-only. This UNDERSTATES what the independent claim reaches
      (the safe / conservative direction — no overreach on OpenAI's sought scope), so it is a
      precision note, not a mislead. shift registers (claim 3) and the log-mux tree (claims 6-9)
      are correctly dependent-only.
    recommendation: |
      Optional precision fix, no hedge involved: either move the shift-calc unit out of the
      "dependent claims" grouping, or add a half-clause that independent claim 20 folds the
      shift-calc unit in (e.g. "...a shift calculation and select decoding unit — which claim 20
      pulls up into the independent claim itself — ..."). Register-sizing and log-mux tree stay
      as the dependent-only specifics.

  - finding_id: r1-F5
    pass: pass-4-logic-causality
    location: "§5, 'Concept filings do not carry clock margins and scan modes. Documents written toward manufacture do, and this one reads like engineering rather than positioning.'"
    severity: low
    severity_under_default_posture: low
    finding: |
      The load-bearing inference (tape-out-depth => real engineering, not positioning) rests on
      a categorical premise: "Concept filings do NOT carry clock margins and scan modes." That
      is broadly true and rhetorically strong, but a skeptical pro-subject reader can name a
      counterexample (a thorough provisional can include implementation detail defensively), so
      the categorical is slightly overstated. The conclusion is already appropriately evidential
      ("reads like engineering rather than positioning"), which contains the risk.
    recommendation: |
      Narrow the categorical, not the verdict (jurisdiction fence: narrow the claim, never add a
      caveat to the call): "Concept filings rarely carry clock margins and scan modes." Preserves
      the contrast and the punch while removing the absolute a skeptic would poke. The "reads
      like engineering" landing stays firm.

  - finding_id: r1-F6
    pass: pass-3-fact-paraphrase   # external-fact precision
    location: "§1 ¶1 ('eleven months later'), §1 ¶2 ('Eleven months before'), §6 ('eleven months older')"
    severity: low
    severity_under_default_posture: low
    finding: |
      fact-check-log.md instructs, in its Notes, to use "about eleven months" for the gap
      between the 2024-11-22 provisional priority date and the 2025-10-13 announcement (the
      true gap is ~10 months 21 days). The draft states "eleven months" without a hedge in all
      three uses, presenting a rounded figure as exact. The gap IS the essay's hook, so the
      figure is load-bearing. This is defensible rounding, but it deviates from the explicit
      design instruction.
    recommendation: |
      Add "about"/"roughly"/"nearly" to at least the first instance (§1 ¶1: "on 13 October
      2025, about eleven months later"), consistent with fact-check-log. The other two can
      inherit the approximation once established. Not a hedge on the verdict — a precision fix
      on a date arithmetic.
    related_fact_entry: openai-broadcom-10gw-2025-10-13

# ---------------------------------------------------------------------------
# CLEAN PASSES (falsifiable scoped_to — states exactly what was checked)
# ---------------------------------------------------------------------------

  - pass: pass-1-voice-anti-ai
    finding: "no findings"
    scoped_to: |
      1B mechanical: greped connective prose (quotes/blockquotes excluded) for the full Tier-1
      banned list (delve/leverage/navigate/crucial/underscore/enhance/robust/seamless/realm/
      utilise/facilitate/commence, etc.) and rhetorical patterns (not-just-X-but-Y,
      despite-the-challenges, copula avoidance represents/constitutes/serves-as/stands-as,
      section-summaries In-summary/To-recap/In-conclusion, sentence-initial
      Additionally/Moreover/Furthermore, "it is worth noting"): ZERO hits in the essay's own
      prose. Note: the patent source [0154]/[0006] themselves contain "leverage", "crucial",
      "Additionally", "Furthermore", "In summary" — the composer correctly did NOT lift any of
      them into the essay. 1A cadence: paragraph lengths 3-7 sentences (§ word counts 158/396/
      312/205/243/190); one load-bearing bold anchor only ("Align once, and the whole
      accumulation becomes integer arithmetic."), no bold/bullet overuse, no emoji. STRUCT-004
      (4 rule-of-three triads) assessed: the triads track the real three-step mechanism
      ("line up the points... add the digits... place the point once"; "One alignment, one
      integer sum, one conversion back") — content-driven enumeration, not AI-cadence padding;
      not flagged.

  - pass: pass-6-lead-conclusion-format
    finding: "no findings"
    scoped_to: |
      6A lead anchor: ¶1 puts the patent + mechanism on the table by sentence 2; full two-sided
      call lands by the lead's end (§1 ¶2). 6B frame closure: lead's corporate-narrative-friction
      (announcement vs priority date) is closed in §6 ("The chip story was told in 2025. The
      design record says the work started earlier..."); firm posture -> closing-forward-watching-
      event (the two dates), matches thesis-spine, NOT closing-open-question. 6C Sources: "# Sources"
      once; 4 categories (Patents/Official statements/News & media/Technical specs), all in enum;
      5 entries across 4 categories -> subgrouped, all-or-nothing satisfied; no Papers so 6D N/A.
      6E: em-dash 0 (gate-confirmed), all [dddd] anchors 4-digit, one # Sources. 6F title: "OpenAI's
      Chip Patent Does Floating-Point Math on Integer Adders" — no em-dash, 63 chars (<70, SURF-001
      clean). 6G OVER-HEDGE (firm posture, high if violated): verdict leads with the CALL
      ("'OpenAI-designed' is literal engineering, and this filing is the primary evidence"), not a
      qualifier; exactly ONE anti-hype guard and it is THIS-patent-specific ("nothing connects these
      circuits to Jalapeño... no source shows this macro running in silicon"), not a generic
      "patents don't guarantee production" truism; no false equivalence, no re-listed caveats, no
      safe-harbor boilerplate — CLEAN, no over-hedge and no overreach. 6H DEFENSIVE-OPEN: ¶1 opens on
      the discovery beat; the "pending application" insurance label sits in ¶2, AFTER the beat —
      clean. 6I ATTENTION-BUDGET: prosecution/status narration confined to the single pricing section
      §5 plus one lead clause plus the §6 recap; no spend-motif spread — clean.

  - pass: pass-7-adversarial-reader
    finding: "no findings"
    scoped_to: |
      Read as impatient investor + skeptical pro-subject reader; each check decomposed yes/no with
      evidence.
      (1) Hook: ¶1 lands the discovery register declaratively ("There is a published OpenAI patent
      that designs an AI chip down to the individual memory cell. The math runs inside the memory
      array itself...") and the two-sided call lands by lead end — PASS.
      (2) Header-as-claim: all six ## headers are assertions; header-only skim reconstructs the arc
      (on file before news -> multiply FP/add int/convert once -> headline described but circuits
      claimed -> result every cycle -> pending but tape-out depth -> literal engineering, two dates)
      — PASS.
      (3) Steelman present + not overweight: the single strongest THIS-patent counter is conceded
      compactly and specifically in §3 (headline features are description not claims; block-scaled/MX
      is prior standardized art — "A skeptic can fairly call the core a known technique, implemented"),
      then the affirmative core (¶3: claimed circuit specifics + primary-source depth) carries >= the
      concession's attention; net-new (pending-status caveat is spent in §5, NOT re-spent here); no
      spend/procedure lexicon inside the beat (SURF-007 clean) — PASS, neither steelman-absent nor
      steelman-overweight.
      (4) Meta posturing: no reader-instruction / essay-as-object. "none is guessed at here", "stays
      labeled as background", "The registry facts, stated once", "The bounds priced in the previous
      section" are functional scope/bridge phrasing (exempt) — PASS.
      (5) Jargon as signpost: mechanism terms glossed functionally, not deep-dived; the §3 three named
      blocks serve the claim-specificity argument (already noted for density in r1-F2) — PASS.
      (6) Stub/rhythm: no section markedly short; lead (158w) and closing (190w) appropriately tighter
      than the mechanism body — PASS.
      (7) Thesis not over-restated: the core verdict is asserted in §1 and §6 (2 sections) plus the
      exempt signature line "The design record says the work started earlier..." — <=3 — PASS.

  - pass: pass-3-fact-paraphrase
    finding: "verbatim + external facts verified (see r1-F4, r1-F6 for the two low precision notes)"
    scoped_to: |
      Verbatim byte-exact against input/patent.md: [0005] conversion-step quote (line 62), [0011]
      both claim spans — align-mantissa + adder-tree-integer (line 68), [0147] pipelined-VMM-every-
      cycle (line 210), [0154] "In some embodiments, 100% utilization of the compute engine 100 may
      be possible" and "256 VMM operations" (line 213), [0118] "serve both compute storage and
      scan-test roles" (line 180), [0199] Emax=22/INT5 (line 264). Paraphrase anchors verified against
      invention-summary Quotable spans / Quote anchor table: [0133] von-Neumann/CIM, [0130]
      FP8/FP6/FP4 activations vs FP6/FP4 weights, [0141] 32-value shared-scale MX block, [0006]
      no-separate-conversion-pipelines, [0104] consistent-scale, [0145] INT35+INT5->FP22, [0183]
      64x64 adders saved, [0002] VMM dominates, [0012]/[0015] dual-bank double-buffering, [0234]/
      [0262]/[0289] PVT/clock/scan depth — all faithful, no drift, no fact introduced beyond the
      Quotable spans. External facts trace to fact-check-log and appear in # Sources: 10GW/2025-10-13
      announcement, Jalapeño 2026-06-24 + end-2026 deployment, Allegrucci Apple/Rain June-2024
      (correctly labeled press-reported background with its bound stated: "no document here says where
      any of the five sat on the provisional date"), OCP MX 2023-09 seven signatories. Sixth-inventor
      trap avoided (essay says "Five inventors"). Claim-scope language uses "seek to protect"/"sought"
      throughout — pending never presented as granted.

  - pass: pass-4-logic-causality
    finding: "no findings beyond r1-F5 (low)"
    scoped_to: |
      4A thesis-section alignment: all four spine axes land (Axis1 claim-triad + Axis2 problem -> §2;
      Axis4 baseline + steelman -> §3; Axis3 effect -> §4; pricing -> §5), no out-of-spine claim
      introduced. 4B causality: the central inference is EVIDENTIARY ("the filing is primary evidence
      that 'OpenAI-designed' is literal engineering"), not causal — the essay does not claim the patent
      caused the announcement, so no correlation->causation drift. Confounders handled: the acquired-
      lineage confounder (Rain AI / Allegrucci) is named and bounded in §5; the production/roadmap
      confounder is scoped out in §6 ("no source shows this macro running in silicon", "nothing
      connects these circuits to Jalapeño"). 4C arc: lead tension (announcement vs priority) is set
      and resolved at close; implication is thesis-specific, not generic. The one low note (r1-F5) is
      a categorical premise in §5, not a spine or causation failure.

  - pass: pass-2-redundancy
    finding: "one finding (r1-F3, low); otherwise clean"
    scoped_to: |
      2A claim repetition: the core verdict appears in §1 + §6 (acceptable lead/closing bookend); the
      "down to the individual memory cell" motif is r1-F3. Declared signature lines (2) exempt and not
      counted. 2B sentence tightening: no "in order to"/"there exists"/stacked-hedge filler; the long
      sentences are dense but information-bearing (the §3 machinery sentence is addressed under r1-F2).
      2C paragraph earn: only §3 ¶3 exceeds 150 words (r1-F2); no essay paragraph reaches the 8-sentence
      high-severity line (max is §3 ¶3 at 7).
```
