# Self-audit round 3 — Reader B (skeptical pro-subject reader)

- essay: handoff/03-edit/essay-final.md (draft_version 5, closing_posture: firm)
- persona: AI-infrastructure practitioner (systolic arrays, HBM, wafer-scale); hunting
  technical overclaim AND unearned hedging; application-vs-grant discipline is home turf
- sources read: essay-final.md, input/patent.md (full text + claims 1-42), input/essay-context.md,
  input/figures/fig-02.png, fig-05.png, fig-06.png, fig-07.png
- isolation honored: no edit-log, no revision-response, no score-history, no prior self-audit reports

## Pass-7 checklist (evidence-forced)

### 1. BLUF lead-altitude — YES (pass)
Para 1 opens declarative and lands the verdict in sentence 2-3: "Three years on, that
document is still not an asset. It is a pending application, still being argued with a
patent examiner, and pledged... as loan collateral." No deferred question. Severity: none.

### 2. Header-as-claim / overpromising headers — YES (pass)
Every `##` header is an assertion; header-only skim reconstructs the argument
(narrative-ahead-of-property-right → founders' bet in writing → combined array → switchless
memory interface → transformer-shaped rest → rejection/pledge/spend → roadmap-not-fence).
Checked for overpromise: "What Exists Today Is a Rejection, a Pledge, and Ongoing Spend" is
literally supported by the 2026-05 record sentence and the two reel/frame liens. No header
promises more than its section delivers. Severity: none.

### 3. Steelman present and correct — YES (pass)
Quoted span: "The strongest objection to the whole origin-document framing lands here, and
it deserves full strength. What is in writing is claim scope Etched has sought and failed to
obtain for three years... The broad combined-array claims, claim 1 and claim 26 as drafted,
sit closest to that art and are exactly the kind of claims that shrink in it. Three years of
prosecution have produced no enforceable claim at all. If the set narrows or dies, what
remains is a disclosure with a date on it, and a disclosure is not a moat."
This is a THIS-application objection (crowded examiner-cited field + claim-1/26 breadth +
zero allowed claims), not a generic truism, conceded at full strength, then refined without
being defanged: "The crowded-field objection survives contact and changes nothing about the
date." The refinement concedes the objection's whole force on value and retreats only to
what the objection cannot touch (date, inventors, disclosure content). Correct steelman
mechanics. Severity: none.

### 4. No meta posturing — YES (pass)
"The filing is still where the checking starts" is functional framing of the essay's
question, not reader-instruction. One continuity clause to the companion essay ("the subject
of an earlier analysis") is inside the essay-context allowance. Severity: none.

### 5. Jargon as signpost — YES (pass)
HBM, UCIe, systolic array, self-attention, layer normalization each get a one-clause gloss
and stop ("Universal Chiplet Interconnect Express, UCIe, a chip-to-chip standard"; "layer
normalization, a bookkeeping step that rescales values between stages"). No deep-dive past
the insight. Severity: none.

### 6. No stub / rhythm break — YES (pass)
Shortest body section ("The Rest of the 2023 Design...") carries ~4 paragraphs + figure
captions; no section markedly shorter than siblings. Severity: none.

### 7. Thesis not over-restated — YES (pass, borderline)
Core verdict (pending-not-asset / roadmap-not-fence) asserted in the lead, the "Both
Founders" section ("A patent application is not a patent"), and the verdict section — 3
sections; the §7 status sentence is the required prosecution label, evidence not assertion.
At the pass condition's edge but inside it. Severity: none.

## Deep claim audit (claims 1/15/26/39 + dependents vs claims text)

- **Claim 1**: essay quotes [0013] verbatim (checked word-for-word) and labels it "in its
  broadest form"; correctly notes UCIe/32 GT/s is "a description preference, not something
  claim 1 requires as drafted" — claim 1 recites only "chip-to-chip connections." Accurate.
- **Claim 26**: named with claim 1 as the "broad combined-array claims"; claim 26 adds only
  the grid-like arrangement — "broad" is fair. Accurate.
- **Claim 39**: essay's translation ("each memory channel is bonded, permanently, to its own
  column or columns of the array, and nothing can reroute it") matches "each of the
  plurality of channels is hardwired to respective one or more columns in the systolic array
  without any switching element." The [0016] summary quote is verbatim-present in patent.md
  and is indeed an almost-word-for-word mirror of claim 39 (claim: "channels, wherein each";
  summary: "channels where each"). "respective one or more columns" → "its own column or
  columns" preserves the one-or-more scope. Accurate.
- **Claims 7/8**: "Claims 7 and 8 put HBMs on that same switchless hardwiring, with claim 8
  asking for several per top-row chip" — claim 7: "HBMs are hardwired to respective columns
  ... without any switching element"; claim 8: "multiple HBMs are hardwired to each of the
  plurality of ICs in the topmost row." Accurate, and "asking for" is application-era.
- **Claims 11-13**: aux circuitry + local memory + no-access boundary. Claim 13 says "do not
  communicate with"; the essay quotes spec [0051] ("do not have access") with the
  embodiment marker "In this embodiment" kept inside the quotation. Consistent; the
  embodiment status travels with the quote. Accurate.
- **Application-era language**: "asks for," "the application claims, as drafted," "Etched is
  seeking," "sought." Grep-level read of the full essay finds zero grant-era verbs
  (locks/fences/requires-as-owned) applied to claim content. No sought-as-owned anywhere;
  the title itself carries "It Is Still Pending." Pass.
- **Independent-claim count**: "the application's four independent claims" — 1, 15, 26, 39.
  Correct.
- **AI-limitation statement**: "The broad combined-array claims carry no AI limitation as
  drafted, and neither does claim 39's memory interface" — verified: claims 1, 26, 39 recite
  no AI; the AI limitation enters at claims 6/12/15/40. Accurate and honest.

## Mechanism honesty (spec + figures, verified against the drawings)

- **Combined array / host view**: "appears to be one large array" [0028] verbatim. FIG. 2
  caption checked against fig-02.png: ICs 215A-215I present, memory chips 210A-210C top row
  only, host 205 over PCIe 240, connections 225/230, dashed boundary 250. Caption accurate.
- **Directionality**: essay does not assert the bidirectional/unidirectional embodiment of
  [0029] as claim scope; it uses [0029] only for the 225/230 numerals. Safe.
- **Top-row feed / weight reuse**: "adding more rows of chips adds compute without adding
  memory chips at the top [0039]" — matches [0039] ("data fed from the memory chips 305 is
  reused across the rows"). Accurate; also correctly used to cover dropped FIG. 3/4.
- **FIG. 5 (header)**: caption checked against fig-05.png: two memory chips 505A/505B above
  one IC 215, channels 510A-510D, wires 520, columns 515A-515D inside array 220; channel-to-
  column mapping matches [0044] exactly. "No switch, no crossbar, nothing between memory and
  math" is [0043]/[0045]-supported. Accurate.
- **FIG. 6**: caption checked against fig-06.png: ICs 615A-615D, each with 605 block + 220
  tile; local memories 610A-610D attach only to the 605 blocks. Matches [0051] embodiment,
  which the body quotes with its embodiment marker. Accurate.
- **FIG. 7 / Time A/B**: caption checked against fig-07.png + [0056]/[0057]. Legend order
  (Attention: Queries/Keys/Values, Projection, MLP Hidden/Output) matches "Attention
  queries, keys, and values, projection, and the MLP layers." Time A: [0056] has DPU 0 on
  MLP output layer while DPU Y still drains the hidden layer — caption's "a new computation
  has already entered while the previous one drains" is exact. Time B: [0057] "This is shown
  at Time B where the array stalls" — the figure shows one hatched stall band at Time B;
  "the only idle gap" matches the drawing. The essay wisely does NOT quantify the stall
  length (the spec is internally inconsistent there, X vs Y cycles). 98% figure is quoted
  with the spec's own conditionality ("can still be"). Accurate.
- **Pinned values not described as bounds-as-achieved**: "more than 1 TB/s" quoted inside
  [0040]'s "can enable"; "up to 32 GT/s" quoted; "128×128" rendered as "top out at" (= "at
  most"); "98% or greater" quoted under "can still be." None presented as achieved
  performance or as claim scope. Pass.

## External-fact fencing

- **Collateral discipline** — honored verbatim: "Both liens are blanket over the portfolio
  at signing, with no selectivity about any single filing, so they say nothing about this
  application in particular." Reel/frames (067204/0877, 071792/0869) and effective dates
  match the brief. The cuts-both-ways frame (bankable asset class vs creditor's reach) is
  the brief's honest frame, rendered without hedging the verdict.
- **ONE prosecution label** — exactly one status sentence ("As of the 2026-05 record, the
  application is pending, with examination continuing after a final rejection... and a
  request for continued examination..."), carrying all required content; no office-action
  chronology anywhere in the body (the 2024-11/2025-07 non-finals are correctly absent).
- **Motive-as-inference** — "reading them as a lender sweeping fresh assets into its
  collateral is an inference, not a record." Three-days-earlier interval stated as dates,
  labeled. Family observation labeled bibliographic and "proves nothing by itself about
  intent." All fenced correctly.

## Over-hedge symmetric check (6G)

Closing posture is firm and the call leads: "Hold the July 2026 thread against the May 2023
filing and the verdict is firm." Exactly one patent-specific anti-hype guard ("broad claim
1... is the part of this filing likeliest to shrink or die"), explicitly framed as scoping
"without softening." "A patent application is not a patent" (§2) is edition-defining
scaffolding for this pending-application analysis, not a verdict-section safe-harbor — and
it is immediately converted into instruction ("the honest verbs... application-era verbs"),
not left as a dodge. Precision labels ("On claim structure alone," "bibliographic
observation," "inference, not a record") each name their evidence basis rather than retract
the claim — none reads as a dodge. The verdict is NOT safer than the body's evidence: the
body earns "origin record + roadmap in formation + best-candidate claim 39 + likeliest-to-
shrink claim 1," and the conclusion asserts exactly that. No 6G finding.

## Findings

### sa3B-F1 — mechanism gloss beyond the anchor — LOW
Check: mechanism honesty / grounding. Verdict: minor unanchored extrapolation.
Quoted span: "There is no program counter to redirect and no scheduler to negotiate with."
[0027] says only "does not take instructions at runtime, and only executes instructions in
a preset loop" — the spec never mentions a program counter or scheduler. The inference is
technically sound and sits directly after the correctly labeled embodiment quote, but it is
the essay's own hardware claim wearing the quote's authority.
Fix (fence-compliant): anchor-adjacent labeling, e.g. "which is to say: no program counter
to redirect..." making it visibly a gloss of the quoted sentence — or cut the sentence.

### sa3B-F2 — embodiment identity stated as flat fact — LOW
Check: mechanism honesty / embodiment discipline. Verdict: embodiment detail un-marked.
Quoted span: "Identical chips (215) tile a package (201)." [0028]: "In one embodiment, the
ICs 215 are all identical." Claim 1 does not require identical ICs. The paragraph's
breadth guard ("not something claim 1 requires as drafted") names only UCIe, so the
identity detail rides unguarded.
Fix: narrow the phrasing ("Identical chips, in the described embodiment, tile a package")
or extend the existing guard to cover the paragraph's embodiment details generally.

### sa3B-F3 — anchor imprecision on numeral 250 — LOW
Check: grounding spot-check (anchor vs cited paragraph). Verdict: anchor supports the
concept but not the numeral.
Quoted span: "join neighboring tiles until they compute as one combined systolic array
(250) [0019]." [0019] contains "form a larger, combined systolic array" but no numeral 250
and no neighboring-tile language; those live in [0025]/[0028]-[0029]. The claim is true and
one paragraph-hop verifiable.
Fix: re-anchor to [0028] (or add [0025]) for the numeral-bearing clause.

### sa3B-F4 — claim 15 folded loosely into the "switchless" family — LOW
Check: deep claim audit / scope framing. Verdict: family framing slightly over-groups.
Quoted span: "The claim set builds a family around the idea. Claims 7 and 8 put HBMs on
that same switchless hardwiring... Claim 15 frames the system version, an AI accelerator
whose memory chips, coupled to the ICs forming the top row, store the model's weights
[0014]." Claim 15 as drafted requires only "coupled" memory — the switchless limitation in
the system family arrives at dependent claim 19, which the essay never mentions. The
sentence itself honestly uses the claim's word ("coupled"), so the risk is confined to the
"family around the idea" umbrella, but a pro reader notices the strongest system-level
switchless claim (19) goes uncited while claim 15 stands in for it.
Fix: narrow ("Claim 15 frames the memory-fed system version — the switchless variant of it
is dependent claim 19") or cite claim 19 alongside.

## 5-sample grounding spot-check (all verified verbatim against input/patent.md)

1. [0013] claim-1 summary quote — verbatim match. PASS
2. [0018] "it is unreasonable to expect a single chip to interface with 100s of GB of
   memory used to store parameters and intermediate computation values" — verbatim. PASS
3. [0043] "a switch (or some kind of switching element such as a crossbar) is typically
   used so that the device can access the entire memory of the HBM" — verbatim. PASS
4. [0045] "hardwiring the memory chips 505 to the columns 515 is permissible" + "which can
   save space and power" — verbatim; and the essay's bolded claim that the 2023 filing books
   the gain as space-and-power ONLY (no latency word) is confirmed: [0043]-[0045] contain no
   latency benefit. The "Latency is the word the 2026 thread added" contrast is grounded. PASS
5. [0047] "self-attention operations use data computed from previous tokens, which means
   such data should be saved" + "Most of the parts of a transformer AI model do not use data
   from previous tokens" — both verbatim. PASS

## Persona verdict

As a practitioner I came in expecting the two classic sins — a pending application dressed
up as a moat, or a verdict hedged into "patents don't guarantee products" mush — and this
essay commits neither: the sought-vs-owned discipline holds in every sentence I checked, the
mechanism story (combined array, top-row feed, switchless channel-to-column, Time A/B
pipelining) matches the spec and the actual drawings, and the space-and-power-vs-latency
catch is the kind of detail only someone who read [0045] would land. The one sentence I
would attack is "On claim structure alone, it is the best candidate to survive in some form
among the application's four independent claims" — narrowness is not novelty, the rejection
record is not parsed per-claim, and weight-stationary arrays with dedicated channel feeds
have prior-art neighbors the essay cannot see — but the sentence pre-concedes exactly that
basis with its own label, so it survives the attack it invites.

## Summary

- Findings: 0 critical, 0 high, 0 medium, 4 low (sa3B-F1..F4)
- All 7 pass-7 checklist items: PASS
- Deep claim audit: PASS (one low framing note, sa3B-F4)
- Grounding spot-checks: 5/5 verbatim PASS; figure captions verified against fig-02/05/06/07
- Over-hedge check: no finding; verdict is evidence-proportionate in both directions
