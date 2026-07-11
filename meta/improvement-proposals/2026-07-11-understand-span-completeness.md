---
proposal_id: 2026-07-11-understand-span-completeness
created: 2026-07-11T14:10:00Z
status: recommended-apply
lever: reference-edit
goal: "1"
root_cause_stage: design
root_cause_artifact: thesis-architect/references/quote-anchor-conventions.md (consumed by patent-understand for invention-summary Quotable spans)
recurrence_count: 2
confidence: high
triggering_findings:
  - essay_id: tesla-us20260196678-hemmed-tabless, iter: 1, finding_id: r1-F4, pattern_tag: quotable-span-scope-clip
  - essay_id: tesla-us20260196678-hemmed-tabless, iter: null (self-audit), finding_id: SA-2, pattern_tag: quotable-span-scope-clip
---

## Problem

The composer fence (invariant 3: **compose never reads raw patent**) makes Quotable-span
fidelity load-bearing: a span clipped mid-sentence at a scope boundary poisons every
downstream stage, and no downstream stage can see past the clip. Two same-mechanism
instances in ONE run, both ending mid-sentence exactly where a qualifier begins:

1. **r1-F4 (HIGH, grounding hard-gate FAIL, cost a full revision round).** `q-0038-1`
   clipped `[0038]` at "...addition of foil material", dropping the second half —
   `or the subtraction of foil material (e.g. "flags")`. The fenced composer, unable to
   see that the patent itself names "flags", wrote a false steelman ("The document does
   not name flags..."); the thesis-spine's adversarial-defense inherited the same clip.
   Fix required a composer revision + upstream re-edit of invention-summary AND spine.

2. **SA-2 (self-audit, post-accept).** `q-0025-1`'s blockquote ends at "debris handling
   device", dropping the purpose clause `to eliminate foil near the core and/or can
   edges, and/or exhaust systems for all of these devices`. Unclipped, the patent
   disclaims the devices *for edge-foil elimination*; clipped, it reads as absolute
   machine deletion — the broader reading the title, §1 header, and lead rode. This clip
   **survived four review rounds**: round-2 pass-3 saw it and accepted it ("an unused
   strengthening anchor, not a defect"); only the blind self-audit (A-3 + B-2, multi-vote
   agree) caught the scope consequence. Restoring the clause also *strengthened* the
   essay's own mapping — the clip hurt in both directions.

Both times the dropped half **changed the available reading** (once against the essay,
once toward overbreadth). The round-1 edit-log itself named the class:
"clipped-quotable-span defeating the composer's fence". The existing convention text
treats mid-sentence clipping as a length/usability suggestion ("If a passage is too long
to be useful as one quote, split into multiple anchors ... rather than excerpting
mid-sentence") — not a checkable rule, and it does not cover *end-clipping* at all
(Disallowed normalizations bans only mid-quote ellipsizing).

**Promotion rationale at recurrence 2:** below RECUR_THRESHOLD=3 by record count, but
promoted cost-weighted — one instance breached a hard gate and cost a full inner-loop
round; the other evaded the entire inner loop; and the class defeats a hard invariant
by construction (the fence guarantees nobody downstream re-reads the source sentence).
Prior cousins (`anchor-offbyone` fixed-at-source 2026-06-26; `phase1-nonquote-label-drift`
2026-07-05) show Phase-1 extraction defects recur as a family.

## Proposed change (exact diff)

**File: `.claude/skills/thesis-architect/references/quote-anchor-conventions.md`**

(1) In `## Verbatim discipline`, after the existing paragraph
"If a passage is too long to be useful as one quote, split into multiple anchors with
sequential `<seq>` rather than excerpting mid-sentence." — replace that sentence with:

```markdown
If a passage is too long to be useful as one quote, split into multiple anchors with
sequential `<seq>` rather than excerpting mid-sentence.

## Span completeness (scope-clip rule)

A span that starts or ends mid-sentence is a **scope-clip risk**: the dropped half can
carry a qualifier (purpose clause, exception, "or the ..." alternative, "in some
embodiments" hedge) that changes what the quoted half licenses. Because Phase 2 is
fenced from patent.md, nobody downstream can see past the clip — the span IS the
sentence as far as the composer knows. Two field cases: a clipped [0038] span made the
patent's own "flags" naming invisible (grounding hard-gate FAIL); a clipped [0025] span
turned a purpose-scoped device list into absolute machine deletion (caught only
post-accept).

Rule — every Quotable-span / Quote-anchor-table entry MUST satisfy one of:

1. **Sentence-complete**: the span ends at a sentence boundary of the source paragraph
   (terminal `.` `!` `?`, optionally inside a closing quote/parenthesis), and begins at
   one (or at the paragraph start).
2. **Clip-noted**: the entry carries an explicit clip note naming the dropped words:
   `clip_note: drops "<first ~10 words of the omitted remainder>..." — scope-neutral
   because <one-line reason>`. A clip note asserting scope-neutrality over a dropped
   qualifier (purpose clause / exception / alternative) is invalid — extend the span or
   split per-sentence instead.

Mechanical self-check (understand stage, before freeze): for each span, locate it in
patent.md; if the character run from span-end to the sentence's true end is non-empty,
the entry requires a `clip_note`. Same check at span-start. The grounding-verifier lane
prompt SHOULD re-verify span ends against patent.md as a second leg.
```

(2) In `## Disallowed normalizations`, append one bullet:

```markdown
- End- or start-clipping a sentence without a `clip_note` (see "Span completeness") —
  the scope-clip variant of ellipsizing
```

**File: `.claude/skills/patent-understand/SKILL.md`** — in the invention-summary output
step (the line "Quotable spans + quote anchor table (verbatim; `quote-anchor-conventions.md`)"),
append: "— including the **span-completeness (scope-clip) rule**: sentence-complete spans
or explicit `clip_note`, mechanically self-checked against patent.md before freeze."

## Why this lever

reference-edit is the cheapest lever that fixes the class at its origin. A gate cannot
do this alone: gate_quotes verifies the *essay* against the spans, and the spans are the
corrupted source of truth — the check must run at extraction time against patent.md,
which only the understand stage (and the verifier lane) may read. The mechanical
self-check is specified so a later gate-promotion (an understand-stage span checker
script) can follow if the class recurs after apply.

## Regression expectation

No gate or fixture touches quote-anchor-conventions extraction rules; `meta/regression.py`
must stay green (gate tests + fixtures unchanged). Field check on this run's corpus: the
corrected q-0038-1 and q-0025-1 entries are sentence-complete under the new rule; every
other span in `handoff/00-understand/invention-summary.md` was byte-verified
clause-boundary-clean by rounds 3-4 (the [0047] clip stopping before the source's typo
zone would need a `clip_note` — a correct, intended flag).
