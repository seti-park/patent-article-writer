---
name: pipeline-retro
description: >
  Meta-loop / self-improvement analyzer for the patent-essay pipeline. Runs after the
  Compose↔Edit inner loop on every essay. Normalizes the run's editorial findings + gate
  results into meta/findings-ledger.jsonl (keyed by north-star goal + owner artifact),
  attributes recurring root causes to the stage that should have prevented them, and writes
  evidence-backed improvement proposals to meta/improvement-proposals/. PROPOSE-ONLY — it
  never edits a skill, reference, gate, or canon; a human applies proposals after a
  regression check. Use after a patent-essay run completes, or when asked to review pipeline
  health / propose pipeline improvements.
allowed-tools: Read, Write, Edit, Grep, Glob, Bash
context: fork
---

# pipeline-retro

Phase-spanning **meta-loop**. The inner loop (Compose↔Edit) improves one essay; this loop
improves the *system* that makes essays — but only by proposing. It is the second tier of the
two-tier design (see `_shared/references/scoring-rubric.md` and `CLAUDE.md`).

```
inner loop output (edit-log.md + gate-result.json) + post-accept revision-notes.md
    → normalize findings (+ revision-delta channel) → meta/findings-ledger.jsonl
    → attribute root cause (meta/attribution-table.md)  → goal + owner stage/artifact
    → score recurrence (count by (pass, root_cause) class across the ledger)
    → on a strong signal: write meta/improvement-proposals/<id>.md (evidence + exact diff)
    → surface top proposal to the user (one line). NEVER edit a skill.
```

## Hard rule: propose-only

This skill **does not modify** any skill body, reference, gate script, `banned_terms.txt`, or
voice canon. Its only writes are: append to `meta/findings-ledger.jsonl`, update
`meta/attribution-table.md` recurrence counts, and create files under
`meta/improvement-proposals/`. Every system change is a human decision applied after the
regression check (`meta/regression.py`). This is the primary anti-drift safeguard.

## Process

1. **Collect** — read the run's `handoff/03-edit/edit-log.md` and `runs/<id>/gate-result.json`.
   Normalize each finding (and each failing gate `check_id`) into a ledger record per
   `references/ledger-schema.md`. Append to `meta/findings-ledger.jsonl`. Empty-pass "no
   findings" entries are recorded too (they prove coverage and prevent false recurrence gaps).

   Also read `handoff/03-edit/revision-notes.md` if present and normalize it with
   `python meta/normalize_revision_notes.py --notes handoff/03-edit/revision-notes.md --essay-id <id> --append meta/findings-ledger.jsonl`.
   This is the **revision-delta channel** (`source: human-revision`, `origin: human-post-accept`):
   it captures the post-acceptance human edits the edit-log never sees — the editorial
   blind-spots a human catches AFTER the loop returns pass. Keep `origin` distinct in recurrence
   (a recurring `human-post-accept` class → extend coverage; an `inner-loop` class → tune a pass).

2. **Attribute root cause** — map each finding class to the *stage + artifact that should have
   prevented it*, using `meta/attribution-table.md`. Tag each record with `goal`
   (1 / 2 / 3 / 4a / 4b from the matrix) and `root_cause_stage` + `root_cause_artifact`.
   Fencing is encoded here: a Phase-3 voice finding routes to `anti-ai-writing.md` /
   `deliverable-voice-rules.md` or a Phase-2 voice-canon admission — never to re-exposing
   `voice-profile.md` in Phase 3.

3. **Score recurrence** — count occurrences of each `(pass, root_cause_artifact)` class across
   the whole ledger. Weak signal = 1 (record as `watch`). Strong signal = ≥ `RECUR_THRESHOLD`
   (default 3) → eligible to promote a proposal to `recommended apply`.

4. **Decide the lever** — choose one of the four improvement levers (see
   `references/proposal-format.md`):
   (a) **reference/procedure edit** (a skill body or reference),
   (b) **gate promotion/strengthening** (a script + `banned_terms.txt`),
   (c) **voice-canon admission** (admit a pass-grade essay's exemplar paragraph into
       `voice-canon-lookup/voice-canon/`),
   (d) **rubric/threshold/posture/banned-list tuning**.

5. **Write the proposal** — `meta/improvement-proposals/<date>-<slug>.md` with: triggering
   essays + finding ids, recurrence count, confidence, the chosen lever, and the **exact diff**
   to apply. Strong signals are marked `recommended apply`; weak signals `watch`.

6. **Hand back to the human** — surface only the single highest-priority new proposal (if any)
   in one line. The human applies it after running `meta/regression.py`.

## Anti-drift safeguards

- **Propose-only** (above) — nothing changes without human approval.
- **Regression guard** — before a human applies a proposal, `meta/regression.py` re-runs the
  gate test suite + `meta/fixtures/` and confirms no regression (gates still pass, previously
  recurring defect absent). A proposal that worsens any fixture is rejected.
- **Fencing preserved** — `attribution-table.md` routes findings within the voice fence; the
  retro must never propose re-exposing `voice-profile.md` to Phase 3.
- **Cascade cap** — if the same skill/artifact has been patched more than `CASCADE_CAP`
  (default 2) times and the ledger still shows the defect, mark the class
  `ineffective-patch — escalate` and stop proposing for it (it needs a human design decision).
- **Audit trail** — every applied change is a git commit citing the triggering finding ids,
  plus the existing `> Revision note` convention and voice-canon `added_timestamp`.

## When to invoke

Automatically, by the `patent-essay` orchestrator, after the inner loop terminates (PASS or
max-iter). Or manually when asked to review pipeline health or propose improvements.

## Out of scope

- Editing any skill / reference / gate / canon (propose-only).
- Scoring or revising the current essay (that is the inner loop's job).
- Applying proposals (a human does that after regression check).

## References

- `references/ledger-schema.md` — the `findings-ledger.jsonl` record schema (incl. the `origin` / human-revision fields).
- `meta/normalize_revision_notes.py` + `handoff-template/03-edit/revision-notes.md` — the revision-delta capture channel (post-accept human edits → ledger).
- `references/proposal-format.md` — proposal file format + the 4 improvement levers + the
  canon-admission procedure.
- `meta/attribution-table.md` — finding-class → goal + owner stage/artifact + lever map (the
  retro's brain; human-editable).
