# Implementation notes — running decision log

A human-readable memory file for decisions made while editing shipped essays or the
pipeline outside a full run. Newest entry first. Each entry records: what was observed,
the root-cause analysis, what was changed and NOT changed (with reasons), and what the
next run should do differently. The machine-readable twins live in
`meta/findings-ledger.jsonl` (pattern_tag rows) and `meta/improvement-proposals/`;
this file is where the reasoning survives in full sentences.

---

## 2026-07-05 (3) — 윤문: no stage ever held the pen for plain language (v6 → v7, new Phase 3.7)

### The observation (owner comment)

The accepted essay's sentence structure and word choice still read a notch above the
general reader — accurate, well-structured, energetic, and slightly hard. Examples:
"the compute" as a noun, "an exchange" for a switch, "assignees", "the structure being
multiplied here", "operational homework", "the applicant electing to call it",
"no-switch limitation".

### Root cause

Every reviewer reviews; nobody smooths. Pass-5 checks comprehension against
reader-profile but only files findings; the composer optimizes for the argument; by the
time the text is accepted, no stage has the JOB of final plain-language polish, and any
ad-hoc smoothing would risk grounding drift with no safety net.

### Decisions taken

- New **Phase 3.7 prose-polish (윤문)** stage: after self-audit DRY, before archive.
  Surface-only jurisdiction (split, simplify, gloss; never re-state facts, never
  re-hedge); signature lines byte-protected; every edit logged (`## polish` blocks);
  gates re-run zero-new; drift verification old-vs-new by a cheap grounding-verifier
  instrument; pen = session's strongest model (same owner rule as composer/promo).
- First run on etched-r2: 17 edits attempted, 15 applied, 2 reverted by the drift
  check (an un-hedged caveat and a term-of-art swap) — the safety net earned its keep
  on round one. v7, gates clean.
- Deliberately NOT in the inner loop: polishing mid-loop would churn against fresh
  reviewers; polishing after acceptance, with mechanical tripwires, converges.

### What the next run should do differently

1. Polish is a stage, not a virtue sprinkled everywhere: let compose argue, let edit
   verify, and let 3.7 smooth — with the drift check as the license to touch prose.
2. Watch the polish-notes classes: a register mistake that recurs across runs should be
   promoted upstream into the composer's voice stack so the text is born plainer.

---

## 2026-07-05 (2) — promo pack: safe-harbor overweight + format/channel mismatch (promo v1 → v2, contract v3)

### The observation (owner comments)

(1) The promo overweighted examination process and safe-harbor hedging — the KR post's
"다만 최종거절 후 RCE로 심사가 계속 중이라 ..." sentence and the digest's prosecution
paragraph. Readers want the bold claim in the promo; the article is where it gets priced.
(2) Format mix was KR short + EN digest + EN thread; the publisher's primary channel is
Korean, so the right mix is KR LONG + EN thread. (3) The posting copy should be written
by the strongest model (Fable 5), since prose quality is bounded by the pen-holder.

### Root causes

- The v2 KR rule "owner-briefing 문장 표현을 우선 재사용" imported the briefing's
  insurance-laden stance sentences into promo copy — the briefing hedges BY DESIGN
  (owner-comprehension artifact), so sentence-level reuse is a hedge pipeline.
- The v2 digest rule "hedge 강도는 essay 와 동일" made the promo inherit essay v5's
  procedure overweight wholesale.
- Nothing stated who holds the pen for promo copy.

### Decisions taken

- v3 promo contract (promo-format.md rewrite): **bold-selection rule** — lead with the
  boldest supportable protected line; insurance <=1 status clause per deliverable, after
  the beat; process narration 0; hedge inheritance one-way (no overreach, no import);
  briefing reuse vocabulary-only. Deliverables: KR long post 400-800자 + EN thread 3-5
  tweets; EN digest dropped. `promo_posture` replaces `digest_posture`.
- **model: inherit declared load-bearing** for promo-composer (agent frontmatter +
  SKILL + CLAUDE.md): posting copy by the session's strongest model; only verification
  may be delegated.
- Regenerated the etched-r2 pack (promo_version 2) against essay v6: copy authored in
  the main session, verified by a pinned-cheap instrument (counts / hygiene / per-phrase
  fact-trace / sub-rules).
- Grounding rules unchanged: bold ≠ ungrounded — boldness comes from SELECTION.

### What the next run should do differently

1. Promo altitude has a stricter attention budget than the essay: 100% payload + one
   status clause. Point at the pricing, never narrate it.
2. Treat fixed-schema reuse sources as REGISTER-specific: a briefing sentence is owner
   language, not reader language; reuse its nouns, never its stance.
3. The pen rule generalizes: any deliverable a human will actually publish (essay,
   promo copy) is composed on the strongest model; pinned-cheap models are for
   retrieval-shaped verification only.

---

## 2026-07-05 — etched-us20240378175-r2: procedure hijacked the reader's attention (v5 → v6)

### The observation (publisher read, post-publication)

The shipped essay front-loaded patent PROCEDURE — the 3-year examination, the RCE, fees,
liens — and buried the TECHNOLOGY. Predicted reader behavior: engage with the lead,
glaze during the prosecution material, skim or abandon the tech sections that were the
actual payload. Meanwhile `owner-briefing.md` and `promo/promo-pack.md` read fine.
So the defect was essay-body-specific, not a facts problem.

### Root-cause analysis (why the essay went to 삼천포 while the briefing/promo didn't)

1. **The verdict frame became the narrative frame (design stage).** The edition contract
   correctly said a pending application can't support a fence-strength verdict, so the
   verdict must be about what the document IS plus how it's treated (collateral,
   continued prosecution). Phase 1 then let that VERDICT frame set the STORY structure:
   the one-line spine ends on "a bet the company keeps paying to convert into an asset",
   the Q7 hook anchors on prosecution status, and the spine→section trace placed
   prosecution/money at the lead (¶2–3) AND §5 AND the closing. Procedure became the
   plot; the invention became the middle.
2. **A per-item budget eroded through echoes (compose + edit stages).** The user
   decision in essay-context was explicit: "prosecution status: exactly ONE label
   sentence, no battle narrative." The letter of the rule held (one full-detail status
   sentence), but the MOTIF metastasized: "expensive to keep alive", "paid at every
   step", "an RCE is, in substance, a fee paid to keep arguing", "the spending is
   repeated", "keeps paying" — each individually grounded and reviewable, none a status
   label per se, so every pass approved every instance. Nothing counts the aggregate.
3. **No attention-budget instrument exists.** gate_surface checks the title length, the
   first body sentence, and a defensive-open lexicon in the first two sentences — point
   checks at the very top. The cold reader checks stop-points — but a paper-trail hook IS
   hooky, so the lead passed; the failure was the procedural pile-up in ¶2–3 and §5,
   which sits between every existing check. Nothing measures time-to-technology or the
   procedural share of prose.
4. **Why briefing/promo survived:** fixed schemas. The owner briefing gives technology
   and status separate numbered slots; the promo formats (≤280자 / ~300 words) force
   selection of the punchiest content, which is the tech + the date beat. Long-form is
   the only artifact where attention allocation is unconstrained — so it is the artifact
   that needs the budget rule.

### Decisions taken (and not taken)

- **Restructured tech-first, verdict intact.** New title ("Etched's First Patent Filing
  Asks to Delete the Memory Switch") and new lead: the switch-deletion idea + its stated
  effect ([0043]/[0016]/[0044]/[0045]) FIRST, discovery beat second, compact two-sided
  call third. §5 compressed to: the ONE mandated label sentence + full-strength steelman
  + record-of-behavior + one merged lien paragraph + the family note.
- **Cut, with reasons:** the RCE explainer paragraph (procedure lecture beyond the label
  budget), the grant-to-lien three-day timing paragraph (inference-labeled procedure
  trivia), the compiler-applications aside, the repeated-spending motif (kept once, in
  the closing signature line, where it earns its place).
- **Kept, deliberately:** the steelman at full strength (contract-required, and it is a
  THIS-application objection); both liens (both-or-neither evidence rule); all three
  protected signature lines byte-intact; the firm closing unchanged.
- **Verified:** 14/14 gates PASS with zero findings (warns included) after the edit;
  publication.md re-stripped (2,906 words); posting-checklist updated.
- **Not done:** no re-run of the inner loop (this is the human-post-accept channel; the
  deltas are in `revision-notes.md` and normalized to the ledger as
  `procedure-overweight-lead`, goal 5).

### What the next run should do differently

1. **Lead order rule (design + compose):** for verdict editions, the lead answers
   "what does it do and what does that change" BEFORE "what does it cost / where does it
   stand". The discovery/status beat may frame, never dominate: procedure gets at most
   one clause in the lead beyond the required call.
2. **Motif budget, not just sentence budget:** when a brief says "exactly one label
   sentence", treat restatements-in-other-words (spend/fee/keep-alive language) as
   drawing on the same budget. The composer's revision mode and pass-6 should count the
   motif across the whole essay.
3. **Structural home for procedure:** prosecution/finance material lives in ONE pricing
   section (plus the closing's verdict), never distributed across lead + body + closing.
4. **Instrument (BUILT 2026-07-05, user-authorized):** `gate_surface` SURF-005 (lead
   procedure-narration sentences > 1) + SURF-006 (spend-motif > 4 in prose), both
   warn-only, with the v5 essay preserved as the `procedure-overweight` regression
   fixture; plus pass-6 6I, spine `payload` tags, and cold-reader early-drag
   auto-escalation. Full application record:
   `meta/improvement-proposals/2026-07-05-procedure-attention-budget.md`.
5. **Schema-envy heuristic:** when the briefing/promo read better than the essay, suspect
   attention allocation, not facts — the fixed-schema artifacts are the control group.
