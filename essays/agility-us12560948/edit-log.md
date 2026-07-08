# Edit log — US 12,560,948 B2 investor moat article (formal pipeline)

Phase 3 editorial-review for the Compose↔Edit inner loop. Posture: measured, plus the
investor firm-closing SETI guard (essay-context.md). Threshold: pass. One iteration: clean PASS.
Findings follow `editorial-review/references/feedback-format.md`.

## Review 1 (iteration 1, on handoff/02-compose/essay-draft.md)

```yaml
review_id: agility-us12560948-moat-editorial-review-1
draft_source: handoff/02-compose/essay-draft.md
review_timestamp: 2026-06-24T03:00:00Z
posture_applied: measured
overall_assessment: pass

findings:
  - pass: pass-1-voice-anti-ai
    finding: "no findings"
    scoped_to: "Banned word/pattern grep clean (gate_banned 0); no copula avoidance, transition fingerprint, elegant variation; lead uses corporate-narrative-friction opening per spine Q7."
  - pass: pass-2-redundancy
    location: lead + §"Why It Matters Now"
    severity: low
    severity_under_default_posture: low
    finding: |
      "$2.5 billion" appears in the lead (hook) and again in §"Why It Matters Now" (detailed
      context). This is the accepted lead -> recap pattern (different framing each time, not a
      third restatement), so it does not rise to redundancy.
    recommendation: |
      Leave as-is. The lead states it as the stakes; §6 states it as sourced detail.
  - pass: pass-3-fact-paraphrase
    location: §Sources, Papers
    severity: low
    severity_under_default_posture: low
    finding: |
      The three academic papers are cited as listed in the patent's Other Publications (title +
      year, no venue). Verified at Tier 2 (cited in the granted patent); venue not load-bearing.
    recommendation: "Optional; leave as provenance from the patent's reference list."
  - pass: pass-3-fact-paraphrase
    finding: "no findings (verbatim / claim-scope)"
    scoped_to: "All 14 [00NN] anchors checked verbatim vs invention-summary Quotable spans; claim-1 block quote matches the granted claim; no dependent/description embodiment attributed to claim 1 (Locked column honored); pinned values not described as bounds; external facts fenced + sourced (f-spac/f-gxo/f-totes/f-customers), 100k-tote count attributed to Agility (Tier 4)."
  - pass: pass-4-logic-causality
    finding: "no findings"
    scoped_to: "Design-around argument mechanism-backed ([0010],[0013],[0033]); strategy inference scoped ('evidence of focus', not a market lock); no correlation/causation or reverse-causation drift; patent and deployments kept separate; thesis arc closes the lead's narrative-friction tension."
  - pass: pass-5-reader-perspective
    finding: "no findings"
    scoped_to: "Hook lands by sentence 4-5; no density wall (claim-scope section broken by Locked/Open/Pinned labels); every paragraph 2-7 sentences and under the mobile line ceiling; reader profile = tech-industry analyst."
  - pass: pass-6-lead-conclusion-format
    finding: "no findings"
    scoped_to: "Lead anchors thesis + patent on table by sentence 5; closing returns to the walk-vs-safe-stop frame; # Sources 5-label enum, all-or-nothing subgroups; 'Last, First, et al.' author form; em-dash 0; [dddd] 4-digit; title has no em-dash."
  - pass: seti-firm-closing-guard
    location: §"The Investor Read"
    severity: low
    severity_under_default_posture: low
    finding: |
      Firm-closing guard satisfied (this is the lesson baked in upstream, verified here, not a
      defect). Verdict opens "The verdict is yes"; limits are referenced as bounding scope ("the
      ones set out above ... scope the moat rather than cancel it"), not re-listed and not given
      equal weight; exactly one anti-hype guard ("nobody should price it as one"). No over-hedge.
    recommendation: "None. Guard holds; do not loosen."
```

## Round result

- Deterministic gates: PASS (0 fail, 0 warn).
- Editorial overall_assessment: pass.
- Grounding hard-gate: clear (no pass-3 high/critical; gate_anchors PASS).
- Goal-2 hard-gate: clear (no FIGUSE-001; figures 1/3/6 used; core-mechanism coverage present).
- **ROUND 1 = PASS.** Loop terminates at iteration 1 (cap 4). Promote essay-draft.md →
  handoff/03-edit/essay-final.md.

## Why one iteration (vs the prior ad-hoc run's three)

The prior ad-hoc run needed three review rounds (8-sentence paragraphs, then a regression, then an
over-hedge SETI catch). This formal run cleared in one because the defects were prevented
upstream: Phase 1's thesis-spine pinned a firm-closing posture and a claim-scope map; Phase 2
drafted to paragraph-length discipline and the firm verdict from the start. The loop had nothing
to fix.
