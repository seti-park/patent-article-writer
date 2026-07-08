# findings-ledger.jsonl schema

`meta/findings-ledger.jsonl` is append-only. One JSON object per line, one object per
normalized finding (or failing gate `check_id`, or empty-pass marker). This is the substrate
the meta-loop scores recurrence over.

## Record fields

```json
{
  "essay_id": "044-tesla-rcm-vindication",
  "iter": 2,
  "run_timestamp": "2026-06-09T10:00:00Z",
  "source": "editorial | gate | human-revision",
  "origin": "inner-loop | human-post-accept",
  "pass": "pass-3-fact-paraphrase",
  "check_id": null,
  "severity": "high",
  "goal": "1",
  "root_cause_stage": "compose",
  "root_cause_artifact": "essay-en-composer/references/citation-format.md",
  "pattern_tag": "paraphrase-accidental-drift",
  "finding": "Prose uses 'complements'; source verbatim is 'supplements'.",
  "recommendation": "Re-anchor to source verbatim.",
  "status": "open"
}
```

| Field | Meaning |
|-------|---------|
| `essay_id` | the run's essay id |
| `iter` | inner-loop iteration the finding came from |
| `run_timestamp` | ISO-8601 |
| `source` | `editorial` (edit-log), `gate` (gate-result.json), or `human-revision` (revision-notes.md) |
| `origin` | `inner-loop` (default) or `human-post-accept` (revision-delta channel — edits a human made AFTER the loop returned pass) |
| `pass` | editorial pass name, or `null` for gate records |
| `check_id` | gate `check_id` (e.g. `FIGUSE-001`), or `null` for editorial records |
| `severity` | `critical/high/medium/low` (editorial) or `fail/warn` (gate) |
| `goal` | north-star goal threatened: `1 / 2 / 3 / 4a / 4b` (from the matrix) |
| `root_cause_stage` | `design / compose / edit / gate / canon` |
| `root_cause_artifact` | the file/script that should have prevented it (attribution-table) |
| `pattern_tag` | stable slug grouping recurring classes (the recurrence key) |
| `finding` | the observation (verbatim from edit-log) |
| `recommendation` | the editor/gate recommendation |
| `status` | `open / watch / proposed / resolved / escalated` |

## Recurrence key

Recurrence is scored over `(pass_or_check, root_cause_artifact, pattern_tag)`. When the count
reaches `RECUR_THRESHOLD` (default 3) the class is eligible for a `recommended apply` proposal.
Empty-pass "no findings" records carry `severity: none` and never contribute to recurrence —
they exist only to prove a pass ran and to avoid mistaking silence for absence.

## Revision-delta channel (human-post-accept records)

Records with `source: human-revision` / `origin: human-post-accept` come from
`handoff/03-edit/revision-notes.md` via `meta/normalize_revision_notes.py` — the editorial
blind-spots a human catches AFTER the loop says pass. They are tagged distinctly so recurrence
over them is not conflated with loop-visible findings: a recurring `human-post-accept` class
signals **extend coverage** (a new gate/pass), where a recurring `inner-loop` class signals
**tune an existing one**.

## Append discipline

Never rewrite history. Corrections are new records with `status` transitions
(`open → proposed → resolved`). A proposal that is applied flips the triggering records to
`resolved` (a new appended record references them); an ineffective patch flips them to
`escalated`.
