# improvement-proposals/

`pipeline-retro` writes evidence-backed, propose-only improvement proposals here, one file per
proposal (`<date>-<slug>.md`, format in `pipeline-retro/references/proposal-format.md`).

Nothing here is applied automatically. To apply one: review it, run
`python meta/regression.py`, and if green, make the edit and commit citing the triggering
finding ids.

**Keep this index updated** whenever a proposal is created, status changes, or recurrence
is revised (pipeline-retro permitted write; humans who apply proposals update the row too).

Status values: `proposed` | `recommended-apply` | `applied` | `rejected`
(legacy frontmatter `watch` is indexed as `proposed` here; `recommended apply` → `recommended-apply`).

## Status index

| proposal_id | status | recurrence | date |
|---|---|---|---|
| 2026-06-11-claim-scope-lock-map | applied | 2 | 2026-06-11 |
| 2026-06-11-emoji-host-fence-decidable | recommended-apply | 3 | 2026-06-11 |
| 2026-06-11-external-fact-scope-discipline | recommended-apply | 3 | 2026-06-11 |
| 2026-06-11-figure-token-panel-suffix | applied | 2 | 2026-06-11 |
| 2026-06-11-gate-structure-word-wall | recommended-apply | 4 | 2026-06-11 |
| 2026-06-24-conclusion-over-hedge-check | watch | 1 | 2026-06-24 |
| 2026-06-24-figuse-selection-scope | watch | 1 | 2026-06-24 |
| 2026-06-26-figure-selection-cover-and-phase | applied | 1 | 2026-06-26 |
| 2026-06-26-gate-structure-sentence-band-align | applied | 3 | 2026-06-26 |
| 2026-06-26-human-revision-blindspots | applied | 1 | 2026-06-26 |
| 2026-06-26-publication-line-wrap | applied | 1 | 2026-06-26 |
| 2026-06-26-self-audit-origin-and-goal-acceptance | applied | 1 | 2026-06-26 |
| 2026-07-03-check-run-confirmation-round-model | applied | 1 | 2026-07-03 |
| 2026-07-03-external-fact-evidence-scope | watch | 1 | 2026-07-03 |
| 2026-07-03-figure-use-selection-scope | watch | 1 | 2026-07-03 |
| 2026-07-03-figures-prep-ocr-first-hybrid | watch | 1 | 2026-07-03 |
| 2026-07-03-longsent-boundary-merge | applied | 3 | 2026-07-03 |
| 2026-07-03-revision-mode-new-sentence-check | watch | 2 | 2026-07-03 |
| 2026-07-04-pending-application-edition | recommended-apply | 1 | 2026-07-04 |
| 2026-07-05-figure-load-and-caption-density | watch | 1 | 2026-07-05 |
| 2026-07-05-figuse-selection-scope-promote | applied | 5 | 2026-07-05 |
| 2026-07-05-phase1-nonquote-label-grounding | watch | 2 | 2026-07-05 |
| 2026-07-05-procedure-attention-budget | applied | 1 | 2026-07-05 |
| 2026-07-05-promo-bold-selection-kr-long | applied | 1 | 2026-07-05 |
| 2026-07-05-prose-polish-stage | applied | 1 | 2026-07-05 |
| 2026-07-06-affirmative-core-contrastive-precision | watch | 1 | 2026-07-06 |
| 2026-07-06-check-run-confirmation-transition-veto | applied | 1 | 2026-07-06 |
| 2026-07-06-steelman-two-sided | applied | 2 | 2026-07-06 |
| 2026-07-08-promo-explainer-register-message-units | applied | 1 | 2026-07-08 |

**Pending recommended-apply (4):** emoji-host-fence-decidable (rec 3),
external-fact-scope-discipline (rec 3), gate-structure-word-wall (rec 4),
pending-application-edition (rec 1).
Oldest pending recommended-apply date: 2026-06-11.

Run `python3 meta/proposals_index.py --check` to verify this index against each
proposal file's `status:` frontmatter.

**Related meta records:** `meta/exemplar-notes.md` (which archives are patterns vs
historical); `meta/templates/incident-notes.md` (capture an aborted / protocol-
violating run so it reaches the ledger); `python3 meta/validate_ledger.py --strict`
(flag unclassified goal/stage on NEW records).
