# Patent-essay validation gates

Deterministic, mechanical checks that a finished English essay draft must pass.
Pure Python 3 standard library — **no pip installs**. Every gate is runnable
standalone and importable; `run_gates.py` aggregates all fourteen. Two pipeline
utilities live here too: `strip_publication.py` (draft → publication.md, incl.
paragraph rejoin) and `check_run.py` (loop run-completeness checker).

These gates are the **mechanical (hard pass/fail) layer** of the quality loop. They are
aligned to the real editorial rules: em-dash / banned-list (anti-ai Pass 1), `[xxxx]` 4-digit
format + anchor chain (Pass 3 / Pass 6), the `# Sources` 5-label enum (Pass 6 6C), and the
goal-2 figure-use check. The qualitative layer is `editorial-review`'s 7-pass severity model.
See `_shared/references/scoring-rubric.md` for how the two combine into PASS/FAIL.

## Files

| File                 | Purpose |
|----------------------|---------|
| `gate_emdash.py`     | Em-dash / en-dash usage gate |
| `gate_anchors.py`    | `[dddd]` format + anchor-chain + figure-reference gate |
| `gate_sources.py`    | `# Sources` block structure gate (5-label enum) |
| `gate_banned.py`     | Banned-terms / AI-tell phrase gate |
| `gate_structure.py`  | Structural heuristics (all warn-only) |
| `gate_figure_use.py` | Figure-use gate — orphan selected figure (north-star goal 2) |
| `gate_meta.py`       | Reader-instruction / essay-self-reference posturing (META-001 fail) |
| `gate_stub.py`       | Section-balance — a section that is a stub vs its siblings (warn) |
| `gate_cashtag.py`    | Venue ticker convention — bare ticker should be a `$`-cashtag (warn) |
| `gate_dupe.py`       | Gross verbatim phrase repetition in body prose (warn) |
| `gate_quotes.py`     | Invention-summary quotes verbatim-present in patent.md (goal-1 chain) |
| `gate_hedge.py`      | Verdict-section over-hedge: boilerplate / qualifier-led / hedge density |
| `banned_terms.txt`   | Mechanical mirror of the anti-ai banned subset (see its header) |
| `run_gates.py`       | Aggregator + CLI |
| `strip_publication.py` | draft.md → publication.md (frontmatter/footnotes strip + paragraph rejoin) |
| `check_run.py`       | Loop run-completeness checker (round artifacts, dispositions, acceptance) |
| `test_gates.py`      | `unittest` suite (inline fixtures) |

## Format assumptions

- **Draft** is Markdown.
- **Quoted text** = anything inside double quotes `"..."` OR a Markdown blockquote line
  starting with `>`. Em-dashes and banned terms inside quoted text are allowed (verbatim
  source quotes). Fenced code blocks are also exempt.
- **Citation anchors** = inline tokens `[dddd]`, 4-digit zero-padded, e.g. `[0123]`.
- **Figure refs** = `Figure N` / `Fig. N` / `Fig N` / `fig-NN` (case-insensitive), N int.
- **Sources block** = exactly one `# Sources` (h1) header; categories, when subgrouped, are
  `##` (h2) sub-headings drawn from the 5-label enum
  (`Patents`, `Papers`, `Official statements`, `News & media`, `Technical specs`);
  subgrouping is all-or-nothing.
- **Figure selection** = `handoff/01-design/figure-selection.md`; every figure number named
  there must be referenced in the draft (orphan = fail).

## Shared gate contract

```python
def check(draft_text: str, context: dict) -> dict
# -> {"gate": str, "passed": bool,
#     "findings": [{"check_id": str,
#                   "severity": "fail"|"warn",
#                   "message": str,
#                   "location": str}, ...]}
```

`context` keys consumed: `invention_summary_text` (str), `figures_index` (list[int]),
`figure_selection_text` (str), plus optional `banned_terms_file` / `banned_patterns` for the
banned gate, and a reserved `mode` pass-through.

## Usage

```bash
python run_gates.py --draft DRAFT.md \
    [--invention-summary SUMMARY.md] \
    [--figures FIGS.txt] \
    [--figure-selection figure-selection.md] \
    [--patent patent.md] \
    [--mode essay|wire] [--json]
```

- `--figures` file: one integer per line, or comma/space separated.
- Exit code: `0` if no gate emits a `fail` finding, else `1`. **Warnings never fail the run.**
- `--json` emits `{"passed": bool, "gates": [...per-gate dicts...]}`.

Standalone:

```bash
python gate_emdash.py     DRAFT.md
python gate_anchors.py    DRAFT.md [--invention-summary S.md] [--figures F.txt]
python gate_sources.py    DRAFT.md
python gate_banned.py     DRAFT.md [--terms banned_terms.txt]
python gate_structure.py  DRAFT.md
python gate_figure_use.py DRAFT.md [--figure-selection figure-selection.md]
```

## Checks at a glance

| check_id     | sev  | goal | meaning |
|--------------|------|------|---------|
| EMDASH-001   | fail | 4b | em-dash `—` outside quoted text / code |
| EMDASH-002   | warn | 4b | en-dash `–` used as a sentence connector |
| ANCHOR-002   | fail | 1  | bracketed-digit anchor not 4-digit zero-padded (`[123]`, `[12345]`) |
| ANCHOR-001   | fail | 1  | `[dddd]` anchor not present in invention-summary |
| ANCHOR-000   | warn | 1  | no invention-summary provided; chain check skipped |
| FIGREF-001   | fail | 2  | figure number not in `figures_index` |
| FIGREF-000   | warn | 2  | no `figures_index` provided; check skipped |
| SOURCES-001  | fail | 4a | `# Sources` block missing, or present more than once |
| SOURCES-002  | fail | 4a | `##` category not in the 5-label enum |
| SOURCES-003  | fail | 4a | partial subgrouping (all-or-nothing violated) |
| SOURCES-004  | warn | 4a | 4+ entries left flat (should be subgrouped) |
| BANNED-001   | fail | 4b | banned literal/regex hit outside quoted text |
| STRUCT-001..004 | warn | 3, 4a | long paragraph / bold / bullet overuse / rule-of-three |
| FIGUSE-001   | fail | 2  | a **selected** figure is never referenced (orphan) |
| FIGUSE-002   | warn | 2  | a referenced figure is not in figure-selection (off-plan) |
| FIGUSE-000   | warn | 2  | no figure-selection provided; check skipped |
| META-001     | fail | 4b | reader-instruction / essay-self-reference posturing |
| META-002     | warn | 4b | softer reader-address worth a human look |
| STUB-001     | warn | 4a | a body section is a stub vs its siblings (merge/expand) |
| CASH-001     | warn | 4a | ticker in labeling context lacks the `$` cashtag prefix |
| DUPE-001     | warn | 4b | a distinctive 5-word phrase repeats verbatim in prose |
| QUOTE-001    | fail | 1  | an invention-summary "verbatim" quote is absent from patent.md |
| QUOTE-000/002 | warn | 1 | quote check skipped (no patent) / summary has no quotes |
| HEDGE-001    | fail* | 4a | safe-harbor boilerplate in the verdict section (*fail iff `closing_posture: firm`, else warn) |
| HEDGE-002    | fail* | 4a | qualifier-led verdict ("a qualified yes") (*same posture rule) |
| HEDGE-003    | warn | 4a | hedge-word density in the verdict section over 50% of sentences |
| HEDGE-000    | warn | 4a | no `##` body section before `# Sources`; hedge check skipped |

## Tunable constants

Top-of-file constants in each gate. Notably: `gate_sources.py` `ALLOWED_CATEGORIES` (the
5-label enum), `gate_banned.py` `BANNED_TERMS_FILE` (+ edit `banned_terms.txt`), the
`gate_structure.py` thresholds. `banned_terms.txt` is the mechanical mirror of
`_shared/references/anti-ai-writing.md` — keep them in sync (the `pipeline-retro` meta-loop
proposes additions with evidence).

## Tests

```bash
python test_gates.py
```

Full `unittest` suite (inline fixtures, no external files); exits nonzero on any failure. The
meta-loop's `meta/regression.py` also runs this suite plus the `meta/fixtures/` cases before
any improvement proposal is applied.
