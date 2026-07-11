# Cold-eyes audit: the human owner's understanding

**Lens:** The owner is a Korean retail-investor-audience publisher who must (a) judge the final
essay before posting, (b) answer reader objections for days afterward, (c) write short Korean
promo posts — all requiring the OWNER to understand the patent, not just the pipeline.

**Evidence base:** CLAUDE.md; docs/architecture/reader-first-overhaul.md; SKILL.md for
patent-essay, thesis-architect (+ invention-summary-schema.md), essay-en-composer,
editorial-review, pipeline-retro; _shared/references/ skim; ground truth =
essays/etched-us20240378175-r2/ (71 tracked files).

**Headline finding:** The pipeline is a self-verifying machine that produces a reader-grade
essay and an agent-grade evidence trail — and consumes owner understanding at input time
(the owner authors a 12KB expert English briefing, `essay-context.md`) without ever producing
owner understanding at output time. Of ~32 artifact types, ~7 are human-facing, and zero are
designed to transfer patent comprehension to the owner. The one artifact family that would
arm the owner for post-publication defense (the steelman, the anchor-by-anchor fidelity
table, the claim scope map) exists but is buried under loop-jargon filenames, unindexed,
English-only — and its anchors point into a patent text that is not in the tracked archive.

---

## 1. Artifact audience map

Legend: **M** = downstream machine phase, **L** = reviewer/orchestrator loop, **H** = human
owner plausibly expected to READ (or write). Language: everything is English prose/tables
unless noted; Korean appears only vestigially.

### Phase 0 — Figures (3 types) — M:3, L:0, H:0
| Artifact | Consumer | Notes |
|---|---|---|
| `input/figures/fig-NN.png` | M (composer, gates, publication-package) | reused by human only at paste time via publication-package |
| `figures-manifest.md` | M (Phase 1, gates) | vision-verified, human-legible but never surfaced |
| `figures-index.txt` | M (gates) | bare list |

### Phase 1 — Design, `handoff/01-design/` (10 types) — M:9, H-decision:1, H-latent:3
| Artifact | Consumer | Notes |
|---|---|---|
| `invention-summary.md` | M (composer's ONLY patent source; pass-3; gate_quotes) | **Nominally human**: schema says "Markdown chosen for human-edit-friendly handoff (SETI can correct extraction errors directly)". Reality in r2: 289 lines, 43-row quote-anchor table, English body under vestigial Korean headers (발명 명칭/기술분야, 종래 문제/과제, 청구항 분석, 유리한 효과). A QA affordance, not a briefing. The de-facto patent dossier. |
| `thesis-spine.md` | M (composer), L (pass-4) | contains §Adversarial defense — steelman + mitigation + residual risk. The best owner asset in the repo; never surfaced to the owner. |
| `thesis-candidates.md` | L/audit | SKILL says "SETI selects one"; orchestrator auto-selects, surfaces "in one line (human can override)" |
| `title-lead-candidates.md` | **H (the one real decision point)** + M | 5 register pairs; r2 score-history confirms "human-selected from 5 Phase-1 candidates" |
| `figure-selection.md`, `figure-rationale.md` | M (composer) | |
| `fact-check-log.md` | L (pass-3, grounding-verifier) | external facts + URLs + evidence_level — latently useful to owner, unadvertised |
| `search-log.md` | audit | |
| `phase2-handoff-notes.md` | M (composer) | mixed-language section spec ("(e) Open questions ... awaiting SETI / orchestrator"); contains claim-scope do/don't traps |
| `figures-index.txt` | M (gates) | |

### Phase 2 — Compose, `handoff/02-compose/` (5 types) — M/L:4, H:1
| Artifact | Consumer | Notes |
|---|---|---|
| `essay-draft.md` | L (reviewer, gates) | frontmatter + [dddd] cites |
| `publication.md` | **H (paste source for X Articles)** | 2,991 words, one line per paragraph |
| `figures-rationale.md`, `thesis-trace.md` | L (reviewer; signature-line declarations) | |
| `revision-response.round-N.md` (+ selfaudit variants) | L (next reviewer, check_run) | disposition ledger per finding_id |

### Phase 3 — Edit, `handoff/03-edit/` (8 types) — L:6, H:2 (+1 owner-WRITE)
| Artifact | Consumer | Notes |
|---|---|---|
| `edit-log(.round-N).md` | L (orchestrator, composer revision, retro) | YAML findings; SKILL still says findings "supply input for SETI's revise decision" — that human role is now automated |
| `gate-result(.round-N).json` | L (orchestrator, check_run) | raw machine JSON, 14 gates, no human rendering |
| `score-history.md` | **H (final report)** + check_run | compact English table; dense loop jargon (double-clean, CAP HIT, r3-F1, SA rounds) |
| `essay-final.md` | **H (the deliverable)** + self-audit | |
| `revision-notes.md` | L (ledger normalize) + **H-WRITE** (post-publication reader-feedback channel per posting-checklist) | owner must know the `## delta` schema |
| `selfaudit-round-N-{readerA,readerB,coldreader}.md` | L (multi-vote) | persona findings |
| `selfaudit-round-N-grounding.md` | L (multi-vote) | **hidden gem**: 41–70-row table, every essay sentence → invention-summary span → patent verbatim → verdict. The only patent text preserved in the tracked archive. |

### Archive + meta (7 types) — H:3, M/L:4
| Artifact | Consumer | Notes |
|---|---|---|
| `essays/<id>/README.md` | **H** | run summary: reader_sentence, run shape, provenance — about the RUN, not the patent |
| `publication-package/posting-checklist.md` | **H (operational)** | title/cover/alt-texts/first-two-lines/paste-source/post-pub channel. Best owner artifact that exists; covers mechanics only, zero comprehension content |
| `publication-package/cover-*.png, fig-*.png` | H (upload) | |
| `essays/<id>/{gate-result.json, edit-log.md, score-history.md}` copies | H-inspectable evidence | |
| `meta/findings-ledger.jsonl` | M (retro) | JSONL |
| `meta/attribution-table.md` | L/H ("human-editable") | |
| `meta/improvement-proposals/*.md` | **H (apply decision)** | about the pipeline, not the patent |

**Counts:** ~32 artifact types → machine/loop ≈ 25, human-facing ≈ 7 (essay-final,
publication.md, posting-checklist, README, score-history, title-lead-candidates surface,
improvement-proposals). Human-facing artifacts split: 2 about the deliverable, 4 about the
run/pipeline, 1 decision prompt. **Zero about the patent for the owner.** Language: 100%
English for everything owner-facing; Korean exists only as vestigial schema headers and in
the unported v1 source-prompts.

---

## 2. Understanding verification: who is ever checked for comprehension?

**Fidelity checks (text↔text) — abundant, mechanical, well-designed:**
- `gate_quotes` (invention-summary spans verbatim-present in patent.md), `gate_anchors`,
  pass-3 verbatim verification + paraphrase-mutation classing, grounding-verifier verdicts
  (SUPPORTED / UNSUPPORTED / MISREAD / OVERREACHED-BEYOND-ANCHOR), gate_hedge/6G symmetry.
  These verify that strings match and claims stay inside anchors.

**Comprehension checks (does someone UNDERSTAND?) — exist only for agents and simulated readers:**
- Agent-side, indirect: invention-summary Layer 1–4 (What/How/Why-novel/Angles) is a
  comprehension *artifact*, but it is verified only by fidelity gates, never as comprehension.
  The two places agent understanding is genuinely exercised: the steelman rule (pass-7 +
  adversarial-defense: must be a THIS-patent objection, generic truisms = `steelman-absent` —
  you cannot fake this without understanding claim 39) and grounding-verifier's MISREAD
  verdict class (distinguishing misreading from misquoting requires comprehension).
- Reader-side, simulated: pass-5 engagement, pass-7 personas, 2 adversarial readers, and the
  cold reader's repeat-to-a-friend test (r2: reader_sentence reproduced unaided 3/3 blind
  rounds — the closest thing in the system to a comprehension verification, but it verifies a
  SIMULATED reader's takeaway of the ESSAY's surface).

**Owner-side: nothing.** The owner's three touchpoints are (1) authoring `essay-context.md`
BEFORE the run — which *presumes* deep understanding (the r2 brief contains claim-family
analysis, RCE/rejection records, reel/frame lien data, evidence tiers); (2) a one-line title
register pick; (3) receiving essay-final + score-history. No checkpoint asks whether the owner
can state the mechanism, the strongest objection, or the verdict's evidence basis. The system
verifies the essay is understandable; it never verifies the owner understood. Notably, the
editorial-review SKILL still encodes the opposite worldview ("SETI's combined sensitivity ...
operates outside single-pass inferential reach", "SETI revises → essay-final.md") — the
orchestrator automated that human role away without replacing its comprehension side-effect:
a human who applies findings by hand necessarily learns the patent; a human who receives
`ACCEPT (double-clean)` learns nothing.

---

## 3. The 3-days-later test

Scenario: a hostile-but-informed reader replies, e.g. "claim 39's no-switch hardwiring is
routine for weight-stationary designs — see the examiner's own citations" or "you misread
[0043]; the crossbar is per-HBM-stack." Owner has `essays/etched-us20240378175-r2/` only.

**What exists (and is genuinely good):**
- `handoff/01-design/thesis-spine.md` §Adversarial defense — the EXACT first objection above,
  pre-answered at full strength (8 examiner references named by assignee class, final
  rejection acknowledged, "the breadth ... is exactly what makes it shrinkable"), plus the
  mitigation line the owner should paraphrase and a falsifiable residual-risk framing (grant
  intact vs narrow-to-ornament). This is the reply, sitting on disk.
- `handoff/03-edit/selfaudit-round-3-grounding.md` — 41-row (earlier rounds 62/70-row)
  sentence→anchor→patent-verbatim→verdict table. For any "you misquoted the patent"
  objection, the row-level receipt already exists.
- `handoff/01-design/invention-summary.md` — Claim scope map (sought/open/pinned per claim),
  reference-number table, 43-row quote-anchor table, prior-art differentiation.
- `handoff/01-design/fact-check-log.md` — every external fact with URL + evidence_level.
- `essay-context.md` §Scope boundaries — the anti-hype guard rails (what was deliberately
  NOT claimed), useful against "you overclaimed" replies.

**What is missing or mis-formatted for a fast human lookup:**
1. **The patent itself is not in the archive.** `git ls-files` shows the only tracked
   patent.md is `meta/fixtures/fabricated-quote/patent.md`. Every `[dddd]` anchor in the
   essay, the 43-row quote table, and the fidelity tables point into a document the owner
   must re-fetch from USPTO/Google Patents to see full-paragraph context. (The grounding
   table's verbatim column is the only patent text preserved.)
2. **No index.** Nothing tells the owner that the steelman lives in
   `handoff/01-design/thesis-spine.md` or that the receipts live in files named
   `selfaudit-round-3-grounding.md`. README and posting-checklist describe the run and the
   paste mechanics; neither says "if challenged, look HERE."
3. **Wrong genre.** The defense material is written as pipeline QA (finding_ids, verdicts,
   errata cross-refs), not as answers. There is no "objection → 2-sentence reply → anchor"
   card. Three grounding tables exist (rounds 1–3) with no pointer to which is final.
4. **Wrong language for speed.** All English; a Korean owner composing a fast, precise reply
   gets no native-language summary of the defense or the claim-scope nuances (sought vs
   granted — the exact distinction a hostile reader will probe).
5. The posting-checklist routes post-publication EDITS into revision-notes.md (good ledger
   hygiene) but provides zero support for post-publication ANSWERS.

Verdict: the owner would win the argument IF they knew the repo layout and loop vocabulary —
the pipeline defended the essay brilliantly against a simulated version of this reader and
then filed the transcript where only the pipeline can find it.

---

## 4. The promo test (200-char Korean promo)

**What exists today:**
- Nothing purpose-built. Phase-4 `promo-composer` exists only as
  `docs/source-prompts/04-promote/` — a v1, Korean-instruction spec for a 280–340-word
  FT/Economist-register X digest — explicitly "preserved for a future port" (CLAUDE.md);
  essay-en-composer lists promo as out of scope, and v2 "deliberately drops
  tech-essay-ko-pub" (the Korean output path). So neither promo nor Korean exists in v2.
- Partial raw material, all English, scattered: the `reader_sentence` (README + essay-context —
  a ready-made hook, literally designed as "the one sentence the reader wants to say"), the
  59-char title, ≤3 declared signature lines (`handoff/02-compose/thesis-trace.md`), the
  first-two-lines preview in posting-checklist.

**What is missing:**
1. A promo artifact of any length; the ported pipeline ends at the posting checklist.
2. Any Korean rendering of anything.
3. A **safe-claims card**: the loop spent SA-1/SA-2 scrubbing exactly the errors a
   memory-written promo would re-commit — "on stage"→"thread" (venue, 6 fixes incl. a
   signature-line rewrite), "both co-founders"→"two of its co-founders", the two-vs-three
   years arithmetic. An owner compressing to 200 Korean characters from memory of the hype
   thread plausibly resurrects all three; nothing hands them the corrected, quote-safe
   phrasings (the errata live inside edit-logs and thesis-spine revision notes).
4. Anchor discipline for the promo: the essay's every claim is anchored; the promo — the
   most-shared, least-defended text — is governed by nothing.

---

## 5. Assumed-knowledge inventory (what the owner must already know or do unaided)

1. **Author a professional English framing brief** (`input/essay-context.md`): the r2 run's
   control document is ~12KB of English with `evidence_level: registry-extract` tiers,
   edition rules, and per-fact sourcing — the pipeline's quality ceiling is set by this
   owner-authored input.
2. **US patent-prosecution literacy, ungloseed internally**: final rejection, RCE, office
   action, reel/frame assignment records, security interests, DOCDB/WIPS exports,
   pending-vs-granted claim discipline. The ESSAY glosses these for readers; the internal
   artifacts the owner would consult do not.
3. **Claim-scope vocabulary**: locked/open/pinned map semantics, the sought-* application
   class, why a pinned point is never a "floor" — needed both to author essay-context and to
   answer scope objections.
4. **Loop/QA jargon to judge quality**: finding_id lifecycle (r1-F1, sa2B-F2), severity
   model, double-clean vs CAP HIT, dispositions, confirmation rounds, postures, energy
   registers, gate check_ids (QUOTE-001, FIGUSE-001, SURF-00N) — all required to read
   score-history.md and edit-log.md, the only quality evidence surfaced.
5. **Read raw gate JSON**: gate-result.json is unrendered machine output (14 gate objects,
   warn/fail semantics).
6. **Repo cartography**: knowing the steelman is in thesis-spine.md, receipts in
   selfaudit-round-N-grounding.md, corrected phrasings in edit-logs, paste source is
   publication.md not essay-final.md (posting-checklist does cover this last one).
7. **Re-fetch the patent**: full-paragraph context for any anchor requires going back to
   USPTO/Google Patents — the archive doesn't carry patent.md.
8. **Digest a 289-line dossier**: the only bridge between the 2,991-word essay and the
   patent is invention-summary.md with its 43-row quote table; no owner-sized digest exists.
9. **Korean is entirely the owner's problem**: promo, any Korean-audience social layer, and
   fast native-language comprehension have zero support in v2.
10. **Know the revision-notes `## delta` schema** to log post-publication reader-driven
    edits so the ledger "keeps learning" (posting-checklist names the channel, not the format).
11. **Exercise the "SETI catch overrides" doctrine with no hook**: the system still assigns
    the human final editorial authority (editorial-review SKILL) but provides no checkpoint,
    checklist, or briefing where that authority is exercised before posting.

---

## 6. Top 5 gaps, ranked

### Gap 1 — No owner-understanding artifact (hits a, b, c)
The pipeline produces a reader-grade essay and an agent-grade dossier, nothing for the
owner-as-defender: no brief stating the mechanism in five bullets, the steelman + reply, the
three numbers that matter, what was deliberately not claimed, and the open low finding
(r3-F1 lives only inside edit-log round 3). Failure: (a) signoff by vibes, (b) slow or wrong
replies, (c) promo drafted from memory.
**Remedy shape:** a generated `essays/<id>/owner-brief.md` (arguably bilingual EN/KO),
assembled mechanically from spine §Adversarial defense + claim scope map + errata + open
findings + reader_sentence.

### Gap 2 — Defense material buried, unindexed, and anchored to an untracked patent (hits b)
The steelman, fidelity tables, claim scope map, and fact-check log answer most objections but
sit under loop-jargon paths; patent.md itself is absent from the tracked archive, so every
anchor dangles for a human. Failure: (b) days of exposure while the owner re-derives or
re-fetches what the pipeline already proved.
**Remedy shape:** track `input/patent.md` (+ essay-context) into `essays/<id>/` and add an
owner index / FAQ table ("objection class → file → section → anchor") to README or the
posting checklist.

### Gap 3 — Promo layer unported, no Korean, no safe-claims card (hits c)
Phase 4 exists only as a v1 source prompt; v2 dropped all Korean output. The specific error
classes the loop scrubbed (venue, founder count, year arithmetic) are the ones a 200-char
memory-written promo re-commits, and the corrected phrasings are filed in edit-logs.
**Remedy shape:** port promo-composer as a post-accept phase emitting an anchored promo pack
(EN + KO, digest + short-post lengths) plus a quote-safe claims card sourced from the final
errata.

### Gap 4 — Quality judgment delivered as loop evidence, not a human decision surface (hits a)
Score-history/gate JSON prove the loop ran; nothing tells the owner what to personally verify
before posting (deferred findings, contentious dispositions, CAP-HIT semantics, what the cold
reader stumbled on). The posting checklist covers paste mechanics only; the "SETI catch
overrides skill output" authority has no operational moment.
**Remedy shape:** a pre-post signoff checkpoint — README acceptance section listing open/
deferred/split findings in plain language + an explicit "owner confirms" step in the
orchestrator before archive.

### Gap 5 — The pipeline consumes owner understanding at input and the human-role contracts have drifted (hits a, b)
essay-context.md presumes expert pre-run understanding; editorial-review still says "SETI
revises → essay-final.md" and thesis-architect says "SETI selects one" while the orchestrator
auto-selects and auto-revises — the comprehension the human used to gain by doing those jobs
now accrues to forked agents. The only surviving interaction is a title pick.
**Remedy shape:** reconcile SKILL human-role language with orchestrated reality and add one
deliberate comprehension checkpoint (a 5-question owner interview at spine-lock or
acceptance: mechanism, novelty, steelman, verdict basis, weakest anchor).

---

## Credit where due (so the gaps read as gaps, not blindness)

- `publication-package/posting-checklist.md` is a genuinely owner-shaped artifact: paste
  source, cover choice, alt texts, feed-preview verification, post-pub edit channel.
- `title-lead-candidates.md` + the human register pick is a real, well-designed human
  decision point (and r2's README records the human made it).
- The self-audit grounding tables and the spine's adversarial defense are exceptional
  material — the failure is distribution, not production.
- The `revision-notes.md` human-post-accept channel means owner corrections feed the ledger:
  the meta-loop already treats the owner as a finding source; it just never treats them as a
  comprehension target.
