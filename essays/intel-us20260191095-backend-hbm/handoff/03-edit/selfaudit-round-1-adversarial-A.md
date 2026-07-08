# Self-audit round 1 — adversarial reader A

- **persona**: impatient investor (instantiates `_shared/references/reader-profile.md`:
  high-school-to-undergraduate technical comprehension, here for the money thread)
- **target**: `handoff/03-edit/essay-final.md` (register: discovery; closing posture: measured)
- **method**: pass-7 checklist (7 items, evidence-forced) + grounding spot-checks (anchors in
  the anchored sections, claim-scope vs Claim scope map, pins-not-bounds)
- **verdict counts**: 0 critical, 0 high, 2 medium, 6 low
- **isolation**: blind to all other reviewers and prior rounds

---

## Checklist verdicts (each → {verdict, quoted span or ABSENT, severity})

### 1. Hook check (lead energy) — PASS (no finding)

¶1 lands the discovery beat declaratively, nothing queued ahead of it:
> "Intel's newest memory filing does something quietly radical. It builds the transistor
> inside each DRAM cell in the chip's back-end wiring layers..."

The two-sided call lands by the lead section's end (§1 ¶3, signature line 1):
> "Intel's filing moves the DRAM cell into logic-stackable back-end layers, and if the yield
> numbers land, who can make HBM stops being a three-company club."

No verdict-insurance fact precedes the beat; SURF-004 defensive-open absent. Passes. (Minor
watch: "does something quietly radical" is a half-clause of throat-clear, but it is paid in
the very next sentence — not elevated.)

### 2. Header-as-claim — PASS (no finding)

All six `##` headers are assertions and a header-only skim reconstructs the argument:
"A Memory Architecture From the Company That Left It" → "Claim 1 Turns on a Single Word:
Backend" → "A Tower Built to Match HBM4's Footprint" → "A Back-End Cell Could Loosen the
DRAM-Fab Bottleneck" → "Read Cold, It Is One Filing That Keeps the Capacitor" → "The Direction
Is Real; the Numbers Are the Test." No `nonclaim-section-header`.

### 3. Steelman present + not overweight — PASS (no finding on this check; see F3)

The concession is a THIS-patent objection, specific, not a generic truism:
> "Claim 1 fixes a single word. It never names the channel material, never claims a
> logic-compatible process, never promises a yield. It keeps the capacitor and merely moves
> it... One filing with no numbers, set against three funded roadmaps, could read as noise."

Ratio is ~9 concession sentences : ~8 rebuttal sentences, and the affirmative core lands last
and decisively:
> "All of that is true, and none of it touches the one thing the claim does settle. The cell
> is backend."

Affirmative core carries ≥ the concession; no spend/procedure motif inside the beat (SURF-007
clean). `steelman-absent` NO, `steelman-overweight` NO. (The one re-spent caveat inside it is
captured separately at F3.)

### 4. No meta posturing — LOW (F7)

§4's boundary markers ("Here the filing's own words stop, and the reading begins"; "the leap
is mine, not the document's") are functional scope disclaimers — **exempt**. Two residual mild
reader-orientations remain (see F7).

### 5. Jargon as signpost — LOW (F4)

Discipline is strong: 1T1C, thin-film transistor, TSV gutter, front-end/back-end, UCIe, HBM4,
hybrid bonding all get a one-clause gloss on first use, and FEOL/BEOL/2T0C/datablock/XBM are
kept out of prose entirely. Two soft spots survive (see F4): "interposer" (unglossed) and
"sub-channel" (unglossed, but self-evident).

### 6. No stub / rhythm break — PASS (no finding)

No section is markedly short. §1 ¶3 is a single sentence, but it is the intentional
signature-line landing, not a stub.

### 7. Thesis not over-restated — MEDIUM (F2)

Core verdict asserted in exactly 3 sections (§1, §4, §6) — technically at the ≤3 limit — but
the closing section restates it internally to the point of circling (see F2).

---

## Findings

### F1 — MEDIUM — jargon-overdepth / attention-budget (§3, the tower)

**Verdict: yes (flag).** The single most likely stop point for the impatient investor. §3 is
where the essay goes deepest into hardware plumbing while the money payoff (§4, who-makes-HBM)
is still gated behind it. The insight §3 owes the reader is "a single back-end die doesn't
rival HBM, but a tall stack sized to HBM4 might." That insight is delivered — and then
over-spent on interconnect mechanics:

> "Traffic moves down the stack through what the patent calls TSV gutters: columns of
> through-silicon vias, the vertical wires punched straight through a die [0073]. Four gutters
> are cut into every die, each carrying the data for a pair of sub-channels [0034]."

and the FIG 1G caption doubles down on the same tile:
> "Eight sub-channels (161A to 161H) are divided by four vertical TSV gutters (162 to 165)..."

The four-gutters / pair-of-sub-channels mechanics are plumbing past the insight the money
thread needs; the reader who came for the stock take is two technical sections deep before §4
pays off. **Fix (cut / de-elaborate):** keep "the stack is wired by TSV gutters and funnels
I/O through a base die," cut the four-gutters-per-pair-of-sub-channels granularity from prose
(the FIG 1G caption already carries it). This tightens the wait to the §4 payoff. Not a hedge.

### F2 — MEDIUM — thesis-restatement / attention-budget in the payoff zone (§6)

**Verdict: yes (flag).** The verdict pays off the lead (see summary), but the closing circles.
"The cell is in the back-end" appears three times in five short paragraphs:
> ¶1: "...the memory cell is built in the back-end."
> ¶4: "...the cell still sits in the back-end..."
> ¶5: "The cell is in the back-end." (signature line 2 — protected)

and the foundry/who-makes-HBM beat is stated twice more (¶1 and ¶4) around the protected line:
> ¶1: "...let a logic-and-packaging maker carry HBM-class memory without owning a DRAM
> front-end."
> ¶4: "...a foundry can quote HBM-class memory as a line item. The tightest bottleneck in AI
> hardware would gain a fourth door."

with "fourth door" (¶4) / "fourth path" (¶5) echoing. The signature line (¶5) is exempt, so
the excess is the ¶1 restatement of the foundry beat, which §4 already made and ¶4/¶5 re-land.
An impatient reader at the finish notices the circling and the payoff dilutes. **Fix (cut):**
drop the ¶1 restatement of "logic-and-packaging maker carry HBM-class memory" (¶4's conditional
version + ¶5's signature carry it) so the core lands fewer times before the leaving-sentence.
Note §6 also carries the capacitor caveat (F3), compounding the closing's restatement load.

### F3 — LOW — caveat re-spent across three sections (capacitor relocation)

**Verdict: yes (flag).** The "relocated, not removed" caveat is stated three times:
> §2 (bold anchor, protected STRUCT-002 slot): "This is still a one-capacitor cell. The
> back-end move relocates DRAM's hardest part. It does not remove it."
> §5 (steelman): "It keeps the capacitor and merely moves it, where the more radical path
> deletes it."
> §6 (sanctioned anti-hype guard): "this is 1T1C, so the capacitor was relocated into the
> back-end rather than removed."

§2 (protected anchor) and §6 (the required single anti-hype guard per the closing directive)
are each doctrine-licensed; the discretionary instance is §5, which re-spends the §2 caveat.
Mitigant: §5 adds net-new content (the imec capacitor-less 2T0C contrast). **Fix
(de-elaborate / return to core):** in §5 lean on the imec contrast ("the more radical path
deletes the capacitor; imec's cell replaces it with two transistors") and let it reference
rather than restate "keeps the capacitor and merely moves it." Low because two of the three
instances are protected/required.

### F4 — LOW — un-glossed term of art (§4 caption; §3)

**Verdict: yes (flag).** "interposer" is used with no first-use gloss, in the FIG 1A caption:
> "A logic die (106) sits beside the high-bandwidth-memory stack (104), the two joined on a
> single interposer."

The impatient investor cannot decode "interposer" in one clause from context. "sub-channel"
(§3) is likewise unglossed but is self-evident (a sub-division of a channel), so it is the
weaker half. **Fix (add a one-clause gloss — calibration, not a hedge):** e.g., "a single
interposer, the silicon bridge that wires the two dies together." Low because it sits in a
caption and is not load-bearing to the money thread.

### F5 — LOW — strategic inference stated in the hook before its §4 label (§1 ¶1)

**Verdict: yes (flag).** The hook closes on the who-can-make-this-memory inference, in the
essay's own voice and unconditioned:
> "Move the cell to the back-end and you change more than a spec. You change where this kind
> of memory can be built."

§4 later owns this as labeled inference ("the leap is mine, not the document's") and §1 ¶3
conditions the strong form ("if the yield numbers land"), but ¶1's line is stated as flat
consequence and is firmer than the carefully-conditioned analysis it previews. A reader who
bounces after §1 carries the who-makes-HBM inference as if it were established. This is the
surface reading firmer than the body's own hedged evidence. **Fix (narrow / anchor to the
physical fact, NOT a hedge):** tie the hook line to the claim-word consequence rather than the
market consequence — e.g., "You change what kind of fab can build it" — which is the grounded
back-end/thin-film physical fact, not the who-makes-HBM leap. Grounding-fence compliant
(narrow, not disclaim).

### F6 — LOW — precision: stack-height conflated with footprint (§1 ¶1)

**Verdict: yes (flag).** 
> "The application says to stack those dies eight high to match the footprint of HBM4..."

The patent keeps these two things separate: "8-high and beyond" is stack height / capacity
`[0023]`, and "With the goal of matching HBM4's footprint" is the die/block X-Y area `[0034]`.
Footprint is area; stacking eight-high adds capacity/Z, not footprint. Linking them with
"eight high **to match the footprint**" is a minor technical conflation. An impatient investor
won't parse it, but it is a precision slip in the surface. **Fix (narrow):** separate the two,
e.g., "stack those dies eight high and size the block to HBM4's footprint." Not a hedge.

### F7 — LOW — mild meta / reader-orientation (§5, §6)

**Verdict: yes (borderline flag).** Two residual reader-orientation phrases survive after the
§4 exemptions:
> §5: "Read cold, the bear case is strong, and it should be put at full strength."
> §6: "Here is where this leaves an investor."

Both are mild and arguably functional (the §5 phrase asserts a claim — the bear case is strong
— then delivers it; the §6 phrase is a standard verdict-section signpost the impatient reader
may welcome). `gate_meta` presumably passed; these are judgment-level watches, not clear
violations. (Separately, §6 "The bounds set out above still hold" is the doctrine-sanctioned
"limits referenced, not re-listed" move and is NOT flagged.) **Fix (optional cut):** "The bear
case is strong" alone carries §5's transition; "the bear case is strong, and it should be put
at full strength" can lose the second clause. Low.

### F8 — LOW — external attribution not pinpointed (§5)

**Verdict: yes (flag).** A load-bearing rebuttal beat rests on a specific external claim whose
source is not identifiable in the Sources list:
> "In ZAM, the partner reported to actually fabricate the DRAM is Powerchip, not Intel."

The claim is correctly fenced as external reporting ("reported to") and does not read as the
patent's own claim, so it is not a grounding-fence violation. But it carries the §5 rebuttal's
"tell" ("that is what you would expect if the aim were a design-and-packaging capability"), and
the Sources block has no Powerchip-specific citation. **Fix (anchor / cut):** pinpoint the
source that reports Powerchip as the ZAM fabricator, or soften the load it carries. Low.

---

## Grounding spot-checks (results)

### Anchor verification — CLEAN

Only §2 and §3 carry `[dddd]` anchors (§1/§4/§5/§6 are framing/inference/pricing). Every
anchor in both anchored sections was checked against `input/patent.md`:

| Anchor | Essay use | Patent paragraph | Verdict |
|---|---|---|---|
| §2 [0018] | "Embodiments are directed to ultra high bandwidth memory (HBM) with backend transistors" | [0018] verbatim | clean |
| §2 [0069] | "Each memory die in the die stack includes one transistor one capacitor (1T1C) backend dynamic random access memory (DRAM)." | [0069] verbatim | clean |
| §2 [0031] | "thin-film-transistor layers stacked one atop another" | [0031] "first thin film transistor database 151... second thin film transistor database 153" | clean (support) |
| §2 [0027] | "can be an approximately 1.5 GB die based on back-end-of-line transistors" | [0027] verbatim | clean |
| §3 [0023] | "a memory cube stacked eight high and beyond" | [0023] "a die stacking cube is 8-high and beyond" | clean |
| §3 [0031] | "the silicon thinned to enable that many-layer stacking" | [0031] "thinning of the silicon can be implemented to enable many-layer stacking" | clean |
| §3 [0073] | "TSV gutters: columns of through-silicon vias..." | [0073] "a plurality of alternating sub-channels and through-silicon via (TSV) gutters" | clean (support) |
| §3 [0034] | "Four gutters are cut into every die, each carrying the data for a pair of sub-channels" | [0034] "four TSV gutters in each die, one carrying data and control for sub-channels 0-1..." | clean |
| §3 [0020] | "UCIe, or Universal Chiplet Interconnect Express..." | [0020] "high speed universal chiplet interconnect express (UCIe) connections" | clean |
| §3 [0034] | "spare memory arrays that can stand in for defective ones once the stack is bonded" | [0034] "redundant memory arrays (32 datablocks) to act as fungible recoverability resources for unrepairable defects" | clean |
| §3 [0034] | "to have a die capacity of 0.5-5 GB" | [0034] verbatim | clean |
| §3 [0034] | "With the goal of matching HBM4's footprint" | [0034] verbatim | clean |

No `[dddd]` anchor misfires. Captions (FIG 1B, 1F, 1A, 1G) also ground cleanly to
[0025]/[0031]/[0022]/[0033].

### Claim-scope vs Claim scope map — HONORED (strength, no finding)

- "The load-bearing word is backend" — matches map ("the single load-bearing claim word is
  'backend'").
- "Claim 1 says backend. It never says foundry, never says logic fab, never says without a
  DRAM fab" — matches map rule verbatim.
- §5 "It never names the channel material, never claims a logic-compatible process, never
  promises a yield" — matches map ("The channel MATERIAL is never named").
- "Claim 1, as filed, then requires..." — sought-locked vocabulary honored (no "Intel
  owns/secured").
- The who-makes-HBM / foundry inference is explicitly labeled ("the leap is mine, not the
  document's"). The locked/open/inference boundary is honored well. (The one place the label
  arrives late relative to the hook is F5.)

### Pins-not-bounds — HONORED (no finding)

- "approximately 1.5 GB" presented as "a size on one such die" (description), never as a claim
  pin.
- "0.5-5 GB" presented as a design target quote (description), never as a claim-1 lock.
- "eight high and beyond" tracks [0023]'s "8-high and beyond"; never asserted as a claim-1
  requirement. No description value is dressed as a claim bound, and no pin is dressed as a
  bound.

### Over-hedge / overreach (6G both directions) — CLEAN (no finding)

The verdict commits firmly on direction ("The direction is not in doubt"; "The one thing
claim 1 settles is that the memory cell is built in the back-end") and reserves numbers, with
no safe-harbor boilerplate. The strong strategic claims are conditioned ("if the yield numbers
land"; "If a back-end die matches HBM4... at a workable cost"). Neither over-hedged nor
overreaching. `gate_hedge` posture (measured) respected.

---

## Return summary

- **Top 3 findings:** F1 (MEDIUM, §3 TSV-gutter/sub-channel plumbing over-spent, money payoff
  gated behind it); F2 (MEDIUM, §6 verdict circles — "the cell is in the back-end" ×3, foundry
  beat ×2 around the protected signature line); F5 (LOW, §1 hook states the who-makes-HBM
  inference unconditioned, firmer than the §4-labeled analysis it previews).
- **Where the impatient investor most likely stops:** §3 ("A Tower Built to Match HBM4's
  Footprint") ¶1 — the deepest hardware plumbing (four TSV gutters per pair of sub-channels)
  with the who-makes-HBM payoff still one section away.
- **Does the verdict pay off the lead?** Yes. The lead promises "if yield lands, who can make
  HBM stops being a three-company club"; the verdict delivers "the architecture is settled
  (backend), the open question is yield, watch VLSI 2026 / ~2029" and hands over a clean,
  repost-safe leaving-sentence. It is evidence-proportionate in both directions — just
  slightly padded (F2).
