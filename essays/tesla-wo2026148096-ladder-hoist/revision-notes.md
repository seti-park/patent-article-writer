<!--
  Produced by: essay-en-composer (REVISION MODE, self-audit apply round 1)
  Self-audit delta ledger: every span moved by the post-accept audit, old → new, verbatim.
  Origin for every row: self-post-accept (adversarial-reader A/B + cold reader +
  grounding-verifier, round 1). Dispositions detail:
  handoff/02-compose/revision-response.selfaudit-round-1.md
  Result: draft_version 2 → 3 (essay-final.md = essay-draft.md, byte-identical;
  publication.md regenerated via strip_publication.py).
-->

# Revision notes — self-audit round 1 delta ledger

## delta (applied edits, old span → new span)

### SA-FIX-1 — sa1-A-3 = sa1-B-1 (medium) — gas engine narrowed to the entry configuration

- §1 (line 19), old: "The machines sold to do that job today are dedicated gas-engine track
  hoists at $3,500 and up."
- §1 new: "The machines sold to do that job today are dedicated track hoists at $3,500 and
  up, with a 4 HP gas engine at the entry price."
- §3 (line 40), old: "The incumbent answer to this job is a 4 HP gas engine, and the doubt
  is first-order physics:"
- §3 new: "The cheapest incumbent answer to this job is a 4 HP gas engine, and the doubt is
  first-order physics:"
- Ground: fact-check-log `tranzsporter-tp250-price-specs` ($3,500.99 = 4 HP Lifan gas entry
  model; electric variants cost more). Category no longer contradicts §4's electric
  incumbents (SPH-250/500, TP250 electric).

### SA-FIX-2 — grounding-verifier PARAPHRASE-DRIFT (mechanical) — "clamp-on" de-drifted

- §1 (line 19), old: "It is three clamp-on modules that turn a standard extension ladder
  and a jobsite cordless drill into a solar-panel hoist [0037]"
- §1 new: "It is three add-on modules that turn a standard extension ladder and a jobsite
  cordless drill into a solar-panel hoist [0037]"
- Ground: "clamp" appears nowhere in the patent; mounting is rung-locking brackets
  ([0049]/[0054]/[0057]) for gearbox and pulley, face-riding rollers ([0044]) for the
  carriage — so no single mounting verb covers all three modules; neutral "add-on" is what
  [0037] supports. Anchor unchanged and honest.

### SA-FIX-3 — sa1-B-3 (medium) + cold-reader biggest stop-point — §7 caveat in reader terms

- §7 (line 85), old: "One further caveat is mechanical. The public OCR text of the claims
  is damaged, with dependent-claim numbers garbled, which is why the citations here point
  to the specification's mirror paragraphs rather than to dependent-claim numbers. The
  independent claims are unaffected: device claim 1 and kit claim 20 are clean boundaries."
- §7 new: "One further caveat is mechanical. The claims in the public copy are a garbled
  scan, so the citations here point to the part of the filing that spells each claim out
  again in intact text. The independent claims are unaffected: device claim 1 and kit
  claim 20 are clean boundaries."
- Trust-repair function kept; "mirror paragraphs" / "OCR" / "dependent-claim numbers"
  jargon removed; no new hedges.

### SA-FIX-4 — sa1-B-2 (medium) + sa1-A-7 (low) — §6 return narrowed to claim 1's ask

- §6 (line 75), old: "Side rollers wrap the ladder's rails so the carriage cannot slip off
  sideways [0044]."
- §6 new: "Optional hardware in the dependent claims does the guiding: side rollers wrap
  the ladder's rails so the carriage cannot slip off sideways [0044]."
  (following ramps sentence unchanged; label covers the pair)
- §6 (line 77), old: "What claim 1 asks for is the thing the 1978 document never drew, the
  guided carriage."
- §6 new: "What claim 1 asks for is the thing the 1978 document never drew, a carriage
  attached to the ladder's face rather than a load hung from a cable."
- Ground: claim 1 locks only carriage-on-first-major-side + pulley + gearbox + rope
  (claim scope map); rollers (claims 10-11, [0044]) and ramps (claim 9, [0051]) are
  leaves-open. Retained as-is: §6 header and §8's "guided carriage" callback (name the
  essay's concept, not claim 1's text).

### SA-FIX-5 — sa1-B-5 (medium) + sa1-A-9 (low) — §8 conversion double-tap removed

- §8 (line 89), old: "What it seeks is not a new machine but the conversion itself: the
  arrangement that turns a standard ladder and a standard drill into the incumbents'
  $3,500 job."
- §8 new: "What it seeks is not a new machine but the arrangement that turns a standard
  ladder and a standard drill into the incumbents' $3,500 job."
- "The conversion" now lands once, in exempt signature line 3 (untouched): "The incumbents
  sell the machine. Tesla is asking to own the conversion."

### SA-FIX-6 — sa1-A-8 + sa1-B-9 (low, agreed) — two jargon glosses at first use

- §7 (line 83), old: "...claims priority to a provisional from 3 January 2025."
- §7 new: "...claims priority to a provisional from 3 January 2025, the placeholder filing
  that reserved that earlier date."
- §8 (line 91), old: "The international search report and the national-phase record will
  show what an examiner stacks between claim 1 and a grant..."
- §8 new: "The international search report will show what an examiner stacks between
  claim 1 and a grant. The national-phase record, the filings Tesla makes in individual
  patent offices, will show whether the guided carriage holds up as the distinguishing
  arrangement."
- One clause each, comma apposition, plain register; no other terms glossed (no glossary
  creep). The §8 sentence was split in the same edit: a first single-sentence gloss form
  ran to 40 words and raised a new typography WARN (LONGSENT-001) absent from round 3;
  the split restores a zero-finding typography gate and divides the labor accurately
  (ISR = the prior-art stack; national phase = where the distinguishing argument is tested).
  Closing paragraph is now 6 sentences (band 3-7 respected).

## Deliberate dispositions (no edit)

- sa1-A-4 = sa1-B-4 + cold-reader (figure captions without embeds): deliberate
  caption-only body convention per design pair-breaks; images inserted at posting;
  posting-checklist will encode the five embeds. Origin: self-post-accept.

## Dropped (multi-vote splits, one line each, origin: self-post-accept, no edit)

- sa1-A-1 (medium, "newest" superlative) — dropped; external-fact table GROUNDED, no agreed vote.
- sa1-A-2 (low, "world patent office") — dropped; no agreement.
- sa1-A-5 (low, signature line 2 vs claim 20 when quoted alone) — dropped; protected surface, no agreement.
- sa1-A-6 (low, "for decades" in concession) — dropped; matches fact-check-log claim text, no agreement.
- sa1-B-6 (low, §1 noun-phrase header) — dropped; deliberate lead-header exception, no agreement.
- sa1-B-7 (low, header pre-spends signature phrase) — dropped; settled surface, no agreement.
- sa1-B-8 (low, borderline meta spans) — dropped; functional scope-disclaimer exemption, no agreement.
- sa1-B-10 (low, §5 money-thread pacing) — dropped; pacing preference, thread fed through §2-§4, no agreement.

## Bookkeeping

- draft_version: 2 → 3 in handoff/03-edit/essay-final.md and handoff/02-compose/essay-draft.md
  (byte-identical, verified by cmp).
- publication.md regenerated: `python3 .claude/skills/_shared/scripts/strip_publication.py
  handoff/02-compose/essay-draft.md -o handoff/02-compose/publication.md`.
- Word count: 2322 → 2366 (draft, +44); publication 2304 → 2348 (+44).
- Signature lines (thesis-trace.md): all three untouched, each appears exactly once.

# Revision notes — self-audit round 2 delta ledger

<!--
  Origin for every row: self-post-accept (adversarial-reader A round 2 +
  grounding-verifier round 2). Dispositions detail:
  handoff/02-compose/revision-response.selfaudit-round-2.md
  Result: draft_version 3 → 4 (essay-final.md = essay-draft.md, byte-identical;
  publication.md regenerated via strip_publication.py).
-->

## delta (applied edits, old span → new span)

### SA2-FIX-1 — sa1-A-1 + sa2-A-1 (two votes, medium) — "newest" superlative de-ranked to the publication event

- §1 (line 19), old: "The newest Tesla document at the world patent office is not about
  cars, batteries, or robots."
- §1 new: "The Tesla document published on 9 July at the international patent bureau is
  not about cars, batteries, or robots."
  (the "world patent office" → "international patent bureau" swap in the same sentence is
  SA2-FIX-4, below)
- §1 ¶2 (line 21), companion trim — the date moved into ¶1, not duplicated:
  old: "The document is WO 2026/148096 A1, \"Ladder Hoist Assembly\", published on
  9 July 2026, and two things are true about it at once."
  new: "The document is WO 2026/148096 A1, \"Ladder Hoist Assembly\", and two things are
  true about it at once."
- Ground: publication date 2026-07-09, invention-summary §Metadata/§Timeline; §7 keeps
  the fully-dated sentence ("It published on 9 July 2026..."). No corpus ranking left for
  a skeptic to falsify; discovery beat and the not-cars-batteries-robots turn intact.

### SA2-FIX-2 — grounding-verifier round 2 (mechanical, 3 occurrences) — "cordless" de-invented

- §1 (line 19), old: "a standard extension ladder and a jobsite cordless drill"
- §1 new: "a standard extension ladder and a jobsite drill"
- §2 (line 34), old: "The cordless drill arrives in dependent claims and the specification"
- §2 new: "The drill arrives in dependent claims and the specification"
- §3 (line 40), old: "A cordless drill does not sound like a machine that hauls solar
  panels to a roofline."
- §3 new: "A hand drill does not sound like a machine that hauls solar panels to a
  roofline."
- Ground: the record says only "a drill" ([0037], [0020]), "standard drill" ([0041]),
  "hand drill adapter" ([0024]); no fact-check-log entry supplies a power source.
  "jobsite" kept per the verifier's note; "hand drill" is patent-native register.

### SA2-FIX-3 — sa2-A-3 (SINGLE vote, medium; applied on orchestrator ruling) — §6 return closes the incumbent guided-carriage loop

- §6 (line 77), old: "The ingredients are old."
- §6 new: "The ingredients are old, and the incumbents' guided carriage rides a custom
  ladder of its own [0039]."
  (final contrast sentence unchanged: "What claim 1 asks for is the thing the 1978
  document never drew, a carriage attached to the ladder's face rather than a load hung
  from a cable.")
- Ground: [0039] "existing assemblies ... utilize custom ladders, batteries, and/or
  motors"; "of its own" echoes §4's logged incumbent facts (own base track / own track
  sections). ONE clause; +16 words, all in the return; concession untouched.
- Iteration: clause first tried on the final colon sentence → 37-40 words →
  LONGSENT-001 WARN (threshold >35); moved to the preceding sentence → typography gate
  zero findings; paragraph stays 4 sentences.
- thesis-trace.md §6 updated: [0039] added to paragraph_anchors_used.

### SA2-FIX-4 — sa1-A-2 + sa2-A-2 (two votes, low, discretionary) — "world patent office" gloss corrected

- §1 (line 19), old: "at the world patent office"
- §1 new: "at the international patent bureau"
- Applied (not rejected) because the sentence was already rebuilt by SA2-FIX-1, so the
  swap costs the cadence nothing; plain-reader register kept, and the gloss now tracks
  the real institution (WIPO's International Bureau — publishes, grants nothing) instead
  of a nonexistent world office §7-§8 had to un-teach.

## Log-and-drop (one line each, origin: self-post-accept round 2, no edit)

- sa2-A-4 (low, market-universal from two listings) — logged, no edit; outside the apply set.
- sa2-A-5 (low, "within five minutes" flattened in two paraphrases) — logged, no edit; §4 carries the verbatim hedge.
- sa2-A-6 (low, unattributed ~18% projection) — logged, no edit; outside the apply set.
- sa2-A-7 (low, "reads on" unglossed) — logged, no edit; adjacent to protected signature line 2.
- sa2-A-8 (low, §1 noun-phrase header) — logged, no edit; settled surface (round-1 sa1-B-6 drop).
- sa2-A-9 (low, §7 citation-convention inversion for the pulley clause) — logged, no edit; outside the apply set.

## Bookkeeping (round 2)

- draft_version: 3 → 4 in handoff/03-edit/essay-final.md and handoff/02-compose/essay-draft.md
  (byte-identical, verified by cmp).
- publication.md regenerated: `python3 .claude/skills/_shared/scripts/strip_publication.py
  handoff/02-compose/essay-draft.md -o handoff/02-compose/publication.md`.
- Word count: 2366 → 2375 (draft, +9); publication 2348 → 2357 (+9).
- Gates: OVERALL PASS, zero findings from any gate (15/15 PASS, 0 FAIL, 0 WARN).
- Residuals: "cordless" 0, "newest" 0 (essay-final, essay-draft, publication).
- Signature lines: all three untouched, each appears exactly once in essay-final.md and
  publication.md.

# Revision notes — self-audit round 3 delta ledger (final, micro-apply)

<!--
  Origin for every row: self-post-accept (adversarial-reader A round 3 +
  grounding-verifier round 3). Dispositions detail:
  handoff/02-compose/revision-response.selfaudit-round-3.md
  Result: draft_version 4 → 5 (essay-final.md = essay-draft.md, byte-identical;
  publication.md regenerated via strip_publication.py).
  DRY declared at cap after this apply — self-audit loop closed.
-->

## delta (applied edits, old span → new span)

### SA3-FIX-1 — sa3-A-1 + grounding round-3 OVERREACH #49 (two votes, medium) — §6 incumbent clause re-sourced

- §6 (line 77), old: "The ingredients are old, and the incumbents' guided carriage rides
  a custom ladder of its own [0039]."
- §6 new: "The ingredients are old, and the incumbents still bring custom ladders of
  their own [0039]: today's machines ride a dedicated base track, not the crew's ladder."
- Ground: [0039] carries only the custom-ladder point ("existing assemblies ... utilize
  custom ladders, batteries, and/or motors"), with the anchor moved onto that clause
  alone; what today's machines ride is now said in the fact-check-log's own vocabulary
  ("dedicated" / "base track", per `tranzsporter-tp250-price-specs` and
  `safety-hoist-solar-price-setup`) and rests on §4's already-cited spec-sheet facts.
  No "guided carriage" is attributed to the incumbents anywhere (no source supports it).
  Differentiation function kept: incumbents bring their own custom structure; claim 1's
  carriage rides the crew's plain ladder. New sentence 25 words (< 35 LONGSENT band);
  paragraph stays 4 sentences. §6 header and §8 "guided carriage" callback (essay's
  concept for claim 1, round-1 SA-FIX-4 ruling) untouched.

### SA3-FIX-2 — grounding round-3 PARAPHRASE-DRIFT #41 (mechanical) — "electrical" de-invented

- §5 (line 67), old: "A tray on the carriage forms a slot that holds long stock like
  electrical conduit, so it..."
- §5 new: "A tray on the carriage forms a slot that holds long stock like conduit,
  so it..."
- Ground: the patent says only "conduit" ([0063]; [0061] "item 842 (e.g., a conduit)").
  The finding cited §5/§8, but draft_version 4 carried exactly one "electrical conduit"
  (§5 body); the FIG. 8A caption already used bare "Conduit (842)". Residual
  "electrical conduit" = 0 across essay-final, essay-draft, publication.

## Log-and-drop (one line each, origin: self-post-accept round 3, no edit)

- sa3-A-2 (medium, five caption-only figures) — logged, no edit; deliberate caption-only convention (round-1 ruling), posting-checklist encodes the five embeds; recurring.
- grounding "rails" rows #14/#22/#47/#51 (recurring paraphrase family) — logged, no edit; verifier-classified defensible vs [0044]/[0053] "minor sides", low.
- sa3-A-3 (low, market-floor from two vendors) — logged, no edit; same drop as sa2-A-4.
- sa3-A-4 (low, [0005] OCR space mismatch) — logged, no edit; same drop as sa2-A-9.
- sa3-A-5 (low, "reads on" unglossed) — logged, no edit; adjacent to protected signature line 2 (same as sa2-A-7).
- sa3-A-6 (low, "fly section" unglossed) — logged, no edit; inside verbatim [0024] quote.
- sa3-A-7 (low, §1 noun-phrase header) — logged, no edit; settled surface, third recurrence.
- sa3-A-8 (low, "already own(s)" echo in §4) — logged, no edit; signature line 1 owns the motif.
- sa3-A-9 (low, "the previous section" self-reference) — logged, no edit; exempt scope-disclaimer class.
- sa3-A-10 (low, title tense) — logged, no edit; owner-accepted title register, propose-only.

## Bookkeeping (round 3)

- draft_version: 4 → 5 in handoff/03-edit/essay-final.md and handoff/02-compose/essay-draft.md
  (byte-identical, verified by cmp).
- publication.md regenerated: `python3 .claude/skills/_shared/scripts/strip_publication.py
  handoff/02-compose/essay-draft.md -o handoff/02-compose/publication.md`.
- Word count: 2375 → 2383 (draft, +8); publication 2357 → 2365 (+8).
- Gates: OVERALL PASS, zero findings from any gate (15/15 PASS, 0 FAIL, 0 WARN).
- Residuals: "electrical conduit" 0; incumbent-attributed "guided carriage" 0
  (essay-final, essay-draft, publication).
- Signature lines: all three untouched, each appears exactly once in essay-final.md and
  publication.md.
- DRY declared at cap: self-audit round 3 was the final apply round; no further
  self-audit edits to this draft.
