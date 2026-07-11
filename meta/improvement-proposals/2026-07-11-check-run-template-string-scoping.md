---
proposal_id: 2026-07-11-check-run-template-string-scoping
created: 2026-07-11T14:20:00Z
status: recommended-apply
lever: gate-promotion
goal: "all"
root_cause_stage: gate
root_cause_artifact: _shared/scripts/check_run.py (CAP_HIT_RE whole-file search; _is_confirmation_transition signal 3 whole-row-line regex) + handoff-template/03-edit/score-history.md schema comment
recurrence_count: 2
confidence: high
triggering_findings:
  - essay_id: tesla-us20260196678-hemmed-tabless, check_id: RUN-013, pattern_tag: checker-template-string-collision
  - essay_id: tesla-us20260196678-hemmed-tabless, check_id: RUN-000, pattern_tag: checker-confirmation-overfire
  - essay_id: intel-us20260191095-backend-hbm, check_id: RUN-000, pattern_tag: checker-confirmation-overfire (prior essay, veto proposal 2026-07-06 applied)
---

## Problem

Two check_run detectors read semantic control tokens from *anywhere* in
`score-history.md` instead of from the field that carries them:

**(a) CAP HIT template-string collision — deterministic on every future run, and it
masks RUN-005.** `cap_hit = CAP_HIT_RE.search(_read(score_path))` (whole file,
`\bCAP\s+HIT\b`, case-insensitive). The shipped template
`handoff-template/03-edit/score-history.md` line 6 contains, inside its schema comment:
`CAP HIT is recorded as a row with notes: CAP HIT.` — so **every faithful template copy
sets cap_hit=True**. Consequences observed this run (pre-strip) and reproduced post-run:

- False `RUN-013 FAIL` ("declares CAP HIT but cap-confirmed.md is missing") on a
  legitimately double-cleaned, never-capped run — RUN-013 fires on cap_hit regardless of
  acceptance.
- RUN-006-path noise mid-loop (cap_hit + not-yet-accepted → "promoted via CAP HIT" warn).
- **False negative (the serious one):** `if not accepted_clean and not cap_hit: RUN-005`
  — a truthy template comment SUPPRESSES the promoted-without-acceptance FAIL,
  downgrading a premature promotion to a warn. A stale comment silently disables the
  acceptance gate.

Reproduction (2026-07-11, this run's handoff copied to scratch): baseline = check_run
PASS-equivalent; after re-adding the template's comment line verbatim → `RUN-013 FAIL`
reappears. The orchestrator had to strip the comment line mid-run to clear verify.

**(b) Confirmation signal-3 cell overreach — 2nd essay for `checker-confirmation-overfire`.**
Signal 3 marks round N a confirmation when any row line matches
`\|\s*N\s*\|` AND contains the word "confirmation" *anywhere in the line* — including
the notes cell. This run, round 3's notes ("publish double-clean needs a round-4
confirmation pass (fresh reviewer...)") mislabeled the REAL 2→3 revision transition.
The applied 2026-07-06 revision-response veto held (downgraded to a RUN-000
both-markers warn; disposition checks still ran), and the orchestrator reworded the
cell to "confirm pass". The veto was designed for exactly this over-fire — but the
detector keeps firing on prose in a free-text column that legitimately *describes* what
a clean round triggers next.

## Proposed change (exact diff)

**File: `_shared/scripts/check_run.py`**

1. Add near the other helpers:

```python
HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.S)

def _score_rows(text):
    """Table-row lines of score-history.md, HTML comments stripped."""
    return [ln for ln in HTML_COMMENT_RE.sub("", text).splitlines()
            if ln.lstrip().startswith("|")]

def _row_cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]
```

2. Replace the cap_hit computation:

```python
-        cap_hit = os.path.exists(score_path) and bool(CAP_HIT_RE.search(_read(score_path)))
+        cap_hit = os.path.exists(score_path) and any(
+            CAP_HIT_RE.search(line) for line in _score_rows(_read(score_path)))
```

(CAP HIT is, per the template's own contract, "recorded as a row" — detection now
requires a table row, and comments can never trip it.)

3. In `_is_confirmation_transition`, scope signal 3 to the `round_type` column
   (column 2 of the row, per the template header
   `| round | round_type | assessment | gates | clean | notes |`):

```python
-    if os.path.exists(score_path):
-        for line in _read(score_path).splitlines():
-            if re.search(r"\|\s*%d\s*\|" % next_round, line) and re.search(
-                    r"confirmation", line, re.I):
-                return True
+    if os.path.exists(score_path):
+        for line in _score_rows(_read(score_path)):
+            cells = _row_cells(line)
+            if len(cells) >= 2 and cells[0] == str(next_round) and re.search(
+                    r"confirmation", cells[1], re.I):
+                return True
     return False
```

4. **File: `handoff-template/03-edit/score-history.md`** — reword the comment so legacy
   checker builds cannot trip either (belt and suspenders):

```markdown
-     CAP HIT is recorded as a row with notes: CAP HIT. -->
+     A promote-at-cap decision gets its own row; its notes column carries the
+     cap marker (two words, CAP + HIT). -->
```

5. **Tests (`test_check_run.py`), shipped with the diff:**
   - a score-history containing ONLY the template comment ⇒ `cap_hit` False (no
     RUN-013/RUN-006; RUN-005 still able to fire);
   - a real `| 4 | revision | ... | CAP HIT |` row ⇒ `cap_hit` True;
   - "confirmation" in a round's **notes** cell ⇒ `_is_confirmation_transition` False;
   - "confirmation" in the **round_type** cell ⇒ True;
   - existing veto tests unchanged (veto stays exactly as applied 2026-07-06).

## Why this lever

gate-promotion (strengthening the checker itself) is the only lever that can fix a
checker false-positive/false-negative; no reference text can stop a regex from matching
a comment. Deference to the 2026-07-06 decision "ship veto alone; do not tighten the
phrase heuristic": that guidance concerned signal 2 (the loose *phrase* heuristic) and
under-fire risk. This diff does not touch signal 1, signal 2, or the veto — it makes
signal 3 read the column it claims to read ("score-history.md's row for round N+1
LABELS it confirmation" — the label lives in `round_type`), and a real confirmation
round always writes `confirmation` in that cell per the template, so no under-fire is
introduced.

## Regression expectation

`test_check_run.py` full suite + `meta/regression.py` green; the new cases above pass;
this run's archived handoff (with its stripped comment AND with the template comment
restored) verifies PASS with only the legitimate 3→4 confirmation RUN-000 warn.
