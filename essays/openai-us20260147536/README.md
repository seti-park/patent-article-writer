# openai-us20260147536 — "OpenAI's Chip Patent Does Floating-Point Math on Integer Adders"

Run of **US 2026/0147536 A1** (OpenAI Opco, LLC, "Alignment in Hardware Accelerators"; filed
2025-11-21, published 2026-05-28, priority 2024-11-22 — a **pending application**, not a
granted patent; claims 11–19 read "(canceled)"). Discovery register, selected from Phase 1's
five title-lead candidates. Figure-enabled edition (the owner supplied the 64 drawing sheets
mid-run; Phase 0 cleaned a priority set).

- **reader_sentence delivered:** "OpenAI had the actual design for its own AI chip on file
  almost a year before they announced it — down to the individual memory cell, so
  'OpenAI-designed' isn't marketing, it's literal." Both self-audit cold readers (rounds 1 and
  2) reproduced it unaided.
- **Thesis (one line):** OpenAI's first-published chip patent claims a compute-in-memory engine
  that does the expensive half of floating-point matrix math on plain integer adders, and its
  transistor-level depth — dated ~11 months before the Broadcom announcement — is primary
  evidence that "OpenAI-designed" silicon is literal engineering. The verdict is bounded (a
  dated *record* of circuit design, not proof of shipping silicon), not hedged.
- **closing_posture:** firm.

## Deliverable
- `essay-final.md` (draft_version 6): double-clean accepted (rounds 5 + 6) → self-audit-dry
  (2 rounds, 4 blind readers each) → Phase 3.7 윤문 polish (5 surface-only edits,
  `polish-notes.md`) → v6.
- `publication-package/publication.md` — the X Articles strip (one line per paragraph),
  `posting-checklist.md`, and the four placed figures.
- `owner-briefing.md` — Korean 발행자 브리핑 (schema ①–⑦, every 근거 verbatim, gate_quotes-verified).
- `promo/promo-pack.md` — Phase 4 (Korean long-form post + English thread).

## Figures
Header **FIG. 4** (the align-once / column adder-tree core — the thesis made visual). Body
captions **FIG. 1** (system datapath) and **FIG. 3** (column-cell multiply) in §2, **FIG. 43**
(dual-bank double-bitcell) in §4. `figures/` holds the cleaned priority set (1, 2, 3, 4, 6, 38,
42, 43, 45, 46); `figures/figures-manifest.md` catalogues all 64 sheets.

## Provenance (loop shape)
- **Independent claims 1, 20, and 29** carry the core triad — a completeness correction (r4-F1)
  that BROKE a candidate double-clean at confirmation round 4 and was fixed upstream (the
  invention-summary Claim scope map omitted claim 29) before re-acceptance at rounds 5 + 6.
- **Self-audit (2 rounds):** applied a prior-art scoping fix (the align-once arithmetic IS
  block floating point; OpenAI seeks the CIM *circuit*, SKPRO-01), a FIG. 4 drawing-type
  correction (functional block, not schematic, SKPRO-02), and two grounding anchor fixes
  (§4 [0002]→[0004]; §2 co-cite [0011] [0133]).
- **Score history:** `score-history.md`. **Loop verification:** check_run.py PASS.
- **Gates:** 14-gate suite PASS (0 fails) on the final; gate_quotes + gate_hedge green;
  verdict hard-gate held every round under firm posture.

## Notes
- This run had NO figures at first (text-only); it became figure-enabled when the owner uploaded
  the drawing sheets. The text-only figure-selection artifacts were superseded in place.
- Not established by this run (stated in the essay): whether this design is in Jalapeño or any
  shipping chip; whether it is in silicon (the numbers are design examples); the final claim
  scope (pending examination). The essay scopes the call to these bounds without hedging it.
