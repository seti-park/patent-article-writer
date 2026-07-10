# Thesis candidate presentation (Step 3)

Each candidate presented in a uniform format. The Owner compares via the table at the end and selects one (orchestrator soft checkpoint / design title-lead surface; forked worker raises `OWNER_QUESTION` if it needs a pick mid-run — see `patent-essay/SKILL.md` Owner checkpoint protocol).

## Per-candidate format

```markdown
## Candidate <N>: <short label>

**Statement**: <single sentence thesis>

**Framing**: <voice direction phrase — implicit, replaces explicit mode taxonomy>

**Evidence required**:
- <category 1>
- <category 2>
- <category 3>

**Evidence available in invention-summary**:
- ✓ <category that has Quotable spans>
- ✓ <another>
- ✗ <category with gap — needs more extraction or external research>

**Structural tension**: <what arc the essay would follow>

**Risks**:
- <thesis-specific weakness or audience pushback>

**Grounding (4-axis — draft, locked in Step 4)**:
- Claims anchor: <청구항 + limitation>
- Problem anchor: <paragraph + quote>
- Effect anchor: <paragraph + quote 또는 why_novel synthesis>
- Baseline-difference anchor: <industry baseline + difference>

**Q7 hook pattern (draft, hard-gated in Step 5)**:
- corporate-narrative-friction | technical-impossibility
- anchor: <pattern-specific anchor>

**Adversarial defense (draft, locked in Step 6)**:
- Strongest objection: <one-line>
- Mitigation: <how>
```

## Comparison table

After presenting candidates, summarize as:

```markdown
## Comparison

| Dimension | Candidate 1 | Candidate 2 | Candidate 3 |
|-----------|-------------|-------------|-------------|
| Evidence completeness | Full | Partial | Full |
| Audience appeal | High | Medium | High |
| Architectural depth | Medium | High | High |
| Defensive strength | High | Medium | Low |
| 4-axis grounding | 4/4 | 3/4 (no baseline) | 2/4 (no problem, no effect) |
| Q7 hook | corporate-narrative-friction | technical-impossibility | (none — disqualified) |
| Hook accessibility | High | High | n/a |
```

## Recommendation

After the comparison table, give a Claude recommendation. Single line; the Owner decides via the orchestrator-relayed checkpoint.

```markdown
## Recommendation

Candidate 1 — strongest 4-axis grounding (Bosch baseline well-documented in context research) and clearest hook (Tesla公식발표 narrative is specific and recent).
```

## Owner selection options

Owner 가 다음 중 하나로 응답 (orchestrator ASK; worker never addresses the Owner directly):

1. **Select Candidate N** — proceeding with that candidate.
2. **Combination Candidates A + B** — combine. Requires multi-spine override per `single-spine-default.md`. Combined statement, combined framing, combined evidence required.
3. **Revise Candidate N** — keep candidate, adjust statement / framing / one axis.
4. **Reject all, restart** — back to Step 2 (context research) or Step 1 (invention-summary 재추출).

## After selection

선정된 candidate 의 4-axis grounding + Q7 hook pattern + adversarial defense 를 `thesis-spine.md` 의 fields 로 lock. Step 9 (figure mapping) + Step 10 (fact-check log seed) 진입.

## Patent-reader 와의 cross-skill 정합 (v1 → v2)

v1 의 `patent-reader.thesis_seeds` 는 별도 skill 의 output 이었음. v2 에서는 `invention-summary.md` §"청구항 분석 — 4-layer core mechanism" Layer 4 `innovation_angles` 가 동일 역할.

- `invention-summary.md` Layer 4 = base candidates (1-2 axis already anchored)
- `thesis-architect` Step 3-6 = 4-axis verification + Q7 gate + defense

Layer 4 angles 가 부족하면 Step 1 (invention-summary 재추출) 으로 회귀. Extraction 이 thesis 보다 cheap.
