# intel-us20250266395 — "Intel Filed the Packaging Flow That Comes After EMIB-T"

> **2026-07-06 human post-accept revision (v5 → v6):** owner read found §5 "One Filing
> Among Hundreds, Except for One Claim" overly defensive / safe-harbor and low on net-new
> information. Compressed in place: cut the prosecution/spend passage (18-months framing,
> JP/KR/CN/DE counterpart list, fee-money inference → one clause "a pending application
> with no granted claim yet") and the caveat restatements already made in §2/§4; kept the
> steelman at full strength (claim-17-off-claim-16 + no-single-claim), the locked
> order-of-operations payoff, and Mahajan/mainline provenance. §5: 6 → 4 paragraphs.
> Gates 14/14, drift clean, signature lines + EMIB fence intact; check_run PASS. Deltas:
> `revision-notes.md` (origin human-post-accept, classes `procedure-overweight` +
> `redundant-caveat-restatement`).

Run of US 2025/0266395 A1 (Intel Corporation, "Multi-Die Bridge Assemblies and Methods
for Three-Dimensional Packaging"; filed 2024-02-20, published 2025-08-21 — a **pending
application**, not a granted patent). Edition framed by the reader's live question: with
Intel's EMIB-T packaging in the news, is this filing that story, or something after it?
Discovery register, selected from Phase 1's five title-lead candidates.

- **reader_sentence delivered:** "Everyone's watching Intel ship EMIB-T, but Intel already
  filed the next move: bond the bridge to the chips first and test the whole thing before a
  substrate ever gets involved." Both self-audit cold readers reproduced it unaided (round 2
  read to the end; round 1's early bail was fixed by the lead narrowing).
- **Thesis (one line):** while the market watches EMIB-T productize the powered bridge, this
  filing stakes out the assembly flow *after* it — bond the bridge to the dies first, test
  the whole multi-die cluster before any substrate is committed, then seat the bridge in a
  cavity and power it from the floor through TSVs/TGVs. The claim that carries it is an
  **order of operations**, not a material or a pitch number.
- **Deliverable:** `essay-final.md` (draft_version 6: double-clean accepted → self-audit-dry
  → Phase 3.7 윤문 polish (3 surface-only §4 edits, `handoff/03-edit/polish-notes.md`) → v6
  human-post-accept §5 compression, see banner) · publication strip
  `publication-package/publication.md` · 3 declared signature lines.
- **Owner artifacts:** `owner-briefing.md` (한국어 발행자 브리핑, gate_quotes PASS against the
  archived `patent.md` snapshot) · `promo/promo-pack.md` (promo_version 1: KR 장문 777자 +
  EN thread 5 tweets behind one Verification Status header; bold-selection = the timing
  claim "Intel filed the flow that comes after EMIB-T"; every factual phrase traced verbatim
  to essay/briefing, IP-signal altitude held, no stock or schedule claim) · `patent.md`
  (the run's exact input snapshot; all `[dddd]` anchors resolve offline).
- **Figures placed:** FIG. 11 (cover/header, the method flowchart — the one figure of the
  claimed core step), FIG. 1 (§2), FIG. 5A+5B (§3), FIG. 7 + FIG. 8 (§4). Not rendered
  (prose pointers instead): FIG. 2A/2B, 3, 4, 6A/6B, 9, 10, 12–15. Cover crop guidance in
  `publication-package/posting-checklist.md` (portrait flowchart → crop the bond→test→attach
  band at publish; auto-crop intentionally not shipped).

## Run shape (score-history.md)

| Round | Type | Assessment | Gates | Note |
|---|---|---|---|---|
| 1 | review | revise-required | 14/14 | 2 high (universal-negative, FIG. 8 numeral 882), 6 medium, 10 low |
| — | revision-1 | — | 14/14 | 8/8 medium+ applied; +upstream "face-down" fix in invention-summary |
| 2 | review | revise-recommended | 14/14 | 1 medium (mobile-line splits), 3 low; 18/18 prior dispositions verified |
| — | revision-2 | — | 14/14 | 4/4 applied; +upstream FIG. 5A caption fix in figure-rationale |
| 3 | review | **pass** | 14/14 | first CLEAN; zero findings |
| 4 | confirmation | **pass** | 14/14 | second CLEAN, fresh independent reviewer, unchanged v3 → **double-clean** |

- **Self-audit:** 2× adversarial-reader + grounding-verifier + cold reader (round 1), then
  skeptic + cold reader confirmation (round 2, dry). Applied SKEP-01 (lead survey-superlative
  narrowed), SKEP-02/03 (claim-17 sourcing, roadmap phrasing). **Rejected** the impatient
  reader's "add a stock-impact clause" — it would breach the filed≠roadmap discipline; the
  IP-signal altitude is deliberate. Grounding: 28/28 SUPPORTED, EMIB fence intact (no
  `[dddd]` anchor on any EMIB/EMIB-T sentence). Normalized to `meta/findings-ledger.jsonl`
  (origin self-post-accept).
- **check_run.py:** PASS (double-clean acceptance; every medium+ finding dispositioned;
  self-audit evidence present; owner-briefing present).

## Grounding discipline notes (this edition)

- The patent **never uses the word "EMIB"/"EMIB-T"**; every link to it is the essay's
  synthesis of a filing date, an unveiling date, and a shared power-delivery idea, and is
  labeled as such. EMIB-T / HBM4 / rollout facts are external, sourced in
  `handoff/01-design/fact-check-log.md`, and carry no patent anchors.
- **Description ≠ claim** kept throughout: the 1–10 µm hybrid-bond pitch is description-only;
  claim 17's glass+TGV limitation hangs off the **no-cavity** claim 16, not the cavity
  packages; the two glass-thickness ranges (~20 µm–1.5 mm description vs 20 µm–1.4 mm
  claim/Example) are never harmonized.
- **Firm verdict, both directions:** the close leads with the call and one this-filing
  anti-hype guard ("nothing in it schedules a product"), evidence-proportionate — no
  overreach, no safe-harbor hedging (`gate_hedge` PASS under firm posture).
