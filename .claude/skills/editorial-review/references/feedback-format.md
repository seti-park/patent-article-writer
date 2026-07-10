# Feedback format

Referenced by editorial-review SKILL.md. Defines structured feedback YAML output.

## Schema

```yaml
review_id: <slug>
draft_source: <draft path>
review_timestamp: <ISO-8601>
round_type: confirmation | revision   # orchestrator assigns; reviewer copies into header
posture_applied: aggressive | measured | conservative
overall_assessment: pass | revise-recommended | revise-required
# arbitration: optional; orchestrator may append after a reject→re-assert cycle
# arbitration:
#   - finding_id: r1-F1
#     ruling: apply | sustain_rejection | owner_question
#     notes: "..."

findings:
  - finding_id: r1-F1        # r<round>-F<seq>; stable for the whole run, never reused
    pass: <pass-name>
    location: <where in draft>
    severity: critical | high | medium | low
    severity_under_default_posture: <severity if measured posture applied>
    prior_severity: <optional: sev (round N)>  # when re-asserting a dispositioned finding
    finding: "<what was observed>"
    recommendation: "<what to do about it>"
    quote: "<optional: the prose passage in question>"
    related_fact_entry: <optional fact_id>
```

## Pass names

- `voice-canon-compliance`
- `redundancy-compression`
- `claim-adequacy`
- `paraphrase-mutation-judgment`
- `reader-perspective`
- `lead-conclusion-strength`

## Required fields per finding

- `finding_id` (`r<round>-F<seq>` — required on every real finding; "no findings" entries carry none)
- `pass` (which pass detected it)
- `location` (which section / paragraph)
- `severity` (critical / high / medium / low)
- `severity_under_default_posture` (posture-lens transparency)
- `finding` (specific observation)
- `recommendation` (what action to take)

## Optional fields

- `quote`: helpful for context, especially redundancy
- `related_fact_entry`: for paraphrase mutation, points to fact-base entry
- `prior_severity`: when a re-review re-asserts a previously dispositioned finding, carry
  `prior_severity: <sev> (round N)` (e.g. `prior_severity: high (round 1)`)

## Severity criteria

### critical (publication-blocking, conservative posture factual findings only)

- Tier 5 only anchor combined with quantitative claim
- Contradicted external fact under conservative posture
- Substantive paraphrase mutation under conservative posture

### high (publication-blocking)

- Paraphrase mutation = substantive change (not stylistic)
- Voice canon violation that changes essay's apparent style
- Critical reader engagement break (incomprehensibility)
- Lead fails to set thesis or conclusion fails to close arc
- Claim adequacy gap that misleads reader
- Tier 5 only anchor + quantitative claim (any posture)

### medium (quality concern)

- Paraphrase mutation = accidental drift (synonym, minor rewording)
- Voice canon drift in supporting section
- Redundancy that wastes word budget
- Reader perspective rough patch
- Section transition awkward
- External fact under partially-verified status

### low (polish)

- Minor wording opportunities
- Tighter alternatives for stylistic choice
- Caption phrasing refinements

## Overall assessment rules

| Has critical? | Has high? | Has medium? | Assessment |
|---|---|---|---|
| Yes | (any) | (any) | revise-required |
| No | Yes | (any) | revise-required |
| No | No | Yes | revise-recommended |
| No | No | No | pass |

Low findings do not affect assessment.

## Finding lifecycle (loop rounds)

Findings are tracked BY ID across the whole Compose↔Edit loop; nothing closes silently:

1. **Review round N** writes `handoff/03-edit/edit-log.round-N.md` with header field
   `round_type: confirmation | revision` (orchestrator assigns; reviewer records). The
   canonical `edit-log.md` is a copy of the latest round. Every real finding carries
   `finding_id: rN-F<k>`. Confirmation rounds have no `revision-response.round-N.md`
   (if one exists, the round counts as revision).
2. **Revision** (composer, revision mode — see
   `essay-en-composer/references/revision-mode.md`) writes
   `handoff/02-compose/revision-response.round-N.md` with exactly one disposition per
   medium/high/critical finding: `applied` (what changed, where) or `rejected` (why — must argue
   from the spine, the source text, or an explicit rule; "disagree" is not a justification).
   Not written for confirmation rounds.
3. **Review round N+1** starts from round N's log + responses (when revision) and MUST rule
   on each carried id before hunting new findings: verify each `applied` disposition actually
   landed (and did not regress a neighbor — after any structural edit, re-count paragraph
   bands), and either accept each `rejected` disposition or re-assert the finding (same id,
   `prior_severity: <sev> (round N)`). A high or critical finding stays open under its id
   until verified fixed or its rejection is accepted.
4. `_shared/scripts/check_run.py` verifies this chain mechanically (artifact presence,
   disposition coverage, no silently dropped ids) before a run may be archived.

## Empty pass handling

If a pass produces no findings, emit:

```yaml
- pass: <pass-name>
  finding: "no findings"
  scoped_to: "<brief description of what was reviewed>"
```

This proves the pass ran. Empty pass output without explicit `no findings` annotation is invalid.

## Example output

### Round 1 (revision)

```yaml
review_id: 044-tesla-rcm-vindication-review-1
draft_source: /mnt/user-data/outputs/044-022-essay-draft.md
review_timestamp: 2026-05-10T19:00:00Z
round_type: revision
posture_applied: measured
overall_assessment: revise-required

findings:
  - finding_id: r1-F1
    pass: paraphrase-mutation-judgment
    location: §3, sentence containing "complements"
    severity: high
    severity_under_default_posture: high
    finding: |
      deterministic-gate flagged mismatch. Source verbatim is 'supplements'.
      Prose uses 'complements'. Context shows accidental drift, not intentional restatement.
    recommendation: |
      Re-anchor to source verbatim. Verbatim quote must match fact-base entry exactly.
    quote: "Tesla Vision data complements traditional accelerometer-based decisions"
    related_fact_entry: tesla-supplements-2026-05-08

  - finding_id: r1-F2
    pass: voice-canon-compliance
    location: §2, paragraph 1
    severity: medium
    severity_under_default_posture: medium
    finding: |
      Section anchored on canon entry lead-1A-news-event but opening sentence
      reads as expository explanation rather than news-event framing.
    recommendation: |
      Re-read canon entry. Consider restructuring opening sentence to lead with the event.
    quote: "The patent describes an architecture where..."

  - finding_id: r1-F3
    pass: claim-adequacy
    location: §4
    severity: low
    severity_under_default_posture: low
    finding: |
      Quantitative claim (70ms reduction) lacks context for readers unfamiliar
      with airbag deployment baselines.
    recommendation: |
      Reference industry baseline (10ms typical) to make 70ms significance land.

  - pass: redundancy-compression
    finding: "no findings"
    scoped_to: "All sections reviewed for repeated claims and tightening opportunities"

  - pass: reader-perspective
    finding: "no findings"
    scoped_to: "Engagement curve and audience accessibility checked across all sections"

  - finding_id: r1-F4
    pass: lead-conclusion-strength
    location: §1 lead
    severity: low
    severity_under_default_posture: low
    finding: |
      Lead opens with event but conclusion does not explicitly return to event framing.
    recommendation: |
      Optional. Closing paragraph could reference the event to close the frame.
```

### Round 2 (carried ruling + new finding)

Composer rejected r1-F1; reviewer re-asserts. One new finding appears.

```yaml
review_id: 044-tesla-rcm-vindication-review-2
draft_source: handoff/02-compose/essay-draft.md
review_timestamp: 2026-05-10T20:00:00Z
round_type: revision
posture_applied: measured
overall_assessment: revise-required

findings:
  - finding_id: r1-F1
    pass: paraphrase-mutation-judgment
    location: §3, sentence containing "complements"
    severity: high
    severity_under_default_posture: high
    prior_severity: high (round 1)
    finding: |
      Re-assert: disposition was rejected but prose still says "complements"
      where source is "supplements". Rejection not accepted.
    recommendation: |
      Re-anchor to source verbatim.

  - finding_id: r2-F1
    pass: redundancy-compression
    location: §4, paragraphs 2–3
    severity: medium
    severity_under_default_posture: medium
    finding: |
      Core mechanism restated almost verbatim across two consecutive paragraphs.
    recommendation: |
      Keep one full pass; compress the second to a single consequence sentence.
```

## Notes

- Severity is the most consequential field. Review carefully.
- Recommendations should be specific and actionable.
- The `quote` field helps caller locate finding quickly.
- Empty passes (no findings) must still appear in output (failure-mode mitigation against editorial inertia).
- `severity_under_default_posture` transparency lets SETI see at a glance which findings shifted due to posture lens.
- Auto-fix is NOT this skill's responsibility. Caller decides what to apply.
