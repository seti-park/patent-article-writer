# Causal reasoning

Referenced by editorial-review SKILL.md. Applied during Pass 3 (Claim adequacy) and Pass 5 (Reader perspective) to evaluate the logical quality of causal claims in essay prose.

## Where this matters

SETI essays carry a recurring shape: patent as primary evidence, leading to an inference about a company's intent, capability, or trajectory. The connection from patent evidence to that inference is the essay's causal spine. When the spine is intact, the essay reads as analysis. When the spine is weak, the essay reads as projection.

This file enumerates the failure patterns and the checks that catch them.

## Causal claim identification

Causal claims surface in two forms.

**Explicit causal language**: `causes`, `leads to`, `results in`, `drives`, `enables`, `allows`, `prevents`, `because`, `means that`, `would explain`.

**Implicit causal structure**: sentence pairs where the second sentence is offered as consequence of the first, without explicit connective.

> Tesla filed the patent in March. The April launch announcement followed.

The juxtaposition reads as causal even without `because` or `as a result`. Pass 3 should flag implicit causal pairs when the connection is load-bearing for the thesis.

## Failure patterns

### Pattern 1: Correlation framed as causation

The essay observes that a patent filing date sits close to a product launch, an executive statement, or a competitor's move. The prose then treats the proximity itself as evidence of causal relationship.

Diagnosis question: does the essay claim the patent caused the event, or does it claim the proximity is anomalous?

These two framings have different evidence requirements. `Anomalous proximity` (the timing-anomaly hook) requires only that the proximity exists and is unusual. `Caused` requires a mechanism connecting patent to event.

Fix: when the essay's claim is anomaly-of-proximity, the prose should signal that explicitly. Avoid `the patent enabled the launch` when the available evidence is only `the patent preceded the launch`.

### Pattern 2: Missing confounders

The essay infers a company strategy from a patent filing. Other plausible motivations for the same filing exist but are unaddressed:

- **Defensive filing**: claim staked to prevent competitor's blocking patent
- **Blocking strategy**: claim staked to prevent competitor's product direction
- **Employee retention**: patent as a credit-assignment instrument for retained engineer
- **Signaling**: filing visible to industry as a capability advertisement, not a product roadmap
- **Carry-over from acquired company**: inherited filing reflects the acquired company's priorities, not current strategy

Fix: the prose should either address the most plausible alternative explanation (one or two sentences) or scope the claim narrowly enough that confounders do not undermine it. Listing every alternative is overkill. Naming the one or two most plausible alternatives is sufficient.

### Pattern 3: Reverse causation

The essay treats `A → B` as the direction of causation when the patent record is equally consistent with `B → A`.

Example: `patent filing enables product launch` reverses to `product launch decision triggers patent filing`. Both are plausible. The essay's choice between them must be defensible by evidence beyond chronology.

Fix: when the direction is ambiguous, the prose should acknowledge it. The thesis can still proceed with the chosen direction, but the acknowledgment of alternative direction is a trust signal.

### Pattern 4: Mechanism stated as `enables` without showing how

The prose claims `X enables Y` but never explains how X enables Y. The reader is asked to take the connection on faith.

Diagnosis question: if a skeptical reader asks `how does X actually produce Y`, does the prose answer the question, or does it move on?

Fix: either supply the mechanism in one or two sentences, or downgrade the claim to a hedge (`may enable`, `appears positioned to`, `suggests potential for`).

### Pattern 5: Counterfactual omission in reversal structure

SETI essays often turn on a reversal: the conventional narrative says X, the patent evidence supports not-X. The counterfactual question is essential here: if the conventional narrative were true, what would the patent evidence look like, and what would it not look like?

Without the counterfactual, the reversal reads as assertion rather than argument.

Fix: Pass 6 (lead/conclusion strength) is the natural place for this check, but the counterfactual reasoning itself belongs to Pass 3. The prose should briefly contrast: under the conventional narrative, the patent would show A; instead it shows B.

### Pattern 6: Indirect patent evidence supporting direct causal claim

The patent's paragraph evidence is indirect (mentions a feature, references a structure, implies a capability). The essay's causal claim is direct (`the company has decided to`, `the company will`).

Indirect evidence cannot support direct causal claims without bridging argument.

Fix: either bring direct evidence (another patent paragraph, an official statement, a Tier 1-2 source from external-fact-verification.md), or hedge the causal claim down to match the evidence's directness.

## Cross-pass application

### Pass 3 lens: evidence supports claim?

For each causal claim:

- Identify the patent paragraph (or external source) that the claim rests on.
- Compare the claim's strength to the evidence's directness.
- Flag mismatches (Pattern 6).
- Flag missing mechanism (Pattern 4) when the claim asserts enablement.
- Flag missing confounder treatment (Pattern 2) when the claim infers strategy.

### Pass 5 lens: reader can follow chain?

For each multi-step causal chain in the prose:

- Read the chain as a domain-fluent skeptic would read it.
- At each step, ask: would the skeptic accept this step on the evidence shown so far?
- Flag steps where the skeptic would stop and ask `why does that follow`.
- Flag spots where reverse causation (Pattern 3) is plausible but not addressed.

## Severity scaling

Causal-reasoning findings follow the standard posture lens (see `posture-lens.md`).

- Under aggressive posture, Pattern 1 (correlation as causation) is medium severity if the essay's hook is timing-anomaly framed, because the anomaly framing is consistent with the evidence even without causal claim.
- Under conservative posture, Patterns 2 and 4 (missing confounders, missing mechanism) shift toward high severity, because conservative posture's bar is whether a skeptical reader can challenge the claim.
- Patterns 3 and 6 (reverse causation, indirect evidence supporting direct claim) hold high severity across postures when they are load-bearing for the thesis.

## Relationship to voice canon

Causal-reasoning checks are about logical quality, not voice. A claim can pass voice canon compliance (Pass 1) while failing causal reasoning (Pass 3 or Pass 5). The two checks are independent. When both fire on the same prose passage, the recommendations stack: voice fix addresses expression, causal-reasoning fix addresses argument structure.
