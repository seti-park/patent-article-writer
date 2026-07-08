<!--
  TEMPLATE: handoff/01-design/fact-check-log.md
  Produced by: thesis-architect (Phase 1 Design, Step 10 — fact-check log seed)
  Schema source: thesis-architect/SKILL.md Step 10 + post-conditions

  Lists every EXTERNAL (non-patent) fact the spine relies on, each with a stable
  Fact ID, the claim, a source URL, and a source-authority tier. Patent-text facts
  do NOT go here — they live as [xxxx] anchors in invention-summary.md. This log
  MAY be empty if the thesis is entirely patent-anchored (emit the header + a note).

  Phase 2 cites each external fact's Fact ID and surfaces it in the essay's
  # Sources block. Phase 3 Edit Pass 3 cross-checks this log against the essay.

  Tier = 5-tier source-authority hierarchy (Pass 3 external-fact-verification):
    tier-1  primary / official (patent office, company filing, standards body)
    tier-2  authoritative secondary (peer-reviewed paper, official spec sheet)
    tier-3  reputable press / named-source interview
    tier-4  trade press / analyst note
    tier-5  unattributed / forum / single-source rumor (weakest — flag if load-bearing)

  Example content: Tesla RCM / 70ms patent.
-->

# Fact-Check Log

## External facts

<!-- One row per external fact. Fact ID = stable kebab-case slug Phase 2 cites and
     Phase 3 cross-checks. Map each to a # Sources category (Patents / Papers /
     Official statements / News & media / Technical specs) for Phase 2. -->
| Fact ID | Claim | Source URL | Tier | Sources category |
|---|---|---|---|---|
| bosch-ecu-10ms-2020 | Accelerometer-based airbag ECUs respond within approximately 10 milliseconds. | https://www.bosch-mobility.com/en/solutions/passive-safety/airbag-control-unit/ | tier-2 | Technical specs |
| tesla-safety-announcement-2026-03 | Tesla publicly described its predictive restraint system as delivering an "unprecedented" pre-impact response. | https://www.tesla.com/blog/predictive-restraint-2026 | tier-3 | Official statements |
| tesla-rcm-filing-date | The RCM patent (US 2026/0125022 A1) was filed 2024-10-23, roughly 11 months before the public announcement. | https://patents.google.com/patent/US20260125022A1 | tier-1 | Patents |

## Notes

<!-- Optional. Flag any tier-5 anchors carrying quantitative weight (Phase 3 may
     escalate these to high/critical). Note partially-verified statuses. -->
- `tesla-safety-announcement-2026-03` is tier-3 (company blog paraphrase). If the essay quotes it verbatim, capture the exact wording at fact-check time.
- No tier-5 anchors carry quantitative claims in this example.

<!--
  EMPTY-LOG FORM (thesis entirely patent-anchored):

  # Fact-Check Log

  ## External facts

  (none — thesis is entirely anchored in patent text via invention-summary.md
   [xxxx] anchors. Phase 2 # Sources block will list the patent only.)
-->
