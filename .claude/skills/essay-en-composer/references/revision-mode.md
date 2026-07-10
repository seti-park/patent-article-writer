# Revision mode (Compose↔Edit loop, round N)

How the composer revises `handoff/02-compose/` when the orchestrator feeds back a failing
round: the round-N edit-log findings + failing gate `check_id`s. Before this reference
existed, "revision mode" was undefined behavior — the loop's weakest link: nothing forced a
finding-by-finding response, so a lazy revision could change little and the next (anchored)
review would wave it through.

## Inputs

- `handoff/03-edit/edit-log.round-N.md` — the findings, each with a `finding_id`.
- The round-N gate result (failing/warning `check_id`s with locations).
- The unchanged Phase-1 handoff (`thesis-spine.md`, `invention-summary.md`, ...). Revision
  never re-derives claim scope or introduces facts beyond the Phase-1 sources
  (execution-boundary rules still bind).

## Protocol

1. **Disposition every finding first, then edit.** For each medium/high/critical finding and
   each failing gate check, decide and record BEFORE touching prose:
   - `applied` — you will make the change; note what and where.
   - `rejected` — you will not; the justification must argue from the spine, the source text,
     or an explicit rule (a reference file, the claim-scope map, the hedge budget).
     "Stylistic preference" is not a justification for rejecting a medium+ finding.
   Low findings may be batched ("applied: all low polish items" / itemized rejections).
2. **Fix at the source.** If a finding traces upstream (a mislabeled anchor, a trap worded
   wrong), flag it for the orchestrator to correct the Phase-1 artifact too — otherwise the
   next recompose reintroduces it.
3. **Grounding fix priority** (jurisdiction fence, mirrors editorial-review): for a pass-3/4
   finding — find a stronger anchor → narrow the claim to the anchor → reframe as
   explicitly-labeled analysis → cut the claim. Adding a hedge or disclaimer to the verdict is
   NOT a grounding fix (6G / `gate_hedge` will flag it).

   **Surface fence** (mirrors editorial-review's surface jurisdiction): a finding that asks to
   reword, compress, or de-duplicate a signature line declared in `thesis-trace.md`, or to sand
   title/header/lead-¶1 style on count grounds, is correctly dispositioned `rejected` citing
   `_shared/references/reader-energy.md` — UNLESS the finding is factual (grounding, scope,
   causality), which is applied like any other. Never fix a defensive-open (6H) finding by
   deleting the insurance facts; reverse their order (discovery first, priced second).
4. **Apply the edits** to `handoff/02-compose/essay-draft.md` in place, re-emit
   `publication.md` via the strip pipeline, and update `figures-rationale.md` /
   `thesis-trace.md` if placement or the spine→section trace moved.
5. **Recount after structural edits.** Any split/merge/move can push a NEIGHBORING paragraph
   across the 3-7 sentence band or orphan a figure reference — re-count every paragraph and
   re-check every figure token after any structural edit (ledger: the "fix introduced a new
   8-sentence paragraph" regression class).
6. **Write the response file**: `handoff/02-compose/revision-response.round-N.md` per
   `handoff-template/02-compose/revision-response.md` — one disposition block per finding_id,
   plus a one-line summary of anything volunteered beyond the findings (so the next reviewer
   knows what else moved). Bump `draft_version` in the frontmatter.

## Exit

Revision round N is complete when: every medium+ finding_id has a disposition, the draft +
publication.md are re-emitted, and the response file exists. The orchestrator then re-runs the
gates and spawns a FRESH reviewer for round N+1 — the reviewer will verify each `applied`
disposition actually landed, so cosmetic compliance is wasted effort: the cheapest path
through the loop is a real fix.

## CAP HIT (orchestrator; not composer)

If revision rounds hit `max_revision` without acceptance, the orchestrator runs the
`cap_hit` owner checkpoint (patent-essay SKILL.md). What ships on cap: the **last draft**
only (not a preferred earlier round). A score-history row records `notes: CAP HIT`. Hard
stop unless `--yes` (then ship last draft and continue downstream stages on publish).
