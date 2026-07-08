# Scoped Post-Cap Delta Verification — v5 (draft_version 5), round-3 edits only

Scope: only the sentences named by the orchestrator (the round-3-revised material in the
"In practice" design-around paragraph, the LVI/HBM absence sentences, the [0026] switch
attribution, the QKV gloss, and the §7 verdict-paragraph claim-5/[0168] clause). Mechanical
fidelity only; no style/tone/hedge commentary. Sources read: `handoff/03-edit/essay-final.md`,
`input/patent.md` (paragraphs + CLAIMS block), `handoff/01-design/invention-summary.md`
(Quote anchor table + Claim scope map), `input/essay-context.md` (attribution rules),
`handoff/01-design/fact-check-log.md` (external-fact tiers).

## 1. Mechanical layer

```
$ python .claude/skills/_shared/scripts/gate_quotes.py handoff/03-edit/essay-final.md \
    --invention-summary handoff/01-design/invention-summary.md --patent input/patent.md
[PASS] gate=quotes
  (no findings)

$ python .claude/skills/_shared/scripts/gate_anchors.py handoff/03-edit/essay-final.md \
    --invention-summary handoff/01-design/invention-summary.md \
    --figures handoff/01-design/figures-index.txt
[PASS] gate=anchors
  (no findings)
```

Both mechanical gates pass clean on the full v5 essay (not just the delta), confirming no
orphan quotes and no anchor-format violations survive the round-3 edit.

Independent byte-check (exact substring counts of `input/patent.md`) run against every
quoted string used in the scoped sentences:

| Quoted string (as it appears in essay) | Verbatim in patent.md? |
|---|---|
| "without communicatively coupling any of the plurality of processing devices in the same set" | yes (6 occurrences: claims 1, 14, 18-dependent 19, [0385]/[0386] region) |
| "expensive to include in a system that performs tensor operations" | yes (1 occurrence, [0026]) |
| Full claim-1 channel clause (line 45 block quote) | yes (4 occurrences: claims 1, 14, [0386], and one Example-family echo) |
| "through at most one other of the plurality of processing devices" | yes (6 occurrences: claims 1, 14, 18-dependent 22, [0387], etc.) |
| "QKV generation" | yes (1 occurrence, [0254]) |
| "attention computation" | yes (2 occurrences, [0254] x2 — definition + cross-ref) |
| "each of the plurality of communication channels is configured for a same data bandwidth" | yes (2 occurrences: claim 5 + [0391]/Example echo) |

## 2. Verdict table

| Ref | Sentence (quoted) | Anchor(s) | Verdict | Evidence | Recommended fix |
|---|---|---|---|---|---|
| 1a | "In practice the fence reaches builders who copy the claimed wiring, and through claim 18 it reaches builders who add links but keep the lane discipline." | claim 1 (implicit), claim 18 (implicit) | SUPPORTED | Claim 18 text: "...wherein data transfer for the first sub-operation occurs only via the plurality of first communication channels and data transfer for the second sub-operation occurs only via the plurality of second communication channels" — this is the "lane discipline" claim 18 requires; claim 18 (unlike claims 1/14, see 1c) has no negative limitation barring extra intra-set links, so it "tolerates added links" while still binding traffic to channel families. | none — none needed |
| 1b | "A rack that keeps its networking switch in place of the claimed direct channels sits outside claim 1: the switch is the foil the filing itself sets against the fixed topology [0026], [0032]." | [0026], [0032] | SUPPORTED | [0026]: "a data switch that allows sharing of data amongst different processing device may be expensive to include in a system that performs tensor operations." [0032]: "the processing devices 110 may be coupled together using a networking switch that enables communication between any one of the processing devices 110 with any other one of the ... processing devices 110." Both paragraphs name the switch as the alternative the fixed topology is built to replace; claim 1's positive recitation is "a plurality of communication channels to directly communicatively couple" every cross-set pair — a switch-mediated rack does not literally recite that structure. | none |
| 1c | 'A rack that copies the pattern but adds links inside a set arguably steps outside claims 1 and 14 as written. Both require channels that couple the sets "without communicatively coupling any of the plurality of processing devices in the same set" [0386].' | [0386] | SUPPORTED | Byte-identical clause confirmed in all three locations: **Claim 1**: "...without communicatively coupling any of the plurality of processing devices in the same set of the plurality of processing devices, wherein..." **Claim 14**: same clause, verbatim, inside "A system comprising: a plurality of tensor parallel groups...". **[0386]**: "a plurality of communication channels to directly communicatively couple every processing device in the first set ... without communicatively coupling any of the plurality of processing devices in the same set of the plurality of processing devices,". The essay's quotation is an exact truncated substring (stops at "the same set," dropping the repeated "of the plurality of processing devices" tail) — a valid partial quote, not a distortion. | none |
| 1d | "That leaves claim 18, which tolerates the added links and binds the traffic instead, the same kind of rule claims 8, 9, and 11 stack on top of claim 1's structure." | claims 8, 9, 11, 18 (implicit) | SUPPORTED | Dependency chain confirmed from the CLAIMS block: claim 8 depends on claim 1 (adds channel-subset exclusivity per sub-operation); claim 9 depends on claim 8 (adds overlapping-time-period simultaneity); claim 10 depends on claim 9 (names the operation matrix multiplication); claim 11 depends on claim 10 (names the sub-operations reduction/gather) — so 8→9→10→11 is a single chain resting on claim 1's bare structure, as the sentence states. Claim 18's own text bundles structure (two groups per set, first/second communication-channel families per FIGS. 7A/7B) AND a routing rule ("data transfer for the first sub-operation occurs only via the...first communication channels and...second sub-operation...only via the...second communication channels") inside ONE independent claim — the same category of channel-exclusivity rule as claim 8, merged with structure rather than stacked as a separate dependent. "Same kind of rule" is read as a categorical (not verbatim-content) comparison, which holds; the sentence does not assert claim 18 itself recites simultaneity (claim-9-type) or reduction/gather naming (claim-11-type) — those remain on claim 18's own dependents (19-23), mirroring claim 1's dependents. | none |
| 1e | "Declining that rule is a firmware choice with a price: reroute the traffic and you forfeit the cheap overlap of reduce and gather, the property that made the pattern worth copying." | claims 8/9/11 + [0140]-family (implicit) | SUPPORTED | Claim 8: sub-operation traffic exclusive per channel subset. Claim 9: "...perform the first sub-operation and the second sub-operation in overlapping time periods such that first data...is transferred...at the same time second data...is transferred..." [0142]: "in the event that the first and second operations are being performed during overlapping time periods, the processing devices A0-A7 may receive and/or transmit data for both operations during overlapping time periods." The claimed simultaneity is contingent on the channel-family exclusivity (claim 8) that keeps the two traffic streams from colliding; declining that exclusivity removes the structural guarantee that lets reduce/gather run concurrently without contention — i.e., forfeits the "cheap" (structurally free) overlap. Consistent with the essay's own earlier framing (§5: "Disjoint lanes make simultaneity cheap... Reduce and gather stop taking turns."). | none |
| 2 | '"Low-Voltage Inference is nowhere in this filing." + "The same goes for the power-delivery work, the cold plates, and the HBM/SRAM hybrid (stacked high-bandwidth memory paired with on-chip SRAM) that the thread folds into CSM."' | (absence claim — no paragraph anchor possible) | SUPPORTED | Full-text case-insensitive sweep of `input/patent.md` (453 paragraphs + 23 claims) for: `voltage`, `VRM`, `cold plate`/`coldplate`, `liquid cooling`, `HBM`, `high-bandwidth memory`, `SRAM`, `static random`, `power`, `latency`, `memory pool`, `shared memory`, `volt`, `regulator`, `thermal`, `cooling`, `cache`, `stacked memory`, `interposer`, `die-to-die`, `watt` — **zero hits on every term**. "Memory" itself appears only re: FIG. 6/630 (a generic tensor-supply memory block, [0112]/[0119]), FIG. 13 boilerplate computer memory, and two un-granted spec "Example" method claims ([0372]-[0374], [0432]-[0433]) — none of the 23 **granted** claims mention memory (confirmed by grep of the CLAIMS block: 0 hits). No sibling-scope gap: the sentence scopes the absence to "this filing" only; it does not assert anything about the two sibling patents (US 12,306,903 B1 / US 12,361,262 B1), consistent with essay-context.md's instruction to cover siblings as context only. HBM/SRAM-hybrid attribution to "the thread" matches fact-check-log `etched-csm-thread-2026-07` (tier-1, company-claimed, logged) and essay-context.md's News-context CSM bullet. | none |
| 3 | 'a data switch the filing calls "expensive to include in a system that performs tensor operations" [0026]' (§3; this is the only occurrence of this exact attribution — §6 line 90 cites [0026] again but with different wording, "the switch is the foil the filing itself sets," covered under 1b above) | [0026] | SUPPORTED | [0026] full sentence: "In some circumstances, a data switch that allows sharing of data amongst different processing device may be expensive to include in a system that performs tensor operations." Grammatical subject = "a data switch..."; the essay's quoted predicate is an exact verbatim substring beginning right after "may be." Subject and quoted words both match. | none |
| 4 | "Its decoding layers, the loop that infers one token at a time [0259], run normalization, then self-attention (QKV generation and attention computation, the making and use of the query, key, and value matrices), then projection, then an MLP [0252], [0254]." | [0252], [0254], [0259] | SUPPORTED | [0252]: "Some of the decoding layers 905 may include a normalization layer 910, a self-attention layer 915, a projection layer 920, and a multi-layer perception layer (MLP) 925" — confirms the four-block order exactly. [0254]: "The self-attention layer 915 may include QKV generation 916, where an input tensor is multiplied by each of the query weight tensor, the key weight tensor, and the values weight tensor to generate a query tensor Q, a key tensor K, and value tensor V... The self-attention layer 915 may also include performing the attention computation 918." — confirms the two named sub-blocks verbatim ("QKV generation," "attention computation") and supports the gloss: "making" = generating Q/K/V (QKV generation), "use" = the softmax(Q·K^T)·V computation (attention computation). [0259] confirms the one-token-at-a-time decoding loop. | none |
| 5 | 'Reduce and gather traffic run at the same time on separate channel families [0142], over equal-bandwidth links (claim 5), with the same load on every link under the description's prescribed split [0168].' | [0142], claim 5, [0168] | SUPPORTED | Claim 5: "The tensor parallel group of claim 1, wherein each of the plurality of communication channels is configured for a same data bandwidth." — an equality requirement (uniform bandwidth across channels), not a magnitude/"high bandwidth" claim; essay's "equal-bandwidth links (claim 5)" is exact. [0168]: "...the same amount of data may be shared by each of the processing devices A0-A7 and a same amount of data may be shared across each of the second communication channels 740. Note that had the first and second tensors been split in unequal tiles, different amounts of data may be shared..." — this is an explicit conditional: equal tile-splitting (the description's worked/prescribed split) produces equal per-link load; the paragraph itself supplies the counterfactual (unequal split -> unequal load), confirming the "under the description's prescribed split" qualifier is doing real, accurate scoping work (a description-level contingent fact, correctly NOT presented as an unconditional claim guarantee, distinct from claim 5's unconditional structural equality). [0142] confirms the same-time/overlapping-period language. | none |

## 3. Findings (any severity)

- **[INFO / no action]** Item 2's second sentence lists three items ("the power-delivery
  work, the cold plates, and the HBM/SRAM hybrid... that the thread folds into CSM") where
  the trailing relative clause is syntactically closest to "the HBM/SRAM hybrid" only.
  Under standard low-attachment reading (and the only reading consistent with
  essay-context.md, which files "power delivery... cold plates" under the **LVI** bullet
  and "HBM/SRAM hybrid design" under the **CSM** bullet), the sentence is accurate: only
  the HBM/SRAM piece is being tied to "the thread['s] CSM" framing, while power-delivery/
  cold-plates were already anchored to LVI by the immediately preceding sentence and by
  §2/§6's established two-pillar framing ("Low-Voltage Inference is the power pillar").
  A reader could in principle mis-parse the clause as scoping over all three items, which
  would misattribute LVI-side features to CSM — but this reading contradicts the essay's
  own established pillar framework and essay-context.md's source categories, so the
  default/intended reading is the correct one. Not rated as a non-SUPPORTED verdict; noted
  for completeness only, no fix recommended (this is a parse-risk observation, not a
  fidelity failure — the asserted content under the natural reading is fully sourced).
- No MISREAD, OVERREACHED-BEYOND-ANCHOR, or UNSUPPORTED verdicts in this delta.
- No unlogged external facts in scope: the one external (non-patent) fact touched by this
  delta (HBM/SRAM hybrid as a thread-claimed CSM feature) is logged at fact-check-log row
  `etched-csm-thread-2026-07` (tier-1, company-claimed, attribution required) and the essay
  text carries the required attribution ("that the thread folds into CSM").
- Claim-1/14/18 quotations and dependency chains all verified byte-exact and legally
  consistent against the CLAIMS block; no drift found.
