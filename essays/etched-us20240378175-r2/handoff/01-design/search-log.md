# Search Log

Environment note: this run was briefed as "outbound web mostly blocked", so context
research was planned registry-first from `input/essay-context.md`'s sourced facts.
In practice WebSearch and one Google Patents fetch succeeded; queries and outcomes below.
Facts that could not be independently re-fetched (reel/frame numbers, office-action dates)
remain at the evidence_level assigned in essay-context and are marked environment-limited.

## Queries

| # | Query | Result URL | Date | Result snippet | Used in | Framing |
|---|---|---|---|---|---|---|
| 1 | Etched Sohu "systolic array" patent US20240378175 | https://patents.google.com/patent/US20240378175A1/en (also: https://wafer.substack.com/p/breaking-down-etcheds-sohu) | 2026-07-04 | Google Patents entry confirms the publication; a third-party Substack teardown ("breaking down Etched's Sohu") reads this application as the architecture used in Sohu — tier-4/5, attribution-only. | fact-check-log: third-party-sohu-linkage (footnote); confirms the filing is publicly read as the Sohu architecture document | footnote |
| 2 | Etched July 2026 thread "$1B" contracts racks ship LVI CSM | https://techcrunch.com/2026/06/30/nvidia-competitor-etched-hits-5b-valuation-1b-in-sales-for-ai-chip/ (also convergedigest.com, wccftech.com, citybiz.co) | 2026-07-04 | Coverage of the stealth-exit: "$1B+ in customer contracts", "$800M raised", "first racks ship this summer", LVI = math at half the voltage, CSM = Cluster Scale Memory (lower-latency shared memory pool). All figures company-claimed. | fact-check-log: thread-claims-2026-07 → Q7 hook + Axis 4 | main-thread |
| 3 | Google TPU systolic array 128x128 MXU matrix unit size | https://cloud.google.com/blog/products/ai-machine-learning/an-in-depth-look-at-googles-first-tensor-processing-unit + https://docs.cloud.google.com/tpu/docs/intro-to-tpu | 2026-07-04 | "On most TPU generations up through v5p, the MXU is a 128x128 systolic array"; Trillium (v6e) moved to 256x256. | fact-check-log: tpu-mxu-128x128 → invention-summary §Prior-art (industry baseline grounding the `[0018]` claim) | paragraph |
| 4 | Etched.ai TriplePoint Capital security interest USPTO patent assignment | (no direct hit; USPTO assignment DB not fetchable this run) | 2026-07-04 | General TriplePoint/USPTO security-interest material only; no Etched-specific public page surfaced. Reel/frame facts stay on essay-context's registry citation. | fact-check-log: lien-1 / lien-2 remain registry-extract / registry-verified per brief; environment-limited | n/a |
| 5 | (fetch) https://patents.google.com/patent/US20240378175A1/en | https://patents.google.com/patent/US20240378175A1/en | 2026-07-04 | Confirms: filed 2023-05-10, published 2024-11-14, Uberti/Zhu, Etched AI Inc, US18/195,769, status pending. Legal events show BOTH TriplePoint security interests (recorded 2024-04-24 and 2025-07-22). Examiner cited 8 prior-art references (assignees incl. Intel, IBM, Rambus, ETRI). Cited-by: Etched US20240419516A1; Google US20250139027A1. | invention-summary Metadata/Timeline; fact-check-log: lien-1, lien-2 (corroboration note), examiner-art-8refs; prosecution-record partially corroborated (status: pending) | main-thread |

## Notes

- Query 5's legal-events corroboration is by RECORDATION date (2024-04-24 / 2025-07-22);
  essay-context's reel/frame facts carry EFFECTIVE dates (2024-04-19 / 2025-07-18). Both are
  kept distinct in fact-check-log; the three-days-after-grant timing detail uses effective
  dates only.
- Office-action detail (final rejection 2025-10-23; RCE 2026-04-24; third non-final as of
  2026-05) was NOT visible on the fetched page — remains evidence_level: registry-extract
  from the 2026-07-02 WIPS/DOCDB export, environment-limited this run.
- CSM expands to "Cluster Scale Memory" in press coverage (query 2); the "each memory layer
  adds latency; the best layer is no layer" phrasing is the brief's characterization of the
  thread's pitch — attribute philosophy language to the company's telling, not to press.
- No query forced a Layer 4 re-extraction; findings landed where planned.
