# Thesis Trace

## Spine source

- **Spine**: handoff/01-design/thesis-spine.md
- **One-line spine**: OpenAI's first-published chip patent claims a compute-in-memory engine that does the expensive half of floating-point matrix math on plain integer adders, and its transistor-level depth, dated a year before the Broadcom announcement, is primary evidence that "OpenAI-designed" silicon is literal engineering.
- **Q7 hook**: corporate-narrative-friction
- **Title-lead register**: discovery (handoff/01-design/title-lead-candidates.md, recommended pick)
- **Figures**: figure-enabled (draft_version 3). Header = FIG. 4 (image-plus-caption). Body =
  FIG. 1 + FIG. 3 in §2, FIG. 43 in §4 (caption-only-italic). No prose cross-references: the two
  earlier value-add pointers (FIG. 38, FIG. 45) were removed in round-2 (r2-F2) once the
  upstream figure-selection.md tokenization was corrected — they pointed to figures the article
  does not display. Only FIG. 1 / 3 / 4 / 43 tokens remain. Placements + captions in
  `figures-rationale.md`.

## Section → spine mapping

### 0-header — FIG. 4 (cover)
- **Spine element carried**: Axis 1 made visual — the claimed align-once, integer-accumulate
  core (per-row Shift Calculation EMax − E, 2's-complement, Adder Tree 426 → INT35). Sits above
  §1; the title rides over it.
- **Rendering**: image-plus-caption, `header_composite` caption (trimmed in round-2 r2-F1 from
  ~86 words to 52 words for cover-surface invitation: dropped the "(426)" reference number and
  the shift-arithmetic narration; kept the align-once/adder-tree core, Emax≤22→INT5, integer
  accumulation, INT35 out, and the claim-1 tie)
- **paragraph_anchors_used (caption)**: `[0199]`, `[0011]`, `[0145]`

### 1-lead — "The Design Was on File Before It Was News"
- **Spine element carried**: Hook (corporate-narrative-friction: announcement vs priority date); tech beat first (math inside the memory array, FP products on integer adders); two-sided call by end of lead, pending-application label as one clause after the beat
- **voice_canon_reference**: `opening-corporate-event-announcement-friction`
- **paragraph_anchors_used**: `[0133]`, `[0011]`
- **external_facts_used**: `openai-broadcom-10gw-2025-10-13`
- **word_target / word_actual**: 150 / 156
- **round-1 edits**: r1-F6 (¶1 "about eleven months"); r1-F3 (¶2 "written to the bitcell",
  de-duplicating the depth motif in adjacent lead paragraphs)

### 2-mechanism — "Multiply in Floating Point, Add as Integers, Convert Once"
- **Spine element carried**: Axis 1 (claim-1 triad) + Axis 2 (problem anchor); secondary technical-impossibility beat
- **round-4 edits**: r4-F1 (claim-scope completeness — the "What independent claims ... seek to
  protect" sentence now enumerates all THREE independent claims: 1, 20, and 29, matching the
  corrected invention-summary Claim scope map; thesis-strengthening, no hedge)
- **voice_canon_reference**: `mechanism-walkthrough`, `inline-bold-thesis-anchor`
- **paragraph_anchors_used**: `[0133]`, `[0142]`, `[0130]`, `[0145]`, `[0131]`, `[0005]`, `[0011]`, `[0104]`, `[0199]`, `[0200]`, `[0139]`, `[0006]`, `[0141]`
- **external_facts_used**: []
- **figures_placed**: FIG. 1 (after ¶1, medium caption), FIG. 3 (after the [0011] blockquote,
  short caption)
- **word_target / word_actual**: 380 / ~437 (incl. FIG. 1 + FIG. 3 captions; prose ~402)
- **round-1 edits**: r1-F1 (split the alignment paragraph at "...before the sum [0104]." into
  ¶4 + ¶5)
- **round-2 edits**: r2-F2 (removed the ¶4 FIG. 4-as-functional-block / FIG. 38-as-circuitry
  cross-reference; the bit-shift sentence now ends at "Here the lining up is a bit shift." —
  FIG. 4 remains tokenized in the header)

### 3-scope-and-baseline — "The Headline Features Are Described. The Circuits Are Claimed"
- **Spine element carried**: Axis 4 (baseline-difference) + steelman beat (claimed vs described in sought-* vocabulary; MX format vs claimed circuits; return to affirmative core)
- **voice_canon_reference**: `baseline-comparison`, `strategic-reframe`
- **paragraph_anchors_used**: `[0130]`, `[0006]`, `[0141]`, `[0011]`, `[0200]`, `[0202]`, `[0206]`, `[0183]`
- **external_facts_used**: `ocp-mx-spec-2023-09`
- **word_target / word_actual**: 300 / ~320
- **round-1 edits**: r1-F2 (split the densest paragraph into ¶3 + ¶4; broke the ~48-word
  machinery sentence into two); r1-F4 (claim-scope precision — the shift-calc + select-decoding
  unit is stated as folded into independent claim 20, not dependent-only)
- **round-4 edits**: r4-F1 (claim-scope completeness — THREE independent claims, not two). ¶2
  concession now reads "independent claims 1, 20, and 29 seek the multiply-align-add triad". ¶3
  "named machinery" paragraph reworked: the machinery is pulled up into the independent claims
  themselves — claim 20 folds in the shift calculation and select decoding unit [0200], claim 29
  folds in a shift register — with dependent claims adding the specifics (register sizing [0202],
  log-mux tree [0206]); the false "one piece claim 20 pulls up" framing removed (claim 29 folds
  in the shift register independently); the "64 by 64 half adders" [0183] sentence kept. This
  STRENGTHENS Axis 4's affirmative return (a third independent shot at the core); no hedge added

### 4-throughput — "The Design Target Is a Result Every Cycle"
- **Spine element carried**: Axis 3 (effect anchor): pipelined product-per-cycle, double-buffered weights (narrated as unclaimed here), utilization hedge kept
- **voice_canon_reference**: `mechanism-walkthrough`
- **paragraph_anchors_used**: `[0147]`, `[0002]`, `[0154]`, `[0012]`, `[0015]`
- **external_facts_used**: []
- **figures_placed**: FIG. 43 (after the double-buffering paragraph, medium caption)
- **word_target / word_actual**: 210 / ~233 (incl. FIG. 43 caption)

### 5-what-the-filing-is — "A Pending Application, Written at Tape-Out Depth"
- **Spine element carried**: pricing (registry facts once): pending application, priority 2024-11-22 vs announcement 2025-10-13, inventor roster + Allegrucci Apple/Rain press-reported background, canceled claims 11-19 as document fact, tape-out-depth evidence
- **voice_canon_reference**: `evidence-level-labeling`
- **paragraph_anchors_used**: `[0234]`, `[0262]`, `[0289]`, `[0118]`
- **external_facts_used**: `allegrucci-apple-rain-2024-06`
- **figures_placed**: none (the §5 depth point is carried in prose)
- **word_target / word_actual**: 250 / ~245
- **round-1 edits**: r1-F5 (narrowed "do not carry" → "rarely carry" clock margins and scan
  modes; verdict landing untouched)
- **round-2 edits**: r2-F2 (removed the trailing "FIG. 45 draws one such scan-wired double
  bitcell" clause; the [0118] scan-test quote is kept and the sentence now closes at the quote)

### 6-closing — "Literal Engineering, With Two Dates to Watch"
- **Spine element carried**: verdict recap + forward-watching events (Jalapeño end-2026 deployment; family examination fate); closing_posture firm
- **voice_canon_reference**: `closing-forward-watching-event`
- **paragraph_anchors_used**: []
- **external_facts_used**: `openai-broadcom-jalapeno-2026-06-24`, `openai-broadcom-10gw-2025-10-13`
- **word_target / word_actual**: 180 / 191
- **round-2 edits**: r2-F3 ("priority date eleven months older" → "priority date about eleven
  months older", uniform with §1 ¶1; date-arithmetic precision, verdict untouched)
- **round-4 edits**: r4-F1 (claim-scope completeness — the patent-office watch-list now reads
  "what examination leaves of claims 1, 20, and 29 will fix how much ... OpenAI ends up owning",
  reflecting all three independent claims; verdict lead and signature line 2 untouched, no hedge)

## Signature lines

<!-- 0-3 EXACT strings ("none" if zero). Protected surface per
     _shared/references/reader-energy.md: pass-2 / pass-7 echo and count rules exempt
     them; pass-3/4 factual review still applies in full. -->
1. "Align once, and the whole accumulation becomes integer arithmetic."
2. "The design record says the work started earlier, and the record is the harder document to argue with."

## Coverage check

- All 4 axes carried: Axis 1 → §2, Axis 2 (problem) → §2, Axis 3 → §4, Axis 4 (baseline) → §3.
- Steelman beat lands in §3 (concede-and-return; concession = headline features outside claim set + MX-is-prior-format; return = claimed circuit specifics + primary-source depth). Pending-status caveat spent in §5, not re-spent in the steelman.
- Attention budget: exactly ONE pricing section (§5); status-label motif elsewhere limited to one lead clause + the closing recap.
- No out-of-spine claims introduced.
- Every `[dddd]` used traces to an invention-summary Quotable span / Quote anchor.
- Every external fact used traces to a fact-check-log Fact ID and appears in # Sources.
- Figures (draft_version 3): all four selected figures (4, 1, 3, 43) referenced; figure
  captions carry only anchor-traceable claims; the only "FIG. N" tokens in the draft are 1, 3,
  4, 43 (the FIG. 38 and FIG. 45 prose cross-references were removed in round-2 r2-F2). Every
  token is in the available index. `gate_figure_use` and `gate_anchors` FIGREF both PASS.
