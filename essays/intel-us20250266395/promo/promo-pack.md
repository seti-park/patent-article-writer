---
essay_id: intel-us20250266395
essay_source: essays/intel-us20250266395/essay-final.md
closing_posture: firm
promo_posture: D
promo_version: 1
owner_briefing: read
---

# Promo pack: intel-us20250266395

=== Verification Status (promo-composer, promo-pack) ===
sources: essay-final.md (draft_version 5) + publication.md + owner-briefing.md read; README.md ABSENT, posting-checklist.md ABSENT (hooks harvested from title + thesis-trace signature lines + lead + closing call; alt text built from essay verbatim captions)
fact_trace: PASS (every factual phrase mapped to a source sentence; wanted-but-unsourced facts dropped: none; nothing fetched; EMIB-T carried only as external news context, never as patent text)
subrules: 1 sequence PASS / 2 arithmetic PASS / 3 anchors PASS
bold_selection: KR lead = title claim ("...Comes After EMIB-T") plus signature line 1, compressed; insurance 1 clause (pending, no granted claim; paragraph 4). T1 = same title claim plus signature line 1, compressed; insurance 0 in the hook. Thread insurance 1 clause total (T5, after the call). Process narration 0 in both.
kr_long: 777자/400-800, 4 단락, 아티클 포인터 있음, 의문형 0, 느낌표 0, 이모지 0
thread: 5 tweets, 224/218/271/211/263 chars/280, link slot in T5
posture: essay firm to promo D (thread verdict carries signature line 3 verbatim; KR close lands signature line 2 plus article pointer); no open-question close
hygiene: em-dash 0, bold 0, emoji 0/1, hashtags 0, banned terms 0 (Tier-1 literals plus regexes clean; Tier-2 tells checked)
attachments: cover-5x2.png ABSENT in archive, so fig-11.png (essay lead figure, the flowchart) on KR post and T1, fig-01.png on T2; alt verbatim from essay captions
suspected_essay_defects: none
=== Deliverables ===

## 1. Korean long-form promo post (X, 400-800자)

```text
인텔은 지금 뉴스에 오른 EMIB-T 패키징 다음에 오는 조립 흐름을 이미 파일에 올려뒀습니다. EMIB-T가 학회 무대에 이름을 올리기 열다섯 달 전의 출원입니다. 뉴스 속 브리지는 전력 비아를 얻고, 이 출원 속 브리지는 보드에서 칩 쪽으로 넘어갑니다.

지금 인텔이 파는 방식은 작은 브리지 다이를 보드에 묻고 칩을 그 위에 얹습니다. 이 출원의 방법은 브리지를 칩에 먼저 접합해 멀티다이 조립체로 만들고, 보드가 끼어들기 전에 클러스터 전체를 시험합니다. 청구항 표현 그대로 "testing the multi-die bridge assembly to determine whether it passes performance metrics", 통과했을 때에만 기판을 붙이는 순서입니다. 2024년 2월 20일 출원, 2025년 8월 공개된 US 2025/0266395 A1입니다.

시험을 통과한 조립체만 기판을 소비합니다. 다이 하나가 불량이면 완성된 패키지를 통째로 버릴 수 있으니, 기판을 대기 전에 클러스터를 걸러내는 순서입니다 (수율 산수 자체는 특허가 아니라 업계 자료입니다). 발명자 13인 중에는 EMIB의 원천 실리콘 브리지 특허를 낸 인텔 펠로우 Ravindranath Mahajan이 있고, 이 출원은 인텔 패키징 본류 조직에서 나왔습니다.

등록된 특허가 아니라 공개된 출원이고, 아직 인정된 청구항은 없습니다. 이 출원이 뉴스의 그 흐름 다음을 어디까지 박아뒀는지, 특허청 문턱에서 지금 어디 서 있는지까지 아티클에 정리했습니다. [ARTICLE-LINK]
```

- 자수: 777 (공백 포함, 줄바꿈 제외, [ARTICLE-LINK]=23자)
- attach: publication-package/fig-11.png
- alt: "FIG. 11: the filed method, end to end. The bridge is attached to the dies to form a multi-die assembly, the assembly goes through performance testing, and only an assembly that passes is attached to a target substrate."

## 2. English thread (3-5 tweets)

```text
The technology in the news is EMIB-T, the bridge die getting power vias. Fifteen months before that hit a conference stage, Intel had already filed the packaging flow that comes next. The filing is the bridge changing sides.
```

- chars: 224/280
- attach: publication-package/fig-11.png
- alt: "FIG. 11: the filed method, end to end. The bridge is attached to the dies to form a multi-die assembly, the assembly goes through performance testing, and only an assembly that passes is attached to a target substrate."

```text
In the flow Intel ships today, the bridge die is buried in the board and the chips land on top. The filed method bonds the bridge to the chips first, then tests the whole cluster before a board ever enters the picture.
```

- chars: 218/280
- attach: publication-package/fig-01.png
- alt: "FIG. 1: the multi-die bridge assembly in cross-section."

```text
The method claim locks an order of operations. In its own words, "testing the multi-die bridge assembly to determine whether it passes performance metrics," then a substrate only when it passes. Only an assembly that has already passed its test gets to spend a substrate.
```

- chars: 271/280

```text
Among the thirteen inventors on the filing is Ravindranath Mahajan, the Intel Fellow whose original silicon-bridge patents became the foundation of EMIB. This came out of Intel's mainline packaging organization.
```

- chars: 211/280

```text
The claim that matters is not a material and not a pitch number. It is an order of operations. Bond first, test before the board exists, power through the floor. Still a pending application, no granted claim yet. The article prices it out. [ARTICLE-LINK]
```

- chars: 263/280 ([ARTICLE-LINK]=23)
