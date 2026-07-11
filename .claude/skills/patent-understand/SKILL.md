---
name: patent-understand
description: >
  Stage `understand` (first content stage): builds a frozen patent model for the Owner and
  downstream stages. Outputs Problem · Solution · Benefits triad (owner-study-pack),
  invention-summary with Quotable spans + claim scope, Korean owner-briefing (①–④, ⑥),
  figure-primer, open-questions. No thesis angle, no title energy, no essay voice. Use when
  the Owner needs to learn a patent, or as the mandatory pre-design stage of patent-essay.
  NOT for: thesis design (thesis-architect), prose (essay-en-composer), review, promo.
context: fork
agent: patent-reader
---

# patent-understand

**Stage id:** `understand`  
**Contract:** `contracts/stages/understand.yaml`  
**Handoff:** `handoff/00-understand/`

This stage exists so the Owner does not have to re-study the raw patent alone, and so
Design cannot angle a document nobody has modeled. Success is Owner-teachable fidelity,
not an interesting essay thesis.

## North star — three aspects

| # | Aspect | Question |
|---|--------|----------|
| 1 | **Problem** | What was wrong / costly / impossible (per this document)? |
| 2 | **Solution** | How does this invention fix it (mechanism + **claim scope**)? |
| 3 | **Benefits** | What upside does **the patent** assert (not the news cycle)? |

Write these first in `owner-study-pack.md`. Everything else supports that triad.

## Process

### 1. Invention summary (evidence warehouse)

Read `input/patent.md` + cleaned figures. Write
`handoff/00-understand/invention-summary.md` per
`../thesis-architect/references/invention-summary-schema.md` (same schema as legacy
Phase 1 Step 1). Include:

- 4-layer core mechanism  
- **Claim scope map** (locked / open / pinned, or sought-* if pending)  
- Quotable spans + quote anchor table (verbatim; `quote-anchor-conventions.md`)  
- Figure relationships (factual; no thesis mapping yet)

Self-check with `gate_quotes` before finishing.

### 2. Figure primer

Write `handoff/00-understand/figure-primer.md`:

| fig | What the figure shows (spec language) | Key labels / panels |
|-----|----------------------------------------|---------------------|
| fig-01 | … | … |

No “use this for the cover” or thesis tags — that is Design.

### 3. Owner study pack (primary Owner artifact)

Write `handoff/00-understand/owner-study-pack.md` in **Korean** (English quotes stay
English inside quote marks) per `references/owner-study-pack-schema.md`.

Fixed order:

1. **한 줄** — problem → solution → benefit in one sentence  
2. **Problem** + 근거  
3. **Solution** — mechanism steps + claim scope card + 근거  
4. **Benefits** — spec-asserted only + 근거  
5. **Boundary** — 단정 불가 / 원문이 열어 둔 것 (short)  
6. **Self-check** — five questions whose answers are already in the pack (source of
   the keyed quiz in step 3b)

No thesis candidates. No energy registers. No firm/open closing posture.

### 3b. Comprehension quiz bank (keyed; P2)

Write `handoff/00-understand/comprehension-quiz.md` — a **keyed** bank derived from
the study pack §5 self-check. Template shape:
`handoff-template/00-understand/comprehension-quiz.md`. Design contract:
`docs/architecture/comprehension-loop.md` §4.1 / IF-2.

Per item fields (frozen):

- `question:` — Korean; same substance as the §5 self-check line it upgrades  
- `options:` — A / B / C … (exactly one correct)  
- `key:` — the correct letter  
- `aspect:` — one of `problem` | `claim-scope` | `benefits` | `boundary`  
- `rationale:` — quotes the study-pack span the answer rests on (positive framing;
  never names a defensive writing behavior)

Coverage: **≥1 item per aspect**; the **`claim-scope` item is mandatory**. Answers
trace only to the study pack — **no new facts**. This file is the bank the
orchestrator grades against at `understand_confirm`; this worker does not run the
loop and does not write `comprehension-notes.md` or `understand-confirmed.md`.

### 4. Owner briefing (shelf artifact)

Write `handoff/00-understand/owner-briefing.md` per
`_shared/references/owner-briefing-schema.md` sections **①–④ and ⑥** (and header +
한 줄 요약).

- **① Problem** aligns with triad Problem  
- **② Prior solutions & limits** bridges Problem → Solution (not a fourth north-star)  
- **③ Solution** aligns with triad Solution + claim scope vocabulary  
- **④ Benefits** aligns with triad Benefits  
- **⑤ Promo link** — write `없음 (Design 단계에서 갱신)` unless purely bibliographic  
  context is already known; Design may update ⑤ only  
- **⑦ 자료 지도** — point at contract paths; Design/self-audit fill round numbers later  

### 5. Open questions

Write `handoff/00-understand/open-questions.md`: ambiguities, missing pages, claim
vs description tensions the Owner may resolve before Design. Empty list is OK if
explicit: `none`.

### 6. Mechanical gates

```
python3 .claude/skills/_shared/scripts/gate_quotes.py \
  handoff/00-understand/invention-summary.md \
  --invention-summary handoff/00-understand/invention-summary.md \
  --patent input/patent.md

python3 .claude/skills/_shared/scripts/gate_quotes.py \
  handoff/00-understand/owner-briefing.md \
  --invention-summary handoff/00-understand/owner-briefing.md \
  --patent input/patent.md

python3 .claude/skills/_shared/scripts/gate_quotes.py \
  handoff/00-understand/owner-study-pack.md \
  --invention-summary handoff/00-understand/owner-study-pack.md \
  --patent input/patent.md
```

Any QUOTE-001 → fix at source before return.

### 7. Compat copies (for design/gates still on 01-design paths)

Copy (do not move-only):

- `invention-summary.md` → `handoff/01-design/invention-summary.md`  
- `owner-briefing.md` → `handoff/01-design/owner-briefing.md`  
- Ensure `handoff/01-design/figures-index.txt` exists from `input/figures/` listing  

Canonical originals remain under `00-understand/`.

## Forbidden in this stage

- thesis-candidates / thesis-spine / title-lead-candidates  
- essay drafting or voice-canon  
- Investor verdict language, stock claims, “reader should”  
- Treating `essay-context.md` as the mechanism story (it may list questions only)
- Writing `understand-confirmed.md` (orchestrator only, via Owner checkpoint protocol)

## Pre / post

**Pre:** `input/patent.md`; cleaned `input/figures/fig-*.png` (or empty figures with primer noting none).

**Post:**

- All `required_outputs` in `contracts/stages/understand.yaml` exist  
- `comprehension-quiz.md` present (keyed bank; ≥1 item per aspect; claim-scope mandatory)  
- gate_quotes PASS on summary, briefing, study pack  
- Compat copies present under `01-design/`  
- Return value to orchestrator (NOT shown to Owner as-is): 한 줄 triad + path to study pack + open-questions count + quiz item count  
- The orchestrator then runs the understand_confirm checkpoint (renders study-pack triad + open-questions INLINE to the Owner — paths alone never satisfy the protocol). On `--comprehension-check` runs the orchestrator (not this worker) drives the P2 grading loop against `comprehension-quiz.md` and writes `handoff/00-understand/comprehension-notes.md`.

## References

- `references/owner-study-pack-schema.md` — triad pack contract  
- `../thesis-architect/references/invention-summary-schema.md`  
- `../thesis-architect/references/quote-anchor-conventions.md`  
- `_shared/references/owner-briefing-schema.md`  
- `contracts/stages/understand.yaml`  
- `contracts/glossary.md`  
