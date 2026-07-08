<!--
  TEMPLATE: handoff/01-design/search-log.md
  Produced by: thesis-architect (Phase 1 Design, Step 2 — context research)
  Schema source: thesis-architect/SKILL.md Step 2 + post-conditions
                 ("every web-search query logged with URL + date + result snippet
                  + used-in column")

  EVERY web-search query run during context research gets a row. The "Used in"
  column traces where the finding landed: a Fact ID in fact-check-log.md, an axis
  in thesis-spine.md, a candidate in thesis-candidates.md, or "discarded".

  Each significant finding is also classified for framing-impact at discovery time
  (main thread / paragraph / footnote) per the SETI quick-decision in Step 2.

  Example content: Tesla RCM / 70ms patent.
-->

# Search Log

## Queries

<!-- One row per query. Snippet = the load-bearing result fragment (verbatim or
     tight paraphrase). Used in = downstream destination (Fact ID / axis / candidate
     / discarded). Framing = main-thread | paragraph | footnote | n/a. -->
| # | Query | Result URL | Date | Result snippet | Used in | Framing |
|---|---|---|---|---|---|---|
| 1 | bosch airbag ECU deployment latency milliseconds | https://www.bosch-mobility.com/en/solutions/passive-safety/airbag-control-unit/ | 2026-06-02 | "Deployment decision is reached within ~10 ms of crash detection." | fact-check-log: bosch-ecu-10ms-2020 → spine Axis 4 | main-thread |
| 2 | tesla predictive restraint announcement 2026 | https://www.tesla.com/blog/predictive-restraint-2026 | 2026-06-02 | "...an unprecedented pre-impact response from Tesla Vision." | fact-check-log: tesla-safety-announcement-2026-03 → Q7 hook | main-thread |
| 3 | US20260125022A1 filing date google patents | https://patents.google.com/patent/US20260125022A1 | 2026-06-02 | "Filed 2024-10-23; published 2026-04-23." | fact-check-log: tesla-rcm-filing-date → timeline + Q7 friction | main-thread |
| 4 | vision-based pre-crash sensing prior art automotive | https://patents.google.com/patent/US20220123456A1 | 2026-06-02 | "Optical sensing used as secondary post-impact confirmation." | invention-summary §Prior-art differentiation | paragraph |
| 5 | accelerometer vs optical sensor crash detection speed | https://example.org/automotive-safety-forum-thread | 2026-06-02 | (forum opinion, single source — not authoritative) | discarded (tier-5, no load-bearing claim) | n/a |

## Notes

<!-- Optional. Record dead-end queries kept for audit, and any finding that forced
     a re-extraction of invention-summary (feedback-loop discipline). -->
- Query 5 retained for audit only; discarded as tier-5 with no quantitative anchor.
- No query forced a Layer 4 re-extraction in this example run.
