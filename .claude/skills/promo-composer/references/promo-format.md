# Promo format: the promo-pack contract + per-deliverable rules

One file, two paste-ready deliverables. v4 (2026-07-08, proposal
`2026-07-08-promo-explainer-register-message-units`) keeps v3's deliverable pair —
(1) a **Korean long-form promo post** (400-800자, the publisher's primary channel) and
(2) an **English thread** — but re-specifies the KR register (존댓말 설명체, 직역 금지),
the composition unit (핵심 1개 + 티저, not whole-essay compression), and the thread
unit (message-unit posts; the owner is X Premium, so 280 chars no longer binds).
v2/v3's grounding, counting, and hygiene machinery is carried intact.

## The bold-selection rule (promo leads bold; the article hedges)

Owner decision, 2026-07-05 (class `promo-safe-harbor-overweight`): the promo's job is
the **boldest claim the essay's evidence supports**. Readers meet the promo first and
want the strong version; the article is where the claim gets priced, bounded, and
risk-hedged — the promo points there for exactly that reason.

- **Boldness comes from SELECTION, never fabrication.** The hook vocabulary is the
  protected surface (reader_sentence, signature lines, title, lead ¶1, closing call);
  pick the strongest of those lines and lead with it. The safe-claims defense is
  unchanged: every factual phrase still traces to the three sources, verbs of certainty
  stay verbatim-consistent (an application-era essay's "asks for" never becomes
  "patented"). Bold and grounded are not in tension: selection does the work.
- **Insurance budget: at most ONE status clause per deliverable**, positioned AFTER the
  bold beat, only when the essay's two-sided call requires it — and phrased as a fact
  with tension ("the patent office hasn't said yes yet"), never as a safe-harbor
  disclaimer ("다만 ... 확정이 아닙니다" 류 유보 마무리 금지).
- **Process narration 0.** Examination mechanics (최종거절, RCE, office actions), fees,
  liens, collateral walks are ARTICLE material, never promo material. The promo may
  point at them ("특허청 문턱에서 어디에 서 있는지까지 아티클에 정리했습니다"); it does
  not narrate them. This is the attention-budget doctrine
  (`_shared/references/reader-energy.md` §6) applied at promo altitude, where the budget
  is stricter than the essay's: the promo is 100% payload plus one status clause.
- **Hedge inheritance is one-way.** The promo must not OVERREACH the essay (never assert
  beyond it), but it also does not INHERIT the essay's in-body hedges: the essay hedges
  because it argues; the promo selects because it invites. Posture agreement
  (`closing-posture.md`) applies to the CLOSING call only.
- **Briefing reuse is vocabulary-only.** `owner-briefing.md` is an owner-comprehension
  document — its stance sentences carry insurance by design. Reuse its 검수된 기술
  어휘 (무스위치 하드와이어링, 채널-열 직결, 결합 어레이 등); never reuse its hedge/
  status SENTENCES as promo copy (v1 promo inherited "다만 ... 확정이 아닙니다" exactly
  this way).

## The promo-pack.md contract

Path: `essays/<id>/promo/promo-pack.md`. Structure, in order:

1. **YAML frontmatter**: `essay_id` (copied from essay-final.md frontmatter),
   `essay_source`, `closing_posture` (copied from essay-final.md), `promo_posture`
   (A/B/C/D per `closing-posture.md`; applies to both deliverables' closes),
   `promo_version`, `owner_briefing` (`read` or `ABSENT`).
2. **Verification Status header** between `=== Verification Status (promo-composer,
   promo-pack) ===` and `=== Deliverables ===` markers. Every line is a measured number
   or PASS/FAIL, never a bare checkmark: sources read, fact_trace + dropped-facts list,
   Sub-rules 1/2/3, per-deliverable counts, posture agreement, **bold-selection line**
   (which protected line leads each deliverable + insurance-clause count per
   deliverable), hygiene tallies, attachment list, `suspected_essay_defects` (default
   `none`).
3. **Two deliverable sections** (`## 1.` KR long post, `## 2.` EN thread). Each section
   = one or more fenced ```` ```text ```` blocks (the paste surface) followed by plain
   metadata list lines (counts, attach path, alt text).

**The fence is the strip boundary.** Nothing outside a fence is ever pasted, everything
inside a fence is paste-ready exactly as written. No separate publication file exists
for promo.

Pack-wide hygiene: em-dash 0 and bold 0 anywhere in the file (scaffolding included, so a
sloppy copy can never smuggle formatting into a post); emoji <=1 total; hashtags 0;
banned-term discipline per `_shared/scripts/banned_terms.txt`.

## Deliverable 1: Korean long-form promo post

발행자가 자기 아티클을 소개하는 X 장문 포스트 (프리미엄 장문). 한 개의 fenced block.
v2 의 280자 단문을 대체한다. 발행자의 주 채널이므로 pack 의 첫 deliverable 이다.

- **분량**: 400-800자, 공백 포함, `[ARTICLE-LINK]` 슬롯은 23자로 계산 (X 의 t.co 단축
  길이). 280자 단문이 아니라 장문이다: 기술의 핵심 그림 하나를 온전히 설명할 공간이
  생겼으므로, 그 공간은 기술에 쓴다.
- **목소리 (v4, owner 결정 2026-07-08)**: **존댓말 설명체 (-ㅂ니다체)**. 호기심 많은
  고등학생/학부생에게 개념을 차근차근 설명하는 톤 — 에세이의 reader-profile 과 같은
  독자상이다. 용어는 첫 등장에서 바로 정의한다 ("이 층을 전공정(front-end)이라고
  부릅니다"). 설명형 수사 의문 <=1 허용: 단락 첫 문장에서만, 바로 다음 문장이 답한다
  ("위치 하나 바꾼 것이 왜 중요할까요? ... 때문입니다"). SNS 식 말 걸기 ("여러분",
  독자 호명, 청유형 후킹) 는 금지 — 설명체이지 대화체가 아니다. 과장 배제와 발행자
  1인칭 절제는 유지; 대담함은 수식어가 아니라 문장 선택에서 나온다 (bold-selection
  rule). 리듬: 같은 길이의 평서문 연쇄를 피하고 짧은 문장/정의/질문으로 변화를 준다.
- **직역 금지 (v4)**: 충실성은 내용에만 binding 이다 — 숫자/날짜/이름/확실성 동사는
  에세이와 verbatim-consistent, 그러나 **영어 구문은 절대 이식하지 않는다**. 의문절
  주어 ("~느냐가"), 영어 관용구 직역 ("3사만의 클럽이 아니게 된다") 이 대표 위반.
  protected line 의 "압축" 은 내용 압축이지 문장 구조 복제가 아니다; 모든 문장을
  한국어 구문으로 재작성한다.
- **구조 (v4: 서사 훅 + 핵심 1개 + 티저; 3-5 단락, 단락당 1-5 문장)** — 프로모는
  요약이 아니라 초대다. 에세이 전체 아크를 압축하지 않는다:
  - **¶1 서사 훅**: 에세이가 서사(아이러니, 사건)를 가지면 스토리로 연다 — 서사도
    protected surface 다 (에세이 lead 섹션에서 선택; 새 서사 발명 금지). 대담한
    주장은 셋업 직후에 landing 한다. thesis 압축으로 여는 것은 스포일러이자 초록이다.
    보험성 사실 0.
  - **¶2(-3) 핵심 1개**: 이 에세이의 가장 중요한 포인트 하나를 제대로 설명한다
    (메커니즘 또는 함의). 구체 수치/verbatim 인용은 그 핵심 1개를 설명하는 데
    필요한 것만 — 한 문장에 스펙 나열 (v1 실패: 용량/단수/TSV/UCIe/풋프린트 6개)
    은 청구항처럼 읽힌다. 나머지 비트는 다음 항목의 티저로 보낸다.
  - **마지막 ¶ 티저 + 포인터**: 아티클에 남은 내용의 **모양만** 가리키고 답은 주지
    않는다 ("옮기기만 하고 없애지는 못한 부품이 하나 있다" — 부품 이름은 아티클에).
    티저 문장에 결론이 들어 있으면 티저가 아니라 요약이다. 허용된 ONE status clause
    는 여기 또는 핵심 단락에, 포인터와 결합해 배치하는 것이 기본형. `[ARTICLE-LINK]`
    로 끝난다.
- **Insurance budget**: status clause 최대 1 (bold-selection rule). 심사 절차 서사
  (최종거절, RCE, 담보) 0. "다만/그러나 + 유보" 형 마무리 금지.
- **금지**: 클릭베이트 의문형 후킹 ("과연?", "어떻게 됐을까요?" 류 — 설명형 수사
  의문과 구분: 클릭베이트는 답을 미끼로 걸고, 설명형은 즉시 답한다), 해시태그, 볼드,
  em dash. 감탄사와 느낌표도 쓰지 않는다. 이모지는 팩 예산 <=1 의 슬롯이 이 포스트의
  마지막 문단에만 있다 (0 이 자연스러우면 0).
- **Protected terms verbatim**: 특허번호, 회사명, 부품번호, 영어 인용구는 원문 그대로.
  따옴표 안은 영어 원문을 유지하고 번역은 따옴표 밖에 둔다 (briefing 과 같은 규율).
- **한국어 표현의 출처**: 기술 어휘는 `owner-briefing.md` 의 검수된 표현을 우선 재사용;
  stance/hedge 문장은 재사용 금지 (bold-selection rule). briefing 이 없으면 에세이의
  protected lines 에서 내용을 가져오되 (직역 금지 rule 적용) 숫자/날짜/이름은 원문과
  일치시킨다.

## Deliverable 2: English thread (2-4 message-unit posts)

English. One fenced block per post. **v4 (owner decision 2026-07-08): the unit of a
post is ONE MESSAGE, not a character count.** The owner posts from an X Premium
account, so 280 chars does not bind; a post may run several paragraphs. Chars per post
are still MEASURED and reported in the header (no bound). Numbering ("1/") is the
owner's call at post time; each post must read standalone (Sub-rule 3 anchors
self-contained). Splitting one argument across two posts because of length is the v1
failure mode this rule exists to prevent; conversely, two messages never share one post.

- **Post 1 (서사 훅, the story)**: if the essay carries a narrative (irony, an event),
  open with it — the narrative is protected surface (the essay's own lead section;
  never coin a new story). The FIRST SENTENCE is what a collapsed feed preview shows:
  it must hook alone. The bold claim lands right after the setup (end of post 1 or
  top of post 2), not as the opening line — a thesis-first opening is a spoiler.
  NO insurance facts anywhere in post 1. Hashtags 0; a single `$cashtag` only if the
  essay itself used one. Default attachment lives here (`figure-attachment-policy.md`).
- **Middle post(s) (0-2: the core point)**: ONE message each — the essay's most
  important point, properly explained (mechanism and its implication may share a post
  when they are one argument). Concrete numbers/quotes only in service of that one
  point, never as a feature list. The interpretation-boundary label (what the document
  says vs what the essay reads into it) rides here, after the beat.
- **Final post (limits + call + link)**: what the filing honestly keeps or does not
  settle (the essay's own bear-case beat), then the essay's call, call-first; the ONE
  permitted status clause may ride here after the call (never qualifier-first); a
  teaser may name the SHAPE of what the article adds (a date to watch, a part not
  removed) without giving the answer; ends with `[ARTICLE-LINK]`.

No emoji, no bold markers, no ALL-CAPS words (acronyms and part numbers excepted) in
any post.

## Hedge 정책 (bold-selection rule 의 표)

| Hedge 영역 | Promo 규칙 |
|---------|-----|
| Overreach (essay 보다 센 단정) | 0 건 — verbs of certainty 는 essay 와 verbatim-consistent |
| Essay 본문 hedge 의 상속 | 상속하지 않는다 — promo 는 선택하는 장르다; hedge 는 아티클의 몫 |
| Status clause | deliverable 당 최대 1, bold beat 뒤, 유보 마무리 금지 |
| 심사 절차 서사 (거절/RCE/담보) | 0 건 — 아티클 포인터로만 가리킨다 |
| Safe-harbor boilerplate | 0 건 ("a patent doesn't guarantee..." 류, `closing-posture.md` 회피 목록) |
| Universal claims / "significantly" 류 | 0 건 (essay 와 동일) |
| 시점 표현 | 정확성 필수 + `fact-verification.md` Sub-rule 1, 2 |

Essay 에 명시 없는 fact 는 promo 에 넣지 않는다 (drop, don't fetch — 불변).

## Counting methods

- KR 자수: paste block 본문을 그대로 세되 공백 포함, 줄바꿈 제외, `[ARTICLE-LINK]` 는
  23자로 치환해 계산. 예: `printf %s "<본문>" | wc -m` 후 슬롯 보정.
- Post chars: `printf %s "<post>" | wc -c` (English ASCII 기준), 링크 슬롯 23자 보정.
  v4: bound 없음 (Premium) — 그래도 측정해서 header 에 적는다.
- 측정값을 Verification Status header 와 각 deliverable 의 metadata line 에 그대로
  적는다. "약 500" 같은 추정치 금지.

## Final Checklist

Pack level:

- [ ] Verification Status header 완결, 모든 줄이 측정치 또는 PASS/FAIL
- [ ] bold_selection line: 각 deliverable 의 리드가 어느 protected line 압축인지 +
      insurance clause 수 (<=1/deliverable, 절차 서사 0)
- [ ] Fact trace: 모든 factual phrase 가 세 source 의 문장에 매핑 (`fact-verification.md`)
- [ ] Sub-rule 1 (시점 sequence) / 2 (date arithmetic) / 3 (quote anchor) PASS
- [ ] Em dash 0, bold 0, emoji <=1 (KR post closing 슬롯만), 해시태그 0
- [ ] Banned terms 0 (`_shared/scripts/banned_terms.txt`) + Tier-2 tells 점검
  (`_shared/references/anti-ai-writing.md`)
- [ ] Attachment 는 `publication-package/` 경로 + alt-text line
- [ ] `suspected_essay_defects` line 존재 (none 또는 routed; essay 는 안 건드림)

KR long post:

- [ ] 400-800자 (공백 포함, 링크 슬롯 23자)
- [ ] ¶1 이 서사 훅 (에세이 lead 에서 선택), 보험성 사실 0; 대담한 주장은 셋업 직후
- [ ] 핵심 1개만 제대로 설명 (전체 아크 압축 아님); 한 문장에 스펙 나열 없음
- [ ] 티저가 답이 아니라 모양만 가리킴 (티저 문장에 결론 없음)
- [ ] status clause <=1, bold beat 뒤, "다만+유보" 마무리 아님; 절차 서사 0
- [ ] 마지막 문장이 아티클 포인터
- [ ] 클릭베이트 의문형 0 (설명형 수사 의문 <=1, 단락 첫 문장 + 즉시 응답), 해시태그 0,
      느낌표 0, 이모지 <=1 (마지막 문단만)
- [ ] 존댓말 설명체 (-ㅂ니다체), 용어 첫 등장 시 정의, SNS 말 걸기 없음
- [ ] 직역투 0: 영어 구문 이식 없음 (의문절 주어, 영어 관용구 직역), 종결어미/문장
      길이에 변화
- [ ] 영어 인용은 따옴표 안 원문 그대로, 번역은 따옴표 밖
- [ ] 특허번호 / 회사명 / 숫자 / 날짜 원문 일치; briefing hedge 문장 재사용 없음

Thread:

- [ ] 2-4 posts, post 당 메시지 1개 (chars 측정·보고, bound 없음)
- [ ] P1 이 서사 훅, 첫 문장이 collapsed-preview 에서 단독으로 훅, 보험성 사실 0
- [ ] 어떤 argument 도 길이 때문에 두 post 로 쪼개지지 않음; 두 메시지가 한 post 를
      공유하지 않음
- [ ] 해석 경계 라벨 (문서가 말하는 것 vs 에세이의 해석) 이 core-point post 에, beat 뒤
- [ ] 마지막 post 가 call-first verdict (+ status clause <=1, call 뒤) + 티저 (답 없이
      모양만) + `[ARTICLE-LINK]`
- [ ] 각 post standalone-readable (baseline / referent / anaphoric anchor 자급)

## v2 → v3 변경 사항

| 영역 | v2 promo-composer | v3 promo-composer |
|---|---|---|
| Deliverable | KR 단문 (<=280자) + EN digest (280-340w) + 3-tweet sketch | KR 장문 (400-800자) + EN thread (3-5 tweets); EN digest 폐기 (owner 결정 2026-07-05) |
| Hedge 자세 | digest hedge 강도 = essay 와 동일 | bold-selection rule: promo 는 boldest-supportable 을 리드, insurance <=1 clause/deliverable, 절차 서사 0; hedge 는 아티클의 몫 |
| Briefing 재사용 | 문장 표현 우선 재사용 | 기술 어휘만 재사용; stance/hedge 문장 재사용 금지 |
| Posture 필드 | `digest_posture` | `promo_posture` (양 deliverable 의 closing 에 적용) |
| 작성 모델 | (명시 없음) | posting copy 는 세션 최강 모델이 직접 작성 (`model: inherit`, 절대 하위 모델로 pin 금지) — 검증 절차만 위임 가능 |
| Grounding / counting / hygiene | safe-claims defense, 측정 의무, em-dash/bold/hashtag 0 | 동일 (carry-over, 불변) |

v1 → v2 변경 이력은 git history 의 이 파일 이전 판 참조.

## v3 → v4 변경 사항 (proposal 2026-07-08-promo-explainer-register-message-units)

| 영역 | v3 | v4 |
|---|---|---|
| KR register | 건조한 평서문 (-다체, working-dialogue register) | 존댓말 설명체 (-ㅂ니다체, 학부생에게 설명하듯; 용어 첫 등장 시 정의; 설명형 수사 의문 <=1; SNS 말 걸기 금지) |
| KR 충실성 | protected lines "직역" 허용 | 직역 금지 — 내용(숫자/날짜/이름/확실성 동사)만 binding, 구문은 한국어로 재작성 |
| KR 구조 | 훅(thesis 압축) → 메커니즘 → 함의 → 포인터 (전체 아크) | 서사 훅 → 핵심 1개 → 티저(모양만) + 포인터; 전체 아크 압축 금지, 스펙 나열 금지 |
| EN thread 단위 | 3-5 tweets, 각 <=280 chars | 2-4 message-unit posts (X Premium, bound 없음, chars 측정만); post 1 첫 문장 = collapsed-preview 훅 |
| Grounding / hygiene / insurance / posture | (v3) | 동일 (carry-over, 불변) |
