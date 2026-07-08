# Fact-Check Log

> **Edition note:** this run is a pending-application analysis. Every external fact below
> carries an `evidence_level` (per essay-context.md's tiering) IN ADDITION to the standard
> source-authority tier. Live web verification was environment-limited this run (see
> search-log.md) — evidence levels are propagated from `input/essay-context.md` and must
> not be silently upgraded downstream.

## External facts

| Fact ID | Claim | Source URL | Tier | evidence_level | Sources category |
|---|---|---|---|---|---|
| tp-lien-1-2024 | TriplePoint Capital LLC took a 1st security interest in Etched's patent assets, effective 2024-04-19, recorded at USPTO reel/frame 067204/0877, covering the four 2023-era applications (all Etched IP existing then), INCLUDING the two later-rejected compiler applications. | https://assignment.uspto.gov/ (via DOCDB legal events, WIPS export 2026-07-02) | tier-2 | registry-extract | Patents |
| tp-lien-2-2025 | TriplePoint Capital LLC took a 2nd security interest, effective 2025-07-18, recorded at USPTO reel/frame 071792/0869, covering the portfolio INCLUDING the granted trio (US 12,306,903 / US 12,361,091 / US 12,361,262). | https://assignment.uspto.gov/ (user-verified against USPTO assignment records, 2026-07-03) | tier-1 | registry-verified | Patents |
| grant-lien-timing | The trio's second and third grants issued 2025-07-15; the second lien is effective 2025-07-18 — three days later. Dates only; any motive reading is inference and must be labeled as such (correlation-only). | https://assignment.uspto.gov/ + https://patents.google.com/ (dates per essay-context) | tier-1 | registry-verified (dates); inference (any motive reading) | Patents |
| prosecution-record | US 18/195,769 prosecution: non-final actions 2024-11 and 2025-07; final rejection mailed 2025-10-23; RCE docketed 2026-04-24; a third non-final office action issuing as of 2026-05. Pending — examination continuing. | https://patentcenter.uspto.gov/ (via DOCDB, WIPS export 2026-07-02) | tier-2 | registry-extract | Patents |
| examiner-cited-field | The examination record lists 8 unique references, all examiner-cited, in multi-node ML acceleration, hybrid parallelism, and NN accelerator architectures — a crowded field. | https://patents.google.com/patent/US20240378175A1 (USPTO/Google Patents citation record) | tier-2 | registry-extract | Patents |
| etched-thread-2026-07 | Etched's July 2026 stealth-exit thread claims: LVI + CSM technology pillars, "$1B+ contracts", "$800m raised", racks shipping summer 2026. ALL company-claimed — attribute as "the company says". | https://x.com/Etched (July 2026 thread, per essay-context) | tier-1 (as a record of what the company said) | company-claimed (content unverified) | Official statements |
| family-us-only | This application's family is US-only: no PCT, no continuation — in contrast with the granted trio's PCT + continuation treatment (contrast usable as a labeled observation only). | https://patents.google.com/patent/US20240378175A1 (via WIPS export 2026-07-02) | tier-2 | bibliographic | Patents |
| prior-essay-wiring-half | The published companion analysis of granted US 12,361,091 B1 ("the wiring half") found the memory-side half absent from the GRANTED record; this pending application is where that memory half exists on paper. Max ONE clause of continuity; no dependence on having read it. | (internal — prior run of this pipeline; full text of US 12,361,091 B1 held in that run) | tier-2 | internal-prior-run (full-text verified in prior run) | Patents |
| lvi-absence-this-filing | LVI (voltage regulation, VRMs, cold plates) is nowhere in THIS filing — zero voltage/power-delivery content, verified against the full text in this run. Caveat: the 18-month publication window means unseen later filings may exist; absence claims about OTHER filings need their own evidence level. | input/patent.md (full text, this run) | tier-1 | full-text-verified (THIS filing only) | Patents |

## Notes

- **Collateral discipline (hard rule, from essay-context):** both liens are BLANKET over
  the portfolio as it existed at each signing date — they carry ZERO patent-specific
  selectivity. The same pledged pool contains two rejected applications. Never present
  either lien as evidence that THIS application is individually important. Honest frame:
  the entire patent stack, crown jewels included, is pledged as venture-debt collateral —
  IP is the company's bankable asset class, and symmetrically, the encumbered pool is what
  a creditor reaches if things go wrong.
- **Both-or-neither rule:** an essay citing the collateral facts MUST also carry the
  prosecution label sentence (`prosecution-record`); citing one without the other is
  one-sided evidence selection.
- **Label-sentence budget:** `prosecution-record` is consumed by exactly ONE sentence in
  the essay (pending; examination continuing after a final rejection and an RCE, as of the
  2026-05 record). No battle narrative.
- `etched-thread-2026-07` content ($1B+ contracts, $800m, ship dates) is promotional and
  unverified; every use takes "the company says" attribution.
- No tier-5 anchors; no external fact carries quantitative weight beyond registry dates
  and reel/frame numbers.
