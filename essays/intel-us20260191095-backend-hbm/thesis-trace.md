# Thesis Trace (Phase 2 Compose)

## Selected title-lead register

- **register**: discovery (orchestrator/owner-confirmed)
- **title**: Intel's Filing Moves the DRAM Cell Into the Back-End (52 chars, ≤ 70; no em-dash; "Filing" replaces "Patent" in round 2, r1-F4 — matches the body's pending-application precision)
- **lead**: invention-first discovery. ¶1 delivers the beat (the DRAM cell's transistor is built in
  the back-end, not the crystalline-silicon front-end) with no verdict-insurance fact ahead of it;
  ¶2 prices it (Intel exited memory; three firms make HBM; one published application, not a
  product); ¶3 lands the full two-sided call = the reader_sentence.
- **mode / posture**: strict-execution + conservative (forked non-interactive worker; locked spine
  and heavy accuracy guards → thesis + framing preserved, factual accuracy emphasized).
- **closing_posture**: measured (copied to draft frontmatter; read by `gate_hedge`).

## Signature lines (declared, exact strings — ≤ 3)

Two declared. Protected surface per `_shared/references/reader-energy.md` (echo/count-exempt;
pass-3/4 factual review still applies). Both render em-dash-free per deliverable voice (the
essay-context reader_sentence design target uses an em-dash; the on-page lines do not).

1. `Intel's filing moves the DRAM cell into logic-stackable back-end layers, and if the yield numbers land, who can make HBM stops being a three-company club.`
   - location: §1-lead ¶3 (the reader_sentence rendering; lands the two-sided call by lead's end).
2. `Whether that becomes a fourth path to HBM is now a question of yield, not of architecture.`
   - location: §6-verdict, closing landing (aphoristic; commits the direction, reserves the numbers).

(The one load-bearing inline bold anchor — "This is still a one-capacitor cell. The back-end move
relocates DRAM's hardest part. It does not remove it." — is the essay's single bold thesis anchor
under §2; not declared as a signature line, but it is the STRUCT-002 single-anchor slot.)

## Spine → section trace

Every section maps to the `thesis-spine.md` spine → section table; payload tags carried through.
Exactly one `payload: pricing` section (§5), as the spine requires.

| # | Section header (claim) | payload | Spine element carried | Patent anchors used | External facts used |
|---|---|---|---|---|---|
| 1 | A Memory Architecture From the Company That Left It | frame | Q7 corporate-narrative-friction; discovery beat leads, status is one clause, reader_sentence lands by end | (none — framing) | intel-exited-memory, hbm-supply-concentration |
| 2 | Claim 1 Turns on a Single Word: Backend | tech | Axis 1 claims anchor; what "backend" means (thin-film / BEOL); capacitor relocated not removed | [0018], [0069], [0031], [0027] | (none) |
| 3 | A Tower Built to Match HBM4's Footprint | tech | Axis 3 effect anchor; 8-high stack, TSV gutters, UCIe base die, redundancy, 0.5-5 GB, match-HBM4 goal | [0023], [0031], [0073], [0034], [0020] | (none) |
| 4 | A Back-End Cell Could Loosen the DRAM-Fab Bottleneck | tech | Axis 4 baseline-difference → strategic reframe (labeled essay inference); connect-not-conflate ZAM | (none — inference rides the claim word only) | hbm-supply-concentration, dram-three-player, zam-hb3dm-specs |
| 5 | Read Cold, It Is One Filing That Keeps the Capacitor | pricing | Steelman (claim-scope + capacitor-relocation + causal-gap), pending status, incumbents on 3D DRAM, imec 2T0C contrast, Powerchip-not-Intel | (none — cites §2/§3 anchors by reference) | imec-2t0c-igzo, incumbent-3d-dram, zam-powerchip-fab |
| 6 | The Direction Is Real; the Numbers Are the Test | frame | Measured call: commit to direction; reserve timing/economics to VLSI 2026 + ~2029; one patent-specific anti-hype guard; forward-watching binary test | (none — framing) | zam-hb3dm-vlsi2026, zam-timeline |

Header-only skim skeleton (argument reconstructs): a memory architecture from the company that left
it → claim 1 turns on one word, backend → a tower built to match HBM4's footprint → a back-end cell
could loosen the DRAM-fab bottleneck → read cold, it is one filing that keeps the capacitor → the
direction is real, the numbers are the test.

## Closing directive realization (measured)

- **forward_pointer**: VLSI 2026 (June) density / yield / cost-per-bit of this class of tall, stacked
  HBM challenger (round 2, r1-F1 — "back-end HBM stack" dropped: the ZAM/HB3DM proxy is hybrid-bonded,
  not BEOL); the same technology family aimed at commercialization around 2029 (binary test, not open
  question).
- **wider_framing**: HBM as a candidate output of a logic-plus-packaging flow; "a fourth door" to
  the tightest bottleneck in AI hardware.
- **thesis_recap**: signature line 2.
- **anti_pattern avoided**: no safe-harbor boilerplate ("a patent doesn't guarantee a product," "only
  time will tell," "remains to be seen"). `gate_hedge` clean; the single anti-hype guard is
  patent-specific (1T1C keeps the capacitor, relocated not removed; a back-end capacitor at HBM
  density/yield is unshipped). Limits are referenced ("The bounds set out above still hold"), not
  re-listed.

## Grounding trace — beats and their support

Every patent-text beat traces to an invention-summary Quotable span / Quote-anchor row (verified by
`gate_anchors` + `gate_quotes`, both PASS). No thesis beat lacked a required patent span.

- **Strategic reframe (§4) — external by design, NOT a grounding gap.** The "back-end cell → no
  dedicated DRAM fab → who can make HBM" synthesis is the essay's reasoning riding fact-check-log
  external facts on the single claim word "backend." It is explicitly labeled in-text ("the leap is
  mine, not the document's"; "Claim 1 says backend. It never says foundry, never says logic fab,
  never says without a DRAM fab"). The patent is never credited with it. This is the spine's
  intended construction, not a missing span.
- **Patent-side vs news-side numbers kept separate**: "0.5-5 GB per die" and the ~1.5 GB die are the
  patent ([0034], [0027]); HBM/DRAM shares, ZAM specs, incumbent roadmaps, imec 2T0C, and the ~2029
  horizon are external (# Sources), never anchored. The patent's own no-number status is stated
  ("the filing reports no bandwidth, no cost, no yield").
- **Channel material** left unnamed for this patent (no oxide/IGZO imported as Intel's); imec's
  capacitor-less cell is the only external contrast.

## Self-check (gates)

13 / 14 gates PASS with zero warnings. The only FAIL is `figure_use` FIGUSE-001 for figures 2-7, a
pre-existing `figure-selection.md` artifact (all selected figures are FIG. 1 panels; the gate reads
the file's non-selection prose as selections). Detail + recommended Phase-1 fix in
`figures-rationale.md`. Not introduced by composition and not fixable by composition without
distorting the locked figure plan.
