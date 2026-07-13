<!--
  CANONICAL stage for this file: understand (patent-understand).
  Also copied to handoff/01-design/ for gate/design compat.
  Schema: _shared/references/owner-briefing-schema.md
-->

# Owner Briefing (발행자 브리핑)

- **특허 번호**: WO 2026/148096 A1 (국제출원 PCT/US2025/061797)
- **제목**: LADDER HOIST ASSEMBLY
- **상태**: 출원 (PCT 국제공개 2026-07-09; 실체 심사·등록 전, 국내단계 진입 여부 미확인)
- **출원일**: 2025-12-31 (국제출원일; 우선일 2025-01-03, US 63/741,689)
- **발명자**: Dylon Lemus, Jacob Pasternak, Brencis Pukinskis, Shiv Vivek Makim (출원인 Tesla, Inc.)

**한 줄 요약**: 표준 연장 사다리에 캐리지(carriage)·풀리(pulley)·기어박스(gearbox)를 얹고
표준 드릴 토크로 로프를 감아 캐리지를 오르내리게 하는 자재 호이스트 구조와 그 전환
키트를 청구한 Tesla 의 PCT 출원이다.

## ① 과거 기술의 과제/문제점

이 문서가 출발점으로 삼는 문제는 지붕 자재 인양의 두 병목이다. 기존 솔루션은 맞춤
장비(custom equipment)나 번거로운 설치에 의존해 설치 시간이 길고 복잡하다 `[0003]`.
그리고 설치가 끝난 뒤에도 자재 이동에 수작업이 개입해, 자재를 손상시킬 가능성이 커지고
부상이나 재산 피해로 이어질 수 있다 `[0003]`. 명세서는 이를 태양광(photovoltaic) 패널을
주택 지붕으로 올리는 장면을 대표 사례로 서술한다 `[0037]`.

**근거 (verbatim):**
- `[0003]`: "Existing solutions for moving materials toward or away from fixed structures (e.g., buildings) often rely on custom equipment or cumbersome setup, leading to extended setup times and increased complexity."
  (기존 솔루션은 맞춤 장비나 번거로운 설치에 의존해 설치 시간이 길어지고 복잡성이 커진다는 뜻)
- `[0003]`: "manual efforts are often involved for moving material once setup is completed, which not only increases the chance of damaging the material but may result in injuries or damage to property"
  (설치 후에도 수작업이 개입해 자재 손상 가능성이 커지고 부상·재산 피해가 생길 수 있다는 뜻)

## ② 기존 기술의 해결 방향과 그 한계

종래의 지붕 인양 어셈블리는 문제를 전용 하드웨어로 풀었다. 맞춤 사다리, 배터리, 모터를
갖춘 전용 리프트를 세우는 방향이다. 그 대가로 어셈블리가 복잡해지고 설치 비용이 높아졌다
`[0039]`. 전용 장비를 쓰지 않는 현장은 반대편 극단으로 갔다. 패널에 로프를 묶어 사람이
직접 당기는 수작업이다 `[0039]`. 문서는 이 관행이 자재 손상과 부상으로 이어질 수 있다고
적는다 `[0039]`. 즉 종래 기술은 "전용 장비의 비용·복잡성" 과 "수작업의 위험" 사이에서
어느 한쪽을 감수해 왔고, 이 문서는 흔한 장비만으로 그 사이를 메우는 것이 바람직하다고
문제를 설정한다 `[0003]`.

**근거 (verbatim):**
- `[0039]`: "existing assemblies for lifting materials to the roofs of buildings utilize custom ladders, batteries, and/or motors such that the assemblies can be complicated and costly to setup or install"
  (기존 인양 어셈블리는 맞춤 사다리·배터리·모터를 써서 복잡하고 설치 비용이 높다는 뜻)
- `[0039]`: "tying ropes around panels and manually pulling the ropes"
  (패널에 로프를 묶어 사람이 직접 당기는 기존 수작업 방식을 가리킴)

## ③ 이 특허의 독창적 해법 (핵심 청구항 중심)

독립항은 둘이다: 장치 청구항 1 과 키트 청구항 20. 출원 건이므로 locked 는 없고 모든 범위
서술은 sought-* (청구 중, 확정 아님) 이다.

**청구항 1 (sought-locked)** 은 네 요소의 결합을 청구한다. 사다리 제1 주면에 이동 가능하게
부착된 캐리지, 사다리 상단부에 부착된 풀리, 제1 주면 반대편 제2 주면에 부착된 기어박스,
그리고 풀리를 적어도 부분적으로 경유하는 로프가 기어박스와 캐리지를 연결하고 기어박스가
그 로프를 감고 풀어 캐리지를 이동시킨다는 한정이다 `[0005]`. 주의할 것은 청구항 1 이
드릴 구동, 웜 기어비(5:1/10:1/15:1) `[0019]`, 연장 사다리일 것 `[0012]`, 접이식 측면 롤러
`[0014]`, 원격 제어 `[0022]`, 트레이 `[0023]` 를 요구하지 않는다는 점이다. 이들은 전부
종속항 내지 명세서 선호(open)다.

**청구항 20 (sought-locked)** 은 베이스 섹션과 플라이 섹션을 가진 연장 사다리를 자재
운반용으로 전환하는 키트를 청구한다. 두 섹션의 레일을 미끄러지는 캐리지, 사다리가
지지하는 풀리, 핸드 드릴 어댑터(hand drill adapter)를 포함한 기어박스, 기어박스에서
풀리를 지나 캐리지로 라우팅되는 로프 또는 케이블, 그리고 어댑터 회전이 캐리지를
미끄러지게 한다는 한정이다 `[0024]`. 청구항 1 과 달리 여기서는 드릴 어댑터가 청구 요소다.

공개 텍스트의 청구항 번호는 OCR 로 훼손돼 있다(10번 문단에 "11." 이 내장, 번호 재시작,
16의 자기 인용, 19 부재). 독립항 경계(1, 20)는 영향이 없으나 종속 관계 일부는 추정이다
(open-questions 참조).

**근거 (verbatim):**
- `[0005]`: "a carriage movably attached to a first major side of a ladder, the carriage configured to carry the materials"
  (청구항 1 의 캐리지 요소: 사다리 제1 주면에 이동 가능하게 부착되고 자재를 운반한다)
- `[0005]`: "wherein the gearbox is configured to wind or unwind the rope to move the carriage along the first major side of the ladder for transporting the materials"
  (청구항 1 의 결합 한정: 기어박스가 로프를 감고 풀어 캐리지를 이동시킨다)
- `[0024]`: "wherein rotation of the hand drill adapter causes the carriage to slide along the rails of the base section and the rails of the fly section"
  (키트 청구항 20 의 한정: 핸드 드릴 어댑터의 회전이 캐리지를 두 섹션의 레일을 따라 미끄러지게 한다)

## ④ 기대 효과

명세서가 주장하는 효과로 한정한다. 표준 장비 기반이라 어셈블리를 바로 구할 수 있고 5분
내 설치될 수 있으며, 기존 솔루션은 30분 이상 걸릴 수 있다고 대비한다 `[0038]`. 두 수치
모두 "e.g." / "may" 가 붙은 예시적 서술이지 시험 데이터가 아니다 `[0038]`. 드릴 구동이라
운반 조작에 수작업이 거의 필요 없어 중량물 수작업 인양에 따르는 부상 위험을 줄인다고
주장하고 `[0038]`, 설치와 운용이 시간·비용 효율적이라고 주장한다 `[0041]`. 원격 제어
변형례(600)에서는 작업자가 사다리에서 떨어져 조작해 이동 하중 노출을 줄이고 시야를
유지하며 `[0060]`, 트레이의 슬롯(slot)이 전선관 같은 장척물을 기계적으로 구속해 오르내림
내내 하중 제어를 개선한다고 주장한다 `[0063]`.

**근거 (verbatim):**
- `[0038]`: "the ladder hoist assembly can be readily available and/or setup in much less time (e.g., within five minutes) compared with existing solutions that may require over half an hour to setup"
  (기존 솔루션이 30분 이상 걸릴 수 있는 것과 달리 5분 내 설치될 수 있다는 주장)
- `[0038]`: "little or no manual effort is required to operate the ladder hoist assembly for moving materials, which reduces risk of injuries associated with manually lifting heavy materials"
  (수작업이 거의 필요 없어 중량물 수작업 인양에 따른 부상 위험을 줄인다는 주장)
- `[0063]`: "by passing the item 842 through the slot 634, the item 842 can be mechanically captured so the item 842 cannot roll off, slide laterally, and/or pivot unexpectedly"
  (슬롯을 관통시키면 장척물이 기계적으로 구속되어 구르거나 미끄러지거나 회전하지 않는다는 주장)

## ⑤ 회사 프로모션 글/기술과의 연결

> Revision note — design 단계 2026-07-13: §⑤ 를 "없음 (Design 단계에서 갱신)" 에서 컨텍스트
> 리서치 결과로 갱신. 출처·등급은 `handoff/01-design/fact-check-log.md` / `search-log.md`.
> ①-④·⑥·⑦ 은 무변경.

**특허가 실제로 뒷받침하는 것** (특허 텍스트 앵커만):
- 표준 연장 사다리 + 표준 드릴 + 기성 부품으로 구성한 전환형 호이스트와 5분 내 설치
  주장 `[0038]`, `[0041]` (모두 "e.g."/"may" 수식의 명세서 주장).
- 대표 사용례가 주택 지붕으로의 태양광 패널 인양이라는 것 `[0037]`.

**회사 주장·외부 맥락** (특허가 뒷받침하지 않음; fact-check-log 등급 부기):
- Tesla 는 2026-01-30 신형 420W 패널 + 레일리스 마운트를 발표하며 설치 시간 30% 이상
  단축(보도 표현 "33% faster installs")을 내세웠다 — `tesla-420w-panel-install-time-2026-01`,
  tier-3 (Tesla 자체 X 게시물 존재로 tier-1 교차확인). 이 출원과 같은 방향(설치 시간 공략)의
  서사지만 corroboration 이며, 이 출원 내용이 그 제품·설치 작업에 실제 적용되는지는 확인
  불가 (⑥(b) 단정 불가 리스트와 동일 취지).
- 미국 주택 태양광 설치는 2025년 감소, 2026년 약 18% 추가 감소 전망이고, Tesla 는 2023년
  이후 설치 실적 공개를 중단하고 서드파티 설치사에 패널을 공급하는 방향으로 재편 중이라는
  보도 — `us-resi-solar-contraction-2026`, tier-3.
- 발명자 4인 중 2인은 LinkedIn 프로필에서 Tesla 기계 엔지니어로 자기 표명(한 명의 소속
  표기는 "Solar Tools" 팀) — `inventors-tesla-energy-engineers`, tier-5 (자기 표명, 미검증;
  에세이에는 헤지된 부기 이하로만 사용, "현장 설치 크루" 프레임 금지).
- 시판 기준선(이 특허의 `[0039]` "custom equipment" 서술이 가리키는 실물 시장): 전용 사다리
  호이스트 TranzSporter TP250 $3,500.99~$4,189.99 (4HP 가스 엔진, 전용 트랙 동봉) —
  `tranzsporter-tp250-price-specs`, tier-4; Safety Hoist SPH-250/500 $5,040/$5,710 (110V 전동,
  자사 "15분 이내 설치" 주장) — `safety-hoist-solar-price-setup`, tier-2. 이 가격은 기존
  제품의 가격이지 Tesla 키트의 가격이 아니다 (키트 가격 정보는 존재하지 않음).

## ⑥ 아는 것/모르는 것 경계 지도

**(a) 이 런의 증거가 확립한 것**
- WIPO 공개 텍스트(WO 2026/148096 A1) 전문과 도면 12장을 확인했다. 서지사항(출원인
  Tesla, Inc., 국제출원일 2025-12-31, 공개일 2026-07-09, 우선일 2025-01-03)은 공개공보
  표지 기준이다.
- 독립항이 장치 청구항 1 과 키트 청구항 20 둘이라는 것, 그리고 두 독립항의 요소 구성.
- 도면 중 FIGS. 1A/1B, 7A/7B, 8A-8C 가 실제 현장 사진이라는 것 (도면 자체로 확인).

**(b) 증거 밖에 있는 것 - 단정 불가 리스트**
- 심사 경과: PCT 국제공개 단계라 등록 여부, 국내단계 진입국, 청구범위의 최종 형태를 알 수
  없다. 국제조사보고서(ISR)의 인용문헌도 이 텍스트에 없다.
- 신규성·진보성 평가: 문서가 특정 선행문헌을 인용하지 않으므로 심사 기준선을 알 수 없다.
- "5분 설치" 등 수치의 실측 여부: 명세서 주장이며 시험 데이터가 아니다.
- Tesla 의 제품·설치 크루가 이 출원 그대로를 실시하는지 여부: 사진이 현장 촬영이라는
  사실이 상용화를 증명하지 않는다.
- 우선권 가출원(US 63/741,689)의 전문: 읽지 않았다.
- 공개공보 원본 PDF 의 정확한 청구항 번호: 이 런은 OCR 텍스트만 보았고, 번호 재구성
  (11=접이식 롤러, 19=트레이 등)은 추정이다.

**(c) 원문 자체가 열어둔 것**
- 로프 재질은 예시다 `[0046]`; 기어비도 선택지다 `[0019]`.
- 렁 브래킷의 스프링 로드 잠금은 "may include" 다 `[0054]`.
  - `[0054]`: "The bracket 232 may include a spring-loaded mechanism that locks around a rung of the ladder 150"
    (렁 브래킷이 스프링 로드 잠금을 포함할 수도 있다는 선택적 서술)
- 자재는 PV 패널이 대표 예시일 뿐 박스·프레임·물건 일반으로 열려 있고 `[0037]`, `[0044]`,
  건물·사다리·기어박스·패널의 종류에 한정되지 않는다는 유보가 명시돼 있다 `[0042]`.
- 원격 제어와 트레이 어셈블리는 변형례(600)의 특징으로, 기본 실시예(100)와 병렬로 열려
  있다 `[0058]`.

## ⑦ 자료 지도

반박이 오면 볼 곳:

| 반박 유형 | 참고 파일 |
|---|---|
| 가장 강한 반론 (steelman) | `handoff/01-design/thesis-spine.md` §Adversarial defense (Design 단계 후 생성) |
| 문장별 검증 | 최종 라운드 `handoff/03-edit/selfaudit-round-N-grounding.md` (N 은 런 종료 시 확정) |
| 외부 사실 | `handoff/01-design/fact-check-log.md` |
| 청구항 범위 | `handoff/01-design/invention-summary.md` §Claim scope map |
| 원문 | `essays/<essay-id>/patent.md` |
