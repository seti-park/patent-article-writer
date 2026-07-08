---
proposal_id: 2026-06-26-human-revision-blindspots
created: 2026-06-26T00:00:00Z
status: applied (run 045, user-authorized, regression-gated)
lever: multi (reference-edit + rubric-tuning + new-capture-mechanism)
goal: "3,4a,4b"
root_cause_stage: edit + architecture
root_cause_artifact: editorial-review 6-pass rubric (blind spots) + no human-revision feedback channel
recurrence_count: 1
confidence: high
triggering_findings:
  - essay_id: 045-agility-638-last-mile-moat
    source: human-revision-delta (v2..v2.4, applied AFTER the inner loop returned overall_assessment == pass)
---

## Applied (2026-06-26, user-authorized + regression-gated)

Most of this was **implemented this session**, not left propose-only (SETI authorized direct
application and `meta/regression.py` passes):

- **4 new self-check gates** built, tested (47/47), wired into `run_gates.py`: `gate_meta`
  (META-001 fail / META-002 warn), `gate_stub` (STUB-001), `gate_cashtag` (CASH-001), `gate_dupe`
  (DUPE-001). They catch the run-045 hand-fixed flaws on flawed input and pass the v2.4 final.
- **Prevention references**: `anti-ai-writing.md` (meta category + gate_meta mirror),
  `section-blueprint.md` (BLUF / claim-headers / steelman beat / no-stub + `header` field),
  `x-articles-format-en.md` (claim-first headers, "What X" deprecated; `$`cashtag),
  `deliverable-voice-rules.md` (meta / BLUF / jargon-signpost / stub-dupe-cashtag).
- **Registration**: `scoring-rubric.md` (Layer-1 table + goal matrix + pass-7 + richer `/goal`),
  `attribution-table.md` (9 rows), `scripts/README.md`, `CLAUDE.md` (6→10 gates), and
  `editorial-review` **pass-7 adversarial reader** (`references/pass-7-adversarial-reader.md`).

**Now applied too (2026-06-26):** the **revision-delta capture channel** —
`handoff-template/03-edit/revision-notes.md` (convention + run-045 worked example),
`meta/normalize_revision_notes.py` (deterministic normalizer with `--selftest`),
`pipeline-retro` second-input wiring, the ledger-schema `origin` field, and the ledger seeded
with run 045's 9 `human-post-accept` deltas (53 → 62); and the `steelman-absent` upstream
wiring into `thesis-architect/references/adversarial-defense.md` (§D steelman beat carried into
`phase2-handoff-notes`).

## Headline: the meta-loop is blind to human post-acceptance editing

`pipeline-retro` normalizes the **inner Compose↔Edit loop** only. Per `scoring-rubric.md`
(Loop ↔ retro hand-off) the orchestrator hands retro the `edit-log.md` + gate result + score
history. But the editorial-review flow is `... → edit-log.md → SETI revises → essay-final.md`
(editorial-review/SKILL.md:17): the **revision itself is human and happens after the loop
terminates**, and any further human rounds on `essay-final.md` are never captured.

Run 045 passed every gate and reached `overall_assessment == pass`, then a human (SETI) took
the accepted draft through **five more rounds (v2 → v2.4)** of high-value editorial change.
None of it touched a gate or an edit-log finding, so **none of it reached the ledger.** Those
edits are not noise — they are precisely the editorial dimensions the 6-pass review does not
yet score. This proposal (a) records that lost signal, (b) inventories the new finding-classes
it exposes, and (c) proposes the missing capture mechanism so future runs learn it
automatically instead of re-discovering it by hand each essay.

## Evidence base — the run-045 revision delta (v2 → v2.4)

Captured from the session transcript (this is the dataset the proposed mechanism would
normalize on its own):

| Round | Human change | Lesson / new class |
|---|---|---|
| pre-v2 | Lead deferred the thesis to a question ("what fences a competitor out?"); rebuilt to state the verdict in para 1 | `lead-thesis-deferral` (BLUF) |
| v2 | Section headers were half-label ("What '638 Actually Claims"); rewritten so headers alone reconstruct the argument | `nonclaim-section-header` |
| v2 | Added a steelman beat conceding "workflow-claim = deliberate breadth strength" before refining ("a fence is not an engine") | `steelman-absent` |
| v2.1 | Restructure introduced "the tell" in the lead, duplicating "the clearest tell" in §4 | `revision-induced-duplication` |
| v2.1 | Ticker written `AGLT` → `$AGLT` (X cashtag) | `venue-ticker-convention` |
| v2.2 | Removed 5 meta/persona phrases ("Read it the way an examiner would", "the timeline is the first clue", "Everything below is the reading…", "…the rest of this essay", "Watch how the patent handles each") | `meta-reader-instruction` / `essay-self-reference` |
| v2.3 | §3 compressed: the two-axis verdict was stated ~5× (lead, §1 steelman, §1 button, §3, §5) | `thesis-restatement-redundancy` (refines `redundancy-bloat`) |
| v2.3 | §101 doctrinal quote ("generic computer implementation … 'not significantly more'") cut; short signpost (Section 101 / Alice) kept | `jargon-overdepth` (complement of existing `jargon-gloss-gap`) |
| v2.4 | Compressed §3 became a 4-sentence stub; merged §3+§4 into "The Territory Is Not the Moat" | `section-stub-imbalance` |

## Blind-spot inventory (proposed new finding-classes)

Routing follows the attribution-table convention (class → goal → owner stage/artifact →
lever) and **preserves the voice fence**: every voice/style item routes to
`anti-ai-writing.md` / `deliverable-voice-rules.md` / a composer reference — never
`voice-profile.md`.

1. **`lead-thesis-deferral`** — goal 4a/3 — owner: design/compose — `thesis-spine` arc +
   `essay-en-composer/section-blueprint.md` lead block + editorial pass-6. For analytical /
   diligence mode the lead must state the verdict in para 1 (claim-then-proof), not defer it to
   a question. Mode/posture-aware: a magazine-narrative piece may legitimately defer. Lever:
   reference-edit (blueprint lead directive) + rubric (pass-6 lead-altitude check).

2. **`nonclaim-section-header`** — goal 4a/3 — owner: compose — `section-blueprint.md`. Section
   headers must be assertions, such that a header-only skim reconstructs the argument. Run 045
   skeleton after fix: *workflow-not-robot → disclaims-the-hard-parts → territory-is-not-the-moat
   → moat-is-filed-elsewhere*. Lever: reference-edit + pass-6 header-as-claim check.

3. **`meta-reader-instruction` / `essay-self-reference`** — goal 4b/3 — owner: canon —
   `anti-ai-writing.md` (new rhetorical-pattern category, distinct from word-level banned
   terms) + pass-1 / pass-5. Ban reader-instruction and essay-self-reference: "read it the way
   an X would", "watch how", "notice that", "as we'll see", "everything below", "the rest of
   this essay", "in this essay". Several are grep-able → **gate-promotion candidate** (like
   em-dash) once the phrase list stabilizes. Lever: reference-edit now, gate-promotion later.

4. **`jargon-overdepth`** — goal 3 — owner: compose/canon — `deliverable-voice-rules.md` +
   pass-5. The complement of the existing `jargon-gloss-gap` (jargon with no gloss): here the
   problem is a domain term-of-art *deep-dived* past the insight. Rule: keep the short signpost
   the target reader scans for (Section 101, Alice), cut the doctrinal explanation only a
   specialist needs. Lever: reference-edit + pass-5 reader-perspective check.

5. **`steelman-absent`** — goal 1/4a — owner: design→compose — `thesis-architect`
   adversarial-defense must flow into `phase2-handoff-notes` as an explicit "concede-then-refine
   the strongest counter" beat, and `section-blueprint.md` must allocate that beat. Run 045: the
   strongest pro-subject counter ("isn't workflow-claiming the smart, broad move?") was only
   surfaced by the reader, not pre-rebutted. Lever: reference-edit + pass-4 (does the draft
   rebut its strongest counter?).

6. **`section-stub-imbalance`** — goal 4a/3 — owner: compose — `section-blueprint.md`
   `word_target` balance + pass-5 rhythm (complement of `mobile-paragraph-wall`, which is the
   too-long end). Flag a section much shorter than its siblings; recommend merge/expand. Run
   045: compressed §3 (4 sentences) → merged into §4. Lever: reference-edit + pass-5.

7. **`thesis-restatement-redundancy`** — goal 3 — owner: compose — refines the held-at-watch
   `redundancy-bloat` (now 6/6, deliberately un-promoted because heterogeneous). This is a
   *nameable sub-mechanism*: the same thesis claim restated across N sections. A concrete
   pass-2 sub-check (count distinct sections asserting the core verdict; flag > 3) is more
   tractable than the umbrella class. Lever: rubric-tuning (pass-2 sub-check).

8. **`revision-induced-duplication`** — goal 4b/3 — owner: edit/compose — sibling of the
   existing `revision-induced-band-break` (watch, 2). A revision must re-scan the **whole
   document** for newly-created word/phrase duplication, not only the changed span. Run 045: the
   restructure introduced "the tell" twice. Lever: rubric-tuning (revision-mode re-scan step in
   `essay-en-composer` revision mode + pass-2).

9. **`venue-ticker-convention`** — goal 4a — owner: compose — `x-articles-format-en.md`.
   Venue-native formatting: stock ticker as `$AGLT` cashtag on first mention for X Articles.
   Mechanical → small gate-promotion candidate. Lever: reference-edit (or gate-promotion).

## The fix that makes all of the above self-sustaining: revision-delta capture

The blind-spot inventory above had to be assembled by hand from the chat transcript. Without a
capture channel, every future essay repeats that. Proposed mechanism (pick one; ascending cost):

- **(a) `handoff/03-edit/revision-notes.md` convention (lightest).** When SETI edits
  `essay-final.md` beyond the edit-log findings, log `{before, after, rationale}` lines. Extend
  `pipeline-retro` to read this file as a second input class ("human-revision findings") and
  normalize it into the ledger with `source: human-revision-delta`. One new doc + a few lines in
  the retro skill. **Recommended first step.**
- **(b) Stop-hook snapshot.** A `Stop` hook snapshots `essay-final.md` on each turn so the
  cross-round delta (v2→v2.3→v2.4) is recoverable even if notes are skipped; retro diffs the
  snapshots. Catches edits SETI forgets to log.
- **(c) `revision-retro` step.** A dedicated normalization pass that diffs
  `essay-final.md` against the edit-log-applied draft, classifies each hunk against this
  inventory, and emits ledger findings — the human-edit analogue of what `pipeline-retro` does
  for machine findings.

Channel design note: human-revision findings should be tagged distinctly
(`origin: human-post-accept`) so the recurrence counts don't conflate "the loop missed it" with
"the loop never had a chance to see it." Both are useful, but they motivate different fixes —
the first tunes a pass, the second extends coverage.

## Proposed attribution-table rows (additive; human applies)

```
| `lead-thesis-deferral` | pass-6 6A + human-revision | 4a | design/compose | thesis-spine arc / section-blueprint lead block | reference-edit |
| `nonclaim-section-header` | pass-6 + human-revision | 4a | compose | section-blueprint header directive | reference-edit |
| `meta-reader-instruction` | pass-1/pass-5 + human-revision | 4b | canon | anti-ai-writing.md (rhetorical-pattern category) | reference-edit → gate-promotion |
| `jargon-overdepth` | pass-5 + human-revision | 3 | compose | deliverable-voice-rules.md | reference-edit |
| `steelman-absent` | pass-4 + human-revision | 1 | design | thesis-spine adversarial-defense → phase2-handoff-notes | reference-edit |
| `section-stub-imbalance` | pass-5 + human-revision | 4a | compose | section-blueprint word_target balance | reference-edit |
| `thesis-restatement-redundancy` | pass-2 + human-revision | 3 | compose | section-blueprint (sub-mechanism of redundancy-bloat) | rubric-tuning |
| `revision-induced-duplication` | pass-2 + human-revision | 4b | compose | essay-en-composer revision-mode re-scan | rubric-tuning |
| `venue-ticker-convention` | pass-6 + human-revision | 4a | compose | x-articles-format-en.md | reference-edit |
```

## Proposed editorial-review pass additions (rubric-tuning)

- **pass-1** (voice + anti-ai): add the meta-instruction / self-reference grep alongside the
  word-level banned grep.
- **pass-2** (redundancy): add a cross-section thesis-restatement count (flag the core verdict
  asserted in > 3 sections) — the tractable face of `redundancy-bloat`.
- **pass-5** (reader perspective): add meta-posturing, `jargon-overdepth`, and
  `section-stub-imbalance` (rhythm: too-short complement of paragraph-wall).
- **pass-6** (lead/conclusion + format): add the BLUF lead-altitude check (does para 1 state
  the verdict in analytical mode?), the header-as-claim check, and the cashtag convention.

These belong in the rubric, not (yet) the gates: most are judgment-level. The two mechanical
ones — the meta-phrase blacklist and the cashtag pattern — are gate-promotion candidates once
their lists stabilize, exactly the `em-dash` / `banned_terms.txt` precedent.

## Regression / apply

Propose-only. Apply per-item after `python meta/regression.py` passes. Reference-edits
(blueprint, anti-ai, voice-rules, format, attribution rows) are low-risk text additions; the
mechanism in the "self-sustaining" section is the one structural change and should land first,
because it converts this hand-assembled list into an automatic input for run 046+.
