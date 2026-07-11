# Pass 6 — Lead/Conclusion + format compliance

Combines v1 Pass 6 (lead/conclusion strength + sources organization) with the v1 deterministic-gate mechanical checks (em-dash count, `[xxxx]` format, banned-words grep, `# Sources` 5-category enum). Brief lock: deterministic-gate is absorbed into Pass 6.

## 6A — Lead anchor to thesis

Lead's first 3 sentences must anchor the thesis. Test: extract the lead, ask "what's the essay about?" If the answer requires §2+, lead is failing.

Specific requirements (per `references/posture-lens.md`):
- First sentence sets up a tension (news event, reader experience, industry norm reversal, corporate event, or visual anomaly — one of the 5 opening voice canon categories).
- By sentence 3, the patent or evidence is on the table.
- Thesis spine appears (explicit or implicit) by lead's end — the full two-sided call lands by the lead section's end (order inside the lead is 6H's jurisdiction: hook beat first, insurance after).

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

**Firm-closing override (verdict editions).** When `thesis-spine.md` declares
`closing_posture: firm` (the default for investor / analysis / assessment editions — see
`posture-lens.md`), an `Acknowledged` residual risk maps toward `closing-forward-watching-event`
or `closing-binary-test`, NOT `closing-open-question`. An open-question or over-hedged close under
a declared firm posture is a 6G finding (below), high severity. Rationale: for an essay whose job
is to land a call, the Acknowledged→open-question default was the structural source of
safe-harbor conclusions ("a patent does not guarantee production") that no pass could see.

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

## 6G — Verdict confidence proportionate to evidence (over-hedge guard)

<!-- Detection names the pattern; the fix handed downstream is a positive precision target
     (docs/architecture/comprehension-loop.md §5.1 + invariant 6). -->

For essays that land a verdict or recommendation (investor / analysis / assessment editions),
check that the conclusion's confidence matches the evidence the body established. This is the
mirror of Pass 3 / Pass 4, which guard OVERREACH; 6G guards OVER-HEDGE.

**Detection** (reviewer names the pattern — detector-side; not composer-facing):

Flag (over-hedge):
- the verdict leads with the qualifier instead of the call ("a qualified yes" before the "yes");
- false equivalence between the thesis and its limits ("the limits are equally real");
- caveats re-listed in the verdict that a dedicated limits section already covered (state once,
  then reference);
- generic safe-harbor boilerplate in the verdict ("a patent does not guarantee production / a
  rising stock price", "only time will tell", "remains to be seen") — a category-level truism is
  never this essay's conclusion;
- stacked hedges a body with firm evidence does not warrant.

**Hedge budget** (detection criterion): the verdict section keeps exactly ONE anti-hype guard,
and it must be specific to this patent (e.g. "nobody should price it as a market lock"), not a
truism about patents in general. Everything else that bounds the thesis lives in the dedicated
limits section, referenced — not re-listed — from the verdict.

**Remediation** (composer-facing `recommendation` — positive precision target):
- state each bound once at its precise claim anchor; lead the close with its affirmative
  commitment;
- keep the one patent-specific anti-hype guard; commit the verdict to what the evidence and
  claim scope support, at the anchor;
- when 6G and Pass 3 appear to conflict on the same sentence, fix priority is: find a stronger
  anchor → narrow the claim to what the anchor supports → reframe as explicitly-labeled
  analysis → commit the call at that bound (Pass 3 still binds; never assert beyond claim
  scope).

Mechanical pre-filter: `gate_hedge` (HEDGE-001 boilerplate, HEDGE-002 qualifier-led verdict,
HEDGE-003 hedge density) — hard-fails when the draft frontmatter declares `closing_posture: firm`.
6G is the judgment backstop for what the regexes miss (false equivalence, caveat re-listing,
evidence-confidence mismatch).

Severity: medium under measured posture; high when `thesis-spine.md` declares a firm-closing
posture and the draft violates it.

## 6H — Defensive-open guard (insurance before discovery)

<!-- Detection names the pattern; the fix handed downstream is a positive precision target
     (docs/architecture/comprehension-loop.md §5.1 + invariant 6). -->

6G's mirror at the TOP of the essay. Check that no verdict-insurance fact — status labels
("pending application", "not yet granted"), liens / collateral, examiner rejections, "still
not an asset" framings — precedes the lead's discovery beat (the energy register's payoff
declared in Phase 1's chosen title-lead pair; doctrine in
`_shared/references/reader-energy.md`).

**Detection** (reviewer names the pattern — detector-side; not composer-facing):

Flag (defensive-open):
- one or more insurance facts stacked ahead of the discovery beat in ¶1;
- a lead ¶1 that opens on a qualifier or disclaimer instead of the register's beat;
- gap-framed headers or a cover caption that bury the discovery under inventory;
- the first two lines (what an X card shows) spent on throat-clearing or insurance.

The insurance facts themselves are NOT findings — the two-sided call, which must still land
by the lead section's END, requires them. The finding is their POSITION ahead of the beat.

**Remediation** (composer-facing `recommendation` — positive precision target): lead with the
discovery beat; keep insurance facts priced second (order, not content). Both 6H and 6G hold
simultaneously.

Mechanical pre-filter: `gate_surface` SURF-002 (qualifier-led first body sentence) and
SURF-004 (defensive-open lexicon before any discovery beat) — both warn. 6H is the judgment
backstop for what the lexicons miss.

Severity: symmetric with 6G — medium under measured posture; high when the draft declares
`closing_posture: firm` (a verdict edition that opens defensively contradicts its own
posture).

## 6I — Attention-budget guard (insurance volume and placement)

6H's volume counterpart. 6H constrains the ORDER of insurance at the top of ¶1; 6I
constrains how MUCH procedure/insurance material the essay carries and WHERE it lives
(doctrine: `_shared/references/reader-energy.md` §6, class `procedure-overweight-lead`).
The named escape route 6I closes: a lead that opens on the discovery beat (6H satisfied)
and then piles process narration — examiner fights, fees, RCE mechanics, spend riffs,
lien walks — into ¶2–3 and again mid-essay and in the closing, so the technology the
reader came for gets crowded into a skimmed middle.

Check, against the spine's declared section `payload` tags (spine → section trace):

- **Lead payload order**: after the hook, the lead answers *what the invention does /
  changes* before *what it costs / where it stands*. Status LABELS are call material and
  fine; process NARRATION in the lead (beyond one clause) is a finding.
- **Single home**: prosecution/finance narration appears in the one section the spine tags
  `payload: pricing` (plus at most one lead clause and the closing recap). The same
  money/process beat surfacing in three or more sections is a finding.
- **Motif budget**: when the edition brief budgets a topic ("exactly ONE label sentence"),
  count paraphrase echoes of the motif (keeps-paying / expensive-to-keep-alive /
  fee-paid-to-argue variants) against that budget across the WHOLE essay. Declared
  signature lines are exempt, per reader-energy §5.

The insurance facts themselves are NOT findings — both-or-neither evidence selection and
the two-sided call stand (6G/6H logic applies unchanged). The finding is VOLUME or
PLACEMENT.

**Remediation** (composer-facing — positive): relocate and compress insurance/process
material into its spine-tagged home; keep the facts, free the tech beat. 6I and 6G both
hold (the call stays firm and two-sided).

Mechanical pre-filter: `gate_surface` SURF-005 (procedure-narration sentence count in the
lead section) and SURF-006 (essay-wide spend-motif count) — both warn. 6I is the judgment
backstop for what the lexicons miss (a procedural plot built from clean vocabulary, a
motif echoed in fresh words).

Severity: symmetric with 6G/6H — medium under measured posture; high when the draft
declares `closing_posture: firm` and the lead's procedure share crowds the tech beat.

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
| 6G over-hedged verdict | medium | medium (high under declared firm-closing) | medium (high under declared firm-closing) |
| 6H defensive-open lead | medium | medium (high under declared firm-closing) | medium (high under declared firm-closing) |
| 6I attention-budget breach | medium | medium (high under declared firm-closing when the lead is crowded) | medium (high under declared firm-closing when the lead is crowded) |

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

v1 had Pass 6 (lead/conclusion + sources) and a separate deterministic-gate skill for mechanical checks (em-dash, format, banned-words). v2 brief locked deterministic-gate's absorption into Pass 6. The merge keeps mechanical checks in the editorial flow where the orchestrator's revise decision is centralized.
