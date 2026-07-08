# Owner Briefing (발행자 브리핑)

- **특허 번호**: US 2024/0378175 A1 (출원번호 US 18/195,769)
- **제목**: Multi-Chip Systolic Arrays (멀티칩 시스톨릭 어레이)
- **상태**: 출원 공개 건 (공개번호 US 2024/0378175 A1; 심사 상태: 2025-10 최종거절(final rejection) 후 2026-04 계속심사청구(RCE), 2026-05 기준 3차 non-final 거절이유통지 발행 중; 등록 전, 청구 범위 확정 아님)
- **출원일**: 2023-05-10
- **발명자**: Gavin Uberti, Christopher Zhu (두 발명자 모두 Etched 공동창업자; 출원인 Etched.ai, Inc.)

**한 줄 요약**: 여러 칩의 시스톨릭 어레이(systolic array)를 하나의 큰 결합 어레이로 묶고 메모리 채널을 스위칭 요소 없이 어레이 열에 직결하는 구조까지 청구한 Etched의 최초 출원으로, 최종거절 후 RCE로 심사가 계속 중이라 모든 청구 범위는 청구 중일 뿐 확정이 아니다.

## ① 과거 기술의 과제/문제점

명세서 background는 두 상한을 지목한다. AI 응용(트랜스포머(transformer) 모델)에서는 행렬 곱셈이 하드웨어 연산을 지배하는데 `[0003]`, 시스톨릭 어레이가 이를 효율적으로 처리해도 달성 FLOPs는 어레이 크기에 좌우되고, 크기는 현재 IC 설계에서 제한된다 `[0003]`. 또 칩 하나가 파라미터·중간 계산값용 수백 GB 메모리와 인터페이스하기는 무리라고 적는다 `[0018]`.

**근거 (verbatim):**
- `[0003]`: "However, the number of floating-point operations per second (FLOPs) that can be achieved is often dependent on the size of the systolic array, which is limited in current IC design."
  (달성 가능한 초당 부동소수점 연산량은 어레이 크기에 좌우되는데, 그 크기가 현행 IC 설계에서 제한된다는 뜻)
- `[0018]`: "One of which, notably, is that it is unreasonable to expect a single chip to interface with 100s of GB of memory used to store parameters and intermediate computation values."
  (칩 하나가 파라미터와 중간 계산값 저장용 수백 GB 메모리와 인터페이스하기를 기대하는 것은 무리라는 뜻)

## ② 기존 기술의 해결 방향과 그 한계

업계는 시스톨릭 어레이를 이미 채택했지만 단일 칩 어레이 크기가 막혀, 문서 기준 대부분의 칩은 커야 128×128 부동소수점 어레이다 `[0018]`. 메모리 쪽 관행도 한계다. HBM(고대역폭 메모리)의 채널들은 서로 통신할 수 없어서, 장치가 전체 메모리에 접근하려면 스위치나 크로스바(crossbar) 같은 스위칭 요소를 끼우는 것이 통례다 `[0043]`. 명세서 본문은 특정 선행문헌을 거명하지 않고 이 현행 관행을 기준선으로 삼는다.

**근거 (verbatim):**
- `[0018]`: "Currently, most chips have, at most, floating point systolic arrays with a size of 128×128."
  (현재 대부분의 칩은 커야 128×128 크기의 부동소수점 시스톨릭 어레이를 갖는다는 뜻)
- `[0043]`: "a switch (or some kind of switching element such as a crossbar) is typically used so that the device can access the entire memory of the HBM"
  (장치가 HBM 전체 메모리에 접근하도록 통상 스위치, 예컨대 크로스바 같은 스위칭 요소를 쓴다는 뜻)

## ③ 이 특허의 독창적 해법 (핵심 청구항 중심)

출원 건이라 확정(locked) 범위는 없다. 아래는 전부 청구 중(sought), 확정 아님. 청구항 1-42항 중 독립항은 1, 15, 26, 39항.

- **1항 (청구 중)**: 패키지. 복수의 IC 각각에 DPU(데이터 처리 유닛)들의 로컬 시스톨릭 어레이, 그리고 각 로컬 어레이를 적어도 하나의 다른 로컬 어레이와 이어 더 큰 결합 어레이를 만드는 칩투칩 연결(chip-to-chip connections). 청구항 본문의 요구는 여기까지다. 격자 배치는 26항의 추가이고, 인터포저(interposer)/스택은 종속항 9/10과 명세서 선호 `[0031]`, UCIe는 예시 `[0030]`, 메모리 칩 존재도 요건이 아니다 `[0037]`.
- **15항 (청구 중)**: AI 가속기. 결합 어레이에 더해, AI 모델 가중치를 저장하는 복수의 메모리 칩이 상단 행 IC들에 결합된다.
- **26항 (청구 중)**: 격자형(grid-like) 배치의 복수 IC. 26항 자체는 칩투칩 연결을 구성요소로 명시하지 않는다. 연결 방식은 종속항 27-29의 추가다.
- **39항 (청구 중)**: 가장 구조 특정적인 독립항. IC 하나의 시스톨릭 어레이와 별도 메모리 디바이스를 두고, 각 채널을 스위칭 요소 없이(without any switching element) 어레이의 하나 이상의 열에 하드와이어링한다. 멀티칩을 요구하지 않는다. 무스위치 메모리 직결의 단독 청구다.

같은 무스위치 하드와이어링은 종속항 7/19/32(청구 중)에도 있다. 종속항 11-13(청구 중)은 로컬 어레이와 분리된 보조 회로(auxiliary circuitry)와 전용 로컬 메모리(셀프어텐션(self-attention)용)를 더하고, 13항은 로컬 어레이가 그 메모리와 통신하지 않는다는 부정 한정이다. "about X"형 점 한정(pinned)은 어느 청구항에도 없다. 상수 가중치 `[0035]`, 프리셋 루프 `[0027]`, FIG. 7 파이프라이닝은 명세서 서술일 뿐 청구항에 없으므로 청구 요건처럼 쓰면 안 된다.

**근거 (verbatim):**
- `[0013]`: "chip-to-chip connections configured to connect the local systolic array in each of the plurality of ICs to at least one other local systolic array in another one of the plurality of ICs to form a larger, combined systolic array"
  (각 IC의 로컬 어레이를 다른 IC의 로컬 어레이와 이어 더 큰 결합 어레이를 만드는 칩투칩 연결, 1항의 명세서 쌍둥이 문장)
- `[0016]`: "a separate memory device comprising a plurality of channels where each of the plurality of channels is hardwired to respective one or more columns in the systolic array without any switching element"
  (별도 메모리 디바이스의 각 채널이 스위칭 요소 없이 어레이의 하나 이상의 열에 하드와이어링된다는 뜻, 39항의 명세서 쌍둥이 문장)

## ④ 기대 효과

명세서가 주장하는 효과는 세 갈래다. 규모: 100×100 칩 4개로 100×400 또는 400×100 결합 어레이가 되고 `[0038]`, 호스트에게는 하나의 큰 어레이로 보인다 `[0028]`. 메모리 경제성: IC 행을 더하면 상단 메모리 칩을 늘리지 않고도 연산력이 는다 `[0039]`. 상수 가중치 워크로드에서는 스위칭 요소를 없애 공간과 전력을 아낀다 `[0045]`. 활용률: 파이프라이닝으로 레이어 정규화 스톨을 감안해도 98% 이상이라 한다 `[0057]`. 단 IC당 1 TB/s 초과 공급 `[0040]`, FIG. 7 파이프라이닝, 98% 수치는 청구항에 없는 명세서 전용 서술이다.

**근거 (verbatim):**
- `[0039]`: "Advantageously, adding more rows of ICs 215 increases the compute power of the systolic array 350, without having to add more memory chips 305 at the top to feed in data in the vertical direction, since data fed from the memory chips 305 is reused across the rows within the combined systolic array 350."
  (IC 행을 더하면 상단 메모리 칩을 더하지 않고도 연산력이 늘어난다는 뜻, 공급된 데이터가 행들에서 재사용되기 때문)
- `[0045]`: "This avoids having to add a switching element between the local systolic array 220and the memory chips 505, which can save space and power."
  (어레이와 메모리 칩 사이 스위칭 요소가 불필요해져 공간과 전력을 아낀다는 뜻; "220and" 붙어 쓰기는 원문 자체의 표기)
- `[0057]`: "the stalled time may be small relative to the computation time and still result in a 98% or greater utilization of the systolic array"
  (스톨 시간이 계산 시간 대비 작아 어레이 활용률이 98% 이상일 수 있다는 뜻)

## ⑤ 회사 프로모션 글/기술과의 연결

연결 맥락은 Etched의 2026년 6월 말 스텔스 종료(stealth-exit) 스레드와 그 보도다(TechCrunch 2026-06-30). 두 축은 LVI(회사 소개: 절반 전압 연산)와 CSM(Cluster Scale Memory, 무계층 메모리 철학)이다.

**특허가 실제로 뒷받침하는 것**
- CSM 축의 메모리-어레이 직결 부분은 이 출원의 청구 내용과 겹친다: 무스위치 채널-열 하드와이어링 `[0016]`, 상수 가중치 전제 `[0044]`, 스위치/크로스바 관행과의 대비 `[0043]`, 공간·전력 절약 `[0045]`. 단 한도는 청구 중 지위: 이 철학이 2023-05-10 출원의 청구항 언어로 존재한다는 사실까지만 지지된다.
- 여러 칩을 하나의 큰 어레이로 묶는 서사도 본문에 있다: 결합 어레이 `[0019]`, 호스트에게 하나로 보임 `[0028]`, 동시 계산 분할 `[0024]`.

**회사 주장**
- "$1B+ 계약", "$800m 조달", 2026년 여름 첫 랙 출하, LVI/CSM 성능 서사: 회사 발표다 (company-claimed). "회사에 따르면" 프레임 필수.
- LVI 계열 내용(전압, VRM, 콜드 플레이트)은 이 출원에 없다 (full-text-verified). LVI가 특허로 뒷받침되는지는 이 문서로 판단 불가.
- 제품 Sohu가 이 아키텍처를 쓴다는 해설은 제3자 독해다 (third-party-read). 실시 확인이 아니다.
- TriplePoint Capital 담보권 2건: 효력 2024-04-19 (reel/frame 067204/0877, registry-extract), 효력 2025-07-18 (reel/frame 071792/0869, registry-verified). 둘 다 포트폴리오 포괄 담보라 이 출원 개별 중요성의 증거가 아니다. 담보 사실은 심사 기록(최종거절 후 RCE, 심사 계속 중)과 반드시 함께 쓴다.
- 등록건 US 12,361,091 B1("wiring half")의 등록 기록에 메모리 절반이 없다는 판단은 선행 발행 분석이다 (internal-prior-analysis).

## ⑥ 아는 것/모르는 것 경계 지도

**(a) 이 런의 증거가 확립한 것**
- 이 출원의 전문(단락 `[0001]`-`[0066]`, 청구항 1-42) 확인. 브리핑의 verbatim 인용은 전부 원문 대조했다.
- LVI 계열 내용의 부재는 전문 검증이다 (full-text-verified).
- Google Patents 대조: 서지(출원 2023-05-10, 공개 2024-11-14, 상태 pending), TriplePoint 담보 2건 기록, 심사관 인용 문헌 8건(Intel·IBM·Rambus·ETRI 포함) (registry-extract; 2차 담보 reel/frame은 registry-verified).
- 패밀리는 US 단독, PCT·계속출원 없음 (bibliographic).

**(b) 증거 밖에 있는 것 - 단정 불가 리스트**
- 미열람 관련 출원의 전문: 확보한 전문은 이 출원과 US 12,361,091 B1(선행 런)뿐이다. 18개월 미공개 창 안의 출원은 존재도 내용도 미지다.
- 레지스트리 스냅샷(2026-07-02 WIPS/DOCDB export) 이후의 심사 경과: 3차 non-final 통지의 내용과 이후 보정·응답. 일자들 자체도 registry-extract다 (environment-limited).
- 제품(Sohu)이 실제로 어느 청구항이라도 실시하는지 여부.
- LVI가 다른(미열람) 출원으로 커버되는지 여부.
- 등록 여부와 최종 범위: 심사관 인용 8건의 밀집 분야에서 가장 넓은 1항이 먼저 좁혀질 수 있다.
- 회사 발표 수치의 사실 여부.

**(c) 원문 자체가 열어둔 것**
- 명세서가 대안 실시예나 "may"로 열어둔 지점: 메모리 칩 없는 구성 `[0037]`, 스택 적층 `[0031]`, 양방향 메모리 연결 `[0034]`, 로컬 어레이의 로컬 메모리 접근 `[0051]`, AI 밖 응용(암호, DNA/단백질 시퀀싱, 신호 처리) `[0019]`.
- `[0037]`: "Further, in some embodiments, the memory chips 210 may not be needed."
  (일부 실시예에서는 메모리 칩이 아예 필요 없을 수 있다는 뜻)
- `[0051]`: "However, in other examples, the local systolic arrays 220 may also have access to the memory chips 610."
  (다른 예에서는 로컬 어레이도 로컬 메모리 칩에 접근할 수 있다는 뜻, 13항이 닫는 지점을 명세서는 열어 둠)

## ⑦ 자료 지도

반박이 오면 볼 곳:

| 반박 유형 | 참고 파일 |
|---|---|
| 가장 강한 반론 (steelman) | `handoff/01-design/thesis-spine.md` §Adversarial defense |
| 문장별 검증 | 최종 라운드 `handoff/03-edit/selfaudit-round-3-grounding.md` |
| 외부 사실 | `handoff/01-design/fact-check-log.md` |
| 청구항 범위 | `handoff/01-design/invention-summary.md` §Claim scope map |
| 원문 | `essays/etched-us20240378175-r2/patent.md` |

N=3은 이 런의 마지막 self-audit 라운드다. 경로는 `essays/etched-us20240378175-r2/` 기준이다.

> Revision note - retro back-fill 2026-07-04: 완료된 런에 owner-briefing-schema.md 계약을 소급 적용해 아카이브 번들과 input/essay-context.md에서 작성했다.
> Revision note - erratum 2026-07-04: ⑤의 스레드 시점 "2026년 7월"을 "2026년 6월 말"로 교정 (essay-final.md와 TechCrunch 2026-06-30 근거; promo-composer가 suspected_essay_defects 채널로 보고한 sa1B-F5 동종 month-slip. 상류 원천은 essay-context.md와 fact-check-log 키 설명의 "July 2026" 표기).
