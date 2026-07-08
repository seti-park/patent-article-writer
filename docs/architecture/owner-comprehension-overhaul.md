# Owner-comprehension overhaul (2026-07-04)

**Motive.** Inspired by the unknown-unknowns framing (Thariq, html-effectiveness/unknowns —
articulated by the owner; the post itself is unreachable from this sandbox): the publisher
cannot judge final quality, answer readers after publication, or write promos for an
article about a patent they do not genuinely understand. The 2026-07-04 reader-first
overhaul fixed what READERS get; this one fixes what the OWNER gets.

**Diagnosis headline (owner interview, 2026-07-04).** After two full runs on this corpus
the owner self-assesses at "one-line summary" comprehension of US 2024/0378175 A1, and has
historically not answered reader reactions — not for lack of will but of armament. Every
understanding artifact the pipeline produces (invention-summary, claim scope map,
fact-check-log, steelman) is machine-facing, English, handoff-formatted. The pipeline
understands the patent; the owner never receives that understanding. Post-publication
response and promotion are OUT-OF-PIPELINE duties that today rest on comprehension the
pipeline never transfers. The independent cold-eyes audit
(`docs/architecture/cold-eyes-owner-audit-2026-07-04.md`) confirms it mechanically: of ~32
artifact types, ~7 are human-facing and ZERO transfer patent comprehension to the owner; the
material that would arm post-publication defense (steelman, 41-70-row grounding tables, claim
scope map) exists but is buried under loop-jargon paths, unindexed, English-only — and its
[dddd] anchors point into a patent text absent from the tracked archive.

**Interview decisions (binding):** Korean owner-briefing ONLY (no Q&A pack, no
comprehension-check interview); Phase 4 promo port INCLUDED with Korean promo drafts.

## As-is → To-be

| # | As-is | To-be | Files |
|---|-------|-------|-------|
| U1 | Phase 1 produces machine-facing design bundle only | Phase 1 gains **step 0 — owner briefing (comprehension before thesis)**: before any thesis work, write `handoff/01-design/owner-briefing.md` in KOREAN for the publisher | `thesis-architect/SKILL.md` + new reference `owner-briefing-schema.md` |
| U2 | No owner-facing understanding contract | Briefing schema = the owner's five elements: ① 과거 기술의 과제/문제점 ② 기존 기술의 해결 방향 ③ 이 특허의 독창적 해법 (핵심 청구항 중심, 잠긴/추구 구분) ④ 기대 효과 ⑤ 회사 프로모션(스레드·제품)과의 연결 — PLUS ⑥ the unknown-unknowns section: **아는 것/모르는 것 경계 지도** (이 런의 증거가 확립한 것 vs 증거 밖에 있는 것 vs 원문 자체가 열어둔 것) and ⑦ **자료 지도** (반박이 오면 어디를 볼지: steelman → thesis-spine §Adversarial defense, 문장별 검증 → 최종 selfaudit-round-N-grounding.md, 외부 사실 → fact-check-log, 청구항 범위 → invention-summary Claim scope map — contract paths named at write time, round numbers filled by the run) | new `_shared/references/owner-briefing-schema.md` |
| U3 | Understanding artifacts unverifiable for humans | Sections ①-④ each end with a `**근거 (verbatim):**` block of gate-parseable span lines (`` - `[dddd]`: "exact English quote" ``) inside the Korean prose → **gate_quotes verifies the briefing** with zero code changes: `gate_quotes.py <briefing> --invention-summary <briefing> --patent input/patent.md` at the Phase-1 early gate | orchestrator invocation in `patent-essay/SKILL.md` |
| U4 | Owner-briefing would die in gitignored handoff/ | Briefing is a TRACKED deliverable: archived to `essays/<id>/owner-briefing.md` (the 3-days-later shelf) | `patent-essay/SKILL.md` archive contract |
| U5 | check_run blind to the new artifact | RUN-008 (fail): `owner-briefing.md` missing from handoff/01-design when the run completes | `check_run.py` + test |
| U6 | Phase 4 promo-composer exists only as a source prompt (docs/source-prompts) | **Port `promo-composer`** as `.claude/skills/promo-composer/` + `.claude/agents/promo-composer.md` (fork, inherit model): consumes the `essays/<id>/` archive (essay-final / publication.md, owner-briefing.md, thesis-trace signature lines, README reader_sentence) → single `essays/<id>/promo/promo-pack.md` with (a) Korean promo post ≤280자, 발행자 목소리 (`working-dialogue-voice.md` register) (b) English promo digest 280-340 words in the source prompt's FT/Economist genre (c) an English 3-tweet thread sketch (each ≤280 chars) — plus a verification-status header. Grounding rule = the safe-claims defense: EVERY factual phrase traces to essay-final/publication.md or owner-briefing.md (which carry the loop-corrected phrasings — venue, founder count, year arithmetic); no new factual claims, no memory-written facts. Runs POST-archive as Phase 4; never edits the essay | new skill + agent |
| U7 | Orchestrator flow ends at retro | Flow: … archive → **Phase 4 promo (on by default for essay mode)** → retro. Briefing surfaced to the owner at Phase-1 return alongside thesis/title candidates | `patent-essay/SKILL.md` |
| U8 | CLAUDE.md silent on owner enablement | Operating principle added: the pipeline's understanding must reach two humans — the READER (goal 5) and the OWNER (briefing + promo). Not a rubric goal; an output contract | `CLAUDE.md` |
| U9 | `input/patent.md` untracked → every [dddd] anchor in the archive dangles for a human (audit Gap 2; only patent text preserved is the grounding tables' verbatim column) | Archive contract adds **`essays/<id>/patent.md`** (the run's exact input snapshot). Retroactive for both 175 essay dirs (input/patent.md still holds that text); 091's input was overwritten — noted, not restored | `patent-essay/SKILL.md` archive contract |
| U10 | Human-role language has drifted (audit Gap 5): thesis-architect step 7 "SETI selects one", editorial-review "SETI revises → essay-final.md" — roles the orchestrator automated away | Reconcile SKILL wording with orchestrated reality: orchestrator selects/revises via agents, owner holds OVERRIDE authority at surfaced decision points (title register pick, briefing review, post-accept channel). No behavior change — the docs stop lying | `thesis-architect/SKILL.md` step 7, `editorial-review/SKILL.md` |

## Grounding discipline for the briefing (unchanged bar, new surface)

Korean prose; every patent-derived claim in the briefing anchored [dddd]; verbatim quotes
stay English (never translated inside quote marks — translation follows OUTSIDE the quote);
external facts carry their evidence_level labels; the 경계 지도 section explicitly lists
what CANNOT be asserted (sibling full texts, prosecution beyond the registry snapshot,
LVI coverage) — the unknown-unknowns made legible.

## Validation (acceptance criteria)

1. Retroactive owner-briefing generated for US 2024/0378175 A1 from the r2 bundle +
   patent.md; gate_quotes PASS on it; owner confirms it moves their self-assessed
   comprehension past "one-line summary".
2. promo-composer produces the r2 promo pack (KR/EN/thread) grounded in the briefing and
   the essay's protected lines; no new factual claims beyond the essay + briefing —
   specifically, none of the three loop-scrubbed error classes (venue, founder count, year
   arithmetic) resurface.
3. test_gates/regression PASS after U5 (fixtures updated so RUN-008 doesn't break them).
4. `essays/etched-us20240378175-r2/patent.md` exists and the briefing's anchors resolve
   against it (U9).
5. Next full pipeline run requires no orchestrator improvisation for any of U1-U10.

## Audit → remedy traceability

| Audit gap (cold-eyes-owner-audit-2026-07-04.md §6) | Addressed by |
|---|---|
| 1 — no owner-understanding artifact | U1-U4 (briefing, gate-verified, tracked) |
| 2 — defense material buried/unindexed; patent untracked | U9 (patent.md archived) + schema ⑦ 자료 지도 |
| 3 — promo unported, no Korean, no safe-claims card | U6 (port + KR; safe-claims handled as a grounding RULE, not a new artifact) |
| 4 — quality judgment has no human decision surface | Partially: U7 (briefing surfaced at Phase-1 return); a formal pre-archive owner-signoff gate is DEFERRED — the interview set scope to 브리핑만, and the title pick + posting-checklist remain the operational human moments |
| 5 — owner understanding consumed at input; role language drifted | U10 (role-language reconciliation); the 5-question comprehension interview is EXCLUDED by the owner's interview decision |

## Out of scope (per interview)

예상 반박 문답집 (Q&A armory) and the comprehension-check interview loop — declined by the
owner; the 경계 지도 + 자료 지도 sections partially serve the first need without a new
artifact class. Also deferred: a formal owner-signoff gate before archive (audit Gap 4's
full remedy).

## Validation results (2026-07-04, r2 retroactive)

1. **PASS** — retroactive briefing at `essays/etched-us20240378175-r2/owner-briefing.md`:
   896 어절, 11 verbatim span lines, gate_quotes PASS against the archived patent.md
   (verified twice, agent + orchestrator). Owner confirmation of the comprehension move is
   the remaining human half.
2. **PASS** — promo pack at `essays/etched-us20240378175-r2/promo/promo-pack.md`: KR 265자 /
   EN digest 295w posture-D-agrees-firm / tweets 223·275·234 chars; fact_trace 18/18, zero
   dropped facts; all three scrubbed error classes verified dead. BONUS: the safe-claims
   fence caught a real defect — the briefing's ⑤ had re-imported the sa1B-F5 month-slip
   ("2026년 7월" vs the essay's late-June TechCrunch-sourced dating) from
   essay-context.md/fact-check-log phrasing; promo followed the essay, routed the finding,
   and the briefing was erratum'd same day. The channel works.
3. **PASS** — test_gates 102/102 (99+3), meta/regression.py PASS, fixtures untouched.
4. **PASS** — `essays/etched-us20240378175-r2/patent.md` archived (md5-identical to input);
   also back-filled to the v7 dir. 091's input snapshot is unrecoverable from disk (noted).
5. **OPEN until the next full run** — U1-U10 need no orchestrator improvisation: to be
   proven on the next pipeline invocation (the doctrine, gate invocation, RUN-008, archive
   contract, and Phase 4 flow are all written and registered).

Retro material logged here for the next `pipeline-retro`: the "July 2026" month-slip class
has three upstream carriers (`input/essay-context.md` — user-owned, flagged to the owner;
the archived fact-check-log key description; the v7 README) and re-entered once through a
Korean summary surface; candidate proposal is a date-canon line in essay-context or a
fact-check-log normalization rule.
