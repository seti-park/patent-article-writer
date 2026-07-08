<!--
  handoff/02-compose/revision-response.round-1.md
  Produced by: essay-en-composer (revision mode, references/revision-mode.md)
  Consumed by: editorial-review round 2 (re-review protocol) + check_run.py
  One disposition block per medium+ finding_id from edit-log.round-1.md; lows itemized.
-->

# Revision response — round 1

draft_version: 2  <!-- this revision produced draft_version 2 -->

Assessment being answered: revise-recommended (medium 2, low 5). All 7 findings APPLIED; 0
rejected. Every fix is anchor/narrow/label per the grounding fence — no hedge added, the
`closing_posture: measured` verdict and both declared signature lines are untouched.

## r1-F1  (medium, §6 verdict — pass-3)

- disposition: applied
- fix direction: narrow → label (grounding fence; verdict NOT hedged)
- change: §6 ¶3, the proof-point sentence. "a back-end HBM stack" → "this class of tall,
  stacked HBM challenger". The ZAM / HB3DM readout that surfaces at VLSI 2026 is hybrid-bonded
  (fact-check-log `zam-hb3dm-specs`), not a BEOL / backend-transistor stack, so the old phrase
  imported a backend property the sources do not support onto the ZAM proxy. The
  direction-commitment ("will either hold up or they will not"), the named test-bed (VLSI 2026,
  June), and the ~2029 horizon are all preserved; only the false backend attribution comes out.
- before: "There, the density, yield and cost per bit of a back-end HBM stack will either hold up or they will not."
- after:  "There, the density, yield and cost per bit of this class of tall, stacked HBM challenger will either hold up or they will not."
- source fix: the same phrasing was mirrored in thesis-trace.md "Closing directive realization"
  forward_pointer; updated there too so a re-compose cannot reintroduce it.

## r1-F2  (medium, §4 — pass-4)

- disposition: applied
- fix direction: narrow the claim to the anchor/spine (Axis 4 = the DRAM FEOL, not front-end
  silicon generally). Logic foundries also run crystalline-silicon front-ends, so the defensible
  claim is the DRAM front-end. Closes the strongest skeptical-pro opening §5's steelman pre-empts.
- change: §4 ¶3, the pivotal inference sentence. Inserted "DRAM": "the crystalline-silicon
  front-end" → "the crystalline-silicon DRAM front-end".
- before: "it does not need the crystalline-silicon front-end that only a dedicated DRAM fab runs"
- after:  "it does not need the crystalline-silicon DRAM front-end that only a dedicated DRAM fab runs"

## r1-F3  (low, §3 ¶1 — pass-3)

- disposition: applied
- change: "so many layers fit inside a standard height [0031]" reached past its anchor ([0031] /
  q-0031-2 supports only "thinning of the silicon ... to enable many-layer stacking"; the height
  budget lives at [0044]-[0045]/[0034], not [0031]). Re-anchored to what [0031] carries:
  "with the silicon thinned to enable that many-layer stacking [0031]". "that" ties back to the
  eight-high stack in the same sentence; no height claim now rides [0031].

## r1-F4  (low, Title — pass-3)

- disposition: applied (judgment call — reasoning below)
- change: title "Intel's Patent Moves the DRAM Cell Into the Back-End" → "Intel's Filing Moves the
  DRAM Cell Into the Back-End".
- reasoning: this is a factual/scope finding (pending application vs granted patent), so
  revision-mode's surface fence does NOT protect the title on style grounds — the "UNLESS the
  finding is factual" carve-out applies and it is dispositioned like any other factual finding.
  Headline "patent" is a defensible colloquial umbrella, but for a *measured, anti-oversell*
  investor edition whose body is scrupulous about status ("not a granted patent and not a
  product"), the highest-read line should not buy feed force with the exact imprecision the body
  spends words correcting. "Filing" is identical length (52 chars, well under SURF-001's 70), the
  round-1 reviewer certified it "equally strong as a hook," and it now matches signature line 1's
  "Intel's filing ...". Net: goal-1/4b accuracy-coherence gained at ~zero goal-5 cost. thesis-trace.md
  title line updated. (If a round-2 reviewer prefers the headline-convention reading, either is
  defensible; flagging the judgment here.)

## r1-F5  (low, §4/§5/§6 identical-cadence refrain — pass-2 / goal-5)

- disposition: applied
- change: varied the §4 occurrence (the inference-intro; NOT a declared signature line) so the
  affirmative core no longer lands three times in the identical "a logic-and-packaging X can carry /
  a [DRAM] Y cannot" antithesis. §5 (steelman return) and §6 ¶1 (verdict) keep their versions.
- before (§4): "Backend is the property a logic-and-packaging flow can carry, where a front-end DRAM cell cannot."
- after  (§4): "Backend belongs to the logic-and-packaging world, not the DRAM front-end."
- content unchanged (backend is achievable via logic+packaging, not the DRAM front-end); the
  "can carry / cannot" chant is de-duplicated on the mobile scroll.

## r1-F6  (low, §4 FIG. 1A caption — pass-3)

- disposition: applied
- change: caption made literal (co-packaging), the manufacturing-flow leap stays in §4 prose where
  it is labeled inference. "the picture of one flow carrying both" (imports §4's FLOW inference onto
  a figure that literally shows co-PACKAGING) → "the two joined on a single interposer" (what FIG. 1A
  [0022] shows: physical co-location on one interposer).
- before: "... on a single interposer, the picture of one flow carrying both."
- after:  "... (104), the two joined on a single interposer."
- figures-rationale.md unchanged: its FIG. 1A note is that the figure grounds the "one flow" reading
  *visually at the point the prose argues it* — still true (the prose still argues it, labeled).

## r1-F7  (low, §5 ¶2 — pass-3)

- disposition: applied
- change: the ~2030 date was over-generalized to all three incumbents; fact-check-log
  `incumbent-3d-dram` pins only SK hynix to ~2030 (2029-2031), logs Samsung as a VCT roadmap (no
  date) and Micron as research since 2019 (no 2030 target). Scoped the date to SK hynix; Samsung and
  Micron kept as programs without a flattened date. The "three funded roadmaps" stake (next sentence)
  is untouched.
- before: "SK hynix, Samsung and Micron each run their own 3D-DRAM programs pointed at roughly 2030."
- after:  "SK hynix, Samsung and Micron each run their own 3D-DRAM programs, SK hynix's aimed at around 2030."

## Gate status

- No gate `check_id` was handed back as failing for this round. Self-check re-run after the edits:
  no new FAIL introduced (em-dash 0, banned 0, anchors/quotes intact, no paragraph crossed the
  3-7 sentence band — all seven edits are in-sentence word swaps, no split/merge).
- Pre-existing `figure_use` FIGUSE-001 (figures 2-7) is unchanged and remains a Phase-1
  `figure-selection.md` tokenization artifact, not a composition defect (documented in
  figures-rationale.md); not introduced or fixable by this revision.

## Volunteered changes (beyond findings)

- None beyond the two thesis-trace.md consistency edits noted under r1-F1 (forward_pointer) and
  r1-F4 (title). No paragraph was split/merged; both declared signature lines and the single §2
  bold anchor are byte-for-byte unchanged; `closing_posture: measured` preserved.
