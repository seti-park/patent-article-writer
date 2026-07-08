---
essay_id: etched-0378175-memory-in-writing-r2
essay_source: essays/etched-us20240378175-r2/essay-final.md
closing_posture: firm
promo_posture: D
promo_version: 2
owner_briefing: read
---

# Promo pack: etched-us20240378175-r2

=== Verification Status (promo-composer v3 contract; copy composed in the main session by the session's strongest model per the 2026-07-05 owner decision) ===
sources: essay-final.md (draft_version 6, closing_posture firm) + publication-package/publication.md + owner-briefing.md (read; technical vocabulary only, stance sentences not reused)
fact_trace: PASS (every factual phrase mapped to a sentence in the three sources; dropped facts: none)
subrules: 1 sequence PASS (filing May 2023 before pitch late June 2026, relationship explicit in essay ¶1) / 2 arithmetic PASS (the essay's own "three years" span carried verbatim, no self-computed intervals) / 3 anchors PASS (per-deliverable referent check; venue is "stealth-exit thread" throughout; founder phrasing kept non-exhaustive: "공동창업자 ... 가 발명자로", "co-founders" without a count)
bold_selection: KR ¶1-2 lead = essay lead beat + signature line 2 KR 압축, insurance 1 clause (마지막 ¶, 포인터 결합형, 절차 서사 0) / T1 = signature-line-2-adjacent claim-language beat, insurance 1 clause (T4, call 뒤); process narration 0 in both deliverables (RCE/최종거절/담보 언급 0)
kr_long: 626자/400-800 (공백 포함, [ARTICLE-LINK]=23자), 4 단락, 아티클 포인터 있음, 의문형 후킹 0, 느낌표 0
thread: 4 tweets, 253/265/268/216 chars/280 (link slot = 23, in tweet 4), each tweet standalone-checked (company named in every tweet)
hygiene: em-dash 0, bold 0, emoji 0/1, hashtags 0, exclamation 0, banned terms 0 (banned_terms.txt literals + regexes, self-run)
attachments: cover-5x2.png (KR post, tweet 1) + fig-05.png (tweet 2 mechanism sheet, aspect 0.99), alt text verbatim from posting-checklist.md, paths verified present
suspected_essay_defects: none
=== Deliverables ===

## 1. Korean long-form promo post (X, 400-800자)

```text
AI 가속기에서 연산 유닛과 메모리 사이에는 통례로 스위치가 들어갑니다. Etched의 첫 특허 출원은 그 스위치를 지우겠다는 문서입니다. 2023년 5월 10일 출원된 US 2024/0378175 A1은 메모리 채널을 스위칭 요소 없이(without any switching element) 거대한 멀티칩 연산 어레이의 열에 직결하는 구조를 청구하고 있고, 공동창업자 Gavin Uberti와 Christopher Zhu가 발명자로 이름을 올렸습니다.

3년 뒤 스텔스 종료 스레드에서 Etched가 내세운 메모리 철학 "the best layer is no layer"는 그러니까 마케팅이 아니라, 2023년 5월자 청구항 언어입니다.

구조는 그림 한 장으로 요약됩니다. HBM의 채널들은 서로 통신할 수 없어서 업계는 메모리와 연산 사이에 스위치나 크로스바를 끼워 왔습니다. 이 출원은 가중치가 움직이지 않는 워크로드에서 각 채널을 어레이의 자기 열에 하드와이어링해 그 층 자체를 없앱니다. 명세서가 적은 이점은 공간과 전력 절약입니다.

이 아이디어가 회사의 피치보다 3년 앞서 어떻게 문서로 존재하는지, 그리고 특허청 문턱에서 지금 어디에 서 있는지까지 아티클에 정리했습니다. [ARTICLE-LINK]
```

- 자수: 626 (공백 포함, [ARTICLE-LINK]=23자), 4 단락
- bold lead: ¶1 기술 훅(스위치 삭제) + ¶2 signature line 2 압축 ("The no-layer pitch is not marketing retrofitted onto hardware. It is claim language, dated May 2023.")
- insurance: 1 clause ("특허청 문턱에서 지금 어디에 서 있는지까지"), 마지막 ¶, 아티클 포인터 결합형; 절차 서사(최종거절/RCE/담보) 0, "다만+유보" 마무리 0
- 표현 출처: 기술 어휘는 owner-briefing ②/③ ("스위칭 요소 없이", "채널", "크로스바", "하드와이어링", "공간·전력 절약") 재사용; stance/hedge 문장 재사용 없음; 날짜/번호/이름은 essay ¶1 원문 일치
- attach: publication-package/cover-5x2.png
- alt: "Patent drawing: two memory chips wired straight down into a processor chip, four independent channels, no switch between them."

## 2. English thread (4 tweets)

Sketch level: "1/" numbering is the owner's call at post time; each tweet reads standalone.

Tweet 1 (bold hook, claim-language beat):

```text
Etched's memory pitch is "the best layer is no layer." The company's very first patent filing, dated 10 May 2023, is that idea in claim language: memory channels hardwired straight into the columns of a giant multi-chip math array, no switch in between.
```

- chars: 253/280
- source: essay ¶1 ("claims memory channels wired straight into the columns of a giant multi-chip math array, no switch in between") + signature line 2's dated-claim-language beat; no insurance facts
- attach: publication-package/cover-5x2.png
- alt: "Patent drawing: two memory chips wired straight down into a processor chip, four independent channels, no switch between them."

Tweet 2 (mechanism beat):

```text
HBM channels cannot communicate with each other, so accelerators typically put a switch between memory and compute. Etched's claim 39 deletes it for weights that never move. Stated payoff: saved space and power. Stated trade: each column reads only its own channel.
```

- chars: 265/280
- source: essay §3 ("the different channels 510 cannot communicate with each other" carry-over; "That switch is the layer this filing exists to delete"; payoff/trade sentences)
- attach: publication-package/fig-05.png (mechanism sheet swap per figure-attachment-policy.md: the full FIG. 5 sheet, aspect 0.99, shows the whole channel-to-column path the 5:2 cover band crops)
- alt: "Patent drawing: two memory chips wired straight down into a processor chip, four independent channels, no switch between them." (cover alt reused; posting-checklist.md carries no separate fig-05 alt, and the sheet depicts the same drawing)

Tweet 3 (receipts beat):

```text
The pitch arrived in late June 2026, in Etched's stealth-exit thread. The written version is three years older, signed by co-founders Gavin Uberti and Christopher Zhu. The no-layer pitch is not marketing retrofitted onto hardware. It is claim language, dated May 2023.
```

- chars: 268/280
- source: essay ¶1 (venue + "The written version is three years older", signature line 1's first clause) + signature line 2 verbatim (both sentences)

Tweet 4 (verdict + link):

```text
What Etched holds today is a dated, signed statement of the memory idea it pitches; whether it becomes property is the patent office's call. The full story, from FIG. 5 to the docket to watch: [ARTICLE-LINK]
```

- chars: 216/280 ([ARTICLE-LINK] = 23)
- verdict: call-first (essay §6 "Etched holds a dated, signed statement of the memory idea it pitches"); the ONE status clause rides after the call ("whether it becomes property is the patent office's call" per essay §5/§6: "The patent office decides", "until the patent office says yes"); watch pointer is the essay's own docket pointer
