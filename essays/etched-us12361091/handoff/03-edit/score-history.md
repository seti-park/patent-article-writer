# Score history — etched-us12361091 (US 12,361,091 B1 "Tensor parallel group")

Run parameters: --threshold pass --max-iter 4 --mode essay --self-audit on
closing_posture: firm (declared in thesis-spine, carried in draft frontmatter)

| round | type | assessment | gates | verdict | note |
|-------|------|------------|-------|---------|------|
| 1 | review (fresh) | revise-required | 13/13 pass (warn: 1 STRUCT-004, 9 LONGSENT-001) | NOT CLEAN | 17 findings: 3 high (r1-F1 lead scope pass-4; r1-F2, r1-F3 pass-3 grounding -> grounding hard-gate), 7 medium, 7 low. 6G clean both directions. |
| 1-rev | composer revision | - | - | - | 17/17 applied (0 rejected; 1 argued in-finding deviation on r1-F9, later accepted on merits). Grounding fixes via narrow/anchor only; closing byte-identical. draft_version 2. |
| 2 | review (fresh) | pass | 13/13 pass (warn: 1 STRUCT-004, 7 LONGSENT-001) | CLEAN (1st) | All 17 round-1 dispositions verified landed by quotation. New findings: 3 low (r2-F1/F2/F3 anchor precision). No hard-gate findings. |
| 3 | confirmation (fresh, no revision between) | pass | 13/13 pass (warn: same) | CLEAN (2nd) -> ACCEPT (double-clean) | Independent full re-derivation; re-found r2-F2/F3 before opening prior logs. 3 new low (r3-F1/F2/F3). Claims 1-23 mechanically swept; all quoted spans byte-match. |

**Acceptance: double-clean at rounds 2+3 (0 critical / 0 high / 0 medium open).**
Open at acceptance: 6 low, all anchor-precision/attribution polish (r2-F1, r2-F2, r2-F3, r3-F1, r3-F2, r3-F3) — carried into post-acceptance self-audit.

## Post-acceptance self-audit (2 adversarial readers + 1 grounding verifier per round, blind, parallel)

| round | readers (A: investor / B: pro-subject) | grounding table | applied | verdict | note |
|-------|-----------------------------------------|------------------|---------|---------|------|
| SA-1 | A: 1 med + 8 low; B: 2 med + 5 low | 56 rows: 53 SUPPORTED, 2 MISREAD, 1 OVERREACH; 4 med | 19 deltas / 28 finding-ids (3 not-applied, reasons logged) | NOT DRY | Steelman completed (2/2 reader convergence), verdict-list narrowed to claim-locked items, 3 anchor pointers fixed, fact-check-log gap filled. v2 -> v3. Gates 13/13. |
| SA-2 | A: 0 med + 5 low; B: 1 med + 2 low | 92 rows: ALL SUPPORTED; 2 med (anchor extensions) | 6 edits / 7 finding-ids (2 not-applied) | NOT DRY | Design-around inventory completed (switch-instead / superset-add / firmware-decline); negative-limitation pricing added; anchors extended. v3 -> v4. Gates 13/13. §7 byte-identical. |
| SA-3 (cap) | A: 0 med + 2 low; B: 1 med + 6 low | 88 rows: 87 SUPPORTED, 1 partial (sibling evidence scope); 1 med | 6 deltas / 8 finding-ids (6 not-applied, reasons logged) | CAP (3) REACHED with final fixes applied | Claim-18/8/9/11 dependency precision (verified vs claims text by orchestrator post-edit); sibling absence-claim narrowed to this-filing (evidence discipline). v4 -> v5. Gates 13/13. §7 unchanged since v3. |

**Self-audit closure: cap 3 reached, final round's medium fixes applied and mechanically re-verified (claims dependency + verbatim negative limitation + gates 13/13). Residual open items (all low/nit, logged considered-not-applied in revision-notes.md): sa3A-F2, sa3A-F4, sa3B-F3, sa3B-F4, sa3B-F5, sa3B-F7, sa1A-F2/F4/F9, sa2A-F4/F2.**

## Post-cap scoped delta verification (2026-07-03)

The self-audit reached its 3-round cap with round-3 fixes applied; the v4→v5 edits were the
only text never verified by a fresh instance. A scoped grounding-verifier pass (blind, fresh)
verified all ten edited locations against the patent + claims: **10/10 SUPPORTED**, negative-
limitation quote byte-identical across claim 1 / claim 14 / [0386], dependency chain 8→9→10→11
confirmed, LVI/HBM absence claims confirmed by exhaustive 453-paragraph + 23-claim sweep,
gate_quotes/gate_anchors clean. One INFO-level note (ambiguous relative-clause attachment,
accurate under the essay's established framing; no fix recommended).
Report: selfaudit-delta-verification.md. **Verification loop closed on evidence, not on cap.**
