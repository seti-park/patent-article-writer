---
proposal_id: 2026-07-13-revision-notes-delta-contract
created: 2026-07-13T12:40:00Z
status: watch
lever: reference-edit
goal: "all"
root_cause_stage: architecture
root_cause_artifact: handoff-template/03-edit/revision-notes.md (self-audit ledger block contract undocumented) + _shared/scripts/check_run.py DELTA_RE / meta/normalize_revision_notes.py parse_notes (two consumers, two different implicit formats)
recurrence_count: 2
confidence: high
triggering_findings:
  - essay_id: tesla-wo2026148096-ladder-hoist, source: handoff/03-edit/revision-notes.md (RUN-007 satisfied via retrofit heading "## delta (applied edits, old span → new span)"; parse_notes() on the file returns 0 blocks — reproduced 2026-07-13), pattern_tag: revision-notes-delta-contract-split
  - essay_id: tesla-us20260196678-hemmed-tabless, source: essays/tesla-us20260196678-hemmed-tabless/revision-notes.md (parse_notes() also returns 0 blocks; that run's 13 self-audit ledger records reached the ledger only by manual normalization), pattern_tag: revision-notes-delta-contract-split
---

## Problem

`revision-notes.md` has **two mechanical consumers with two different implicit
contracts, and neither contract is documented where the writer reads**:

1. `check_run.py` RUN-007 requires a literal `## delta` heading
   (`DELTA_RE = ^##\s+delta\b`) or a "self-audit … no … finding" sentence. This
   requirement exists only in check_run.py's source/docstring and a `test_gates.py`
   fixture — `contracts/stages/self_audit.yaml` just lists the file, the composer's
   revision-mode instructions never mention it, and the handoff template documents
   `## delta` blocks only for the *human-post-accept* channel. This run's composer
   ledger shows the accommodation seam: its natural heading ("applied edits, old span
   → new span") survives only as a parenthetical bolted onto the literal token —
   `## delta (applied edits, old span → new span)`.

2. `meta/normalize_revision_notes.py` additionally requires each `## delta` block to
   carry key-per-line fields (`class:` required) and treats any other heading as a
   block terminator. The composer's natural self-audit ledger (`### SA-FIX-N`
   subsections, prose bullets, no `class:` lines) satisfies RUN-007 **and parses to
   zero records**. Reproduced 2026-07-13: `parse_notes()` returns **0 blocks** for
   this run's file AND for `tesla-us20260196678-hemmed-tabless`'s, while all six
   earlier archived essays parse to 8-31 blocks.

Consequence: RUN-007 is green while the meta-loop's `self-post-accept` channel gets
nothing — this run's 11 applied fixes + 24 dispositions are invisible to
`findings-ledger.jsonl` unless a human hand-normalizes them (which is how the prior
run's 13 records got in). That is precisely the "silence mistaken for absence"
failure the ledger schema exists to prevent, on the pipeline's own learning channel.

## Proposed change (exact diff)

**File: `handoff-template/03-edit/revision-notes.md`** — extend the header note to
state the full contract for BOTH channels:

```markdown
+> **Format contract (mechanically consumed — both rules, or the record is lost):**
+> 1. `check_run.py` RUN-007: the file must contain at least one heading that BEGINS
+>    `## delta` (a descriptive suffix is fine: `## delta — self-audit round 2`), or
+>    the literal sentence "self-audit: no unresolved findings".
+> 2. `meta/normalize_revision_notes.py`: each `## delta` / `## incident` heading
+>    opens ONE ledger record; the lines until the next heading must carry
+>    key-per-line fields (`class:` REQUIRED; `round:` / `before:` / `after:` /
+>    `rationale:` / `origin:` / `finding_id:` optional). Any other heading (`###`
+>    included) closes the block. Self-audit apply rounds use one `## delta` block
+>    PER APPLIED FIX (`origin: self-post-accept`), not one umbrella heading over a
+>    prose ledger — prose under the heading without `class:` yields ZERO records.
```

**File: `contracts/stages/self_audit.yaml`** — annotate the output line:

```yaml
-  - handoff/03-edit/revision-notes.md               # deltas origin: self-post-accept
+  - handoff/03-edit/revision-notes.md               # deltas origin: self-post-accept;
+    # format: one `## delta` block per applied fix, key-per-line, `class:` required
+    # (RUN-007 + normalize_revision_notes.py both parse this file — see
+    # handoff-template/03-edit/revision-notes.md header)
```

**Held as secondary (needs its own decision):** a tolerant mode in
`normalize_revision_notes.py` that ingests `### <ID> — <title>` subsections under a
`## delta` heading as records with `class: ?`. Not in the primary diff: it would
paper over missing `class:` attribution (the field recurrence scoring keys on) and
history says prose ledgers vary per run; fixing the contract at the writer is what
makes records attributable.

## Why this lever

Both zero-parse files were written by composers following the visible exemplars, not
the invisible parser — that is a documentation gap, and reference-edit is its lever.
A gate change (tightening RUN-007 to require parseable blocks) would convert silent
data loss into a loud FAIL and may be worth proposing once the documented contract has
been field-tested for a run; proposing both at once would gate on a contract no writer
has yet been shown.

## Regression expectation

`meta/regression.py` green (no gate fixtures touch the template text). Validation for
the applier: `python3 meta/normalize_revision_notes.py --selftest` still passes, the
six pre-multi-vendor archived essays still parse to their current block counts, and
the NEXT run's revision-notes yields >0 parsed blocks with `class:` on every record
(spot-check via parse_notes before archiving).
