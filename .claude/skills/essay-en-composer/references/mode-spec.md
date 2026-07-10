# Mode specification

Referenced by tech-essay-en SKILL.md Step 0 and Step 4. Defines the two-dimensional mode space, default behavior, mid-pipeline shifts, and per-mode composition rhythm.

**Pipeline rule:** when composing inside the patent-essay pipeline (forked worker),
**strict-execution is the ONLY mode**. `walkthrough` and `pair` are reserved for direct,
non-forked invocation by the Owner. Worker questions inside the pipeline go through the
`OWNER_QUESTION` relay (patent-essay SKILL.md), not in-session elicitation.

## Two dimensions

tech-essay-en operates along two orthogonal dimensions, both selectable at invocation.

### Dimension 1: Mode category

| Mode | Behavior |
|---|---|
| **strict-execution** | Pure prose expansion from Blueprint. No mid-session intervention. Plan ⊥ Execute strict reading. **Only mode when forked inside the pipeline.** |
| **walkthrough** (default for direct/Owner invocation) | Section-by-section composition. Owner mid-session editorial intervention welcome (direct invocation only). Catches at sentence or section level for voice, clarity, thesis alignment, audience perception. **Not used in pipeline forks.** |
| **pair** | Interactive at each sentence. Owner plus Claude step-by-step dialogue. **Not used in pipeline forks.** |

### Dimension 2: Posture (mode spectrum)

| Posture | Behavior |
|---|---|
| **aggressive** | Thesis-altering catches welcome. Framing changes possible. Voice bold experimentation. |
| **measured** (default) | Voice and clarity polish plus minor thesis adjustment. Major framing preserved. |
| **conservative** | Voice and clarity polish only. Thesis plus framing preserved. Factual accuracy emphasized. |

### Default combination

When mode is not specified at invocation: **walkthrough + measured**.

## Step 0 selection logic

- Invocation specifies mode and posture → adopt both
- Invocation specifies only mode → adopt mode and apply default posture (measured)
- Invocation specifies neither → adopt walkthrough plus measured

Confirm mode and posture in the opening response before Step 1.

Example opening:

> "Beginning tech-essay-en in walkthrough mode plus measured posture. Section-by-section composition; please catch any voice, clarity, or thesis concerns mid-session."

## Step 4 composition rhythm per mode

Per-mode composition behavior during Step 4 of the SKILL.md process:

- **walkthrough**: compose section → present → Owner elicit catch → refine if catch → next section. Each section is a checkpoint.
- **strict-execution**: compose all sections → emit full draft → no mid-session checkpoint.
- **pair**: compose sentence → Owner elicit → refine → next sentence. Sentence-level checkpoint.

## Catch scope by posture (walkthrough only)

Mid-session catches in walkthrough mode have posture-bounded scope.

**Measured (default) catches bounded to:**

- Voice and clarity polish (voice canon compliance)
- Sentence-level refinement
- Section transition adjustments
- Minor thesis hint refinement (within blueprint thesis)

**Always out of catch scope** (require blueprint revision, return to essay-architect):

- Fact introduction (new facts beyond `facts_locked`)
- Structural deviation (section reorder, add, remove)
- Major thesis change (blueprint `thesis_statement` modification)

Aggressive posture extends the bounded scope to allow framing variation. Conservative posture narrows the bounded scope to voice and clarity polish only.

## Mid-pipeline mode shift

Owner may explicitly shift mode mid-essay (direct/Owner invocation only). Pipeline forks raise `OWNER_QUESTION` instead. The nature of an emerging catch may also trigger an implicit shift suggestion:

- Thesis-altering catch in measured-posture walkthrough → propose aggressive shift
- Thesis-altering catch in conservative-posture walkthrough → propose either upgrade to measured or aggressive, or return to essay-architect for blueprint revision
- Strict-execution session reveals blueprint coverage incomplete → propose shift to walkthrough or return for blueprint revision

Surface the shift proposal explicitly. Owner decides (direct) or orchestrator relays `OWNER_QUESTION` (pipeline): shift, abandon attempt, or return to design.

**Inside the pipeline (forked):** do not elicit mid-session. End with
`OWNER_QUESTION: <question>` + `FILES: <paths>` so the orchestrator runs the Owner
checkpoint protocol and re-invokes the worker with the answer.
