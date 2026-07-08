# Phase 2 Handoff Notes

## (a) Audience reframe decision

None. Audience held at the default reader-profile (curious retail investor, advanced high
school to early undergraduate technical comprehension) per input/essay-context.md. One
framing consequence of the news moment: assume the reader ARRIVES from the Etched
stealth-exit thread already primed with "Cluster-Scale Memory" vocabulary - the essay
does not need to sell why the question matters, it needs to adjudicate it. The secondary
technical-impossibility hook ("any-to-any without a switch or a wire per pair") is
available inside section 3 as the mechanism on-ramp; the locked spine leads with
corporate-narrative-friction.

## (b) Citation priority mapping

| Quotable span / anchor | Primary section | Role |
|---|---|---|
| fact `etched-csm-thread-2026-07` (thread claims) | 1-lead | the narrative half of the friction; attribute "the company says"; do NOT spend claim quotes in the lead |
| fact `etched-family-trio-wips` | 2-grant | trio identity + commitment signal (one paragraph cap on siblings) |
| `[0386]` q-0386-1 (cross-set coupling, = claim 1) | 3-wiring | THE claims anchor; use first, verbatim |
| `[0387]` q-0387-1 (at most one other device, = claim 1) | 3-wiring | the reachability guarantee; pairs with q-0386-1 |
| `[0026]` q-0026-1 (switch expensive) | 3-wiring | problem framing; the patent's own foil, not an external market claim |
| `[0032]` q-0032-1 (networking switch) / `[0130]` q-0130-2 (point-to-point foil) | 3-wiring | the two conventional alternatives; keep both, they bound the design space |
| `[0126]` q-0126-1 (which devices in which set) | 3-wiring | makes FIG. 7 readable (odd chips one set, even the other) |
| `[0140]` q-0140-1/2, `[0142]` q-0142-1 | 4-traffic | channel-family segregation + simultaneity; pair with FIGS. 7A/7B |
| `[0168]` q-0168-1 (balanced data) + `[0061]` q-0061-1/2 (p=4, q=2 math) | 4-traffic | the "balanced by wiring" payoff; `[0061]`'s decimals are the one nerd-candy number - spend once |
| `[0251]` q-0251-1, `[0258]` q-0258-1, `[0313]` q-0313-1/2 | 5-workload | LLM/transformer tie + the 4x feedforward pressure; description-level, label as such |
| `[0278]` q-0278-1, `[0267]` q-0267-1 (never-gather invariant) | 5-workload | the honest kernel of "the pool is the cluster" - closest the patent comes to CSM's memory idea, WITHOUT being a memory claim; handle precisely |
| `[0119]` q-0119-1 (memory 630) + `[0134]` q-0134-1 (PCIe/SPI/ethernet/UCIe) + `[0133]` q-0133-1 | 6-boundary | reserved for the steelman/boundary beat - do not spend earlier |
| `[0124]` q-0124-1 / `[0250]` q-0250-1 (effect statements) | 3-wiring / 7-verdict recap | effect anchors; `[0124]` may recur once in the verdict recap |
| `[0385]` q-0385-1 ("two or more" description framing) | 6-boundary only | ONLY as the narrowing exhibit next to claim 1's "four or more"; never as the scope of the granted claim |

## (c) Framing trace (rejected candidates)

- Candidate 2 ("no switch, no n-squared wires") rejected as spine: mechanism explainer
  with no CSM verdict - fails the essay-context mandate. It survives as section 3's
  on-ramp. Phase 2 must NOT let the essay become a topology explainer that gestures at
  CSM in the last paragraph.
- Candidate 3 ("three patents, one machine") rejected: portfolio intent has no claims
  anchor; hook maps to the deprecated timing-anomaly pattern; essay-context caps siblings
  at one context paragraph. Phase 2 must NOT expand the trio into a filing-strategy
  narrative or deep-dive 903/262 mechanics.
- Candidate 4 ("balanced by construction") rejected: Axis 4 needs an external
  collective-scheduling baseline that is unverifiable in this environment; hook
  vocabulary sits above the reader profile. Its material lives inside section 4 with the
  contrast kept patent-internal.

## (d) Traps to avoid

Claim-scope traps (restating invention-summary.md §Claim scope map; locked / open /
pinned vocabulary - this patent's map has NO pinned points, so nothing here may be
described with "about X" approximation language, and no lock may be softened into a
preference):

- **Claim 1 / claim 14 device floor.** DO say claims 1 and 14 require two sets of four
  or more devices each (locked). DON'T carry the abstract's / SUMMARY `[0004]`'s /
  `[0385]`'s "two or more" into any statement about the granted claims - that wording is
  description framing the grant narrowed. When the essay shows the narrowing, quote
  q-0385-1 AS the before-picture, explicitly labeled.
- **Claim 18 is the broad-floor independent.** DON'T say "all three independent claims
  require four per set." Claim 18 locks "two or more" per set but pays with structure:
  each set must contain two groups, and the two channel families must wire group1↔group3
  / group2↔group4 (first channels) and group1↔group4 / group2↔group3 (second channels)
  with exclusive per-family sub-operation traffic. The three independents trade floor for
  structure differently; collapsing them re-seeds the drift this map exists to prevent.
- **Eight devices.** DON'T present eight devices, four channels per device, or the 16-link
  count as claim-1 requirements. Eight is FIG. 7's worked example and dependent claim
  13's exact locked count; "four other devices" is `[0129]`'s example arithmetic; 16 vs
  28 links is OUR derived arithmetic (flagged derived in invention-summary) - if used,
  present as arithmetic from the figure, never as patent text.
- **No latency, no bandwidth magnitude, no memory, no AI in the claims.** DON'T write
  that the claims cover an "ultra-low-latency" link, a bandwidth number, a memory pool,
  HBM/SRAM, transformers, or inference. Claim 5 locks bandwidth EQUALITY across channels,
  not magnitude. The AI-model mapping (`[0251]`-`[0313]`) and memory 630 (`[0119]`) are
  description-level: narrate them as the description's intended workload/embodiment, on
  description anchors. The claims' only workload hooks: systolic array (claim 7), matrix
  multiplication (claims 10/23), reduction/gather sub-operations (claims 11/23).
- **Channel-family assignment.** Claims 8/11/23 lock that the two sub-operations use
  disjoint channel subsets and (11/23) that the first is a reduction and the second a
  gather. WHICH physical family in FIG. 7 carries which (gather on 730, reduction on 740)
  is the description's example `[0140]` - description-preferred, not claim-locked. Same
  for simultaneity: overlapping-time execution is locked by claim 9 (under claim 1), and
  is NOT a limitation of claim 18 itself (dependent 22 adds reachability, 23 adds
  reduce/gather - neither adds simultaneity).
- **Link technology.** PCIe / SPI / ethernet / UCIe / optical / on-die (`[0134]`,
  `[0133]`) are description OPTIONS - open, not locked. This is steelman fuel (section
  6), not a claim feature. DON'T let the mitigation quietly upgrade "channels" into a
  proprietary PHY.

Other traps:

- **LVI / HBM-SRAM fence (the single anti-hype guard).** Never credit LVI (voltage, VRMs,
  power delivery, cold plates) or the HBM/SRAM hybrid to this filing or its granted
  siblings. State the absence once, in section 6, with the 18-month unpublished-filings
  window noted once - that is the essay's one patent-specific anti-hype guard. Do not
  multiply hedges around it (closing_posture: firm; gate_hedge will hard-fail
  safe-harbor boilerplate).
- **Generic-truism ban (steelman).** The section-6 steelman is the claim-scope thinness
  objection (standard links, no latency number, topology-only) conceded at full strength
  and then refined. "Patents don't guarantee products/stock prices" may not appear as the
  steelman or as the closing posture; the product-practice question appears only as the
  closing binary test (summer-2026 racks make the topology inspectable).
- **Company numbers.** "$1B+ in customer contracts", "$800m raised", 80%+ FLOPs, half
  voltage, ship dates: company-claimed only. Every use carries "the company says" (fact
  IDs `etched-csm-thread-2026-07`, `etched-lvi-biz-thread-2026-07`). No independent
  verification exists in this run.
- **No external competitor specs.** The switch-fabric and full-mesh foils are the
  PATENT'S OWN (`[0026]`, `[0032]`, `[0130]`). Do not name NVLink/NVSwitch or any
  competitor product spec as fact - unverifiable here (search-log L2). Industry framing
  stays generic ("switched fabrics", "point-to-point meshes") or patent-anchored.
- **FIGS. 7A/7B are not a sequence.** They are a decomposition of ONE topology split "for
  case of illustration" [sic - source typo, preserve if quoted] `[0123]`; 7C is the
  union `[0125]`. No before/after language. FIG. 9B's pair-break (dropped) is
  intentional - do not reopen; FIG. 6's "Tensor Parallel Device" drawing label vs
  "tensor parallel groups 620" text label is a source inconsistency - use the text label.
- **Computed numbers.** 266-day examination period and the 16-vs-28 link count are
  computed/derived, not quotable patent text. Attribute as computation.
- **Verbatim quirks.** `[0026]` "different processing device" (singular), `[0032]` "any
  other one of the one of the processing devices", `[0123]` "for case of illustration",
  `[0125]` "A 0 -A 7" spacing: preserve exactly when quoting (gate_quotes string-matches);
  paraphrase outside quotation marks if the quirk would read as our typo.
- **Em-dash ban** applies to essay body; patent verbatim quotes keep their original
  punctuation (none of the selected spans contain em dashes).

## (e) Open questions for Phase 2 (awaiting SETI)

- **Name the graph or not**: "complete bipartite graph (K4,4)" is the precise label for
  FIG. 7C's example. Default: describe structurally ("two sets, every cross-pair wired,
  none within"), offer the math label once in parentheses for readers who want the
  handle. SETI may strike the label entirely.
- **Quote the thread's "the best layer is no layer" line in the lead?** It mirrors the
  patent's own move (the best switch is no switch) and makes the friction vivid. Default:
  yes, once, with "the company says" attribution and the quote-chain caveat from
  fact-check-log. SETI may prefer the lead to paraphrase.
- **Title pattern**: the spine supports both a declarative-reversal title ("Etched
  patented the wiring, not the memory") and a question-resolution title. SETI picks at
  compose time.
- **Sibling mention depth**: one paragraph is the cap (essay-context); confirm whether
  the part-2 teaser (903 dataflow deep-dive reserved) is stated explicitly or left
  implicit. Default: one clause, implicit.
