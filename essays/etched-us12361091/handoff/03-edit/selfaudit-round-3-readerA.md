# Self-audit round 3 — Reader A (impatient investor)

- essay: `handoff/03-edit/essay-final.md` (draft_version 4, closing_posture: firm)
- persona: impatient investor per `_shared/references/reader-profile.md` — came from the
  Etched stealth-exit thread, 6-minute budget, skims headers, reads captions before body,
  bails at homework, allergic to hype and lawyer-speak
- blind protocol honored: no edit-log, no revision-response/notes, no score-history, no
  prior selfaudit reports read. Sources consulted: essay-final.md, input/patent.md,
  input/essay-context.md, input/figures/fig-07C.png, handoff/01-design/invention-summary.md
  (Claim scope map only, for the locked/open/pinned check), pass-7 checklist.
- posture of this report: ADD-only. Nothing below proposes relaxing any gate, pass, or the
  acceptance bar.

## Checklist verdicts (evidence-forced)

### 1. BLUF lead-altitude — PASS

Declarative verdict inside paragraph 1, sentences 2-3: "Half of the loudest architecture
claim in the thread already has a granted US patent standing behind it. The other half, the
shared memory pool that gives Cluster-Scale Memory its name, has no granted substance in the
filings you can read today." No deferred question; the title itself is the verdict ("Etched
Patented the Wiring Half of Its Memory Story, Not the Memory"). Severity: none.

### 2. Header-as-claim — PASS

All seven body headers are assertions, and header-only skim reconstructs the argument arc:
"The Memory Story Has a Checkable Half" → "A Structure Patent Etched Keeps Paying to
Extend" → "Every Chip Reaches Every Chip Without a Switch" → "The Wiring Schedules the
Traffic" → "The Description Aims It at Transformer Decoding" → "No Latency Number, No
Memory Claim" → "One Leg Substantiated, One Leg Absent". `# Sources`/`# Footnotes` are
functional apparatus. Severity: none.

### 3. Steelman present — PASS (THIS-patent, full strength, then refined)

Conceded at full strength: "The objection an informed reader should press lands at full
strength. Claim 1 recites a wiring pattern and nothing else. ... No granted claim recites a
latency figure or a bandwidth magnitude, and claim 5 requires equal bandwidth across
channels, not high bandwidth. ... A topology-only claim over standard link technologies is a
thin moat for a 'proprietary ultra-low-latency, high-bandwidth interconnect'." This is a
THIS-patent objection (claim 1 content, [0134] link menu, claim 5 equality-not-magnitude —
all verified below), not a generic truism. Refinement follows without retracting the
concession: "In practice the fence reaches only builders who copy the wiring and stop
there." / "**Structure is what an apparatus claim can lock, and structure is exactly what
this one locks.**" / "The granted fence is not the adjective. It is the discipline
underneath it". Severity: none.

### 4. No meta posturing — PASS (two borderline spans noted, nit)

No "this essay/article will...", no "as we'll see", no reader-handholding. Two borderline
spans, both judged inside the functional exemption but recorded:

- "The boundaries set out above scope that call. They do not soften it." — self-reference
  ("above") but a functional scope disclaimer, exempt by the check's own terms.
- "Hold the thread against the grant and the verdict is firm both ways." — direct reader
  imperative opening the verdict section (finding sa3A-F4, nit).

### 5. Jargon as signpost — PASS overall, one gloss gap (low)

Glossed on first load-bearing use: tensors ("the grids of numbers AI models multiply"),
reduction ("combine partial results into one"), gather ("hand out copies of pieces"),
systolic array ("a grid of small processing elements that computes as data flows through
it"), MLP ("the multi-layer perceptron block that follows attention"), HBM/SRAM hybrid
("stacked high-bandwidth memory paired with on-chip SRAM"), PCT/continuation glossed by
function ("extends each abroad" / "keeps each open at home"). The K4,4 aside is one
skippable parenthetical, not a deep-dive. The p/q paragraph stops at the insight ("No link
runs hot."). Gaps: "QKV generation" and "the Q, K, and V matrices" never glossed
(sa3A-F1, low); "scale-up domain" used bare in the verdict section (sa3A-F2, nit).
No jargon-overdepth found: nothing is deep-dived past its insight.

### 6. No stub / rhythm break — PASS

Body sections run 3-7 paragraphs; no section markedly shorter than siblings. The one-line
bolded paragraph "**Structure is what an apparatus claim can lock...**" is a deliberate
pivot inside a 7-paragraph section, not a stub section. Severity: none.

### 7. Thesis not over-restated — FAIL by the letter (low; taste-level, multi-vote item)

Pass condition is "core verdict asserted in <= 3 sections". I count 4 sections carrying an
assertion-form statement of the wiring-substantiated / memory-absent verdict:

1. §1 lead: "Half ... already has a granted US patent standing behind it. The other half
   ... has no granted substance..."
2. §5 close: "The patent claims the wiring and the lane schedule that make such behavior
   cheap. It does not claim the store."
3. §6: "Described, never claimed." + "The granted fence is not the adjective. It is the
   discipline underneath it" + "none of them mentions memory."
4. §7 verdict: "The interconnect leg of Cluster-Scale Memory has granted, checkable
   substance ... The memory-pool leg has no substance in this filing..."

Persona experience: each echo rides new evidence (QKV tiles; FIG. 6 memory 630), so it read
as reinforcement, not fatigue — but the check is atomic and 4 > 3. Finding sa3A-F5 (low):
the §5 closer and §6 "Described, never claimed." are the compressible pair; varying or
cutting one restores the letter. This is a majority-vote taste check; my single vote flags
it.

### 8. Grounding spot-check — 5 samples, HOLDS / STRETCHES / BREAKS

Sampled across four different sections; verified against `input/patent.md` line-anchored
text and the CLAIMS section (lines 933-977).

| # | Essay claim (span) | Patent evidence | Verdict |
|---|---|---|---|
| 1 | §3 blockquote "a plurality of communication channels to directly communicatively couple every processing device in the first set ... without communicatively coupling any of the plurality of processing devices in the same set..." attributed "claim 1, [0386]"; plus "four or more a side under the granted claim" | Verbatim in granted claim 1 (patent.md line 933) AND in [0385]-[0387] example text (lines 793-797); claim 1 reads "first set of four or more ... second set of four or more" | **HOLDS** |
| 2 | §4 blockquote "During the second operation, data may only be transmitted ... using the second communication channels 740 and not the first communication channels 730 ." + "Which physical family carries which is the description's worked example rather than a claim requirement" | Verbatim in [0140]. Claims 8/11 bind sub-operations to abstract "first/second subset" labels only; [0140]'s gather-on-730 / reduction-on-740 pairing is the description's example. The essay correctly refuses to promote the example pairing into claim scope | **HOLDS** |
| 3 | §4 "p and q ... come out to about 4.35 and about 1.84 [0061]. Rounded to divisors, that is 4 and 2, and ... the whole input matrix lives spread across four of the eight chips [0061]" | [0061]: "p=4.35235, q=1.83809 ... when n=8, p=4 and q=2 ... an entirety of the input matrix is found on 4 of the 8 processing devices" | **HOLDS** |
| 4 | §5 quote "during the feedforward operation, the number of elements involved in a specific computation may be four times the depth of the transformer model" [0313] + "inflates processing time, or the bandwidth needed to hold processing time flat" | Verbatim in [0313]; same paragraph: "processing time ... may be much larger ... and/or a data bandwidth required to maintain a processing time ... may be increased" | **HOLDS** |
| 5 | §6 "No granted claim recites a latency figure or a bandwidth magnitude, and claim 5 requires equal bandwidth across channels, not high bandwidth" + §6 "none of them mentions memory" | Full read of claims 1-23: no latency, no bandwidth magnitude, no memory, no AI/transformer/inference token anywhere; claim 5 = "configured for a same data bandwidth" | **HOLDS** |

BREAKS: none. STRETCHES: none at severity; one nit-level conflation recorded as sa3A-F3
(the [0026] "expensive to include..." quote is said of "a data switch" while the essay's
sentence subject is the "networking switch [0032]" — same design alternative, both anchors
present).

**Full anchor sweep (exceeds the 3-section requirement):** every `[dddd]` anchor in the
header caption and in §3 ("Every Chip Reaches..."), §4 ("The Wiring Schedules..."), §5
("The Description Aims..."), and §6 ("No Latency Number...") was checked against the cited
paragraph: [0021], [0026], [0032], [0036], [0037], [0039], [0061], [0112], [0119], [0121],
[0123], [0124], [0125], [0126], [0128], [0129], [0130], [0133], [0134], [0135], [0136],
[0138], [0139], [0140], [0142], [0143], [0168], [0178], [0251], [0252], [0254], [0258],
[0259], [0267], [0278], [0313], [0336], [0337], [0384], [0385], [0386], [0387], [0418] —
all support the sentences they anchor. All four blockquotes are verbatim (including the
OCR spacing "730 ." / "905 ."). The [0278] and [0267] quotes match character-for-character.

**Claim scope map compliance (locked/open/pinned):** honored throughout.
- Locked: claim 1/14 "four or more" per set stated as granted scope; [0385]'s "two or more"
  correctly attributed to the specification's summary framing, never to claim 1.
- Open: link technology ("can be PCIe, SPI, ethernet, UCIe..."), memory attachment
  ("Described, never claimed."), which-family-carries-which, and the eight-device count
  ("In the drawings' eight-chip example") are all presented as description options or
  examples, never as claim requirements. Claim 18's two-or-more floor and its structural
  price match the map row exactly.
- Pinned: the map pins nothing; the description's point values (p=4.35235, q=1.83809) are
  rendered as "about 4.35 and about 1.84" — point values, NOT bounds. The only bound
  language used ("four or more", "at most one other") is genuine claim language. PASS.
- Derived values labeled: "16 channels ... counted off the drawing"; "both counts read off
  the figure, not numbers the patent states"; "inside nine months" = 266 days (footnote).
  Verified against fig-07C.png: 16 cross-column channels, none intra-column; caption's
  710a-right (a1, a3, a5, a7) / 710b-left (a0, a2, a4, a6) matches the drawing, and the
  lowercase chip labels follow the drawing itself. PASS.

### 9a. Persona verdict (impatient investor)

- **Where did I want the answer sooner?** Nowhere — the title is the verdict and paragraph
  1 sentence 2 delivers it. Evidence: "Half of the loudest architecture claim in the thread
  already has a granted US patent standing behind it."
- **Stop-point:** no hard bail. One skim-zone: §4 paragraphs 3-4 ("Balance is the other
  bought property..." with p/q decimals) is the densest stretch; I skimmed and was re-hooked
  by "No link runs hot." and §5's opener "None of this is claimed for AI." Length ~1,900
  words — a shade over my 6 minutes at full read, but the claim-headers make the skim path
  honest.
- **Money thread:** held throughout — "$1 billion in customer contracts against $800
  million raised" up front, "thin moat" pricing the objection, and a concrete watch-item at
  the close: "The company says its first systems ship in summer 2026. When they do, the
  scale-up domain becomes inspectable." I leave knowing what is substantiated, what is not,
  and what to watch.
- **Un-glossed jargon hits:** "QKV generation" (sa3A-F1); "scale-up domain" bare at the
  close (sa3A-F2). Neither made me bail; both cost a beat.
- **Leaving question:** "When the racks ship, who actually checks the wiring against claim
  1 — and would we hear about it?" The essay hands me the test but not who runs it. Benign;
  no unanswered money-question.
- **Share yes/no:** **YES** — quotable close ("The thread sells a memory story. The granted
  record holds a wiring story."), and it makes me the informed reply in the Etched thread.

### 9b. Over-hedge symmetric check (6G direction) — PASS both directions

- Safe-harbor boilerplate ("a patent doesn't guarantee production/stock gains", "not
  investment advice", "only time will tell"): **ABSENT**.
- Qualifier-led verdict: ABSENT — verdict section leads with the call: "Hold the thread
  against the grant and the verdict is firm both ways." Boundaries are scoped, not
  counterweighted: "The boundaries set out above scope that call. They do not soften it."
- Conclusion vs body evidence: NOT safer than the evidence (wiring leg asserted as granted
  and checkable, which claims 1/5/8/9/11 support; memory leg asserted absent, which the
  full claim read supports). Not stronger either: "and it holds" is scoped to the checkable
  wiring half, and the thin-moat concession stays priced in. Exactly one anti-hype guard,
  patent-specific and floor-not-census: "US applications can stay unpublished for up to 18
  months after filing, so the visible record is a floor, not a census. ... Nothing readable
  today does." The body's "arguably steps outside claims 1 and 14 as written" is labeled
  legal analysis in the body, not verdict hedging. No 6G finding.

## Findings (ADD-only; ids sa3A-F*)

| id | check | severity | verdict + evidence | recommended fix (jurisdiction-fenced) |
|---|---|---|---|---|
| sa3A-F1 | 5 jargon-gloss | **low** | "QKV generation" (§5: "then self-attention (QKV generation and attention computation)") and "the Q, K, and V matrices are processed as tiles" — term of art never glossed; reader-profile rule 1 requires a one-clause gloss on first use | Add one clause, e.g. "QKV generation — building the query, key, and value matrices attention works on"; no verdict text touched |
| sa3A-F2 | 5 jargon-gloss | nit | "the scale-up domain becomes inspectable" (§7) — thread jargon used bare outside quotation marks; first uses are inside fenced thread quotes | One-clause gloss at the §7 use ("the rack's worth of chips acting as one machine") or rephrase to "the rack" |
| sa3A-F3 | 8 grounding precision | nit | §3: "a networking switch that lets any chip talk to any chip [0032], which the filing calls 'expensive to include in a system that performs tensor operations' [0026]" — [0026]'s "expensive" sentence names "a data switch"; [0032] names the "networking switch". Same foil, both anchors present, subject conflated by a word | Anchor-precision wording fix: "a switch" or "a data switch" as the quote's subject. NOT a hedge; verdict untouched |
| sa3A-F4 | 4 meta-reader-instruction | nit | "Hold the thread against the grant and the verdict is firm both ways." — reader-directed imperative opening the verdict section; functional (it compresses the method into the call), but it is the essay instructing the reader | Optional: declarative recast ("Held against the grant, the verdict is firm both ways."); keep the firm lead either way |
| sa3A-F5 | 7 thesis-restatement | **low** | Core verdict asserted in 4 sections (>3): §1 lead; §5 "It does not claim the store."; §6 "Described, never claimed." / "The granted fence is not the adjective."; §7 verdict. Letter-fail of the <=3 pass condition; persona experienced reinforcement, not redundancy — taste-level, multi-vote | Compress one mid-essay echo (vary or cut the §5 closer OR §6 "Described, never claimed."), keeping lead + verdict at full strength. Not a hedge, not a softening |

Severity totals: 0 critical, 0 high, 0 medium, 2 low, 3 nit. Grounding: 0 breaks,
0 stretches at severity. No over-hedge finding; no overreach finding.

## Bottom line (this reader's vote)

All hard-gate-adjacent territory is clean from this seat: anchors verified across four-plus
sections, quotes verbatim, claim scope honored to the letter of the Claim scope map, pinned
values rendered as points, verdict firm in both directions with the single mandated guard.
The five findings are polish-tier (2 low, 3 nit); none individually or jointly rises to a
revision-forcing level under the severity model, and none licenses any relaxation elsewhere.
