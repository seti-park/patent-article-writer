# Revision notes — openai-us20260147536

> **The revision-delta capture channel.** Post-acceptance edits — the delta from the
> accepted final to the revised final — are logged here as one `## delta` block per edit.
> `pipeline-retro` normalizes each block into `meta/findings-ledger.jsonl` via
> `meta/normalize_revision_notes.py`. For this round the deltas came from the **autonomous
> post-acceptance self-audit** (adversarial-reader + grounding-verifier + cold reader, no
> human in the loop), so they normalize with `origin: self-post-accept` (run the normalizer
> with `--origin self-post-accept --source self-audit`).
>
> One block per edit. Keys parsed by the normalizer: `class` (required; a pattern_tag from
> `meta/attribution-table.md`), `round`, `before`, `after`, `rationale`, `goal` — each on ONE
> line. `origin` / `finding_id` lines are documentary (the normalizer keys origin off the CLI
> flag). Unknown classes flag for a new attribution-table row.

<!-- Round: post-acceptance self-audit, applied to the double-clean-accepted final
     (draft_version 4 -> 5). Three multi-voted findings applied; grounding fix priority
     (anchor -> narrow -> label -> cut) observed; NO hedge added; verdict untouched.
     Both signature lines preserved byte-identical. -->

## delta
class: anchor-pointer-offbyone
round: self-audit (v4->v5)
origin: self-post-accept
finding_id: GROUNDING (grounding-verifier, verified)
goal: 1
before: §4 VMM gloss anchored the "operation that dominates AI training and inference" clause to [0002], a generic cross-domain framing span
after: re-anchored the same clause to [0004] (inference and training repeatedly applying matrix-vector / matrix-matrix multiplications); prose byte-unchanged, only the citation moved
rationale: anchor-precision fix under the grounding fix priority (find the stronger anchor); [0004] is the closer-fitting span for the VMM-dominates-AI claim than the generic [0002]; no prose change, no hedge, verdict untouched.

## delta
class: claim-scope-misattribution
round: self-audit (v4->v5)
origin: self-post-accept
finding_id: SKPRO-01 (medium, verified against [0141])
goal: 1
before: §2 sold the align-once / integer-accumulate mechanism as "that is the trick, and it is the part OpenAI wants to own [0011]", attributing the arithmetic idea itself to OpenAI
after: "One alignment, one integer sum, one conversion back: that arithmetic is block floating point [0141], a shared-scale style older than this filing, so the trick itself is not OpenAI's invention. What the claim seeks to own is the compute-in-memory circuit that executes it inside the array [0011]."
rationale: LABEL/NARROW fix (grounding fix priority), NOT a hedge — the align-once move IS block floating point (a known style; [0141] / OCP MX 2023), so what claim [0011] seeks is the CIM circuit that realizes it, not the concept; the edit foreshadows §3's concession instead of contradicting it and sharpens the circuit-level thesis; the verdict is unchanged; the signature line "**Align once, and the whole accumulation becomes integer arithmetic.**" is preserved byte-identical.

## delta
class: caption-drawing-type-overstatement
round: self-audit (v4->v5)
origin: self-post-accept
finding_id: SKPRO-02 (low) + IABI-02 (low, cold-reader corroborated)
goal: 2
before: FIG. 4 header caption opened "the align-once core, drawn as circuitry" and front-loaded un-glossed mantissa/exponent plus Emax 22 / 5-bit / 35-bit numerals — the essay's first text, before §2 glosses any of it
after: "FIG. 4: the align-once core as a functional block diagram [0138]. After multiplication, every product is shifted onto one shared scale, then an adder tree sums the aligned results as plain integers [0011]. This is claim 1's align-then-integer-accumulate step, drawn as data flow."
rationale: two mechanisms in one caption fix — (SKPRO-02, goal 2) per [0138] FIG. 4 is a functional / data-flow block, not a circuit schematic, so "drawn as circuitry" is corrected to "functional block diagram ... drawn as data flow"; (IABI-02, goal 5, cold-reader) the caption is the essay's first text, so the bit-width numerals now defer to §2's numeric walk (Emax 22 / 5-bit / INT35) and the caption leads with the align-once idea; anchors that remain ([0138], [0011]) still support their claim; ~40 words. New class → flag a meta/attribution-table.md row (cousins: figure-caption-scope-deferral, procedure-overweight-lead, jargon-gloss-gap).

## delta — self-audit round 2 (origin: self-post-accept)

- **finding**: grounding-verifier (round 2) — §2 "the compute-in-memory circuit that executes it inside the array [0011]" is OVERREACHED-BEYOND-ANCHOR: [0011] (claim 1) supports "compute-in-memory circuit" but the "inside the array" locational claim belongs to [0133] ("computations ... directly performed within a memory array").
- **fix (anchor-only, grounding-mandated)**: co-cite → "... inside the array [0011] [0133]." No prose change. [0133] is already in active use one section earlier for the same idea.
- **applied to**: handoff/03-edit/essay-final.md + handoff/02-compose/essay-draft.md (in sync).
- **multi-vote note**: round-2 impatient-investor DRY (0 medium+), skeptical-pro DRY (0 medium+, SKPRO-01 fix confirmed correct), grounding-verifier surfaced this one anchor co-cite. Cold-reader round-2 stop-point (the §2 FP8×FP6→22→5-bit→35-bit numeric cluster) was NOT corroborated by any rubric reader as a finding (impatient-investor rated the same cluster PASS) — logged as considered-not-applied here and routed to Phase 3.7 prose-polish for plain-language smoothing (anchor convention [dddd] is house style, retained). Low residuals (INV-R2-L1/L2/L3, SKPRO C1/C2) all recommend no change.

self-audit: no unresolved findings
