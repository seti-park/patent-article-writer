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
  "source": "editorial | gate | human-revision | self-audit | incident | retro",
  "origin": "inner-loop | self-audit | human-post-accept | polish | self-post-accept | orchestration-protocol",
  "pass": "pass-3-fact-paraphrase",
  "check_id": null,
  "severity": "high",
  "goal": "1",
  "root_cause_stage": "compose",
  "root_cause_artifact": "essay-en-composer/references/citation-format.md",
  "pattern_tag": "paraphrase-accidental-drift",
  "finding": "Prose uses 'complements'; source verbatim is 'supplements'.",
  "recommendation": "Re-anchor to source verbatim.",
  "status": "open",
  "finding_id": null
}
```

| Field | Meaning |
|-------|---------|
| `essay_id` | the run's essay id |
| `iter` | inner-loop iteration the finding came from |
| `run_timestamp` | ISO-8601 |
| `source` | `editorial` (edit-log), `gate` (gate-result.json), `human-revision` / `self-audit` (revision-notes.md), `incident` (orchestration/process failures), or `retro` (meta-loop / empty-pass markers) |
| `origin` | provenance class (see Origin enum). **Records without `origin` are read as `inner-loop`** — do not rewrite historical entries; the ledger is append-only |
| `pass` | editorial pass name, or `null` for gate / incident records |
| `check_id` | gate `check_id` (e.g. `FIGUSE-001`), or `null` for editorial / incident records |
| `severity` | `critical/high/medium/low` (editorial) or `fail/warn` (gate) or `none` (empty-pass) |
| `goal` | north-star goal threatened: `1 / 2 / 3 / 4a / 4b` (from the matrix); process failures may use `all` |
| `root_cause_stage` | `design / compose / edit / gate / canon / orchestrator / promo` |
| `root_cause_artifact` | the file/script that should have prevented it (attribution-table) |
| `pattern_tag` | stable slug grouping recurring classes (the recurrence key) |
| `finding` | the observation (verbatim from edit-log / notes) |
| `recommendation` | the editor/gate/incident recommendation |
| `status` | `open / watch / proposed / resolved / escalated / none` (`none` = empty-pass marker only) |
| `finding_id` | optional stable id from the source block (e.g. `r1-F2`, `SA-delta-9`); may be absent |

## Origin enum

| Value | Meaning |
|-------|---------|
| `inner-loop` | Compose↔Edit editorial / gate findings (default when `origin` is absent) |
| `self-audit` | autonomous adversarial self-audit channel (source typically `self-audit`) |
| `human-post-accept` | revision-delta: a human edit after the loop returned pass |
| `polish` | prose-polish (윤문) surface pass findings |
| `self-post-accept` | self-audit loop caught it adversarially post-accept (no human in the loop) |
| `orchestration-protocol` | process failures: checkpoint-skipped, stage-order violations, confirm-file misuse — not content failures |

**Absent-origin rule:** readers (and `meta/validate_ledger.py`) treat a missing `origin` field as
`inner-loop`. Never backfill historical ledger lines.

## Recurrence key

Recurrence is scored over `(pass_or_check, root_cause_artifact, pattern_tag)`. When the count
reaches `RECUR_THRESHOLD` (default 3) the class is eligible for a `recommended apply` proposal.
Empty-pass "no findings" records carry `severity: none` and never contribute to recurrence —
they exist only to prove a pass ran and to avoid mistaking silence for absence.

Keep `origin` distinct when interpreting recurrence: a recurring `human-post-accept` class →
extend coverage; an `inner-loop` class → tune a pass; an `orchestration-protocol` class →
tighten checkpoint / stage-order protocol (orchestrator artifact), not an editorial pass.

## Revision-notes block schema (delta + incident)

`handoff/03-edit/revision-notes.md` (and ad-hoc notes on aborted runs) feed the ledger via
`meta/normalize_revision_notes.py`. Per-block keys (each on one line):

| Key | Required | Notes |
|-----|----------|-------|
| `class` | yes | pattern_tag / incident class |
| `round` | no | revision or audit round label |
| `before` | no | prior text (delta); omit or short for incidents |
| `after` | no | new text (delta); omit or short for incidents |
| `rationale` | no | why the edit / what failed |
| `goal` | no | overrides CLASS_MAP goal when set |
| `origin` | no | per-block provenance; overrides CLI `--origin` default for that block |
| `finding_id` | no | stable id preserved onto the ledger record |

Block headings:

- `## delta` — content edit (post-accept human, self-audit, polish, etc.)
- `## incident` — process / orchestration failure on **any** run (completed or aborted)

CLI `--origin` / `--source` remain **default-only fallbacks** when a block omits `origin`.

## Revision-delta channel (human-post-accept / self-post-accept)

Records with `source: human-revision` / `origin: human-post-accept` (or self-audit /
self-post-accept) come from revision-notes via the normalizer — editorial blind-spots caught
AFTER the loop says pass. They are tagged distinctly so recurrence over them is not conflated
with loop-visible findings.

## Incident channel (orchestration-protocol)

`## incident` blocks capture process failures that never produce an archived essay or
edit-log finding: e.g. owner confirm skipped, design started before understand-confirmed,
confirm-file backdated. Source is `incident`; origin is typically `orchestration-protocol`.
Usable on aborted runs — no archive required.

## Append discipline

Never rewrite history. Corrections are new records with `status` transitions
(`open → proposed → resolved`). A proposal that is applied flips the triggering records to
`resolved` (a new appended record references them); an ineffective patch flips them to
`escalated`.
