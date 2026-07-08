# Owner Briefing (발행자 브리핑)

- **특허 번호**: US 2026/0191095 A1 (출원번호 19/001921)
- **제목**: Ultra High Bandwidth Memory with Backend Transistors (백엔드 트랜지스터 기반 초고대역폭 메모리)
- **상태**: 출원 (공개 공보, 2026-07-02 공개; 등록 전, 심사 계속 중; Google Patents 기준 pending)
- **출원일**: 2024-12-26
- **발명자**: Abhishek Anil Sharma, Anand Iyer, Prashant Majhi, Nitin A. Deshpande / 출원인 Intel Corporation (Santa Clara, CA)

**한 줄 요약**: HBM 메모리 다이의 1T1C DRAM 셀을 종래의 결정질 실리콘 전공정(FEOL)이 아니라 후공정(BEOL)의 백엔드 트랜지스터로 만들고, 그 다이를 8단 이상으로 쌓아 TSV 거터와 UCIe 베이스 다이로 묶어 "HBM4의 풋프린트에 맞추는 것을 목표로" 청구한 인텔의 출원이다.

## ① 과거 기술의 과제/문제점

명세서 배경은 매우 짧다. HBM(high bandwidth memory)이 GPU, 데이터센터 AI ASIC, CPU, FPGA, 슈퍼컴퓨터에 두루 쓰이는 3D 적층 SDRAM 인터페이스라고만 소개한 뒤 `[0001]`, "이 분야에 개선이 필요하다"고 문제를 제기한다 `[0002]`. 그리고 이 발명이 출발점으로 삼는 종래 기술을 명시한다: 현재의 HBM은 단일 다이(single die)에 1T1C 메모리, 즉 트랜지스터 하나와 커패시터 하나로 이루어진 통상의 DRAM 셀을 쓴다 `[0019]`. 요컨대 "단일 다이 1T1C"가 이 특허가 벗어나려는 기준선이다.

**근거 (verbatim):**
- `[0002]`: "However, improvements are needed in the field of high bandwidth memory."
  (고대역폭 메모리 분야에 개선이 필요하다는 뜻)
- `[0019]`: "state-of-the-art approaches for high bandwidth memory (HBM) can include use of single die one-transistor one-capacitor (1T1C) memory"
  (최신 HBM 접근법이 단일 다이 1T1C 메모리를 쓸 수 있다는, 즉 현재 기준선이 단일 다이 1T1C라는 뜻)

## ② 기존 기술의 해결 방향과 그 한계

패키징 쪽에도 한계가 있다고 명세서는 정리한다. 메모리를 패키지 위에 올리는 MoP(memory on package) 방식은 최적의 DDR 성능과 최소 풋프린트를 위해 쓰여 왔지만, 메모리 패키지가 더해지면서 패키지의 Z 높이가 커지는 고질적 문제가 있다 `[0045]`. 이를 완화하려고 코어리스(coreless) 패키지 구조를 쓰기도 하지만, 명세서는 코어리스가 "대단히 비싼 해법일 수 있다"고 지적한다 `[0045]`. 즉 종래 방향은 단일 다이 1T1C 메모리 `[0019]` 와 그것을 얹는 패키징 기법이었고, 전자는 밀도, 후자는 높이와 비용에서 각각 막혔다.

**근거 (verbatim):**
- `[0045]`: "In some instances, the increase in the Z-height is mitigated by using a coreless package architecture."
  (Z 높이 증가를 코어리스 패키지 구조로 완화하기도 한다는 뜻)
- `[0045]`: "the use of a coreless architecture can be an extremely expensive solution"
  (코어리스 구조를 쓰는 것은 대단히 비싼 해법일 수 있다는 뜻)

## ③ 이 특허의 독창적 해법 (핵심 청구항 중심)

이 건은 출원이므로 확정된 권리범위(locked)는 없다. 아래는 모두 sought-* (청구 중, 확정 아님)이다. 핵심 독립항은 구조 청구항 1이다: 패키지 기판, 그 위의 베이스 다이(base die), 베이스 다이 위의 메모리 다이 스택을 두고, 스택의 각 메모리 다이가 "1T1C 백엔드(backend) DRAM"을 포함하도록 청구한다 (청구항 1 ≒ Example 1 `[0069]`). 독립항 6은 베이스 다이 없이 기판 위에 스택을 얹는 변형, 독립항 11은 그 메모리 구조를 보드에 얹은 컴퓨팅 장치를 청구한다. 명세서는 이 접근을 "1T1C 백엔드 DRAM을 담은 N개 메모리 다이의 스택 + TSV 거터 + 양면 HBI 접속"으로 서술한다 `[0020]`.

여기서 청구항이 실제로 요구하는(sought-locked) 핵심 단어는 "backend" 하나다. HBM 경쟁력을 만드는 나머지 요소는 청구항 1의 요구사항이 아니라 명세서 또는 종속항이다: "박막 트랜지스터(thin film transistor)"와 "back-end-of-line"이라는 표현은 명세서 서술이고 `[0031]` `[0027]`, 8단 적층은 종속항 2, BIST는 종속항 3, 리던던시는 종속항 4, 서브채널과 TSV 거터는 종속항 5, UCIe와 "HBM4 풋프린트에 맞춘다"는 목표는 명세서다 `[0034]`. 채널의 재료(예: 산화물, IGZO)는 특허 어디에도 나오지 않는다. 그리고 1T1C는 커패시터가 없는 셀이 아니다: 커패시터 하나가 그대로 있고, 그 셀을 백엔드로 옮겼을 뿐이다.

**근거 (verbatim):**
- `[0069]`: "Each memory die in the die stack includes one transistor one capacitor (1T1C) backend dynamic random access memory (DRAM)."
  (스택의 각 메모리 다이가 1T1C 백엔드 DRAM을 포함한다는 뜻; 청구항 1과 동일 취지의 Example 1, 청구항 본문은 includes 대신 comprises)
- `[0020]`: "an approach involves the use of a stack of N memory dies containing 1T1C backend DRAM, through silicon via (TSV) gutters and both-sided high bandwidth interconnect (HBI) connections"
  (1T1C 백엔드 DRAM을 담은 N개 다이 스택에 TSV 거터와 양면 HBI 접속을 쓰는 접근이라는 뜻)

## ④ 기대 효과

명세서가 스스로 주장하는 효과는 절제되어 있고, 대부분 측정치가 아니라 설계 목표로 서술된다. 비용, 수율, 리텐션, $/bit, HBM4 대비 대역폭 같은 수치는 특허 어디에도 없다. 정량 서술은 다이 용량과 적층 높이에 몰려 있다: 첫 번째 다이 옵션은 "back-end-of-line 트랜지스터에 기반한 약 1.5 GB 다이"가 될 수 있다고 하고 `[0027]`, XBM 다이는 "HBM4의 풋프린트에 맞추는 것을 목표로" 0.5-5 GB 용량으로 설계되며 `[0034]`, 적층은 8단 이상(8-high and beyond)이라고 한다 `[0023]`. 채널은 2 GHz, UCIe I/O는 32 GHz로 동작한다 `[0034]`.

**근거 (verbatim):**
- `[0027]`: "can be an approximately 1.5 GB die based on back-end-of-line transistors"
  (back-end-of-line 트랜지스터에 기반한 약 1.5 GB 다이가 될 수 있다는 뜻)
- `[0034]`: "With the goal of matching HBM4's footprint"
  (HBM4의 풋프린트에 맞추는 것을 목표로 한다는 뜻)

## ⑤ 회사 프로모션 글/기술과의 연결

인텔이 메모리로 되돌아오는 듯한 뉴스가 걸려 있는 시점이다. 인텔+소프트뱅크(자회사 SAIMEMORY)의 ZAM(Z-Angle Memory)/HB3DM "HBM 킬러"가 2026년 2월 공개됐고 VLSI 2026(6월)에 논문이 예정돼 있으며, 인텔 파운드리는 맞춤형 HBM 베이스 다이 로드맵을 발표한 바 있다. 두 칸을 명확히 가른다.

**특허가 실제로 뒷받침하는 것**
- DRAM 셀을 백엔드 트랜지스터로 만들어 다이를 8단 이상 쌓는다 `[0020]` `[0023]`, "HBM4 풋프린트에 맞춘다"는 목표 `[0034]`, UCIe 베이스 다이로 I/O를 모으고 리던던시로 사후 수리를 한다 `[0034]`.
- 이 문서에는 "EMIB", "ZAM", "Z-angle", "foundry(파운드리)", "logic fab(로직 팹)", "without a DRAM fab" 같은 단어가 없다. "이것이 ZAM이다" 또는 "이것이 파운드리 메모리다"라고 특허가 말하지 않는다. "메모리가 파운드리의 역량이 된다"는 해석은 특허 밖의 전략적 추론이다.

**회사 주장 / 외부 사실 (특허 밖, fact-check-log 라벨 부기)**
- ZAM/HB3DM: 9층(로직 1 + DRAM 8), 하이브리드 본딩, 층당 약 13,700 TSV, 약 171 mm² 다이, 약 10 GB 모듈, 모듈당 약 5.3 TB/s(HBM4 스택당 약 2 TB/s의 두 배 이상), 용량 2-3배, 전력 절반 (trade-press-reported; fact-check-log: zam-hb3dm-specs).
- ZAM에서 DRAM 제조는 인텔이 아니라 파워칩(Powerchip)이 맡는다고 보도됨 (trade-press-reported; zam-powerchip-fab). 프로토타입 2027 회계연도, 상용화 약 2029 (trade-press-reported; zam-timeline).
- 인텔은 메모리 사업에서 물러났다: NAND를 SK하이닉스(Solidigm)에 매각(2021년 12월 1차 완료), 옵테인(Optane)은 2022년 정리하며 5.59억 달러 재고 상각 (trade-press-reported; intel-exited-memory).
- HBM 공급은 SK하이닉스 약 60% 집중, DRAM은 삼성/SK하이닉스/마이크론 3사 과점 (analyst-estimate; hbm-supply-concentration, dram-three-player).
- 기존 3사도 이미 3D DRAM 로드맵을 간다: SK하이닉스 약 2030년, 삼성 VCT 기반, 마이크론 연구 지속 (trade-press-reported; incumbent-3d-dram). imec은 커패시터 없는 2T0C IGZO BEOL DRAM을 시연했으나 아직 연구 단계다 (bibliographic; imec-2t0c-igzo).

## ⑥ 아는 것/모르는 것 경계 지도

**(a) 이 런의 증거가 확립한 것**
- 특허 전문(공개 공보 텍스트) 확인: 1T1C 백엔드 DRAM, 8단 이상 스택, TSV 거터, UCIe 베이스 다이, MoP/반전 오버행 패키징의 청구·서술 위치.
- 서지사항: 출원 2024-12-26, 공개 2026-07-02, 상태 pending, 출원인 Intel, 발명자 4인 (registry-extract).
- ZAM/HB3DM, HBM/DRAM 점유율, 인텔의 메모리 철수, 경쟁사 3D DRAM 로드맵, imec 연구의 존재와 내용 (fact-check-log에 출처별 기재).

**(b) 증거 밖에 있는 것 - 단정 불가 리스트**
- 이 출원이 ZAM/HB3DM이거나 그 후속이라는 것. 방향은 같으나(초고층 커스텀 3D DRAM으로 HBM4를 넘김; 베이스 다이 + 고속 I/O) 인터커넥트가 다르다(이 특허는 수직 TSV 거터 + UCIe, 공개된 ZAM은 대각 Z-angle + 하이브리드 본딩). 같은 계열의 사촌 정도로만 본다.
- 심사 경과(거절·보정 여부), registry 스냅샷 이후의 일.
- 인텔이 이 구조를 실제 제품·공정에 쓰거나 쓸 것이라는 것. 출원 1건은 로드맵이 아니다.
- 로직+패키징 흐름이 실제로 HBM급 밀도·수율로 백엔드 DRAM을 만들 수 있는지. 특허에 비용·수율·리텐션·$/bit 수치가 없다. 채널 재료도 명시가 없다.

**(c) 원문 자체가 열어둔 것**
- 베이스 다이는 생략 가능하다 (독립항 6; 베이스 다이 없는 다이 옵션 `[0029]`).
- 적층은 8단 "이상"이며 16단까지 언급된다 `[0023]` `[0034]`; 적층은 웨이퍼-투-웨이퍼 또는 다이-투-다이로 가능하다 `[0023]`.
- MoP, 반전 오버행 등 여러 패키징 변형이 "may" 표현으로 열려 있다 `[0039]` `[0053]`.

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
