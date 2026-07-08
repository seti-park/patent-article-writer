<!--
  Produced by: essay-en-composer (revision mode, references/revision-mode.md)
  Consumed by: editorial-review round 3 (re-review protocol) + _shared/scripts/check_run.py
  Round-2 inputs: handoff/03-edit/edit-log.round-2.md (1 medium, 1 low) +
  handoff/03-edit/gate-result.round-2.json (14/14 PASS, zero findings incl. warns — no gate
  check_ids to disposition).
-->

# Revision response — round 2

draft_version: 3

## r2-F1 (medium, pass-3 — forward-exhaustive "eight references, nowhere else" in the verdict)

- disposition: applied
- fix class: narrow (grounding priority: no stronger anchor exists — no anchor can close an
  open reference set, since the same May 2026 record that carries the count says examination
  is continuing after the RCE with a third non-final action issuing, so the set of art the
  decision will be made against is open by the record's own terms. Claim narrowed to the
  spine's own guard phrasing). No hedge added; the sentence stays declarative; "nowhere else"
  kept at full punch per the reviewer's own instruction.
- before: "That question gets decided against the examiner's eight references, nowhere else."
- after: "That question gets decided against the examiner's cited art, nowhere else."
- note: this is the reviewer's one-clause narrow executed with the design bundle's guard noun
  phrase — thesis-spine.md closing posture: "the examiner-cited field is where that gets
  decided" (same phrasing in essay-context.md's anti-hype guard material). "Cited art" is
  forward-open (it covers the eight references of record AND whatever the examiner adds in
  RCE prosecution) while staying exclusive against the stage, so "nowhere else" is now
  supportable as written. Chose this over the reviewer's fuller option (a) ("at the patent
  office, against the examiner's cited art") deliberately: §6 already carries "until the
  patent office says yes" (¶1) and signature line 3's landing IS the venue beat ("At the
  patent office, Etched is still paying to own the deletion.") — pre-echoing "at the patent
  office" one paragraph before the landing would dilute the declared line the surface fence
  protects. The clause "the examiner's cited art" resolves by back-reference to §5 ¶2's
  fully-glossed steelman ("The examiner has assembled eight references against this
  application... a crowded field"), so no new gloss is needed in the verdict. Secondary 6G
  point cleared by the same edit: the count ("eight") no longer re-lists a §5 detail inside
  the verdict — the exact figure now lives only in §5, dated by ¶1's "As of the May 2026
  record" (fact examiner-art-8refs stays exact there, per the reviewer). Word-count-neutral
  swap (11 → 11 words); ¶ stays 3 sentences; §6 ¶1 verdict call and ¶3 untouched.
- location: §6 (An Asset in Formation) ¶2, last sentence

## Low findings sweep (1 low)

- r2-F2 (low, pass-2 — "past + rejection" echo inside §5 ¶4, side effect of the r1-F6 fix) —
  applied, reviewer's primary variant. "And the spending is repeated: examination has been
  paid for through a rejection and past it." → "And the spending is repeated: examination
  has been paid for through a rejection and beyond it." Colon device kept; sentence 6
  ("defended past a final rejection", the registry-exact landing) untouched per the
  reviewer's instruction. Echo-check before applying: "beyond" appears nowhere else in the
  draft, so the smoothing introduces no replacement echo; registry truth unchanged (the RCE
  is spend beyond the final rejection). Word-count-neutral ("past" → "beyond", 1:1);
  ¶4 stays 6 sentences.

## Gate check_ids

None to disposition: gate-result.round-2.json is 14/14 PASS with zero findings (warns
included). Post-revision self-check re-run to keep it that way.

## Recount (revision-mode step 5)

No structural edit this round — both fixes are in-place, word-count-neutral single-clause
swaps. Re-verified after editing: paragraph and sentence counts unchanged everywhere
(§5 ¶4 = 6 sentences, §6 ¶2 = 3 sentences); no figure token touched, figure set and
positions unchanged; thesis-trace word_actual values remain exact (total word count
identical to draft_version 2).

## Surface confirmation

Title, cover caption, §1 ¶1 (byte-identical, zero tokens changed), all six section headers,
and the three declared signature lines are byte-identical to draft_version 2. §6: ¶1 (the
verdict call) and ¶3 (binary test + landing) byte-identical; the only §6 delta is the
r2-F1 clause in ¶2's last sentence. Mechanically verified by line diff v2 → v3: exactly
three changed lines (frontmatter draft_version, §5 ¶4, §6 ¶2).

## Volunteered changes (beyond findings)

- None in prose. Bookkeeping only: thesis-trace.md §6 spine-element parenthetical synced to
  the applied r2-F1 wording ("decided against the examiner's cited art" — it previously
  quoted "decided against the examiner's references"). publication.md regenerated via the
  strip pipeline.
