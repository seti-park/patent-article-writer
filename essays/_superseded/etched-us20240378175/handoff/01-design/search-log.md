# Search Log

> **Environment limitation (this run):** outbound web access is blocked for most hosts in
> this execution environment, so NO live web searches were executed. All external facts
> were propagated from `input/essay-context.md`, which carries pre-sourced findings with
> per-fact evidence tiers (WIPS/DOCDB registry exports of 2026-07-02, a user verification
> against USPTO assignment records of 2026-07-03, and company-claimed thread content).
> The table below logs each finding's provenance in place of a live query row, with the
> canonical source that a live re-verification would target. Live verification was
> environment-limited, not skipped by choice — Phase 3's external-fact pass should treat
> these as pre-verified to the evidence level recorded in fact-check-log.md, not higher.

## Queries

| # | Query (intended / provenance) | Result URL | Date | Result snippet | Used in | Framing |
|---|---|---|---|---|---|---|
| 1 | (not run — environment-limited) USPTO assignment records, Etched.ai security interests | https://assignment.uspto.gov/ (canonical); provenance: DOCDB legal events via WIPS export 2026-07-02 | 2026-07-04 | 1st security interest, TriplePoint Capital LLC, effective 2024-04-19, reel/frame 067204/0877, blanket over the four 2023-era applications (incl. two later-rejected compiler applications) | fact-check-log: `tp-lien-1-2024` → spine Axis 4 / asset-status beat | paragraph |
| 2 | (not run — environment-limited) USPTO assignment records, 2nd TriplePoint lien | https://assignment.uspto.gov/ (canonical); provenance: user-verified against USPTO assignment records 2026-07-03 | 2026-07-04 | 2nd security interest, TriplePoint Capital LLC, effective 2025-07-18, reel/frame 071792/0869, portfolio incl. granted trio US 12,306,903 / 12,361,091 / 12,361,262 | fact-check-log: `tp-lien-2-2025` → asset-status beat | paragraph |
| 3 | (not run — environment-limited) US 18/195,769 prosecution history | https://patentcenter.uspto.gov/ (canonical); provenance: DOCDB via WIPS export 2026-07-02 | 2026-07-04 | non-final actions 2024-11 and 2025-07; final rejection mailed 2025-10-23; RCE docketed 2026-04-24; third non-final action issuing as of 2026-05 | fact-check-log: `prosecution-record` → Q7 friction + label sentence | main-thread |
| 4 | (not run — environment-limited) US20240378175A1 examiner citations | https://patents.google.com/patent/US20240378175A1 (canonical); provenance: USPTO/Google Patents citation record per essay-context | 2026-07-04 | 8 unique references, all examiner-cited (multi-node ML acceleration, hybrid parallelism, NN accelerator architectures) | fact-check-log: `examiner-cited-field` → adversarial defense steelman + claim-scope-map risk notes | main-thread |
| 5 | (not run — environment-limited) Etched July 2026 announcement thread | https://x.com/Etched (canonical); provenance: essay-context "News moment" | 2026-07-04 | company-claimed: LVI + CSM pillars, "$1B+ contracts", "$800m raised", racks ship summer 2026 | fact-check-log: `etched-thread-2026-07` → Q7 hook (narrative side of the friction) | main-thread |
| 6 | (not run — environment-limited) family data US 18/195,769 | https://patents.google.com/patent/US20240378175A1 (canonical); provenance: WIPS export 2026-07-02 | 2026-07-04 | US-only, no PCT, no continuation — contrasts with the granted trio's PCT + continuation treatment | fact-check-log: `family-us-only` → asset-status beat (labeled observation) | paragraph |
| 7 | (not run — prior-run artifact) published analysis of granted US 12,361,091 B1 ("the wiring half") | (internal prior run; essay-context "News moment" + spine material) | 2026-07-04 | prior essay's verdict: the memory half was absent from the GRANTED record — this pending application is where the memory half lives on paper | fact-check-log: `prior-essay-wiring-half` → Axis 4 baseline-difference | main-thread |
| 8 | (not run — full-text check done in-run) voltage/power-delivery content in THIS filing | input/patent.md (full text, this run) | 2026-07-04 | zero voltage / power-delivery (LVI) content anywhere in the specification or claims — verified against the full text in this run | fact-check-log: `lvi-absence-this-filing` → boundary guard | footnote |

## Notes

- Framing-impact classification done at propagation time (Step 2 discipline): rows 3, 4,
  5, 7 are main-thread (they shape the Q7 friction, the steelman, and Axis 4); rows 1, 2,
  6 are paragraph-level (the asset-status beat); row 8 is a footnote-level boundary guard.
- No finding forced a re-extraction of invention-summary Layer 4 angles.
- Layer-confusion watch (priority input for adversarial defense): the sharpest confusion
  risk is between what a PENDING application proves (a dated, authored disclosure) and
  what a grant would prove (a property right). This is elevated into the Category-1
  steelman in thesis-spine.md rather than left as a footnote.
- If web access is available in a later phase, priority re-verification order: row 2
  (registry-verified lien; cite reel/frame 071792/0869), row 3 (prosecution record), row
  4 (examiner citation clusters).
