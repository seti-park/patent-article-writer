---
proposal_id: 2026-07-05-promo-bold-selection-kr-long
created: 2026-07-05T00:00:00Z
status: applied (2026-07-05, owner-directed, regression-gated)
lever: multi (reference-edit + format-contract change + model-allocation rule)
goal: "5"
root_cause_stage: promo
root_cause_artifact: promo-composer promo-format.md v2 (KR briefing-sentence reuse rule + digest hedge-parity rule + deliverable mix)
recurrence_count: 1
confidence: high
triggering_findings:
  - essay_id: etched-0378175-memory-in-writing-r2
    source: human-revision (owner read of promo v1, 2026-07-05, class promo-safe-harbor-overweight)
---

## Headline: the promo inherited the pipeline's insurance reflexes, and its formats did not match the channels

Owner findings on the shipped promo pack (three, one root):

1. **Safe-harbor overweight.** The KR post spent 2 of 4 sentences on prosecution status
   ("다만 최종거절 후 RCE로 심사가 계속 중이라 청구 범위는 아직 확정이 아닙니다"), and
   the EN digest carried a full prosecution paragraph. Readers want the BOLD claim in the
   promo; the article is where the claim gets priced. Structural causes: (a) the v2 KR
   rule "owner-briefing 문장 표현을 우선 재사용" — the briefing is an owner-comprehension
   document whose stance sentences carry insurance BY DESIGN, so reuse imported hedges
   into promo copy; (b) the v2 digest rule "hedge 강도는 essay 와 동일" inherited essay
   v5's procedure overweight into the digest's pricing paragraph.
2. **Format/channel mismatch.** v2 shipped KR short (<=280자) + EN long digest + EN
   thread. The publisher's primary channel is Korean: the KR deliverable deserved the
   long form, and the EN digest had no channel of its own.
3. **Model allocation unstated.** Nothing recorded that the posting copy must be written
   by the strongest model; a future run could silently pin promo to a cheap model.

## Applied (v3 contract, 2026-07-05)

- **Bold-selection rule** (promo-format.md, new top section): the promo leads with the
  boldest claim the essay supports, selected from the protected surface — boldness by
  selection, never fabrication; safe-claims defense unchanged. Insurance <=1 status
  clause per deliverable, after the beat, never a "다만+유보" close. Process narration
  (rejections, RCE, fees, liens) 0 — the article hedges, the promo points. Hedge
  inheritance is one-way (no overreach, no hedge import). Briefing reuse is
  technical-vocabulary-only; stance sentences never become promo copy.
- **Deliverables reshaped**: (1) KR long-form promo post 400-800자 (digest 단락 아크의
  한국어 이식: 훅 → 메커니즘 → 함의/receipts → 아티클 포인터), (2) EN thread 3-5
  tweets (bold hook / one-beat middles / call-first verdict + link). EN digest dropped;
  frontmatter `digest_posture` → `promo_posture`.
- **Model allocation**: posting copy composed by the session's strongest model —
  `model: inherit` declared LOAD-BEARING in the agent frontmatter, SKILL.md, and
  CLAUDE.md; verification may be delegated, composition may not.
- **Verification header** gains a `bold_selection` line (lead source + insurance count
  per deliverable) so the pack self-reports its boldness budget.
- **Regenerated**: essays/etched-us20240378175-r2/promo/promo-pack.md promo_version 2
  against essay v6, copy authored in the main session (Fable 5), mechanically verified
  (counts, hygiene, per-phrase fact-trace) by a pinned-cheap instrument agent.
- **Files**: promo-composer/SKILL.md, references/promo-format.md (v3 rewrite),
  .claude/agents/promo-composer.md, CLAUDE.md, attribution-table row +
  normalize_revision_notes.py CLASS_MAP (`promo-safe-harbor-overweight`), ledger record.

## Watch

- If a future promo again narrates process, the Final Checklist bold_selection line and
  the class `promo-safe-harbor-overweight` are the tripwires; candidate hard check: a
  promo-side lexicon scan (same procedure lexicon as SURF-005) if the class recurs.
- closing-posture.md still governs the closing call only; no change needed there.
