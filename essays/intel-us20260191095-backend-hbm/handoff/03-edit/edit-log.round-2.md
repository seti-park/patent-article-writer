review_id: intel-us20260191095-backend-hbm-editorial-review-2
draft_source: handoff/02-compose/essay-draft.md
review_timestamp: 2026-07-06T00:00:00Z
round: 2
posture_applied: conservative        # draft frontmatter declares posture_used: conservative (matches round 1); measured gives identical severity on the single low finding below
closing_posture: measured            # verdict confidence (owner-set, option A) — orthogonal to the editorial severity lens
register: discovery
overall_assessment: pass             # clean at medium+ (critical 0 / high 0 / medium 0); ONE new low. Per double-clean, this is the FIRST clean round -> triggers a CONFIRMATION round (round 3), NOT acceptance.

# ---------------------------------------------------------------------------
# Reviewer's note (FRESH round-2 instance — no memory of composing or of prior rounds)
# ---------------------------------------------------------------------------
# Re-review protocol run in order: (1) ruled on all 7 carried finding_ids from round 1
# BEFORE hunting new findings; (2) re-audited the owner-set accuracy guards (police list);
# (3) ran the full 7 passes on the round-2 draft for NEW findings.
#
# Round-1 was revise-recommended (medium 2, low 5); the composer APPLIED all 7 (no
# rejections), all as anchor/narrow/label edits with no hedge added and both signature lines +
# the single §2 bold anchor untouched. I verified each disposition ACTUALLY LANDED by quoting
# the fixed span from the round-2 draft (below), and confirmed no neighbour regressed: every
# edit was an in-sentence word swap (no split/merge), so paragraph bands are unchanged — the
# draft still has 6 body sections (§1-§6) mapping 1:1 to the spine trace, and gate_structure
# stays PASS.
#
# This is a genuinely clean round at medium+. The orchestrator's caution about round-N
# rubber-stamping was taken seriously: I re-read the whole draft against pass-5 (reader) and
# pass-7 (adversarial) after finding nothing at medium+, and re-verified the pass-3 verbatim
# chain byte-by-byte against patent.md. The two round-1 mediums were the only real substance in
# round 1 and both are correctly closed. One NEW low precision note (r2-F1) is a downstream
# refrain that the round-1 §4 fix (r1-F2) did not reach; it does not touch the assessment.
#
# Explicit all-clear answers the orchestrator asked for:
#   - grounding hard-gate (pass-3 high/critical): NONE.
#   - goal-2 figure coverage: NONE (all 4 selected figures — 1B cover, 1F §2, 1G §3, 1A §4 —
#     used with accurate captions; FIGUSE-001 figs 2-7 is the documented Phase-1 tokenization
#     artifact, gate PASS per orchestrator).
#   - verdict / 6G over-hedge: NONE (6G clean in BOTH directions — measured-not-hedged; no 6H,
#     no 6I breach).

# ===========================================================================
# PART A — Re-review rulings on carried round-1 finding_ids (each VERIFIED against round-2 draft)
# ===========================================================================

carried_findings:

  - finding_id: r1-F1
    original_severity: medium
    disposition_claimed: applied (narrow -> label; verdict NOT hedged)
    ruling: VERIFIED LANDED
    location: §6 (verdict), 3rd paragraph
    evidence: |
      Round-2 draft §6 ¶3 now reads: "There, the density, yield and cost per bit of this class
      of tall, stacked HBM challenger will either hold up or they will not." The old phrase
      "a back-end HBM stack" is GONE. This is the orchestrator's explicit r1-F1 check: the
      VLSI-2026 / ZAM proxy is no longer characterized as backend/BEOL. Confirmed against
      fact-check-log `zam-hb3dm-specs` — ZAM is a 9-layer HYBRID-BONDED stack, not a
      backend-transistor design, so the false backend attribution to the proxy is correctly
      removed. The direction-commitment ("will either hold up or they will not"), the named
      test-bed (VLSI 2026, June), and the ~2029 horizon are all preserved — measured close
      intact, not hedged. Cross-checked: thesis-trace.md forward_pointer was updated in tandem
      (composer note), so a re-compose cannot reintroduce it. No neighbour regression.

  - finding_id: r1-F2
    original_severity: medium
    disposition_claimed: applied (narrow to the anchor/spine Axis 4 = DRAM FEOL)
    ruling: VERIFIED LANDED
    location: §4 ("A Back-End Cell Could Loosen the DRAM-Fab Bottleneck"), 3rd paragraph
    evidence: |
      Round-2 draft §4 ¶3 now reads: "Because it is deposited at low temperature in the wiring,
      it does not need the crystalline-silicon DRAM front-end that only a dedicated DRAM fab
      runs." The word "DRAM" was inserted before "front-end". This is the orchestrator's explicit
      r1-F2 check — confirmed present. The pivotal inference sentence now narrows to the
      DRAM-specific FEOL (matching spine Axis 4 + essay-context), closing the skeptical-pro
      opening the §5 steelman pre-empts (logic foundries also run crystalline-silicon
      front-ends). §2's generic definition of "front-end" is unchanged and does not conflict —
      §2 defines the concept, §4 applies the DRAM-specific constraint. No neighbour regression.

  - finding_id: r1-F3
    original_severity: low
    disposition_claimed: applied (re-anchor to what [0031] carries)
    ruling: VERIFIED LANDED
    location: §3 ("A Tower Built to Match HBM4's Footprint"), 1st paragraph
    evidence: |
      Round-2 draft §3 ¶1: "It describes a memory cube stacked eight high and beyond [0023],
      with the silicon thinned to enable that many-layer stacking [0031]." The over-reaching
      "fit inside a standard height" is gone; [0031] now carries only what q-0031-2 supports
      ("thinning of the silicon can be implemented to enable many-layer stacking"). Verbatim-
      checked against patent.md [0031]. Correct.

  - finding_id: r1-F4
    original_severity: low
    disposition_claimed: applied (factual carve-out; title is scope-accurate, not a style edit)
    ruling: VERIFIED LANDED
    location: Title (line 11)
    evidence: |
      Round-2 title: "# Intel's Filing Moves the DRAM Cell Into the Back-End". "Patent" ->
      "Filing" landed; the highest-read line now matches the body's pending-vs-granted precision
      ("one published application, not a product") and signature line 1's "Intel's filing".
      52 chars, well under SURF-001's 70. Energy/hook force preserved. I accept the composer's
      judgment-call reasoning; nothing to re-assert.

  - finding_id: r1-F5
    original_severity: low
    disposition_claimed: applied (varied the §4 occurrence; §5/§6 kept)
    ruling: VERIFIED LANDED
    location: §4 ¶3 (inference-intro restatement — NOT a declared signature line)
    evidence: |
      Round-2 draft §4 ¶3: "That is the strategic weight of the claim word. Backend belongs to
      the logic-and-packaging world, not the DRAM front-end." The identical "a logic-and-
      packaging X can carry / a [DRAM] Y cannot" antithesis is de-duplicated at §4; the refrain
      now recurs in 2 places (§5, §6), not 3, and both signature lines are untouched. Content
      unchanged. See r2-F1 for a residual precision note this fix surfaced in the §5 copy.

  - finding_id: r1-F6
    original_severity: low
    disposition_claimed: applied (caption made literal; flow-inference stays in labeled prose)
    ruling: VERIFIED LANDED
    location: §4, FIG. 1A caption (line 58)
    evidence: |
      Round-2 caption: "FIG. 1A: logic and memory on one package. A logic die (106) sits beside
      the high-bandwidth-memory stack (104), the two joined on a single interposer." The
      manufacturing-"one flow" gloss is gone from the caption; the caption now describes what
      FIG. 1A literally shows (co-packaging on one interposer, [0022]), and the labeled "one
      flow" leap stays in §4 body. Correct.

  - finding_id: r1-F7
    original_severity: low
    disposition_claimed: applied (scope the ~2030 date to SK hynix only)
    ruling: VERIFIED LANDED
    location: §5 ("Read Cold ..."), 2nd paragraph (line 66)
    evidence: |
      Round-2 draft §5 ¶2: "SK hynix, Samsung and Micron each run their own 3D-DRAM programs,
      SK hynix's aimed at around 2030." The blanket "pointed at roughly 2030" is gone; the date
      is now scoped to SK hynix only, matching fact-check-log `incumbent-3d-dram` (SK hynix
      2029-2031; Samsung VCT roadmap no date; Micron research since 2019). The "three funded
      roadmaps" stake in the next sentence is intact. Correct.

carried_findings_rollup: "7 of 7 round-1 finding_ids ruled on; 7 VERIFIED LANDED; 0 re-asserted; 0 dropped. No neighbour regression (all edits in-sentence swaps; 6-section structure, both signature lines, single §2 bold anchor unchanged)."

# ===========================================================================
# PART B — Owner-set accuracy guard re-audit (input/essay-context.md police list) — each VERIFIED HELD
# ===========================================================================

guard_audit:
  - guard: "patent must NOT be asserted = ZAM (same direction, different interconnect)"
    status: HELD
    evidence: "§4 'ZAM stacks on a diagonal Z-angle joined by hybrid bonding ... This filing uses vertical TSV gutters and UCIe instead. Same goal, different document, and no ground for calling them one chip.' The r1-F1 fix strengthened this: the verdict proxy is now 'this class of tall, stacked HBM challenger', not 'a back-end HBM stack', so ZAM is no longer implicitly given a backend property."
  - guard: "1T1C must NOT be called capacitor-less (capacitor relocated, not removed)"
    status: HELD
    evidence: "§2 bold anchor 'This is still a one-capacitor cell. The back-end move relocates DRAM's hardest part. It does not remove it.'; §5 'keeps the capacitor and merely moves it'; §6 'the capacitor was relocated into the back-end rather than removed.'"
  - guard: "channel material (IGZO/oxide) must NOT be attributed to the patent"
    status: HELD
    evidence: "§5 'It never names the channel material.' The only capacitor-less/TFT-material contrast is imec's 2T0C ('two thin-film transistors replace the storage capacitor entirely'), explicitly imec's and lab-stage — never conflated with the patent. No IGZO/oxide imported as Intel's."
  - guard: "'beats HBM4' numbers must NOT be attributed to this filing (patent has only the match-footprint GOAL)"
    status: HELD
    evidence: "§3 'in the document's words, \"With the goal of matching HBM4's footprint\" ... a goal on the page, not a result on a bench: the filing reports no bandwidth, no cost, no yield.' 'beating HBM' is attributed to ZAM (external, §4), not the patent."
  - guard: "productization must NOT be asserted (pending application)"
    status: HELD
    evidence: "§1 'This is one published application, not a product.'; §5 'a single published application, not a granted patent and not a product.' Title now says 'Filing' (r1-F4)."
  - guard: "strategic payload (foundry / who-can-make-HBM) is EXTERNAL INFERENCE, must stay labeled, never attributed to patent text"
    status: HELD
    evidence: "§4 ¶1 'Here the filing's own words stop, and the reading begins. Claim 1 says backend. It never says foundry, never says logic fab, never says without a DRAM fab ... the leap is mine, not the document's.' §6 keeps the inference conditional ('could let', 'if a back-end die matches ...'). gate_meta PASS — this is REQUIRED functional scope labeling, not banned reader-instruction."

# ===========================================================================
# PART C — NEW findings, round-2 full 7-pass fresh review
# ===========================================================================

findings:

  # ========================= LOW =========================

  - finding_id: r2-F1
    pass: pass-4-logic-causality
    location: §5 ("Read Cold ..."), 3rd paragraph
    severity: low
    severity_under_default_posture: low
    finding: |
      The §5 steelman-return restates the affirmative core as: "The cell is backend. That is the
      single property a logic-and-packaging line can carry and a front-end fab cannot, which
      makes the open question the numbers, not the direction."

      Read literally, "a front-end fab cannot [carry a backend cell]" over-states the contrast:
      a dedicated DRAM front-end fab is not intrinsically incapable of back-end / thin-film
      processing (every fab has a back-end-of-line). The precise, thesis-carrying claim — stated
      correctly in §6 ("the property that could let a logic-and-packaging maker carry HBM-class
      memory WITHOUT owning a DRAM front-end") and, after the r1-F2 fix, in §4 — is about what a
      backend cell does NOT NEED (the DRAM FEOL), which is what widens "who can make HBM". This
      is the SAME front-end / DRAM-front-end precision seam r1-F2 tightened on the §4 pivotal
      sentence; the round-1 fix did not reach this downstream §5 refrain (it is one of the two
      restatements r1-F5 deliberately left in place). It is LOW, not a repeat medium, because:
      (a) it is not the pivotal inference sentence (§4 is, and it is now correct); (b) the precise
      form is present in §6; (c) it sits inside the explicitly-labeled synthesis/steelman section;
      (d) the directional meaning (backend shifts the gating capability) is correct, so the reader
      is not misled about the thesis. A skeptical-pro reader could still catch the one-clause
      over-statement.
    recommendation: |
      Optional consistency tighten (narrow to what the anchor/spine supports — NEVER hedge, and
      do NOT touch the declared signature lines). Align the §5 restatement to the precise §6 form,
      e.g. "... the single property a logic-and-packaging line can carry without a DRAM front-end
      fab ..." or "... that a logic-and-packaging line can carry and a pure DRAM front-end play
      cannot claim as its own ...". Keeps the aphoristic return; removes the literal "a front-end
      fab cannot do backend" reading. Content and commitment unchanged.
    quote: "That is the single property a logic-and-packaging line can carry and a front-end fab cannot, which makes the open question the numbers, not the direction."

  # ========================= NO-FINDINGS PASSES (scoped_to = what was checked; falsifiable) =========================

  - pass: pass-1-voice-anti-ai
    finding: "no findings"
    scoped_to: |
      All 6 sections + 4 captions + title re-checked against deliverable-voice-rules.md +
      anti-ai-writing.md. Em-dash: 0 (re-grepped, confirmed). Banned-word grep: 0 (no delve /
      leverage / navigate / underscore / crucial / pivotal / showcase / groundbreaking / robust,
      etc.). No copula avoidance (direct is/are: "The cell is backend", "The direction is not in
      doubt", "The test is a number"). No not-just-X-but-Y, no despite-challenges, no
      sentence-initial Furthermore/Moreover/Additionally, no puffery. No elegant variation (Intel
      stays "Intel"; filing/application/document are plain descriptors). Bold: still exactly ONE
      load-bearing anchor (§2), unchanged by the revision (STRUCT-002 single-anchor slot). No
      naked FEOL/BEOL/HBI/XBM acronyms exposed to the reader. The §6 header semicolon ("The
      Direction Is Real; the Numbers Are the Test") is a deliberate parallel-antithesis on
      PROTECTED header surface, not the body-prose clause-splice AI tell — not flagged.

  - pass: pass-2-redundancy
    finding: "no findings"
    scoped_to: |
      Re-checked claim repetition and word-budget after the r1-F5 fix. The affirmative-core
      antithesis now lands in 2 identical-cadence places (§5, §6) + 1 varied (§4), down from 3;
      within the pass-7 <=3-section bound and no longer a felt chant. Both declared signature
      lines (§1 ¶3, §6 close) exempt per reader-energy §5 and are not among the counted
      restatements. No new redundancy introduced by the seven in-sentence swaps. (The residual
      §5 precision looseness is logged as r2-F1 under pass-4, not a redundancy finding.)

  - pass: pass-3-fact-paraphrase
    finding: "no findings"
    scoped_to: |
      Every [dddd] cite and every double-quoted span re-verified BYTE-BY-BYTE against patent.md
      and invention-summary.md Quote anchors: [0018] q-0018-1 (exact), [0069] blockquote q-0069-1
      (exact; correctly framed as claim 1 "as filed" WITH the Example anchor attached, per the
      invention-summary sanctioned method — Example 1 mirrors claim 1, "includes" vs "comprises"),
      [0027] q-0027-1 "approximately 1.5 GB ... back-end-of-line transistors" (exact), [0023]
      q-0023-1 "8-high and beyond" (paraphrased "eight high"), [0031] q-0031-1/q-0031-2 (r1-F3
      re-anchored, now exact-supported), [0034] q-0034-1 "With the goal of matching HBM4's
      footprint" + q-0034-2 "0.5-5 GB" (exact), q-0034-5 redundancy + q-0034-6 four gutters
      (accurate paraphrase), [0020] UCIe/HBI (accurate), [0073] TSV gutters term (accurate).
      All EXTERNAL facts matched to fact-check-log with Sources entries: HBM ~60% SK hynix
      (hbm-supply-concentration), three-player DRAM (dram-three-player), Intel NAND->SK hynix
      2021 + Optane 2022 (intel-exited-memory), ZAM hybrid-bonded / Z-angle (zam-hb3dm-specs),
      Powerchip-not-Intel (zam-powerchip-fab), incumbents 3D DRAM + SK hynix ~2030 (incumbent-
      3d-dram, r1-F7-scoped), imec 2T0C lab-stage (imec-2t0c-igzo), VLSI 2026 (zam-hb3dm-vlsi2026),
      ~2029 commercialization (zam-timeline). The SEEDED / not-re-verified `intel-foundry-hbm-
      basedie` fact is correctly NOT used in the draft. No paraphrase drift, no fact introduced
      beyond the Quotable spans, no patent-vs-news label collision.

  - pass: pass-5-reader-perspective
    finding: "no findings"
    scoped_to: |
      Re-read as the curious retail investor (reader-profile.md). Every term of art still glossed
      on first use (back-end, front-end, thin-film transistor, 1T1C, HBM4, TSV gutters, UCIe, base
      die, hybrid bonding, capacitor) — none removed by the revision; r1-F2/F3 swaps did not strip
      a gloss. No FEOL/BEOL/HBI/XBM acronym exposed. Money thread structural: every section feeds
      the verdict (§3 resolves to "no bandwidth, no cost, no yield"; §4 is the who-can-make-it
      stake; §5 steelman; §6 the call). No prerequisite-chain overload (<=1 new dependent concept
      per paragraph). No dead-spot / boredom point on the impatient-investor read. gate_structure
      PASS (no >=8-sentence paragraph); mobile line count fine.

  - pass: pass-6-lead-conclusion-format
    finding: "no findings"
    scoped_to: |
      6A lead — ¶1 opens on the discovery beat ("Intel's newest memory filing does something
      quietly radical. It builds the transistor inside each DRAM cell in the chip's back-end
      wiring layers"); patent on the table by sentence 2; full two-sided call lands by §1 ¶3
      (signature line 1). 6B closure — §6 returns to the Intel-left-memory / who-can-make-HBM
      frame and lands signature line 2; residual-risk = Acceptance(falsifiable) -> maps to
      closing-forward-watching-event / binary-test (VLSI 2026), which §6 delivers; under
      closing_posture: measured this is correct (NOT open-question). 6C Sources — 3 categories
      (Patents/Papers/News & media), all in the 5-enum, subgrouped all-or-nothing. 6D — Papers
      entry is institutional (imec), no "First, et al." issue. 6E — em-dash 0, [dddd] all
      4-digit, one "# Sources" h1. 6F title — no em-dash. 6G OVER-HEDGE — CLEAN in BOTH
      directions: verdict LEADS with the call ("The direction is not in doubt"), keeps exactly
      ONE patent-specific anti-hype guard (1T1C capacitor relocated-not-removed + "a back-end
      capacitor at HBM density and yield is precisely what no one has shipped"), references not
      re-lists the limits ("The bounds set out above still hold"), no safe-harbor boilerplate, no
      false equivalence, no qualifier-led verdict; and no OVERREACH (every forward claim
      conditioned: "could", "if the yield numbers land", "If a back-end die matches ..."). 6H
      DEFENSIVE-OPEN — CLEAN: no insurance fact precedes the ¶1 beat; status sits in ¶2. 6I
      ATTENTION-BUDGET — CLEAN: prosecution/status confined to §5 (the one pricing section) + one
      §1 lead clause + §6 recap; no process narration (fees/RCE/liens) anywhere; status LABELS
      only; spend-motif within budget.

  - pass: pass-7-adversarial-reader
    finding: "no findings"
    scoped_to: |
      Read fresh as impatient investor + skeptical pro-subject reader; 7 checks, each yes/no with
      a span. (1) HOOK: PASS — ¶1 declarative discovery beat, no verdict-insurance ahead, call by
      lead's end. (2) HEADER-AS-CLAIM: PASS — all 6 headers assert; header-only skim reconstructs
      the argument (company that left it -> claim 1 = one word backend -> tower matches HBM4 ->
      back-end cell could loosen the bottleneck -> read cold, it keeps the capacitor -> direction
      real, numbers are the test). (3) STEELMAN present + not overweight: PASS — §5 concedes
      SPECIFICALLY and THIS-patent (single application/no yield; keeps the capacitor vs imec 2T0C;
      incumbents already on 3D DRAM; Powerchip-not-Intel), ~9 concession sentences vs ~8 affirmative,
      and the section CLOSES on the affirmative ("not a rebuttal ... confirms the road is real, and
      this filing sketches a different lane" + the Powerchip supporting tell) — the affirmative core
      carries >= the concession, beat is net-new, no spend/procedure motif inside it, generic
      "patents don't guarantee products" truism NOT used as the steelman (SURF-007 clean). (4)
      META: PASS — "the leap is mine, not the document's" is REQUIRED functional scope labeling,
      gate_meta PASS. (5) JARGON: PASS — signposted, not deep-dived. (6) STUB: PASS — no section
      markedly shorter than siblings. (7) THESIS OVER-RESTATE: PASS — affirmative core in 3
      sections (§4/§5/§6), 2 declared signature lines exempt; within the <=3 bound (r1-F5 reduced
      the identical-cadence copies to 2). The one residual is the §5 precision looseness logged as
      low r2-F1 (pass-4), not a pass-7 count/steelman breach.

# ---------------------------------------------------------------------------
# Severity roll-up: critical 0 | high 0 | medium 0 | low 1
# Assessment rule (feedback-format.md): no critical, no high, no medium -> pass.
# Double-clean status: round 1 = revise-recommended; round 2 = FIRST clean round. This is a
# CONFIRMATION trigger (a fresh round-3 reviewer must independently return clean), NOT acceptance.
# Low r2-F1 does not change the assessment and is optional for the composer; if applied it is a
# narrow §5 precision align (never a hedge, never touching the signature lines).
# ---------------------------------------------------------------------------
