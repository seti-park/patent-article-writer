review_id: intel-us20260191095-backend-hbm-editorial-review-1
draft_source: handoff/02-compose/essay-draft.md
review_timestamp: 2026-07-06T00:00:00Z
round: 1
posture_applied: conservative        # draft frontmatter + thesis-trace declare posture_used: conservative; measured gives identical severities on every finding below
closing_posture: measured            # verdict confidence (owner-set, option A) — orthogonal to the editorial severity lens
register: discovery
overall_assessment: revise-recommended

# ---------------------------------------------------------------------------
# Reviewer's note (fresh instance, no memory of composing)
# ---------------------------------------------------------------------------
# This is a genuinely strong first draft: the verbatim-quote chain is clean, the
# owner-set accuracy guards hold, the strategic payload stays labeled as inference,
# the four selected figures are all used with accurate captions, and the verdict is
# measured-not-hedged (commits to a direction + carries ONE patent-specific anti-hype
# guard). It is NOT a clean round, though — two medium precision findings hold, both on
# load-bearing claims (the verdict's proof-point label, and the central inference
# sentence). Per the loop's double-clean rule this routes to the composer and a fresh
# round-2 reviewer confirms; it is not an acceptance.
#
# Explicit all-clear answers the orchestrator asked for:
#   - grounding hard-gate (pass-3 high/critical): NONE.
#   - goal-2 figure coverage: NONE (all 4 selected figures used, captions accurate).
#   - verdict / 6G over-hedge: NONE (6G clean — see pass-6 entry). No 6H, no 6I breach.

# ---------------------------------------------------------------------------
# Guard audit (owner-set accuracy guards from input/essay-context.md) — each VERIFIED HELD
# ---------------------------------------------------------------------------
guard_audit:
  - guard: "Strategic payload (foundry / who-can-make-HBM) is EXTERNAL INFERENCE, must stay labeled, never attributed to patent text"
    status: HELD
    evidence: "§4 ¶1 'Here the filing's own words stop, and the reading begins. Claim 1 says backend. It never says foundry, never says logic fab, never says without a DRAM fab ... the leap is mine, not the document's.' Inference never credited to the patent. (Functional scope labeling, gate_meta PASS — required, not banned meta.)"
  - guard: "patent must NOT be asserted = ZAM (same direction, different interconnect)"
    status: HELD
    evidence: "§4 'ZAM stacks on a diagonal Z-angle joined by hybrid bonding ... This filing uses vertical TSV gutters and UCIe instead. Same goal, different document, and no ground for calling them one chip.'"
  - guard: "1T1C must NOT be called capacitor-less (capacitor relocated, not removed)"
    status: HELD
    evidence: "§2 bold anchor 'This is still a one-capacitor cell. The back-end move relocates DRAM's hardest part. It does not remove it.'; §5 'keeps the capacitor and merely moves it'; §6 'the capacitor was relocated ... rather than removed.'"
  - guard: "channel material (IGZO/oxide) must NOT be attributed to the patent"
    status: HELD
    evidence: "§5 'It never names the channel material.' No IGZO/oxide imported as Intel's. imec's 2T0C is the only external contrast and is not conflated with the patent."
  - guard: "'beats HBM4' numbers must NOT be attributed to this filing (patent has only the match-footprint GOAL)"
    status: HELD
    evidence: "§3 'in the document's words, \"With the goal of matching HBM4's footprint\" ... a goal on the page, not a result on a bench: the filing reports no bandwidth, no cost, no yield.' 'beating HBM' attributed to ZAM (external), not the patent."
  - guard: "productization must NOT be asserted (pending application)"
    status: HELD
    evidence: "§1 'This is one published application, not a product.'; §5 'a single published application, not a granted patent and not a product.'"

findings:

  # ========================= MEDIUM =========================

  - finding_id: r1-F1
    pass: pass-3-fact-paraphrase
    location: §6 (verdict), 3rd paragraph ("The test is a number ...")
    severity: medium
    severity_under_default_posture: medium
    finding: |
      The measured verdict routes its proof point to VLSI 2026 and calls what will be
      tested there "a back-end HBM stack": "The related work is due to surface at VLSI
      2026 in June. There, the density, yield and cost per bit of a back-end HBM stack
      will either hold up or they will not."

      The VLSI 2026 work is the ZAM / HB3DM paper (fact-check-log zam-hb3dm-vlsi2026).
      But the fact-check-log NOWHERE characterizes ZAM as a back-end / BEOL / thin-film-
      transistor design — zam-hb3dm-specs describes it as a 9-layer HYBRID-BONDED stack
      and says nothing about the cell being backend. The only BEOL/thin-film entry in the
      log is imec's 2T0C path, which §5 correctly separates from this patent AND from ZAM.
      So the phrase "a back-end HBM stack" imports a backend-transistor property onto the
      VLSI/ZAM proof point that the sources do not support — and it is the load-bearing
      proof point the measured close rests on. The draft otherwise keeps the ZAM link at
      arm's length ("related work", "same technology family"), so this is a scope/label
      over-tightening in one clause, not a guard breach — but it slightly softens the
      grounding of the verdict's central test, and a skeptical reader who knows VLSI 2026 =
      hybrid-bonded ZAM would catch the seam against §4's "no ground for calling them one
      chip" discipline. (Inherited from the design: thesis-trace.md "Closing directive
      realization" forward_pointer uses the same "back-end HBM stack" phrasing.)
    recommendation: |
      Narrow / re-label the proof point to what the sources support — do NOT hedge the
      verdict. This patent has no announced benchmark; the nearest PUBLIC readout on
      whether tall 3D-stacked DRAM competes with HBM4 on density/yield/cost is the RELATED
      ZAM/HB3DM family's VLSI 2026 paper. Change "a back-end HBM stack" to something that
      does not assert ZAM is backend-transistor, e.g. "this class of tall, stacked
      HBM challenger" or "the nearest public 3D-DRAM readout." Keep the commitment and the
      named test-bed intact (measured close preserved); only the backend-transistor
      attribution to the ZAM proxy comes out. (Fix direction: narrow → label. Never hedge.)
    quote: "There, the density, yield and cost per bit of a back-end HBM stack will either hold up or they will not."
    related_fact_entry: zam-hb3dm-vlsi2026

  - finding_id: r1-F2
    pass: pass-4-logic-causality
    location: §4 ("A Back-End Cell Could Loosen the DRAM-Fab Bottleneck"), 3rd paragraph
    severity: medium
    severity_under_default_posture: medium
    finding: |
      The essay's single load-bearing inference sentence reads: "Because it is deposited at
      low temperature in the wiring, it does not need the crystalline-silicon front-end that
      only a dedicated DRAM fab runs."

      §2 defined "front-end" GENERICALLY as "the crystalline silicon at the base of the die"
      — which is true of logic dies too (logic transistors are crystalline-silicon front-end
      devices). Carrying that definition forward, "the crystalline-silicon front-end that
      only a dedicated DRAM fab runs" is imprecise: logic foundries also run crystalline-
      silicon front-ends. The precise claim (and the one the spine Axis 4 and essay-context
      state — "the crystalline-silicon DRAM FEOL") is the DRAM-SPECIFIC front-end. As written,
      the sentence invites exactly the strongest skeptical-pro objection the §5 steelman is
      meant to pre-empt ("but a back-end access transistor doesn't make the whole thing a
      pure logic-line output; there is still front-end silicon in the base/logic die"). The
      thesis survives — this is a one-word precision gap on the pivotal sentence, not a
      thesis break.
    recommendation: |
      Restore the DRAM-specificity so the claim narrows to what is true: "... it does not
      need the crystalline-silicon DRAM front-end that only a dedicated DRAM fab runs" (or
      "the DRAM front-end"). This tightens the load-bearing inference to the DRAM-FEOL
      constraint the spine actually claims and closes the skeptic's opening. (Fix direction:
      narrow the claim to what the anchor/spine supports. Never hedge.)
    quote: "it does not need the crystalline-silicon front-end that only a dedicated DRAM fab runs"

  # ========================= LOW =========================

  - finding_id: r1-F3
    pass: pass-3-fact-paraphrase
    location: §3 ("A Tower Built to Match HBM4's Footprint"), 1st paragraph
    severity: low
    severity_under_default_posture: low
    finding: |
      "with the silicon thinned so many layers fit inside a standard height [0031]". The
      [0031] anchor supports only "thinning of the silicon can be implemented to enable
      many-layer stacking" (Quote anchor q-0031-2). "fit inside a standard height" is an
      interpretive addition — [0031] says nothing about a height budget. The height concern
      lives elsewhere (MoP Z-height, [0044]-[0045]) and the fit-to-target is [0034]'s
      "match HBM4's footprint" goal. Reasonable engineering gloss, but the specific clause
      is not carried by the cited anchor.
    recommendation: |
      Match the anchor: drop "inside a standard height" (→ "with the silicon thinned so
      many layers fit" or "... to enable many-layer stacking"), or attach the height/footprint
      idea to its real support ([0034]) rather than [0031].
    quote: "with the silicon thinned so many layers fit inside a standard height [0031]"

  - finding_id: r1-F4
    pass: pass-3-fact-paraphrase
    location: Title
    severity: low
    severity_under_default_posture: low
    finding: |
      Title: "Intel's Patent Moves the DRAM Cell Into the Back-End". This is a PUBLISHED
      APPLICATION, not a granted patent — a distinction this edition is otherwise scrupulous
      about (body: "one published application, not a product"; "a single published
      application, not a granted patent"). "Patent" is common headline shorthand and the body
      corrects it within ¶2, so this is a minor surface-accuracy note, not a defect — flagged
      only because the pending-vs-granted line is load-bearing for this edition. Title style
      is protected surface (energy contract); accuracy is the only lever here.
    recommendation: |
      Optional, composer/owner's call: "Intel's Filing Moves the DRAM Cell Into the Back-End"
      is one character longer, equally strong as a hook, and matches the body's precision.
      If retained for feed force, the immediate ¶2 correction is an acceptable mitigation.
    quote: "Intel's Patent Moves the DRAM Cell Into the Back-End"

  - finding_id: r1-F5
    pass: pass-2-redundancy
    location: §4 ¶3, §5 ¶3, §6 ¶1 (affirmative-core restatements)
    severity: low
    severity_under_default_posture: low
    finding: |
      The affirmative core is restated in a near-identical "a logic-and-packaging X can carry /
      a [DRAM] Y cannot" antithesis three times:
        §4: "Backend is the property a logic-and-packaging flow can carry, where a front-end DRAM cell cannot."
        §5: "That is the single property a logic-and-packaging line can carry and a front-end fab cannot ..."
        §6: "That is the property that could let a logic-and-packaging maker carry HBM-class memory without owning a DRAM front-end."
      This is within pass-7's ≤3-section thesis-restatement bound (the two DECLARED signature
      lines — §1¶3 and §6's closing landing — are exempt and are NOT these three), and each
      occurrence is structurally motivated (inference intro → steelman return → verdict). So it
      is not a count violation; it is a felt stylistic refrain — the identical "can carry /
      cannot" cadence three times reads as a chant on a mobile scroll.
    recommendation: |
      Vary the phrasing of ONE of the three non-signature restatements (§4, §5, or §6 ¶1 — NOT
      the declared signature lines) so the affirmative core lands three times without the
      identical antithesis structure. Content unchanged; cadence de-duplicated.

  - finding_id: r1-F6
    pass: pass-3-fact-paraphrase
    location: §4, FIG. 1A caption
    severity: low
    severity_under_default_posture: low
    finding: |
      "A logic die (106) sits beside the high-bandwidth-memory stack (104) on a single
      interposer, the picture of one flow carrying both." The literal description is accurate
      (FIG. 1A is the co-package cross-section, [0022]). The gloss "the picture of one flow
      carrying both" imports §4's manufacturing-FLOW inference onto a figure that literally
      shows co-PACKAGING (physical co-location on one interposer), not one manufacturing flow.
      In the labeled-inference section this has some latitude, but a caption should describe
      what the figure shows and leave the leap to the body.
    recommendation: |
      Describe the figure, keep the leap in the prose: e.g. "... logic and memory sharing one
      package" or "... on one interposer — logic and memory side by side." The "one flow"
      reading is already carried (and labeled as inference) by §4's body.
    quote: "the picture of one flow carrying both"

  - finding_id: r1-F7
    pass: pass-3-fact-paraphrase
    location: §5 ("Read Cold ..."), 2nd paragraph
    severity: low
    severity_under_default_posture: low
    finding: |
      "SK hynix, Samsung and Micron each run their own 3D-DRAM programs pointed at roughly
      2030." fact-check-log incumbent-3d-dram supports that all three have 3D-DRAM PROGRAMS
      (load-bearing, fine), but pins only SK hynix to ~2030 (2029-2031). Samsung is logged as
      a disclosed VCT roadmap (no date), Micron as research since 2019 (no 2030 target). So
      "each ... pointed at roughly 2030" over-generalizes the timing to all three. The
      load-bearing point ("three funded roadmaps") is unaffected; the ~2030 is color.
    recommendation: |
      Attribute the date to what is sourced: "... each run their own 3D-DRAM programs, with
      SK hynix's targeted around 2030" or "pointed at roughly the end of the decade." Keeps
      the "three funded roadmaps" stake, drops the unsourced blanket date.
    quote: "each run their own 3D-DRAM programs pointed at roughly 2030"

  # ========================= NO-FINDINGS PASSES (scoped_to = what was checked) =========================

  - pass: pass-1-voice-anti-ai
    finding: "no findings"
    scoped_to: |
      All 6 sections + 4 captions + title checked against deliverable-voice-rules.md and
      anti-ai-writing.md. Banned-word grep: 0 hits (gate_banned PASS, re-confirmed). Em-dash:
      0 (gate_emdash PASS, re-confirmed by grep). No copula avoidance (is/are used directly:
      "That is the strategic weight", "The test is a number"). No not-just-X-but-Y, no
      despite-challenges, no sentence-initial Furthermore/Moreover/Additionally, no puffery
      (unprecedented/remarkable). No elegant variation (Intel stays "Intel"; "filing/
      application/document" are plain descriptors, not cute renamings). Bold: exactly ONE
      load-bearing anchor (§2), = the STRUCT-002 single-anchor slot. Colons follow complete
      clauses; no mid-sentence "The problem:" tell; no semicolon-joined independent clauses.

  - pass: pass-5-reader-perspective
    finding: "no findings"
    scoped_to: |
      Engagement curve, stake clarity, jargon budget, mobile line count checked against
      reader-profile.md (curious retail investor, adv-HS-to-early-undergrad). Every term of
      art carries a one-clause gloss on FIRST use: back-end ("low-temperature metal stacked
      on top"), front-end ("crystalline silicon at the base ... engineers call the
      front-end"), thin-film transistor ("a thin coating in the wiring rather than carved
      into the silicon"), 1T1C ("one transistor to select a bit, one capacitor to hold it"),
      HBM4 ("newest generation of the high-bandwidth memory that feeds AI accelerators"), TSV
      gutters ("columns of through-silicon vias ... punched straight through a die"), UCIe
      ("industry standard for wiring one chiplet to another"), base die ("small controller
      chip that routes signals in and out"), hybrid bonding ("fuses two dies face to face
      without solder"), capacitor ("tiny well of charge that stores each bit"). No FEOL/BEOL
      acronyms exposed. No density wall (every tech section resolves to a stake — §3 ends on
      "no bandwidth, no cost, no yield"). Money thread structural: every section feeds the
      verdict. Closing reads standalone. No prerequisite-chain overload (≤1 new dependent
      concept per paragraph). gate_structure PASS (no ≥8-sentence paragraph).

  - pass: pass-6-lead-conclusion-format
    finding: "no findings"
    scoped_to: |
      6A lead anchor — ¶1 sets the discovery beat and the patent is on the table by sentence 2;
      full two-sided call lands by §1¶3 (signature line 1). 6B frame closure — §6 returns to the
      lead's Intel-left-memory / who-can-make-HBM frame and lands signature line 2; residual-risk
      = Acceptance(falsifiable) → maps to closing-forward-watching-event/binary-test (VLSI 2026),
      which §6 delivers. 6C Sources — 3 categories (Patents/Papers/News & media), all in the
      5-enum, subgrouped all-or-nothing (gate_sources PASS). 6D author format — Papers entry is
      institutional (imec), no "First, et al." violation. 6E mechanical — em-dash 0, [dddd] all
      4-digit, one "# Sources" h1 (gates PASS). 6F title — no em-dash (colon-free). 6G OVER-HEDGE
      — CLEAN: verdict leads with the call ("The direction is not in doubt"), not a qualifier;
      keeps exactly ONE patent-specific anti-hype guard (1T1C capacitor relocated-not-removed +
      "a back-end capacitor at HBM density and yield is precisely what no one has shipped"); no
      safe-harbor boilerplate; limits referenced ("The bounds set out above still hold"), not
      re-listed; gate_hedge PASS. 6H DEFENSIVE-OPEN — CLEAN: ¶1 opens on the discovery beat;
      insurance (Intel exited memory, one application) sits in ¶2 AFTER the beat. 6I ATTENTION
      BUDGET — CLEAN: prosecution/status material confined to §5 (the one pricing section) + one
      lead clause + closing recap; no process narration (fees/RCE/liens) anywhere; status LABELS
      only.

  - pass: pass-7-adversarial-reader
    finding: "no findings"
    scoped_to: |
      Read as impatient investor + skeptical pro-subject reader; 7 checks, each yes/no with a span.
      (1) HOOK: PASS — ¶1 "Intel's newest memory filing does something quietly radical. It builds
      the transistor inside each DRAM cell in the chip's back-end wiring layers" is declarative
      discovery, no verdict-insurance ahead; two-sided call by lead's end. (2) HEADER-AS-CLAIM:
      PASS — all 6 headers are assertions; header-only skim reconstructs the argument (memory from
      the company that left it → claim 1 = one word, backend → tower matches HBM4 → back-end cell
      could loosen the bottleneck → read cold, it keeps the capacitor → direction real, numbers are
      the test). (3) STEELMAN present + not overweight: PASS — §5 concedes SPECIFICALLY and
      THIS-patent (single application/no yield; keeps the capacitor vs imec 2T0C; incumbents already
      on 3D DRAM; Powerchip-not-Intel fabs), then returns to the affirmative core with >= attention;
      net-new (does not re-spend the lead's Intel-exited clause verbatim); no spend/procedure motif
      inside the beat; generic "patents don't guarantee products" truism is NOT used as the steelman.
      (4) META: PASS — gate_meta PASS; §4 "the leap is mine, not the document's" is REQUIRED
      functional scope labeling (the anti-hedge-ratchet fence demands it), not banned reader-
      instruction. (5) JARGON: PASS — terms glossed as signposts, none deep-dived past the insight.
      (6) STUB: PASS — no section markedly shorter than siblings (gate_stub PASS). (7) THESIS
      OVER-RESTATE: PASS at the boundary — affirmative core asserted in 3 sections (§4/§5/§6); the 2
      declared signature lines are exempt; the identical-cadence refrain is logged as low r1-F5, not
      a count breach.

# ---------------------------------------------------------------------------
# Severity roll-up: critical 0 | high 0 | medium 2 | low 5
# Assessment rule (feedback-format.md): no critical, no high, >=1 medium -> revise-recommended.
# ---------------------------------------------------------------------------
