# Promo pack — openai-us20260147536

> **Composed by the orchestrator (main session model), not the promo-composer agent:** the
> Phase-4 agent hit a session limit before it could run. This pack follows the promo-composer
> contract (bold-selection rule, ≤1 insurance clause per deliverable, 0 examination-process
> narration) and the hard grounding rule — every factual phrase traces verbatim-consistent to
> `essay-final.md` / `publication-package/publication.md` or `owner-briefing.md`; no fact was
> fetched. Re-run the promo-composer agent next session if a fully independent pass is wanted.

## Verification Status
- Source of every claim below: `essays/openai-us20260147536/essay-final.md` +
  `owner-briefing.md` (both gate-verified; essay double-clean accepted → self-audit-dry → 윤문).
- Independent claims to the core triad: **1, 20, and 29** (not "1 and 20").
- The align-once / integer-accumulate arithmetic is **block floating point** — prior art, not
  OpenAI's invention. What OpenAI seeks to own is the **compute-in-memory circuit** that runs it.
- Pending application (claims 11–19 canceled). **No source ties this design to Jalapeño or to
  any shipping silicon** — the promo does not claim it does.
- Dates: priority **2024-11-22** · OpenAI/Broadcom announcement **2025-10-13** (~11 months
  later) · Jalapeño reveal **2026-06-24** · deployment target end of 2026.

---

## (a) Korean long-form post (설명체, 존댓말)

OpenAI가 "우리가 설계한 AI 가속기"를 공개적으로 발표한 건 2025년 10월이었습니다. 그런데 특허 기록은 그보다 앞섭니다. OpenAI Opco 명의로 출원된 US 2026/0147536 A1의 가출원 우선일은 2024년 11월 22일 — 발표보다 약 11개월 빠릅니다.

이 문서가 흥미로운 건 깊이입니다. 메모리 셀(비트셀), 클록 타이밍, 테스트용 스캔 회로까지 내려간 컴퓨트-인-메모리 연산 회로 설계예요. 핵심 아이디어는 하나로 요약됩니다. 저정밀 부동소수점 곱셈을 메모리 배열 안에서 수행하되, 곱들의 가수(mantissa)를 딱 한 번만 정렬해 두면, 그 비싼 누산을 통째로 값싼 정수 덧셈기로 처리할 수 있다는 겁니다. 부동소수점 덧셈 회로가 통째로 필요 없어집니다.

다만 정확히 짚자면, 이 "한 번 정렬하고 정수로 더한다"는 방식 자체는 블록 부동소수점이라는 이미 알려진 기법입니다. OpenAI가 소유하려는 건 그 아이디어가 아니라, 그걸 메모리 배열 안에서 실행하는 회로예요 — 독립항 1·20·29번이 겨냥하는 대상입니다.

주의할 점도 분명합니다. 아직 등록 전 출원이고, 이 설계가 실제 칩(예: Jalapeño)에 들어갔다거나 실리콘으로 제조됐다는 근거는 어디에도 없습니다. 그럼에도 이 문서가 증명하는 건 "방향"입니다. "OpenAI가 설계했다"는 말이 홍보 문구가 아니라, 발표 11개월 전에 이미 회로 단위로 적혀 있던 문자 그대로의 엔지니어링이라는 사실이죠.

---

## (b) English thread

**1/**
OpenAI announced "OpenAI-designed" AI accelerators with Broadcom in October 2025.
The patent record is older. A compute-in-memory design filed under OpenAI Opco, LLC carries a priority date of November 22, 2024 — about eleven months before the announcement.

**2/**
The trick is one move.
Multiply low-precision floating-point numbers (FP8/FP6/FP4) right inside the memory array. Align the mantissas onto one shared scale a single time. Now the whole expensive accumulation runs on plain integer adders — the floating-point adder tree disappears.

**3/**
Being fair about it: that align-once, integer-accumulate style *is* block floating point — a known technique, not OpenAI's invention.
What its independent claims (1, 20, and 29) seek to own is the compute-in-memory *circuit* that executes it inside the array.

**4/**
And it isn't a concept sketch. The filing descends to bitcell circuits, clock margins, and scan-test structures — a document written toward manufacture, assigned to OpenAI.
Concept filings rarely carry clock margins. This one does.

**5/**
The bounds, stated plainly: it's a pending application (claims 11–19 canceled), and nothing ties it to Jalapeño or to shipping silicon.
What it proves is direction — "OpenAI-designed" is literal engineering, on file before it was news.
