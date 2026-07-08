# Figures rationale — compose placement

Composer's actual placement decisions (vs Phase-1 figure-rationale intent).

| Figure | Placement | Render mode | Caption (as drafted) |
|---|---|---|---|
| FIG. 5 | Cover, directly under the title | image-plus-caption (header) | *FIG. 5A-5AD, the reconfiguration in the patent's four phases [0046]: 5A (start), then 5G, 5L, 5W, 5AD ... one embodiment of the locked step.* |
| FIG. 1 | §"What The Body Forces", inline reference in first sentence | reference-only (no image block in draft) | establishing the body; referenced as "(Fig. 1)" |
| FIG. 3 | §"What Claim 1 Locks", after the interpretation paragraph | caption-only-italic | *FIG. 3, [0033]: the escalation the claim locks, including the clearance check that gates the reconfiguration.* |
| FIG. 6 | §"Locked, Open, And Pinned", end of section | caption-only-italic | *FIG. 6, [0047]: the kneel is one open embodiment of the locked instruction to lower the center-of-gravity, a compact pose that collapses predictably on a fault.* |

Notes:
- All four selected figures (1, 3, 5, 6) are referenced; no off-plan figures (figure-use gate PASS).
- FIG. 5 is referenced both as the cover (image-plus-caption) and inline in §"Locked, Open, And
  Pinned" ("the patent walks that fold frame by frame across FIG. 5"), per the cover + inline
  decision. A bare `FIG. 5` token is present so the figure-use regex registers it (lettered
  `FIG. 5A` panels do not parse).
- Captions carry paragraph anchors ([0033], [0047]) per x-articles caption convention.
- Image files for publication: figures/fig-05-sequence.png (cover strip) + fig-01.png, fig-03.png,
  fig-06.png; full-sequence composites fig-05AF/GO/PX/YAD also in figures/.
