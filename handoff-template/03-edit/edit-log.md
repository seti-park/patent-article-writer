<!--
  TEMPLATE: handoff/03-edit/edit-log.md
  Produced by: editorial-review (Phase 3 Edit — 6-pass review)
  Schema source: editorial-review/references/feedback-format.md (exact YAML schema)

  This file is structured YAML feedback (NOT auto-fix). SETI reads the findings and
  applies them to produce essay-final.md. The YAML body lives inside the fenced block
  below so the file is readable as Markdown while the parser consumes the YAML.

  REQUIRED per finding: pass / location / severity / severity_under_default_posture
                        / finding / recommendation
  OPTIONAL per finding: quote / related_fact_entry
  Empty pass MUST still appear, using the "no findings" + scoped_to form.

  pass enum:  voice-canon-compliance | redundancy-compression | claim-adequacy
              | paraphrase-mutation-judgment | reader-perspective
              | lead-conclusion-strength
  severity enum: critical | high | medium | low
  overall_assessment: pass | revise-recommended | revise-required
    (Yes critical OR Yes high => revise-required; only medium => revise-recommended;
     none => pass. Low findings do not affect assessment.)

  Example content: Tesla RCM / 70ms patent (reviewing essay-draft.md).
-->

# Edit Log

```yaml
review_id: 044-tesla-rcm-vindication-review-1
draft_source: handoff/02-compose/essay-draft.md
review_timestamp: 2026-06-09T14:30:00Z
posture_applied: measured
overall_assessment: revise-required

findings:
  # --- a HIGH finding makes overall_assessment revise-required ---
  - pass: paraphrase-mutation-judgment
    location: "§2, sentence quoting [0017]"
    severity: high
    severity_under_default_posture: high
    finding: |
      Draft quotes "the vision sensor functions as a predictive input rather than a
      redundant sensor" [0017]. invention-summary.md Quote anchor q-0017-1 verbatim is
      "the vision sensor functions as a predictive input rather than a redundant
      sensor" — match is exact here, BUT the draft elsewhere paraphrases [0024] as
      "made ~70 milliseconds before"; source verbatim uses "approximately 70
      milliseconds". Accidental drift on the quantitative anchor.
    recommendation: |
      Re-anchor the [0024] quote to source verbatim ("approximately 70 milliseconds").
      Verbatim cites must string-match invention-summary.md exactly.
    quote: "deployment decision is made approximately 70 milliseconds before"
    related_fact_entry: q-0024-1

  - pass: voice-canon-compliance
    location: "§1, paragraph 1"
    severity: medium
    severity_under_default_posture: medium
    finding: |
      Section anchored on opening-corporate-event-announcement-friction, but the
      opening sentence leads with "This spring, Tesla described..." which reads as
      summary rather than event-forward framing.
    recommendation: |
      Consider opening on the event beat itself before characterizing it.

  - pass: claim-adequacy
    location: "§3"
    severity: low
    severity_under_default_posture: low
    finding: |
      The 10ms Bosch baseline lands well, but the ~70ms significance could be stated
      once more in plain terms for readers new to restraint timing.
    recommendation: |
      Optional. One clause restating what 70ms of lead buys (occupant pre-positioning).

  # --- empty passes MUST still appear with the "no findings" form ---
  - pass: redundancy-compression
    finding: "no findings"
    scoped_to: "All sections reviewed for repeated claims and tightening opportunities"

  - pass: reader-perspective
    finding: "no findings"
    scoped_to: "Engagement curve, stake clarity, and mobile line-count checked across all sections"

  - pass: lead-conclusion-strength
    finding: "no findings"
    scoped_to: "Lead hook anchors thesis; closing returns to the filing-vs-announcement frame; # Sources 5-category enum and [xxxx] format verified"
```

<!--
  ALTERNATE: an all-clean review (overall_assessment: pass). Every pass emits the
  "no findings" form; the file would look like:

  review_id: <essay-id>-editorial-review-N
  draft_source: handoff/02-compose/essay-draft.md
  review_timestamp: <ISO-8601>
  posture_applied: measured
  overall_assessment: pass

  findings:
    - pass: voice-canon-compliance
      finding: "no findings"
      scoped_to: "Voice canon adherence + anti-AI banned-pattern grep across all sections"
    - pass: redundancy-compression
      finding: "no findings"
      scoped_to: "Repeated-claim + tightening review across all sections"
    - pass: claim-adequacy
      finding: "no findings"
      scoped_to: "Every [xxxx] cite + external claim verified against sources"
    - pass: paraphrase-mutation-judgment
      finding: "no findings"
      scoped_to: "Verbatim string-match of all [xxxx] quotes against invention-summary.md"
    - pass: reader-perspective
      finding: "no findings"
      scoped_to: "Engagement curve + mobile rendering checked"
    - pass: lead-conclusion-strength
      finding: "no findings"
      scoped_to: "Hook/closure + format compliance verified"
-->
