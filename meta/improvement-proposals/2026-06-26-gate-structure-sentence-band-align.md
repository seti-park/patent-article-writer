---
proposal_id: 2026-06-26-gate-structure-sentence-band-align
created: 2026-06-26T00:00:00Z
status: applied  # 2026-07-02 architecture refactor; regression PASS
lever: gate-strengthen
goal: "3"
root_cause_artifact: _shared/scripts/gate_structure.py (STRUCT-001 threshold off-by-one vs editorial Pass 2C)
recurrence_count: 3
confidence: high
triggering_findings:
  - essay_id: us12560948b2 ad-hoc run, pattern_tag: paragraph-eight-sentence-slip (3 instances incl. one revision regression)
---

## Problem

`gate_structure` STRUCT-001 warns only when a paragraph has **more than** `MAX_SENTENCES_PER_PARA`
sentences (`n > 8`, i.e. 9+). Editorial Pass 2C flags `>= 8` as **high** ("8+ sentence paragraphs
in essay: high severity"). So a paragraph of exactly 8 sentences passes the mechanical gate and
then fails the editor. The ad-hoc run on US 12,560,948 hit this three times, including once as a
regression: splitting one over-long paragraph pushed a neighbor to exactly 8, invisible to the
gate, caught only on a manual re-count.

This is a one-off-by-one between the two layers that are supposed to agree. Closing it makes
paragraph length fully mechanical (the author/composer sees the warn before Pass 2C does) and kills
the "fix introduced a new 8" regression class at the gate.

## Proposed change (exact diff)

**File: `.claude/skills/_shared/scripts/gate_structure.py`**

```diff
-MAX_SENTENCES_PER_PARA = 8       # STRUCT-001 threshold
+# Editorial Pass 2C flags >= 8 sentences as high; the gate warns at the same boundary.
+MAX_SENTENCES_PER_PARA = 7       # STRUCT-001: warn when a paragraph exceeds the 3-7 band
```

(The comparison stays `if n > MAX_SENTENCES_PER_PARA`, so with the constant at 7 it now warns at
`>= 8`, matching Pass 2C. Update the docstring line "more than MAX_SENTENCES_PER_PARA sentences"
to "more than 7 sentences (8+ is a Pass 2C high)".)

**File: `.claude/skills/_shared/scripts/test_gates.py`** — add a case: an 8-sentence body
paragraph emits exactly one STRUCT-001 warn; a 7-sentence paragraph emits none. Update any existing
STRUCT-001 fixture that assumed the `>8` boundary.

## Why this lever

- The defect is a mechanical threshold mismatch, so a mechanical fix is exact and safe — no
  judgment. STRUCT-001 is warn-only, so this never changes any round's pass/fail; it only surfaces
  the 8-sentence case earlier, where it is cheap to fix.
- Complements `2026-06-11-gate-structure-word-wall.md` (word-count walls). Sentence-count and
  word-count are the two paragraph-length failure modes; with both, the band is fully gated.

## Regression expectation

- `python .claude/skills/_shared/scripts/test_gates.py` — add the 8-sentence case; all pass.
- `python meta/regression.py` — `clean-baseline` and `figure-orphan` verdicts unchanged (STRUCT
  warnings never flip a verdict; confirm clean-baseline has no 8-sentence paragraph, else it gains a
  harmless warn).
- Success criterion: next run, any exactly-8-sentence paragraph shows a STRUCT-001 warn before Edit.
