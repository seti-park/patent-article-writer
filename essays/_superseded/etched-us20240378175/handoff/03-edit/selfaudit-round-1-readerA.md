# Self-audit round 1 — Reader A (impatient investor)

- essay: handoff/03-edit/essay-final.md (draft_version 3, closing_posture: firm)
- persona: curious retail investor per `_shared/references/reader-profile.md`; 6 minutes;
  captions before body; came from the Etched stealth-exit thread
- reviewer isolation honored: no edit-log, no revision-response, no score-history, no other
  reader output consumed
- checks: pass-7 items 1-9 + grounding spot-checks (claim scope, anchors, pinned values)
- finding ids: sa1A-F*

## Checklist results

### 1. BLUF lead-altitude — verdict YES (pass)

Para 1 carries a declarative verdict, not a deferred question:

> "Three years on, that document is still not an asset. It is a pending application, still
> being argued with a patent examiner, and pledged alongside the rest of the company's
> patent stack as loan collateral."

The title itself is the verdict ("...It Is Still Pending."). As the impatient reader I had
the call before the first figure. No finding.

### 2. Header-as-claim — verdict YES (pass)

Every `##` header is an assertion, and header-only skim reconstructs the argument:
"The Narrative Is Three Years Ahead of the Property Right" → "Both Founders Put the Bet in
Writing in May 2023" → "Many Small Arrays, Presented to the Host as One" → "The Application
Claims a Memory Interface With No Switch in It" → "The Rest of the 2023 Silicon Is Already
Transformer-Shaped" → "What Exists Today Is a Rejection, a Pledge, and Ongoing Spend" →
"A Dated Roadmap the Company Keeps Funding, Not Yet a Fence". Filler: NONE.

### 3. Steelman present — verdict YES (pass)

THIS-application objection, conceded at full strength, then refined — not a generic truism:

> "The strongest objection to the whole origin-document framing lands here, and it deserves
> full strength. What is in writing is claim scope Etched has sought and failed to obtain
> for three years. The examination record lists 8 references, all examiner-cited ...
> The broad combined-array claims, claim 1 and claim 26 as drafted, sit closest to that art
> and are exactly the kind of claims that shrink in it. Three years of prosecution have
> produced no enforceable claim at all."

Refinement lands in the verdict: "The crowded-field objection survives contact and changes
nothing about the date." Specific claims named, specific art field named. No finding.

### 4. No meta posturing — verdict NO (finding sa1A-F4, low)

Two spans, both borderline-to-real:

- Body: "The claim language, **mirrored in the citable summary**, reads:" — "the citable
  summary" is pipeline vocabulary, not reader vocabulary. A retail reader does not know
  what a "citable summary" is or why the anchor is [0016] rather than the claim number;
  the phrase reads as the essay explaining its own sourcing process.
- The `# Footnotes` annex references internal artifacts by name: "per figure-selection.md
  cover note", "fact-check-log `etched-thread-2026-07`", "quote chain is thread →
  input/essay-context.md → essay", "per the run's label-sentence budget". None of the
  `[^...]` markers are referenced anywhere in the body text. If this annex ships to X
  Articles as-is, it is a meta-leak of the production system into the deliverable; if it is
  stripped by `strip_publication.py`, the finding reduces to the "citable summary" phrase
  only. Severity low, conditional as stated.

### 5. Jargon as signpost — verdict NO (finding sa1A-F3, low)

First reader-profile-breaking term for a captions-first reader: the header caption uses
"systolic array (220)", "IC (215)", and "claim 39" cold — the body gloss ("a grid of small
calculating cells") arrives two sections later. Within the body proper, the breaking terms
are:

- "layer normalization" — used twice ("Even with a stall for layer normalization" [§5 body]
  and "the layer-normalization stall, marked at Time B" [FIG. 7 caption]) with no one-clause
  gloss. Reader-profile rule 1 requires a gloss on first use; this is the one term I hit
  where I had no handle at all.
- Secondary, below the flag line on their own: "PCIe (240)" (first use in the FIG. 2
  caption, unglossed), "32 GT/s" (inside a verbatim quote; magnitude never landed on a
  familiar scale, contrast the well-handled "1 TB/s ≈ a full laptop drive per second"),
  "reel/frame 067204/0877" (functions as a citation, but a two-word gloss would help).

Jargon-OVERDEPTH: NONE — glosses that do exist ("the examiner's formal no", "a paid restart
that keeps the argument alive", "a lender's collateral claim", "the ones that stand on their
own rather than adding to another") are exactly one clause and stop at the insight.

### 6. No stub / rhythm break — verdict YES (pass)

Sections run 3-5 paragraphs each; no section is markedly shorter than its siblings. The
single bolded paragraph in §4 is an emphasis beat, not a stub section. NONE.

### 7. Thesis not over-restated — verdict NO (finding sa1A-F1, medium)

Pass condition is core verdict asserted in <= 3 sections. I count 4 sections plus the title:

1. Title: "Etched Filed the Memory Half of Its Story in 2023. It Is Still Pending."
2. §1: "The memory half of Etched's architecture story has been in writing since
   10 May 2023 ... Three years on, that document is still not an asset."
3. §2: "Etched is seeking these claims, as drafted, and has been paying to seek them for
   three years."
4. §4 (bolded standalone paragraph): "**The memory half of the no-middlemen story is not a
   2026 slogan here. It is claim language Etched has been asking the patent office for
   since May 2023.**"
5. §7: "The philosophy was in writing by May 2023 either way."

Each recurrence adds a modifier (pledge, spend, rejection), so the drum is partly designed —
but as the impatient reader I registered "you already said this" precisely at the §4 bold,
which is near-verbatim with the title and with §7. This is a taste-level check; my vote is
FLAG. Severity medium (explicit pass-condition breach; mild reader-facing drag).

## Grounding spot-checks (3 sections sampled: §3, §4/§5, §7; every anchor in each checked)

| # | Essay span (anchor) | Patent span | Verdict |
|---|---|---|---|
| 1 | "top out at 'floating point systolic arrays with a size of 128×128' [0018]" | [0018] "Currently, most chips have, at most, floating point systolic arrays with a size of 128×128." | HOLDS |
| 2 | "'it is unreasonable to expect a single chip to interface with 100s of GB of memory...' [0018]" | [0018] verbatim | HOLDS |
| 3 | "'does not take instructions at runtime, and only executes instructions in a preset loop' [0027]" | [0027] verbatim | HOLDS |
| 4 | "adding more rows of chips adds compute without adding memory chips at the top [0039]" | [0039] "adding more rows of ICs 215 increases the compute power ... without having to add more memory chips 305 at the top ... data fed from the memory chips 305 is reused across the rows" | HOLDS |
| 5 | "'supports up to 32 GT/s' [0030]; That is a description preference, not something claim 1 requires as drafted" | [0030] verbatim; claim 1 carries no UCIe/rate limitation | HOLDS |
| 6 | Claim-39 blockquote anchored [0016] ("...hardwired to respective one or more columns in the systolic array without any switching element") | [0016] verbatim (summary mirror of claim 39; claim 39 text matches) | HOLDS |
| 7 | "'a switch (or some kind of switching element such as a crossbar) is typically used...' [0043]" | [0043] verbatim | HOLDS |
| 8 | "'can save space and power' [0045]; 'hardwiring the memory chips 505 to the columns 515 is permissible' [0045]" | [0045] verbatim | HOLDS |
| 9 | "'can enable the memory chips 305 to transmit more than 1 TB/s of data to each of the ICs' [0040]" | [0040] verbatim (truncated before "215 in the topmost row"; essay gloss "into each top-row chip" preserves it) | HOLDS |
| 10 | "'self-attention operations use data computed from previous tokens...' [0047]; 'Most of the parts of a transformer AI model do not use data from previous tokens' [0047]" | [0047] verbatim | HOLDS |
| 11 | "'In this embodiment, the local systolic arrays 220 do not have access to the local memory chips 610.' [0051]" | [0051] verbatim — and quoting "In this embodiment" honors the spec's own scope ([0051] later allows the opposite in other examples) | HOLDS |
| 12 | "'98% or greater utilization of the systolic array' [0057]; the layer-normalization stall at Time B" | [0057] verbatim; stall description matches | HOLDS |
| 13 | Header caption channel/column mapping (510A-D → 515A-D via wires 520) [0044] | [0044] mapping matches element-for-element | HOLDS |
| 14 | §7 "or the set narrows **again** or dies" | Record in evidence: two non-final actions, final rejection, RCE — refusals, not a documented narrowing. "again" asserts a prior narrowing that is not in the cited record; §6 itself uses the clean form ("If the set narrows or dies") | STRETCHES → sa1A-F2 |
| 15 | §4 translation: "each memory channel is bonded, permanently, to **its own column** of the array" | Claim 39 / [0016]: "hardwired to respective **one or more columns**" — the translation renders a one-to-one-or-more mapping as strictly one-to-one; the verbatim quote two sentences later mitigates | STRETCHES → sa1A-F6 |

Claim-scope language: application-era verbs held everywhere I checked ("asks for", "as
drafted", "sought", "seeking"); grant-era language appears only for the actually-granted
US 12,361,091 B1, correctly. Independent-claim count ("four independent claims") verified:
claims 1, 15, 26, 39. Pinned values are never converted to bounds: "up to 32 GT/s",
"more than 1 TB/s", "98% or greater", "at most ... 128×128" all keep the patent's own
directionality. Lien discipline honored ("Both liens are blanket over the portfolio at
signing ... they say nothing about this application in particular"); the three-days-later
motive reading is explicitly labeled "an inference, not a record". Prosecution status:
exactly one label sentence found ("As of the 2026-05 record, the application is pending,
with examination continuing after a final rejection ... and a request for continued
examination ..."); later mentions are analytic reuse, no office-action chronology — the
essay-context contract is met.

## Findings

### sa1A-F1 — thesis-restatement-redundancy — MEDIUM
- check: 7 · verdict: no (asserted in 4 sections + title, > 3)
- evidence: title; §1 "still not an asset"; §2 "has been paying to seek them for three
  years"; §4 bold "**...claim language Etched has been asking the patent office for since
  May 2023**"; §7 "The philosophy was in writing by May 2023 either way."
- note: the §4 bolded paragraph is the near-verbatim echo of both title and §7. Taste-level
  check — this is one vote for the multi-vote.

### sa1A-F2 — grounding (unsupported prior-event implication) — MEDIUM
- check: grounding spot-check #14 · verdict: STRETCHES
- evidence: §7 "or the set narrows again or dies" vs. the cited record (rejections + RCE;
  no documented narrowing). §6 already carries the supported form "If the set narrows or
  dies."
- recommended fix class (jurisdiction fence respected): NARROWER claim — drop "again"
  (i.e., "or the set narrows or dies"). Not a hedge; the verdict stands unchanged.

### sa1A-F3 — jargon-gloss gap — LOW
- check: 5 · verdict: no
- evidence: "layer normalization" unglossed at both uses (§5 body, FIG. 7 caption);
  header caption uses "systolic array (220)" / "claim 39" before any gloss for a
  captions-first reader; secondary: PCIe (FIG. 2 caption), "32 GT/s", "reel/frame".
- fix class: one-clause gloss at first body use of "layer normalization"; optionally a
  two-word handle in the FIG. 2 caption for PCIe.

### sa1A-F4 — meta-reader-instruction / process leak — LOW
- check: 4 · verdict: no
- evidence: "mirrored in the citable summary" (pipeline vocabulary in reader-facing prose);
  Footnotes annex names internal artifacts ("figure-selection.md", "fact-check-log
  `etched-thread-2026-07`", "input/essay-context.md", "the run's label-sentence budget")
  and its markers are never used in the body.
- conditional: if `# Footnotes` is stripped at publication, only the "citable summary"
  phrase remains in scope. Fix class: rephrase ("mirrored word-for-word in the filing's
  own summary [0016]") / confirm annex stripping.

### sa1A-F5 — caption carries no claim for the caption-first skimmer — LOW
- check: 2/6 adjunct (caption altitude) · verdict: no for FIG. 1 only
- evidence: "*FIG. 1: a systolic array, logically.*" — every sibling caption carries the
  argument (FIG. 5: "No switch, no crossbar, nothing between memory and math"; FIG. 6:
  "division of labor"); FIG. 1's tells the skimmer nothing, and it sits below the body
  paragraph it depends on.
- fix class: one-clause claim in the caption (e.g., what enters top vs left, what a bigger
  grid buys).

### sa1A-F6 — claim-scope translation narrower than claim text — LOW
- check: grounding spot-check #15 · verdict: STRETCHES
- evidence: "each memory channel is bonded, permanently, to its own column" vs claim 39
  "respective one or more columns"; header caption likewise "a dedicated column".
- mitigation: verbatim quote is adjacent both times. Fix class: precise gloss ("its own
  column, or its own small set of columns") — a narrower-sentence fix, not a hedge.

## Check 8 — persona verdict

- Stop-point (closest to bailing): the composition paragraph in §3 — "Identical chips (215)
  tile a package (201), each holding its own small array (220). Horizontal connections
  (230) and vertical connections (225) join neighboring tiles..." — five reference numerals
  and a standards acronym (UCIe, "32 GT/s") in four sentences. The section-closing money
  hook ("this is a machine you build when one workload ... deserves its own dedicated
  hardware") pulled me back; I did not bail.
- Did the essay ever let me forget this is a pending application, not a patent? No — the
  opposite: the pending drumbeat is the over-restatement in sa1A-F1. And it made me care
  anyway: "origin record, both founders' signatures, still paying, already pledged" is a
  concrete investor object, not a shrug.
- Question I leave with: if broad claim 1 dies and only claim 39 survives narrow, does the
  granted wiring patent cover what actually ships in the summer-2026 racks? (A fair
  leave-with question — it points at the companion essay, not at a gap in this one.)
- Share: YES. The verdict is a call, not a hedge; FIG. 5 is a story I can retell in one
  sentence; "The racks are shipping, the company says. The paper is still asking." is the
  line I would quote-post.

## Check 9 — over-hedge symmetric check — verdict NONE

- Verdict section leads with the call, unqualified: "Hold the July 2026 thread against the
  May 2023 filing and the verdict is firm."
- No safe-harbor boilerplate in the close; the one generic-adjacent line ("A patent
  application is not a patent", §2) is the required edition discipline, sits in the body
  not the verdict, and is immediately made specific ("the claims in it can shrink or die").
- Exactly one patent-specific anti-hype guard, as required: "broad claim 1 ... is the part
  of this filing likeliest to shrink or die."
- Pending status is not used as a crutch to avoid a call — the essay commits to specifics a
  hedger would not: "the likeliest survivor among the application's four independent
  claims" (claim 39) and a named falsifier already on the docket.
- Reverse (6G) check: the conclusion is not safer than the body's evidence — the body's
  strongest material (origin date, founder inventorship, switchless interface in claim
  language) is fully spent in the verdict. NONE.

## Totals

- critical: 0 · high: 0 · medium: 2 (sa1A-F1, sa1A-F2) · low: 4 (sa1A-F3, F4, F5, F6)
- Additive only; no gate, pass, or acceptance-bar relaxation suggested.
