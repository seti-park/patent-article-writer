# `owner-study-pack.md` schema

Primary **Owner learning** artifact of stage `understand`. Designed for a 20–40 minute
study session. The machine warehouse is `invention-summary.md`; this file is the teachable
triad.

Language: Korean body; English only inside verbatim quote marks. Every patent-derived
claim carries an inline `[dddd]` anchor. Sections Problem / Solution / Benefits each end
with a gate-parseable `**근거 (verbatim):**` block (same line format as owner-briefing).

## Skeleton

```markdown
# Owner Study Pack — <patent id>

- **특허 번호**: …
- **상태**: 등록 | 출원 (… )
- **학습 목표**: Problem · Solution · Benefits 를 원문 없이 설명할 수 있을 것

## 한 줄
<problem → solution → benefit 를 한 문장으로>

## 1. Problem (무엇이 문제였나)
…
**근거 (verbatim):**
- `[dddd]`: "…"

## 2. Solution (어떻게 푸나)

### 2a. Mechanism
1. …
2. …
(필요 시 fig-NN 참조 — figure-primer 와 일치)

### 2b. Claim scope card
| Claim | Plain meaning | Scope |
|-------|---------------|-------|
| … | … | locked / open / pinned / sought-* |

**근거 (verbatim):**
- …

## 3. Benefits (무엇이 좋아지나)
- 명세서가 주장하는 효과만. 수치에는 앵커.
- 외부/회사 주장은 넣지 않는다 (briefing ⑤ / fact-check 영역).

**근거 (verbatim):**
- …

## 4. Boundary (짧게)
- **단정 불가**: …
- **원문이 열어 둔 것**: …

## 5. Self-check (답이 이미 위에 있음) — source of comprehension-quiz items
<!-- P2: these become keyed items in handoff/00-understand/comprehension-quiz.md
     (IF-2). Keep answers traceable to sections above; no new facts. -->
1. 이 특허가 출발점으로 삼는 문제는?                         → aspect: problem
2. 핵심 독립항이 요구하는 것은?                             → aspect: claim-scope  (mandatory)
3. 명세서 선호일 뿐인 것은? (청구와 구분)                   → aspect: claim-scope or boundary
4. 문서가 주장하는 효과 한 가지는?                           → aspect: benefits
5. 독자 앞에서 단정하면 안 되는 것 한 가지는?               → aspect: boundary
```

The keyed bank (`comprehension-quiz.md`) is the graded form of this section. Each
quiz item must carry `question:` / `options:` / `key:` / `aspect:`
(`problem|claim-scope|benefits|boundary`) / `rationale:` (quotes a study-pack span).
≥1 item per aspect; the `claim-scope` item is mandatory. See
`handoff-template/00-understand/comprehension-quiz.md` and design
`docs/architecture/comprehension-loop.md` §4.1 / IF-2.

## Rules

1. Order is fixed: Problem → Solution → Benefits.  
2. Solution without claim scope card is incomplete.  
3. Benefits must answer a bottleneck named under Problem when the spec does.  
4. No thesis, energy register, closing_posture, or promo bold-selection.  
5. Quotes ≥ 8 characters; verbatim; gate_quotes must PASS.  
6. Self-check answers (and the keyed quiz derived from them) introduce no new facts —
   every correct option traces to a span already in sections 1–4.  

