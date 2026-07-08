# Self-Audit — Skeptical Pro-Subject Reader (semiconductor packaging engineer)

Persona: informed industry skeptic; will not accept a published application dressed as a
product, an EMIB-T fact smuggled in as the patent's, description/Example numbers treated as
claimed limits, standard practice sold as novelty, or a firm verdict softened into safe-harbor
mush. Blind to other readers. Can only ADD findings. Jurisdiction fence: grounding fixes are
anchor/narrow/label/cut; over-hedge fixes are de-hedge/point, never add-hedge.

Grounding source: `input/patent.md` (US 2025/0266395 A1 — contains numbered paragraphs
`[0001]`-`[0147]`; the CLAIMS are not in this file, only the mirrored Example paragraphs
`[0122]`-`[0147]`). Design context: thesis-spine.md, invention-summary.md (Claim scope map),
fact-check-log.md.

## Verdict summary

The essay is unusually disciplined against my persona's usual kills. The EMIB-T fence holds
("The document never uses the word EMIB" is stated twice, every EMIB/EMIB-T sentence carries an
external Source cite, never a `[dddd]` anchor). The KGD trap is avoided — testing is named as
"the industry's term of art," not sold as the patent's novelty, and the yield math is
explicitly "the industry's and this essay's, not the patent's." Claim scope is handled at full
rigor: the 1-10 µm pitch is repeatedly quarantined to the description, the through-via claim is
quoted at its spare width, and the claim-17-hangs-off-claim-16 problem is CONCEDED, not
smuggled. The steelman (§5) is a genuine THIS-patent objection conceded at full strength then
refined — steelman PRESENT. The firm verdict does not over-hedge; the single anti-hype guard is
spent once and the close actively refuses safe-harbor ("none of them moves the call").

Findings are additive and small. Nothing rises to high/critical.

---

## Findings

### SKEP-01 — Unsupported superlative / survey claim in the lead
- **severity**: medium
- **pass/lens**: pass-7 skeptical-pro (overreach) / grounding
- **verdict**: yes (overreach present)
- **quoted span (essay §1)**: "This is the most concrete piece of after-EMIB-T assembly
  thinking on the public record."
- **evidence**: No cited source supports a survey of "the public record." This is a universal
  claim over ALL public disclosures (competitor filings, academic chiplet/die-first literature,
  other Intel filings), none of which the essay has examined. A packaging engineer knows the
  public literature on die-first assembly, test-before-assembly, and bridge inversion is large;
  "the most concrete ... on the public record" is exactly the kind of unverifiable superlative a
  skeptic seizes on. It is also load-bearing — it sits in the lead and primes the whole thesis.
  The defensible core (this filing documents an inverted, test-gated bridge flow the public
  EMIB-T story lacks) is narrower than the sentence claims.
- **recommendation (narrow, not hedge)**: narrow the scope to what the evidence carries — e.g.
  tie the superlative to the specific object ("the most concrete public disclosure of an
  inverted, test-gated bridge flow from Intel's own packaging group") or drop "on the public
  record." Fence-compliant: this is a narrowing, not an added qualifier.

### SKEP-02 — Claim-dependency structure asserted but not verifiable in the shipped grounding file
- **severity**: low
- **pass/lens**: grounding spot-check (anchor/label)
- **verdict**: yes (transparency gap)
- **quoted span (essay §5)**: "The glass-and-TGV claim, claim 17 as filed, hangs off the
  no-cavity inverted package of claim 16, not off the cavity packages described above. The
  parallel Example paragraph is written broader [0138]. The claim as filed is not."
- **evidence**: `patent.md` contains no numbered claims — only Examples. Example 17 `[0138]`
  reads "the semiconductor package of any one of Examples 12-16" (verified line 196), i.e. the
  ONLY claim-scope evidence physically present in the offline anchor file states the OPPOSITE
  (broad) dependency. The narrow "claim 17 hangs off claim 16 only" fact lives solely in the
  external Google Patents claim text (design Claim scope map). The essay flags the Example/claim
  discrepancy honestly and moves in the conservative (narrowing) direction, so this is not
  overreach — but a reader who opens the shipped `patent.md` to verify cannot confirm the claim
  dependency and will find the contradicting Example. This is the essay's single most-repeated
  claim-number architecture (claims 1/2/16/17/19/20) resting on an anchor set that only proves
  Examples.
- **recommendation (label/anchor, not hedge)**: at the claim-16/17 assertion, attach the
  external authority the way §5's bibliographic line already does ("(Google Patents)"), so the
  claim-dependency fact is sourced to the published claims rather than reading as derivable from
  the `[0138]` Example anchor that in fact contradicts it.

### SKEP-03 — "bridge roadmap" softly implies a productization track the essay elsewhere denies
- **severity**: low
- **pass/lens**: pass-7 skeptical-pro (filed ≠ roadmap)
- **verdict**: yes (mild)
- **quoted span (essay §4)**: "this filing is one of the places where the glass roadmap and the
  bridge roadmap touch."
- **evidence**: The glass "roadmap" is grounded (Intel's Sept-2023 glass-substrate announcement,
  intel-glass-substrate-2023, tier-1). There is no cited "bridge roadmap" — the essay's own
  thesis is that this is a pending application that "nothing in it schedules" and whose
  after-EMIB-T reading is "this essay's synthesis." Calling the filing a node on a "bridge
  roadmap" leans, for one clause, toward the productization framing the rest of the essay
  scrupulously refuses. Low severity because the phrasing is intersection-language ("where ...
  touch"), not a schedule claim, and the surrounding paragraph is otherwise conservative.
- **recommendation (narrow)**: swap "the bridge roadmap" for a non-scheduling phrase (e.g. "the
  bridge work" / "this bridge-inversion filing"), keeping "glass roadmap" which is sourced.

---

## Checks that PASSED (evidence-forced, no finding)

- **Steelman present (full strength then refined)**: §5 "Read cold, this is one filing among the
  hundreds Intel produces in a year... No single claim contains the full architecture narrated
  above. And the document never mentions EMIB." then refines to the locked order-of-operations.
  THIS-patent objection, not a generic truism. PASS.
- **EMIB-T not smuggled as the patent's**: "The document never uses the word EMIB, and every
  link this essay draws to it rests on timeline and mechanism, not on anything Intel has said."
  Every EMIB/EMIB-T sentence carries a Source cite (Tom's Hardware / IEEE ECTC), never a
  `[dddd]`. PASS (honors fact-check-log HARD GUARD).
- **Pitch numbers not claimed as limits**: "The 1-to-10-micron pitch lives in the description's
  examples, and no claim carries it [0034]." `[0034]` verbatim confirms "in a range of 1 to 10
  microns" is description. PASS (locked/open/pin scope honored).
- **Claim-17 pin not called a bound**: essay quotes "a thickness in a range of 20 microns to 1.4
  millimeters [0138]" attributed to "Example 17," never described as a bound or as a required
  claim limit of the cavity story. `[0138]` verbatim. PASS.
- **Through-via claim quoted at its spare width**: "The through-via claim never says power, TSV,
  or cavity; it locks in only 'at least one contact on the second surface that provides an
  electrical pathway to the first surface' [0123]." `[0123]` (Example 2) verbatim. PASS.
- **KGD not sold as novelty**: named "the industry's term of art," yield math labeled "the
  industry's and this essay's, not the patent's"; and "Note whose yield that is. The description
  ties it to the routing and the saved substrate layers, not to the test step" — correctly
  separates the patent's stated `[0035]` effect from the essay's economic gloss. PASS.
- **Granted ≠ filed honored**: "a set of claims Intel is asking for, not a product it has
  scheduled"; "Every 'locks' above is a lock Intel is asking for: this is a pending application
  ... with no granted claim yet." Sought-locked vocabulary throughout. PASS.
- **Both quote blocks verbatim vs `[0142]`**: Example 21 (line 200) matches both block quotes
  exactly. PASS.
- **Anchor spot-checks (3+ sections)**: §2 `[0060]`/`[0061]` (carrier→mold→detach→bridge) matches
  lines 117-118; §3 `[0061]`/`[0062]` (test then substrate) matches lines 118-119; §4 `[0024]`
  (passive/active Imax) matches line 80, `[0035]` (power from cavity floor, routing/yield)
  matches line 91, `[0049]` glass frame matches line 105, `[0025]` "many substrates remain
  solder-attach components" matches line 81. All verbatim/faithful. PASS.
- **Over-hedge under firm posture**: verdict is firm; single anti-hype guard ("nothing in it
  schedules a product") spent once; "The limits priced in the previous section stand as written,
  and none of them moves the call" actively de-hedges. No safe-harbor mush. PASS (no 6G finding).
- **Timeline arithmetic**: "Fifteen months before ... EMIB-T" (Feb 2024→May 2025 = 15 mo);
  "eighteen months after its February 2024 filing" (→Aug 2025 = 18 mo). Both correct. PASS.
- **Inventor count**: "thirteen inventors" matches the 13-name Sources list. Mahajan attribution
  ("mainline packaging organization ... nothing stronger") honors the fact-check-log guard. PASS.
