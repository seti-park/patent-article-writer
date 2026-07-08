# Self-audit round 2 — Reader B (skeptical pro-subject reader)

- **Essay**: handoff/03-edit/essay-final.md (draft_version 4, essay_id etched-0378175-memory-in-writing-r2)
- **Persona**: AI-infrastructure practitioner; application-vs-grant discipline is home turf; hunting technical overclaim AND unearned hedging; surface energy-vs-evidence audited (title, header caption, lead, signature lines)
- **Blind protocol honored**: did NOT read edit-log*, revision-response*, revision-notes, score-history, or any selfaudit-round-* report. Read: essay-final.md, input/patent.md (claims read directly), input/essay-context.md, all 7 figure images (image = truth over manifest), invention-summary.md (Claim scope map), thesis-spine.md, fact-check-log.md, thesis-trace.md (signature-line declarations only).
- **Finding ids**: sa2B-F*
- **Totals**: 0 critical / 0 high / 2 medium / 4 low. Additive only; no gate, pass, or acceptance-bar relaxation proposed.

---

## 1. Pass-7 checklist (pro-subject weighting) — {verdict, evidence, severity}

| # | Check | Verdict | Evidence (quoted span or ABSENT) | Severity |
|---|---|---|---|---|
| 1 | Hook check (lead energy) | **yes (pass)** | ¶1 opens on the declared discovery beat, declarative: "Three years before Etched pitched 'the best layer is no layer' as its memory philosophy, both of its co-founders had signed that idea into the company's very first patent filing." No deferred question; verdict-insurance facts (pending, examiner) follow the beat, never precede it. Full two-sided call lands by §1 ¶3: "The filing proves authorship … What the filing is not, yet, is the property itself." Arithmetic on the surface is correct (2023-05 → 2026-06 = three years); the essay did NOT inherit the brief's "two years" error. | none |
| 2 | Header-as-claim | **yes, one low** | All six `##` headers are assertions; header-only skim reconstructs the argument (paper trail → one array from chips → memory claims delete the switch → forgets/remembers split → keeps paying → asset in formation). One scope wrinkle: §2 header, see sa2B-F4. | low |
| 3 | Steelman present | **yes (pass)** | THIS-application objection conceded at full strength in §5: "The bear case is genuinely strong, and it is already on file. The examiner has assembled eight references … a crowded field." + "Claim 1, as drafted, reads on more or less any multi-chip systolic-array package, and breadth like that is usually the first casualty of examination." + "Even claim 39's distinctive absence, the no-switch hardwiring, could yet be judged routine for weight-stationary designs". Then refined, not rebutted: "What survives the bear case is the record of behavior … None of that requires the claims to survive." No generic patent truism used as the steelman (the optional category-limit sentence is ABSENT entirely). | none |
| 4 | No meta posturing | **yes (pass)** | ABSENT. "Now the pricing." is a transition; "One more registry note, offered as an observation." and "with its label attached" are functional evidence-labels (exempt), not reader-instruction. | none |
| 5 | Jargon as signpost | **yes (pass)** | Every term of art glossed in one clause and left: "High-bandwidth memory, HBM, the stacked memory that feeds modern AI accelerators"; "an RCE is, in substance, a fee paid to keep arguing after the examiner has said no with finality"; "the PCT, the treaty route for filing abroad"; "continuation … the follow-on filing that keeps a patent family growing"; "weight-stationary designs, accelerators that keep weights parked in place"; "an independent claim, one that stands alone instead of refining another". Systolic-array explainer held to one paragraph tied to the insight. No over-depth. | none |
| 6 | No stub / rhythm break | **yes (pass)** | Section paragraph counts 3/5/6/5/6/3; the short closer is a closing, not a stub. ABSENT. | none |
| 7 | Thesis not over-restated | **yes (pass)** | Full verdict asserted in §1 ¶3 and §6; §5 ¶4 is refinement, not restatement. The §3 bold ("The no-layer pitch is not marketing retrofitted onto hardware. It is claim language, dated May 2023.") is declared signature line 2 in thesis-trace.md — exempt from count, factually reviewed (accurate). ≤3 sections. | none |

## 2. Deep claim audit (sought-as-owned? translations vs claims text)

Read claims 1–42 directly from input/patent.md and compared every essay translation:

- **Claim 39** (essay §3): "a package with a chip carrying a math array, plus a separate memory device, with every memory channel hardwired to its own column or columns, 'without any switching element' in between [0016]" — vs claim text "each of the plurality of channels is hardwired to respective one or more columns in the systolic array without any switching element". **Faithful**, including the easy-to-flub "respective one or more columns" → "its own column or columns". The [0016] summary twin is block-quoted verbatim. PASS.
- **"Claim 39 is an independent claim … and it does not require the multi-chip package at all"** — claim 39 recites "an IC" (singular). TRUE, and honored per the Claim scope map row 39. PASS.
- **"the broadest package claim does not require memory chips, which the description concedes 'may not be needed' [0037]"** — claim 1 has no memory element; [0037] verbatim. PASS.
- **Claim 15** (essay: "A second independent claim seeks the weight-streaming arrangement itself: memory chips storing an AI model's weights, coupled to the chips that form the array's top row [0014]") — matches claim 15 / [0014]. "Seeks" = application-era. PASS.
- **Claims 11–13** (essay: "give each chip the sidecar, give the sidecar the attention work, and wall its memory off from the arrays") — matches claims 11/12/13; the quoted negative rule "the local systolic arrays 220 do not have access to the local memory chips 610" is correctly anchored to its description twin [0051] (claim 13's own verb is "do not communicate with" — the essay paraphrase "wall … off" covers both). PASS.
- **"Claim 1, as drafted, reads on more or less any multi-chip systolic-array package"** — accurate breadth statement; matches map row 1 prosecution-risk note. PASS.
- **Sought-as-owned: ABSENT.** Every ownership construction is conditional or negated: "to turn that language into property. What the filing is not, yet, is the property itself"; "can be judged, and owned, on its own"; header "Etched Keeps Paying to Own It"; "becomes property it owns" (inside an explicit if); "not an exclusive right to it"; "still paying to own the deletion". No grant-era verb ("locks/requires/fences") applied to this application anywhere. The only "granted" language targets US 12,361,091 B1, which IS granted. PASS.
- **No enforceability language anywhere** (brief hard rule). ABSENT — confirmed. PASS.
- **Pinned values**: the Claim scope map declares none exist; the essay presents no number as a claim bound — 128×128, 1 TB/s, 98%, 100×400 are all narrated as the description's or the industry's ("by the description's own numbers"; FIG. 7 material labeled "Description-only, no claim covers it" in BOTH prose and caption). PASS.
- **One wording finding at the verdict surface**: sa2B-F1 below.

## 3. Mechanism honesty vs spec + figures (images checked directly)

- **FIG. 5** (header embed + §3): image shows exactly what the caption says — memory chips 505A/505B, four independent channels 510A–D, wires 520, four columns 515A–D inside array 220 on IC 215, no switching element drawn. Caption "with no switch anywhere in the path" is what [0043]–[0045] and the drawing show. PASS.
- **FIG. 6 — known manifest defect verified against the image**: the manifest line is WRONG ("Local memory chips 605A-605D built into each IC block"); the image and [0047]–[0048] show 605A–D = auxiliary circuitry INSIDE ICs 615A–D beside tiles 220, and 610A–D = local memory chips OUTSIDE, hanging off the 605s, outside the dashed combined array 650. The essay caption uses the corrected reading ("the array tile (220) and the auxiliary circuitry (605) sit side by side; the private local memory chips (610) hang off the auxiliary circuitry, outside the combined array (650)") — the defect did NOT propagate. PASS.
- **FIG. 1** ("two computations sharing one grid") — image shows Multiplication #1/#2 hatching. PASS. **FIG. 2** ("nine ICs (215) … memory chips (210) line the top row; host (205) … PCIe (240)") — image shows 215A–I / 220A–I, 210A–C top row, host + PCIe. PASS. **FIG. 3** ("six memory chips across the top") — 305A–F. PASS. **FIG. 4** ("unequal rows and columns") — 2×3. PASS. **FIG. 7** ("the lone stall at layer normalization (Time B)") — Time B marked on the axis; [0057] puts the stall at Time B. PASS.
- **Derived numbers**: 128×128 ≈ "roughly sixteen thousand multipliers" (16,384 ✓); 1 TB/s → "a feature film's worth of data every five thousandths of a second" (5 GB/5 ms ✓, logged as derived comparison film-per-5ms, scoped "by the description's own numbers"); "passes through the systolic array three times" [0055] ✓; "a 98% or greater utilization" [0057] ✓. PASS.
- One embodiment-scoping drop: sa2B-F3 below.

## 4. External-fact fencing

| Fence | Verdict | Evidence |
|---|---|---|
| Venue + date wording vs cited source | **pass** | "its stealth-exit thread in late June 2026" / "The thread that announced Etched's stealth exit" / Sources: "TechCrunch, Etched stealth-exit coverage (30 June 2026)" — matches the cited URL date (techcrunch.com/2026/06/30/…). No stage/keynote venue anywhere. |
| ONE prosecution label sentence | **pass** | Exactly one dated label, §5 ¶1: "As of the May 2026 record, this application is still pending, with examination continuing after a final rejection mailed 23 October 2025 and a request for continued examination (an RCE) docketed 24 April 2026." Carries all required elements. Other mentions are status-only clauses ("still hasn't said yes", "still being argued with an examiner") or date-free argumentative reuse ("defended past a final rejection") — no battle narrative, no re-narrated dates. |
| Both-or-neither | **pass** | Collateral facts and the rejection/RCE label sit in the same section (§5); neither appears without the other. |
| Lien discipline (portfolio scope, blanket, symmetric) | **pass** | "The first, effective 19 April 2024 (USPTO reel/frame 067204/0877), covered the four applications Etched had at the time, all the IP it then owned … and so were two compiler applications that were later rejected." + "Both liens are blanket, selecting nothing and saying nothing about any single filing's worth." + symmetric creditor frame + "The dates are facts. Any motive read into them is inference." Effective dates used (not recordation dates). Reel/frames match the fact log exactly. |
| TPU facts | **pass** | "Google's TPU ran its floating-point matrix units at 128×128 on generations through v5p, and moved to 256×256 with Trillium" — matches fact tpu-mxu-128x128, and the word "floating-point" correctly excludes TPU v1's integer 256×256 MXU. Both Google sources listed. |
| Company-claim attribution | **pass** | Every thread figure attributed on use: "every figure the company's own claim (TechCrunch)", "presented as shipping hardware in the company's telling", "the racks the company says are shipping", "in the press's expansion". Tier-5 Sohu linkage NOT used. |
| LVI absence + 18-month caveat | **pass** | "a power-delivery story the company calls LVI, appears nowhere in this filing. That absence carries one standing caveat: applications younger than 18 months can exist unpublished and unseen." Matches lvi-absent-here (full-text verified) and the brief. |
| Founder-count wording | **FINDING** | sa2B-F2 below. |
| Sources provenance | **finding (low)** | sa2B-F6 below. |

## 5. Grounding spot-check (samples, all against input/patent.md)

| # | Essay span | Anchor | Verdict |
|---|---|---|---|
| S1 | Block quote "from the perspective of the host 205 … distributed on separate ICs 215" | [0028] | verbatim-pass |
| S2 | Block quote "Another embodiment in this disclosure is a package that includes an IC … without any switching element." | [0016] | verbatim-pass |
| S3 | "could extend through all the ICs 215 in a column" | [0044] | verbatim-pass |
| S4 | "transmit more than 1 TB/s of data to each of the ICs" | [0040] | verbatim-pass (substring ends before the source's "215in" run-on — substring discipline honored) |
| S5 | "a 98% or greater utilization" | [0057] | verbatim-pass |
| S6 | "the local systolic arrays 220 do not have access to the local memory chips 610" | [0051] | verbatim-pass |
| S7 | Split-quote "avoids having to add a switching element between the local systolic array" + "which can save space and power" | [0045] | verbatim-pass (the unquoted bridge "and the memory chips" cleanly routes around the source's "220and" typo without editing a quote) |

Additionally, every [dddd] anchor in §1, §2, §3, and §4 was walked against the cited paragraph while reading ([0002], [0003], [0013], [0014], [0016], [0018]×2, [0019], [0021]×2, [0024], [0027], [0028]×3, [0035], [0037], [0038], [0039]×2, [0040], [0043]×2, [0044]×2, [0045], [0047]×2, [0048], [0051], [0053], [0055]×2, [0056], [0057]×2): all support the sentences they anchor. §5/§6 carry no patent anchors (external facts only), consistent with the trace.

## 6. Over-hedge symmetric check (6G)

- Safe-harbor boilerplate: ABSENT. Generic "patents don't guarantee products/returns" truism: ABSENT.
- Verdict is call-led, not qualifier-led: "The verdict is firm. This document is the real origin of Etched's memory story."
- Exactly ONE anti-hype guard, and it is patent-specific: "Racks shipping this summer, if they ship, are not evidence that these claims will grant. That question gets decided against the examiner's citations, nowhere else." (§3's "What no filing can show is silicon" is an evidence-boundary statement needed by the CSM-echo beat, not verdict insurance — it prevents the stronger overreach of reading the product as practicing the claims.)
- Conclusion vs body: NOT safer than the evidence. The bear half of the close ("The claims as drafted can shrink or die") is earned by an on-file final rejection, and the bull half ("the real origin", "authentically the founders' own", binary conversion test) actually pushes slightly PAST the record in one word — see sa2B-F1, which is an overreach-side finding, not a hedge. **No over-hedge finding.**

## 7. Findings

### sa2B-F1 — medium — deep-claim-audit / verdict wording (overreach-side)
- **Span** (§6, essay line 103): "The no-switch idea is authentically the founders' own, written into claim language before there was anything to sell."
- **Problem**: "authentically the founders' own" is ambiguous between authorship (proven: named inventors, dated filing) and originality (expressly undecided by the essay's own §5: "The founders wrote it down early. The patent office decides whether early also meant original." and "could yet be judged routine for weight-stationary designs"). Read as originality — the natural pro-subject reading of "their own idea" — the verdict's second sentence asserts what the steelman concedes is an open question. This is the single sentence I would attack in public.
- **Fix (fence-compliant, narrower claim — not a hedge)**: bind the word to authorship, e.g. "The no-switch idea is authentically the founders' own writing, in claim language before there was anything to sell." (or "…the founders' own, on the record's authorship…"). One-word-scale change; keeps the firm register.

### sa2B-F2 — medium — external-fact fencing / founder count
- **Spans**: §1 ¶1 (line 20): "both of its co-founders had signed that idea into the company's very first patent filing"; §1 ¶2 (line 22): "Gavin Uberti and Christopher Zhu, the two founders"; §5 ¶4 (line 93): "10 May 2023, both founders."
- **Problem**: the run's fact base (patent.md header; essay-context) establishes only that the two inventors ARE co-founders — never that the company has exactly two founders. "Both of its co-founders" and "the two founders" assert an exhaustive count no cited source supports, and public reporting on Etched commonly names a third co-founder; an Etched-aware reader catches this instantly and it discounts the essay's registry-grade precision elsewhere.
- **Fix (narrower claim)**: "its co-founders Gavin Uberti and Christopher Zhu" / "two of its founders" / "co-founders both" as a postnominal ("Gavin Uberti and Christopher Zhu, co-founders, as its inventors"). No hedge needed; the thesis (inventor-founders authored the architecture) survives untouched.

### sa2B-F3 — low — mechanism honesty / embodiment scoping
- **Span** (§4 ¶1, line 71): "The combined array 'does not take instructions at runtime, and only executes instructions in a preset loop' [0027]."
- **Problem**: [0027] scopes this with "in one embodiment"; the essay drops the qualifier while (correctly) flagging description-not-claim status. Inconsistent with the care shown at [0028] ("In a version the filing describes, the chips are all interchangeable").
- **Fix (label, not hedge)**: "In the version the description settles on, the combined array 'does not take instructions at runtime…'".

### sa2B-F4 — low — header-as-claim / scope
- **Span** (line 26): header "One Giant Array, Stitched From Identical Chips".
- **Problem**: identicality is an [0028] embodiment preference ("In one embodiment, the ICs 215 are all identical."), not claim content; the header states it as the design's headline. The body corrects within the section ("In a version the filing describes…"), so harm is bounded — but a header-only skim carries an unclaimed limitation.
- **Fix (optional)**: none required if the body scoping is judged sufficient; otherwise "…Stitched From Small Chips".

### sa2B-F5 — low — brief budget / continuity clause
- **Span** (§2 end, line 43): "The wiring half of that story, the part Etched has since gotten granted, was read separately in a companion analysis of US 12,361,091 B1. That granted record never wrote the memory half down."
- **Problem**: the brief allows "one clause of continuity"; this is two sentences. (thesis-trace.md declares it as composer deviation 4 — recorded here independently for the multi-vote; no reader harm found, and the absence claim about the granted record is covered by the prior run's full text per the brief.)
- **Fix (if budget enforced)**: compress to one sentence/clause.

### sa2B-F6 — low — sources provenance precision
- **Span** (Sources, line 114): "USPTO assignment, prosecution and citation records for application US 18/195,769 … via Google Patents legal events."
- **Problem**: per fact-check-log, the office-action dates come from the DOCDB/WIPS registry export (2026-07-02); Google Patents corroborated status and liens, not the OA dates. The Sources line credits the access path that did not supply the load-bearing dates.
- **Fix**: append the registry export to the line (e.g. "…via Google Patents legal events and a DOCDB/WIPS registry export (2026-07-02)").

## 8. Persona verdict

As a skeptical practitioner I came hunting sought-as-owned slippage, claim-translation drift, and manufactured hedging, and found none: claim 39's single-IC independence and "respective one or more columns" are rendered faithfully, claim 1's breadth is conceded rather than sold, the steelman is a real this-application objection stated at full strength, the figures say what the captions say (including the manifest-defective FIG. 6, read correctly from the image), and the firm close is earned on both sides. The sentence I'd attack is "The no-switch idea is authentically the founders' own…" — read as an originality claim it outruns the record the essay itself calls undecided — and "the two founders" hands an Etched-aware reader a needless count quibble; both are one-phrase narrowing fixes, neither touches the thesis.
