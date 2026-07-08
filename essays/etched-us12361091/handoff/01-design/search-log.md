# Search Log

## Environment constraint (read first)

Outbound web access from this sandbox is blocked for most hosts (patent databases, news
sites, X). **Zero live web-search queries were executed in this run.** Per the run
instructions, context research consumed the pre-sourced, tiered facts documented in
`input/essay-context.md` (sources: Etched official X thread 2026-07; WIPS ON bibliographic
export 2026-07-02). Anything beyond those facts is recorded below as
**environment-limited: not verified** and must not be presented as verified downstream.

## Queries

| # | Query | Result URL | Date | Result snippet | Used in | Framing |
|---|---|---|---|---|---|---|
| — | (no live queries executed - web access blocked; see constraint note above) | — | 2026-07-02 | — | — | — |

## Context facts consumed in lieu of live search (from input/essay-context.md)

Each row is a "finding" in the Step-2 sense, classified for framing-impact at consumption
time (Sub-step 1d).

| # | Finding | Original source (per essay-context.md) | Used in | Framing |
|---|---|---|---|---|
| C1 | Etched exited stealth 2026-07 claiming "Cluster-Scale Memory (CSM)": "shared low-latency memory pool across the entire scale-up domain", "proprietary ultra-low-latency, high-bandwidth interconnect", "each memory layer inherently adds latency; thus, the best layer is no layer", HBM/SRAM hybrid design. Company-claimed, not independently verified. | Etched official X thread, 2026-07 | fact-check-log: `etched-csm-thread-2026-07` → Q7 hook anchor + spine Axis 4 (narrative baseline) | main-thread |
| C2 | Same thread, LVI + business claims: math blocks under half typical voltage; "trillion parameter sparse MoEs at 80%+ peak FLOPs without thermal throttling"; A0 tapeout; first racks built; "$1B+ in customer contracts"; "$800m raised"; first racks ship summer 2026. Company-claimed. | Etched official X thread, 2026-07 | fact-check-log: `etched-lvi-biz-thread-2026-07` → anti-hype guard (LVI not covered by this filing) + closing falsifier (racks ship summer 2026) | paragraph |
| C3 | Patent family: US 12,361,091 B1 filed 2024-10-22, granted 2025-07-15, sole inventor Gavin Uberti (co-founder/CEO), assignee Etched.ai Inc., 23 claims / 3 independent, 16 figures, expected expiry 2044-10-22, small entity. Same-day trio with US 12,306,903 B1 (granted 2025-05-20) and US 12,361,262 B1 (granted 2025-07-15); each with a PCT (WO 2026/090208-090210) and a 2026 US continuation (US 2026-0111513/0111514/0111709 A1). Trio division of labor: 903 = tile movement (method), 091 = wiring (structure), 262 = model-level umbrella. | WIPS ON bibliographic export, 2026-07-02 | fact-check-log: `etched-family-trio-wips` → invention-summary Timeline family note + spine section 2-grant (commitment-signal paragraph) | paragraph |
| C4 | Etched's earlier 2023 filings (multi-chip systolic arrays, self-attention circuit, compiler applications) exist but are OUT of scope for this essay. | WIPS ON bibliographic export, 2026-07-02 | fact-check-log: `etched-2023-filings-out-of-scope` (footnote; only if the essay needs "not their first filing" color) | footnote |

## Environment-limited items (wanted but NOT verified - do not use as verified)

| # | Item the skill would normally web-verify | Status | Consequence for design |
|---|---|---|---|
| L1 | Independent verification of the Etched X thread wording/claims | NOT verified (source is the essay-context brief's transcription of the official thread) | All thread content is used ONLY with "the company says/claims" attribution; tiered as official company statement whose content is company-claimed. |
| L2 | Industry scale-up baseline specs (e.g., switch-fabric scale-up domains such as NVLink/NVSwitch-class systems; link counts, latencies) | NOT verifiable in this environment | Spine Axis 4's engineering baseline is anchored ONLY on the alternatives the patent itself names: any-to-any networking/data switch `[0026]`, `[0032]` and full point-to-point mesh `[0130]`. The essay must not cite named competitor products/specs as verified fact. |
| L3 | Prosecution history of US 18/922,976 (the "two or more" → "four or more" narrowing event) | NOT verifiable (no file-wrapper access) | The narrowing is stated as a document-comparison fact (abstract/summary/[0385] vs granted claims 1/14) - which IS verifiable inside patent.md - without asserting WHY the examiner/applicant narrowed it. |
| L4 | Prior-art landscape for bipartite/two-hop accelerator interconnects | NOT verifiable | The essay must not assert "first ever" / "no one else does this"; novelty framing stays on the patent's own differentiation against switch and full mesh. |

## Notes

- No finding forced a re-extraction of invention-summary Layer 4 (no feedback loop).
- Verbatim-quote extraction from patent.md is mechanical and was gate-verified
  (`gate_quotes.py`: PASS, 44 quotes) - not a web-research item.
