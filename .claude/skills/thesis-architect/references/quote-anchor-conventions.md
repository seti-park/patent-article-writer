# Quote anchor conventions

Format and discipline for `**Quotable spans:**` blocks in `invention-summary.md` and `Quote anchor table` entries. Carries forward from v1 patent-reader with v2 inline-anchor format.

## `**Quotable spans:**` block format

Used inline within sections of `invention-summary.md` (specifically §"종래 문제 / 과제" and §"유리한 효과 + 정량 데이터"). Phase 2 Compose pulls verbatim text from these without re-touching patent.md.

```markdown
**Quotable spans:**
- `[XXXX]`: "verbatim text exactly as it appears in patent paragraph XXXX"
- `[XXXX]`: "another verbatim quote"
- `[XXXX]`: "..."
```

- 2-5 entries per block.
- Each line starts with the paragraph anchor in backticks: `` `[XXXX]` `` (4-digit, zero-padded).
- Verbatim text in double quotes.
- Korean and English content both allowed; preserve patent's original language.

## Quote anchor table format

Used in `invention-summary.md` §"Quote anchor table" — comprehensive list of every quote-worthy passage. Phase 3 Edit Pass 3 uses this for verbatim verification.

```markdown
| Quote ID | Paragraph | Verbatim text | Significance |
|---|---|---|---|
| q-0016-1 | `[0016]` | "verbatim text" | claim-supporting |
| q-0024-1 | `[0024]` | "..." | quantitative |
```

### Quote ID

Format: `q-<paragraph>-<seq>`

- `<paragraph>` = paragraph identifier without brackets (e.g., `0016`).
- `<seq>` = 1-based sequence number for quotes within the same paragraph.

Examples: `q-0016-1`, `q-0024-1`, `q-0024-2`.

### Significance enum

Mutually exclusive. If a passage genuinely fits two categories, split into two table entries with same paragraph + different seq.

| Significance | Meaning |
|---|---|
| `claim-supporting` | Sentence directly supports what patent claims (paraphrases claim language) |
| `mechanism-critical` | Core technical description any mechanism section needs to cite verbatim |
| `quantitative` | Numeric value or measurement in context (e.g., "approximately 70 ms") |
| `prior-art-contrast` | Passage contrasts invention with cited prior art or industry practice |

## What qualifies as a quote anchor

Four passage types qualify. Most patent sentences do NOT qualify — only the ones below.

1. **Claim-supporting statements** — sentences in the description that paraphrase or restate claim language.
2. **Mechanism descriptions with verbatim phrasing** — the patent's own wording for how the invention works, where rephrasing loses technical precision.
3. **Quantitative data with specific phrasing** — numeric values in context (e.g., "approximately 70 milliseconds", "factor of three").
4. **Comparisons with prior art** — passages explicitly contrasting the invention with cited references or industry practice.

## Verbatim discipline

`verbatim_text` (table) and verbatim quotes (Quotable spans blocks) must match patent exactly. No paraphrasing, no summarization, no normalization.

**Why exactness matters**:
- Phase 3 Edit Pass 3 verifies essay `[xxxx]` quotes against verbatim_text by string match. Any deviation = paraphrase mutation flag.
- Phase 2 Compose treats verbatim_text as the canonical citation source. Mismatch propagates.

If a passage is too long to be useful as one quote, split into multiple anchors with sequential `<seq>` rather than excerpting mid-sentence.

## Allowed normalizations

Markdown conversion of USPTO source text introduces typographic artifacts that don't affect meaning. These normalizations are allowed during verbatim verification (Phase 1 extraction time AND Phase 3 verification time):

- NBSP (`U+00A0`) → space (`U+0020`)
- `**bold**` markdown → plain text (strip the `**` markers)
- Smart quotes (`U+201C`, `U+201D`) → straight quotes (`U+0022`)
- Smart apostrophe (`U+2019`) → straight apostrophe (`U+0027`)

Em dash (`U+2014`) is preserved as-is — patent verbatim 의 일부. Essay 본문 em dash 금지 rule (deliverable voice) 과 다른 영역: deliverable rule 은 essay 본문에만 적용, patent quote 는 verbatim 보존.

Implementation: Phase 3 Edit Pass 3's string-match verification applies these normalizations to BOTH sides of the comparison before matching. Phase 1 Step 1 extraction stores the already-normalized form in `Quotable spans:` blocks (so the verbatim text in `invention-summary.md` is post-normalize).

See `docs/usage-guide.md` § "patent.md preparation conventions" for the user-side patent.md preparation workflow that pairs with this normalize policy.

## Disallowed normalizations

These deviate from verbatim — Phase 3 flags as paraphrase mutation:

- Word substitution (e.g., "vehicle" → "car")
- Sentence restructure (e.g., active ↔ passive voice)
- Punctuation changes beyond the Allowed list (e.g., adding/removing commas, semicolons)
- Capitalization changes (except markdown-bold strip)
- Adding/removing words for "flow"
- Translating between languages (if patent is non-English, preserve as-is; essay can translate inline at cite time, but `invention-summary.md`'s anchor stays in source language)
- Ellipsizing within a single quote ("first part...last part") — split into separate anchors instead

## Phase 2 Compose's contract

Phase 2 cites patent paragraphs with `[XXXX]` inline. The text Phase 2 quotes must be substring-matchable against either:

1. A `**Quotable spans:**` entry's verbatim text, OR
2. A `Quote anchor table` row's verbatim_text field.

If Phase 2 needs to cite a paragraph NOT in either source, Phase 2 returns to Phase 1 for extraction. Phase 2 never re-extracts directly from patent.md (patent.md isn't in Phase 2 Knowledge).

## Edge cases

**Patent has no clear quote-worthy passages**. Emit empty `Quotable spans:` blocks (just the header line) + empty Quote anchor table. Phase 1 Step 3 relies on Layer 4 innovation_angles for thesis seeds.

**Quote contains a typo from the patent**. Preserve verbatim. Do not silently correct. If the typo is material, flag in a `> Note:` block-quote near the table.

**Quote spans paragraph boundary**. Treat as separate quote anchors per paragraph, even if the sentence wraps.

**Equations, tables, formulas**. Equation itself is not a quote anchor. Surrounding prose may be. Numeric values from equations go to §"유리한 효과 + 정량 데이터" Metric table.

**Patent in Korean**. Anchors stay in Korean. Phase 2 (English essay) translates inline when citing, but the source-of-truth in `invention-summary.md` is the verbatim Korean.
