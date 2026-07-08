---
essay_id: intel-us20260191095-backend-hbm
essay_source: essays/intel-us20260191095-backend-hbm/essay-final.md
closing_posture: measured
promo_posture: D
promo_version: 2
owner_briefing: read
---

# Promo pack: intel-us20260191095-backend-hbm

=== Verification Status (promo-composer, promo-pack) ===
sources: essay-final.md (draft_version 6) + publication-package/publication.md + owner-briefing.md (read)
revision_basis: owner rewrite session 2026-07-08 (v1 findings: KR 직역투 + 압축 과다 + 서사 훅 미사용 + 단조 리듬; EN 글자수 단위 기계 분할) -> proposal 2026-07-08-promo-explainer-register-message-units
fact_trace: PASS (every factual phrase in both deliverables maps to a sentence in essay-final.md / publication.md / owner-briefing.md; dropped facts: none)
external_guard: PASS (no ZAM property attributed to the filing; ZAM / Z-angle / Powerchip / VLSI 2026 detail / ~2029 / imec / IGZO all excluded; the calendar tease names no venue and attributes nothing to the filing; the foundry reading is labeled the essay's in BOTH deliverables; 1T1C never called capacitor-less)
subrules: 1 sequence PASS (2021 -> the year after, essay-consistent) / 2 arithmetic PASS (no date arithmetic used) / 3 anchors PASS (each post and each KR paragraph standalone-readable)
bold_selection: KR lead = 서사 훅 (essay §1 the-company-that-left irony, protected lead surface), bold beat ¶3 (fourth-door / 파운드리, publication §4 압축), insurance 1 clause (¶4 해석 경계, beat 뒤); EN P1 = same 서사 훅, bold beat P2 (fourth door + signature compression), insurance 1 clause (P2 scope label, after the beat); examination-process narration 0 per deliverable
posture: essay closing_posture measured; promo_posture D (both closings point at the article; KR close = 문서/해석 경계 + 날짜 티저, EN close = "a question of yield, not of architecture" signature + date tease); agreement PASS (no open-question close, no safe-harbor boilerplate, closing sentence is the article pointer not a hedge)
kr_long: 772자 / 400-800 (공백 포함, 줄바꿈 제외, [ARTICLE-LINK]=23자), 4 단락 (문장 3/5/3/2), 존댓말 설명체, 수사 의문형 1/1 (설명형, 단락 첫 문장, 즉시 응답; 클릭베이트 0), 느낌표 0, 이모지 0, 아티클 포인터로 종료
thread: 3 posts, message-unit (X Premium, no char cap), 439 / 775 / 552 chars ([ARTICLE-LINK]=23), one message per post (P1 서사 훅 / P2 핵심+해석 경계 / P3 한계+call+link), each post standalone-readable, link in P3
hygiene: em-dash 0, en-dash 0, bold 0, emoji 0/1, hashtags 0, banned terms 0 (literal + regex scan clean), semicolons 0
attachments: fig-01B.png (KR post + P1; cover source sheet, 5:2 feed crop applied at publish time per posting-checklist.md), fig-01F.png (P2, mechanism beat); alt lines below each block
suspected_essay_defects: none
=== Deliverables ===

## 1. Korean long-form promo post (X, 400-800자, 존댓말 설명체)

```text
인텔은 메모리에서 손을 뗀 회사입니다. 2021년에 NAND 사업을 SK하이닉스에 팔았고, 이듬해에는 Optane 라인도 정리했습니다. 지금 세계의 HBM은 SK하이닉스, 삼성, 마이크론 세 회사가 만들고, 인텔의 몫은 없습니다.

그런 인텔이 최근 DRAM 출원을 하나 냈습니다. 특이한 것은 셀을 만드는 위치입니다. 보통 DRAM은 다이 맨 아래 결정질 실리콘층에 트랜지스터를 새겨 만듭니다. 이 층을 전공정(front-end)이라고 부릅니다. 그런데 이 출원은 그 트랜지스터를 위쪽의 금속 배선층, 즉 후공정(back-end)에 얇은 막 형태로 올려 만듭니다. 청구항 1이 실제로 요구하는 것도 이 한 단어, "backend"입니다.

위치 하나 바꾼 것이 왜 중요할까요? 배선층은 낮은 온도에서 쌓는 층이라, 전용 DRAM 팹만 돌릴 수 있는 결정질 실리콘 전공정이 필요 없기 때문입니다. 로직과 패키징 라인을 이미 가진 파운드리라면, 원리상 HBM급 메모리를 세 공급사에서 사 오는 대신 자기 라인에서 만들 수 있게 됩니다. AI 가속기 메모리의 가장 좁은 병목에 네 번째 문이 생기는 셈입니다.

물론 출원 문서가 직접 말하는 것은 "backend"까지고, 파운드리 이야기는 거기서 읽어낸 해석입니다. 이 출원이 옮기기만 하고 없애지는 못한 부품이 하나 있다는 것(DRAM에서 가장 줄이기 어려운 그 부품입니다), 어디까지가 문서이고 어디부터가 해석인지, 그리고 이 방향의 성패를 확인할 수 있는 날짜가 언제인지는 아티클에 정리했습니다. [ARTICLE-LINK]
```

- 자수: 772 (공백 포함, 줄바꿈 제외, [ARTICLE-LINK]=23자)
- attach: publication-package/fig-01B.png (cover source sheet; crop to 5:2 at publish time, excluding the sideways USPTO header band, per posting-checklist.md)
- alt: "FIG. 1B: the claimed eight-high memory stack on its base die."

## 2. English thread (3 posts, message-unit; X Premium, no char cap)

```text
Intel walked away from memory. It sold its NAND business to SK hynix in 2021 and wound down Optane the year after. Three companies make the world's HBM today, and Intel is not one of them.

So it is strange to find a new DRAM filing under Intel's name, and stranger still where it builds the memory cell. Not carved into the crystalline silicon at the base of the die, where DRAM has always lived, but up in the chip's metal wiring layers.
```

- chars: 439 (message: the story; first sentence is the collapsed-preview hook)
- attach: publication-package/fig-01B.png (cover source sheet; 5:2 crop at publish time)
- alt: "FIG. 1B: the claimed eight-high memory stack on its base die."

```text
Claim 1 turns on a single word: backend.

In every DRAM made today, the cell's access transistor is etched into crystalline silicon at the bottom of the die, the front-end, and only dedicated DRAM fabs run that process. This filing builds the transistor as a thin film up in the back-end wiring instead, layers deposited at low temperature. That is territory a logic fab already owns.

Follow that one word and the implication is large: a foundry that already has logic and advanced packaging could, in principle, build HBM-class memory on its own line instead of buying it from one of three suppliers. The tightest bottleneck in AI hardware would gain a fourth door. To be precise, the claim says backend. It never says foundry. That leap is the essay's, not the document's.
```

- chars: 775 (message: the one word that matters, and the interpretation boundary)
- attach: publication-package/fig-01F.png (mechanism beat, the back-end cell)
- alt: "FIG. 1F: the back-end cell made literal. An exploded view shows the tiers labeled TRANSISTOR, the thin-film transistors that switch each cell."

```text
The honest part is what the filing keeps. The cell is still 1T1C: one transistor, one capacitor. And the capacitor is the hardest thing in DRAM to shrink. The back-end move relocates it. It does not remove it. A back-end capacitor at HBM density and yield is exactly what no one has shipped.

So whether this becomes a fourth path to HBM is now a question of yield, not of architecture. There is a date on the calendar that will start answering it. The full read, including where the document ends and the interpretation begins: [ARTICLE-LINK]
```

- chars: 552 ([ARTICLE-LINK]=23; message: what it keeps, and when we find out)
