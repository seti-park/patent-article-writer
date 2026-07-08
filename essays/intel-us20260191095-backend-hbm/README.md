# intel-us20260191095-backend-hbm — "Intel's Filing Moves the DRAM Cell Into the Back-End"

> **2026-07-07 human post-accept revision (v5 → v6):** owner-directed credit added — a
> one-sentence italic standfirst under the title acknowledging that this essay was prompted by a
> thread from @Underfox3, which flagged the filing, its Cross-Batch Memory (XBM) design, and the
> backend-DRAM-over-UCIe move. Additive note only: no argument prose, no `[dddd]` anchor, no
> signature line touched; the credit holds to the design facts shared with the patent (XBM = the
> patent's `[0034]` term; backend 1T1C DRAM `[0020]`; UCIe `[0034]`) and does not adopt the
> source thread's bolder "HBM4 competitor / lower cost" framing into the essay's measured voice.
> Gates 14/14 PASS (0 warns); publication re-stripped; check_run PASS. Deltas: `revision-notes.md`
> (origin human-post-accept). The Phase 4 promo pack is unchanged (article-only credit).

Run of US 2026/0191095 A1 (Intel Corporation, "Ultra High Bandwidth Memory with Backend
Transistors"; filed 2024-12-26, published 2026-07-02 — a **pending application**, not a
granted patent). Edition framed by the reader's live question: with Intel back in the memory
headlines (the Intel + SoftBank ZAM / HB3DM "HBM killer"), is this filing that story, or
something else? Discovery register, selected from Phase 1's five title-lead candidates.

- **reader_sentence delivered:** "Intel's filing moves the DRAM cell into logic-stackable
  back-end layers, and if the yield numbers land, who can make HBM stops being a three-company
  club." Both self-audit cold readers reproduced it unaided (round-1 cold reader: *"…build the
  memory cell up in the chip's wiring… could let a foundry make the AI memory everyone's short
  on… but it's just a filing with no numbers yet"*; round-2 cold reader read to the end).
- **Thesis (one line):** the filing builds the 1T1C DRAM cell from back-end (BEOL) transistors
  and stacks the dies eight-high to match HBM4's footprint; because the cell now lives in the
  back-end, the filing quietly reframes HBM-class memory as a candidate output of a
  logic-plus-BEOL-plus-packaging flow, not the exclusive product of a dedicated DRAM front-end
  fab. The claim that carries it turns on **one word — "backend."** The strategic payload
  ("who can make HBM") is the essay's labeled inference, riding external facts on that one
  claim word — never attributed to the patent.
- **Deliverable:** `essay-final.md` (draft_version 5: double-clean accepted → self-audit-dry
  (3 rounds) → Phase 3.7 윤문 polish, 9 surface-only §2→§3 edits, `polish-notes.md`) ·
  publication strip `publication-package/publication.md` · 2 declared signature lines · register
  discovery · `closing_posture: measured`.
- **Owner artifacts:** `owner-briefing.md` (한국어 발행자 브리핑, gate_quotes PASS against the
  archived `patent.md` snapshot; ⑥ knowledge-boundary map holds the guards) ·
  `promo/promo-pack.md` (Phase 4) · `patent.md` (the run's exact input snapshot; all `[dddd]`
  anchors resolve offline).
- **Figures placed:** FIG. 1B (cover/header, the isometric 8-high die stack on a base die),
  FIG. 1F (§2, the back-end "TRANSISTOR" layers — the claimed cell), FIG. 1G (§3, the basic
  building block: sub-channels + TSV gutters), FIG. 1A (§4, logic die beside the memory stack
  on one package). Not rendered (prose pointers instead): FIG. 1C/1D/1E/1H, 2, 3, 4, 5, 6, 7.
  Cover crop guidance in `publication-package/posting-checklist.md`.

## Run shape (score-history.md)

| Round | Type | Assessment | Gates | Note |
|---|---|---|---|---|
| 1 | review | revise-recommended | 14/14 | 2 medium (§6 verdict attributed "back-end" to the hybrid-bonded ZAM proxy; §4 "crystalline-silicon front-end" → needs "DRAM"), 5 low |
| — | revision-1 | — | 14/14 | 7/7 applied (2 medium + 5 low); all narrow/label/cut, no hedge added |
| 2 | review | **pass** | 14/14 | first CLEAN; both mediums verified landed; 1 new low |
| 3 | confirmation | **pass** | 14/14 | second CLEAN, fresh independent reviewer, unchanged draft → **double-clean** |

- **Self-audit (3 rounds, converged dry):** round 1 = 2× adversarial-reader (impatient
  investor + skeptical domain expert) + grounding-verifier + cold reader; round 2 = grounding +
  skeptic + cold reader; round 3 = skeptic dryness confirmation. **Applied 12 findings** — the
  headline one being an accuracy fix the expert caught: §4 had set up a false "TSV gutters +
  UCIe **instead of** [ZAM's] hybrid bonding" dichotomy (mixed axes, and the filing's own
  `[0020]` both-sided HBI / `[0023]` wafer-to-wafer are hybrid-bonding-consistent), corrected so
  the ZAM contrast rests on the back-end-cell axis and the filing's bonding is left unstated.
  Also: §3 plumbing compressed (cold-reader stall), §5 affirmative core narrowed to "without
  owning a DRAM front-end", §6 verdict de-circled + VLSI-2026 scoped to a class/direction test,
  glosses for "sub-channel"/"interposer", §6 "direction" term-collision fix. **Rejected** the
  impatient reader's meta-phrase nit (single-vote) and **kept** the Powerchip-fabs-ZAM tell (its
  double edge — a DRAM foundry still in the loop — is a fair measured-verdict limit). Grounding:
  **ALL SUPPORTED across rounds 1-2** (double-clean grounding). Normalized to
  `meta/findings-ledger.jsonl` (origin self-post-accept).
- **check_run.py:** PASS (double-clean acceptance; every medium+ finding dispositioned;
  self-audit evidence present; owner-briefing present). Two informational RUN-000 WARNs flag a
  transition-classification heuristic (gate results identical across a revised transition) —
  no real gap: `revision-response.round-1.md` carries the 7 dispositions.

## Grounding discipline notes (this edition)

- The strategic payload — foundry / logic-fab / "who can make HBM" — is **external inference by
  design**. The patent supports only the claim word **"backend"**; it never says foundry, logic
  fab, cost, $/bit, yield, or the channel material. The leap is labeled in-text ("the leap is
  mine, not the document's") and rides `fact-check-log.md` external facts, never a patent anchor.
- **Not asserted = ZAM.** Same direction (tall custom 3D DRAM to beat HBM4; base die + high-speed
  I/O), distinct filing; the distinction is spent exactly twice (§4 + §6 class-vs-cell). The
  filing's own bonding method is left unstated (consistent with `[0020]`/`[0023]`); no ZAM
  property (Z-angle, hybrid bonding, ~171 mm², Powerchip, 2× HBM4) is attributed to the patent.
- **1T1C is not capacitor-less** — the cell keeps its capacitor, relocated to the back-end, not
  removed; imec's 2T0C/IGZO capacitor-less path is external contrast only. Channel material is
  unnamed in the patent and never imported.
- **Description ≠ claim** throughout: claim 1 requires only "backend"; 8-high is claim 2, UCIe /
  "match HBM4 footprint" / sub-channels / BIST are spec or dependent claims; pinned values
  (1.5 GB, 0.5-5 GB, eight-high) are presented as description, never as claim bounds.
- **Measured verdict, both directions:** the close leads with the direction-commitment, prices
  the uncertainty with two this-filing anti-hype guards (the 1T1C capacitor ceiling; the
  back-end-cell differentiator has no public proof point yet, VLSI 2026 → ~2029), and lands firm
  ("a question of yield, not of architecture") — no overreach, no safe-harbor hedging
  (`gate_hedge` PASS under the measured posture).
- **Gate-scope fix (round 1):** `gate_figure_use` false-orphaned figs 2-7 (it scrapes every
  `FIG. N` token in `figure-selection.md`, including the non-selected packaging-variant figures
  named in prose). Fixed at the Phase-1 artifact by naming non-selected figures in word form;
  the selection is unchanged and no figure was forced into the draft. The systemic fix (scope the
  gate's selected-set to the explicit selection table) is routed to `pipeline-retro` (propose-only).
