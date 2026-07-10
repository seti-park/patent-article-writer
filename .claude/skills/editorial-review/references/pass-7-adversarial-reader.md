# Pass 7 — Adversarial reader-pass (fresh-eyes)

Added run 045. The judgment complement of the run-045 self-check gates (`gate_meta` /
`gate_stub` / `gate_cashtag` / `gate_dupe`). Where passes 1-6 review the draft on its own
terms, pass-7 refuses to trust it: it reads as the *audience*, hunting for the editorial
blind-spots a human used to catch only in post-acceptance revision (see
`meta/improvement-proposals/2026-06-26-human-revision-blindspots.md`).

## Why a separate pass

The pipeline declared run 045 `pass`, then a human took it through five more rounds. The misses
were not capability gaps — the model can judge "is paragraph 1 a question?" — they were
*missing criteria*. Pass-7 makes the criteria explicit, evidence-forced, and adversarial, which
is what converts an unreliable holistic judgment into a reliable atomic one.

## Method (reliability comes from HOW, not just WHAT)

1. **Fresh eyes.** Run in a separate context from the composer (extends the voice fence): a
   reviewer with no commitment to the draft's choices.
2. **Persona simulation.** Read as the two readers who bounce hardest:
   - the **impatient investor** — instantiates `_shared/references/reader-profile.md`
     (high-school-to-undergraduate technical comprehension, here for the money thread):
     "where did I want the answer sooner / get bored / hit un-glossed jargon or filler?"
   - the **skeptical pro-subject reader** — "what is the strongest objection to the thesis, and
     is it rebutted?" The steelman must be a THIS-patent objection; a generic patent truism
     ("patents don't guarantee products") counts as `steelman-absent`. The check is **two-sided**:
     a concession that is present and specific but out-weighs its own rebuttal — elaborates the
     counter past conceding it, re-spends a caveat an earlier section already made, or narrates
     spend/procedure inside the beat — counts as `steelman-overweight` (elaborating an objection
     primes it; the reader leaves carrying the counter, not the invention). De-elaborate / return
     to the core, never add a hedge.
3. **Decompose + force evidence.** Every check is a yes/no with a quoted span (or `ABSENT`),
   never a holistic rating.
4. **Multi-vote the fuzzy ones.** For taste-level checks (jargon depth, redundancy feel), N
   independent judges; accept the flag on a majority.

## Checklist (each → {verdict, quoted evidence, severity})

| # | Check | Pass condition | Finding class |
|---|---|---|---|
| 1 | **Hook check (lead energy)** | ¶1 lands the declared energy register's beat (declarative, not a deferred question, no verdict-insurance fact ahead of it) AND the full two-sided call lands by the lead section's end — replaces the run-045 bare BLUF-in-¶1 rule; see `_shared/references/reader-energy.md` | `lead-thesis-deferral` |
| 2 | **Header-as-claim** | every `##` header is an assertion; header-only skim reconstructs the argument | `nonclaim-section-header` |
| 3 | **Steelman present + not overweight** | the single strongest pro-subject counter is conceded compactly and specifically, then the affirmative core carries >= the concession's attention; the beat is net-new (no re-spent prior caveat) and carries no spend/procedure motif | `steelman-absent` / `steelman-overweight` |
| 4 | **No meta posturing** | no reader-instruction / essay-self-reference (functional scope disclaimers exempt) | `meta-reader-instruction` |
| 5 | **Jargon as signpost** | domain term-of-art kept short, not deep-dived past the insight | `jargon-overdepth` |
| 6 | **No stub / rhythm break** | no section markedly shorter than its siblings | `section-stub-imbalance` |
| 7 | **Thesis not over-restated** | the core verdict is asserted in <= 3 sections; the ≤ 3 signature lines declared in `thesis-trace.md` are exempt from the count (protected surface — factual review still applies) | `thesis-restatement-redundancy` |

Checks 2, 4, 6 (and duplication) have mechanical pre-filters (`gate_meta`, `gate_stub`,
`gate_dupe`); pass-7 is the judgment backstop for what the gates' resolution misses — a subtle
single-word echo, a header that is grammatically a claim but says nothing, a question-lead that
slips the blacklist.

## Output

Findings in the standard `feedback-format.md` schema with `pass: pass-7-adversarial-reader`.
They feed `overall_assessment` like any pass. A `/goal` driver can require "pass-7 returns no
unresolved high findings" as part of the acceptance set (see
`_shared/references/scoring-rubric.md`).

## Voice fence

Pass-7 stays inside the Phase-3 fence: `deliverable-voice-rules.md` + `anti-ai-writing.md`
+ `_shared/references/reader-energy.md` (the goal-5 surface contract check 1 rules on),
never `voice-profile.md`.
