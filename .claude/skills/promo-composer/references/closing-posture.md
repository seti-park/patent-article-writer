# Closing posture: the promo closing's 4 taxonomy (KR long post + EN thread final tweet)

Promo deliverable 의 closing (KR long post 마지막 단락, thread 의 final tweet) 4 가지 posture 중 하나를 선택한다. 모두 defensive
hedge (이 파이프라인의 over-hedge class: `gate_hedge` boilerplate, editorial 6G 가
essay 에서 걷어내는 격) 회피가 공통이다.

## The agreement rule (v2 addition)

`essay-final.md` frontmatter 의 `closing_posture` 를 읽고 promo 의 closing 이 그것과
합치해야 한다. 선택한 posture 는 pack frontmatter 의 `promo_posture` 와 Verification
Status header 에 기록한다.

- **Essay `closing_posture: firm`** → promo closing 도 call 또는 관찰 가능한 pointer 로
  끝난다. Open-question 격, "remains to be seen" 격 금지. Essay 가 loop 네 겹 (spine
  선언, composer closing directive, 6G, gate_hedge) 으로 지킨 firm 결론을 promo 가
  마지막 순간에 무르게 하는 것이 이 규칙이 막는 실패다.
- **Essay 가 firm 이 아닌 경우** → promo 는 essay 의 call 보다 세게 단정하지 않는다.
  단 v3 부터 상속은 one-way: no overreach 는 불변이지만 essay 본문의 hedge 를 promo 가 수입하지도 않는다 (bold-selection rule, promo-format.md) (scoring-rubric 의 verdict hard-gate 와 같은
  원칙, promo 표면에 적용).
- Posture D (essay closing 직접 carry-over) 는 정의상 항상 합치한다. 의심되면 D.

## 4 Posture taxonomy

| Posture | 사용 시점 | Confidence | 예시 |
|---------|---------|-----------|------|
| A. Minimal: essay echo | 단순 압축 / essay closing 간접 carry-over | 중 | *"X will answer when it chooses. What competitors filed is on record."* |
| B. Forward-looking: 다음 관찰 지점 | 분석가 voice / follow-up 시사 | 높음 | *"The next 46xx patent filing will signal whether Tesla holds the mechanism alone. The filings run on their own schedule. Tesla's lead will be measurable from there."* |
| C. IP weight: thesis 회수 | Standalone analysis / IP 함의 강조 | 가장 높음 | *"Tesla anchored the patent on its production line, then claimed the mechanism across the entire convergence. The first filing has weight."* |
| D. Essay 결론 직접 carry-over | Essay 와 voice 정합 가장 강 | 높음 | Essay 마지막 두 sentence 단어 단위 carry-over |

Default 권장:

- Thesis-driven IP analysis essay (verdict edition, firm) → B 또는 C. Essay 가 docket
  watch pointer 로 끝났다면 B 가 자연스럽고 사실상 D 와 겹친다.
- 단순 patent identification 압축 (news 격) → A 또는 D.

## 회피 패턴 (defensive hedge violations)

- *"only X can confirm"* / *"X 만 알 수 있다"*: passive hedge
- *"remains to be seen"* / *"지켜봐야 한다"*: disclaimer
- *"the future will tell"* / *"두고 봐야 한다"*: temporal hedge
- *"we cannot say"* / *"단정 짓기 어렵다"*: epistemic distancing
- *"a patent doesn't guarantee production / stock gains"* 류 generic 보일러플레이트:
  essay 의 gate_hedge 가 hard-fail 시키는 바로 그 문장, promo 에도 0 건

이 목록은 KR post 의 마지막 문장에도 그대로 적용된다 (아티클 포인터 앞 문장이 hedge 로
끝나지 않게).

## 교정 패턴 (forward-looking pointer)

- *"The next [event] will signal..."*
- *"X will say when [condition]"*
- *"[Specific next observable] is on record / publishes on its own schedule"*

Digest 의 pointer 는 essay 가 이미 지정한 관찰 지점 (docket, 다음 filing, 다음 office
action) 만 쓴다. 새 관찰 지점을 promo 가 발명하면 그것이 new claim 이다.

## 시그니처 요약

- 1-3 개의 단순 사실 sentences (현재 진행 / 향후 관찰 지점)
- Quote 회수 (essay closing 과 같은 quote) optional
- *"make visible" / "describe" / "signal" / "appear"* 같은 관찰 동사
- 🤔 는 optional: 팩 전체 emoji 예산 <=1, 슬롯은 여기뿐. Essay 가 🤔 없이 끝났으면
  promo 도 없이 끝나는 쪽이 정합적이다.

예시 (canon):

```
LFP dry electrode is not yet in production. Silicon-carbon anode chemistry is in
development. Eggleston named the milestone "just the beginning." The patents make
visible which beginning he meant.
```

## 실패 사례 (Tesla 944 promo, 2026-05)

초안 closing: *"Whether Texas cells carry this insert today, only Tesla can confirm"*.
Passive hedge, "safe-harbor 격, 너무 defensive" 로 catch. Posture B 로 교체:

*"The next 46xx patent filing will signal whether Tesla holds the floating-insert
mechanism alone. The filings run on their own schedule. Tesla's lead will be measurable
from there."*
