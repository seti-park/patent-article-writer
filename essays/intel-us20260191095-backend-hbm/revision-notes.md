# Revision notes — intel-us20260191095-backend-hbm

> **The revision-delta capture channel.** These deltas are the multi-voted **self-audit
> round-1** fixes, applied to the accepted essay by the composer in revision mode AFTER the
> inner loop returned double-clean. `pipeline-retro` normalizes each `## delta` block into
> `meta/findings-ledger.jsonl` with `origin: self-post-accept`
> (`meta/normalize_revision_notes.py --origin self-post-accept`). One block per edit; keys
> `class` / `round` / `before` / `after` / `rationale`, each on one line.
>
> Source reports: `selfaudit-round-1-{adversarial-A,adversarial-B,grounding,coldreader}.md`.
> Grounding-verifier returned ALL SUPPORTED — no grounded claim was weakened; every fix below
> is narrow / label / cut / compress / gloss, never a hedge. `closing_posture: measured` and
> both declared signature lines are preserved byte-identical; every `[dddd]` anchor and every
> verbatim quote is preserved. draft_version 2 -> 3.

## delta
class: paraphrase-accidental-drift
round: v3 (self-audit r1)
before: §1 "stack those dies eight high to match the footprint of HBM4" (conflates stack-height [0023] with die/block area [0034])
after: "stack those dies eight high, and to size the block to the footprint of HBM4" (height and footprint separated)
rationale: resolves adversarial-A F6; [0023] is Z-height/capacity, [0034] is X-Y area — a precision fix, not a hedge.

## delta
class: claim-scope-misattribution
round: v3 (self-audit r1)
before: §1 hook "You change where this kind of memory can be built." (states the who-makes-HBM market inference unconditioned, firmer than §4's labeled analysis)
after: "You change what kind of factory can build it." (narrowed to the grounded fab-type consequence of a low-temp back-end cell)
rationale: resolves adversarial-A F5; light-touch narrow keeps the discovery hook's force and defers the market leap to §4 and the conditioned signature line.

## delta
class: jargon-overdepth
round: v3 (self-audit r1)
before: §3 "Traffic moves down the stack ... Four gutters are cut into every die, each carrying the data for a pair of sub-channels [0034]" (spec-sheet plumbing; cold-reader + impatient-reader stop point)
after: compressed to the load-bearing idea (columns of TSVs split traffic into many independent sub-channels whose combined width is bandwidth); four-gutters granularity left to the kept FIG 1G caption; "sub-channel" glossed on first use
rationale: resolves adversarial-A F1 + the cold-reader stop-point; the [0034] four-gutters fact is preserved verbatim in the FIG 1G caption, so no grounding is lost.

## delta
class: jargon-gloss-gap
round: v3 (self-audit r1)
before: §4 FIG 1A caption "joined on a single interposer" (term of art, no first-use gloss)
after: "a single interposer, the silicon bridge that wires the two dies together" (one-clause gloss)
rationale: resolves adversarial-A F4; reader-profile jargon-gloss budget — calibration, not a hedge. (class may need a main attribution-table row.)

## delta
class: paraphrase-substantive-change
round: v3 (self-audit r1)
before: §4 "ZAM stacks on a diagonal Z-angle joined by hybrid bonding ... This filing uses vertical TSV gutters and UCIe instead." (mixes three axes; "instead" implies the filing avoids hybrid bonding, contradicting [0020] both-sided HBI + [0023] wafer-to-wafer)
after: "ZAM's public signature is its diagonal Z-angle stacking; what this filing turns on is the back-end transistor cell, organized by vertical TSV gutters." (contrast rests on the true axis — cell architecture + channel organization; hybrid bonding dropped, asserted neither way)
rationale: resolves adversarial-B F1; corrected without asserting hybrid bonding as a new patent claim — the essay simply stops asserting the filing's die-joining, so it neither mixes joining/I-O/bonding axes nor contradicts [0020]/[0023].

## delta
class: thesis-restatement-redundancy
round: v3 (self-audit r1)
before: §5 "It keeps the capacitor and merely moves it, where the more radical path deletes it." (re-spends the §2 bold-anchor "relocated, not removed" caveat a third time)
after: "The more radical path deletes the capacitor; in imec's capacitor-less cell ..." (leans on the net-new imec 2T0C contrast; the relocate-not-remove caveat stays in §2 and §6 only)
rationale: resolves adversarial-A F3; the caveat is now referenced via the imec contrast rather than restated, keeping §2's protected anchor and §6's sanctioned guard as its only two homes.

## delta
class: claim-scope-misattribution
round: v3 (self-audit r1)
before: §5 "the single property a logic-and-packaging line can carry and a front-end fab cannot" (over-reach; a DRAM front-end fab runs BEOL too, and the essay itself says the incumbents are already building 3D DRAM)
after: "the property a logic-and-packaging line can carry without owning a DRAM front-end" (matches the §4/§6 form; drops the incapability claim)
rationale: resolves adversarial-B F2; narrowed to the supported claim, removing the in-section self-contradiction — a narrow, not a hedge.

## delta
class: thesis-restatement-redundancy
round: v3 (self-audit r1)
before: §6 ¶1 "... built in the back-end. That is the property that could let a logic-and-packaging maker carry HBM-class memory without owning a DRAM front-end." (foundry beat restated; ¶4 and the ¶5 signature already land it)
after: "... built in the back-end." (the ¶1 foundry restatement cut)
rationale: resolves adversarial-A F2(a); de-circles the closing so the foundry payoff lands fewer times before the protected leaving-sentence.

## delta
class: evidence-scope-overreach
round: v3 (self-audit r1)
before: §6 ¶3 "the density, yield and cost per bit of this class of tall, stacked HBM challenger will either hold up or they will not" (implies VLSI 2026 / ZAM tests THIS filing's back-end cell)
after: labels VLSI 2026 as a class/direction test (ZAM is a hybrid-bonded, Powerchip-fabbed cousin, not established to use back-end cells) and states the back-end-cell differentiator "has no public proof point yet"; the ~2029 horizon and the direction commitment are kept
rationale: resolves adversarial-B F3; separates the direction-proof from the differentiator-proof — an honest measured close, not a hedge (the grounded "cell is backend" fact is untouched).

## delta
class: thesis-restatement-redundancy
round: v3 (self-audit r1)
before: §6 ¶4 "If the numbers miss, the cell still sits in the back-end, and the filing waits for the process to catch up." (third "cell in the back-end" just before the ¶5 signature setup)
after: "If the numbers miss, the filing waits for the process to catch up." (one restatement cut; the ¶5 signature landing preserved byte-identical)
rationale: resolves adversarial-A F2(a); trims "the cell is in the back-end" from ~3x toward the leaving-sentence without touching the exempt signature line.

## delta
class: source-pointer-style-drift
round: v3 (self-audit r1)
before: Sources — the ZAM Tom's Hardware entry did not identify itself as the source for "Powerchip fabricates ZAM's DRAM" (the §5 tell)
after: entry annotated "(also names Powerchip, not Intel, as ZAM's DRAM fabricator)"; the §5 Powerchip point is kept — its double edge (a DRAM foundry still in the loop) is a fair limit for the measured verdict
rationale: resolves adversarial-A F8 (pinpoint) and dispositions adversarial-B F4 as kept-not-cut; same fact-check URL (zam-powerchip-fab), so annotated in place rather than duplicated as a new entry.

## Dispositions volunteered / not applied

- **adversarial-A F7 (LOW, single-vote, borderline) — NOT applied.** Mild reader-orientation
  phrases ("Read cold, the bear case is strong, and it should be put at full strength"; "Here
  is where this leaves an investor"). `gate_meta` passed; the §5 phrase asserts-then-delivers a
  claim and the §6 phrase is a standard verdict-section signpost the impatient reader welcomes.
  A judgment-level watch, not a clear violation, and not in the multi-voted fix set.
- **adversarial-B F4 (LOW) — kept, not cut** (logged in the Sources delta above): the Powerchip
  tell's double edge is a fair, honest limit that strengthens the measured verdict; cutting or
  narrowing it would drop a legitimate limit.
- **grounding-verifier — ALL SUPPORTED, nothing to weaken.** Every fix above is
  narrow / label / cut / compress / gloss; no grounded claim was hedged or removed.

---

## Round 2 (self-audit r2) — draft_version 3 -> 4

> Two localized **self-audit round-2** fixes, applied to the accepted essay by the composer in
> revision mode. Both edits land in §6 only. Grounding-verifier round 2 returned ALL SUPPORTED
> (double-clean across r1 and r2), so no grounded claim, `[dddd]` anchor, or verbatim quote was
> weakened; both are label / cut per the grounding fence, never a hedge. `closing_posture:
> measured` preserved; both declared signature lines + the §2 bold anchor preserved
> byte-identical. Source reports: `selfaudit-round-2-{adversarial-B,coldreader,grounding}.md`.

## delta
class: term-collision-coherence
round: v4 (self-audit r2)
before: §6 ¶3 "That tests the direction, not the differentiator: ZAM is not established to use a back-end-transistor cell, and the back-end cell at the center of this application has no public proof point yet" (reuses "direction" in the being-tested sense four lines below the settled sense — the header "The Direction Is Real" and "The direction is not in doubt" — so the verdict's headline word silently flips referent in the highest-stakes section)
after: "That tests the class, not this filing's cell: ZAM is not established to use a back-end-transistor cell, and the back-end cell itself has no public proof point yet" ("direction" reserved for the settled commitment; the tested thing renamed "the class", echoing "this class of tall, stacked challenger" one sentence up; the differentiator named "this filing's cell")
rationale: resolves adversarial-B SELFAUDIT-R2-B-01 (medium); label/clarity per the revision-mode grounding fence, not a hedge — verdict substance unchanged, both patent-specific anti-hype guards kept (1T1C capacitor ceiling in §6 ¶2; this-cell proof-point gap retained as "the back-end cell itself has no public proof point yet"); the firm close "a question of yield, not of architecture" is byte-identical.

## delta
class: caveat-restatement-redundancy
round: v4 (self-audit r2)
before: §6 ¶3 "Intel and SoftBank's ZAM, a hybrid-bonded cousin of this filing, is due to be presented at VLSI 2026 in June" (the "ZAM is a hybrid-bonded cousin / not the same as this filing" distinction recurs 3-4x essay-wide and is doubled inside §6 — this appositive plus the class-vs-cell point one sentence later; round-2 cold-reader flags it as a last-section attention-budget drag)
after: "Intel and SoftBank's ZAM is due to be presented at VLSI 2026 in June" (the appositive restatement cut; the §6 class-vs-cell point "ZAM is not established to use a back-end-transistor cell" now carries the distinction once, and more precisely, inside the verdict)
rationale: resolves the round-2 cold-reader last-section drag; a cut/compress, not a hedge. The distinction is preserved — once at introduction (§4 "no ground for calling them one chip") and once in the verdict (§6 class-vs-cell) — just no longer doubled in §6; the §5 Powerchip tell is a distinct, sanctioned limit and is untouched. No ZAM conflation reintroduced: the class-vs-cell statement is the stronger anti-conflation claim, and "hybrid-bonded, not BEOL" (r1-F1) is asserted neither way, so the filing's own bonding stays unstated (consistent with [0020]/[0023]).

## Round 2 dispositions (self-audit r2)

- **adversarial-B SELFAUDIT-R2-B-01 (medium) — applied** (delta 1). The §6 "direction"
  term-collision introduced by the round-1 fix-3 clause; disambiguated by naming the tested
  thing "the class" and reserving "direction" for the settled commitment.
- **round-2 cold-reader ZAM-caveat over-repetition (attention-budget) — applied** (delta 2).
  Trimmed the §6 appositive restatement; the distinction now appears once at introduction (§4)
  and once in the verdict (§6 class-vs-cell). §5 Powerchip tell kept (distinct sanctioned limit).
- **round-2 grounding-verifier — ALL SUPPORTED, nothing to weaken.** Both edits are label / cut
  on external-fact framing (§6 ¶3 carries no `[dddd]` anchors and no verbatim patent quote); no
  grounded claim, quote, or anchor touched. Both declared signature lines + the §2 bold anchor
  byte-identical; `closing_posture: measured` unchanged. draft_version 3 -> 4.

## Self-audit closure

self-audit: no unresolved findings

Round 3 (dryness confirmation, within cap 3): a fresh, blind skeptical-domain-expert reader
returned "none — self-audit is dry" (critical/high/medium/low all 0). The §6 "direction"
term-collision is resolved (tested thing = "the class", differentiator = "this filing's cell";
"direction" reserved for the settled commitment) and the ZAM-not-this-filing caveat is spent
exactly twice (§4 introduction + §6 verdict), no conflation reintroduced. Grounding held
double-clean across self-audit rounds 1-3 (grounding-verifier ALL SUPPORTED each pass); §6
remains evidence-proportionate under the measured posture (neither overreach nor over-hedge).
Self-audit loop: round 1 applied 10 findings, round 2 applied 2, round 3 dry.

## Human-post-accept revision (v5 -> v6)

- **origin: human-post-accept.** Owner-directed credit line added near the top of the essay
  (immediately under the H1, before the cover figure): an italic one-sentence acknowledgment
  that the piece was prompted by a thread from @Underfox3, which flagged this Intel filing, its
  Cross-Batch Memory (XBM) design, and the move to a backend DRAM cell fed over UCIe links.
- Scope: additive standfirst note only. No argument prose, no [dddd] anchor, no verbatim patent
  quote, and no signature line touched. The credit stays at the design facts shared with the
  patent (XBM is the patent's own term at [0034]; backend 1T1C DRAM at [0020]; UCIe at [0034]);
  it deliberately does NOT adopt the source thread's bolder framing ("direct HBM4 competitor",
  "reduces production cost") into the essay's measured voice.
- Gates re-run: 14/14 PASS, 0 warns. publication.md re-stripped; draft_version 5 -> 6;
  essay-draft.md synced.
