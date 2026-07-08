<!--
  Produced by: essay-en-composer (revision mode, references/revision-mode.md)
  Consumed by: editorial-review round 2 (re-review protocol) + _shared/scripts/check_run.py
  Round-1 inputs: handoff/03-edit/edit-log.round-1.md (5 medium, 7 low) +
  handoff/03-edit/gate-result.round-1.json (14/14 PASS, zero findings — no gate check_ids
  to disposition).
-->

# Revision response — round 1

draft_version: 2

## r1-F4 (medium, pass-3 — TPU 128×128 over-generalization)

- disposition: applied
- fix class: narrow (grounding priority: no stronger anchor exists for an external fact;
  claim narrowed to what the logged sources support — reviewer option a). No hedge added;
  the sentence stays declarative.
- before: "Google's TPU ran its matrix unit at exactly 128×128 through the v5p generation,
  and moved to 256×256 with Trillium (Google Cloud TPU documentation)."
- after: "Google's TPU ran its floating-point matrix units at 128×128 on generations
  through v5p, and moved to 256×256 with Trillium (Google Cloud TPU documentation)."
- note: the floating-point scope is the reviewer-verified exactness device (the first TPU's
  256×256 unit was 8-bit, so it falls outside the narrowed claim) and matches the register
  of the [0018] quote the sentence echoes ("floating point systolic arrays"). Aligns with
  fact-check-log `tpu-mxu-128x128` ("on generations through v5p"); the "exactly ... through
  the v5p generation" hardener is gone.
- location: §2 ¶1

## r1-F5 (medium, pass-3 — embodiment content under the claims verb)

- disposition: applied
- fix class: narrow (claims-verb clause restricted to claim-as-drafted content; the
  identicality beat already lands three paragraphs later on its correct register, verbatim
  [0028] embodiment quote — unchanged).
- before: "It claims a package holding many identical chips, each carrying its own modest
  math array, joined to its neighbors so that the whole package computes as one enormous
  array [0013], [0028]."
- after: "It claims a package holding many small chips, each carrying its own modest math
  array, joined to its neighbors so that the whole package computes as one enormous array
  [0013], [0028]."
- note: [0028] anchor retained — it still carries the host-sees-one-array half of the
  sentence (q-0028-1), no longer the identicality. The §2 header ("... Stitched From
  Identical Chips") stands untouched per the reviewer's own carve-out and the surface
  fence (energy-contract surface; the finding does not name the header factually wrong —
  it is embodiment-true as the document's design story).
- location: §2 ¶1, first claims sentence

## r1-F6 (medium, pass-3/4B — "second time" undercounts the choice-point record)

- disposition: applied
- fix class: narrow (de-precision: the count is removed, not re-estimated — the registry
  record supports "not the first time" exactly; each office action answered was itself a
  spend-or-lapse choice, so any event index is contestable).
- before (§5 ¶1): "It is the second time the company has chosen to keep spending on this
  document rather than let it lapse."
- after (§5 ¶1): "It is not the first time the company has chosen to keep spending on this
  document rather than let it lapse."
- before (§5 ¶3, now ¶4): "A dated, signed, twice-defended statement of the architecture
  is evidence about the company, whatever the office eventually says about the field."
- after (§5 ¶4): "A signed, dated statement of the architecture, defended past a final
  rejection, is evidence about the company, whatever the office eventually says about the
  field."
- note: chose the reviewer's "defended past a final rejection" option over "repeatedly
  defended" deliberately — the same paragraph already carries "the spending is repeated"
  and §6 ¶1 carries "defended with repeated spending" (r1-F1 flagged that kinship), so the
  registry-exact phrasing avoids stacking a third repeated/repeatedly echo. "Signed, dated"
  order (not "dated, signed") because removing "twice-defended" otherwise created a
  verbatim five-word duplicate (DUPE-001) with §6 ¶1's untouchable "a dated, signed
  statement of the memory idea". §6 ¶1 left untouched per the reviewer. The spine's
  "twice-made spending decision" framed phases, not an event index; thesis-trace §5
  wording synced so the trace no longer implies a count.
- location: §5 ¶1 last sentence; §5 ¶4 last sentence

## r1-F7 (medium, pass-3 — unlogged "product name" timeline fact)

- disposition: applied
- fix class: anchor (re-anchored to the record-supported variant riding on fact
  `thread-claims-2026-07`, first racks summer 2026 — reviewer's first option; no new fact
  logged, none needed).
- before: "The filing proves authorship: the memory half of Etched's architecture story
  was in claim language before the company had a product name."
- after: "The filing proves authorship: the memory half of Etched's architecture story was
  in claim language before the company had a product to sell."
- note: did NOT reuse §6's exact string "before there was anything to sell" — a verbatim
  reuse would create a §1/§6 five-word duplicate (DUPE-001) and sand the verdict's own
  phrasing; the "product to sell" variant carries the same record-supported content.
- location: §1 ¶3, second sentence

## r1-F11 (medium, pass-5 — steelman paragraph renders as a mobile wall)

- disposition: applied
- fix class: structural split, zero content change. Split exactly where the reviewer
  marked: after "...usually the first casualty of examination."
- before: one 127-word, 7-sentence paragraph (§5 ¶2).
- after: ¶2 = the examiner's record and the breadth risk (4 sentences: bear case on file →
  eight references → quotable/shrinkable → claim 1 breadth); ¶3 = claim 39's routine-risk
  and the landing (3 sentences: claim 39 could be judged routine → wrote it down early →
  early versus original).
- recount after split (revision-mode step 5): every §5 paragraph re-counted — ¶1: 4, ¶2: 4,
  ¶3: 3, ¶4: 6, ¶5: 5, ¶6: 6, ¶7: 4 sentences (¶7 includes the r1-F12 gloss split);
  full-document recount shows every paragraph within the 3-7 band; no figure token in §5,
  none orphaned elsewhere (figure set and positions unchanged, figures_locked).
- location: §5 ¶2 (now ¶2 + ¶3; downstream §5 paragraphs renumber +1)

## Low findings sweep (7 low)

- r1-F1 — applied. "And Etched has kept paying, from the filing fee through the
  examination it is still in, to turn that language into property." → "And Etched has paid
  at every step since, from the filing fee through the examination it is still in, to turn
  that language into property." Keeps the paragraph's closing "keeps paying to convert
  into an asset" (the spine's phrase). §5 ¶4 / §6 ¶1 left alone per the reviewer.
- r1-F2 — applied. "One more registry observation, offered as an observation." → "One more
  registry note, offered as an observation." (mandatory labeled-observation device kept;
  echo killed).
- r1-F3 — no action, per the reviewer's primary recommendation (acceptable-bridge
  repetition; every recurrence does contextual work; signature line 1 exempt). The
  optional §2 ¶1 thinning was declined to avoid churning the thesis number's motif.
- r1-F8 — applied (reviewer option 2). Both "(TechCrunch, July 2026)" parentheticals →
  "(TechCrunch)"; "July 2026" now appears only where it labels the thread per the brief;
  the exact article date (30 June 2026) lives in # Sources. Three-years arithmetic
  unaffected.
- r1-F9 — applied (factual anchoring on the lead surface — accuracy-first per
  reader-energy.md; zero wording change). "...no switch in between [0016]." →
  "...no switch in between [0016], [0044]." — [0044] carries the multi-chip half (column
  extending through all ICs) the composite sentence rides on. thesis-trace §1 anchor list
  synced.
- r1-F10 — applied. "a sibling sheet, FIG. 4, redraws the same package with unequal rows
  and columns" → "a sibling sheet, FIG. 4, redraws the same design with unequal rows and
  columns" (FIG. 4 is package 401, a distinct embodiment; "design" is what the
  variant-pair row supports). figures-rationale.md and thesis-trace deviation 3 quotes
  synced.
- r1-F12 — applied. "and no continuation, while the granted trio got both treatments" →
  the sentence gains the reviewer's one-clause gloss and is split so it stays inside the
  sentence-length band (the gloss pushed it to 38 words, LONGSENT-001): "This application
  is US-only, with no international counterpart under the PCT, the treaty route for filing
  abroad. It has no continuation either, the follow-on filing that keeps a patent family
  growing, while the granted trio got both treatments." The draft's last unglossed term of
  art now glossed; paragraph is 4 sentences, within band.

## Gate check_ids

None to disposition: gate-result.round-1.json is 14/14 PASS with zero findings (warns
included). Post-revision self-check re-run to keep it that way.

## Surface confirmation

Title, cover caption, §1 ¶1 wording (r1-F9 adds a citation token only), all six section
headers (incl. §2 "One Giant Array, Stitched From Identical Chips"), the three declared
signature lines, and the §6 verdict section are byte-identical to draft_version 1.

## Volunteered changes (beyond findings)

- None in prose. Bookkeeping only: thesis-trace.md (§1 anchors +[0044]; §5 spine-element
  wording no longer implies an event count; deviation-3 quote; steelman paragraph refs;
  word_actual recounts) and figures-rationale.md (FIG. 3 note's quoted FIG. 4 clause)
  synced to the applied findings above. publication.md regenerated via the strip pipeline.
