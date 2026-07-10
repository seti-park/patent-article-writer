# Self-Audit — Grounding Verifier (Round 2, confirm-dryness)

Blind to other self-audit readers. Confirm-dryness pass on `draft_version: 5`. Round 1
changed three spans: the §4 VMM anchor ([0002]→[0004]), a new §2 sentence citing [0141]
(block floating point), and a rewritten FIG. 4 caption citing [0138]. This round verifies
the new/changed anchors and spot-re-verifies the rest for regression. Verdicts only
(SUPPORTED / UNSUPPORTED / MISREAD / OVERREACHED-BEYOND-ANCHOR). Stance, tone, and hedging
are out of jurisdiction.

## Mechanical gate outputs

```
$ python .claude/skills/_shared/scripts/gate_quotes.py handoff/03-edit/essay-final.md \
    --invention-summary handoff/01-design/invention-summary.md --patent input/patent.md
[PASS] gate=quotes
  (no findings)

$ python .claude/skills/_shared/scripts/gate_anchors.py handoff/03-edit/essay-final.md \
    --invention-summary handoff/01-design/invention-summary.md
[PASS] gate=anchors
  WARN  FIGREF-000   no figures_index provided, figure-ref check skipped  ((global))
```

Both mechanical gates pass clean, same as round 1.

## Changed-span table (this round's focus)

| # | Location | Text as written | Anchor | Patent span | Verdict |
|---|---|---|---|---|---|
| 1 | §4 body | "A VMM is the document's shorthand for vector-matrix multiplication, the operation that dominates AI training and inference [0004]." | [0004] | "AI... techniques frequently rely on multilayer neural networks... inference and training often involve repeated application of matrix-vector and matrix-matrix multiplications... These workloads commonly process large batches of data in parallel and employ compact numerical formats to increase computational density..." | SUPPORTED — this is exactly the round-1 recommended fix, applied verbatim (round 1 flagged the identical clause as OVERREACHED-BEYOND-ANCHOR when cited to [0002], and explicitly named [0004] as the span that "fully supports" it). No further change needed. |
| 2 | §2 body | "...that arithmetic is block floating point [0141], a shared-scale style older than this filing, so the trick itself is not OpenAI's invention." | [0141] | "A microscale (MX) format is a type of Block Floating Point (BFP) data format specifically designed for AI and machine learning workloads." | SUPPORTED — [0141] states MX IS a type of Block Floating Point verbatim; the sentence asserts no more than that characterization. ("older than this filing" is a general/background clause, not itself [0141]-anchored, and rests on the same MX-2023 dating already fact-logged and cited two paragraphs later in §3 — not a new unlogged fact.) |
| 3 | §2 body | "What the claim seeks to own is the compute-in-memory circuit that executes it inside the array [0011]." | [0011] | "a computing system can include a compute-in-memory (CIM) macro having columns of computing units. The columns of computing units have a column cell... a functional block... an adder tree..." (claim-1 language; no mention of "array") | OVERREACHED-BEYOND-ANCHOR — [0011] fully supports "the compute-in-memory circuit" (the column cell + functional block + adder tree triad) as what the claim seeks to own, but does not itself establish that this circuit executes "inside the array." That locational claim is established elsewhere, at [0133] ("computations... can be directly performed within a memory array to minimize data movement") — which the essay itself correctly cites for this exact idea one section earlier ("The math runs inside the memory array itself [0133]"). Citing [0011] alone for the "inside the array" clause borrows meaning the anchor doesn't carry. **Recommended fix**: co-cite [0133] alongside [0011] (`[0011] [0133]`) — the better-fitting span already exists and is already in active use elsewhere in this essay for the identical claim; no prose change needed. |
| 4 | FIG. 4 caption | "FIG. 4: the align-once core as a functional block diagram [0138]." | [0138] | "FIG. 4 illustrates an exemplary functional block for mantissa alignment 3880 in a computing unit that is configured to perform mantissa alignments and accumulations after primitive products have been produced by the column cells... An example of process flow and data flow for mantissa align-ups and accumulation of primitive products is also depicted in FIG. 4." | SUPPORTED — [0138] itself uses "functional block" and explicitly describes FIG. 4 as depicting "process flow and data flow," which is what "functional block diagram" (a drawing-type descriptor) characterizes. Asserts nothing beyond the span. |
| 5 | FIG. 4 caption | "After multiplication, every product is shifted onto one shared scale, then an adder tree sums the aligned results as plain integers [0011]." | [0011] | claim-1 (b)+(c): functional block aligns mantissa bits by shifting; adder tree outputs accumulation value in integer format by adding the shifted mantissa bits | SUPPORTED — matches the claim triad exactly, and the adder tree is confirmed as part of what FIG. 4 depicts: [0139] ties adder tree 426 to FIG. 4 explicitly ("a synthesizable... adder tree 426 (see FIG. 4)"), and the invention-summary's own reference-number table pairs "426 \| adder tree" with "FIG. 4, FIG. 38." The caption claims nothing beyond what FIG. 4 depicts. |
| 6 | FIG. 4 caption | "This is claim 1's align-then-integer-accumulate step, drawn as data flow." | (unanchored, continuation clause) | [0138]: "An example of process flow and data flow... is also depicted in FIG. 4" | SUPPORTED — restates [0138]'s own "process flow and data flow" language; consistent with round-1's precedent for this same closing clause. |

## Spot-re-verification of unchanged material (regression check)

- **Verbatim blockquote byte-exactness** — re-checked all 9 verbatim quoted spans directly
  against `input/patent.md` (normalized for markdown `**bold**` markers around reference
  numerals only — a source-formatting artifact, not a text discrepancy): "reducing the von
  Neumann bottleneck" [0133], the [0005] conversion-cost blockquote, both [0011] claim-1
  clauses (functional block / adder tree), "without requiring separate conversion pipelines
  or dedicated cores for each format" [0006], the [0147] pipelined-VMM blockquote, "minimize
  compute stalls during updates" [0015], "In some embodiments, 100% utilization of the
  compute engine 100 may be possible." [0154], "serve both compute storage and scan-test
  roles" [0118], and "(canceled)" for claims 11–19. All 9 — byte-exact.
- **Claim independence** — re-confirmed directly against `input/patent.md` lines 505, 516,
  525: claim 1 ("A computing system comprising:"), claim 20 ("A system comprising:"), and
  claim 29 ("A computing system comprising:") are each independent (none reads "according to
  claim X"), each recites the full column-cell / functional-block / adder-tree triad, matching
  the essay's repeated framing. Claims 11–19 read "(canceled)" verbatim at line 515. No
  regression from round 1's finding.
- **Fact-check-log coverage** — no new external (non-patent) facts were introduced this round;
  the three changed spans are patent-internal citations only. All external facts elsewhere in
  the essay (10GW announcement, Jalapeño unveiling, Allegrucci/Rain AI, OCP MX 2023-09) are
  unchanged from round 1 and remain matched to their fact-check-log entries and tiers.

## Tally

- Changed/new spans checked: 6 (rows 1–6 above)
- SUPPORTED: 5
- OVERREACHED-BEYOND-ANCHOR: 1 (row 3)
- MISREAD: 0
- UNSUPPORTED: 0
- Spot-re-verified regressions: 0 (9/9 blockquotes byte-exact, claim independence confirmed,
  fact-check-log coverage intact)
