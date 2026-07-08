# etched-us20240378175 — "Etched Filed the Memory Half of Its Story in 2023."

> **SUPERSEDED (2026-07-04)** by `essays/etched-us20240378175-r2/` (the reader-first
> re-run of the same patent; see `docs/architecture/comparison-v7-vs-r2.md`). Kept as
> the pre-overhaul baseline for the architecture comparison. Do not publish or cite as
> current; do not use as a grounding source for new runs.

English long-form analysis (X Articles) of **US 2024/0378175 A1 — "Multi-chip systolic
arrays"** (Etched.ai; application 18/195,769, filed 2023-05-10 — the company's earliest
filing; inventors: co-founders Gavin Uberti and Christopher Zhu; **PENDING, not granted**),
written for a curious retail investor following Etched's July 2026 stealth-exit thread.
**First pending-application ("prosecution-watch") edition of this pipeline.**

- **Thesis (spine C1):** the company's origin filing already claims the memory half of its
  Cluster-Scale Memory philosophy — memory channels hardwired to systolic-array columns
  "without any switching element" (claim 39) — three years before the thread said "the best
  layer is no layer"; but it is a roadmap the company keeps funding, not yet a fence: no
  claim has been allowed, and the whole portfolio (crown jewels included) is pledged as
  venture-debt collateral.
- **Deliverable:** `essay-final.md` (draft_version 7, incl. human-directed confidence pass) · publication strip at
  `handoff/02-compose/publication.md` (2,802 words) · cover figure FIG. 5.
- **Figures placed:** FIG. 5 (header/cover), FIG. 1 + FIG. 2 (§3), FIG. 6 + FIG. 7 (§5);
  FIG. 3/4 intentionally dropped (scaling point carried in prose).

## Edition rules this run pioneered

- Claim scope map with **sought-\*** classes only (no "locked" class exists for an
  application); application-era language throughout; zero enforceability verbs.
- Prosecution status: exactly ONE label sentence (pending; final rejection 2025-10; RCE
  2026-04) — no battle narrative, per the user's editorial decision.
- Venture-debt collateral beat: one paragraph, PORTFOLIO scope only (blanket liens
  2024-04-19 reel 067204/0877 and 2025-07-18 reel 071792/0869; the trio granted 2025-07-15,
  lien three days later — dated fact, motive labeled inference). Never presented as
  patent-specific importance; "both-or-neither" rule (lien fact and rejection fact travel
  together).

## Run shape (see score-history.md)

- Inner loop: round 1 revise-recommended (7 medium) → revision → round 2 revise-recommended
  (1 medium: FIG. 7 caption vs the drawing) → revision → round 3 pass → round 4
  confirmation pass → **double-clean accept**. Gates 13/13 every round.
- Self-audit: 3 rounds (blind readers + grounding verifier). 24 deltas; both readers dry
  for the final two rounds; the last two grounding items were fixed via **fix-at-source**
  (Phase 1 added q-0056-1 and q-0055-1 spans so the composer could anchor the FIG. 7
  caption without breaching the patent fence). Cap reached with the final mechanical fix
  orchestrator-verified.
- check_run.py: **PASS** (`runs/etched-us20240378175/check-run-verdict.txt`).
- §7 call sentence and landing byte-stable since acceptance.

## Provenance

- `input/patent.md` from the USPTO publication full text (user-provided), official
  paragraph numbering [0001]–[0066], claims 1–42; bold-numeral normalization applied;
  cross-checked against Google Patents.
- Figure sheets (7) user-supplied; Phase 0 cleaned (header crops ×7, rotations ×3,
  vision-verified). Known artifact: figures-manifest.md swapped FIG. 6's 605/610 labels —
  caught and overridden by four independent reviewers; retro material.
- Prosecution and lien facts from the WIPS/DOCDB export (2026-07-02); the 2025-07 lien's
  coverage of the granted trio user-verified against USPTO assignment records (2026-07-03).
- Companion essay: `essays/etched-us12361091/` (the granted "wiring half"); this essay is
  its standalone follow-up.
