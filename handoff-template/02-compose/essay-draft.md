---
# Verification anchor (Phase 2 Compose output). YAML frontmatter is REQUIRED here
# and is stripped by the strip pipeline when producing publication.md.
essay_id: 044-tesla-rcm-vindication        # stable essay slug
patent_reference: US 2026/0125022 A1        # the subject patent
spine_source: handoff/01-design/thesis-spine.md   # the locked spine this draft executes
draft_version: 1                            # increments each Compose↔Edit loop iteration
mode_used: walkthrough                      # walkthrough | strict-execution | pair
posture_used: measured                      # aggressive | measured | conservative
closing_posture: firm                       # copied from thesis-spine.md; read by gate_hedge (firm | open)
---

<!--
  TEMPLATE: handoff/02-compose/essay-draft.md
  Produced by: essay-en-composer (Phase 2 Compose, Step 7)
  Schema sources: essay-en-composer/SKILL.md "Output format"
                  + references/citation-format.md ([xxxx] inline)
                  + references/x-articles-format-en.md (# Sources 5-category enum)
                  + references/strip-pipeline.md (this file -> publication.md)

  RULES:
    - Inline patent cites are [xxxx], 4-digit zero-padded (e.g. [0024]). Every
      [xxxx] must trace to a Quotable span / Quote anchor in invention-summary.md.
    - Body figures: italic caption only, no image embed (caption-only-italic).
      Header figure: ![](path) + caption (image-plus-caption).
    - External claims are surfaced in the # Sources block (NOT inline footnotes)
      AND trace to a fact-check-log.md Fact ID.
    - # Sources is h1; subheadings are h2 from the 5-label enum ONLY:
        Patents | Papers | Official statements | News & media | Technical specs.
    - # Footnotes (optional) sits BELOW # Sources and is stripped for publication.

  Example content: Tesla RCM / 70ms patent.
-->

# Tesla Filed the 70ms Airbag Patent Before It Announced the 70ms Airbag

<!-- Title: 9-14 words, Title Case, no em-dash. This is Pattern 1 (declarative
     reversal): the title IS the thesis. -->

<!-- Header figure (FIG. 1): image-plus-caption rendering, per figure-rendering.md.
     The header figure IS embedded (unlike body figures, which are caption-only). -->
![FIG. 1: the predictive restraint architecture.](figures/fig-01.png)

*FIG. 1: the predictive restraint architecture. The vision sensor array (416) feeds a pre-impact prediction to the vehicle control unit (414), which arms the airbag module (430) over the safety bus (420) before an accelerometer registers the crash.*

## When the Announcement Arrived Late

<!-- §1 Lead. Voice canon: opening-corporate-event. Carries the corporate-narrative-
     friction hook. No patent claim is advanced here (framing only), so no [xxxx]. -->
This spring, Tesla described its predictive restraint system as an unprecedented
pre-impact response. The description was accurate. It was also roughly eleven months
late: the patent that explains the response had already been on file since October
2024. The announcement did not reveal the architecture. It caught up to it.

## What the Patent Actually Routes

<!-- §2 Architecture. Axis 1 claim anchor + mechanism. Reference numbers (NNN) from
     invention-summary Reference number table; [xxxx] anchors from Quotable spans. -->
The restraint-control module does not wait for the crash. The vision sensor array
(416) computes a pre-impact prediction and routes it to the vehicle control unit
(414), which arms the airbag module (430) before an accelerometer would register
the impact. The patent is explicit that this is not a backup channel: it describes
"the vision sensor providing pre-impact prediction to the airbag controller" [0016],
and notes that "the vision sensor functions as a predictive input rather than a
redundant sensor" [0017].

*FIG. 2: the vision sensor array.*

## The Baseline the Number Hides

<!-- §3 Baseline. Axis 4 baseline-difference + adversarial mitigation (apples-to-
     apples). Patent claims cite [xxxx]; external baseline cites the # Sources entry. -->
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

<!-- §4 Implication. Axis 3 effect anchor -> strategic reframe. Bounds the claim
     with the false-positive figure [0029]. -->
The lead time is not free of cost, and the patent bounds it: "the false-positive
deployment rate remains below 0.1 percent across the validation set" [0029]. Read
against the filing date, the announcement stops being a product reveal and becomes a
confirmation. The architecture that made the 70-millisecond claim possible was
committed to silicon and to the patent record before the public ever heard the number.

## What the Number Was Always Going to Confirm

<!-- §5 Closing. forward_pointer + wider_framing + thesis_recap. No defensive hedging.
     Voice canon: closing-forward-watching-event (residual risk = Acknowledged). -->
The next continuation filing, or the next safety disclosure, will either carry the
same vision-first decision path or quietly walk it back. The patent is the more
durable record. Companies announce when it is convenient; they file when they have
already decided.

# Sources

<!-- h1 heading. Subgrouped (4+ entries across 2+ categories => all-or-nothing
     subgrouping). h2 subheadings drawn ONLY from the 5-label enum. No descriptive
     annotation after a citation. -->

## Patents
- US 2026/0125022 A1, "Predictive Airbag Deployment using Vehicle Vision Data," Tesla, Inc., priority 2024-10-23, published 2026-04-23, inventors: Jane A. Roe, Marcus Lindgren, Priya Nair.

## Official statements
- Tesla, "Predictive Restraint" announcement (2026-03). https://www.tesla.com/blog/predictive-restraint-2026

## Technical specs
- Bosch airbag ECU spec sheet. https://www.bosch-mobility.com/en/solutions/passive-safety/airbag-control-unit/

# Footnotes

<!-- OPTIONAL. Stripped for publication.md (boundary is this "# Footnotes" heading).
     Use for figure-asset notes or non-Sources context. Omit the whole block if
     unused. -->
[^fig-4a]: FIG. 4A cleaned asset stored at figures/fig-04a.png for X Articles upload at publication time.
