<!--
  Incident notes — for an ABORTED or protocol-violating run that produced no
  archive (so pipeline-retro's normal Collect step, which reads an archived run,
  cannot see it). Fill one block per incident, then run it through
  meta/normalize_revision_notes.py so it lands in meta/findings-ledger.jsonl as a
  `source: incident` record (origin typically `orchestration-protocol`).

  This closes the meta-loop's blind spot (ML-04): a checkpoint-skipped or
  stage-order violation on a run that never reaches archive can still be recorded
  and counted toward recurrence, instead of going permanently unobserved.

  Copy this file to the run workspace (or meta/), fill it, delete the comments.
-->

# incident-notes

## incident
- **run_id**:            # e.g. intel-us20250266395 (or "unarchived-<date>" if none)
- **profile**:           # publish | draft | wire | understand-only
- **stage_reached**:     # the last stage that ran before the incident
- **class**:             # checkpoint-skipped | stage-order-violation | confirm-file-misuse | other
- **origin**: orchestration-protocol
- **finding_id**:        # e.g. ORCH-01 (stable slug for recurrence)
- **rationale**:         # what protocol was violated, in one or two sentences
- **evidence**:          # paths / timestamps proving it, e.g.
                         #   understand-confirmed.md by:/date: LATER than the earliest
                         #   handoff/01-design/ artifact ⇒ post-hoc (backdated) confirm
- **recommendation**:    # the artifact/rule that should have prevented it

<!--
  Protocol checklist (run when reviewing ANY run, per pipeline-retro SKILL.md):
  compare handoff/00-understand/understand-confirmed.md by:/date: against the
  earliest handoff/01-design/ timestamps. Missing confirm, or a confirm dated
  AFTER design outputs ⇒ log a checkpoint-skipped / post-hoc-confirmation incident
  here — do not treat a backdated confirm as a clean run.
-->
