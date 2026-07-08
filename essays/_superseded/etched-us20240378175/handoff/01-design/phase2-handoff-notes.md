# Phase 2 Handoff Notes

## (a) Audience reframe decision

None. Default reader-profile holds (curious retail investor, advanced high school - early
undergraduate). Two calibration notes within that default:
- The reader needs the systolic-array mental model built once, early (§3, FIG. 1: weights
  fall, data flows right, every cell multiplies-and-adds) — everything after reuses it.
- This is the pipeline's FIRST pending-application edition. Assume the reader does not
  know the difference between an application and a grant; the essay must teach it in one
  or two working sentences (an application = scope the company is ASKING for), because
  the verdict depends on the reader holding that distinction.

## (b) Citation priority mapping

| Quotable span / anchor | Primary section | Role |
|---|---|---|
| q-0013-1 `[0013]` (claim-1 mirror: package of ICs, combined array) | 2-origin-document | what the document claims, stated once |
| q-0019-1 `[0019]` (multi-chip approach) | 2-origin-document → 3-one-big-array | mechanism bridge |
| q-0018-1 / q-0018-2 `[0018]` (128×128 ceiling; 100s of GB) | 3-one-big-array | problem framing — spend here, not in the lead |
| q-0028-1 `[0028]` (host sees one large array) | 3-one-big-array | the "splittable math arrays" payoff line |
| q-0027-1 `[0027]` (no runtime instructions, preset loop) | 3-one-big-array | the specialization bet in one quote |
| q-0030-1 / q-0030-2 `[0030]` (UCIe; 32 GT/s) | 3-one-big-array | optional color — description preference, NOT claim-required |
| q-0016-1 `[0016]` (claim-39 mirror: channels hardwired, no switching element) | 4-memory-half | THE spine quote — reserve for §4, do not spend earlier |
| q-0043-1 `[0043]` (a switch is typically used) | 4-memory-half | baseline first, then the inversion |
| q-0044-1 `[0044]` (channels directly wired to a column) | 4-memory-half | mechanism support |
| q-0045-1 / q-0045-2 `[0045]` (hardwiring permissible; save space and power) | 4-memory-half | effect payoff |
| q-0040-1 `[0040]` (>1 TB/s) | 4-memory-half | quantitative support |
| q-0047-1 / q-0047-2 `[0047]` (self-attention needs history; most of a transformer does not) | 5-division-of-labor | the transformer-shaped split |
| q-0051-1 `[0051]` (arrays do not access local memory) | 5-division-of-labor | claims 11-13 anchor |
| q-0057-1 `[0057]` (98% or greater utilization) | 5-division-of-labor | quantitative close of the mechanism half |
| q-0039-1 `[0039]` (more rows without more memory chips) | 3 or 4 (one clause) | carries dropped FIG. 3's point in prose |
| q-0002-1 / q-0003-1 / q-0003-2 | 3-one-big-array | educational scaffolding, use sparingly |
| q-0021-1 `[0021]` (weights may be constants) | 4-memory-half | the WHY of hardwiring (constants always feed the same columns) |
| q-0035-1 `[0035]` (memory chips store weights at runtime) | 4-memory-half | claim-15 support if needed |

## (c) Framing trace (rejected candidates)

- **Candidate 2 ("one array from many chips", technical-impossibility)** rejected: the
  impossibility premise is undercut by the crowded examiner-cited field this essay itself
  reports, and a mechanism-first frame cannot land the edition's required document-as-asset
  verdict. Its material IS §3/§5 — but Phase 2 must not let the essay's center of gravity
  drift back to "look how clever the architecture is"; the mechanism sections serve the
  origin-document reading.
- **Candidate 3 ("the collateral story")** rejected: 1/4 on 4-axis grounding and it
  over-reads a blanket lien by construction. It survives as EXACTLY ONE paragraph in §6
  under the discipline in trap T2 below. Phase 2 must not expand it or move it to the lead.

## (d) Traps to avoid

**T1 — Claim scope (pending edition; restates the Claim scope map's vocabulary):**
- The map has NO locked class. Classes: claim 1 sought-broad, claim 26 sought-structured,
  claim 15 sought-system, claim 39 sought-memory-interface (plus deps 7/8 HBM hardwiring
  and 11-13 sought-auxiliary-division).
- DO say "the application claims / Etched is seeking / as drafted". DON'T say "the patent
  locks / requires / fences / protects" — grant-era verbs are wrong for every claim in
  this document.
- DON'T use enforceability language anywhere: nothing here can be infringed until (unless)
  it grants.
- DON'T present description preferences as claim-required: UCIe (`[0030]`), interposer vs
  stacking, unidirectional-vertical/bidirectional-horizontal (deps 2-4 only), HBM-on-top
  — claim 1 as drafted requires none of these. Claim 26 requires the grid-like pattern;
  claim 1 does not.
- DON'T call any number a claim limitation: 128×128, 100-10000, 32 GT/s, 1 TB/s, 98% are
  specification statements, not claim text. There are no pinned "about X" values in this
  claim set (Pins column is empty — do not invent floors or ceilings).
- DO carry each independent's prosecution-risk note if scope comes up: claim 1 likeliest
  to narrow; claim 39 most specific and likeliest to survive in some form — as drafted.

**T2 — Collateral discipline (hard):**
- The two TriplePoint liens are BLANKET over the portfolio at each signing date. DON'T
  present either lien as evidence that THIS application is individually important — the
  same pledged pool contains two rejected applications. DO use the honest two-sided frame:
  the whole stack, crown jewels included, is banked as venture-debt collateral — IP is the
  company's bankable asset class, AND the encumbered pool is what a creditor reaches if
  things go wrong.
- DO cite reel/frames (067204/0877; 071792/0869) — they are the verifiable spine of the
  beat.
- Timing: grants 2025-07-15, second lien effective 2025-07-18. DO state the dates; DON'T
  assert motive — any motive reading must be explicitly labeled as inference
  (correlation-only).

**T3 — Label sentence (hard):**
- The prosecution status gets EXACTLY ONE sentence, carrying: pending; examination
  continuing after a final rejection and a request for continued examination (as of the
  2026-05 record). No battle narrative, no office-action play-by-play.
- Both-or-neither: if the essay cites the collateral facts, this label sentence MUST also
  appear (same section, §6). Omitting it is one-sided evidence selection.

**T4 — Attribution and boundaries:**
- Thread claims ($1B+ contracts, $800m raised, summer 2026 racks, LVI/CSM) are
  company-claimed ONLY — attribute as "the company says" every time.
- LVI (voltage/power delivery) is nowhere in THIS filing (full-text verified). DON'T
  extend that to other filings without its own evidence level; the 18-month unpublished
  window caveat applies to what may exist unseen.
- Max ONE clause of continuity with the published wiring-half essay (US 12,361,091 B1);
  no dependence on the reader having read it.
- US-only / no-PCT / no-continuation family status is a labeled observation
  (bibliographic), not a conclusion about company intent.

**T5 — Verbatim mechanics:**
- Quote ONLY from invention-summary Quotable spans / Quote anchor table — never re-touch
  patent.md. The source text contains run-on artifacts ("105passes" `[0022]`, "230are"
  `[0029]`, "225and 230" `[0030]`, "250formed" `[0025]`, "215in" `[0040]`, "220and"
  `[0045]`) and the exponent artifact "2N{circumflex over ( )} 2" `[0018]`. Anchors were
  cut to stop BEFORE these; extending any quote will fail verbatim verification or
  reproduce an artifact.
- Em-dash banned in essay body; verbatim patent quotes keep their punctuation.

**T6 — Verdict shape (closing_posture: firm):**
- Draft the call FIRST: this document is the memory-side half of the architecture bet, in
  writing, dated May 2023, authored by both founders — a roadmap the company keeps paying
  to defend and has already banked, not yet a fence. Then bound it.
- Exactly ONE patent-specific anti-hype guard: the sought-broad claim 1 is the part
  likeliest to shrink in the examiner-cited field. Not more.
- The steelman beat (concede-then-refine, §6→§7): concede at full strength that the
  examiner has said no once and three years of prosecution have produced no enforceable
  claim; refine with what is already true regardless (date, authorship, disclosure
  content) and the claim-39 specificity. NEVER swap in a generic "patents don't guarantee
  products/stock prices" truism — that is banned as a steelman and scores steelman-absent.
- Residual risk is Acceptance → closing-binary-test: the RCE outcome (allowance vs further
  narrowing/abandonment) is the watchable falsifier. DON'T close on an open question.

**T7 — Figures:**
- FIG. 3 / FIG. 4 are intentionally dropped (variant family of FIG. 2) — do not reopen;
  their one point travels as q-0039-1 in prose.
- FIG. 1 → FIG. 2 order: logical view before physical realization (`[0028]` pair).
- FIG. 6 captions: 605 = auxiliary circuitry, 610 = local memory chips (the manifest
  one-liner has these swapped; follow the specification).
- Cover: FIG. 5 (claim-39 core step). Caption in application-era language.

## (e) Open questions for Phase 2 (awaiting SETI)

- Placement of the single continuity clause referencing the wiring-half essay: default is
  §2-origin-document (where "earliest filing" is established); alternative is §6 (where
  the granted-vs-pending contrast does verdict work). Composer's call; keep it to one
  clause either way.
- Whether the examiner-cited-field fact (8 references, crowded field) appears as its own
  clause in §6 or only inside the steelman concession. Default: inside the steelman —
  essay-context marks it optional, one clause.
- Title pattern: the friction hook supports both a dated-artifact reversal ("the memory
  half was in writing in May 2023 — it just isn't granted") and a verdict-led declarative.
  SETI to pick at compose time.
