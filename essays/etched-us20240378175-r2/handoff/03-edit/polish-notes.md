# Polish notes — etched-0378175-memory-in-writing-r2 (Phase 3.7 윤문, 2026-07-05)

> First run of the prose-polish stage (owner request 2026-07-05: 대중 독자를 위한 문장·표현
> 다듬기). Applied to the archived essay via the human-post-accept channel: v6 → v7
> (draft_version 7). Pen: session's strongest model (main session). Jurisdiction per
> `prose-polish/SKILL.md`: surface-only; facts, numbers, dates, names, [dddd] anchors,
> quoted spans, blockquotes, verbs of certainty, stance, Sources, and the three declared
> signature lines untouched (signature lines verified byte-identical). Gates re-run after
> editing: 14/14 PASS, zero findings (warns included). Every edit below: before / after /
> why-plainer.

## polish
before: Between an AI accelerator's math units and the memory that feeds them, chip designers typically place a switch, an exchange that lets the compute reach the whole of the memory [0043].
after: Between an AI chip's math units and the memory that feeds them, designers typically place a switch, a piece of routing hardware that lets the chip reach all of its memory [0043].
why-plainer: "accelerator" (trade term) → "AI chip"; "the compute" as a noun and "an exchange" are engineer-register abstractions → concrete "routing hardware" + "the chip".

## polish
before: The thread that announced Etched's stealth exit is a corporate telling:
after: The thread that announced Etched's stealth exit is the company telling its own story:
why-plainer: "a corporate telling" is a compressed abstraction; spelled out as an ordinary clause.

## polish
before: which is the scale a large model's parameters occupy.
after: which is the space a large model's parameters take up.
why-plainer: "scale ... occupy" → everyday "space ... take up"; same referent ([0018] gloss).

## polish
before: A systolic array, the structure being multiplied here, is a grid of small arithmetic units
after: A systolic array, the building block being copied here, is a grid of small arithmetic units
why-plainer: "the structure being multiplied" reads as math-on-structures; "building block being copied" names the actual relationship (many identical arrays).

## polish
before: The wiring half of that story, the part Etched has since gotten granted, was read separately in a companion analysis of US 12,361,091 B1.
after: The wiring half of that story, the part Etched has since gotten granted, has a companion analysis of its own (US 12,361,091 B1).
why-plainer: agentless passive "was read separately" → plain possession; same cross-reference.

## polish
before: exposes its capacity through independent channels, and "the different channels 510 cannot communicate with each other" [0043]. So designers put an exchange in the middle:
after: delivers its capacity through independent channels, and "the different channels 510 cannot communicate with each other" [0043]. So designers put a switch in the middle:
why-plainer: "exposes" is API-register; "an exchange" renamed to the concrete "switch" the following blockquote names.

## polish
before: [0044], the top of the package to the bottom.
after: [0044], from the top of the package to the bottom.
why-plainer: elliptical apposition → complete prepositional phrase.

## polish
before: The description's twin sentence carries the whole design in one breath:
after: The description says the same thing in one long sentence:
why-plainer: "twin sentence" + "in one breath" are two figures stacked; replaced with the literal statement.

## polish
before: A second independent claim seeks the weight-streaming arrangement itself:
after: A second independent claim asks for the weight-streaming setup itself:
why-plainer: "seeks ... arrangement" → the essay's own plain application-era verb "asks for" + "setup"; certainty level unchanged.

## polish
before: That absence carries one standing caveat: applications younger than 18 months can exist unpublished and unseen.
after: That absence comes with one standing caveat: patent applications stay unpublished for their first 18 months, so newer filings can exist unseen.
why-plainer: the 18-month rule stated as a rule (why unseen) instead of a compressed consequence; same fact, same scope.
REVERTED: drift verification verdict MEANING-CHANGED — the rewrite dropped the modal "can exist" for a flat universal rule, an un-hedge, which the polish jurisdiction forbids. Original sentence restored verbatim.

## polish
before: The last drawing is operational homework. FIG. 7 charts one row of the combined array pushing a transformer layer through in batches [0053], [0055], and none of what it shows is claimed anywhere. It is the description demonstrating that the giant array can be kept busy.
after: The last drawing tackles a practical worry, whether a machine this large can be kept busy. FIG. 7 charts one row of the combined array pushing a transformer layer through in batches [0053], [0055], and none of what it shows is claimed anywhere. It is the description showing its work.
why-plainer: "operational homework" decoded on first contact; the kept-busy point moves to the topic sentence where the reader needs it.

## polish
before: with Intel, IBM and Rambus among the assignees: a crowded field.
after: with Intel, IBM and Rambus among the companies behind them: a crowded field.
why-plainer: "assignees" is registry jargon; "companies behind them" preserves the ownership relation.

## polish
before: The examiner has assembled eight references against this application, drawn from multi-node machine-learning acceleration, hybrid parallelism and neural-network accelerator architectures, with Intel, IBM and Rambus among the companies behind them: a crowded field.
after: The examiner has assembled eight references against this application, spanning multi-node machine-learning acceleration, hybrid parallelism and neural-network accelerators, with Intel, IBM and Rambus among the companies behind them: a crowded field.
why-plainer: length trim (38 → 34 words) after the assignees swap pushed the sentence past the LONGSENT budget; "drawn from ... architectures" → "spanning ... accelerators", no content change.

## polish
before: the memory idea got a stand-alone independent claim rather than a dependent footnote to the package claim, the applicant electing to call it an invention in its own right.
after: the memory idea got a stand-alone independent claim rather than a dependent footnote to the package claim. Etched chose to call it an invention in its own right.
why-plainer: absolute construction ("the applicant electing ...") split into a plain sentence; "the applicant" named as Etched (same referent).

## polish
before: Both liens are blanket, selecting nothing and saying nothing about any single filing's worth.
after: Both liens are blanket: they cover everything, and they say nothing about any single filing's worth.
why-plainer: "blanket" now glossed by its consequence ("cover everything"); participle chain → two plain clauses.

## polish
before: The no-switch idea is authentically the founders' own writing, in claim language before there was anything to sell.
after: The no-switch idea is the founders' own writing, in claim language before there was anything to sell.
why-plainer: "authentically" is an intensifier doing no work; the sentence asserts the same thing without it.

## polish
before: If claim 39 and its memory-side siblings emerge with the no-switch limitation materially intact,
after: If claim 39 and its memory-side siblings emerge with the no-switch language materially intact,
why-plainer: "limitation" is claim-drafting jargon the essay never glossed; "language" matches the essay's own recurring "claim language".
REVERTED: drift verification verdict PROTECTED-TOUCHED — "limitation" is a prosecution term of art (the binding requirement, not the wording); "language materially intact" states a different survival test. Original wording restored verbatim.

## verification

- Edits applied: 15 (of 17 attempted; 2 REVERTED by drift verification, marked above —
  the un-hedged 18-month caveat and the limitation-to-language term-of-art swap).
  Paragraph and section order unchanged; no sentence added or deleted except the two
  splits logged above (operational-homework topic sentence, applicant-electing split).
- Protected surface: signature lines 1-3 byte-identical (asserted); all [dddd] anchors,
  block quotes, quoted spans, numbers, dates, names, patent numbers untouched; Sources
  block untouched; verbs of certainty unchanged (asks for / claims / describes register
  intact; "seeks" → "asks for" is the essay's own weaker-or-equal application-era verb).
- Gates after polish: 14/14 PASS, zero findings (warns included). publication.md
  re-stripped: 2,913 words (after reverts).
- Drift verification (grounding-verifier-class instrument, old-vs-new per changed
  sentence): 15 MEANING-PRESERVED; 1 MEANING-CHANGED + 1 PROTECTED-TOUCHED, both
  reverted per contract; whole-file protected surface verified (signature lines 3/3
  byte-identical, [dddd] anchors 41/41 multiset-identical, blockquotes and quoted spans
  diff-empty, numbers/names identical except draft_version and the same-referent
  applicant→Etched naming, Sources byte-identical).
