---
name: prose-polish
description: "Phase 3.7 Polish (윤문): the final plain-language pass for the general reader. Runs AFTER double-clean acceptance and self-audit closure, BEFORE archiving (or standalone on an archived essay via the human-post-accept channel). Jurisdiction is surface-only: split long or nested sentences, swap formal/latinate words for plain ones, smooth transitions, add a short grounded gloss where a term of art lands cold — while preserving, byte-for-byte where marked, every fact, number, date, name, [dddd] anchor, verbatim quote, blockquote, signature line, verb of certainty, and stance. Never adds or removes a factual claim; never re-hedges or un-hedges; never touches the Sources block. Output: polished essay + polish-notes.md (per-edit before/after) + gates re-run PASS + drift verification by a pinned-cheap instrument. Use when a finished essay needs 윤문, plain-language polish, readability smoothing for the public. NOT for: fact fixes (composer revision mode), editorial findings (editorial-review), thesis or structure changes."
context: fork
agent: prose-polish
---

# prose-polish (윤문)

**Contract:** `contracts/stages/polish.yaml`

Phase 3.7. The pipeline's passes defend accuracy, structure, and energy; this pass defends
the GENERAL READER's ear (owner decision 2026-07-05: 대중 독자를 위한 문장·표현 다듬기).
It runs when the text is already true and well-argued, and makes it easier to read without
letting it become less true.

```
essays/<id>/essay-final.md  (accepted + self-audit DRY)      [or handoff/03-edit/essay-final.md pre-archive]
  + handoff/02-compose/thesis-trace.md   (## Signature lines: byte-protected exact strings)
  + _shared/references/reader-profile.md (the target ear)
    -> essay-final.md (polished, draft_version bumped)
    -> handoff/03-edit/polish-notes.md   (every edit: before / after / why-plainer)
    -> gates re-run: 14/14, zero NEW findings (warns included)
    -> drift verification: grounding-verifier-class instrument over every changed sentence
    -> publication re-strip (strip_publication.py)
```

## Jurisdiction (hard)

ALLOWED, sentence by sentence:
- Split a long or nested sentence into two or three; target the reader-profile ear
  (advanced high school – early undergraduate), ~15-25 words per sentence.
- Swap a formal, latinate, or trade word for the plain one (assignee → the company that
  owns it; concedes → admits; utilize → use) UNLESS it is claim language, a term of art
  the essay glossed, a part number, or inside a quote.
- Reorder within a sentence for subject-first flow; smooth a transition.
- Add a short gloss for a term that lands cold, GROUNDED in what the essay already says
  (a gloss is a restatement, never a new fact).

FORBIDDEN, no exceptions:
- Adding, removing, strengthening, or weakening any factual claim; changing any number,
  date, name, patent number, or figure reference; changing a verb of certainty
  (asks for / claims / describes stay exactly as strong as they are).
- Touching anything inside double quotes or blockquotes (verbatim source text), the
  `[dddd]` anchors (each anchor stays attached to the sentence carrying its fact — when
  a sentence splits, the anchor stays with the clause that carries the anchored fact),
  the Sources block, the frontmatter (except `draft_version`), or image/caption figure
  numerals.
- Touching a declared signature line (thesis-trace `## Signature lines`): byte-protected.
- Re-hedging or un-hedging anything (gate_hedge / 6G / 6I territory, not polish
  territory); changing stance, order of sections, or headers' claims (a header may be
  simplified only if its claim survives word for word in meaning).

## Process

1. Read the essay, thesis-trace signature lines, reader-profile. List the sentences that
   would make a general reader stall: length, nesting, cold jargon, abstract subjects.
2. Edit sentence by sentence within the jurisdiction. Prefer MANY SMALL edits over
   rewrites: the accepted text earned its acceptance.
3. Log EVERY edit in `handoff/03-edit/polish-notes.md` as `## polish` blocks
   (before / after / why-plainer), so the drift check and the ledger have the full diff.
4. Bump `draft_version` in the frontmatter.
5. Re-run the full gate suite with the run's context files: must stay PASS with zero new
   findings (warns included). A polish that wakes a gate gets reverted, not argued with.
6. **Drift check (two-step; AUD-W7).** Produce the changed-sentence list (from
   polish-notes) and return `drift-check PENDING` to the orchestrator. Do **not** spawn
   the verifier yourself. The orchestrator forks a grounding-verifier-class instrument
   (pinned cheap model) on every old/new pair: meaning preservation, protected-surface
   integrity (numbers, dates, names, anchors, quotes, certainty verbs), signature-line
   byte-identity. Any `MEANING-CHANGED` or `PROTECTED-TOUCHED` ⇒ orchestrator re-forks
   polish to revert that sentence and re-run step 5.
7. Re-strip `publication.md` (strip_publication.py) and sync the posting-checklist word
   count. On archived essays, log the round in score-history.md and revision-notes.md
   (`origin: polish`).

## Model allocation

The pen is the session's strongest model (`model: inherit`, same owner rule as the
composer and promo copy). The drift verification is retrieval-shaped and runs on a
pinned-cheap instrument (grounding-verifier pattern).

## Out of scope

- Anything a gate or editorial pass owns: grounding, figures, hedge symmetry, attention
  budget, format. Polish runs LAST precisely so it cannot relitigate those.
- The Korean owner briefing and promo pack (own registers; promo already writes for the
  feed, the briefing for the owner).
- Voice-canon changes; new signature lines; title changes beyond word-level smoothing
  within SURF-001's budget.
