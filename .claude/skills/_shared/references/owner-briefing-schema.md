# Owner briefing schema: the Korean comprehension contract

Single source of truth for `handoff/01-design/owner-briefing.md`. The briefing transfers the
pipeline's patent comprehension to the PUBLISHER (a Korean native) before thesis work begins:
from this document alone the publisher must be able to judge the final essay, answer reader
objections after publication, and brief a promo. It is a comprehension artifact, not a run
report, and it is fidelity-checked like the invention-summary: every verbatim span in it must
appear verbatim in `input/patent.md`.

- **Writer**: `patent-reader` (`patent-understand` stage, voice-off) writes ①–④ + ⑥ into
  `handoff/00-understand/owner-briefing.md` **before** any thesis work. `design-architect`
  may update section ⑤ (promo link) only after context research. Comprehension precedes
  thesis: the briefing describes the PATENT, never the essay's angle.
- **Consumers**: the OWNER first; later `promo-composer` (Phase 4), which uses the briefing
  as a grounding source for the promo pack.
- **Verification**: `gate_quotes` at the Phase-1 early gate. The `근거 (verbatim)` span lines
  parse as Quotable-span lines, so the existing gate verifies the briefing with zero code
  changes; any QUOTE-001 is fixed at the source before Phase 2 runs.
- **Archive**: `essays/<essay-id>/owner-briefing.md`, tracked next to the run's `patent.md`
  snapshot so every `[dddd]` anchor resolves offline.

## Document structure

### Header block

Korean field labels; names, numbers, and dates verbatim from the patent cover page:

- **특허 번호** / **제목** / **상태** (등록·출원 구분: 등록이면 등록번호·등록일, 출원이면
  공개번호·심사 상태) / **출원일** / **발명자**
- **한 줄 요약**: the owner's Korean takeaway sentence, exactly one line. If the owner keeps
  nothing else, they keep this line; draft it last, after ①-⑦ are written.

The 상태 field decides section ③'s vocabulary: 등록 건은 locked 어휘, 출원 건은 sought-* 어휘.

### ① 과거 기술의 과제/문제점

이 특허가 출발점으로 삼는 문제. 명세서 background 가 지목하는 "무엇이 안 되고 있었는가"를
서술한다. 업계 일반론이 아니라 이 문서가 명시한 문제로 한정한다. Ends with a `근거` block.

### ② 기존 기술의 해결 방향과 그 한계

종래 기술(선행 문헌·업계 관행)이 그 문제를 어떻게 풀려 했고 어디서 막혔는지. 이 특허와의
차별점이 여기서 준비된다. Ends with a `근거` block.

### ③ 이 특허의 독창적 해법 (핵심 청구항 중심)

발명이 실제로 청구하는 해법. 핵심 독립항 번호를 명시하고, `invention-summary.md` Claim
scope map 의 구분을 그대로 사용한다: locked(청구항 본문이 요구) / open(명세서 선호일 뿐) /
pinned("about X" 점 한정). 출원 건에는 locked 가 없다: 모든 범위 서술은 map 의 sought-*
표기(청구 중, 확정 아님)를 그대로 따른다. 청구항이 요구하는 것과 명세서가 선호만 하는 것을
절대 섞지 않는다. Ends with a `근거` block.

### ④ 기대 효과

명세서가 주장하는 효과로 한정한다. 수치는 문단 앵커와 함께 적고, 명세서 밖의 효과 추정은
넣지 않는다(그것은 ⑥ (b)의 영역). Ends with a `근거` block.

### ⑤ 회사 프로모션 글/기술과의 연결

회사의 공개 발언·프로모션 글·제품 서사와 이 특허의 관계. 두 칸을 명확히 가른다:

- **특허가 실제로 뒷받침하는 것**: 특허 텍스트에 앵커되는 부분만.
- **회사 주장**: 특허가 뒷받침하지 않는 회사 발언. 외부 사실에는 `fact-check-log.md` 의
  evidence_level 라벨을 그대로 부기한다 (예: registry-verified / registry-extract /
  bibliographic / company-claimed).

Step 2 context research 와 `input/essay-context.md`(있으면)가 이 섹션의 재료다. 연결할
프로모션 맥락이 없으면 "없음"이라고 명시한다.

### ⑥ 아는 것/모르는 것 경계 지도

Three subsections, all three always present:

- **(a) 이 런의 증거가 확립한 것**: 특허 전문 확인, 레지스트리 사실 등 이번 런이 검증한 것.
- **(b) 증거 밖에 있는 것 - 단정 불가 리스트**: 독자 앞에서 단정하면 안 되는 것의 명시적
  목록. 예: 읽지 않은 관련 출원의 전문, 레지스트리 스냅샷 이후의 심사 경과, 제품이 실제로
  청구항을 실시하는지 여부.
- **(c) 원문 자체가 열어둔 것**: 명세서가 대안 실시예나 "may" 표현으로 열어둔 지점
  (`[dddd]` 인용 가능; verbatim 인용 줄 형식을 쓰면 그 줄도 게이트 검증 대상이 된다).

### ⑦ 자료 지도

반박이 오면 어디를 볼지. 고정 계약 경로만 쓰는 작은 표:

| 반박 유형 | 참고 파일 |
|---|---|
| 가장 강한 반론 (steelman) | `handoff/01-design/thesis-spine.md` §Adversarial defense |
| 문장별 검증 | 최종 라운드 `handoff/03-edit/selfaudit-round-N-grounding.md` |
| 외부 사실 | `handoff/01-design/fact-check-log.md` |
| 청구항 범위 | `handoff/01-design/invention-summary.md` §Claim scope map |
| 원문 | `essays/<essay-id>/patent.md` |

Paths are deterministic contract paths; inside the archive they resolve relative to
`essays/<essay-id>/`. Round numbers are filled by the run: N is the run's final self-audit
round, i.e. the largest N present under `handoff/03-edit/` when the run completes.

## Grounding rules (the gate-parseable format)

1. **Inline anchors everywhere.** Every patent-derived claim in the Korean prose carries an
   inline `[dddd]` paragraph anchor (backtick-wrapped, 4-digit, zero-padded), matching
   invention-summary style.
2. **근거 blocks close ①-④.** Sections ①-④ each END with a `**근거 (verbatim):**` block of
   1-3 lines in EXACTLY this format:

   ```markdown
   **근거 (verbatim):**
   - `[0014]`: "conventional accelerometer-based systems respond only after the collision has begun"
     (기존 가속도계 기반 시스템은 충돌이 시작된 뒤에야 반응한다는 뜻)
   ```

   Per-line constraints: backtick-wrapped `[dddd]` anchor; straight double quotes; quote
   length at least 8 characters (the gate silently ignores shorter captures, so shorter
   quotes are banned); text verbatim from `input/patent.md`. Tolerances are exactly those of
   `thesis-architect/references/quote-anchor-conventions.md`: NBSP to space, `**bold**`
   marker strip, smart quotes to straight. Nothing else.
3. **Quotes stay English.** Text inside the quote marks is NEVER translated. The Korean
   gloss follows OUTSIDE the quotes, on the next line as an indented parenthetical (see the
   example above). The span line must end at its closing quote: any trailing text after the
   quote breaks gate parsing and silently un-verifies the line.
4. **The span-line format is reserved.** Any line matching the span-line grammar (dash,
   backticked anchor, colon, double-quoted text to end of line) anywhere in the briefing is
   treated as a verbatim claim and gate-checked. Use it only for true verbatim patent
   quotes; everywhere else, cite with inline anchors in prose.

## Register (embedded style contract)

Phase 1 is voice-off: the design agent may not read voice-canon files, so this schema
carries the style itself.

- 건조한 한국어 평서문. 단정은 근거 위에서만: 앵커 없는 특허 단정 금지.
- 과장·수식어 배제. 세일즈 톤 금지: 이 문서의 일은 이해를 옮기는 것이다.
- 특허 용어는 원어 병기: 예) 크로스바(crossbar), 시스톨릭 어레이(systolic array). 청구항
  용어·부품 번호·verbatim 인용은 원문 그대로 둔다.
- No em dashes (the deliverable rule applies here too).
- Target length: 본문 600-900 단어(어절 기준) + 인용 블록. A 5-minute read: depth belongs to
  the invention-summary dossier; the briefing must survive one sitting.

Full worked template: `handoff-template/01-design/owner-briefing.md`.
