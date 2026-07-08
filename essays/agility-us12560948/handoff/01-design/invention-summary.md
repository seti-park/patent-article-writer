# Invention Summary

## Metadata

- **Patent ID**: US 12,560,948 B2 (granted)
- **Title**: Escalating hazard-response of dynamically stable mobile robot in a collaborative environment and related technology
- **Priority date**: 2024-03-01 (provisional 63/560,583)
- **Filing date**: 2025-02-28 (appl. 19/067,681)
- **Publication date**: 2025-09-04 (US 2025/0278092 A1); **Grant date**: 2026-02-24
- **Inventors**: Kevin Reese, Andrew Abate, Tianyao Chen, Jay Jasper, Ezm Masoud, Brian Kirby, Melonee Wise, Prasanna Velagapudi, Ryan Domres, Todd Lewis, Matteo Parigi Polverini, Yves Georgy Daoud
- **Classification**: CPC G05D1/633, G05D1/495, G05D1/498, B62D57/032, G05D2101/15, G05D2109/12
- **Assignee**: Agility Robotics, Inc.

## 발명 명칭 / 기술분야

Reader-ready framing: a control method for stopping a balancing (dynamically stable) robot
safely when a person comes near, by responding in rising tiers instead of cutting power. 기술분야:
control of dynamically stable mobile robots (humanoid/bipedal and counterparts) in collaborative
environments shared with humans.

## 종래 문제 / 과제

A dynamically stable robot holds its pose only through active control, so disabling it (the
classic industrial E-stop, a power cut) makes it fall rather than makes it safe; the moment a
human reaches in to disable it is itself a hazard. The conventional alternative, caging the robot
(segregation), removes the hazard but also removes the productivity that justifies a humanoid in
the first place. The patent targets the gap between those two failing options.

**Quotable spans:**
- `[0010]`: "Such robots are always falling to some degree during normal operation."
- `[0010]`: "If a dynamically stable robot loses power or otherwise becomes disabled, it collapses."
- `[0012]`: "Ironically, this includes close encounters associated with accessing and activating a disabling feature on such a robot."
- `[0013]`: "segregation strategies for hazard mitigation greatly reduce the productive potential of dynamically stable robots"

## 청구항 분석 — 4-layer core mechanism

### Layer 1 — What (one sentence)

A computer-implemented method that meets a rising human-collision risk in escalating tiers: first
decelerate, then (after checking the surrounding clearance) reconfigure to a lower
center-of-gravity, then bring the robot to a safe operating stop, with each tier triggered by a
later hazard reading whose risk is greater than the one before.

### Layer 2 — How (mechanism)

1. Determine first hazard information about a human (first risk level), via sensors plus
   machine-learning models. `[0024]`
2. Decelerate based on the first hazard information (e.g., ambulating to standing).
3. Determine second hazard information at a later time, with risk greater than the first.
4. Determine clearance information about the surroundings, after decelerating. `[0027]`
5. Reconfigure based on the second hazard information and the clearance information, lowering the
   center-of-gravity. `[0028]`
6. (Dependent, claim 2) Determine third hazard information, then cause a safe operating stop. `[0031]`

**Key components**: computer system; mobile robot (100); hazard information (306a-c); clearance
information (308); reconfiguration to lowered center-of-gravity; safe operating stop.

### Layer 3 — Why novel

- **Relative to prior art**: cited art covers pieces of the space (behavior-based safe
  deployment, an emergent ZMP walking-stop, arm-compliance fall protection) but not the claimed
  combination: a time-escalating response that integrates a clearance check and a
  center-of-gravity-lowering reconfiguration keyed to rising risk.
- **Industry practice contrast**: the established machine-safety answer is an E-stop that cuts
  power; for a dynamically stable robot that produces a fall, so the claimed graduated,
  balance-preserving stop departs from standard practice.

### Layer 4 — Innovation angles

- **angle-escalation**: time-graduated response that trades efficiency for risk reduction in tiers.
  - Evidence paragraphs: `[0014]`, `[0032]`
  - Quote anchor refs: q-0014-1, q-0032-1
- **angle-clearance-aware-reconfig**: checks the surroundings before reconfiguring, since a
  reconfiguration into an obstacle or person can raise risk.
  - Evidence paragraphs: `[0027]`, `[0033]`
  - Quote anchor refs: q-0027-1, q-0033-1
- **angle-cog-lowering**: lowering the center-of-gravity so a fault-state collapse is compact and
  predictable.
  - Evidence paragraphs: `[0028]`, `[0029]`, `[0047]`
  - Quote anchor refs: q-0028-1, q-0029-1, q-0047-1
- **angle-deployability-moat** (investor lens): the claimed safety capability is the gate to
  un-caged deployment in shared human space.
  - Evidence paragraphs: `[0002]`, `[0013]`, `[0042]`
  - Quote anchor refs: q-0002-1, q-0013-1, q-0042-1

## Reference number table

| Number | Label | Paragraphs | Figures |
|---|---|---|---|
| 100 | Mobile robot | `[0016]`, `[0020]`, `[0046]` | FIG. 1, 5, 6 |
| 102 / 104 | Body / torso | `[0017]` | FIG. 1 |
| 106 | Head | `[0017]` | FIG. 1 |
| 110a/b | Arms | `[0017]`, `[0018]` | FIG. 1 |
| 112a/b | Legs | `[0017]`, `[0018]` | FIG. 1 |
| 114a/b | End effectors | `[0018]`, `[0047]` | FIG. 1, 6 |
| 116a/b | Feet | `[0018]`, `[0025]` | FIG. 1 |
| 200 / 350 | Method (hazard / stop-command) | `[0020]`, `[0044]` | FIG. 2, 4 |
| 202a-g | Method blocks | `[0020]`-`[0031]` | FIG. 2 |
| 300a-e | Time periods | `[0035]` | FIG. 3 |
| 302a-e | Decisions | `[0035]`-`[0039]` | FIG. 3 |
| 306a-c | Hazard information | `[0035]` | FIG. 3 |
| 308 | Clearance information | `[0038]` | FIG. 3 |
| 500 | System (electrical/computer) | `[0049]` | FIG. 7 |
| 552/554/556 | Planning / estimating / execution modules | `[0057]` | FIG. 8 |

## Figure relationships

| Figure | Paired with | Relationship | Notes |
|---|---|---|---|
| FIG. 2 | FIG. 3 | method block diagram ↔ its decision tree | FIG. 3 shows the branching/hold states for method 200 |
| FIG. 5 (A-AD) | (sequence) | progressive sequence (kneel reconfiguration phases) | multi-panel; lowering of center-of-gravity over time |
| FIG. 6 | (standalone) | post-reconfiguration end state | compact kneel, end effectors + knees on ground |
| FIG. 7 | FIG. 8 | system hardware ↔ software architecture | supporting detail |
| FIG. 1 | (standalone) | the robot | establishes the body / why a power cut is dangerous |

## Quote anchor table

| Quote ID | Paragraph | Verbatim text | Significance |
|---|---|---|---|
| q-0002-1 | `[0002]` | "Some analysts forecast a shortage of a million or more workers to staff order-fulfillment centers within the next ten to fifteen years." | prior-art-contrast (commercial motivation) |
| q-0010-1 | `[0010]` | "Such robots are always falling to some degree during normal operation." | mechanism-critical |
| q-0010-2 | `[0010]` | "If a dynamically stable robot loses power or otherwise becomes disabled, it collapses." | mechanism-critical |
| q-0013-1 | `[0013]` | "segregation strategies for hazard mitigation greatly reduce the productive potential of dynamically stable robots" | prior-art-contrast |
| q-0014-1 | `[0014]` | "a variable (e.g., escalating) hazard response by a mobile robot" | claim-supporting |
| q-0015-1 | `[0015]` | "the word \"bipedal\" as used herein may be replaced with \"mobile\" to encompass non-bipedal counterparts" | claim-supporting (scope breadth) |
| q-0024-1 | `[0024]` | "An example of this first model is YOLOV8 (Ultralytics Inc.)." | mechanism-critical |
| q-0027-1 | `[0027]` | "determining clearance information about a portion of the environment around the mobile robot" | claim-supporting |
| q-0028-1 | `[0028]` | "lowering the center-of-gravity of the mobile robot" | claim-supporting |
| q-0029-1 | `[0029]` | "by at least 30%, by at least 50%" | quantitative (pinned) |
| q-0031-1 | `[0031]` | "While in a safe operating stop, the mobile robot 100 may halt all movement without completely shutting down." | claim-supporting (dependent) |
| q-0032-1 | `[0032]` | "increasingly greater losses of efficiency while providing increasingly greater risk reduction" | mechanism-critical |
| q-0033-1 | `[0033]` | "may increase rather than decrease the risk to the human" | mechanism-critical |
| q-0042-1 | `[0042]` | "are protective and controlled forms of Category-1 and Category-2 stops" | claim-supporting (standards) |
| q-0047-1 | `[0047]` | "the mobile robot 100 may tend to collapse in a predictable manner and into a compact form, thereby reducing or eliminating a safety hazard to nearby humans" | quantitative/effect |

## Timeline

- **Priority date**: 2024-03-01 (provisional)
- **Filing date**: 2025-02-28
- **Publication date**: 2025-09-04
- **Grant date**: 2026-02-24
- **Examination period**: ~362 days (grant - filing)
- **Prior-art chronology**: cites ~40 US patent documents plus 3 academic publications (2007-2021),
  all predating the subject filing; co-pending US 19/067,693 and PCT/US25/17985 filed same day
  (2025-02-28).

## Prior-art references + differentiation

- **Scianca, Nicola, et al. (2021)** "A behavior-based framework for safe deployment of humanoid robots": addresses safe deployment behaviors; does not claim the graduated clearance-aware COG-lowering escalation.
- **Takubo, T., et al. (2007)** "Emergent walking stop using 3-D ZMP modification criteria map for humanoid robot": an emergent stop via ZMP modification; a stop technique, not the tiered hazard escalation with a clearance gate.
- **Zhou, Yuhang, et al. (2016)** "Falling protective method for humanoid robots using arm compliance to reduce damage": post-fall damage reduction, not pre-fall graduated hazard response.
- **Dense US patent citation set (~40)**: indicates a crowded, actively-filed area (collaborative robotics safety).

## 유리한 효과 + 정량 데이터

The reconfiguration lowers the center-of-gravity so that a fault-state collapse is compact and
predictable, reducing the fault-state fall extent; the tiered approach trades efficiency for risk
reduction as risk rises.

**Quotable spans:**
- `[0029]`: "by at least 30%, by at least 50%"
- `[0047]`: "the mobile robot 100 may tend to collapse in a predictable manner and into a compact form, thereby reducing or eliminating a safety hazard to nearby humans"

| Metric | Value | Paragraph |
|---|---|---|
| Fault-state fall-extent reduction (example, pinned at claim 13) | by at least 30%, by at least 50% | `[0029]` |
| Decision loop cycle (illustrative) | e.g., 1 Hz, 10 Hz | `[0036]` |

## Claim scope map (locked / open / pinned)

Required because Phase 2 cites claim anchors. The moat verdict rests only on the Locked column.

| Layer | Content |
|---|---|
| **Locked (independent claim 1 requires)** | A time-ordered, rising-risk sequence: first hazard info at a first time (first risk level); deceleration; second hazard info at a later time whose risk level is greater than the first; clearance information about the surroundings determined after decelerating; and a reconfiguration driven by both the second hazard info and the clearance info, where the reconfiguration lowers a center-of-gravity. |
| **Open (description / dependent claims add; claim 1 does not require)** | Safe operating stop with trained-operator release (claim 2, `[0031]`); proximity (3), trajectory (5), speed (6), human state (8) triggers; ML hazard model incl. YOLOv8 / Rekognition (7, 8, `[0024]`); foot placement during deceleration (9); knee bend (10), torso tilt (11), crouch (12), kneel (14), standing-to-non-standing (19); selecting a reconfiguration type by hazard (17) or clearance (18); placing a carried payload on the ground (20). |
| **Pinned (approximate point limitations, not floors/ceilings)** | Fault-state fall-extent reduction "by at least 30%, by at least 50%" (`[0029]`), with only claim 13 committing "at least 50%"; decision-loop rates "e.g., 1 Hz, 10 Hz." Example values; not bounds the independent claim states. |

**Scope-breadth note**: `[0015]` lets "bipedal" read as "mobile," extending the method to
one-arm, multi-arm, non-legged, and wheeled dynamically stable robots. A construction aid, not an
added claim limitation.
