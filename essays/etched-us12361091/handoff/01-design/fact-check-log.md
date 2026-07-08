# Fact-Check Log

## External facts

Every non-patent fact the spine relies on. Patent-text facts live as `[xxxx]` anchors in
invention-summary.md and do not appear here. Live web verification was not possible in
this environment (see search-log.md); "Source URL" therefore names the documented source
chain of record for this run.

| Fact ID | Claim | Source URL | Tier | Sources category |
|---|---|---|---|---|
| etched-csm-thread-2026-07 | Etched's stealth-exit X thread (July 2026) claims "Cluster-Scale Memory (CSM)": a "shared low-latency memory pool across the entire scale-up domain", a "proprietary ultra-low-latency, high-bandwidth interconnect", the line "each memory layer inherently adds latency; thus, the best layer is no layer", and an HBM/SRAM hybrid design. | Etched official X thread, 2026-07 (as documented in input/essay-context.md; thread URL not fetchable in this environment) | tier-1 (official company statement) - content is COMPANY-CLAIMED, not independently verified; every use must carry "the company says/claims" attribution | Official statements |
| etched-lvi-biz-thread-2026-07 | Same thread: LVI (Low-Voltage Inference) - math blocks at under half the voltage of typical AI chips; "trillion parameter sparse MoEs at 80%+ peak FLOPs without thermal throttling"; out of stealth after A0 tapeout; first racks built; "$1B+ in customer contracts"; "$800m raised"; first racks ship summer 2026. | Etched official X thread, 2026-07 (via input/essay-context.md) | tier-1 (official company statement) - company-claimed; attribute; the summer-2026 rack date doubles as the closing's binary test | Official statements |
| etched-family-trio-wips | US 12,361,091 B1: filed 2024-10-22 (US 18/922,976), granted 2025-07-15; sole inventor Gavin Uberti (Etched co-founder/CEO); assignee Etched.ai Inc.; 23 claims, 3 independent; 16 figures; expected expiry 2044-10-22; small-entity status on filing. Same-day trio: filed alongside US 12,306,903 B1 ("Performance of tensor operations", granted 2025-05-20) and US 12,361,262 B1 ("Tensor operations in AI models", granted 2025-07-15), same sole inventor; each of the three carries a PCT international filing (WO 2026/090208, 090209, 090210) and a US continuation published in 2026 (US 2026-0111513 / 0111514 / 0111709 A1). Division of labor: 903 = how tensor tiles move between chips (method); 091 = how the chips are wired (structure/topology); 262 = the model-level execution umbrella. | WIPS ON bibliographic export, 2026-07-02 (per input/essay-context.md) | tier-2 (authoritative bibliographic database export) | Patents |
| etched-2023-filings-out-of-scope | Etched's earlier 2023 filings (multi-chip systolic arrays, self-attention circuit, compiler applications) exist but are out of scope for this essay. | WIPS ON bibliographic export, 2026-07-02 (per input/essay-context.md) | tier-2 | Patents |
| us-18month-publication-window | US patent applications can remain unpublished for up to 18 months after filing, so the visible record of a company's filings is a floor, not a census. | General US patent-publication practice (35 U.S.C. §122(b)); carried into this run via input/essay-context.md Scope-boundaries prose ("later filings may still be unpublished — 18-month window") | tier-2 (general patent-law fact) | n/a (general legal fact stated in-body; no Sources entry) |

## Notes

- **Attribution discipline**: `etched-csm-thread-2026-07` and
  `etched-lvi-biz-thread-2026-07` are tier-1 as statements-of-the-company, but their
  CONTENT (latency, FLOPs, contracts, dollars, ship dates) is unverified. The essay may
  state that the company claims X; it may not state X. If the essay quotes thread
  language ("the best layer is no layer", "$1B+ in customer contracts"), the quoted
  wording is as transcribed in input/essay-context.md - flag at compose time that the
  quote chain is thread → essay-context → essay.
- **Cross-check available**: the trio division of labor in `etched-family-trio-wips` is
  corroborated patent-internally - 091's spec enumerates Example families 1 (methods),
  2 (topology), 3 (AI-model computations) at `[0336]`+, and 091's granted claims track
  only Example 2 (see invention-summary.md §Prior-art references + differentiation). The
  essay can make the division-of-labor point on this internal evidence plus the tier-2
  bibliographic facts without needing the siblings' full texts.
- **Bibliographic overlap with the patent itself**: filing date, grant date, inventor,
  assignee, claim/figure counts in `etched-family-trio-wips` match the provided
  patent.md cover data exactly (consistency check done at extraction time). The sibling
  grant dates, PCTs, continuations, expiry, and entity status exist only in the WIPS
  export.
- **No tier-5 anchors.** No quantitative external claim rests below tier-2 except the
  company's own numbers, which are handled by attribution (above).
- **Environment limitation**: no live URL in this table was fetched during this run;
  verification chain is input/essay-context.md as provided (it records its own sources
  and tiers). Recorded per the run instruction "never present an unverified claim as
  verified."
- **Post-audit registry addition**: `us-18month-publication-window` was added during the
  post-acceptance self-audit (finding sa1G-F9). The essay's §6 sentence "US applications
  can stay unpublished for up to 18 months after filing" had been sanctioned only by
  essay-context.md prose; it is now itemized here so every external fact the essay uses
  has a registry row. No essay text change was needed (the fact is accurate).
