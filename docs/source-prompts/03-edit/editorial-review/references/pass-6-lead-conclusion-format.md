# Pass 6 — Lead/Conclusion + format compliance

Combines v1 Pass 6 (lead/conclusion strength + sources organization) with the v1 deterministic-gate mechanical checks (em-dash count, `[xxxx]` format, banned-words grep, `# Sources` 5-category enum). Brief lock: deterministic-gate is absorbed into Pass 6.

## 6A — Lead anchor to thesis

Lead's first 3 sentences must anchor the thesis. Test: extract the lead, ask "what's the essay about?" If the answer requires §2+, lead is failing.

Specific requirements (per `references/posture-lens.md`):
- First sentence sets up a tension (news event, reader experience, industry norm reversal, corporate event, or visual anomaly — one of the 5 opening voice canon categories).
- By sentence 3, the patent or evidence is on the table.
- Thesis spine appears (explicit or implicit) by lead's end.

Failures:
- Lead is throat-clearing for 4+ sentences.
- Lead introduces 2 unrelated tensions.
- Patent never appears in the lead (essay reads like industry op-ed).

## 6B — Frame closure (lead ↔ closing)

The closing must return to the lead's frame. If lead opens with a corporate-narrative-friction (e.g., "Tesla 's 70ms announcement…"), closing should land that frame.

Closing posture must match `handoff/01-design/thesis-spine.md` adversarial defense residual_risk:

| Residual risk | Closing voice canon category |
|---|---|
| `none` | `closing-aphoristic-landing` or `closing-forward-watching-event` |
| `Acknowledged` | `closing-open-question` or `closing-aphoristic-landing` |
| `Acceptance` (binary falsifier) | `closing-binary-test` |

Mismatch is high severity.

## 6C — `# Sources` 5-category enum check

The `# Sources` block must conform to:

- **At most 5 categories**, all from this enum: `Patents`, `Papers`, `Official statements`, `News & media`, `Technical specs`.
- **Subgrouping is all-or-nothing** — if any category appears as a subheading, every source must be categorized.
- **Flat list rule** — 0-3 entries, or all-one-category: flat. 4+ entries across 2+ categories: subgrouped.

Failures:

| Failure | Description | Severity |
|---|---|---|
| Category outside enum | "Industry data" (not in enum) | high |
| 6+ categories | enum violated | high |
| Partial subgrouping | Some entries categorized, others bare | high |
| Subgrouping with 3 entries | Should be flat | medium |

## 6D — "First, et al." author format

Multi-author papers in `# Sources / Papers`:

- 1 author → "Last, First (YYYY). Title. Venue."
- 2 authors → "Last1, First1 & Last2, First2 (YYYY). …"
- 3+ authors → "Last1, First1, et al. (YYYY). …"

The "First, et al." form (first author's first name + et al.) is wrong. Use "Last1, First1, et al."

## 6E — Mechanical compliance grep

Direct text matching. Each is binary — pass or high-severity fail.

| Check | Pattern | Failure |
|---|---|---|
| Em dash count | `—` regex (excluding inside quoted patent text) | ≥1 = fail |
| `[xxxx]` format | `\[\d{4}\]` regex on inline cites | Any non-4-digit `[XXX]` or `[XXXXX]` = fail |
| Banned word grep | `\b(delve\|tapestry\|vibrant\|...)\b` case-insensitive | Each hit = high (already covered in Pass 1 but re-checked here for safety) |
| Footnote stripped | `[^...]:` defs in publication.md | Any present = strip pipeline broke |
| Sources block | `# Sources` exactly once | 0 or 2+ = fail |

## 6F — Title em-dash check

Title rule (per `legacy/v1/phase-a-spec.md`'s em-dash decision): title may NOT use em-dash. Pattern "X: subtitle" (colon) or "X — subtitle" (em-dash forbidden).

| Title pattern | OK? |
|---|---|
| "Tesla's 70ms Vindication: A Patent Reading" | ✓ colon |
| "Tesla's 70ms Vindication — A Patent Reading" | ✗ em-dash |
| "Tesla's 70ms Vindication" | ✓ no separator |

## Severity calibration per posture

| Sub-check | aggressive | measured | conservative |
|---|---|---|---|
| 6A lead anchor weakness | medium | high | high |
| 6B closing voice mismatch | high | high | high |
| 6C category outside enum | high | high | high |
| 6D author format wrong | medium | medium | high |
| 6E em-dash present | high | high | high |
| 6E other mechanical fails | high | high | high |
| 6F title em-dash | high | high | high |

## Output finding template

```yaml
- pass: pass-6-lead-conclusion-format
  location: # Sources block
  severity: high
  severity_under_default_posture: high
  finding: |
    Sources block has 6 categories: Patents (3), Papers (2), Official statements
    (1), News & media (1), Technical specs (1), Industry data (1).
    "Industry data" is not in the 5-category enum.
  recommendation: |
    Reassign the "Industry data" source. Most likely fits "Technical specs"
    (if the source is a spec sheet, datasheet, or industry standard document)
    or "News & media" (if it's a derivative report).
```

## Pass 6's place in the pipeline

v1 had Pass 6 (lead/conclusion + sources) and a separate deterministic-gate skill for mechanical checks (em-dash, format, banned-words). v2 brief locked deterministic-gate's absorption into Pass 6. The merge keeps mechanical checks in the editorial flow where SETI's revise decision is centralized.
