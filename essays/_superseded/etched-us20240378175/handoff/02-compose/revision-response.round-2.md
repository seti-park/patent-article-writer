# Revision response — round 2

draft_version: 3

## r2-F1

- disposition: applied
- change: FIG. 7 caption re-anchored to what the two time marks MEAN instead of treating
  them as interval bounds (grounding fix priority: anchor — the reviewer's quoted
  [0056]/[0057] evidence and the drawing itself are the anchor; no hedge added, no new
  [dddd] cite needed). Re-verified against fig-07.png directly before rewriting: the six
  stage bands span the full time axis (0 to X), Time B sits left of X/2 at the stall bar,
  Time A sits right of X/2 where the MLP output/hidden overlap is drawn — so the old
  caption's "between Time A and Time B" both misstated the span and inverted the axis
  order. The reviewer's suggested rewrite adopted with one equivalence edit: its single
  long clause chain was split at the semicolon into two sentences (keeping body prose
  semicolon-free per the pass-1 scope note); semantics identical.
  - Before: "*FIG. 7: pipelining one array row. Attention queries, keys, and values,
    projection, and the MLP layers follow each other through the row between Time A and
    Time B. The only idle gap is the layer-normalization stall [0057].*"
  - After: "*FIG. 7: pipelining one array row. Attention queries, keys, and values,
    projection, and the MLP layers follow each other through the row, and at Time A a new
    computation has already entered while the previous one drains. The only idle gap is
    the layer-normalization stall, marked at Time B [0057].*"
  - Grounding trace: stage sequence + enter-before-drain = invention-summary core-mechanism
    step 6 (same source as the body sentence the reviewer confirmed accurate); stall +
    [0057] = q-0057-1; Time A = pipelining overlap and Time B = stall per the reviewer's
    quoted [0056]/[0057] spans in edit-log.round-2.md (the fenced patent source for this
    fix) and the drawing.
- location: §5, FIG. 7 caption (draft line 94)

## Low findings sweep (r2-F2, r2-F3)

- disposition: applied (both, with the reviewer's rewrites).
  r2-F2: §4 "The header drawing, FIG. 5, is the whole argument in one picture: ..." ->
  "FIG. 5 is the whole argument in one picture: ..." (layout self-reference dropped; the
  FIG. 5 figure token survives, gate_figure_use re-checked).
  r2-F3: §7 para 2 "That objection survives contact..." -> "The crowded-field objection
  survives contact and changes nothing about the date." (referent named once; the §6
  steelman IS the crowded-field objection — "the field was already crowded when the
  founders filed"). No other §7 text touched; verdict wording, guard, and posture
  unchanged.

## Volunteered changes (beyond findings)

- figures-rationale.md synced: FIG. 7 "Caption (as written)" updated to the new caption
  and its decision note now records the Time A/Time B semantics; FIG. 5 decision note's
  embedded quote of the §4 sentence updated to match the r2-F2 rewrite. No figure moved,
  set still locked.
- thesis-trace.md untouched (no spine→section mapping or word target moved; net word
  delta is +9 inside §5's ±20% band).
- No structural edits (no split/merge/move); all paragraph sentence counts and figure
  tokens re-checked unchanged. No other prose moved — §7 verdict paragraphs 1, 3, and 4
  are byte-identical to draft_version 2.

---

## Orchestrator addendum — carried finding_id accounting (round 2 transition)

**Author:** orchestrator (loop policy). The round-2 revision applied r2-F1..F3 only, because
those were round 2's findings. The r1-F1..F10 ids also appear in round 2's edit-log — inside
its `carried_finding_rulings` verification blocks (`prior_severity:` notation) — where the
round-2 reviewer verified every one of them as landed-and-closed with current-text quotes.
They required no revision at this transition. For the mechanical id-continuity record:

| finding_id | status at round-2 transition |
|------------|------------------------------|
| r1-F1, r1-F2, r1-F3, r1-F4, r1-F5, r1-F6, r1-F7 | applied in revision round 1; closed-verified by the round-2 reviewer (disposition-verification table, current-text quotes) |
| r1-F8, r1-F9, r1-F10 | lows, applied in revision round 1; closed-verified by the round-2 reviewer |

No finding_id was dropped: every r1 id is closed at round 2; r2 ids were dispositioned above;
r3-F1 was deferred per revision-response.round-3.md and resolved in the self-audit.
