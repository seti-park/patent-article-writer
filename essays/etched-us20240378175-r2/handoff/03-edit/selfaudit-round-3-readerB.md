# Self-audit round 3 — Reader B (skeptical pro-subject reader) — FINAL dry-check

- **Essay**: handoff/03-edit/essay-final.md (draft_version 5, closing_posture: firm)
- **Persona**: AI-infrastructure practitioner; hunts technical overclaim AND unearned hedging;
  application-vs-grant discipline is home turf.
- **Blind protocol honored**: did NOT read edit-log*, revision-response*, revision-notes,
  score-history, or any selfaudit-round-* report. Read: essay-final.md, input/patent.md
  (full text + claims 1-42 myself), input/essay-context.md, all seven figure images,
  handoff/01-design/invention-summary.md (Claim scope map + quote-anchor table),
  handoff/01-design/fact-check-log.md, handoff/02-compose/thesis-trace.md (signature-line
  declaration only, for check 7 exemption).
- **Mode**: add-findings-only. No gate, pass, or acceptance-bar relaxation proposed.

## Finding count

| Severity | Count |
|---|---|
| critical | 0 |
| high | 0 |
| medium | 0 |
| low | 5 |

No medium+ findings. Round is DRY at my desk.

---

## Pass-7 checklist (pro-subject weighting) — verdict / evidence / severity

### 1. Hook check (lead energy) — YES (pass)

¶1 opens on the declarative discovery beat: "Three years before Etched pitched 'the best
layer is no layer' as its memory philosophy, two of its co-founders had signed that idea
into the company's very first patent filing." Not a question; no verdict-insurance fact
precedes the beat (pending status arrives as ¶1's LAST sentence: "the patent office still
hasn't said yes to it" — a declared signature line). The full two-sided call lands by §1 ¶3:
"The filing proves authorship... What the filing is not, yet, is the property itself."
Date arithmetic checked: filed 2023-05-10, thread 2026-06-30 → "three years" is correct
(the brief's own "two years" was wrong; essay uses the dates). Severity: none.

### 2. Header-as-claim — YES (pass), one low (sa3B-F1)

All six `##` headers are assertions; header-only skim reconstructs the argument: paper trail
→ one giant array from identical chips → the memory claims delete the switch → math that
forgets / sidecar that remembers → Etched keeps paying to own it → an asset in formation.
See sa3B-F1 on "Identical Chips".

### 3. Steelman present — YES (pass, full strength, THIS-patent)

Conceded at full strength: "The bear case is genuinely strong, and it is already on file.
The examiner has assembled eight references against this application... a crowded field.
The breadth that makes this filing quotable is exactly what makes it shrinkable. Claim 1,
as drafted, reads on more or less any multi-chip systolic-array package, and breadth like
that is usually the first casualty of examination. Even claim 39's distinctive absence, the
no-switch hardwiring, could yet be judged routine for weight-stationary designs...
precisely the category this filing lives in." That is the strongest THIS-patent objection I
can construct as a practitioner (obviousness of switchless weight-stationary feeds over the
examiner's art + claim-1 breadth), and it is the essay's own words. Refined, not retracted:
"What survives the bear case is the record of behavior... None of that requires the claims
to survive." No generic patent truism appears anywhere as steelman. Severity: none.

### 4. No meta posturing — YES (pass)

"offered as an observation", "with its label attached", "Any motive read into them is
inference" are functional scope/evidence labels the brief REQUIRES (exempt class). No
reader-instruction, no essay-self-reference beyond verdict labeling in a verdict edition.
Severity: none.

### 5. Jargon as signpost — YES (pass)

Every term of art is glossed in one clause and dropped: HBM ("the stacked memory that feeds
modern AI accelerators"), RCE ("a fee paid to keep arguing after the examiner has said no
with finality"), independent claim ("one that stands alone instead of refining another"),
weight-stationary ("accelerators that keep weights parked in place"), security interest
("a lender's registered claim on the assets if the loan sours"), PCT ("the treaty route for
filing abroad"), continuation ("the follow-on filing that keeps a patent family growing").
"DPUs" appears only inside verbatim quotes (exempt). No overdepth past the insight.
Severity: none.

### 6. No stub / rhythm break — YES (pass)

Section word counts (trace-confirmed by my own read): 274 / 477 / 735 / 449 / 571 / 237.
The 237-word closer is a proportionate verdict coda, not a stub. Severity: none.

### 7. Thesis not over-restated — YES (pass, at the boundary)

Verdict asserted in exactly 3 sections net of the 3 declared signature lines (thesis-trace
declares: §1 ¶1 closer, §3 bold, §6 final two sentences; all three appear verbatim in the
essay): lead ¶3 ("That mix is the verdict in miniature"), §5 refinement ("What survives the
bear case..."), §6 ("The verdict is firm"). ≤3 satisfied. Severity: none.

---

## Deep claim audit (sought-as-owned sweep) — CLEAN

Read all 42 claims myself. Independents are 1, 15, 26, 39 — matches the essay and the Claim
scope map. Every essay statement of claim content uses application-era language: "asks for"
(§1), "It claims" (§2), "Claim 39 is where the drawing becomes a legal ask" (§3), "As
drafted, claims 11 through 13..." (§4), "seeks" (claim 15, §3), "the claims as drafted can
shrink or die" (§6). Zero instances of locks/requires/fences/owns for sought scope. Grant
language appears only for the OTHER, actually granted patent ("the part Etched has since
gotten granted", US 12,361,091 B1) — correct. Specific verifications:

- "Claim 39 is an independent claim... and it does not require the multi-chip package at
  all" — TRUE against claim text ("A package, comprising: an IC comprising a systolic
  array...").
- "the broadest package claim does not require memory chips, which the description concedes
  'may not be needed' [0037]" — TRUE (claim 1 has no memory element; [0037] verbatim).
- "every memory channel hardwired to its own column or columns, 'without any switching
  element'" — faithful translation of claim 39's "each of the plurality of channels is
  hardwired to respective one or more columns... without any switching element".
- "none of what it shows is claimed anywhere" (FIG. 7) — TRUE: no claim recites pipelining,
  batching, passes, or utilization.
- Scope map honored: no locked entries anywhere; map declares "No pinned point limitations
  exist" and the essay invents none — 128×128, 1 TB/s, 98%, 100×400/400×100 are all
  narrated as the description's own numbers on description anchors, never as claim bounds.

## Mechanism honesty vs spec + figures — CLEAN (images read myself)

- **FIG. 5** (header embed + §3 walk): image shows exactly two memory chips 505A/505B, four
  channels 510A-D, wires 520, four columns 515A-D inside array 220 on IC 215, nothing else
  in the memory-to-column path. Caption matches. The known FIG. 6 manifest defect is NOT
  reproduced anywhere.
- **FIG. 6**: image truth confirmed — 605A-D (auxiliary circuitry) sit INSIDE ICs 615A-D
  beside array tiles 220; 610A-D (local memory chips) are the small boxes OUTSIDE each IC,
  attached to 605; dashed 650 encloses only the 220 tiles. Essay caption states precisely
  this. Defect avoided.
- **FIG. 1/2/3/4/7**: captions verified against images ("two computations sharing one grid"
  = hashed/unhashed Multiplication #1/#2; nine labeled ICs 215A-I with 210A-C on top and
  host 205 over PCIe 240; six drawn memory chips 305A-F; FIG. 4 = 2×3 unequal grid; FIG. 7
  legend and the Time-B stall band match [0053]-[0057]).
- All quoted spans re-checked verbatim against input/patent.md AND confirmed substrings of
  the invention-summary quote-anchor rows (including the [0045] run-on-typo-safe substring).
  Zero quote failures.

## Grounding spot-check (exceeded 5-sample: all anchors, four body sections) — CLEAN

Every `[dddd]` anchor in §1-§4 verified against the cited paragraph: [0016], [0044] (§1);
[0013], [0028], [0018]×2, [0002], [0021]×2, [0024], [0019], [0038] (§2); [0043]×2,
[0044]×2, [0045]×2, [0016]×2, [0037], [0014], [0039]×2, [0040], [0035] (§3); [0027],
[0003], [0047]×2, [0048], [0051], [0053], [0055]×2, [0056], [0057] (§4). All support their
sentences. Arithmetic glosses check out: 128×128 ≈ "roughly sixteen thousand multipliers"
(16,384); 1 TB/s × 5 ms = 5 GB ≈ "a feature film's worth" (logged derived comparison
film-per-5ms). Zero anchor failures.

## External-fact fencing — CLEAN (one low on source coverage, sa3B-F3)

- **Venue/date/founder wording**: thread (never "stage"), "late June 2026" everywhere, body
  consistent with the cited TechCrunch URL date (2026/06/30); "two of its co-founders" /
  "co-founders Gavin Uberti and Christopher Zhu" matches the record (and implies, correctly,
  that other co-founders exist).
- **ONE prosecution label**: exactly one dated label sentence (§5 ¶1: pending; final
  rejection mailed 23 October 2025; RCE docketed 24 April 2026; "As of the May 2026
  record"). Lead carries status-only clauses without dates; no round-by-round battle
  narrative (the two non-finals and the third non-final are never narrated). Compliant.
- **Both-or-neither**: rejection record and collateral facts co-travel in §5 (and at
  preview altitude together in §1 ¶2-¶3). Satisfied.
- **Liens**: portfolio scope only; both reel/frames correct (067204/0877, 071792/0869);
  EFFECTIVE dates used (19 April 2024, 18 July 2025), not recordation dates; blanket
  discipline stated in-text ("selecting nothing and saying nothing about any single
  filing's worth"); symmetric creditor frame present; grant/lien timing stated as dates
  with motive labeled inference. The rejected-compiler-applications detail is used to
  ENFORCE anti-selectivity. Fully compliant with the hard discipline.
- **Company claims**: "$1B+ contracts", "$800m raised", racks shipping — all attributed
  ("the company's own claim", "in the company's telling", "the company says"). CSM
  expansion attributed to "the press's expansion". Tier-5 Sohu linkage correctly unused.
- **Examiner-art assignees** ("Intel, IBM and Rambus among the assignees"): grounded in
  fact-check-log `examiner-art-8refs` (tier-1, registry-extract; ETRI omitted, covered by
  "among"). TPU 128×128→256×256 grounded in `tpu-mxu-128x128` with both Google URLs in
  Sources; "floating-point" qualifier correctly excludes the int8 v1 MXU.
- **LVI absence + 18-month caveat**: matches `lvi-absent-here` (full-text verified) and the
  brief's required caveat, rendered verbatim in spirit ("applications younger than 18
  months can exist unpublished and unseen").

## Over-hedge symmetric check (6G) — CLEAN in the hedge direction

Verdict leads declaratively ("The verdict is firm."); zero safe-harbor boilerplate; the
generic "patents don't guarantee products" move is ABSENT (good — banned); exactly ONE
patent-specific anti-hype guard in the closing ("Racks shipping this summer, if they ship,
are not evidence that these claims will grant. That question gets decided against the
examiner's citations, nowhere else."). "if they ship" is attribution calibration on a
company-claimed fact, not verdict hedging. The conclusion is NOT safer than the body: the
body proves authorship-on-record, deliberate drafting, repeated spend, collateral both ways
— and the verdict claims exactly that, no less. The residual asymmetry runs in the
OVERREACH direction (sa3B-F4), not over-hedge.

---

## Findings (add-only; fixes respect the jurisdiction fence: anchor / narrow / label / cut)

### sa3B-F1 — check 2 (header-as-claim) / mechanism honesty — LOW
- **Verdict**: yes (finding stands, minor)
- **Evidence**: header "One Giant Array, Stitched From Identical Chips" vs [0028] "In one
  embodiment, the ICs 215 are all identical." — identicality is an optional embodiment
  required by NO claim (claim 1 recites only "a plurality of ICs, each comprising a local
  systolic array"). The body scopes it correctly ("In a version the filing describes, the
  chips are all interchangeable"), so the header outruns sought scope only at skim level.
- **Fix (narrow, optional)**: e.g. "One Giant Array, Stitched From Small Chips". Body needs
  no change.

### sa3B-F2 — deep claim audit (quote-vs-claim attribution blur) — LOW
- **Verdict**: yes (finding stands, minor)
- **Evidence**: §4: "claims 11 through 13... wall its memory off from the arrays, down to a
  flat negative rule: 'the local systolic arrays 220 do not have access to the local memory
  chips 610' [0051]." The quoted sentence is the DESCRIPTION's ([0051]); claim 13's operative
  words are "do not communicate with the local memory chips". Anchor is honest and the
  limitation is equivalent at this altitude, but the essay's own translate-then-quote device
  (§3, "The description's twin sentence") shows the cleaner pattern.
- **Fix (label, optional)**: mark the quote as the description's twin of claim 13, or quote
  claim 13's own words.

### sa3B-F3 — external-fact fencing (Sources coverage gap) — LOW
- **Verdict**: yes (finding stands, minor)
- **Evidence**: §5: "while the granted trio got both treatments" (PCT + continuation) is a
  factual claim about US 12,306,903 / 12,361,091 / 12,361,262, sourced in the fact-check-log
  to a WIPS bibliographic export — but no entry in `# Sources` covers the TRIO's family
  records (the Google Patents line is scoped "for application US 18/195,769").
- **Fix (anchor)**: widen the registry Sources line to cover family/bibliographic records for
  the granted trio, or (cut) drop the trio-treatment clause and keep only this filing's
  US-only/no-continuation observation.

### sa3B-F4 — overreach-direction calibration (authorship verbs) — LOW
- **Verdict**: yes (finding stands, minor)
- **Evidence**: §1 "The filing proves authorship" and §6 "The no-switch idea is authentically
  the founders' own writing". Named-inventor attestation evidences conception of the claimed
  subject matter; it does not make the drafted text "the founders' own writing" (claims are
  ordinarily attorney-drafted). The essay's own steelman refinement carries the calibrated
  verb: "A signed, dated statement of the architecture... is EVIDENCE about the company."
- **Fix (narrow)**: "the founders' own, in writing" / "signed statement of the founders'
  idea". This is an overreach nitpick, not a request for hedging; the verdict's strength is
  otherwise earned.

### sa3B-F5 — external-fact fencing (identity claim rests on a pitch line) — LOW
- **Verdict**: yes (finding stands, minor)
- **Evidence**: §3: "the company's stealth-exit thread made the same idea its memory pillar
  and named it CSM". The mechanism-level identity between claim 39's on-package
  channel-to-column hardwiring and a rack-scale product pillar is unverifiable from the
  record; the support is a nine-word company pitch line. The essay's very next sentences
  carry both the correct level ("The pitch and the claims name the same absence") and the
  correct concession ("Whether the racks the company says are shipping practice these
  claims is invisible from the patent record") — but the identity assertion ("the same
  idea") precedes them.
- **Fix (narrow)**: "made the same absence its memory pillar" / "made that philosophy its
  memory pillar", aligning the first assertion with the already-present calibrated line.

---

## Persona verdict (skeptical pro-subject reader)

This essay survives a hostile practitioner read unusually well: every quote is verbatim,
every claim-scope statement is sought-not-owned, the steelman is the real objection stated
better than most bears would state it, and the verdict is firm without borrowing strength
the record doesn't have. The one sentence I'd attack is "The no-switch idea is authentically
the founders' own writing" — inventorship attests the idea, not the pen, and the essay's own
refined line ("a signed, dated statement... is evidence about the company") already knows
the correct verb; that gap between "writing" and "signed statement" is the only joint where
a skeptic gets a finger in, and it bends rather than breaks.

**Energy-vs-evidence (surface)**: title (59 chars) and lead deliver the discovery register
at exactly the evidence's strength — "Put Its ... Idea in Writing" is the precise,
non-inflated verb for a pending application. No SURF-class defect observed.

**Round-3 dry status at this desk: DRY — 0 critical / 0 high / 0 medium / 5 low.**
