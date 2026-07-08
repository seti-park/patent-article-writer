# Self-Audit Grounding Verification — Round 2 (dry-check)

Target: `handoff/03-edit/essay-final.md` (draft_version 4, US 2024/0378175 A1)
Blind self-audit — mechanical fidelity only. No edit logs / revision notes / prior self-audit
reports consulted.

## 1. Mechanical gate outputs

```
$ python .claude/skills/_shared/scripts/gate_quotes.py handoff/03-edit/essay-final.md \
    --invention-summary handoff/01-design/invention-summary.md --patent input/patent.md
[PASS] gate=quotes
  (no findings)

$ python .claude/skills/_shared/scripts/gate_anchors.py handoff/03-edit/essay-final.md \
    --invention-summary handoff/01-design/invention-summary.md --figures <fig-list: 1,2,5,6,7>
[PASS] gate=anchors
  (no findings)
```

Both mechanical gates pass clean. All 35 `[dddd]` anchor tokens and all block quotes resolve
verbatim against `input/patent.md`.

## 2. Full anchor-by-anchor fidelity table

Every `[dddd]`-anchored sentence in reading order (35 anchor tokens; some sentences carry two).

| # | Location | Sentence (anchor) | Invention-summary span | Patent paragraph | Verdict | Evidence |
|---|---|---|---|---|---|---|
| 1 | FIG.5 header caption | "Two memory chips (505A, 505B) sit above one IC (215)...dedicated column (515A to 515D)...(220) [0044]." | Layer 2 step 4; q-0044-1 | [0044]: "the independent channels 510 can be directly wired (or hardwired) to a particular column 515..." + worked example (505A/505B, 510A-D, 515A-D) | SUPPORTED | Drawing detail matches [0044]'s worked example exactly (2 chips, 4 channels, 4 columns). |
| 2 | FIG.5 header caption | "This is the interface the application claims, as drafted, in claim 39 [0016]." | Claim scope map row "39 (indep.)"; q-0016-1 | [0016] mirrors claim 39 verbatim | SUPPORTED | Correct application-era verb ("claims...as drafted"); claim 39 confirmed sought-memory-interface, not locked. |
| 3 | Body, blockquote | "a package that includes a plurality of integrated circuits (ICs)...to form a larger, combined systolic array" / [0013] | q-0013-1 | [0013] | SUPPORTED | Verbatim block quote, exact match; correctly attributed to [0013] (the spec's claim-1 mirror), not to "claim 1" directly. |
| 4 | Body | "a multi-chip approach where local arrays are joined by high-speed chip-to-chip links into one larger, combined array [0019]." | q-0019-1 | [0019] | SUPPORTED | Accurate paraphrase. |
| 5 | Body | "hardware built for algorithms that "perform the same task with different data at different times" [0002]." | q-0002-1 | [0002] | SUPPORTED | Verbatim quote fragment. |
| 6 | Body | "the task that dominates the hardware's work is matrix multiplication [0003]." | q-0003-1 | [0003] | SUPPORTED | Accurate paraphrase. |
| 7 | Body | "Model weights (110)...enter from the top row of cells (105) [0021]." | Layer 2 step 3 | [0021]: "topmost row of DPUs 105 receive AI model weights 110" | SUPPORTED | Direct match. |
| 8 | FIG.1 caption | "Weights (110) come down from the top [0021]" | Layer 2 step 3 | [0021] (receipt at top row); downward-flow phrasing is in [0022] ("weights 110 flow from top to bottom") | SUPPORTED (low confidence — see §5) | [0021] supports "top"; the "come down" direction is technically [0022]'s statement. |
| 9 | Body | "most chips top out at "floating point systolic arrays with a size of 128×128" [0018]." | q-0018-1 | [0018] | SUPPORTED | Verbatim quote. |
| 10 | Body, blockquote | "it is unreasonable to expect a single chip to interface with 100s of GB..." / [0018] | q-0018-2 | [0018] | SUPPORTED | Verbatim block quote. |
| 11 | Body | "Hundreds of gigabytes is the working size...roughly a whole laptop's storage...[0018]." | q-0018-2 | [0018] | SUPPORTED (low confidence — see §5) | "Laptop's storage" is the essay's own scale illustration, footnoted (`derived-comparisons`), not patent text. |
| 12 | Body | "Horizontal connections (230) and vertical connections (225) [0029] join neighboring tiles until they compute as one combined systolic array (250) [0019]." | Layer 2 step 2 | [0029], [0019] | SUPPORTED | Matches spec description of both connection types and the resulting combined array. |
| 13 | Body | "with a physical layer that "supports up to 32 GT/s" [0030]." | q-0030-2 | [0030] | SUPPORTED | Verbatim fragment (drops "16 to 64 lanes," not misleading). |
| 14 | Body | "the combined array "appears to be one large array" [0028]." | q-0028-1 | [0028] | SUPPORTED | Verbatim fragment. |
| 15 | Body | "adding more rows of chips adds compute without adding memory chips at the top [0039]." | q-0039-1 | [0039] | SUPPORTED | Accurate paraphrase. |
| 16 | Body | "the combined array "does not take instructions at runtime, and only executes instructions in a preset loop" [0027]." | q-0027-1 | [0027] | SUPPORTED | Verbatim quote. |
| 17 | Body, blockquote | "a switch (or some kind of switching element such as a crossbar) is typically used..." / [0043] | q-0043-1 | [0043] | SUPPORTED | Verbatim block quote. |
| 18 | Body, blockquote | "a separate memory device comprising a plurality of channels...without any switching element" / [0016] | q-0016-1 | [0016] (mirrors claim 39) | SUPPORTED | Verbatim; essay's framing sentence ("mirrored word for word in the filing's own summary") checked true — claim 39's closing clause is identical to [0016]'s. |
| 19 | Body | "The weights streaming into the top of the array "may be constants" [0021]" | q-0021-1 | [0021] | SUPPORTED | Verbatim fragment. |
| 20 | Body | "the channels "can be directly wired (or hardwired) to a particular column" [0044]" | q-0044-1 | [0044] | SUPPORTED | Verbatim fragment. |
| 21 | Body | "concludes that "hardwiring the memory chips 505 to the columns 515 is permissible" [0045]" | q-0045-1 | [0045] | SUPPORTED | Verbatim. |
| 22 | Body | "books the deletion as a gain, "which can save space and power" [0045]." | q-0045-2 | [0045] | SUPPORTED | Verbatim. |
| 23 | Body | ""can enable the memory chips 305 to transmit more than 1 TB/s of data to each of the ICs" [0040]." | q-0040-1 | [0040] | SUPPORTED | Verbatim; quote correctly truncated before the "215in" typographic artifact per the invention-summary's typo note. |
| 24 | Body | "Claim 15 frames the system version...store the model's weights [0014]." | claim-scope-map "15 (indep.)"; q-0014-1 | [0014] | SUPPORTED | Accurate. |
| 25 | Body (bold) | "The 2023 filing books the gain as space and power [0045]." | q-0045-2 | [0045] | SUPPORTED | Correctly distinguishes patent-sourced "space and power" gain from thread-sourced "latency" framing (verified — "latency" does not appear anywhere in patent.md). |
| 26 | Body | ""self-attention operations use data computed from previous tokens, which means such data should be saved" [0047]." | q-0047-1 | [0047] | SUPPORTED | Verbatim (minus lead-in clause). |
| 27 | Body | ""Most of the parts of a transformer AI model do not use data from previous tokens" [0047]." | q-0047-2 | [0047] | SUPPORTED | Verbatim. |
| 28 | Body, blockquote | "In this embodiment, the local systolic arrays 220 do not have access to the local memory chips 610." / [0051] | q-0051-1 | [0051] | SUPPORTED | Verbatim block quote. |
| 29 | Body | "Attention's bookkeeping gets its own circuit and its own private memory, and the two never contend for the same store [0051]." | q-0051-1 | [0051] | SUPPORTED | Accurate paraphrase. |
| 30 | Body | "the filing puts the result at "98% or greater utilization of the systolic array" [0057]." | q-0057-1 | [0057] | SUPPORTED | Verbatim. |
| 31 | FIG.7 caption | "at Time A a new computation has already entered while the previous one drains. The only idle gap is the layer-normalization stall, marked at Time B [0057]." | q-0057-1 | Time B / 98%: [0057]. Time A mechanism ("new computation entering before the previous drains"): [0056], NOT cited. | SUPPORTED (low confidence — see §5) | Content is accurate to both paragraphs, but the caption's single trailing anchor [0057] doesn't cover the Time A clause, which is [0056]'s statement. |
| 32 | Body | "claim 39's hardwired channels "without any switching element" [0016]" | q-0016-1 | [0016] | SUPPORTED | Verbatim fragment. |
| 33 | Body | "inverts the crossbar practice the specification itself calls typical [0043]." | q-0043-1 | [0043] | SUPPORTED | Accurate. |
| 34 | Footnote `[^figures-not-placed]` | "their one load-bearing point, more compute rows without more memory chips, travels in prose via [0039]." | q-0039-1 | [0039] | SUPPORTED | Verified — [0039]'s content is indeed carried in body row 15 above. |

Row count: 34 (35 anchor tokens; rows 12 and one other group each carry two tokens in one
sentence, counted once where the sentence is a single fidelity unit).

## 3. Sub-table 1 — Claim statements vs CLAIMS text + scope map

| Claim(s) | Essay sentence | Claims text (verbatim check) | Scope map class | Verb check | Verdict |
|---|---|---|---|---|---|
| 1 | Blockquote [0013] presented as "what the application asks for, in its broadest form" | [0013] mirrors claim 1 almost word for word (confirmed by direct comparison) | sought-broad | "asks for" — application-era | SUPPORTED |
| 1 | "That is a description preference, not something claim 1 requires as drafted" (re: UCIe) | Claim 1 has no connection-technology limitation; UCIe is spec-only ([0030]) | Scope map: "Leaves open... Connection technology (UCIe is a description preference)" | "requires as drafted" — explicitly qualified, matches scope-map header phrasing exactly | SUPPORTED |
| 1, 26 | "claim 1 and claim 26 as drafted, sit closest to that art and are exactly the kind of claims that shrink in it" | — | Scope map risk notes for claim 1 ("likeliest to narrow or die") and claim 26 ("shares claim 1's fate") | Probabilistic framing ("likeliest," "kind of claims that shrink"), no certainty asserted | SUPPORTED |
| 7, 8 | "Claims 7 and 8, as drafted, put HBMs on that same switchless hardwiring, several of them per top-row chip" | Claim 7: "HBMs are hardwired to respective columns...without any switching element"; Claim 8: "multiple HBMs are hardwired to each...in the topmost row" | sought-memory-interface (HBM form) | "as drafted" | SUPPORTED |
| 11–13 | "Claims 11 to 13, as drafted, add auxiliary circuitry (605)...backed by local memory chips (610)...The last of them, claim 13, then draws a boundary" | Claims 11/12/13 verbatim confirmed (auxiliary circuitry, self-attention data use, "do not communicate") | sought-auxiliary-division | "add," "draws a boundary" — descriptive of claim content only | SUPPORTED |
| 15 | "Claim 15 frames the system version, an AI accelerator whose memory chips...store the model's weights" | Claim 15 text confirmed | sought-system | "frames" | SUPPORTED |
| 39 | "Claim 39...asks for the opposite," "the interface the application claims, as drafted, in claim 39" | Claim 39 text confirmed identical to [0016] | sought-memory-interface | "asks for," "claims...as drafted" | SUPPORTED |
| 39 | "claim 39's hardwired channels "without any switching element" [0016], inverts the crossbar practice..." "it is the best candidate to survive in some form among the application's four independent claims" | — | Scope map: "likeliest of the four to survive in some form...though the negative limitation remains examinable" | "best candidate...in some form" mirrors scope-map hedge almost exactly | SUPPORTED |
| general | "So the honest verbs for this document are application-era verbs: Etched is seeking these claims, as drafted..." "Three years of prosecution have produced no enforceable claim at all." "does not yet own anything in it." | — | Edition note: no locked class, no enforceability language | No grant-era verb ("locks/requires/fences/owns/guarantees") found anywhere applied to claim content; every instance of "requires"/"claims" as a verb carries an "as drafted" or equivalent qualifier | SUPPORTED |

No grant-era or enforceability verb was found attached to claim content anywhere in the essay
(checked via full-text grep for "the patent locks/requires/fences," "patented," "guarantee").
The two hits on "patent stack"/"patent assets"/"three granted patents" (asset-status
paragraph) refer to the portfolio's already-granted trio, not to this pending application, and
are accurate collateral-registry language, not enforceability claims about US 2024/0378175 A1.

## 4. Sub-table 2 — External facts vs fact-check-log

| Essay location | Fact | fact-check-log ID | evidence_level | Attribution check | Verdict |
|---|---|---|---|---|---|
| ¶ "The money facts sit in the public registry..." | 1st TriplePoint lien, 2024-04-19, reel/frame 067204/0877, covers 4 applications incl. 2 rejected compiler filings | `tp-lien-1-2024` | registry-extract | No selectivity claimed; "blanket" framing present | SUPPORTED |
| same ¶ | 2nd TriplePoint lien, 2025-07-18, reel/frame 071792/0869, covers portfolio incl. 3 granted patents | `tp-lien-2-2025` | registry-verified | Matches | SUPPORTED |
| same ¶ | "second and third of those grants had issued three days earlier, on 15 July 2025" | `grant-lien-timing` | registry-verified (dates) / inference (motive) | "reading them as a lender sweeping fresh assets...is an inference, not a record" — correctly labeled | SUPPORTED |
| same ¶ | "Both liens are blanket over the portfolio at signing, with no selectivity...say nothing about this application in particular" | Collateral-discipline hard rule (fact-check-log Notes) | — | Both-or-neither rule honored (both lien facts + prosecution label appear in the same section) | SUPPORTED |
| ¶ "As of the 2026-05 record..." (line 98) | Pending; final rejection; RCE | `prosecution-record` | registry-extract | **Label-sentence budget = 1.** Occurrence count: exactly 1 full chronology sentence (line 98). Later mentions ("refused once," "rejection record," "no rejection can un-write," heading "Rejection") are callbacks to the established fact, not restatements of registry chronology with new dates — budget honored. | SUPPORTED |
| ¶ "The examination record lists 8 references..." | Examiner-cited field | `examiner-cited-field` | registry-extract | Matches verbatim ("8...references, all examiner-cited, clustered in multi-node ML acceleration, hybrid parallelism, and neural-network accelerator architectures") | SUPPORTED |
| ¶ "The filing's family is US-only..." | Family facts | `family-us-only` | bibliographic | "That is a bibliographic observation...proves nothing by itself about intent" — correctly labeled, contrast-only usage | SUPPORTED |
| ¶2 "The company says its first racks ship in summer 2026..." + footnote `[^thread-claims]` | $1B+ contracts, $800m raised, summer 2026 ship, LVI/CSM pillars | `etched-thread-2026-07` | company-claimed | "The company says" attribution present at first use + "Every number and claim in that thread is the company's own account" reinforcement; footnote repeats attribution chain | SUPPORTED |
| ¶ "So is the memory half that is absent from the company's granted wiring patent...the subject of an earlier analysis" | Companion-analysis continuity clause | `prior-essay-wiring-half` | internal-prior-run | One clause in body prose (budget: "Max ONE clause of continuity"); Sources-list restatement is bibliographic identification, not a second narrative clause | SUPPORTED |

**Thread-claims count:** all thread-sourced figures ($1B+, $800m, summer-2026, LVI, CSM,
"latency" philosophy) appear in one paragraph plus the footnote gloss — all "company says"
attributed, none presented as verified.

**3-day timing count:** stated once (line 100), correctly labeled as dates-only-with-inference-caveat.

**Prosecution-label count:** stated once (line 98) — budget of ONE honored; verified by full-text
grep.

**Family facts count:** stated once (line 98), labeled bibliographic.

No unlogged external fact was found in the essay — every non-patent factual assertion traces to
a fact-check-log entry.

## 5. Sub-table 3 — Figure captions vs images + cited paragraphs

| Figure | Caption claim | Cited paragraph(s) | Manifest cross-check | Verdict |
|---|---|---|---|---|
| FIG. 5 (header) | "memory channels hardwired to array columns, with no switch in between" | — (uncaptioned image alt-text) | Matches manifest description | SUPPORTED |
| FIG. 5 caption | One-to-one drawing: "each independent channel (510A to 510D) runs over its own wires (520) straight into a dedicated column (515A to 515D)" | [0044] | Matches manifest and [0044]'s worked example exactly (1:1 channel-to-column) | SUPPORTED — correctly scoped to the *drawing's* specific 1:1 instance, distinct from... |
| Body | Claim 39 / [0016] gloss: "each memory channel is bonded...to its own column **or columns**" | [0016] / claim 39 | "one or more columns" is the claim's actual (broader) language | SUPPORTED — correctly scoped to the *claim's* broader "one or more" breadth. No conflation between the drawn 1:1 embodiment and the claim's broader gloss; both are accurate at their own scope, as required. |
| FIG. 1 caption | "Weights (110) come down from the top [0021], data (115) comes in from the left" | [0021] | — | SUPPORTED (low confidence — "come down"/downward-flow specifics are [0022]'s statement, not [0021]'s; [0021] establishes only that weights are received at the top row) |
| FIG. 2 caption (no bracket anchor) | ICs 215A-215I, tile 220, connections 230/225, Combined Systolic Array 250, memory chips 210A-210C, host 205/PCIe 240 | [0025]-[0029], [0034] | Matches manifest description (three memory chips 210A-210C, PCIe host link) | SUPPORTED |
| FIG. 6 caption | "Each IC (615A to 615D) holds an array tile (220) plus an auxiliary-circuitry block (605). The local memory chips (610A to 610D) are reachable only by that auxiliary circuitry." | (uncaptioned; body cites [0051] separately for the same content) | **KNOWN MANIFEST DEFECT**: figures-manifest.md line 10 swaps the labels ("Local memory chips 605A-605D...feeding array tiles...directly"). Essay caption is the CORRECT one — matches the specification (605 = auxiliary circuitry per [0047]-[0052]; 610 = local memory chips per [0048]-[0051]) and the invention-summary's reference-number table, which explicitly documents the manifest's defect and instructs to follow the spec. | SUPPORTED — essay avoided the manifest defect; caption is spec-accurate. |
| FIG. 7 caption | "at Time A a new computation has already entered while the previous one drains. The only idle gap is the layer-normalization stall, marked at Time B [0057]." | [0057] cited; Time A content is [0056]'s | Time A/B semantics checked against [0056]-[0057] directly: Time A = new computation (MLP output layer) starting before previous (MLP hidden layer) fully drains — [0056]; Time B = layer-normalization stall — [0057]. Caption's semantics are accurate; no swap. | SUPPORTED (low confidence on citation precision — see row 31 above; content is correct, but [0056] is not cited alongside [0057]) |

## Findings

No `sa2G-F*` findings raised at medium-or-higher severity. Every anchored sentence, every
claim statement, every external fact, and every figure caption checked SUPPORTED. This is a
dry round (round 2 of the self-audit grounding loop).

One advisory-only, non-blocking citation-precision observation (informational, not a formal
finding — does not change any verdict, no disposition required):

- `sa2G-F1` (informational/low): FIG.7 caption's Time A clause ("a new computation has already
  entered while the previous one drains") is sourced from [0056], but the caption's single
  trailing anchor is `[0057]` (which covers only the Time B / 98%-utilization clause).
  Recommended fix if picked up in a future round: **anchor** — add `[0056]` alongside
  `[0057]` in the FIG. 7 caption's anchor set. Content itself is accurate; this is a citation-
  completeness note, not a fidelity failure.
