# Single-spine default

v2 default: single-spine. Multi-spine (multi-vendor synthesis, cross-company convergence, multi-thread restrained) requires Owner explicit override (invocation keyword, or `OWNER_QUESTION` if the worker needs to surface the choice).

## Default behavior

Step 3 (thesis candidate generation) 의 candidate 들은 single-spine 후보로 도출. `invention-summary.md` 의 Layer 4 `innovation_angles` 중 하나의 angle 에 anchor. Multi-spine 후보는 default 에서 제외.

## Override trigger keywords

Owner 가 다음 키워드 중 하나를 명시 invocation 에 포함하면 multi-spine candidate 진입.

- "multi-thread essay"
- "cross-vendor synthesis"
- "multi-spine 으로"
- "BP1 모드" — historical reference (v1 의 BP1 was Tesla 4680 multi-patent essay)
- "multi-spine 후보 도출"

Override 가 명시 안 됐으면 multi-spine 후보 자체가 candidate 목록에 들어가지 않음.

## Why single-spine default

v1 운영 결과:

- Single-spine essay: thesis arc 가 lock-on, reader engagement 높음, voice fidelity 5% 이내.
- Multi-spine essay (multi-vendor synthesis, restrained mode): word_target ±20% 자주 위반 (~3-4 essay), voice drift 10%+ 발생.
- A-style deprecate 메커니즘: multi-thread restrained essay 의 voice canon entry 가 누적 corpus 에 영향 안 주도록 manual rejection (v1). v2 에서는 단순화 — default 자체를 single-spine 으로.

Multi-spine 은 정당한 use case 가 있을 때만 (예: 같은 회사의 cross-domain patent cluster, 또는 cross-vendor convergence 분석). 매 essay 의 default 가 아님.

## Override 시 추가 의무

Multi-spine 후보가 candidate 목록에 들어가면 다음 명시.

1. 각 spine 의 4-axis grounding 독립 적용.
2. Spine 간 정합 (어떻게 thesis 가 연결되는가) 명시.
3. Q7 hook gate 가 spine 별 적용 — 모든 spine 이 같은 hook pattern 일 필요는 없으나 essay 전체의 entry point 는 하나.
4. word_target 자동 격상 (single-spine 의 1.5x 권장).
5. `thesis-spine.md` 의 "Single-spine declaration" 영역에 `Multi-spine` 체크.

## Owner 의 결정

Multi-spine 진입 후에도 Owner 가 final selection 단계에서 single-spine 으로 회귀 가능 (orchestrator soft checkpoint). Override 가 candidate 진입 허가일 뿐 selection 강제 아님.

## v2 vs v1 차이

| 영역 | v1 | v2 |
|---|---|---|
| Default | Single-spine + multi-spine candidates 함께 도출 | Single-spine candidates 만 도출 |
| Multi-spine 진입 | thesis_candidates 에 포함되지만 Owner 가 select | Owner 가 override keyword 명시할 때만 candidates 에 포함 |
| A-style deprecate | (dropped; v1 pool-admission) | 불필요 (default 가 single-spine) |
| Override 부담 | 항상 multi-spine candidate 도 처리 | Override 명시할 때만 처리 |

v2 의 simplification 은 default path 의 burden 감소 + multi-spine 의 explicit cost 가시화.
