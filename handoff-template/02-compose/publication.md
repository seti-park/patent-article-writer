<!--
  TEMPLATE: handoff/02-compose/publication.md
  Produced by: essay-en-composer (Phase 2 Compose, Step 7) via the strip pipeline
  Schema source: essay-en-composer/references/strip-pipeline.md

  This is essay-draft.md AFTER stripping:
    - YAML frontmatter removed
    - inline [^footnote] markers removed from body prose
    - the # Footnotes definitions block removed (boundary = "# Footnotes" heading)
  And PRESERVING:
    - all body prose + headings + figure italic captions
    - inline [xxxx] patent cites (these are NOT footnotes; they stay)
    - the # Sources block (sits above the stripped # Footnotes heading)

  This is the reader-facing artifact SETI pastes into X Articles. Example content:
  Tesla RCM / 70ms patent (same essay as essay-draft.md, post-strip).
-->

# Tesla Filed the 70ms Airbag Patent Before It Announced the 70ms Airbag

![FIG. 1: the predictive restraint architecture.](figures/fig-01.png)

*FIG. 1: the predictive restraint architecture. The vision sensor array (416) feeds a pre-impact prediction to the vehicle control unit (414), which arms the airbag module (430) over the safety bus (420) before an accelerometer registers the crash.*

## When the Announcement Arrived Late

This spring, Tesla described its predictive restraint system as an unprecedented
pre-impact response. The description was accurate. It was also roughly eleven months
late: the patent that explains the response had already been on file since October
2024. The announcement did not reveal the architecture. It caught up to it.

## What the Patent Actually Routes

The restraint-control module does not wait for the crash. The vision sensor array
(416) computes a pre-impact prediction and routes it to the vehicle control unit
(414), which arms the airbag module (430) before an accelerometer would register
the impact. The patent is explicit that this is not a backup channel: it describes
"the vision sensor providing pre-impact prediction to the airbag controller" [0016],
and notes that "the vision sensor functions as a predictive input rather than a
redundant sensor" [0017].

*FIG. 2: the vision sensor array.*

## The Baseline the Number Hides

Conventional restraint systems are reactive by construction: "conventional
accelerometer-based systems respond only after the collision has begun" [0014].
Industry accelerometer-based ECUs reach a deployment decision within roughly ten
milliseconds of crash detection (Bosch technical specs). Tesla's architecture moves
that decision upstream of the crash entirely: the patent states the "deployment
decision is made approximately 70 milliseconds before traditional accelerometer-based
systems would respond" [0024]. Both figures describe the same thing, a pre-deployment-
decision latency, which is what makes the comparison fair rather than rhetorical.

*FIG. 4A: pre-impact decision timing. The vision-path decision lands ~70 ms ahead of the accelerometer baseline.*

## What the Filing Date Reframes

The lead time is not free of cost, and the patent bounds it: "the false-positive
deployment rate remains below 0.1 percent across the validation set" [0029]. Read
against the filing date, the announcement stops being a product reveal and becomes a
confirmation. The architecture that made the 70-millisecond claim possible was
committed to silicon and to the patent record before the public ever heard the number.

## What the Number Was Always Going to Confirm

The next continuation filing, or the next safety disclosure, will either carry the
same vision-first decision path or quietly walk it back. The patent is the more
durable record. Companies announce when it is convenient; they file when they have
already decided.

# Sources

## Patents
- US 2026/0125022 A1, "Predictive Airbag Deployment using Vehicle Vision Data," Tesla, Inc., priority 2024-10-23, published 2026-04-23, inventors: Jane A. Roe, Marcus Lindgren, Priya Nair.

## Official statements
- Tesla, "Predictive Restraint" announcement (2026-03). https://www.tesla.com/blog/predictive-restraint-2026

## Technical specs
- Bosch airbag ECU spec sheet. https://www.bosch-mobility.com/en/solutions/passive-safety/airbag-control-unit/
