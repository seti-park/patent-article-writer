<!--
  handoff/02-compose/revision-response.round-4.md
  Produced by: essay-en-composer (revision mode, references/revision-mode.md)
  Consumed by: editorial-review round 5 (re-review protocol) + _shared/scripts/check_run.py
-->

# Revision response — round 4

draft_version: 4  <!-- the version this revision produced -->

## r4-F1

- disposition: applied
- finding class: pass-3 claim-adequacy / claim-scope completeness (medium). NOT a verdict-hedge
  finding. The correction ADDS a third independent claim (29) to the core align-once /
  integer-accumulate coverage, so it strengthens the thesis. Grounding fix priority: this is an
  anchor/narrow correction (make the claim-scope enumeration accurate), never a hedge.
- upstream fix confirmed landed: the orchestrator corrected the invention-summary Claim scope map
  before this round. It now lists THREE independent claims — claim 1, claim 20 (triad + shift
  calculation and select decoding unit), and claim 29 (triad + shift register, CIM configured for
  a VMM operation) — with claim 29 added as its own row and the "Registry facts inside the
  document" note updated. The essay edits below re-anchor to that corrected grounding source; no
  patent re-read occurred.
- changes (four claim-scope loci, all "claims 1 and 20" / "claim 20" statements):
  - §2 ¶3 (line 34): "What independent claims 1 and 20 seek to protect" -> "What independent
    claims 1, 20, and 29 seek to protect".
  - §3 ¶2 (line 52): "independent claims 1 and 20 seek the multiply-align-add triad, not the mode
    decoding unit and not the format switching [0011]" -> "independent claims 1, 20, and 29 seek
    the multiply-align-add triad, not the mode decoding unit and not the format switching [0011]".
  - §3 ¶3 (line 54): reworked the "named machinery" paragraph so the machinery is pulled up into
    the independent claims themselves — claim 20 folds in the shift calculation and select
    decoding unit [0200], and claim 29 folds in a shift register — with the DEPENDENT claims
    adding the specifics (shift-register sizing = max exponent + mantissa bit count [0202], the
    logarithmic multiplexer tree [0206]). Removed the now-false "that unit is the one piece
    independent claim 20 pulls up into itself" framing (the shift register is folded up into
    independent claim 29, not only added by a dependent claim). The "64 by 64 half adders" [0183]
    sentence is kept verbatim. Reworked sentence (the fold-in resolution):
    "The named machinery is pulled up into the independent claims themselves. Claim 20 folds in a
    shift calculation and select decoding unit that works out each product's shift [0200], and
    claim 29 pulls in a shift register, each carried alongside the same multiply-align-add triad."
    (Wording note: the second verb is "pulls in", not a second "folds in". Substance is identical
    to the finding's directive — claim 29 independently carries a shift register — but the varied
    verb avoids a mechanical back-to-back "claim NN folds in a shift..." parallelism that would
    otherwise trip a new DUPE-001 warning and read as a pass-1 cadence tell. No fact changed.)
  - §6 ¶3 (line 87): "what examination leaves of claims 1 and 20 will fix how much" -> "what
    examination leaves of claims 1, 20, and 29 will fix how much". Sought-* vocabulary ("ends up
    owning") preserved; the verdict lead and both signature lines untouched.
- verdict discipline: closing_posture remains firm. No hedge, caveat, or disclaimer was added.
  The correction is a coverage-STRENGTHENING enumeration fix (a third independent shot at the same
  core), consistent with the finding's own "do NOT hedge the verdict" instruction and the 6G
  jurisdiction fence. The §6 call still LEADS with the assertion; the single THIS-patent anti-hype
  guard (Jalapeño / no-silicon) is unchanged and not re-listed.
- anchors: all [dddd] anchors in the edited spans ([0011], [0200], [0202], [0206], [0183]) were
  already present and valid in draft v3; no new anchor introduced, none removed. Every anchor
  traces to an invention-summary Quotable span / Quote anchor table row.
- recount after edit: §3 ¶3 moved from ~4 sentences to 5 sentences (~112 words) — still inside the
  3-7 band and < 150 words, no STRUCT-001 exposure; neighboring paragraphs untouched. No figure
  token added, moved, or orphaned (only FIG. 1/3/4/43 present). Verbatim blockquotes untouched.

## Volunteered changes (beyond findings)

- None. Only the four r4-F1 claim-scope loci were edited; captions, blockquotes, signature lines,
  figures, Sources, and all other prose are byte-unchanged from draft v3.
