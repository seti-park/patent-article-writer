---
proposal_id: 2026-07-08-promo-explainer-register-message-units
created: 2026-07-08T00:00:00Z
status: applied (2026-07-08, owner-directed, regression-gated)
lever: multi (reference-edit + format-contract change)
goal: "5"
root_cause_stage: promo
root_cause_artifact: promo-composer promo-format.md v3 (KR 직역 fallback + 건조한 평서문 register + 전체 아크 압축 규칙 + EN 280-char tweet unit)
recurrence_count: 1
confidence: high
triggering_findings:
  - essay_id: intel-us20260191095-backend-hbm
    source: human-revision (owner rewrite session of promo v1, 2026-07-08, classes promo-translationese-register / promo-summary-not-invitation)
---

## Headline: the promo summarized the essay instead of inviting to it, and its Korean was English wearing Korean words

Owner read of the shipped v1 pack: "어색하고 딱딱하다". The owner then rewrote both
deliverables in-session; the diffs decompose into five findings with two roots. Both
roots are SPEC-INDUCED: v1 followed promo-format.md v3 faithfully, and v3 itself
produced the stiffness. (That is the meta-lesson: when an owner rewrite reads
this differently from spec output, diff the SPEC, not just the copy.)

### Root 1 (KR): fidelity was binding SYNTAX, not just content

1. **직역투 (translationese).** v1 KR sentences were syntax-level transplants of the
   essay's English: "who can make HBM stops being a three-company club" became "HBM을
   누가 만들 수 있느냐가 더 이상 3사만의 클럽이 아니게 된다" (interrogative-clause
   subject + English idiom, neither native Korean). Spec cause, two rules: "briefing 이
   없으면 에세이의 protected lines 를 직역하되" and bold-selection's "KR lead =
   reader_sentence 압축" read as sentence-structure transplantation. The safe-claims
   defense needs facts, numbers, and certainty verbs to stay verbatim-consistent; it
   never needed English syntax. Fix: fidelity binds CONTENT; syntax is always rewritten
   as native Korean.
2. **Register mismatch.** v3 prescribed 건조한 평서문 (-다체, working-dialogue
   register). The owner's channel voice is 존댓말 설명체: explaining to a curious
   student (the SAME reader the essay's reader-profile targets — advanced high school
   to early undergraduate), defining each term at first use, allowed to open a
   paragraph with one rhetorical question it immediately answers. NOT the SNS
   direct-address tone ("여러분", 말 걸기) — the owner rejected that variant explicitly.
   The -다체 flat declarative chain is what read as 딱딱함.
3. **단조 리듬 (uniform rhythm).** Five same-length -다 declaratives, no question, no
   short sentence, no register variation. Partly a consequence of finding 2; kept
   separate because rhythm needs its own checklist eye even in 존댓말.

### Root 2 (both deliverables): the unit of composition was wrong

4. **압축 과다 — 요약이지 초대가 아니다.** v1 compressed the essay's ENTIRE argument
   arc (backend → foundry implication → 1T1C limit → yield verdict) into 5 paragraphs;
   one sentence carried six spec items (0.5-5 GB / 8단 / TSV 거터 / UCIe / 베이스
   다이 / HBM4 풋프린트) with zero explanation, reading like claim language. Spec
   cause: the v3 arc (훅 → 메커니즘 → 함의 → 포인터) implicitly covered the whole
   essay, and "구체 숫자/날짜/인용 >=1" rewarded density. A promo that gives the whole
   argument leaves no reason to click. Fix: the promo carries ONE core point, properly
   explained; everything else becomes a teaser that names the SHAPE of what the article
   holds, not the content ("옮기기만 하고 없애지는 못한 부품이 하나 있다" — the answer
   stays in the article).
5. **EN thread split by chars, not messages.** v1's five tweets were the essay's
   sections cut to fit <=280 chars: one argument (front-end/back-end mechanism + its
   foundry implication) was mechanically split across tweets 2-3, and every tweet ran
   at identical summary density. The owner is an X Premium user: the 280-char bind is
   obsolete for this channel. Fix: the unit of a post is ONE MESSAGE (multi-paragraph
   allowed); the intel run resolves to three (서사 훅 / 핵심+해석 경계 / 한계+티저+link).

### What did NOT change (carried intact)

Safe-claims defense (three sources, drop-don't-fetch), verbatim-consistent numbers/
dates/names/certainty verbs, bold-selection-by-selection-never-fabrication, insurance
<=1 status clause per deliverable, process narration 0, posture agreement, hygiene
budgets (em-dash 0, bold 0, emoji <=1, hashtags 0, banned terms), measured-counts
duty. The 서사 훅 is not a grounding loosening: the irony lead (the company that left
memory) IS protected surface — it is the essay's own §1.

## Applied (v4 contract, 2026-07-08)

- **promo-format.md v4** (KR rules rewritten, EN deliverable re-specified, both
  checklists updated, v3→v4 delta table appended):
  - KR register: 존댓말 설명체 (-ㅂ니다체), 용어 첫 등장 시 정의, 설명형 수사 의문
    <=1 (단락 첫 문장, 즉시 응답; 클릭베이트 의문형은 여전히 0). SNS 말 걸기 금지.
  - 직역 금지: 충실성은 내용(숫자/날짜/이름/확실성 동사)에만 binding; protected
    line "압축"은 내용 압축이지 구문 이식이 아니다.
  - 구조: 서사 훅 (에세이가 서사를 가지면 스토리로 연다; bold beat은 셋업 직후) →
    핵심 1개 설명 → 티저 (모양만 가리키고 답은 아티클로). 전체 아크 압축 금지;
    구체 수치는 핵심 1개를 설명하는 데 필요한 것만.
  - EN thread: 2-4 message-unit posts (X Premium, no char cap; chars still measured
    and reported), post 1 first sentence = collapsed-preview hook, one message per
    post, standalone-readable, final post call-first + [ARTICLE-LINK].
- **SKILL.md + .claude/agents/promo-composer.md + CLAUDE.md**: deliverable
  descriptions, process steps 6-7, hygiene counting, and register-fence lines updated
  to match v4.
- **meta**: CLASS_MAP + attribution-table rows for `promo-translationese-register`
  and `promo-summary-not-invitation`; ledger records (origin: human-post-accept).
- **Regenerated**: essays/intel-us20260191095-backend-hbm/promo/promo-pack.md
  promo_version 2 against essay v6 (KR 772자 존댓말 설명체 4단락; EN 3 posts
  439/775/552 chars), copy authored in the owner session (Fable 5), counts and
  hygiene mechanically measured.

## Watch

- If a future KR promo reads stiff again, the cheap tripwire is a 종결어미 scan:
  -다체 종결이 지배적이면 register 위반. Candidate mechanical check (promo-side,
  pack sits outside run_gates.py): flag a KR paste block whose 종결어미가 모두
  평서형 -다 인 경우 + flag any EN post that is a <=280-char fragment of the
  adjacent post's argument. Propose as a hard check only if either class recurs.
- The 400-800자 KR band survived this rewrite exactly (772자) — 설명체가 본질적으로
  길어지면 band 재검토, 지금은 변경 없음.
- Teaser discipline is the fragile part: a future run may "tease" by restating the
  conclusion. The test: does the teaser sentence contain the ANSWER or only its
  shape? (v2 KR ¶4 and EN P3 close are the reference examples.)
