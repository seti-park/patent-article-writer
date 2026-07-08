---
proposal_id: 2026-07-05-prose-polish-stage
created: 2026-07-05T00:00:00Z
status: applied (2026-07-05, owner-directed, regression-gated)
lever: new-stage (skill + agent + orchestrator wiring) + rubric-tuning candidate
goal: "3"
root_cause_stage: edit + architecture
root_cause_artifact: pass-5 reader-perspective (reviews against reader-profile but never holds the pen); no stage owned final plain-language smoothing
recurrence_count: 1
confidence: high
triggering_findings:
  - essay_id: etched-0378175-memory-in-writing-r2
    source: human-revision (owner read of v6, 2026-07-05, class plain-language-gap)
---

## Headline: every pass reviews readability, no stage ever held the pen for it

Owner finding on the accepted v6 essay: sentence structure and word choice sat a notch
above the general reader — engineer-register abstractions ("the compute" as a noun, "an
exchange"), registry jargon ("assignees", "limitation"), stacked figures ("twin sentence
... in one breath", "operational homework"), absolute constructions and agentless
passives. Each survived because it is ACCURATE: pass-5 flags comprehension blockers, but
nothing in the pipeline had the job of actually smoothing the prose for the public once
the text was true, well-structured, and energetic.

## Applied (2026-07-05)

- **New Phase 3.7 stage**: `.claude/skills/prose-polish/SKILL.md` +
  `.claude/agents/prose-polish.md` (`model: inherit`, owner pen rule). Runs after
  self-audit DRY, before check_run/archive; standalone on archives via the
  human-post-accept channel. Surface-only jurisdiction: sentence splitting, plain word
  swaps, grounded glosses; facts/numbers/dates/names/anchors/quotes/blockquotes/verbs of
  certainty/stance/Sources/signature lines untouchable.
- **Safety net, mechanical**: every edit logged as a `## polish` block
  (before/after/why-plainer, template `handoff-template/03-edit/polish-notes.md`); gates
  re-run with zero NEW findings or the edit reverts; changed sentences drift-verified
  old-vs-new by a grounding-verifier-class instrument (pinned cheap); MEANING-CHANGED /
  PROTECTED-TOUCHED verdicts force reverts. Polish never reopens the loop.
- **Wiring**: patent-essay SKILL Phase 3.7 section; CLAUDE.md (architecture box, run
  flow, loop-control bullet, standalone list).
- **First run**: etched-us20240378175-r2 v6 → v7, 17 edits attempted, 15 applied, 2
  REVERTED by the drift check (1 MEANING-CHANGED un-hedge, 1 PROTECTED-TOUCHED term of
  art) — the tripwires fired correctly on round one. Gates 14/14 zero findings,
  signature lines byte-intact, publication re-stripped (2,913 words).
- **Ledger**: class `plain-language-gap` (goal 3) + attribution row + CLASS_MAP entry.

## Watch / follow-ups

- If polish rounds keep finding the same register classes, promote them upstream into
  the composer's voice stack (rubric-tuning for pass-5 or a deliverable-voice-rules
  addition) so the text is born plainer — the stage's edit log is the evidence feed.
- The stage deliberately does NOT touch the KR briefing (owner register) or promo
  (already feed-register, strongest-pen).
