# Fact-Check Log

Pending-application edition: every fact below carries BOTH the 5-tier source-authority tier
and the edition's `evidence_level` (registry-verified > registry-extract > bibliographic >
company-claimed > third-party-read > internal-prior-analysis). Patent-text facts are NOT
here — they live as `[xxxx]` anchors in invention-summary.md.

## External facts

| Fact ID | Claim | Source URL | Tier | evidence_level | Sources category |
|---|---|---|---|---|---|
| lien-1-triplepoint-2024 | TriplePoint Capital LLC holds a security interest effective 2024-04-19, USPTO reel/frame 067204/0877, covering the four 2023-era Etched applications (all Etched IP existing then), including the two later-rejected compiler applications — this application among the four. | USPTO assignment records via DOCDB legal events (WIPS export 2026-07-02); corroborated this run via Google Patents legal events (security interest recorded 2024-04-24): https://patents.google.com/patent/US20240378175A1/en | tier-1 | registry-extract | Patents |
| lien-2-triplepoint-2025 | A second TriplePoint security interest effective 2025-07-18, reel/frame 071792/0869, covers the portfolio INCLUDING the granted trio (US 12,306,903 / 12,361,091 / 12,361,262). | USPTO assignment records, user-verified 2026-07-03; corroborated this run via Google Patents legal events (recorded 2025-07-22): https://patents.google.com/patent/US20240378175A1/en | tier-1 | registry-verified | Patents |
| grant-lien-timing | The trio's second and third grants issued 2025-07-15; the second lien is effective 2025-07-18, three days later. Dates only; any motive reading must be labeled inference. | USPTO records per essay-context (grant dates bibliographic; lien effective date registry-verified) | tier-1 | registry-verified | Patents |
| prosecution-record | US 18/195,769: non-final actions 2024-11 and 2025-07; final rejection mailed 2025-10-23; RCE docketed 2026-04-24; third non-final action issuing as of 2026-05. Pending. | DOCDB via WIPS export 2026-07-02 (status "pending" corroborated via Google Patents this run; office-action dates environment-limited, not re-fetched) | tier-1 | registry-extract | Patents |
| examiner-art-8refs | The examination record carries 8 unique references, all examiner-cited (multi-node ML acceleration, hybrid parallelism, NN accelerator architectures; assignees include Intel, IBM, Rambus, ETRI) — a crowded field. Optional in essay: one clause. | USPTO/Google Patents citation record: https://patents.google.com/patent/US20240378175A1/en | tier-1 | registry-extract | Patents |
| thread-claims-2026-07 | Etched's July 2026 stealth-exit thread: LVI + CSM claims, "$1B+ contracts", "$800m raised", first racks ship summer 2026. ALL company-claimed; attribute as "the company says". CSM = "Cluster Scale Memory" per press; the "each memory layer adds latency; the best layer is no layer" philosophy line is the thread's pitch (company framing). | https://techcrunch.com/2026/06/30/nvidia-competitor-etched-hits-5b-valuation-1b-in-sales-for-ai-chip/ (+ convergedigest.com, citybiz.co) | tier-3 | company-claimed | News & media |
| family-us-only | This application is US-only: no PCT, no continuation. Contrast with the granted trio's PCT + continuation treatment is allowed as a labeled observation. | WIPS export 2026-07-02 (bibliographic; not independently re-fetched this run) | tier-1 | bibliographic | Patents |
| wiring-half-essay | The published companion analysis of granted US 12,361,091 B1 ("the wiring half") found the memory half absent from the GRANTED record. One clause of continuity allowed; no dependence on having read it. | Prior run's published essay (user-supplied context in essay-context.md) | tier-4 | internal-prior-analysis | News & media |
| lvi-absent-here | LVI-type content (voltage, VRMs, cold plates, power delivery) appears nowhere in THIS filing — full text verified this run (zero voltage/power-delivery content in [0001]-[0066] or claims 1-42). The 18-month-unpublished-window caveat applies to what other, unseen filings may exist. | input/patent.md full text (this run's verification) | tier-1 | full-text-verified | Patents |
| tpu-mxu-128x128 | Google's TPU MXU is a 128×128 systolic array on generations through v5p; Trillium (v6e) moved to 256×256 — the concrete industry instance behind the document's `[0018]` "most chips ... 128×128" characterization. | https://cloud.google.com/blog/products/ai-machine-learning/an-in-depth-look-at-googles-first-tensor-processing-unit + https://docs.cloud.google.com/tpu/docs/intro-to-tpu | tier-1 | press/official-doc | Technical specs |
| third-party-sohu-linkage | Third-party technical readers publicly read this application as the Sohu chip's architecture document ("breaking down Etched's Sohu", wafer.substack.com). Use only as attribution-labeled color, never as confirmation the shipping product practices the claims. | https://wafer.substack.com/p/breaking-down-etcheds-sohu | tier-5 | third-party-read | News & media |

## Notes

- **Collateral discipline (hard, both liens):** the liens are blanket over the portfolio at
  each signing date — zero patent-specific selectivity. Never present a lien as evidence
  that THIS application is individually important (lien-1's pool contains the two
  later-rejected compiler applications). Honest frame: the entire patent stack, crown jewels
  included, is pledged as venture-debt collateral — IP is the company's bankable asset
  class, and symmetrically, the encumbered pool is what a creditor reaches if things go wrong.
- **Both-or-neither (edition rule):** any essay use of the collateral facts REQUIRES the
  prosecution label sentence (pending; examination continuing after a final rejection and an
  RCE, as of the 2026-05 record), and vice versa.
- **Recordation vs effective dates:** Google Patents legal events show recordation
  2024-04-24 / 2025-07-22; the reel/frame effective dates are 2024-04-19 / 2025-07-18. Use
  effective dates in the essay; do not mix.
- No tier-5 fact carries quantitative weight. `third-party-sohu-linkage` is color only.
- `thread-claims-2026-07` figures are unverified company claims even where press repeats
  them; the attribution "the company says" is mandatory on every use.

## Derived comparisons (essay-own arithmetic)

| Comparison ID | Essay rendering | Derivation | Basis |
|---|---|---|---|
| film-per-5ms | "about a feature film's worth of data every five thousandths of a second" (§3) | 1 TB/s × 5 ms = 5 GB; ~5 GB is a standard HD feature-film file size | Patent `[0040]` "more than 1 TB/s" (q-0040-1) converted to a commonplace scale by the essay. Illustrative only, no external quantitative weight; "by the description's own numbers" in the sentence scopes the 1 TB/s figure, and the film conversion is the essay's own arithmetic. Logged post-acceptance, origin: self-audit sa1G-F2. |
