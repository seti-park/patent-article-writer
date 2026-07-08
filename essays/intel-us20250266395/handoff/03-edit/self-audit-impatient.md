# Self-audit — persona: IMPATIENT RETAIL INVESTOR

Essay: `handoff/03-edit/essay-final.md` (US 2025/0266395 A1). Blind to other self-audit readers.
Protocol: pass-7 checklist (lead hook, header-as-claim, steelman, meta, jargon depth, stub,
restatement) + grounding spot-checks. Evidence-forced; every finding carries a quoted span.
Grounding recs are anchor/narrow/label/cut — never "add a hedge."

## Grounding spot-check result (PASS — recorded for the record)

Verified every `[dddd]` anchor in well over 3 sections against `input/patent.md`. All verbatim
quotes match their cited paragraph exactly:

- `[0142]` Example 21 — both quoted method spans (lines 29-30, 34-35) match line 200 verbatim. ✓
- `[0122]` "directly bonded" apparatus-claim span (line 39, 77) matches line 180. ✓
- `[0024]` passive/active bridge (line 59) matches line 80. ✓
- `[0025]` "many substrates remain solder-attach components" (line 41) matches line 81. ✓
- `[0034]` "in a range of 1 to 10 microns" (line 39) matches line 90. ✓
- `[0035]` power-routing + "reduces the number of substrate routing layers and can improve
  product yield" (lines 67, 69) match line 91. ✓
- `[0061]`/`[0062]` test/substrate (line 47) match lines 118-119. ✓
- `[0123]` "at least one contact on the second surface..." (lines 69, 77) matches line 181. ✓
- `[0138]` glass thickness (line 73) matches line 196; Example 17 depends on "any one of
  Examples 12-16" — the essay's §5 claim-scope statement (line 79) that claim 17 "hangs off the
  no-cavity inverted package of claim 16" while "the parallel Example paragraph is written
  broader" is CORRECT and matches the Claim scope map. ✓
- `[0144]` "placing the bridge component in the cavity" (line 83) matches line 202. ✓
- `[0049]`, `[0059]`, `[0033]`, `[0030]`, `[0054]`, `[0057]`, `[0058]` all confirmed. ✓

Claim-scope discipline is exemplary: pitch labeled "description examples, not in any claim"
(lines 39, 77); through-via claim "never says power, TSV, or cavity" (line 77); every "locks"
recast as "a lock Intel is asking for... pending application" (line 85). Pinned values are NOT
described as bounds. KGD math checks out (0.95^4 ≈ 81%, 0.95^20 ≈ 35.8%) and is labeled "the
industry's and this essay's, not the patent's" (line 51). Inventor count "thirteen" matches the
Sources list. No grounding finding at medium+.

---

## Findings

### F-IMP-01 — Money-relevance thread is implicit; verdict is an IP signal, not an investment one
- **severity:** medium
- **pass/lens:** pass-1 (lead energy) + reader-profile rule 4 ("the money thread is structural")
- **verdict:** yes (flag)
- **evidence:** The lead's payoff clause is "This is the most concrete piece of after-EMIB-T
  assembly thinking on the public record" (line 23) — a patent-position claim, not a
  company/stock stake. The verdict close resolves only to a documents watch: "the tell will be
  in the documents. The paperwork moved first last time" (line 93). Nowhere does the essay state
  what packaging leadership means for Intel as an *investment* — no line connects the flow to
  Intel's competitive position in AI/HBM packaging or foundry. The persona "opened the article
  because of the company or the stock" (reader-profile line 13) and is left with "Intel is
  serious about this direction" inferred, never stated.
- **where I felt it:** I skimmed to the verdict looking for "so what does this do for the
  stock," and got a research-watchlist instead. The competitive stake (this is Intel's answer
  for AI-accelerator packaging, the thing EMIB-T/HBM4 is about) is gestured at via the EMIB-T
  and 120mm/HBM references but never named as the investment reason.
- **recommendation:** ADD one competitive-stake clause (surface fix, not a hedge) — name once,
  in the lead or the close, why the assembly flow matters to Intel's packaging position. Keep it
  measured (no product is scheduled); this is naming the stake, not hyping it.

### F-IMP-02 — The glass paragraph is where I bail: concept overload, off-thesis, later conceded
- **severity:** medium
- **pass/lens:** pass-7 jargon-overdepth / attention-budget (6I) + reader-profile rule 5
  ("no prerequisite chains — at most one new concept per paragraph")
- **verdict:** yes (flag)
- **evidence (line 73, single paragraph):** "There is a quiet glass thread here: the bridge
  itself may be silicon, organic, or glass [0033]. A glass frame between the dies, drawn in FIG.
  6A, is there 'to provide structural stability' [0049]. And the receiving substrate can be built
  on a layer of glass shot through with through-glass vias, TGVs... Example 17 even sizes it: 'a
  layer of glass having a thickness in a range of 20 microns to 1.4 millimeters' [0138]. Intel
  announced glass-core substrates as a packaging direction in September 2023... and this filing
  is one of the places where the glass roadmap and the bridge roadmap touch. The ambition line
  sits at the end of the embodiments: assemblies like these may provide 'the functionality
  conventionally associated with a monolithic system on chip (SoC)' [0059]..."
- **why I bail:** one paragraph stacks six new things — glass bridge, glass frame, glass-core
  substrate, TGV, Example 17 sizing, Intel's Sept-2023 announcement — plus the SoC ambition
  line. It is off the essay's own spine (order of operations), and §5 later concedes glass is
  claimed narrowly and "hangs off the no-cavity inverted package" (line 79). So I invested
  reading effort in a glass wall that the essay then tells me is not the point — the exact
  "made me work for nothing" feeling the persona resents.
- **recommendation:** CUT/split. Keep the one glass beat that feeds the thesis (the glass-core
  substrate roadmap tie), drop or compress the glass-frame/Example-17 sub-variants, and relocate
  the SoC ambition line (see F-IMP-03).

### F-IMP-03 — The most investor-legible payoff (SoC-class from chiplets) is buried at a paragraph tail
- **severity:** low
- **pass/lens:** pass-1 (buried payoff)
- **verdict:** yes (flag)
- **evidence:** "assemblies like these may provide 'the functionality conventionally associated
  with a monolithic system on chip (SoC)' [0059], big-chip behavior from a cluster of small
  ones" (line 73, final clause of the glass paragraph). This is the single most legible "why
  chiplets matter" line in the essay and it sits at the tail of the densest, most off-thesis
  paragraph, where a skimmer will miss it.
- **recommendation:** SURFACE — move the SoC line to a load-bearing position (lead or verdict
  vicinity) rather than the end of the glass pile.

### F-IMP-04 — "vias" and "HBM" arrive unglossed before they are earned
- **severity:** low
- **pass/lens:** pass-5 jargon budget (reader-profile rule 1)
- **verdict:** yes (flag)
- **evidence:** "The technology in the news is the bridge getting power vias" (line 19) and "New
  vias let power climb into it" (line 21) both precede the first gloss of via at line 59
  ("through-silicon vias, TSVs, vertical metal shafts running through the die"). "twelve HBM
  memory stacks" (line 53) uses HBM unglossed. "one underfill (860) runs across the surface"
  (line 71 caption) uses underfill unglossed.
- **recommendation:** GLOSS "vias" on first use (line 19) or defer the term to line 59; add a
  two-word gloss for HBM ("high-bandwidth-memory HBM stacks").

### F-IMP-05 — Mild essay-self-reference skirts the meta line
- **severity:** low
- **pass/lens:** pass-7 check 4 (meta / essay-self-reference)
- **verdict:** borderline-yes
- **evidence:** "its impressive numbers do not sit where the previous sections may have left the
  impression they do" (line 77). This references the reader's experience of the essay's own
  earlier sections rather than the patent. It serves steelman honesty (conceding the essay may
  have oversold the numbers), which is close to a functional scope disclaimer — hence
  borderline, not a hard meta violation.
- **recommendation:** REPHRASE to point at the numbers themselves ("the 1-to-10-micron pitch and
  the glass cores do not sit in the claims") rather than "the previous sections."

### F-IMP-06 — Verdict restates the triad twice inside one closing paragraph
- **severity:** low
- **pass/lens:** pass-7 check 7 (restatement rhythm)
- **verdict:** yes (flag)
- **evidence (line 91):** "Bond the bridge to the chips first, test the cluster while no board is
  committed, then feed it power through the floor of a cavity... It is an order of operations,
  filed fifteen months before EMIB-T had a name on a stage. **Bond first, test before the board
  exists, power through the floor.**" The triad is stated in expanded form and then again as the
  compressed signature line within the same paragraph; line 93 restates it a third time as
  "die-first assembly and pre-substrate testing." For a reader who got the point in §2, the
  close feels like being told the same thing three times.
- **note:** the compressed signature line is likely a declared signature line (exempt from the
  restatement count per pass-7); this is flagged as a rhythm observation, not a gate breach.
- **recommendation:** consider CUT of one of the two adjacent triad statements in line 91.

### F-IMP-07 — "with no solder in between" is glossed onto [0122], which states only "directly bonded"
- **severity:** low
- **pass/lens:** grounding (anchor precision)
- **verdict:** borderline-yes
- **evidence:** "insulating material 'directly bonded' to insulating material, metal contacts
  bonded straight to metal contacts, with no solder in between [0122]" (line 39). Example 1
  `[0122]` states "directly bonded" but does not literally say "no solder"; the no-solder fact
  lives at `[0043]` ("There is no solder material at this HB interface 225-1"). The gloss is
  correct in meaning (directly bonded = hybrid bonding = no solder) but the anchor cited does not
  carry the "no solder" wording.
- **recommendation:** ANCHOR the no-solder gloss to `[0043]`, or present it explicitly as the
  meaning of "directly bonded" rather than as text carried by `[0122]`. (Anchor fix, not a
  hedge.)

---

## Summary

- **medium:** 2 (F-IMP-01 money-thread implicit; F-IMP-02 glass-paragraph overload / bail point)
- **low:** 5 (F-IMP-03 buried SoC payoff; F-IMP-04 unglossed vias/HBM; F-IMP-05 self-reference;
  F-IMP-06 close restatement; F-IMP-07 no-solder anchor)
- **grounding:** clean at medium+; anchors verify verbatim, claim scope honored, pins not called
  bounds.
