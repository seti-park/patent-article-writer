---
proposal_id: 2026-06-11-claim-scope-lock-map
created: 2026-06-11T16:30:00Z
status: applied  # 2026-07-02 architecture refactor; field-validated on the 2026-06-24 run (class did not recur with the map applied manually)
lever: reference-edit
goal: "1"
root_cause_stage: design
root_cause_artifact: thesis-architect/references/invention-summary-schema.md (claim layer) + thesis-architect/SKILL.md Step 11 (phase2-handoff-notes trap spec)
recurrence_count: 2
confidence: high
triggering_findings:
  - essay_id: 2026-06-10-us12636684b1-deleted-dome, iter: 1, pattern_tag: claim-scope-misattribution
  - essay_id: 2026-06-11-us20260158546a1-both-and-steel, iter: 1, pattern_tag: claim-scope-misattribution
---

## Problem

The single most damaging finding class in the system: in **2 of 2 essays** the inner loop's
only `high` finding was a claim-scope misattribution — a grounding hard-gate breach (goal 1),
invisible to all six deterministic gates, and each time the sole driver of a
`revise-required` verdict and a full Compose↔Edit revision round.

- **Run 1** (`deleted-dome`, iter 1, HIGH): the description's preferred wipe-first order was
  presented as locked by claim 1, which locks only the tail partial order. Root cause: the
  Phase-1 trap list covered adjacent classes but the invention-summary claim layer never
  stated, per claim, which orderings/conditions the claim locks vs leaves open.
- **Run 2** (`both-and-steel`, iter 1, HIGH): claim 5's pinned approximate onset point
  ("martensite formation **begins at about 50° C.**" [8005]) was characterized as a "floor"
  in §3 and §4 — a bound the claim does not state. Root traces **upstream into Phase 1's own
  output**: `phase2-handoff-notes` trap 10 itself called the [8002]–[8005] limitations "such
  floors", so Compose inherited the drift from the artifact that exists to prevent it. The
  round-2 editor explicitly carried the retro note: *"propose fixing the trap wording
  upstream so the next run does not re-inherit the drift."*

Pattern: Phase 1 hands Compose claim material without a per-claim statement of what is
**locked** (required by the claim text), **open** (description preference only), and
**pinned** (approximate point values that are neither floors nor ceilings). Compose then
flattens the distinction, and only the qualitative pass-3 review catches it — at the cost of
a full iteration.

`recurrence_count` is 2 (below RECUR_THRESHOLD=3), so this files at `watch` per the
promotion rules — but both occurrences were HIGH grounding hard-gate breaches, the class is
2/2 cross-essay, and the run-2 editor requested the upstream fix on the record. The exact
diff is included so a human can apply early rather than wait for a third grounding breach.

## Proposed change (exact diff)

**File 1: `.claude/skills/thesis-architect/references/invention-summary-schema.md`** — add a
required "Claim scope map" sub-block to the 청구항 분석 section spec, immediately after the
Layer-4 paragraph ("Layer 4 target: 2-4 angles. ... No anchor = exclude.") and before
"### Reference number table":

```markdown
### Claim scope map (locked / open / pinned)

Required whenever Phase 2 will cite claim anchors ([80NN]). One row per independent claim
plus every dependent claim the spine relies on.

| Claim | Locks (required by claim text) | Leaves open (description preference only) | Pins (approximate point limitations) |
|---|---|---|---|
| 1 | <orderings / conditions / ranges the claim text actually requires> | <what the description prefers but the claim does not require> | <"about X" point values, if any> |
| 5 | ... | ... | e.g. "begins at about 50° C." — a pinned onset point, NOT a floor |

Rules:
- **Locks** lists only what the claim text requires. Never attribute the description's
  preferred embodiment (ordering, protocol, geometry) to a claim — narrate such preferences
  as the description's, on description anchors.
- **Pins** lists approximate point limitations ("about X"). A pinned point is never a floor
  or a ceiling: do not describe it with bound vocabulary the claim does not state.
- `phase2-handoff-notes.md` trap wording must restate this map's distinctions, not collapse
  them (a trap that groups a pinned point under "floors" re-seeds the exact drift it exists
  to prevent — see run 2026-06-11-us20260158546a1, finding F1).
```

**File 2: `.claude/skills/thesis-architect/SKILL.md`** — Step 11, extend item (d):

```diff
-11. **Phase 2 handoff notes** — write `phase2-handoff-notes.md` capturing: (a) Phase 1 의 audience reframe 결정 (if any) (b) 인용 priority 매핑 (어느 Quotable span 이 essay 의 어느 section 에 우선 사용) (c) framing decision 의 trace (rejected candidates 의 핵심 사유) (d) Phase 2 가 우회해야 할 함정 (e) open questions for Phase 2 (SETI 결정 대기 항목).
+11. **Phase 2 handoff notes** — write `phase2-handoff-notes.md` capturing: (a) Phase 1 의 audience reframe 결정 (if any) (b) 인용 priority 매핑 (어느 Quotable span 이 essay 의 어느 section 에 우선 사용) (c) framing decision 의 trace (rejected candidates 의 핵심 사유) (d) Phase 2 가 우회해야 할 함정 — including, for every claim the spine cites, a claim-scope trap restating the invention-summary Claim scope map (locked vs open vs pinned) in do/don't form; trap wording itself must honor the map's vocabulary (never call a pinned point a "floor", never present description-preferred ordering/protocol as claim-locked) (e) open questions for Phase 2 (SETI 결정 대기 항목).
```

## Why this lever

- The defect is born in Phase 1 (Design): both runs' roots were a Phase-1 coverage gap
  (run 1: claim layer silent on locked-vs-open; run 2: the trap list itself used the wrong
  vocabulary). A Compose-side or gate-side fix would treat the symptom: no mechanical gate
  can decide claim semantics, and the composer can only be as precise as the handoff it is
  required to follow (execution-boundary forbids it re-deriving claim scope).
- reference-edit is the cheapest lever that hits the root: the schema row forces the
  distinction to be made once, at extraction time, where the patent text is in hand; the
  Step-11 sentence forces trap wording to inherit (not flatten) it.
- Not gate-promotion: "is this limitation a floor or a pin?" requires reading claim
  language; any regex would false-positive heavily.

## Regression expectation

Documentation-only change (two Markdown skill/reference files; no script, no banned list, no
fixture input). After applying:

- `python .claude/skills/_shared/scripts/test_gates.py` — all tests pass, unchanged.
- `python meta/regression.py` — `clean-baseline` and `figure-orphan` fixtures produce
  identical verdicts (no gate reads these files).
- Observable success criterion for the next run: `handoff/01-design/invention-summary.md`
  contains a Claim scope map; `phase2-handoff-notes.md` claim traps cite it; zero pass-3
  `high` claim-scope findings (third occurrence would instead promote this class to
  `recommended-apply` and bump CASCADE accounting).
