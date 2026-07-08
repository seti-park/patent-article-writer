# Pass 3 — Claim adequacy + fact verification + paraphrase mutation

Combines v1 Pass 3 (claim adequacy + external fact verification) with v1 Pass 4 (paraphrase mutation judgment). All claims verified, all citations cross-checked.

## Three sub-passes

### 3A — Patent claim verification (verbatim)

For every `[XXXX]` inline citation in the draft:

1. Locate the paragraph anchor in `invention-summary.md` Quotable spans block OR Quote anchor table.
2. If the essay quotes verbatim (text in double quotes), compare to the source verbatim_text byte-by-byte.
3. If the essay paraphrases (no quotes), verify the paraphrase preserves the source's meaning without drift.

Failure cases:
- `[XXXX]` cites a paragraph not in `invention-summary.md` — flag as "anchor missing". Phase 2 must return to Phase 1 for extraction.
- Quoted text differs from source verbatim_text — flag as paraphrase mutation (see 3C).
- Paraphrase introduces a claim not in source — flag as fact introduction (high severity, may break Plan ⊥ Execute).

### 3B — External fact verification

For every external (non-patent) claim in the draft:

1. Locate the claim in `handoff/01-design/fact-check-log.md` by Fact ID or context.
2. Verify the `Source URL` is reachable and the claim is supported.
3. Verify the essay's `# Sources` block lists the source.

Source authority hierarchy (from `references/external-fact-verification.md`):

| Tier | Source type | Example |
|---|---|---|
| 1 | 1차 source | patent filing, official transcript, primary company statement |
| 2 | Authoritative secondary | major newspaper of record (NYT, FT, Reuters) directly quoting tier-1 |
| 3 | Trade publication | InsideEVs, Electrek, The Information |
| 4 | Aggregated coverage | derivative reporting without primary access |
| 5 | Social/forum | unverified posts, forum claims |

Tier 4-5 sources require tier 1-3 backing or the claim is dropped.

### 3C — Paraphrase mutation classification

When sub-pass 3A flags a verbatim mismatch, classify the mutation:

| Classification | Description | Severity |
|---|---|---|
| **intentional restatement** | Composer's deliberate paraphrase, preserves meaning, adds clarity for English readers | low — accept |
| **accidental drift** | Word substitution that shifts meaning slightly ("supplements" → "complements", "approximately" → exactly) | high — re-anchor to source |
| **substantive change** | Paraphrase materially alters the claim (changes scope, polarity, certainty) | critical — re-anchor or drop claim |

### 3D — Causal claim quality (cross-pass with Pass 5)

For every causal claim ("X causes Y", "X drives Y", "X explains Y"), verify the source supports causation, not just correlation. See `references/causal-reasoning.md` for the 인과/상관/우연 distinction framework.

If the source only supports correlation, the essay must either:
- Reframe as "X correlates with Y", or
- Provide an additional causal chain (mechanism explanation tying X → Y).

## Severity calibration per posture

| Sub-check | aggressive | measured | conservative |
|---|---|---|---|
| 3A verbatim mismatch (intentional) | low | low | medium |
| 3A verbatim mismatch (drift) | high | high | high |
| 3A fact introduction beyond Quotable spans | high | high | critical |
| 3B tier-5 source without backing | high | high | critical |
| 3B missing # Sources entry | medium | medium | high |
| 3C accidental drift | high | high | high |
| 3C substantive change | critical | critical | critical |
| 3D correlation→causation drift | high | high | critical |

## Output finding template

```yaml
- pass: pass-3-fact-paraphrase
  location: §3, sentence 4
  severity: high
  severity_under_default_posture: high
  finding: |
    Essay quotes "deployment decision is made approximately 70 milliseconds before".
    invention-summary.md Quote anchor q-0024-1 has "deployment decision is made
    approximately 70 milliseconds before traditional accelerometer-based systems
    would respond". The trailing context was clipped, changing the comparison frame.
  recommendation: |
    Restore "before traditional accelerometer-based systems would respond"
    OR rephrase as paraphrase: "The patent claims a 70ms lead over accelerometer
    baselines [0024]."
```

## Cross-skill anchors

- `invention-summary.md` Quotable spans and Quote anchor table — patent verbatim source-of-truth.
- `fact-check-log.md` — external fact source-of-truth.
- `patent.md` re-uploaded to Phase 3 Knowledge — fallback verification when invention-summary entry seems wrong.

## Pass 3's place in the pipeline

v1 had Pass 3 (claim adequacy) and Pass 4 (paraphrase mutation) separately. v2 merges because both share the same source materials and the workflow is sequential: fact-check first, then paraphrase classification on any verbatim mismatches surfaced. Merging eliminates context-switch.
