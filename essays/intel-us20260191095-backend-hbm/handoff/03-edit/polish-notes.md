# Polish notes (Phase 3.7 윤문)

- **origin:** polish
- **essay_id:** intel-us20260191095-backend-hbm
- **target:** handoff/03-edit/essay-final.md
- **draft_version:** 4 → 5
- **jurisdiction:** surface-only (split long/nested sentences, swap latinate for plain,
  disambiguate a pronoun). No fact, number, date, name, patent number, `[dddd]` anchor,
  verbatim quote, certainty verb, stance, header, or Sources line changed.
- **priority zone worked:** §2 "backend means" paragraph (the §2→§3 technical stretch the two
  cold readers flagged as the low point) + all of §3 "A Tower Built to Match HBM4's Footprint".
- **edits:** 9 operations across 8 sentences. No content compressed, no fact cut — the
  retained sentences are made to read more plainly (shorter, subject-first, one gloss kept as
  its own sentence). All splits keep each anchor on the clause that carries its fact.
- **gates:** re-run 14/14 PASS, 0 warns (identical to the pre-polish baseline; zero new findings).
- **drift check:** every changed sentence audited old-vs-new (grounding-verifier rubric:
  meaning preserved? protected surface intact?). All 9 = MEANING-PRESERVED, no PROTECTED-TOUCHED.
  Zero reverts.
- **protected, verified byte-identical after edits:** both declared signature lines (grep count
  1 each), the §2 bold thesis anchor (count 1), all five verbatim patent quotes (count 1 each),
  11/11 `[dddd]` anchors conserved, zero em-dash/en-dash introduced.

---

## polish 1 — §2, filing-description sentence (split a compound joined by "and")

**before:** The filing's description spells this out, showing thin-film-transistor layers stacked one atop another [0031], and it puts a size on one such die, at what "can be an approximately 1.5 GB die based on back-end-of-line transistors" [0027].

**after:** The filing's description spells this out, showing thin-film-transistor layers stacked one atop another [0031]. It puts a size on one such die, at what "can be an approximately 1.5 GB die based on back-end-of-line transistors" [0027].

**why-plainer:** One ~35-word sentence carrying two anchors and a verbatim quote is split at the "and" into two. [0031] stays with the thin-film-layers fact; [0027] and the quote stay with the die-size fact. Quote byte-identical.

**drift:** MEANING-PRESERVED · protected intact ([0031], [0027], quote, "1.5 GB" all untouched).

---

## polish 2 — §2, front-end sentence (split + subject-first)

**before:** In an ordinary memory chip, that transistor is etched into the crystalline silicon at the base of the die, the layer engineers call the front-end.

**after:** In an ordinary memory chip, that transistor is etched into the crystalline silicon at the base of the die. Engineers call that layer the front-end.

**why-plainer:** This is the exact clause the cold readers quoted as "heavy." The trailing reduced-relative appositive ("the layer engineers call the front-end") becomes its own short subject-first sentence. "that layer" = the base crystalline-silicon layer = the front-end; the definition is unchanged.

**drift:** MEANING-PRESERVED · no protected tokens in span.

---

## polish 3 — §2, thin-film-transistor gloss (split off the definition)

**before:** Building the access transistor up there makes it a thin-film transistor, a device deposited as a thin coating in the wiring rather than carved into the silicon below.

**after:** Building the access transistor up there makes it a thin-film transistor. That is a device deposited as a thin coating in the wiring, rather than carved into the silicon below.

**why-plainer:** A ~27-word sentence is split so the term ("thin-film transistor") lands first and its gloss follows as a clean sentence. Added a comma before "rather than" to mark the contrast for a general reader. Gloss content unchanged.

**drift:** MEANING-PRESERVED · no protected tokens in span.

---

## polish 4 — §3, cube/silicon sentence (split + latinate swap)

**before:** It describes a memory cube stacked eight high and beyond [0023], with the silicon thinned to enable that many-layer stacking [0031].

**after:** It describes a memory cube stacked eight high and beyond [0023]. The silicon is thinned to allow that many-layer stacking [0031].

**why-plainer:** Split the double-anchor sentence; "with the silicon thinned" → subject-first "The silicon is thinned"; "enable" → the plainer "allow" (exact synonym here, no strengthening). [0023] stays with "eight high and beyond"; [0031] stays with the silicon-thinning fact. Certainty unchanged (essay already asserted it declaratively).

**drift:** MEANING-PRESERVED · protected intact ([0023], [0031], "eight high" untouched).

---

## polish 5 — §3, sub-channels / bandwidth sentence (split off the relative clause)

**before:** They split the traffic into many independent sub-channels, the parallel data lanes whose combined width is where a memory's bandwidth comes from [0073].

**after:** They split the traffic into many independent sub-channels, the parallel data lanes [0073]. A memory's bandwidth comes from their combined width.

**why-plainer:** The nested relative clause ("whose combined width is where a memory's bandwidth comes from") is unpacked into a short standalone sentence. [0073] stays with the sub-channels fact it anchors; the bandwidth statement is the essay's existing gloss, meaning unchanged ("comes from" preserved).

**drift:** MEANING-PRESERVED · protected intact ([0073] stays on the sub-channels clause).

---

## polish 6 — §3, UCIe sentence (split off the gloss)

**before:** The base die carries the high-speed link to the processor over UCIe, or Universal Chiplet Interconnect Express, an industry standard for wiring one chiplet to another [0020].

**after:** The base die carries the high-speed link to the processor over UCIe, or Universal Chiplet Interconnect Express [0020]. UCIe is an industry standard for wiring one chiplet to another.

**why-plainer:** A ~26-word acronym-dense sentence (acronym + full name + gloss) is split. The patent-anchored fact (the UCIe link) keeps [0020]; the general-knowledge gloss becomes its own sentence. Full name "Universal Chiplet Interconnect Express" preserved; "UCIe" repeated as an explicit subject (states the same relationship the appositive did — no new fact).

**drift:** MEANING-PRESERVED · protected intact ([0020] stays on the UCIe-link clause; name untouched).

---

## polish 7 — §3, spare-arrays sentence (split off the gloss)

**before:** It also holds spare memory arrays that can stand in for defective ones once the stack is bonded [0034], a built-in repair budget for a part that cannot be reworked after stacking.

**after:** The base die also holds spare memory arrays that can stand in for defective ones once the stack is bonded [0034]. That is a built-in repair budget for a part that cannot be reworked after stacking.

**why-plainer:** A ~30-word sentence is split at the appositive; the "repair budget" gloss becomes its own sentence. [0034] stays with the spare-arrays fact. (Subject change "It" → "The base die" logged separately as polish 9.)

**drift:** MEANING-PRESERVED · protected intact ([0034] untouched).

---

## polish 8 — §3, target sentence (split a two-quote compound at "and")

**before:** Intel sizes each die "to have a die capacity of 0.5-5 GB" [0034], and designs the whole block, in the document's words, "With the goal of matching HBM4's footprint" [0034].

**after:** Intel sizes each die "to have a die capacity of 0.5-5 GB" [0034]. It designs the whole block, in the document's words, "With the goal of matching HBM4's footprint" [0034].

**why-plainer:** Two verbatim patent quotes were riding one sentence joined by "and"; splitting gives each quoted fact its own sentence. Both quotes byte-identical; both [0034] anchors preserved; "0.5-5 GB" and "HBM4" untouched. "and designs" → "It designs" (It = Intel).

**drift:** MEANING-PRESERVED · protected intact (both quotes, both [0034], "0.5-5 GB", "HBM4" untouched).

---

## polish 9 — §3, pronoun disambiguation (companion to polish 6/7)

**before:** ... chiplet to another. It also holds spare memory arrays that can stand in for defective ones ...

**after:** ... chiplet to another. The base die also holds spare memory arrays that can stand in for defective ones ...

**why-plainer:** After polish 6 split off the UCIe gloss sentence, the pronoun "It" (the base die) sat one sentence further from its referent, with "UCIe" as the nearer noun. Naming the subject ("The base die also holds ...") removes the ambiguity and preserves the "carries ... also holds" parallel. Referent unchanged.

**drift:** MEANING-PRESERVED · no protected tokens in span.
