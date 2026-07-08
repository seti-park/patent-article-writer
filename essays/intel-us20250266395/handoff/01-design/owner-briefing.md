# Owner Briefing (발행자 브리핑)

- **특허 번호**: US 2025/0266395 A1 (출원번호 18/582,203)
- **제목**: Multi-Die Bridge Assemblies and Methods for Three-Dimensional Packaging
- **상태**: 출원 (공개 공보, 2025-08-21 공개; 등록 전, 심사 계속 중 — Google Patents 기준 pending)
- **출원일**: 2024-02-20
- **발명자**: Jeremy D. Ecton 외 12인 (Minglu Liu, Mohamed R. Saber, Brandon C. Marin, Bohan Shan, Ravindranath V. Mahajan, Benjamin T. Duong, Gang Duan, Srinivas V. Pietambaram, Suddhasattwa Nad, Kristof Darmawikarta, Zhiguo Qian, Rahul Manepalli) / 출원인 Intel Corporation

**한 줄 요약**: 브리지(bridge) 다이를 기판보다 먼저 칩들에 접합해 하나의 멀티다이 조립체를 만들고, 기판을 붙이기 전에 그 조립체를 성능 시험한 뒤, 통과한 것만 기판 캐비티(cavity)에 앉혀 바닥에서 전력을 올려 받는 조립 순서를 청구한 인텔의 출원이다.

## ① 과거 기술의 과제/문제점

명세서 배경은 3D 패키징에서 범프 밀도(bump density), 전력 효율, 속도, 대역폭을 올리려는 업계의 압박을 출발점으로 삼는다 `[0001]`. 그러나 기존 다이-투-다이(D2D)·다이-투-웨이퍼(D2W) 방식은 제조 난이도와 비용이 문제라고 지적한다 `[0022]`. 특히 구리-구리 접합(copper-to-copper bonding) 기술의 복잡성과 높은 비용 `[0023]`, 그리고 브리지 부품 자체의 한계를 문제로 명시한다: 신호만 통과시키는 수동(passive) 브리지는 싸지만 요구되는 최대 전류(Imax)를 감당하지 못하고, TSV(through silicon via)로 전력을 통과시키는 능동(active) 브리지는 드릴링·정렬·캐비티 충전·솔더링 문제가 남는다 `[0024]`.

**근거 (verbatim):**
- `[0022]`: "However, many available D2D and D2 W methods and architectures face fabrication challenges and higher costs."
  (기존 D2D·D2W 방식 다수가 제조상의 난제와 더 높은 비용에 부딪힌다는 뜻)
- `[0024]`: "Passive bridge components are easier to fabricate and lower cost but cannot achieve the maximum current (Imax) that many applications require."
  (수동 브리지는 만들기 쉽고 싸지만 많은 응용이 요구하는 최대 전류를 내지 못한다는 뜻)
- `[0024]`: "Active bridge components often include through silicon vias (TSVs) to route power and ground between surfaces, and thereby improve Imax; however, technical challenges, such as drilling, alignment, cavity filling and soldering remain."
  (능동 브리지는 TSV로 전력·접지를 관통시켜 Imax를 개선하지만 드릴링·정렬·캐비티 충전·솔더링 난제가 남는다는 뜻)

## ② 기존 기술의 해결 방향과 그 한계

종래 방향은 두 갈래였다고 명세서는 정리한다. 하나는 브리지를 수동 부품으로 두고 신호 경로만 맡기는 것인데, 위 ①의 Imax 한계에 걸린다 `[0024]`. 다른 하나는 하이브리드 본딩(hybrid bonding, HBI)으로 미크론급 미세 피치를 여는 것인데, 명세서는 HBI가 10미크론 미만, 경우에 따라 1미크론 미만의 "small" 피치를 가능하게 한다고 쓰면서도 `[0025]`, 현실의 기판 다수는 여전히 솔더 접합(solder-attach) 부품이라는 점을 한계로 든다. 즉 미세 피치 세계(HBI)와 솔더 세계(기판)를 한 조립체 안에서 통합하는 문제가 남아 있었다 `[0025]`.

**근거 (verbatim):**
- `[0025]`: "many substrates remain solder-attach components, having solder-based interconnects for electrical communication with IC dies"
  (많은 기판이 여전히 솔더 기반 접속을 쓰는 솔더 접합 부품으로 남아 있다는 뜻)
- `[0025]`: "HBI advantageously enables "small" pitches (defined herein as a pitch less than 10 microns+/−10%, and in some cases, the pitch is less than 1 micron+/−10%)"
  (HBI가 10미크론 미만, 때로 1미크론 미만의 미세 피치를 가능하게 한다는 뜻)

## ③ 이 특허의 독창적 해법 (핵심 청구항 중심)

이 건은 출원이므로 확정된 권리범위(locked)는 없다. 아래는 모두 sought-* (청구 중, 확정 아님)이다. 핵심 독립항은 방법 청구항 19다: 캐리어(carrier) 위에 두 IC 다이를 조립하고, 몰드로 덮고, 캐리어를 떼어낸 뒤, 브리지를 다이들에 접합해 멀티다이 브리지 조립체를 만들고, 그 조립체를 성능 시험하고, 통과했을 때(when it passes) 기판을 붙이는 순서를 청구한다 (청구항 19 ≒ Example 21 `[0142]`). 종속항 20은 기판 캐비티에 브리지를 앉히는 단계를 청구한다 `[0144]`. 구조 쪽 독립항 1은 브리지와 두 다이의 절연막·금속 접점이 직접 접합(directly bonded)되는 구조, 즉 하이브리드 본딩 구조를 청구한다 `[0122]`. 종속항 2는 브리지 아랫면에서 윗면으로 통하는 전기 경로(관통 비아 구조)를 `[0123]`, 종속항 17은 20미크론-1.4밀리미터 두께의 유리층과 복수의 TGV(through-glass via)를 가진 기판을 청구한다 `[0138]`. 주의: 방법 청구항 19에는 하이브리드 본딩·TSV·유리·피치 수치가 요구사항으로 들어 있지 않다(명세서 선호 사항). 청구항이 요구하는 것은 조립 순서와 시험 단계다.

**근거 (verbatim):**
- `[0142]`: "testing the multi-die bridge assembly to determine whether it passes performance metrics; and attaching a substrate to the multi-die bridge assembly when the multi-die bridge assembly passes the performance metrics to thereby create a package assembly"
  (조립체가 성능 지표를 통과하는지 시험하고, 통과했을 때 기판을 붙여 패키지 조립체를 만든다는 뜻; 청구항 19와 동일 취지의 Example 21)
- `[0122]`: "wherein the first insulating material is directly bonded to the second insulating material and some first metal contacts are directly bonded to a respective second metal contact"
  (브리지와 다이의 절연재끼리, 금속 접점끼리 직접 접합된다는 뜻; 청구항 1과 동일 취지의 Example 1)
- `[0123]`: "further comprising at least one contact on the second surface that provides an electrical pathway to the first surface"
  (브리지 아랫면 접점이 윗면까지 전기 경로를 제공한다는 뜻; 청구항 2와 동일 취지)

## ④ 기대 효과

명세서가 스스로 주장하는 효과는 절제되어 있다. 브리지 관통 경로(TSV/TGV)로 캐비티 바닥에서 전력을 받으면 기판 배선층 수가 줄고 제품 수율이 개선될 수 있다고 쓴다 `[0035]`. HBI는 1-10미크론 피치의 다이-브리지 접속을 연다 `[0034]`. 시험 단계의 효과(불량 조립체가 기판을 소비하기 전에 걸러짐)는 수치 없이 흐름 순서로만 서술된다 `[0061]` `[0062]`. 전체적으로는 모놀리식 SoC에 상응하는 기능을 멀티다이 패키지로 제공할 수 있다고 주장한다 `[0059]`.

**근거 (verbatim):**
- `[0035]`: "The electrical pathways or routing indicated by optional cartoon arrow 123 reduces the number of substrate routing layers and can improve product yield."
  (브리지 관통 배선이 기판 배선층 수를 줄이고 제품 수율을 개선할 수 있다는 뜻)
- `[0034]`: "When the means for attachment 125 is HBI, the HBI pitch on the bridge components 102 is smaller still, in a range of 1 to 10 microns."
  (브리지 접합을 HBI로 하면 피치가 1-10미크론까지 작아진다는 뜻)
- `[0059]`: "The above embodiments may provide, in a multi-die package assembly, the functionality conventionally associated with a monolithic system on chip (SoC)."
  (이 실시예들이 멀티다이 패키지로 모놀리식 SoC에 상응하는 기능을 제공할 수 있다는 뜻)

## ⑤ 회사 프로모션 글/기술과의 연결

인텔의 EMIB-T 패키징이 뉴스에 올라 있는 시점이다. 두 칸을 가른다.

**특허가 실제로 뒷받침하는 것**
- 브리지에 관통 비아를 두고 기판 캐비티 바닥에서 전력을 올려 받는 아이디어 `[0035]`, 관통 경로 구조 청구 `[0123]`.
- 브리지를 다이에 먼저 접합하고, 기판 접합 전에 조립체를 성능 시험하는 조립 순서 `[0061]` `[0062]` `[0142]`.
- 유리 브리지 `[0033]`, 유리 프레임 `[0049]`, TGV를 가진 유리층 기판 `[0138]` 등 유리 계열 옵션.
- 이 문서에 "EMIB"라는 단어는 없다. "이것이 EMIB-T다"라고 특허가 말하지 않는다.

**회사 주장 (특허 밖, fact-check-log 라벨 부기)**
- EMIB-T: ECTC 2025에서 인텔이 공개한 TSV 브리지 기술로, 패키지 바닥에서 TSV 브리지 다이를 통해 전력을 공급해 기존 EMIB의 전압 강하(voltage droop) 문제를 푼다고 설명 (company-claimed / trade-press-reported; fact-check-log: emib-t-ectc-2025).
- EMIB-T의 팹 적용은 2026년으로 보도됨 (trade-press-reported; fact-check-log: emib-t-fab-rollout-2026).
- 2026년부터 120x120mm급, HBM 스택 최대 12개 패키지 로드맵 보도 (trade-press-reported; fact-check-log: emib-package-roadmap-120mm).
- 인텔 유리 기판 로드맵: 2023-09 공식 발표, 2020년대 후반 상용화 목표 (company-official; fact-check-log: intel-glass-substrate-2023).
- 발명자 중 Ravindranath (Ravi) Mahajan은 Intel Fellow로, EMIB의 원천 실리콘 브리지 특허 보유자로 소개된다 (bibliographic, IEEE EPS 약력; fact-check-log: mahajan-intel-fellow). 이 출원이 인텔 패키징 본류 조직에서 나왔다는 정황이며, 그 이상을 단정할 근거는 아니다.

## ⑥ 아는 것/모르는 것 경계 지도

**(a) 이 런의 증거가 확립한 것**
- 특허 전문(공개 공보 텍스트) 확인: 조립 순서, 시험 단계, 관통 비아, 유리 옵션의 청구·서술 위치.
- Google Patents 서지사항: 출원 2024-02-20, 공개 2025-08-21, 상태 pending, 출원인 Intel (registry-extract).
- EMIB-T·유리 기판 관련 외부 보도·발표의 존재와 내용 (fact-check-log에 출처별 기재).

**(b) 증거 밖에 있는 것 - 단정 불가 리스트**
- 이 출원이 EMIB-T이거나 그 후속 제품이라는 것. 특허는 EMIB를 언급하지 않는다.
- 심사 경과(거절·보정 여부). 공개 텍스트와 registry 스냅샷 이후의 일은 모른다.
- 인텔이 이 흐름을 실제 제품·공정에 쓰고 있거나 쓸 것이라는 것. 인텔은 옵션 공간 전반에 방어적으로 출원한다; 출원 1건은 로드맵 증거가 아니다.
- 시험 단계가 실제로 얼마의 수율·비용을 아끼는지. 명세서에 수치 없음. 에세이의 수율 산수는 외부 업계 자료(fact-check-log: kgd-yield-multiplier) 기반이다.

**(c) 원문 자체가 열어둔 것**
- 브리지 재료: 실리콘·유기·유리 또는 그 조합 `[0033]`.
- 접합 수단: 솔더, 하이브리드 본딩, TCB 마이크로볼, 도금 등 복수 옵션 `[0033]`, 캐비티 바닥 접합도 솔더 `[0056]`, 직접 접합 `[0057]`, 접착제까지 열려 있음.
- 캐비티 없는 반전(inverted) 조립 변형 `[0058]`, 유리 프레임 추가 변형 `[0049]`.
- "may" 서술: 관통 비아(화살표 123)는 선택 사항이고, 있으면 능동 브리지가 되는 경향이라고만 쓴다 `[0035]`.

## ⑦ 자료 지도

반박이 오면 볼 곳:

| 반박 유형 | 참고 파일 |
|---|---|
| 가장 강한 반론 (steelman) | `handoff/01-design/thesis-spine.md` §Adversarial defense |
| 문장별 검증 | 최종 라운드 `handoff/03-edit/selfaudit-round-N-grounding.md` |
| 외부 사실 | `handoff/01-design/fact-check-log.md` |
| 청구항 범위 | `handoff/01-design/invention-summary.md` §Claim scope map |
| 원문 | `essays/<essay-id>/patent.md` |

(N은 이 런의 마지막 self-audit 라운드 번호. 경로는 고정 계약 경로로, 아카이브 안에서는 essays/<essay-id>/ 기준으로 그대로 통한다.)
