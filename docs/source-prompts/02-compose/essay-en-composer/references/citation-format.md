# Inline citation format

Conventions for inline citations enabling Phase 3 Edit Pass 3 verification. v2 differs from v1 — `[xxxx]` paragraph anchors replace `[^fact-base-entry-id]` footnotes for patent quotes.

## Two citation systems

v2 uses two distinct citation forms, by source type:

### Patent paragraph anchors → `[xxxx]` inline

```markdown
Tesla's claim of pre-impact deployment derives from the vision sensor's predictive role in the airbag controller's decision path [0016].
```

- Format: `[XXXX]` (4-digit zero-padded paragraph identifier in square brackets).
- Source-of-truth: `handoff/01-design/invention-summary.md` — specifically the `**Quotable spans:**` blocks and the `Quote anchor table`.
- Phase 2 never re-extracts from patent.md (patent.md isn't in Phase 2 Knowledge).
- Quoted text must match the verbatim text in the invention-summary source — Phase 3 Edit Pass 3 verifies this by string match.

### External (non-patent) sources → entries in `# Sources` block

External attributions go in the essay's `# Sources` block at the end, NOT as inline footnotes. The 5-category enum (Patents / Papers / Official statements / News & media / Technical specs) applies.

```markdown
Industry-standard airbag ECUs typically respond within approximately ten milliseconds. (See: Bosch ECU spec sheet, technical specs.)
```

OR

```markdown
Industry-standard airbag ECUs typically respond within approximately ten milliseconds.
[...]
# Sources
## Technical specs
- Bosch airbag ECU spec sheet — <URL>
```

External claims also appear in `handoff/01-design/fact-check-log.md` with `Fact ID` for traceability. Phase 3 Edit Pass 3 cross-checks the log against the essay.

## What does NOT need citation

- Lead/transition prose with no factual claim: "This week's announcement raises a question..."
- Interpretive framing: "The architectural implication is significant..."
- Connective tissue: "Three days later, however..."
- Rhetorical questions or framing devices

But: even non-cited prose must not introduce facts. If "three days later" is a fact, the date must be derivable from cited facts.

## Examples

### Verbatim patent quote

```markdown
The patent describes the controller's decision: "deployment decision is made approximately 70 milliseconds before traditional accelerometer-based systems would respond" [0024].
```

The quoted text must match `invention-summary.md` Quote anchor table row `q-0024-1` verbatim_text exactly.

### Paraphrased patent claim

```markdown
The vision sensor functions as a predictive input to the airbag controller, not as a redundant sensor [0017].
```

Paraphrasing is allowed for non-verbatim citations. The paragraph anchor `[0017]` ties the claim to the source.

### Quantitative claim with external context

```markdown
Tesla's 70-millisecond claim [0024] sits against an industry baseline of approximately 10 milliseconds for accelerometer-based ECUs (Bosch technical specs).
```

Patent claim cites `[0024]`. External baseline cites the Bosch entry in `# Sources`.

### Reference number context

```markdown
The Vehicle Control Unit (414) receives the vision sensor's pre-impact signal [0016] and triggers deployment within the 70ms window [0024].
```

Reference numbers `(414)` come from `invention-summary.md` Reference number table. Paragraph anchors `[XXXX]` from Quotable spans. The two operate independently.

## Citation placement

Prefer end-of-clause or end-of-sentence placement:

✓ "Tesla announced 70ms improvement [0024]."
✓ "The architectural decision [0016], detailed in patent figures, predates the announcement."

Avoid:
✗ "Tesla [0024] announced 70ms improvement." (interrupts flow)

## Multiple citations

If a sentence draws on multiple paragraphs:

```markdown
The mechanism — vision input [0016] feeding the controller [0017] within the 70ms window [0024] — is claim-anchored.
```

Cite each contributing paragraph.

## How Phase 3 Edit uses citations

Pass 3 (Claim adequacy + fact verification + paraphrase mutation):

- Extract all `[XXXX]` markers from draft.
- For each marker, find the surrounding quoted text.
- Match quoted text to `invention-summary.md` Quote anchor table or Quotable spans block.
- Verify quoted text equals source verbatim_text (verbatim citations).
- Flag mismatches as paraphrase mutation (intentional / accidental drift / substantive change classification).

Pass 6 (Lead/Conclusion + format compliance):

- Verify every `[XXXX]` is 4-digit zero-padded inside square brackets.
- Verify `# Sources` block has at most 5 categories from the enum.
- Verify external attributions in the essay all appear in either `# Sources` or the source-of-truth `fact-check-log.md`.
