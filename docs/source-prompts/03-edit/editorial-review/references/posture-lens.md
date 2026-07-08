# Posture lens

Referenced by editorial-review SKILL.md. Defines 3-tier posture and how it modulates per-pass finding severity.

## What posture is

Each essay's Blueprint `mode_hint` field, or tech-essay-en invocation, names a posture. The posture sets the editorial-review's finding severity lens: the same prose passage produces different severity classifications under different postures.

Posture is not a quality judgment. It is an essay-level intent declaration that scales reviewer sensitivity.

## 3-tier definition

- **aggressive**. Bold framing essay. Forward-looking thesis priority. Voice experimentation acceptable. Factual accuracy stays high severity because it grounds the bold framing.
- **measured** (default). Standard reviewer sensitivity. No tier bias. Factual accuracy + thesis adequacy + voice canon all evaluated against ordinary publication bar.
- **conservative**. Defensive framing essay. Thesis-altering findings are publication-blocking. Voice canon strict. Factual accuracy critical (no hedge tolerance).

Posture unspecified → measured applies.

## Finding severity per posture

The cross-tabulation below sets the default severity classification for each finding type under each posture.

| Posture | Thesis-altering finding | Voice / clarity finding | Factual finding |
|---|---|---|---|
| aggressive | normal severity (framing change welcome) | normal severity | high severity (factual grounds the framing) |
| measured | medium severity | medium severity | high severity |
| conservative | high severity (thesis-altering = publication-blocking) | medium severity | critical severity (factual absolute priority) |

The same thesis-altering finding can be `revise-recommended` under aggressive and `revise-required` under conservative.

## Per-pass posture sensitivity

Not every pass responds to posture the same way. Some passes have rules independent of posture (Pass 4 verbatim mutation), some scale strongly (Pass 3 factual claims), some scale moderately.

| Pass | Posture sensitivity |
|---|---|
| 1 Voice canon | Low. Voice canon violation is judged against canon patterns, posture does not loosen the canon. |
| 2 Redundancy | Medium. Aggressive posture permits intentional reinforcement (repeated thesis anchor for emphasis). Conservative posture enforces strict avoidance. |
| 3 Claim adequacy | High. Conservative = critical severity, aggressive = normal severity. See external-fact-verification.md for posture × tier-source matrix. |
| 4 Paraphrase mutation | None. Verbatim mutation is a hard rule across all postures. Severity = high regardless. |
| 5 Reader perspective | Medium. Aggressive posture permits bold experimentation (delayed thesis, longer setup). Conservative posture enforces strict accessibility. |
| 6 Lead / conclusion strength | High. Conservative posture requires thesis directly anchored at lead + closed at conclusion. Aggressive posture permits thesis-hint variation. |

## Severity transparency in output

The feedback YAML carries two severity fields per finding.

- `severity`: actual severity applied under current posture
- `severity_under_default_posture`: what severity would have been under measured posture, for SETI's quick grasp of why current severity differs

This transparency lets SETI see at a glance which findings shifted because of posture and which would have triggered regardless.

## Quote-integrated paragraph heuristic

When a paragraph contains a direct verbatim quote + surrounding narrative anchor + `[^fact-entry-id]` as a unified structure, the posture lens applies one demotion level for paragraph-length findings only.

- measured + quote-integrated → low severity (down from medium)
- aggressive + quote-integrated → flagging skipped (down from low)
- conservative + quote-integrated → medium severity (down from high)

Rationale: voice rhythm + quote anchor integration justifies extended paragraph length as a SETI rhythm-priority pattern.

## Severity assignment discipline

Severity is inferential judgment. To avoid drift:

- "Publication-blocking" is the bar for high severity. If unsure, escalate to SETI rather than auto-assigning high.
- Severity_under_default_posture must be populated for every finding so the posture differential is auditable.
- Critical severity reserved for conservative posture's factual findings. Other passes max out at high.
