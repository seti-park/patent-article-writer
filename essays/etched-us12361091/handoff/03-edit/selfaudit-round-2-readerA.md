# Self-audit round 2 — Reader A (impatient investor)

- essay: handoff/03-edit/essay-final.md (draft_version 3, closing_posture: firm)
- persona: impatient investor (reader-profile tier; 6 minutes; skims headers, reads captions
  before body; allergic to hype and lawyer-speak)
- blind protocol honored: no edit-log, no revision-response/notes, no score-history, no
  round-1 or other round-2 reports read
- sources consulted: essay-final.md, input/patent.md, input/essay-context.md,
  handoff/01-design/invention-summary.md (Claim scope map only), input/figures/fig-07C.png,
  fig-07A.png, fig-06.png, reader-profile.md, pass-7 checklist
- finding ids: sa2A-F1 .. sa2A-F5 (ADD-only; no gate, pass, or acceptance-bar relaxation
  proposed)

## Checklist (evidence-forced)

### 1. BLUF — verdict in paragraph 1?

**Verdict: YES (pass).** Paragraph 1 carries the declarative call, both halves:

> "Half of the loudest architecture claim in the thread already has a granted US patent
> standing behind it. The other half, the shared memory pool that gives Cluster-Scale
> Memory its name, has no granted substance in the filings you can read today. That split
> is the story, and the claims make it checkable."

No deferred question, no throat-clearing. The title ("Etched Patented the Wiring Half of
Its Memory Story, Not the Memory") already states the verdict before paragraph 1.
Severity: none.

### 2. Headers-as-claims — argument visible from headers alone?

**Verdict: YES (pass). Filler headers: NONE.** The seven body headers, read in sequence,
reconstruct the argument:

1. "The Memory Story Has a Checkable Half"
2. "A Structure Patent Etched Keeps Paying to Extend"
3. "Every Chip Reaches Every Chip Without a Switch"
4. "The Wiring Schedules the Traffic"
5. "The Description Aims It at Transformer Decoding"
6. "No Latency Number, No Memory Claim"
7. "One Leg Substantiated, One Leg Absent"

Every header is an assertion; the header-only skim yields: checkable half → company is
fencing it → what the wiring does → how it schedules traffic → what it's aimed at → what
is missing → verdict. Severity: none.

### 3. Steelman — strongest THIS-patent objection, conceded then refined?

**Verdict: YES (pass).** Section 6 opens with a patent-specific objection at full
strength, not a truism:

> "The objection an informed reader should press lands at full strength. Claim 1 recites a
> wiring pattern and nothing else. The description says the channels realizing it can be
> PCIe, SPI, ethernet, UCIe, or other wired or optical links [0134], the ordinary buses
> commodity hardware already uses ... A topology-only claim over standard link
> technologies is a thin moat for a 'proprietary ultra-low-latency, high-bandwidth
> interconnect'."

It is conceded with teeth (design-around named: "a rack that keeps its networking switch
... sits outside claim 1, and the scheduling claims (8, 9, 11) bind only traffic routed
the claimed way, a firmware choice") and then refined without retreat ("The granted fence
is not the adjective. It is the discipline underneath it"). This is grounded in the actual
claims (1, 5, 8, 9, 11) and [0134]/[0133] — not "patents don't guarantee products."
Severity: none.

### 4. Meta / scaffolding leakage

**Verdict: borderline — one candidate span.** → finding sa2A-F1... see sa2A-F4.

> "The boundaries set out above scope that call. They do not soften it."

"Set out above" is an essay-self-reference (the essay talking about its own preceding
text). Its function is exactly the scope-disclaimer the closing discipline mandates
(limits as boundaries, not counterweights), so it plausibly falls under the pass-7
functional-scope exemption — but it is the only sentence in the piece that is about the
essay rather than the patent, and to this persona it reads faintly lawyer-adjacent.
Logged as **sa2A-F4 (low)** for multi-vote. No other candidates: "The document to check is
US 12,361,091 B1" is functional (tells the reader which document), and "Hold the thread
against the grant..." is an idiom of comparison, not a reader instruction.

### 5. Jargon depth — first reader-profile-breaking term

**Verdict: one break found.** → finding **sa2A-F1 (low)**, section 4:

> "The description works the optimum once: 'When the number of processing devices is 8,
> p=4.35235, q=1.83809.' [0061]"

Why it breaks: p and q are never defined in the essay (the patent defines them at [0061]
as parallelism of input/output); the reader-profile says the audience is "NOT [comfortable]
with equations ... or unglossed terms of art" and rule 1 requires a one-clause gloss on
first use. The follow-up sentence translates p ("the whole input matrix lives spread
across four of the eight chips") but never translates q=2, so the raw symbols land
unassisted. It costs a beat, not a bail-out — the surrounding insight ("No link runs hot")
survives without parsing it. Severity: low. Suggested fix class: one-clause gloss of what
p and q count, or demote the raw figures to the derived-counts footnote and keep "the
description works the optimum once: four chips of eight carry the whole input matrix" in
body.

Secondary (below finding threshold, recorded for multi-vote context):
- "self-attention (QKV generation and attention computation)" — "QKV" unglossed at first
  use (section 5); tolerable because it is a stage-name in a list and Q/K/V reappear only
  as "matrices ... processed as tiles."
- "scale-up domain" — first appears inside the thread quote (verbatim source text, exempt);
  the essay's own-voice reuse in section 7 ("the scale-up domain becomes inspectable") is
  implicitly glossed by apposition to "The racks can. The company says its first systems
  ship in summer 2026. When they do..." No finding.

### 6. Stubs / restatement / rhythm break

**Verdict: NONE.** Section lengths run 3-7 paragraphs with no section markedly shorter
than its siblings; the closing section (3 paragraphs) is proportionate for a verdict
section. The single-sentence bold paragraph ("**Structure is what an apparatus claim can
lock, and structure is exactly what this one locks.**") is a deliberate pivot inside
section 6, not a stub section. No copy-paste restatement found; the closing line ("The
thread sells a memory story. The granted record holds a wiring story.") is a bookend of
the title, not a duplicate span.

### 7. Grounding spot-checks (six samples, six different sections)

Method: essay claim vs the cited paragraph in input/patent.md and the granted claims
(patent.md lines 931-977); Claim scope map (invention-summary.md) checked for
locked/open/pinned discipline.

| # | Section | Essay claim (span) | Patent evidence | Verdict |
|---|---|---|---|---|
| A | S1 lead + S3 | "two sets, every cross-set pair directly wired, nothing wired inside a set [0386]. Any chip can reach any other through at most one chip in between [0387]" ; "four or more a side under the granted claim" | [0386]/[0387] verbatim match; claim 1: "a first set of four or more ... and a second set of four or more"; blockquote in S3 is verbatim [0386]/claim-1 text | **HOLDS** |
| B | S2 | "The specification enumerates three example families, methods, topology, and AI-model computation [0336], [0337], [0384], [0418], and the claims granted here track only the topology family" | [0336] numbered-example convention; [0337] "Example 1 may include method of performing tensor operations"; [0384] "Example 2 may include a tensor parallel group"; [0418] "Example 3 may include method of performing computations for artificial intelligence models"; granted claims 1/14/18 are all group/topology | **HOLDS** |
| C | S3 | payoff quote "may be used to reduce data sharing ... and thereby help to reduce a processing time" [0124]; relay "may begin forwarding data before it has finished receiving it" [0143]; 16-vs-28 count | [0124] verbatim; [0143] "may send the received data to the third processing device A2 before all the data from the first processing device A0 is received"; 16-vs-28 explicitly labeled "both counts read off the figure, not numbers the patent states" (labeled analysis, honored) | **HOLDS** |
| D | S4 | blockquote [0140] exclusivity; "Which physical family carries which is the description's worked example rather than a claim requirement, with gather traffic on the first channels and reduction traffic on the second [0140]" | [0140] blockquote verbatim incl. spacing; [0140] "the first operation may be a data gather operation and the second operation may be a data reduction operation"; note claim 11 assigns reduction to the FIRST sub-operation — the essay's description-vs-claim split is exactly right | **HOLDS** |
| E | S5 | [0251] "large language model or a transformer decoder"; [0313] "four times the depth of the transformer model" + bandwidth-or-time framing; [0278] blockquote; [0267] "without rejoining the tiles..." | all four verbatim in [0251], [0313], [0278], [0267] | **HOLDS** |
| F | S6 | link-tech list [0134]; separate dies + optional shared memory [0133]; memory 630 role quote [0119]; "[0385] two or more" vs claims 1/14 "four or more"; claim 18 structure ("keeps the two-or-more floor but pays for it in structure"); claim 5 "equal bandwidth ... not high bandwidth" | [0134] lists PCIe/SPI/ethernet/UCIe/optical; [0133] both; [0119] verbatim; [0385] "two or more" vs claims 1/14 "four or more" confirmed; claim 18 = two-or-more + four groups + dual channel families + per-family exclusivity ("at least the dual-family pattern" is accurate — hop bound is dependent claim 22); claim 5 = "a same data bandwidth" | **HOLDS** |
| G | S2 | "every claim pursues one idea: how the chips of an AI cluster should be wired to each other" | No claim mentions AI (claims 1-23 verified; essay's own S5: "AI, transformers, and inference are absent from the claim language"). "AI cluster" imports the description's aim into a claims characterization | **STRETCHES** → sa2A-F5 |

**Claim scope map discipline:** locked/open/pinned honored. Pins = none in the map, and no
value is described as a bound: p/q presented as the description's worked optimum, "four or
more" as the granted floor, "eight chips" always as the drawings' example (dependent claim
13 never misattributed to claim 1). The [0140] gather/reduction physical assignment is
kept as description, not claim — the trickiest scope trap in this patent, handled
correctly. Figure captions verified against fig-07C, fig-07A, fig-06: set membership,
left/right placement, no intra-column wires, and FIG. 6's memory-630 box all match.

**sa2A-F5 (low, grounding/claim-scope, STRETCHES).** S2: "every claim pursues one idea:
how the chips of an AI cluster should be wired to each other." The claims never mention
AI; the essay itself says so three sections later. The "one idea = wiring" half is
accurate; the noun "AI cluster" is the description's aim, not the claims'. Fix class:
**narrow** — e.g. "how the chips of a cluster should be wired to each other" or "an
accelerator cluster" (patent-vocabulary: a tensor parallel group). Not a hedge; do not
touch the verdict.

### 8. Persona verdict (impatient investor)

- **Where I'd slow down/skim (not stop):** section 4's numeral-dense middle —
  "The first communication channels (730) pair the groups straight across, 712a with 712c
  and 712b with 712d [0138]. The second communication channels (740) run the criss-cross:
  712a with 712d, 712b with 712c [0139]." Four reference numerals per sentence is the one
  homework-feeling stretch; the verbal handles ("straight across", "criss-cross") and the
  payoff lines ("Reduce and gather stop taking turns", "No link runs hot") pull me
  through, and the next headers ("No Latency Number, No Memory Claim") promise the answer
  I came for, so I skim rather than bail. Logged as **sa2A-F2 (low)**.
- **I would NOT stop reading.** The BLUF pays out in paragraph 1 and the money thread
  ($1B contracts vs $800m raised, "paying to keep all three alive", term to October 2044,
  racks inspectable summer 2026) resurfaces in every non-mechanism section.
- **Question I leave with:** "When the racks ship in summer 2026, who actually opens one
  and checks the wiring against claim 1 — and where will I read about it?" (A legitimate
  forward question, not a gap in the essay's own argument.)
- **Would I share it: YES.** It hands me a repostable one-liner (the title) plus a
  falsifiable check with a date ("Etched has, in effect, published the diagram its own
  hardware can now be checked against") — that is exactly what I forward to the group
  chat instead of the hype thread.

### 9. Over-hedge symmetric check (6G)

**Verdict: NONE.** No safe-harbor boilerplate anywhere ("patents don't guarantee
products/production/stock gains" absent in all forms). The verdict is call-led, not
qualifier-led: "Hold the thread against the grant and the verdict is firm both ways."
Exactly one anti-hype guard and it is patent-specific (the 18-month unpublished-window
caution: "the visible record is a floor, not a census"), stated once and immediately
bounded ("Nothing readable today does."). The closing line is firm: "The wiring half is
the one you can check today, and it holds." Reverse-6G (conclusion safer than the body's
evidence): not present — the body's strongest evidence (claim-1 hop bound, claims 8/9/11
lane discipline, [0168] balance) is claimed at full strength in the close, and the
concession ("thin moat", firmware-gated scheduling claims) is scoped, not allowed to
dilute the call. The steelman is refined without adding hedges. No finding.

## Findings register

| id | check | class | severity | verdict | span (abbrev.) |
|---|---|---|---|---|---|
| sa2A-F1 | 5 jargon | jargon-overdepth / reader-profile rule 1 | low | un-glossed symbols in body | "When the number of processing devices is 8, p=4.35235, q=1.83809." (q never translated) |
| sa2A-F2 | 8 persona / reader-profile rule 5 | section-skim-risk (numeral density) | low | skim, not stop | "712a with 712c and 712b with 712d ... 712a with 712d, 712b with 712c" |
| sa2A-F3 | 7 thesis-restatement | thesis-restatement-redundancy | low | 4 sections vs <=3 letter of check | S1 "Half ... has a granted US patent standing behind it"; S5 "It does not claim the store."; S6 "The memory half has no equivalent fence anywhere in the claims"; S7 "The memory-pool leg has no substance in this filing"; plus the LVI echo across the S6/S7 boundary ("Low-Voltage Inference is nowhere in this filing" → "Low-Voltage Inference is untouched by it") |
| sa2A-F4 | 4 meta | meta-reader-instruction (borderline; plausibly exempt as functional scope disclaimer) | low | one self-reference | "The boundaries set out above scope that call. They do not soften it." |
| sa2A-F5 | 7 grounding | claim-scope stretch; fix class: narrow | low | STRETCHES | "every claim pursues one idea: how the chips of an AI cluster should be wired" (claims never mention AI; essay's own S5 says so) |

Mitigation notes for the multi-vote: sa2A-F3's S5 instance carries new analysis ("This is
the closest the filing comes to the thread's memory idea"), so the redundancy FEEL is
mild — flagged on the letter of the <=3 condition. sa2A-F4 sits inside the pass-7
functional-scope exemption if read as the mandated limits-scope-the-finding sentence.

**Totals: 0 critical / 0 high / 0 medium / 5 low.** No hard-gate territory touched
(grounding chain verbatim-clean at all sampled anchors; verdict firm in both directions;
figure use faithful). Nothing here blocks acceptance; all five are add-only polish
candidates.
