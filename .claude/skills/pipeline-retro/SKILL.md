---
name: pipeline-retro
description: >
  Meta-loop / self-improvement analyzer for the patent-essay pipeline. Runs after the
  Compose↔Edit inner loop on every essay. Normalizes the run's editorial findings + gate
  results into meta/findings-ledger.jsonl (keyed by north-star goal + owner artifact),
  attributes recurring root causes to the stage that should have prevented them, and writes
  evidence-backed improvement proposals to meta/improvement-proposals/. PROPOSE-ONLY — it
  never edits a skill, reference, gate, or canon; a human applies proposals after a
  regression check. Use after a patent-essay run completes, when an orchestration-protocol
  violation was observed (archived or aborted), or when asked to review pipeline health /
  propose pipeline improvements.
allowed-tools: Read, Write, Edit, Grep, Glob, Bash
context: fork
---

# pipeline-retro

Phase-spanning **meta-loop**. The inner loop (Compose↔Edit) improves one essay; this loop
improves the *system* that makes essays — but only by proposing. It is the second tier of the
two-tier design (see `_shared/references/scoring-rubric.md` and `CLAUDE.md`).

```
inner loop output (edit-log.md + gate-result.json) + post-accept revision-notes.md
    + optional ## incident blocks (any run, incl. aborted)
    → normalize findings (+ revision-delta + incident channel) → meta/findings-ledger.jsonl
    → attribute root cause (meta/attribution-table.md)  → goal + owner stage/artifact
    → score recurrence (count by (pass, root_cause) class across the ledger)
    → on a strong signal: write meta/improvement-proposals/<id>.md (evidence + exact diff)
    → surface top proposal + backlog disposition requests. NEVER edit a skill.
```

## Hard rule: propose-only

This skill **does not modify** any skill body, reference, gate script, `banned_terms.txt`, or
voice canon. Its only writes are: append to `meta/findings-ledger.jsonl`, update
`meta/attribution-table.md` recurrence counts, create/update files under
`meta/improvement-proposals/` (proposal files **and** keep `meta/improvement-proposals/README.md`
status index updated), and never anything else. Every system change is a human decision applied
after the regression check (`meta/regression.py`). This is the primary anti-drift safeguard.

## Process

1. **Collect** — read the run's `handoff/03-edit/edit-log.md` and `runs/<id>/gate-result.json`
   when present. Normalize each finding (and each failing gate `check_id`) into a ledger record
   per `references/ledger-schema.md`. Append to `meta/findings-ledger.jsonl`. Empty-pass "no
   findings" entries are recorded too (they prove coverage and prevent false recurrence gaps).
   Validate the ledger with `python meta/validate_ledger.py` (required keys, enums;
   absent `origin` is read as `inner-loop` — do not rewrite history).

   Also read `handoff/03-edit/revision-notes.md` if present and normalize it with
   `python meta/normalize_revision_notes.py --notes handoff/03-edit/revision-notes.md --essay-id <id> --append meta/findings-ledger.jsonl`.
   This is the **revision-delta channel** (`source: human-revision`, `origin: human-post-accept`
   by default; per-block `origin:` / `finding_id:` override): it captures the post-acceptance
   human edits the edit-log never sees — the editorial blind-spots a human catches AFTER the
   loop returns pass. Keep `origin` distinct in recurrence (a recurring `human-post-accept`
   class → extend coverage; an `inner-loop` class → tune a pass; an `orchestration-protocol`
   class → tighten checkpoint protocol).

   **Incident path (any run, including aborted):** if the run produced no archive or was
   aborted mid-graph, still collect process failures as `## incident` blocks in revision-notes
   (or a free-standing notes file) and normalize the same way. Origin is typically
   `orchestration-protocol` (checkpoint-skipped, stage-order violations, confirm-file misuse).
   Example:

   ```
   ## incident
   class: checkpoint-skipped
   origin: orchestration-protocol
   finding_id: ORCH-01
   rationale: design started without owner confirm; understand-confirmed.md by:/date: later than design artifacts
   ```

   **Protocol checklist (when reviewing any run):** compare
   `handoff/00-understand/understand-confirmed.md` `by:` / `date:` against the earliest
   design-artifact timestamps under `handoff/01-design/`. If confirm is missing, or its
   timestamp is *later* than design outputs, log a `post-hoc-confirmation` /
   `checkpoint-skipped` incident — do not treat a backdated confirm as a clean run.

2. **Attribute root cause** — map each finding class to the *stage + artifact that should have
   prevented it*, using `meta/attribution-table.md`. Tag each record with `goal`
   (1 / 2 / 3 / 4a / 4b from the matrix) and `root_cause_stage` + `root_cause_artifact`.
   Fencing is encoded here: a Phase-3 voice finding routes to `anti-ai-writing.md` /
   `deliverable-voice-rules.md` or a Phase-2 voice-canon admission — never to re-exposing
   `voice-profile.md` in Phase 3. Orchestration-protocol classes route to the orchestrator
   stage (patent-essay SKILL checkpoint protocol + check_run RUN-010), not an editorial pass.

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
   to apply. Strong signals are marked `recommended apply`; weak signals `watch`. When adding
   or changing a proposal's status/recurrence, **keep the status index in
   `meta/improvement-proposals/README.md` updated**.

6. **Hand back to the human** — surface:
   - the single highest-priority **new** proposal (if any), one line; **and**
   - **backlog disposition** (META-BACKLOG-01):
     - pending `recommended-apply` count
     - oldest pending recommended-apply item's age in days
     - every proposal whose `recurrence_count` ≥ 3 (even if not yet recommended-apply)
   - for each backlog line, ask a one-line owner disposition: **apply now** / **defer-with-reason**.

   The human applies after running `meta/regression.py`. Retro never applies.

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

- Automatically, by the `patent-essay` orchestrator, after the inner loop terminates (PASS or
  max-iter) on an archived run.
- **Also** (manual invocation allowed) when an **orchestration-protocol violation** was observed
  — checkpoint skipped, stage-order broken, confirm-file misuse — **regardless of whether an
  archive exists**. Use the incident path in Collect.
- Or when asked to review pipeline health or propose improvements.

## Out of scope

- Editing any skill / reference / gate / canon (propose-only).
- Scoring or revising the current essay (that is the inner loop's job).
- Applying proposals (a human does that after regression check).

## References

- `references/ledger-schema.md` — the `findings-ledger.jsonl` record schema (incl. the `origin`
  enum, absent-origin rule, delta + incident block schema).
- `meta/normalize_revision_notes.py` + `handoff-template/03-edit/revision-notes.md` — the
  revision-delta + incident capture channel.
- `meta/validate_ledger.py` — schema validator for the ledger (run in Collect).
- `references/proposal-format.md` — proposal file format + the 4 improvement levers + the
  canon-admission procedure.
- `meta/attribution-table.md` — finding-class → goal + owner stage/artifact + lever map (the
  retro's brain; human-editable).
- `meta/improvement-proposals/README.md` — maintained status index (update on every proposal write).
