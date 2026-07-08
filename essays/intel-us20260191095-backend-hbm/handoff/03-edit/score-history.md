# Score History — US20260191095A1 (Intel "Ultra HBM" / backend-transistor DRAM)

Essay-id: `intel-us20260191095` · register: discovery · closing_posture: measured · threshold: pass · max-iter: 4

Acceptance = **double-clean** (two consecutive clean rounds from independent reviewers).

| Round | Type | Gates | Assessment | Grounding HG | Goal-2 HG | Verdict/6G HG | Verdict | Note |
|---|---|---|---|---|---|---|---|---|
| 1 | review | 14/14 PASS | revise-recommended | none | none | none | NOT CLEAN (medium 2, low 5) | r1-F1 (§6 verdict: "back-end HBM stack" attributed backend to hybrid-bonded ZAM proxy), r1-F2 (§4: "crystalline-silicon front-end" → needs "DRAM"); routed to composer revision |
| 1→2 | revision | — | — | — | — | — | 7/7 applied, 0 rejected | both mediums + 5 lows applied (narrow/label only; no hedge added); draft_version 1→2; publication re-stripped |
| 2 | review | 14/14 PASS | pass | none | none | none | CLEAN (first) | r1-F1 + r1-F2 landed (verified); new: r2-F1 (low, §5 "cannot" loose). First clean → confirmation trigger, NOT acceptance |
| 3 | review (confirmation, no revision) | 14/14 PASS | pass | none | none | none | CLEAN (independent) | **DOUBLE-CLEAN ACCEPTANCE.** Independent fresh reviewer, cold read before consulting round 2. Carried r2-F1 (low); new r3-F1 (low, "sub-channel" first-use gloss). No medium+ |

## Acceptance

- **Accepted at round 2 draft (draft_version 2)**, confirmed independently at round 3. Promoted to `handoff/03-edit/essay-final.md`.
- Finding-id chain intact (for check_run.py): r1-F1..r1-F7 CLOSED (verified-landed at round 2), r2-F1 re-asserted low at round 3, r3-F1 new low. Nothing dropped.
- **Carried lows → self-audit / prose-polish** (non-gating): r2-F1 (§5 affirmative-core narrow-align to §4/§6 "without a DRAM front-end" form), r3-F1 ("sub-channel" grounded gloss on first use).

## Note — mechanical gate scope fix (round 1, orchestrator)

`gate_figure_use` initially FIGUSE-001-failed figures 2-7 as orphans: the gate scrapes every `FIG. N` token from `figure-selection.md` as "selected," but that file names the non-selected packaging-variant figures (2-7) in token form. The draft correctly uses only the 4 selected FIG-1 panels (locked plan). Fixed at the Phase-1 artifact by rendering non-selected figure mentions in word form ("figures two through six", "figures three and four", "figures five and six"), so the gate's selected-set reads {1} = used. Selection unchanged; no figure forced into the draft. Systemic gate limitation (scope selected-set to the explicit selection table) routed to pipeline-retro (propose-only).
