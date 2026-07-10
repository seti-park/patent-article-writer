# Posting checklist — openai-us20260147536

## Cover image
- **Candidate:** FIG. 4 (`fig-04.png`), the align-once / column adder-tree functional block —
  the one drawing that shows the thesis (per-row Shift Calculation `EMax − E`, the shifted
  mantissas, `Shift >> + 2's Complement`, `INT30 → Adder Tree → INT35`).
- **Crop guidance:** the cleaned sheet is landscape (2000×1301). For a 5:2 feed cover, crop the
  horizontal band from the `Shift Calculation (EMax − E)` block through `Shift >> + 2's
  Complement` to the `Adder Tree` → `INT35` output; the align-then-integer-accumulate flow
  survives the crop in one line. Auto-crop intentionally NOT shipped — crop at publish time so
  the `INT35` output label is not clipped.
- **Fallback:** FIG. 1 (`fig-01.png`, the system datapath) as header if the FIG. 4 crop reads
  too dense at feed size.
- Cover caption carries no reference numeral (numerals deferred to §2 in round-2 r2-F1 +
  self-audit) — within the ≤6 feed budget (SURF-003).

## Figures placed (in-body)
- FIG. 4 — header/cover (image + caption)
- FIG. 1 — §2 (the one-pass datapath: input buffer → CIM macro 101 → mode decoding 110 →
  dequantization 106 → FP22), caption-only-italic
- FIG. 3 — §2 (one column cell, the multiply that makes a primitive product), caption-only-italic
- FIG. 43 — §4 (double-bitcell / dual-bank behind double-buffered weight loads), caption-only-italic
- Available but NOT placed (prose carries these): FIG. 2, 6, 38, 42, 45, 46 (cleaned, in
  `figures/`); the full 64-sheet catalogue is `figures/figures-manifest.md`.

## Pre-post verification
- Confirm the independent-claim set is stated as **1, 20, and 29** (not "1 and 20"): the core
  triad is claimed by three independent claims — this survived a broken double-clean at
  confirmation round 4 (r4-F1) and must not regress.
- Confirm the align-once/integer-accumulate arithmetic is labeled **block floating point**
  (prior art, `[0141]`) and that what OpenAI "seeks to own" is scoped to the **compute-in-memory
  circuit** — not the arithmetic idea (self-audit SKPRO-01).
- Confirm the FIG. 4 cover caption calls it a **functional block diagram** / data flow, not a
  circuit schematic (`[0138]`; self-audit SKPRO-02).
- Confirm the verdict is firm and un-hedged: no source connects these circuits to Jalapeño and
  none shows the macro in silicon — that single THIS-patent guard is the only insurance clause.
- Confirm dates: priority **2024-11-22** vs the OpenAI/Broadcom announcement **2025-10-13**
  ("about eleven months"); Jalapeño reveal **2026-06-24**, initial deployment target end of 2026.
- publication.md is the strip source (one line per paragraph); `# Sources` block intact; every
  `[dddd]` is a patent-paragraph anchor (house convention, retained).
