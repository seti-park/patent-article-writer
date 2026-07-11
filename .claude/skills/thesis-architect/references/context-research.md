# Context research (Step 1-2)

essay-architect Step 1 의 web-search-first context research + Step 1.5 placeholder stop + Step 2 pool admission proposals 의 detail.

## Step 1: Context research

Web search for cascade, industry baseline, prior art, related news. Output is *staged* as ProposedEntries — not directly injected to Blueprint.

### Sub-step 1a: Web-search-first

Step 1 의 모든 synthesis 는 web search 결과 기반. 모델의 내부 지식 기반 synthesis 는 금지. 출원인, 업계 동향, 경쟁사 기술 등의 industry context 는 web search 로 evidence 확보 후에만 작성.

검증 절차:

1. Step 1 진입 시 search log file (`/mnt/user-data/outputs/{essay-id}/search-log.json`) 생성. 매 web search 마다 query + timestamp + top-3 result URLs 기록.
2. Synthesis 전 search log file 존재 + 최소 3 query 기록 확인.
3. Synthesis 의 모든 claim 이 search log 의 specific URL 에 anchor 되는지 cross-check.
4. deterministic-gate 의 web-search-required check 가 Step 1 종료 후 자동 호출. Search log file 부재 시 Step 2 진입 차단.

### Sub-step 1b: Source authority application

Industry context, 경쟁사 기술, 출원인 정보 의 source 는 primary source authority hierarchy 따름. Hierarchy detail 과 verification rule 의 SoT 는 editorial-review 의 `references/external-fact-verification.md` (essay-architect 와 editorial-review Sub-pass 3.5 가 cross-skill share).

essay-architect Step 1 적용 시 다음 application rule 만 의식:

- **경쟁사 또는 타사 기술 claim** 시 최소 Tier 2 source 필수 (그 회사의 official statement 또는 registered patent 또는 peer-reviewed paper). Tier 3 news media 만으로는 부족.
- **출원인 정보 또는 회사 전략** claim 시 Tier 1 우선 (Company official statement, press release, IR page, SEC filing).
- **시의성 이벤트** claim 시 Tier 1 과 Tier 3 양쪽 cross-check.
- **기술 mechanism** claim 시 Tier 2 (patent 또는 spec) 우선. Tier 4 의 reverse-engineered claim 은 hedge 필수.
- **Personal blog, Twitter, Reddit** (Tier 5) 은 Tier 1-4 의 backup 으로만 사용. 단독 anchor 불가.

### Sub-step 1c: Academic citation re-verify

External academic citations (author lists, DOI, journal, year, volume/issue) 의 web-search re-verify 의무. Memory caching 또는 prior session 의 reference 를 trusted 안 함.

본 의무가 Tesla 944 essay 의 "Tranter et al." → "Li, Marzook et al." 정정의 anchor — 본 정정이 web search re-verify 로 catch 됐고, Memory caching 으로 skip 했으면 stale citation 잔존 가능성.

### Sub-step 1d: Framing-impact classification

Each significant finding (web search result that anchors a 4-axis or shifts the thesis frame) must be classified for framing-impact at discovery time. Without this, Step 3 candidate generation may produce a candidate set that's invalidated by the next finding's framing impact.

| Class | Meaning | Phase 1 next action |
|---|---|---|
| **main thread** | finding shifts the thesis's primary anchor or audience hook | raise `OWNER_QUESTION` immediately (orchestrator relays); possibly re-extract `invention-summary.md` Layer 4 angles |
| **paragraph** | finding deserves one body paragraph but doesn't reshape the spine | record in `fact-check-log.md`; plan paragraph in spine |
| **footnote** | finding is supporting only — useful for credibility but not load-bearing | record only in `fact-check-log.md` |

The classification is a 1-line decision per finding. Claude proposes (with rationale); Owner accepts / overrides via the orchestrator-relayed checkpoint.

Origin: phase1-retrospective.md Insight 5-1 (STM partnership 발견의 framing 진동) + 5-2 (graceful degradation layer 구분의 정밀화).

## Step 1.5: Placeholder stop

Context research output 과 staged ProposedEntries 의 placeholder detection. TBD, [insert later], null, [...] 같은 unresolved placeholder 의 identification + blocking decision.

### Detection patterns (mechanical)

- `TBD`, `tbd`, `[TBD]`
- `[insert later]`, `[fill in]`, `[need]`, `[?]`
- `null` 또는 빈 essential fields
- `<...>` (unfilled template markers)
- Trailing `...` in fact statements

### Modes

- **Soft mode** (default): Placeholder 발견 시 warning + `OWNER_QUESTION`. Pipeline 진행 가능 (Owner 가 accept-with-knowledge 또는 fix, orchestrator-relayed).
- **Hard mode** (명시 시): Placeholder 발견 시 immediate STOP. Pipeline halt + FailureReport. Owner 의 fix 후 재진입 (orchestrator checkpoint).

### Default selection

- Time-constrained 또는 wire-style essays (strict-execution-mode): hard mode. 시간 제약 시 placeholder 의 silent passing 위험.
- Standard essays (walkthrough-mode, direct/Owner invocation only): soft mode. Pipeline forks raise `OWNER_QUESTION` instead of mid-session elicit.
- Adversarial reader 또는 strategic essays (conservative posture): hard mode. Placeholder 의 factual gap 위험.

본 placeholder stop 가 engineer-the-environment 적용 — placeholder 의 silent acceptance 회피.

## Step 2: Pool admission proposals (via pool-admission)

For each context research finding worth using:

1. Construct ProposedEntry (claim_text, source_url, source_anchor, usage_type).
2. Invoke pool-admission with entry.
3. If admitted, entry_id usable in facts_locked.
4. If rejected, discard or revise.

Owner 가 full visibility 가짐 (via orchestrator surfaces) — every proposed admission is explicit.

### Hybrid strictness (pool-admission 의 책임)

- **Verbatim entries** (quote attribution): strict admission. Source verbatim match required.
- **Paraphrase entries** (background reference): lightweight admission. URL fetchable only.

Detail 은 pool-admission 의 `references/admit-criteria.md` 참조.

### Output of Step 2

facts_locked 의 entry_id list. 각 entry_id 는 fact-base.yaml 에 admitted 상태로 존재.
