---
proposal_id: 2026-07-03-longsent-boundary-merge
created: 2026-07-03T00:20:00Z
status: applied  # 2026-07-04 reader-first overhaul; regression PASS
lever: gate-strengthen
goal: "3"
root_cause_artifact: _shared/scripts/gate_typography.py sentence splitter
recurrence_count: 3+
confidence: high
triggering_findings:
  - essay_id: etched-us12361091, 7-9 LONGSENT-001 warns per gate run (x6 runs); three independent reviewers separately re-verified the same false positives (rounds 1-3)
  - prior ledger records: 2 pre-existing LONGSENT entries
---

## Problem

The LONGSENT-001 splitter merges text across structural boundaries — frontmatter into the
first heading, headings into captions, `**bold thesis line**` into the following sentence,
"# Sources" into list rows — producing 37-137-word "sentences" that are not sentences. Every
round, a fresh reviewer burned verification effort re-clearing the same artifacts (documented
in edit-log rounds 1-3 and two selfaudit reports). Real long sentences (quote-integrated
claim clauses) are permitted by the voice rules, so nearly the entire warn census is noise.

## Proposed change (exact diff sketch)

**File: `.claude/skills/_shared/scripts/gate_typography.py`**

```diff
-    text_for_sentences = strip_markdown(body)
+    # Split into structural units first; never merge across these boundaries.
+    units = re.split(r"^---$|^#{1,6}\s|^\*\*[^*]+\*\*$|^\!\[|^\|", body, flags=re.M)
+    text_for_sentences = [strip_markdown(u) for u in units]
```

(Plus: skip YAML frontmatter block entirely; treat a figure caption line as its own unit.)
Ship with test_gates cases: frontmatter+heading merge (no warn), bold-line boundary (no
warn), genuine 40-word prose sentence (warn preserved).
