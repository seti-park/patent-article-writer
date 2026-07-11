---
name: promo-composer
description: "Phase 4 Promote: composes the post-archive promo pack for a finished essay. Promo는 이 작업의 정수 — Understand 삼각형(문제·해법·효과)의 대중 번역: the public translation of the Understand triad for a reader between high-school and undergraduate (고등학생과 학부생 사이). Consumes the essays/<id>/ archive (essay-final.md + publication-package/publication.md + owner-briefing.md + owner-study-pack.md triad + comprehension-notes.md landed frames + thesis-trace.md signature lines + README.md reader_sentence) and emits a single essays/<id>/promo/promo-pack.md: (a) Korean long-form promo post 400-800자, 존댓말 설명체 (직역 금지; 서사 훅 + 핵심 메커니즘 1개 + 왜 좋아지는가 + 티저 + 마지막 한 문장 지위 헤지), (b) English thread 2-4 message-unit posts (X Premium, no char cap), both behind one Verification Status header. Bold-selection rule: the promo leads with the boldest claim the sources support (selection from the protected surface and landed frames, never fabrication); insurance <=1 status clause per deliverable, isolated as the FINAL sentence of that deliverable (no defensive mid-body narration; examination-process narration 0). Hard grounding rule (safe-claims defense): every factual phrase traces verbatim-consistent to essay-final/publication.md/owner-briefing.md/owner-study-pack.md (comprehension-notes = hook/framing seed, not a freestanding fact quarry); a fact not in those sources is dropped, never fetched. Posting copy is composed by the session's strongest model (model: inherit, never pinned down); grok lane is an opt-in cost mode (--promo-vendor grok). Use when an archived essay needs promo, an X post, share copy, a tweet thread, 프로모, or 홍보 문구. NOT for: long-form essay composition (essay-en-composer), editorial review (editorial-review), thesis design (thesis-architect), Korean full-article adaptation (still dropped; the KR deliverable is a promo post, not an article), or editing essay-final.md (the essay is FINAL)."
context: fork
agent: promo-composer
---

# promo-composer

**Contract:** `contracts/stages/promo.yaml`

Phase 4 Promote. Runs POST-archive against a finished `essays/<id>/` tree and emits one
promo pack. The essay is FINAL: this skill digests it, never edits it, and its findings
never reopen the Compose↔Edit loop.

Promo is the essence of this pipeline's work — the **public translation of the Understand
triad** (problem · solution · effects), not a compression of the finished essay's own
prose. Reader profile: between high-school and undergraduate (고등학생과 학부생 사이).

```
essays/<id>/essay-final.md                 (FINAL; frontmatter: essay_id, closing_posture)
  + publication-package/publication.md    (the paste-ready strip readers actually saw)
  + owner-briefing.md                     (Korean owner briefing; parallel archive contract,
                                           may be ABSENT on older archives)
  + owner-study-pack.md                   (Understand triad: problem · solution · benefits;
                                           may be ABSENT on older archives)
  + comprehension-notes.md                (landed frames from Owner comprehension check;
                                           first-class hook material; may be ABSENT)
  + thesis-trace.md                       (## Signature lines: <=3 protected exact strings)
  + README.md                             (reader_sentence)
  + publication-package/ images + posting-checklist.md   (cover + alt-text lines)
  + optional owner context               (emphasis and timing only, never new facts)
    -> essays/<id>/promo/promo-pack.md
       Verification Status header
       (a) Korean long-form promo post, 400-800자, 발행자 목소리, bold lead
       (b) English thread, 2-4 message-unit posts (X Premium, no char cap), bold hook
```

**Model allocation (owner decision, 2026-07-05; P7 restore 2026-07-12):** the posting
copy — the fenced paste blocks — is composed by the session's strongest model (the agent
declares `model: inherit`; never pin promo-composer to a cheaper model: prose quality is
bounded by the model that holds the pen). The grok CLI lane (`--promo-vendor grok`) is an
**opt-in cost mode**, not the default. Mechanical verification (fact-trace, counts,
hygiene) and the GPT safe-claims+AI-tell judge may be delegated to a cheaper or
cross-vendor instrument; composition may not.

## When to invoke

After the orchestrator archives a run to `essays/<id>/` (Phase 4, on by default for essay
mode), or standalone when the user points at an archived essay and asks for promo, an
X post, share copy, thread, 프로모, 홍보 문구.

## vs essay-en-composer

- `essay-en-composer`: long-form ~2,000-3,500w from `handoff/01-design/`, full `[dddd]`
  citation apparatus, investor-reader altitude.
- `promo-composer`: two short deliverables from the ARCHIVE, zero new facts, zero `[dddd]`
  anchors in output, feed-reader altitude. It translates the Understand triad for the
  public; it performs no analysis of its own.

## The grounding rule (hard): the safe-claims defense

1. **Allowed factual sources**, and the only ones: `essays/<id>/essay-final.md`,
   `essays/<id>/publication-package/publication.md`, `essays/<id>/owner-briefing.md`,
   `essays/<id>/owner-study-pack.md`. `comprehension-notes.md` seeds hooks and framing
   only (landed frames) — it does not expand the factual license beyond those four.
   These carry the loop-corrected phrasings and the frozen triad; treating them as the
   sole quarry is what keeps already-fixed errors dead (rationale + the scrubbed error
   classes: `references/fact-verification.md`).
2. **Every factual phrase traces** to a sentence in those sources. Numbers, dates, names,
   venue words, and verbs of certainty stay verbatim-consistent with the essay's wording
   (an application-era essay says "asks for" and "filed"; the promo never upgrades that to
   "patented" or "owns").
3. **No new factual claims. No memory-written facts. No fetching.** No web search, no
   re-reading the patent, no mining fact-check-log or other handoff internals for facts the
   essay chose not to print. If a fact you want is not in the sources, you drop it. You do
   not fetch it.
4. **The essay is FINAL.** Promo never edits any file under `essays/<id>/` except writing
   `promo/promo-pack.md`. A suspected factual defect noticed while packing goes on the
   header's `suspected_essay_defects` line for the human-post-accept channel
   (revision-notes.md); the affected claim stays OUT of the promo. Promo findings never
   reopen the loop.
5. **Owner context steers, never grounds.** Optional owner input (시의성, channel, timing)
   may adjust emphasis and posting register; a fact the owner supplies that is not in the
   sources is surfaced back as a question, not printed.

## Process

1. **Load the archive.** `essay-final.md` (frontmatter: `essay_id`, `closing_posture`,
   `draft_version`), `publication-package/publication.md`,
   `publication-package/posting-checklist.md`, `owner-briefing.md`,
   `owner-study-pack.md`, `comprehension-notes.md`, `thesis-trace.md`, `README.md`.
   Reject the run if `essay-final.md` or `publication.md` is missing.
   `owner-briefing.md` / `owner-study-pack.md` / `comprehension-notes.md` absent: proceed
   and record `ABSENT` in the header (older archives may lack any of them); do not fail
   the run. When the study pack is present, harvest Problem · Solution · Benefits as the
   compositional spine. When comprehension-notes is present, harvest "Framing that landed"
   as first-class hook seeds.
2. **Harvest the protected surface**: `reader_sentence` (README.md), the `## Signature
   lines` exact strings (thesis-trace.md), the title, the lead ¶1, the closing call,
   `closing_posture`, plus any landed frames from `comprehension-notes.md`. This is the
   entire hook vocabulary: promo hooks compress these lines and landed frames; they do
   not coin new ones.
3. **Audience adapt** per `references/audience-adaptation.md` (essay reader → X feed; KR
   post → the publisher's own Korean followers). Reader altitude: high-school through
   undergraduate — explain the mechanism; do not lecture the patent process.
4. **Voice shift** per `references/voice-shift-from-essay.md`. Optional: invoke
   `voice-canon-lookup` for the `opening-news-event` and closing pattern bodies, the
   pack's only two canon touchpoints.
5. **Select the bold lead** per `references/promo-format.md` bold-selection rule: pick
   the boldest supportable line from the protected surface (or a landed frame) for each
   deliverable's lead; budget insurance as exactly **ONE status/stage hedge sentence
   per deliverable, positioned as the LAST sentence of that deliverable** (process
   narration 0 mid-body — the article hedges, the promo points, then ends with one
   stage caveat).

### Understanding-first compositional shape (KR post AND EN thread)

Both deliverables follow this five-beat shape. It is the public translation of the
Understand triad, not a defensive summary of the essay:

1. **Hook** (서사 훅) — seed from a `comprehension-notes.md` landed frame when one
   exists, else from the protected surface (reader_sentence / signature lines / title /
   lead ¶1 / closing call).
2. **발명의 핵심 메커니즘 하나를 쉬운 그림/비유로** — the triad's Solution component,
   pulled from `owner-study-pack.md` (or essay/publication when the pack is ABSENT).
   One core mechanism; one easy image or analogy. Not a claim chart.
3. **왜 좋아지는가** — the triad's Benefits component. Keep the document's own
   can/may-qualified claims (never strengthen into certainty), but **explain** why the
   improvement follows — 왜 이게 개선인지 설명하라, 매 문장마다 유보하지 말라.
4. **티저 (에세이로)** — point at the essay for the full read (`[ARTICLE-LINK]`).
5. **마지막 한 문장 지위 헤지** — exactly ONE status/stage hedge sentence, as the
   LAST thing in the deliverable. No examination-process narration anywhere in the body.

**Anti-AI-tell duty (explicit; also GPT-judged):** no 3항 병렬 남용 (no parallel-triad
overuse), no 은유 사슬 (no metaphor chains), no 균질 결어 (no homogeneous paragraph
endings), no 직역투 (no translation-ese), no 줄표 (no em-dashes). Prefer one concrete
image over a stack of metaphors; vary paragraph landings; write as if composed natively
in the target language.

**KR register-calque ban (Owner calibration, 2026-07-12):** the subtler failure class is
English-ESSAY rhetoric transplanted into Korean, not word-level translation-ese —
(a) 문서 의인화: an inanimate document as the agent of a pointed action ("명세서가 ~를
짚어 적습니다"). Korean 설명체 treats the document as a location: "명세서에는 ~가 적혀
있습니다." (b) 영어 수사 이식: abstract compound nouns ("성능 논리") and
metaphor-transition sentences ("같은 그림에서 나옵니다"). Transitions go through the
substance itself ("저항이 줄어든다는 주장도 같은 구조에서 나옵니다"), never through a
metaphor. Test each KR sentence: would you say it aloud to a student? If not, recompose.

**KR voice anchors (P8, 2026-07-12):** before composing, read (or receive inlined from
the orchestrator) BOTH: (1) the `promo-kr-*` entries in
`.claude/skills/voice-canon-lookup/voice-canon/` — Owner-approved KR promo posts; match
their cadence the way the essay composer matches the essay canon; and (2)
`references/kr-correction-pairs.md` — the Owner's actual before→after corrections.
The pairs outrank any abstract rule: if a sentence you wrote resembles a ✗ side,
recompose it toward the ✓ side's shape.

6. **Compose the KR long post** (400-800자) per `references/promo-format.md` KR rules
   and the understanding-first shape above. Register per
   `_shared/references/working-dialogue-voice.md`: 건조한 평서문, 과장 배제, 발행자
   1인칭 허용 — 대담함은 문장 선택에서. 기술 어휘는 briefing / study-pack 재사용,
   stance/hedge 문장은 재사용 금지 (hedge lives only in beat 5).
7. **Compose the EN thread** (2-4 message-unit posts; X Premium, no char cap) per
   `references/promo-format.md` thread rules and the same five-beat shape: post 1
   narrative hook (first sentence = collapsed-preview; no insurance), middle post(s)
   mechanism + why-better (one message each), final post call + `[ARTICLE-LINK]` + the
   single closing status hedge as its last sentence. Chars measured and reported, not
   bound. Closing posture of both deliverables agrees with the essay's `closing_posture`
   per `references/closing-posture.md` (firm essay → no open-question close).
8. **Attachment lines** per `references/figure-attachment-policy.md`:
   `publication-package/` images only, `cover-5x2.png` default, 1-2 figures max per
   deliverable, alt text verbatim from `posting-checklist.md`.
9. **Fact-verification pass** on both deliverables per
   `references/fact-verification.md`: per-sentence source trace + Sub-rules 1 (시점
   sequence), 2 (date arithmetic), 3 (quote anchor preservation).
10. **Hygiene self-check** (mechanical, self-run; the pack sits outside `run_gates.py`):
    - em-dash 0 and bold 0 across the whole pack; emoji <=1 total (the KR post closing
      slot only, 0 is fine); hashtags 0; cashtag only if the essay itself used one.
    - banned terms 0 against `_shared/scripts/banned_terms.txt` (literal lines plus `re:`
      regexes); Tier-2 judgment tells checked per `_shared/references/anti-ai-writing.md`.
    - counts: KR long post 400-800자 (공백 포함, `[ARTICLE-LINK]` = 23자), each EN post
      chars measured (no 280 bound; link slot = 23); bold-selection line (lead source +
      insurance count per deliverable); confirm the status hedge is one final sentence
      per deliverable (not interleaved mid-body).
11. **Emit** `essays/<id>/promo/promo-pack.md` (create `promo/` if needed). Every
    Verification Status line carries a measured number or PASS. Revisions overwrite in
    place with `promo_version` bumped.

## Pre-conditions

- `essays/<id>/essay-final.md` and `essays/<id>/publication-package/publication.md` exist;
  the run is accepted (double-clean or an explicit CAP HIT ship). Promo never runs on a
  mid-loop draft.
- `essays/<id>/thesis-trace.md` and `README.md` present in the archive.
- `essays/<id>/owner-briefing.md` expected (tracked archive deliverable per the
  owner-comprehension overhaul; contract landing in parallel). Absence is tolerated and
  recorded, not fatal.
- `essays/<id>/owner-study-pack.md` and `essays/<id>/comprehension-notes.md` expected on
  post-P7 archives (understanding-first sources). Absence on older archives is tolerated
  and recorded `ABSENT`, not fatal — same posture as `owner-briefing.md`.

## Post-conditions

- `essays/<id>/promo/promo-pack.md` exists: frontmatter + Verification Status header +
  three fenced paste-ready blocks + attachment metadata lines.
- All budgets met and MEASURED (자수, words, chars printed in the header).
- Every factual phrase traceable to the licensed sources; dropped-fact list in the header
  (usually `none`).
- Digest posture agrees with `closing_posture`.
- Everything else under `essays/<id>/` byte-identical to before the run.

## Output skeleton (condensed; full contract in references/promo-format.md)

```markdown
---
essay_id: etched-0378175-memory-in-writing-r2
essay_source: essays/etched-us20240378175-r2/essay-final.md
closing_posture: firm
promo_posture: D
promo_version: 2
owner_briefing: read
---

# Promo pack: etched-us20240378175-r2

=== Verification Status (promo-composer, promo-pack) ===
sources: essay-final.md (draft_version 6) + publication.md + owner-briefing.md
fact_trace: PASS (every factual phrase mapped; dropped facts: none)
subrules: 1 sequence PASS / 2 arithmetic PASS / 3 anchors PASS
bold_selection: KR lead = signature line 2 압축, insurance 1 clause; P1 = reader_sentence 압축, insurance 1 clause (final post); process narration 0
kr_long: 612자/400-800, 4 단락, 아티클 포인터 있음, 의문형 0, 느낌표 0
thread: 3 posts, message-unit (X Premium, no char cap), 439/775/552 chars, link slot in final post
hygiene: em-dash 0, bold 0, emoji 0/1, hashtags 0, banned terms 0
attachments: cover-5x2.png (KR post, post 1), alt verbatim from posting-checklist.md
suspected_essay_defects: none
=== Deliverables ===

## 1. Korean long-form promo post (X, 400-800자)

<fenced text block, paste-ready, ends with article pointer + [ARTICLE-LINK]>

- 자수: 612 (공백 포함, [ARTICLE-LINK]=23자)
- attach: publication-package/cover-5x2.png
- alt: "<cover alt, verbatim from posting-checklist.md>"

## 2. English thread (2-4 message-unit posts)
...
```

## Out of scope

- Long-form composition (Phase 2 `essay-en-composer`); editorial review (Phase 3
  `editorial-review`); thesis design (Phase 1 `thesis-architect`).
- Korean full-article adaptation (v1 `tech-essay-ko-pub` stays dropped; the KR deliverable
  here is a 400-800자 promo post that INVITES to the article, not an article adaptation).
- The EN digest (dropped in v3, owner decision 2026-07-05; its paragraph craft lives on
  in the KR long post spec).
- Editing anything under `essays/<id>/` except writing `promo/promo-pack.md`.
- Reopening the inner loop or the self-audit; re-running gates on the essay.
- First-instance fact verification (Phase 1 fact-check-log + Phase 3 pass 3 already did
  it; promo only reuses corrected text).

## References

- `references/promo-format.md`: the promo-pack.md contract (fenced paste blocks as the
  strip boundary), the bold-selection rule, KR long-post rules, thread rules,
  counting methods, Final Checklist, v2→v3 deltas.
- `references/fact-verification.md`: the safe-claims rationale + per-sentence trace
  procedure + Sub-rules 1/2/3 + posting-time cross-check + KR quote handling.
- `references/closing-posture.md`: the 4-posture taxonomy + the closing_posture agreement
  rule + Pattern-8 hedge avoidance.
- `references/audience-adaptation.md`: essay reader → X general public; expand / compress /
  drop / preserve lists; KR-post audience.
- `references/voice-shift-from-essay.md`: register shift, attribution density, markdown
  weight, KR register pointer to working-dialogue-voice.md.
- `references/figure-attachment-policy.md`: publication-package/ images, cover-5x2.png
  default, swap criteria, alt-text lines.
