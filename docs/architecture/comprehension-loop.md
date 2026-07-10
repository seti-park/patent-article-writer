# Design: Comprehension Loop — understand_confirm as an active, two-way check

**Status:** PROPOSED (design only; not yet implemented)
**Author:** architect session, 2026-07-11
**Depends on:** the STOP/CONFIRM checkpoint protocol (`.claude/skills/patent-essay/SKILL.md`), the understand stage (`contracts/stages/understand.yaml`), the owner study pack (`.claude/skills/patent-understand/references/owner-study-pack-schema.md`).

---

## 1. Why

Today `understand_confirm` is a **passive** checkpoint. The orchestrator RENDERs the
study-pack triad, ASKs one yes/no question — *"Can you restate Problem, Solution
(incl. claim scope), and Benefits?"* — STOPs, and RECORDs on any affirmative. Two
things go unused:

1. **The Owner's understanding is never measured, only asserted.** A tired "yes" passes
   the gate. The checkpoint's whole reason to exist (per invariant 4: *the Owner should
   not have to re-study the raw patent under deadline*) is only nominally served.
2. **The checkpoint never tests the model.** The frozen patent model
   (`invention-summary.md`, `owner-study-pack.md`) is Claude's reading. If Claude
   misread the claim scope, nothing at this boundary catches it — the error propagates
   into design → compose → the published article.

The comprehension loop turns the single ASK into a short **interactive quiz + teach**
loop that (a) confirms the Owner can actually teach the patent back, and (b) uses the
dialogue as a **second, human-in-the-loop audit of Claude's own reading**, correcting the
frozen model *before* it is frozen for design.

The scaffolding already exists, unused: `owner-study-pack.md` §5 *"Self-check (답이 이미
위에 있음)"* is five questions whose answers are already in the pack. Today they are
printed for the Owner to read silently. This design makes them **keyed, asked, and
graded**, and adds a correction channel.

## 2. The core insight — two signals, not one

The dialogue produces **two distinct kinds of signal**, and conflating them is the main
design risk:

| Signal | What it is | Where it flows | Changes facts? |
|---|---|---|---|
| **model-correction** | Owner pushback reveals Claude misread the patent (wrong claim scope, invented benefit, mislabeled figure) | back into the understand artifacts → **re-freeze** | YES — corrects the frozen model |
| **explanation-prior** | What the Owner found confusing; which framing/analogy landed; what they consider the crux | forward into a new artifact design & compose read | NO — never changes a fact, only *how it is explained* |

The **explanation-prior** channel is the higher-value half and the part that does not
exist anywhere today. It converts the Owner's live learning process into calibration data
for the writing: *the reader will stumble here; lead with this framing; this analogy
clicked.* This is exactly the "optimize the sub-agent instructions" the loop is for — it
is not a fact edit, it is a **teaching brief** for the downstream lanes.

## 3. Where it sits

**Not a new stage.** It is an optional *mode of the `understand_confirm` checkpoint*, run
after the understand artifacts pass their gates and before RECORD. Modeling it as a stage
would duplicate the checkpoint's STOP semantics; modeling it as a checkpoint mode reuses
the STOP/CONFIRM protocol as-is (each question is one ASK→STOP→reply turn).

```
understand (worker builds triad + quiz bank)
   → gates (gate_quotes) pass
   → understand_confirm checkpoint:
        comprehension loop  ← this design (optional; RENDER→ASK→STOP per question)
        → RECORD (by: owner) with the comprehension result quoted in notes
   → design
```

Generation of the question bank is **understand-stage worker** work (it reads the frozen
study pack, which the worker already produced). Driving the interactive loop is
**orchestrator** work (workers cannot address the Owner — the OWNER_QUESTION-relay lesson;
the orchestrator owns every Owner-facing turn).

## 4. Mechanics

### 4.1 The question bank artifact — `comprehension-quiz.md`

The understand worker emits `handoff/00-understand/comprehension-quiz.md`, an upgrade of
the study pack's §5 self-check into a **keyed** bank. Each item is derived from a triad
aspect and its answer is already in the study pack (no new facts):

```markdown
# comprehension-quiz

<!-- Keyed bank derived from owner-study-pack.md §5. Answers trace to the pack;
     no new facts. The orchestrator asks these one at a time at the checkpoint. -->

## Q1  (aspect: Problem)
question: 이 특허가 출발점으로 삼는 문제는?
options:
  A: …
  B: …   # correct
  C: …
key: B
rationale: owner-study-pack §2 "Problem" — "<verbatim span the answer rests on>"

## Q2  (aspect: Solution / claim scope)
...
```

Coverage requirement: at minimum one item per triad aspect **Problem / Solution (claim
scope) / Benefits / Boundary** (the four the study pack already fences). The claim-scope
item is mandatory — it is the most-misread aspect and the one whose error is costliest
downstream.

### 4.2 The loop (orchestrator-driven)

Per question, in order:

1. **ASK** — RENDER the question + options inline; STOP (end the turn; wait for the Owner).
2. **GRADE** — on the Owner's reply, compare against `key` (mechanical, decidable).
   - Correct → advance.
   - Incorrect → **TEACH**: render the `rationale` (which quotes the study-pack span the
     answer rests on), then re-ASK a *paraphrased* form of the same item once. A second
     miss does not fail the Owner — it is logged as an **explanation-prior** ("this aspect
     did not land") and the loop advances.
3. **PUSHBACK CAPTURE** — at any point the Owner may reply not with a letter but with a
   correction ("that's not what the claim covers — it's limited to X"). This is a
   **model-correction candidate** → §4.4.

### 4.3 The decidable pass condition (`/goal` predicate)

The loop is a `/goal`-style run-until-met loop. The completion predicate is **hard and
mechanical** — this is deliberate, to avoid the "undecidable boundary" failure class the
loop audit repeatedly flagged (a checkpoint whose exit condition is vibes is a checkpoint
that does not gate):

> **PASS** ⇔ every mandatory aspect (Problem, Solution/claim-scope, Benefits, Boundary)
> has at least one item answered correctly on the first or second try, **OR** the Owner
> explicitly opts out with the phrase the checkpoint offers ("I'll confirm without the
> quiz").

Both paths lead to RECORD. The opt-out is always available (the Owner is the authority;
the loop assists, it never imprisons) — but taking it is recorded in `notes:` so a later
retro can see that comprehension was self-asserted, not demonstrated. The claim-scope item
is the one aspect for which a second miss surfaces a soft warning in the confirm record
("claim scope not demonstrated") rather than silently passing.

### 4.4 Model-correction → bounded re-freeze

When the Owner's pushback is a genuine model-correction (not just a wrong answer):

1. The orchestrator raises it as a structured item and **STOPs** to confirm the correction
   with the Owner ("You're saying the claim is limited to X, not X-or-Y — shall I correct
   the frozen model?"). The Owner is the arbiter; Claude does not overrule the human, nor
   silently accept (the correction could itself be the Owner mis-remembering — it is
   *confirmed*, then applied).
2. On confirmation, the understand worker is re-forked to **amend only the affected
   artifacts** (`invention-summary.md` / `owner-study-pack.md`), re-run `gate_quotes`, and
   invalidate any prior confirm. The quiz bank item(s) for that aspect are regenerated.
3. The loop resumes. **Re-freeze is bounded** (cap: 3 correction cycles, mirroring the
   review loop's `max_revision` discipline); hitting the cap raises an OWNER_QUESTION
   ("the model and your reading still disagree after 3 passes — re-run understand from
   scratch, proceed with your correction recorded as an open question, or stop?").

This preserves **invariant 4 (understand before design)**: corrections *re-open and
re-freeze* understand; they never leak into design, and design cannot start until a valid
confirm exists for the corrected model.

### 4.5 The explanation-prior artifact — `comprehension-notes.md`

The loop's forward output: `handoff/00-understand/comprehension-notes.md`, a **teaching
brief** design and compose consume. It is *never* a fact source (fences below); it records
only *how to explain*:

```markdown
# comprehension-notes

<!-- Explanation priors from the Owner's comprehension dialogue. NOT a fact source
     (facts live in invention-summary / owner-study-pack). Design & compose read this
     to calibrate emphasis and framing, never to introduce a claim. -->

## Stumble points (aspects that needed a second pass or missed twice)
- claim scope: the reversible/irreversible distinction did not land on first read →
  lead with a concrete before/after, not the statutory phrasing.

## Framing that landed
- the "airbag fires before the crash, not during" one-liner clicked → candidate hook seed
  (design decides; this is a prior, not a directive).

## Owner-declared crux
- the Owner considers the 70 ms head-start the whole story → weight it in the thesis brief.
```

## 5. Downstream consumption

- **`design` (thesis-architect)** reads `comprehension-notes.md` as **priors, not
  directives**: stumble points become "explain-carefully" flags; the Owner-declared crux
  is an input to thesis selection (not an override — design still owns the angle). Add
  `comprehension-notes.md` to `contracts/stages/design.yaml` `may_read`.
- **`compose` (essay-en-composer)** reads it to calibrate where a plain-language gloss is
  mandatory (the stumble points) and which framing to test first. Add to
  `contracts/stages/compose.yaml` `may_read`.
- Neither may treat it as a fact source — enforced by the fence in §6 and by the existing
  `gate_patent_leak` / span-grounding gates (a fact still has to trace to a Quotable span
  regardless of what the notes say).

## 6. Invariants & fences

1. **Facts vs framing is absolute.** `comprehension-notes.md` carries zero claims. Any
   sentence in it that reads as a fact about the invention is a defect. (Lint candidate:
   a gate that flags claim-shaped sentences in the notes file.)
2. **Understand-first is preserved.** Corrections re-freeze understand; design waits for a
   valid confirm of the corrected model (already enforced by `design.yaml entry_requires`
   + RUN-010).
3. **No thesis/angle in the quiz.** Questions are about the *patent's factual triad*, not
   the essay's angle (mirrors the understand stage's existing "no thesis" fence). A quiz
   item that asks the Owner to pick a *thesis* is out of scope.
4. **The Owner is the authority.** The loop can be opted out of at any turn; a model
   correction is *confirmed with the Owner* before it is applied; the loop never blocks the
   Owner from proceeding, only records what was and was not demonstrated.
5. **Checkpoint STOP semantics unchanged.** Each ASK ends the turn. The loop is a sequence
   of protocol-compliant STOP turns, not a single mega-turn.

## 7. Surface (flags / profiles)

- New flag `--comprehension-check on|off`. Default: **on** for `publish` and
  `understand-only`; **off** for `draft` / `wire` (fast paths); forced **off** under
  `--yes` (no Owner present to quiz — falls back to `by: orchestrator-yes-flag`, and the
  confirm `notes:` records "comprehension check skipped: unattended").
- `understand-only` is the profile where this feature earns the most — its entire purpose
  is Owner learning — so it defaults on there too.

## 8. Failure modes designed against

| Failure | Guard |
|---|---|
| Quiz never terminates (Owner keeps missing) | second miss advances (logs a prior), never blocks; opt-out always available |
| Claude teaches its own error as truth | Owner pushback is a first-class correction channel (§4.4), confirmed then applied — not "Owner is wrong" |
| Frozen model becomes permanently mutable | re-freeze capped at 3 cycles, then OWNER_QUESTION |
| Scope creep into design/angle | §6.3 fence: quiz + notes are triad-facts and framing only |
| Notes smuggle unlicensed facts into compose | §6.1 fence + existing span-grounding/`gate_patent_leak` gates catch any fact without a span |
| Undecidable "sufficiently understands" | §4.3 hard predicate (per-aspect correct-within-two OR explicit opt-out) |

## 9. Decidability checklist (vs the loop-audit failure classes)

- **Stop procedure defined?** Yes — reuses STOP/CONFIRM; each question is an ASK→STOP turn.
- **Pass condition mechanical?** Yes — §4.3 keyed grading + per-aspect coverage.
- **Producer assigned for every artifact?** Yes — worker: `comprehension-quiz.md`;
  orchestrator: `comprehension-notes.md` + the graded result in the confirm `notes:`.
- **Mechanical backstop?** The confirm record gains a `comprehension:` field
  (`demonstrated | self-asserted | skipped-unattended`); `check_run` RUN-010 can assert it
  is present and well-formed on publish when `--comprehension-check on`.
- **Bounded?** Yes — re-freeze cap 3.

## 10. Open questions for the Owner

1. **Default aggressiveness.** On `publish`, should the comprehension check default **on**
   (recommended — the point is quality) or stay **opt-in** until it has proven itself on a
   few real runs?
2. **Claim-scope hard gate?** Should a *second* miss on the claim-scope item be a soft
   warning (current design) or a **hard STOP** requiring the Owner to either re-read or
   explicitly accept the risk? (More rigorous, more friction.)
3. **Quiz length.** Minimum one item per aspect (4 total) — enough, or a fixed 5–7 to
   cover figure comprehension and the boundary/"must-not-assert" line too?
4. **Notes authority in design.** Should the Owner-declared crux be a *prior* design may
   overrule (current design) or a *soft override* design must justify departing from?

## 11. Phased implementation (when approved)

- **P1 — capture-only (no grading).** Ask the existing §5 self-check questions interactively,
  capture answers + pushback into `comprehension-notes.md`; no keyed grading, no re-freeze.
  Lowest risk; immediately yields the explanation-prior artifact. Design/compose start
  reading it.
- **P2 — keyed grading + pass predicate.** Add `comprehension-quiz.md` (keyed), the §4.3
  predicate, the `comprehension:` confirm field, and the RUN-010 assertion.
- **P3 — model-correction re-freeze.** Add §4.4 (bounded correction cycles). Highest value,
  highest care — this one mutates the frozen model, so it lands last, behind the other two.

Each phase is independently shippable and independently useful; P1 alone already delivers
the "optimize the downstream instructions" win the idea started from.
