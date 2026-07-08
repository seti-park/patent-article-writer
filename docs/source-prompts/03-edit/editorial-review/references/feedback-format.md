# Feedback format

Referenced by editorial-review SKILL.md. Defines structured feedback YAML output.

## Schema

```yaml
review_id: <slug>
draft_source: <draft path>
review_timestamp: <ISO-8601>
posture_applied: aggressive | measured | conservative
overall_assessment: pass | revise-recommended | revise-required

findings:
  - pass: <pass-name>
    location: <where in draft>
    severity: critical | high | medium | low
    severity_under_default_posture: <severity if measured posture applied>
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

- `pass` (which pass detected it)
- `location` (which section / paragraph)
- `severity` (critical / high / medium / low)
- `severity_under_default_posture` (posture-lens transparency)
- `finding` (specific observation)
- `recommendation` (what action to take)

## Optional fields

- `quote`: helpful for context, especially redundancy
- `related_fact_entry`: for paraphrase mutation, points to fact-base entry

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

## Empty pass handling

If a pass produces no findings, emit:

```yaml
- pass: <pass-name>
  finding: "no findings"
  scoped_to: "<brief description of what was reviewed>"
```

This proves the pass ran. Empty pass output without explicit `no findings` annotation is invalid.

## Example output

```yaml
review_id: 044-tesla-rcm-vindication-review-1
draft_source: /mnt/user-data/outputs/044-022-essay-draft.md
review_timestamp: 2026-05-10T19:00:00Z
posture_applied: measured
overall_assessment: revise-required

findings:
  - pass: paraphrase-mutation-judgment
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

  - pass: voice-canon-compliance
    location: §2, paragraph 1
    severity: medium
    severity_under_default_posture: medium
    finding: |
      Section anchored on canon entry lead-1A-news-event but opening sentence
      reads as expository explanation rather than news-event framing.
    recommendation: |
      Re-read canon entry. Consider restructuring opening sentence to lead with the event.
    quote: "The patent describes an architecture where..."

  - pass: claim-adequacy
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

  - pass: lead-conclusion-strength
    location: §1 lead
    severity: low
    severity_under_default_posture: low
    finding: |
      Lead opens with event but conclusion does not explicitly return to event framing.
    recommendation: |
      Optional. Closing paragraph could reference the event to close the frame.
```

## Notes

- Severity is the most consequential field. Review carefully.
- Recommendations should be specific and actionable.
- The `quote` field helps caller locate finding quickly.
- Empty passes (no findings) must still appear in output (failure-mode mitigation against editorial inertia).
- `severity_under_default_posture` transparency lets SETI see at a glance which findings shifted due to posture lens.
- Auto-fix is NOT this skill's responsibility. Caller decides what to apply.
