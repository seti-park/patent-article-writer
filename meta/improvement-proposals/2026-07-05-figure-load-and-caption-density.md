---
proposal_id: 2026-07-05-figure-load-and-caption-density
created: 2026-07-05T19:30:00Z
status: watch
lever: multi (gate-strengthen + reference-edit)
goal: "5"
root_cause_stage: gate + design
root_cause_artifact: _shared/scripts/gate_structure.py sentence splitter (splits on "FIG." abbreviation period → phantom sentence break, blocks the light-touch fix) + thesis-architect figure-selection.md (no per-section body-figure / caption-numeral load budget)
recurrence_count: 1
confidence: medium
triggering_findings:
  - essay_id: intel-us20250266395, self-post-accept goal-5-4a (§4 part-number/FIG-reference density stop-point; 2 cold readers "slid"; polish LEFT with reason — protected numerals)
  - essay_id: intel-us20250266395, self-post-accept goal-5-4a rationale (a light-touch fix was blocked because "gate_typography/structure counts 'FIG. 6A' as a phantom sentence break" → paragraph already at the STRUCT-001 7-sentence ceiling)
related:
  - 2026-07-03-longsent-boundary-merge (APPLIED; fixed the SAME merge class in gate_typography.py — did NOT reach gate_structure.py's SENTENCE_SPLIT_RE)
  - 2026-06-26-gate-structure-sentence-band-align (APPLIED; tightened STRUCT-001 to warn at >=8 — which makes the phantom "FIG." break more likely to trip a spurious warn)
  - 2026-07-05-procedure-attention-budget (APPLIED; goal-5 attention-budget doctrine + SURF-005/006 for PROCEDURE load — this is the FIGURE-load sibling)
  - SURF-003 (cover-caption numeral density >6, warn) — the cover-side precedent for a body-caption-density check
---

## Problem — a real goal-5 stop-point that the surface passes cannot relieve

The essay shipped double-clean, self-audit-DRY, 14/14 gates zero warns — and **two independent
cold readers** still "slid" through §4 ("Power Comes Up Through the Floor"). Both named the same
cause: a pile-up of protected figure numerals across three captions plus prose
(**526, 536, 701, 702, 704, 872, 882, 860**) with the acronyms (TSV, TGV) and "FIG. this / FIG.
that" stacked fast. This is a genuine goal-5 (reader-energy) cost, and it is **structurally hard**
because the surface passes have no lever left:

1. **The numerals are protected surface.** Each `NNN` is a grounded reference part-number; the
   `prose-polish` pass (윤문) correctly LEFT them byte-intact ("could not smooth without dropping a
   protected numeral", `polish-notes.md` §4 density outcome). Polish fixed what it could (two
   acronym double-appositives, one 42-word split) but could not thin the numeral density.
2. **The light-touch structural fix is *blocked by a gate parsing artifact*.** The self-audit
   drafted a stronger side-thread signal for the §4 glass paragraph, then had to **revert** it:
   the paragraph "already sits at the gate's 7-sentence ceiling (gate_typography/**structure**
   counts 'FIG. 6A' as a phantom sentence break), so adding a sentence trips STRUCT-001 at 8."

Point 2 is a **verifiable, mechanically-safe** defect. `gate_structure.py` splits sentences with
`SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?])\s+")` and `_count_sentences` counts the pieces. The
period in "**FIG. 6A**" (or "No. 8", "e.g. ") is followed by a space, so it is counted as a
sentence terminator — an inline **phantom sentence break** that inflates every figure-referencing
paragraph's STRUCT-001 count. The applied `2026-07-03-longsent-boundary-merge` fixed the *same
class* in `gate_typography.py` but did **not** touch `gate_structure.py`'s splitter; and the
applied `2026-06-26-gate-structure-sentence-band-align` tightened STRUCT-001 to warn at `>=8`,
which makes a spurious phantom break *more* likely to reach the warn line and to falsely block a
legitimate light-touch split — exactly what happened here.

So signal 3 decomposes into a clean mechanical fix and a harder design question. This proposal
carries **both** levers (as `2026-07-05-procedure-attention-budget` did), with distinct statuses.

## Part A — gate-strengthen (the unblock): abbreviation-aware sentence split in gate_structure

**File: `.claude/skills/_shared/scripts/gate_structure.py`** — before splitting, protect
abbreviation periods (at minimum `FIG.`, `Fig.`, `No.`, `e.g.`, `i.e.`, single-capital initials)
so an inline "FIG. 6A" is not counted as a sentence boundary:

```diff
 SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?])\s+")
+# Abbreviation periods are NOT sentence terminators. "FIG. 6A", "No. 8", "e.g. x" must not
+# create phantom sentence breaks that inflate STRUCT-001 (ledger: longsent-parser-merge-artifact,
+# the gate_structure sibling of the applied 2026-07-03 gate_typography fix).
+_ABBREV_RE = re.compile(r"\b(FIG|Fig|fig|No|Nos|e\.g|i\.e|cf|vs|Dr|Mr|Ms|St)\.", re.IGNORECASE)
+
+def _protect_abbrev(text):
+    return _ABBREV_RE.sub(lambda m: m.group(0).replace(".", ""), text)

 def _count_sentences(text):
     text = text.strip()
     if not text:
         return 0
-    parts = [s for s in SENTENCE_SPLIT_RE.split(text) if s.strip()]
+    parts = [s for s in SENTENCE_SPLIT_RE.split(_protect_abbrev(text)) if s.strip()]
     return len(parts) if parts else 1
```

Ship with `test_gates.py` cases: a paragraph with N real sentences + several "FIG. K" tokens
counts N (not N + tokens); a genuine terminal "…metrics. And then…" still splits; a fixture drawn
from this run's §4 glass paragraph counts at its true sentence total (headroom restored below the
STRUCT-001 warn). **Warn-only gate → never flips a round's pass/fail**; this only stops false
STRUCT-001 warns and restores the light-touch split headroom the self-audit needed.

Part A is mechanically safe with an applied precedent (same class, sibling gate); on its own it
would file at `recommended-apply`. It is carried here at the proposal's `watch` status because it
is bundled with Part B; a human may split it out and apply Part A immediately.

## Part B — reference-edit (the durable fix): a Phase-1 body-figure / caption-numeral load budget

Part A restores *headroom*; it does not reduce the intrinsic numeral density a figure-heavy section
carries. The only lever that actually thins the density is **upstream, at figure selection** — the
numerals cannot be dropped in Phase 3 (protected), so the count has to be budgeted before the
figures are chosen. Proposed, symmetric with the applied procedure-attention-budget and the
cover-side SURF-003:

1. **thesis-architect figure-selection (reference-edit):** add a per-section **figure-load budget**
   awareness — when a single body section is assigned ≥3 body captions **or** its captions carry
   more than ~6 distinct reference numerals (the SURF-003 cover budget, applied to a body section),
   surface it to the orchestrator as a goal-5 attention-budget flag (thin the section, move a figure,
   or split the section), rather than discovering it as a cold-reader stop-point at self-audit. This
   run's §4 carried FIG. 7 + FIG. 8 captions + FIG. 9/10 prose pointers + the numeral set above — a
   selection-time flag would have caught it.
2. **Candidate warn-only SURF-007 (gate-strengthen; build only if the class recurs):** a body
   section whose figure captions carry > K distinct reference numerals ⇒ warn (never fail — numerals
   are protected). Mirrors SURF-003's cover check on the body. Ship a fixture from this run's §4 to
   size K empirically; hold until a second run corroborates the density-as-stop-point signal.

## Why this shape / why watch

- Numerals are **protected surface**, so a hard gate is impossible in both parts — the mechanical
  lever can only *surface* (warn) or *restore headroom* (Part A), never fail. The durable relief is
  the Phase-1 budget (Part B).
- `watch`, count 1: the density-as-stop-point is corroborated by two cold readers **within one run**
  but not yet across runs; K for SURF-007 needs a second data point to size without false positives.
- Sequencing note for the human: apply **Part A first** (mechanically safe, unblocks light-touch
  goal-5 splits immediately, applied-precedent), then trial Part B's selection-time flag on the next
  figure-heavy run before committing SURF-007.

## Regression expectation

- Part A: `python .claude/skills/_shared/scripts/test_gates.py` — new abbreviation cases pass; the
  existing STRUCT-001 cases (incl. `2026-06-26-gate-structure-sentence-band-align`'s 8-sentence case)
  must still emit exactly one warn at a true 8 sentences. `python meta/regression.py` — `clean-baseline`
  / `figure-orphan` verdicts unchanged (STRUCT is warn-only; confirm no fixture paragraph loses/gains a
  warn *except* where a phantom "FIG." break was previously miscounted, which is the intended change).
- Part B: reference-edit + optional gate; no regression impact until SURF-007 is built (then it ships
  with its own fixture and cases).
