# Polish Notes (윤문 / Phase 3.7)

- **origin**: polish
- **target**: handoff/03-edit/essay-final.md
- **draft_version**: 4 → 5
- **date**: 2026-07-05
- **jurisdiction**: surface-only (split long/nested sentences, plain-word swaps, acronym
  signposting; no fact/number/date/name/anchor/quote/stance/hedge/certainty change)
- **edits applied**: 3 prose edits (all in §4) + 1 metadata (draft_version bump)
- **priority routed from self-audit**: §4 "Power Comes Up Through the Floor" reads dense
  (goal-5 signal; two casual readers "slid" on the pile-up of part numbers + FIG refs +
  parentheticals). Outcome summary at the bottom.

---

## polish 1 — §4, TSV gloss (double-appositive untangled)

- **before**: Active bridges answer with through-silicon vias, TSVs, vertical metal shafts running through the die so power and ground can cross it.
- **after**: Active bridges answer with through-silicon vias, or TSVs, which are vertical metal shafts running through the die so power and ground can cross it.
- **why-plainer**: the original stacked two bare appositives ("...vias, TSVs, vertical
  metal shafts...") so a general reader could not tell whether TSVs and "vertical metal
  shafts" were one thing or two. Inserting "or" marks TSVs as the abbreviation of
  through-silicon vias, and "which are" turns the definition into an explicit relative
  clause. Same gloss, now unambiguous on first read.
- **protected surface**: no anchor on this sentence; no number/date/name; no quote; verb
  of certainty "answer with" unchanged. Both "through-silicon vias" and "TSVs" preserved.

## polish 2 — §4, split a 42-word nested sentence at the conjunction

- **before**: In the cavity embodiments, the tested assembly is lowered onto a substrate whose top surface holds a cavity shaped for the bridge, and the description says what the through-bridge path is for: it "is often used to enable power to be routed into the bridge component" from "a source located at a bottom of a cavity in a substrate" [0035].
- **after**: In the cavity embodiments, the tested assembly is lowered onto a substrate whose top surface holds a cavity shaped for the bridge. The description says what the through-bridge path is for: it "is often used to enable power to be routed into the bridge component" from "a source located at a bottom of a cavity in a substrate" [0035].
- **why-plainer**: one long sentence carried two distinct images (the assembly being
  lowered into a cavity; the description stating the power-routing purpose). Replacing the
  ", and" hinge with a full stop lets the reader finish the first picture before the
  second begins. Target-ear length (~15-25 words) restored.
- **protected surface**: both [0035] verbatim quotes byte-identical; the [0035] anchor
  stays attached to the clause carrying the quoted fact (new sentence 2); certainty verb
  "says" unchanged; no number/date/name touched. Paragraph goes 2 → 3 sentences (well
  under STRUCT-001's 8-sentence warn line).

## polish 3 — §4, TGV acronym signposting (parallel to polish 1)

- **before**: And the receiving substrate can be built on a layer of glass shot through with through-glass vias, TGVs, the same vertical-power idea executed in glass [0054].
- **after**: And the receiving substrate can be built on a layer of glass shot through with through-glass vias, or TGVs, the same vertical-power idea executed in glass [0054].
- **why-plainer**: same friction as polish 1 in the same dense section — a bare acronym
  appositive. "or" marks TGVs as the abbreviation of through-glass vias, matching the
  fixed TSV gloss so the section handles its two acronyms consistently.
- **protected surface**: [0054] anchor intact; "through-glass vias" preserved; no
  number/date/name; no quote in this clause; verb "can be built on" unchanged.

## metadata — frontmatter

- **before**: draft_version: 4
- **after**: draft_version: 5
- **why**: skill contract (bump on polish). Explicitly the only frontmatter field polish
  may change.

---

## §4 density outcome (priority target)

**Smoothed (within surface jurisdiction):**
- The two prose stall-points a cold reader hits in §4 were the double-appositive acronym
  glosses (TSV, polish 1) and one 42-word nested sentence (polish 2). Both are now
  split/signposted so the plain-English action leads and each acronym is defined once,
  cleanly. Polish 3 makes the TGV gloss consistent with the TSV fix.

**Left with reason (could not smooth without dropping a protected numeral):**
- The number pile-ups the self-audit readers actually slid on — **526 / 536** (FIG. 5A/5B
  caption, §3), **701 / 702 / 704** (FIG. 7 caption), **872 / 882 / 860** (FIG. 8 caption)
  — all live inside **image/caption figure numerals**, which are protected surface (a
  reference numeral is a grounded part number; dropping or changing one is forbidden).
  Each caption already leads with the plain-English object *before* its numeral
  ("A cavity (701)...", "The bridge (872) sits solder-attached...", "ball-pitch solder
  pads (526, FIG. 5A)"), so the requested "plain action before the part number" ordering
  is already satisfied. Their density is intrinsic to being a figure caption that ties
  three drawn parts to the drawing; reducing it would mean dropping a grounded numeral.
  Left byte-intact by design.
- The FIG. 8 / FIG. 9 / FIG. 10 attach-option list (§4, "Even here the attach options stay
  open: ...") was left intact: each item already leads with its plain action (solder /
  direct bonding / no-cavity version), and the [0057] and [0058] anchors are precisely
  scoped to their clauses. Splitting the list would force re-scoping those anchors — a
  protected-surface risk that outweighs the marginal readability gain. Left as accepted.

**The protected [0035] verbatim quote** ("is often used to enable power to be routed into
the bridge component" / "a source located at a bottom of a cavity in a substrate") was
carried through polish 2 unchanged and byte-identical; both fragments remain patent-verbatim.

---

## Gates (re-run, full suite)

`run_gates.py --draft handoff/03-edit/essay-final.md --invention-summary ... --figures ...
--figure-selection ... --patent input/patent.md --mode essay --json`

- **Result: PASS — 14/14 gates, zero findings, zero warns.** Identical to the pre-polish
  baseline (emdash, anchors, quotes, sources, banned, structure, figure_use, meta, stub,
  cashtag, dupe, typography, hedge, surface — all clean). No gate awakened; no revert.

## Drift verification (grounding-verifier-class, inline)

Method: inline old-vs-new check of each changed sentence against invention-summary.md +
patent.md (no agent-spawn tool available to this worker; inline verification is the
sanctioned alternative). Checked: meaning preserved, protected surface intact
(numbers/dates/names/anchors/quotes/certainty verbs), signature-line byte-identity.

- **polish 1** — MEANING-PRESERVED, PROTECTED-INTACT. Gloss = lay restatement of [0024]
  ("route power and ground between surfaces"); unchanged.
- **polish 2** — MEANING-PRESERVED, PROTECTED-INTACT. Conjunction → full stop only; both
  [0035] quotes and the anchor intact; content and order unchanged.
- **polish 3** — MEANING-PRESERVED, PROTECTED-INTACT. Restatement of [0054] TGV concept;
  "or" is signposting only.
- **Reverts: none.**

## Signature-line integrity

All 3 declared thesis-trace signature lines present and byte-identical (none is in an
edited sentence):
1. "The technology in the news is the bridge getting power vias. The filing is the bridge changing sides."
2. "Only an assembly that has already passed its test gets to spend a substrate."
3. "Bond first, test before the board exists, power through the floor."

## publication re-strip

`strip_publication.py handoff/03-edit/essay-final.md` → handoff/02-compose/publication.md.
Diff against the prior publication.md = exactly the 3 §4 edits above and nothing else
(102 lines, unchanged). Signature lines and Sources block intact.
