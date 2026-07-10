# X Articles format (English)

X Articles platform conventions for English essays. Referenced by tech-essay-en SKILL.md.

본 파일은 두 차원으로 구성. Section 1 은 X Articles platform 전반의 spec (Owner authoritative — tech-essay-ko-pub 도 동일 적용 의무). Section 2 는 영문 essay 의 editorial convention (BP 6건 분석 기반).

X Articles 는 X platform 의 long-form publication format. tech-essay-en (영문 essay) 과 tech-essay-ko-pub (한글 essay) 의 발행 산출물이 본 platform 의 영역. patent-wire 와 patent-promo 는 X post format 영역 — X Articles 가 아니므로 본 spec 적용 안 됨 (각 skill 의 자체 format 영역).

---

## Section 1 — X Articles platform spec

본 section 의 모든 rule 은 X Articles platform 의 발행 constraint 와 정합 의무. tech-essay-en / tech-essay-ko-pub 의 발행 작업 시 본 spec cover 영역.

### Markdown rendering

**Bold 표기**. X Articles 는 markdown `**text**` 형식의 bold 를 정상 렌더링. active convention — `**text**` 사용.

**Tables — image 변환 필요**. X Articles 는 markdown table 을 정상 렌더링하지 않음. 작업 path — table 본문을 image 로 변환 후 X Articles 에 image 형식으로 발행. 본 변환은 작성 단계의 image preparation 영역.

**Line wrapping (publication.md)**. One line per paragraph, blank line between paragraphs. No
intra-paragraph hard wraps (X Articles honors single newlines, so a mid-sentence wrap renders as a
ragged break). A block quote is one `>` line for the quote plus one `>` line for the attribution.
Headings, list items, and italic captions each stay on their own line. Enforced mechanically by the
strip pipeline's paragraph-rejoin step (`_shared/scripts/strip_publication.py`) — see
`references/strip-pipeline.md`.

### Stock ticker — cashtag

주식 ticker 는 first mention 에서 `$` prefix 의 cashtag form 사용 (예: `$AGLT`). X platform 의 native·linkable token — discoverability + convention 정합. ticker-labeling context ("trading as", "NASDAQ:", "ticker") 뒤의 bare ticker 는 cashtag 로 승격. *(gate: `CASH-001` warn; 근거: run 045 `venue-ticker-convention`.)*

### Patent citation format

특허 paragraph 인용은 `[xxxx]` 형식 사용 (예: `[0047]`, `[0036]`).

본 convention 의 anchor — paragraph anchor 의 명확한 identifier. 모든 essay / wire / promo 에 일관 적용.

다음 영역에서도 본 convention 적용.

- 본문 안의 paragraph reference
- §Sources 안의 patent quote anchor
- caption 안의 figure-reference (예: *FIG. 3, [0042]*)

### Sources block structure

발행 산출물의 §Sources 의 구조.

**Heading level**. `# Sources` (h1) 가 default. 본 영역의 anchor — Sources 가 본문의 일부가 아니라 발행 산출물의 별도 영역의 visual 정합. Sub-group 사용 시 `##` (h2) 의 sub-heading.

**List 구조**.

- **Default — flat list**. 모든 source 가 분류 없이 한 list. 본 구조의 anchor — 분류의 over-engineering 회피.
- **Category subgrouping — all-or-nothing 영역**. 4개 이상의 source 가 2개 이상의 category 에 spans 시 subgrouping 적용 가능. 다만 partial subgrouping 회피 — 모든 source 의 category 명시가 all-or-nothing 의 정합.

**허용 category (5개 제한 enum)**.

- Patents
- Papers
- Official statements
- News & media
- Technical specs

위 5개 외 category 사용 금지 (예: Financial reports / Public record / Regulatory 같은 ad-hoc category 는 spec 위반).

### Sources per-item citation format

각 source 의 citation format.

**Papers (academic)**. 저자 4명 이상 시 *First, et al.* 형식 (full author list 안 함). citation 의 simplicity + Chicago / IEEE style 의 정합.

예 — *Li, Marzook, et al. (2024). "Title". Journal Name, Vol(Issue).*

**Patents**. 6 field 의 sequence.

1. 공개 / 등록번호 (publication number 또는 grant number)
2. 발명의 명칭 (인용 부호 안)
3. 출원인 (assignee)
4. priority date (`YYYY-MM-DD`)
5. publication date (`YYYY-MM-DD`)
6. inventors (전원, full name)

예 — *US20260134331A1, "Systems and Methods for Structure-Conforming Generation of Content," Google DeepMind, priorited 2024-11-08, published 2026-05-14, inventors: Ishita Dasgupta, Nikita Saxena, Isabelle M. Guyon, Mathangi Venkatesan, Benjamin Jan Pietrzak.*

**Descriptive annotation 회피**. 각 source 의 citation 후 descriptive annotation 추가 안 함. citation 의 essence 는 source 의 identifier 만, 해석 또는 평가 의 annotation 영역 아님.

❌ *<citation> — 본 patent 는 ... 의 핵심 영역을 cover.*

✓ *<citation>*

descriptive content 가 필요하면 본문의 figure caption 또는 footnote 영역.

---

## Section 2 — English essay editorial convention

본 section 은 영문 essay specific. tech-essay-ko-pub / patent-wire / patent-promo 와 별개 영역.

### Title conventions

**Length**. 9-14 words. 짧은 title (9-10 words) 은 declarative single-clause, 긴 title (13-14 words) 은 multi-clause 또는 subtitle-bearing.

**Character budget (feed)**. Title ≤ 70 chars (spaces 포함) — X card truncation budget, `_shared/references/reader-energy.md` 의 feed-context rule. 9-14 word convention 과 conflict 시 character budget 이 우선 (아래 BP 관찰 예시 중 70 chars 초과분은 pre-budget 시대의 기록). Phase 1 의 `title-lead-candidates.md` 가 이미 budget 안에서 title 을 제안 — composer 는 선택된 pair 를 따름. *(gate: `SURF-001` warn.)*

**Em-dash 금지**. Title 에서도 em-dash 사용 안 함 (deliverable voice 의 em-dash 금지 rule 이 title 까지 적용).

**Three observed patterns (BP 6건 분석 기반)**.

**Pattern 1: Declarative reversal**.

Subject + reversal verb + reframed object 의 one clause. Length 9-10 words. Title IS the thesis.

Examples 관찰:

- "Tesla's 4680 Line Replaced X-Ray with a Signal" (9 words, BP3)
- "Tesla's Etherloop, Published Just in Time for Cybercab" (9 words, BP4)

When to use — thesis 가 one declarative sentence 로 압축 가능. Reversal verb (replaced, eliminated, anchored) 가 punch carry.

**Pattern 2: Aphoristic phrase + colon explainer**.

Catchy phrase 또는 compound noun + colon + clarifying subtitle. Length 13 words. Hook front + technical context back.

Em-dash 사용한 BP 의 alternative form 적용. BP2 / BP5 의 original em-dash 는 colon 으로 변환.

Examples (em-dash 회피 form):

- "Photon In, Perception Out: How Tesla Runs a Transformer on 8-Bit Hardware" (13 words, BP2 form)
- "The Cybercab's Hidden Taillight: A Patent Filed One Day Before the Unveiling" (13 words, BP5 form)

When to use — thesis 가 aphoristic summary phrase + technical context.

**Pattern 3: Multi-clause reversal narrative**.

Two-to-three short sentences with reversal pivot. Length 14 words. 각 sentence 가 fact 또는 counter-fact, last sentence 가 thesis carry.

Example 관찰:

- "SpaceX merged with xAI. Tesla was left out. But their patents tell a different story." (14 words, BP6)

When to use — corporate narrative (news, M&A, public statement) 가 patent evidence 와 직접 contradict. hook_pattern `corporate-narrative-friction` 의 best fit.

**Pattern 4: Statement + forward-looking event**.

Declarative statement + comma + ", and what X will Y" forward pointer. Length 14 words. Title 이 binary test commit.

Example 관찰:

- "How Google's Cloud Profits Catapulted, and What Two Imminent AI Announcements Will Confirm" (14 words, BP1)

When to use — thesis 가 binary observable future event include. "and what..." pattern 이 forward-looking essay signal.

**Mapping to hook_pattern** (observed correlations, not strict rules).

- `timing-anomaly` → Pattern 1 또는 Pattern 4
- `visual-contradiction` → Pattern 2 (subject + visible-anomaly subtitle)
- `corporate-narrative-friction` → Pattern 3
- `technical-impossibility` → Pattern 2 (aphoristic catch + technical context)

Final title pattern 은 editorial judgment.

### Heading conventions (body)

본 영역은 본문 §section heading. §Sources heading 은 Section 1 의 platform spec 영역.

**Markdown level**. `##` (h2) 가 본문 major section 의 default. `#` (h1) 안 씀 — X Articles platform 이 title 설정.

`###` (h3) 은 본문에서 rare. 대부분 section 이 one `##` heading + 본문 prose.

**Numbering**. `§N` prefix 없음. Heading 은 descriptive title 만.

tech-essay-en 의 Blueprint 가 internally `section_id` (예: `1-lead`, `2-architecture`) 사용. `publication.md` 에서는 `## <descriptive title>` 의 numeric prefix 없는 form.

**Title style — claim-first (updated, run 045).** Section header 는 *주장(assertion)* 으로 작성. header 만 이어 읽어 essay 의 argument 가 재구성되는 skim-skeleton 이 목표 (run 045: *workflow-not-robot → disclaims-the-hard-parts → territory-is-not-the-moat → moat-is-filed-elsewhere*). 2-8 words typical.

- **Declarative claim (default)** — "The Claim Is a Delivery Workflow, Not a Robot", "The Territory Is Not the Moat". header IS the section thesis.
- **Noun phrase (secondary)** — "Operating Income Gap" (BP1), "The Margin Architecture" (BP1). label form; argument 를 carry 안 하면 claim 으로 승격.
- **"What X..." question form — 비권장(deprecated)** — "What '638 Actually Claims" 같은 label 은 claim 이 아니라 skim-skeleton 을 깸. declarative 로 변환.

*(editorial pass-6 / pass-7 header-as-claim check 가 검증. 근거: `meta/improvement-proposals/2026-06-26-human-revision-blindspots.md` 의 `nonclaim-section-header`.)*

**Capitalization**. Title Case in observed essays.

### Inline quote conventions

Two quote forms.

**Block quote (substantial verbatim, 15+ words)**. Block quote markdown (`> `).

Attribution form — em-dash 회피. Patent paragraph attribution 은 paragraph anchor `[xxxx]` form 사용. Multi-source attribution 은 separate line 의 comma-separated metadata.

Patent quote.

```markdown
> "Conventionally, x-ray and beta-ray systems are used for measurement of electrode basis weight..."
> US20260017051A1, [0017]
```

Person quote.

```markdown
> "We have a Gigabit Ethernet loop in the car that connects all of the high-speed controllers in the car. **It's bidirectional for redundancy**."
> Pete Bannon, Sandy Munro interview, December 2023
```

**Inline quote (short verbatim, under 15 words, embedded in sentence)**. Double quotes within sentence. No separate attribution — citation marker `[^fact-id]` 가 source linkage carry.

```markdown
The CEO told lawmakers the company "has never and will never sell user data." [^fact-id]
```

**Choice rule**.

- 15+ words verbatim → block quote
- Under 15 words verbatim → inline quote
- Quoted phrase mid-sentence → inline quote regardless of length

Block quote 는 prose flow 의 interrupt, inline quote 는 flow preserve. Quote 가 visual emphasis merit 시 block.

**Bold emphasis within block quote** (BP4 관찰). Author 가 thesis-relevant phrase 를 bold mark 가능.

```markdown
> "the second controller is further configured to: receive a second copy of the Ethernet message; and **discard the second copy** of the Ethernet message."
```

Bold 가 quote 안의 thesis anchor mark.

---

## Sources placement

§Sources 는 본문 (closing 포함) 후 위치. `draft.md` 의 §Sources 뒤에 §Footnotes block (strip pipeline 이 `publication.md` 작성 시 §Footnotes 만 strip, §Sources preserve).
