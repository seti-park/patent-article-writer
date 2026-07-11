# Design: Multi-vendor lanes — cheap generation, strict cross-vendor verification

**Status:** PROPOSED (design + minimal spec; not yet implemented)
**Author:** architect session, 2026-07-11
**Depends on:** the hardened loop (STOP/CONFIRM, RUN-005/010b/013/014/015, physical
isolation, double-clean), `contracts/pipeline.yaml`, `.claude/agents/*`, the
`fable-advisor` plugin's CLI-lane mechanism.

---

## 1. Thesis

Assign each vendor to the role it is strongest at, and let the **loop we just hardened**
be the safety net:

- **Grok 4.5 = cheap, fast generator** for the voice-bearing prose (`compose`, `promo`).
- **GPT-5.6-sol high = rigorous verifier** — reads the draft against the source and
  confirms every claim is licensed (`self_audit` grounding + adversarial).
- **Claude (`inherit`) = voice authority + judge + arbiter** — the review loop, thesis
  design, the Owner-facing Korean surface.

The whole point of the loop-hardening refactor was to make "cheap generate + strict
verify" safe: the reviewer, the gates, and double-clean turn a cross-vendor draft's
voice/grounding risk from *unmanaged* into *gated*. A Grok draft is a hypothesis until an
independent Claude review confirms it — exactly the discipline this session applied to
its own implementation (Grok implements, Claude verifies by execution).

## 2. The one non-negotiable rule

**The judge/verifier tier is NEVER the same vendor that generated the artifact.** If Grok
composes, Claude reviews and GPT verifies grounding — never Grok grading its own draft.
This is `physical isolation` (invariant 1) generalized to vendors: an independent judge,
of a different family, is what makes cheap generation trustworthy.

## 3. Practical constraint (read before designing)

Claude Code subagents (`.claude/agents/*.md` `model:` frontmatter) run **Claude models
only** (`inherit`/`opus`/`sonnet`/`fable`/`haiku`). You **cannot** set `model: grok` or
`model: gpt-5.6-sol`. To use a non-Anthropic model you need the **`fable-advisor`
CLI-lane pattern**: a thin Claude wrapper (or an orchestrator step) that shells out to the
`grok` / `codex` CLI, hands it the stage spec + on-disk handoff, and writes the result
back to the handoff file. So "multi-vendor pipeline" concretely means: **give `compose`,
`promo`, and the `self_audit` verifier an optional CLI-lane, with a Claude wrapper and a
graceful fallback.** It reuses the exact machinery `fable-advisor` already provides.

## 4. Allocation

| Stage | Role | Vendor | Notes |
|---|---|---|---|
| `understand` | read + freeze the patent model | `inherit` (Claude) | judgment + Korean surface |
| `design` | thesis/angle | `inherit` (Claude) | voice-adjacent judgment |
| **`compose`** | **generate prose** | **Grok 4.5 (CLI lane)** | fast/cheap; gated by the loop |
| `review_loop` | **voice + quality judge** | **`inherit` (Claude) — FIXED** | the strict supervisor; must not be Grok |
| `self_audit` grounding-verifier | **verify claim ↔ source** | **GPT-5.6-sol high (CLI lane)** | spec-determined cross-check; was pinned `sonnet` |
| `self_audit` adversarial-reader | refute thesis/grounding | `inherit` + optional GPT vote | independent failure distribution |
| `polish` | plain-language surface | `inherit` (Claude) | byte-protected; voice-sensitive |
| **`promo`** | **draft** | **Grok 4.5 (CLI lane)** | same pattern; safe-claims gate is load-bearing |

Rationale for the two cross-vendor placements:
- **compose/promo → Grok**: the artifacts are re-generatable and fully gated (voice-canon
  Pass 1, anti-AI gates, `gate_quotes`, `gate_patent_leak`, double-clean). Cheap + fast,
  and the loop catches drift.
- **grounding-verifier → GPT-5.6-sol high**: "read the essay, read the invention-summary,
  confirm every claim traces to a Quotable span / the claim-scope card" is precisely a
  clear-task verification job, and a different family catches what Claude misses —
  especially the corpus's #1 defect class, **claim-scope misattribution**. Upgrading this
  from `sonnet` to a strong cross-vendor verifier is the highest-value single change.

## 5. Guardrails (all four required)

1. **Isolation of vendor** (§2): the judge/verifier is never the generator's vendor.
2. **Fast voice-drift pre-gate.** Before the full editorial round, a cheap Claude check
   compares a cross-vendor `compose` draft against the `voice-canon` exemplars and the
   anti-AI tells; a voice failure fails *fast and cheap* instead of after a full review
   round. (Pass 1 is a judgment pass, so when the generator is cross-vendor the reviewer
   must be explicitly voice-strict — this pre-gate enforces that.)
3. **Round-cap → `inherit` fallback.** If the Grok draft does not converge to double-clean
   within `N` rounds (default 2), the orchestrator re-composes the failing sections with
   `inherit` (Claude). Cheap generation only wins when convergence is fast; this caps the
   downside (Grok×N + review×N could otherwise exceed one strong pass).
4. **Graceful degradation.** CLI missing / quota hit / running on **web (no local shell)**
   ⇒ the lane silently falls back to `inherit`, and the run report records the
   substitution (never a silent swap — the `fable-advisor` doctrine). The pipeline must
   run identically, if more expensively, with zero CLI lanes available.

## 6. Invariants preserved

- **Physical isolation** (compose ≠ review context) — unchanged; now also vendor-isolated.
- **Composer never reads the raw patent** (invariant 3) — the Grok composer gets only the
  design handoff + Quotable spans, and `gate_patent_leak` (LEAK-001) is vendor-agnostic, so
  a Grok leak is caught the same as a Claude one.
- **Double-clean on publish** — unchanged; a cross-vendor draft still needs two independent
  clean Claude rounds.
- **Owner-facing surface stays Claude** — the Korean briefing/study-pack and the
  understand checkpoint are `inherit`; only the English essay draft and the promo draft are
  cross-vendor, both fully gated.

## 7. Web feasibility

- **CLI lanes (grok/codex) need a local shell** → they do **not** run on claude.ai/code.
  On web the lanes degrade to `inherit` per guardrail 4. (A local-execution bridge, if
  available, restores them — out of scope here.)
- **The `fable-advisor` *advisor agent*** (a Claude subagent, `model: fable`) is
  interface-agnostic and works on web — so the commitment-boundary advisory (below) is
  available everywhere; only the cross-vendor generate/verify lanes are local-only.

## 8. Minimal implementation spec

Phased so each step is independently shippable and the lowest-risk, highest-value one lands
first. All lanes are opt-in flags that default to today's behavior (`inherit`/`sonnet`), so
absent flags = no change.

### P1 — GPT verifier upgrade (lowest risk, additive, highest value)
- New flag `--verifier-vendor gpt|claude` (default `claude`), consumed by the `self_audit`
  stage. When `gpt`: the grounding-verifier work is driven through a `codex` CLI lane
  (`codex exec -m gpt-5.6-sol -c model_reasoning_effort=high -s read-only`), fed the
  essay-final + invention-summary + patent, and asked to return a structured verdict per
  claim (licensed / unlicensed-with-span-gap). A Claude wrapper validates the structured
  output and normalizes it into the existing self-audit findings shape.
- Contract: `contracts/stages/self_audit.yaml` gains `verifier_vendor` + the fallback rule.
- No generation touched. Purely a stronger, cross-vendor verifier. Ship this first.

### P2 — compose vendor lane
- New flag `--compose-vendor grok|inherit` (default `inherit`). When `grok`: the compose
  step drives the `grok` CLI (`grok --prompt-file <spec> -m grok-4.5 --output-format plain
  --cwd <root>`) with the full compose spec (design handoff + Quotable spans + voice-canon
  refs + the five-part contract) and writes `handoff/02-compose/essay-draft.md`.
- Add the **voice-drift pre-gate** (guardrail 2) as a cheap Claude step before review.
- Add the **round-cap → inherit fallback** (guardrail 3) in the orchestrator's review loop.
- `contracts/stages/compose.yaml` gains `compose_vendor` + the two guardrails + fallback.

### P3 — promo vendor lane
- New flag `--promo-vendor grok|inherit` (default `inherit`). Same wrapper pattern; the
  **safe-claims grounding** gate (every factual phrase traces to essay-final/publication/
  owner-briefing) is the load-bearing catch and is already vendor-agnostic.

### Cross-cutting
- One shared CLI-lane helper (reuse `fable-advisor`'s): builds the prompt file, runs the
  CLI, captures output, on non-zero/absent/timeout returns a `substituted` signal so the
  orchestrator falls back to `inherit` and records it in the run report.
- The `patent-essay` SKILL "Model allocation" section documents the vendor lanes + the
  non-negotiable rule (§2) + graceful degradation.
- No new gate is required — the existing gates + double-clean + the P1 verifier ARE the
  safety net. (A voice-drift *detector* could later back guardrail 2 mechanically.)

## 9. Cost model (why this can be a net win)

The premium is spent where judgment lives (review, design, understand, polish stay Claude;
verification gets a strong GPT). The volume — drafting long English prose and the promo —
moves to a cheaper/faster vendor. It only pays off if cross-vendor drafts converge inside
the round cap; guardrail 3 bounds the loss when they don't. Measure convergence rounds on
the first few real runs before trusting the default.

## 10. Open questions for the Owner

1. **compose default**: keep `inherit` as default and make `grok` opt-in until convergence
   is measured (recommended), or default `compose-vendor grok` once P2 lands?
2. **verifier**: GPT-5.6-sol high as a *replacement* for the sonnet grounding-verifier, or
   as an *additional* vote alongside it (more cost, more coverage)?
3. **round cap N** before falling back to inherit compose (default 2)?
