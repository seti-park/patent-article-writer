# Self-Audit R2 (confirmation) — Skeptical Pro-Subject Reader (semiconductor packaging engineer)

Persona: informed industry skeptic; rejects a pending application dressed as a product, an
EMIB-T fact smuggled as the patent's, description/Example numbers sold as claimed limits,
standard practice sold as novelty, and a firm verdict softened into safe-harbor mush. Blind to
other readers (round-1 skeptic report read only for regression-check, per task instruction). Can
only ADD findings. Jurisdiction fence: grounding fixes = anchor/narrow/label/cut; over-hedge
fixes = de-hedge/point, never add-hedge.

Grounding source: `input/patent.md` (numbered paragraphs `[0001]`-`[0147]`; CLAIMS are not in
the file — only the mirrored Example paragraphs `[0122]`-`[0147]`). Design context:
thesis-spine.md, invention-summary.md (Claim scope map), fact-check-log note (patent never says
"EMIB").

Scope of R2: the 4 surgical edits (narrowed lead, "roadmap"→"bridge work on file", claim-17
re-sourced, frontmatter), plus a full adversarial re-read for any NEW medium+ issue the edits
might have introduced.

---

## Verdict summary

The revision landed cleanly. All three round-1 findings (SKEP-01 medium, SKEP-02 low, SKEP-03
low) are resolved in the direction the fence requires — narrow / label, never add-hedge — and
none regressed or spawned a new issue. The firm verdict is intact and did not gain safe-harbor
mush. **No NEW medium+ finding. No round-1 finding regressed.**

Finding count by severity: **critical 0 / high 0 / medium 0 / low 0.**

---

## The three round-1 findings — confirmation of resolution

### SKEP-01 (was medium: survey superlative in the lead) — RESOLVED, clean
- **before**: "This is the most concrete piece of after-EMIB-T assembly thinking on the public
  record." (universal survey claim over all public disclosures — unsupported).
- **after (essay §1, line 23)**: "What Intel put on file is the specific after-EMIB-T move: the
  assembly order inverted, the whole cluster test-gated before a board is committed."
- **verdict**: no overreach. The survey superlative ("most concrete ... on the public record")
  is gone. "What Intel put on file" scopes the sentence to THIS filing, not to all public
  thinking. The predicate is grounded: order inversion mirrors Example 21 [0142] ("attaching a
  bridge component ... to thereby create a multi-die bridge assembly"), the test-gate mirrors
  [0061]/[0142] ("testing the multi-die bridge assembly ... attaching a substrate ... when ...
  passes"). Verified verbatim (patent lines 118, 200).
- **under-hedge / hype check**: no. The clause is immediately balanced by the two-sided call —
  "It is also a pending application: a set of claims Intel is asking for, not a product it has
  scheduled." Firm, not hype.
- **hook check (pass-7 #1)**: still lands. Declarative, no deferred question, no verdict-insurance
  fact ahead of the beat; the technical payload (inverted order + test gate) precedes the status
  clause. Energy preserved.
- **"after-EMIB-T" scope**: the phrase is the essay's declared synthesis, conceded at full
  strength downstream (§5, line 81: "The after-EMIB-T reading is this essay's synthesis of a
  filing date, an unveiling date, and a shared power-delivery idea. Intel has not connected the
  two documents."). The definite article in the lead is a firm-posture thesis stance, not an
  un-conceded claim — proportionate given the explicit label. Not a finding.

### SKEP-02 (was low: claim-17 dependency not verifiable in shipped patent.md) — RESOLVED, clean
- **after (essay §5, line 79)**: "The glass-and-TGV claim, claim 17 as filed, hangs off the
  no-cavity inverted package of claim 16, not off the cavity packages described above, going by
  the published claims themselves (Google Patents). The parallel Example paragraph is written
  broader [0138]. The claim as filed is not."
- **verdict**: sound conservative sourcing, not a new overreach. `patent.md` contains no claims;
  Example 17 [0138] reads "the semiconductor package of any one of Examples 12-16" (verified
  patent line 196) — i.e. the only claim-scope evidence physically in the anchor file states the
  BROAD dependency. The narrow "claim 17 hangs off claim 16" fact lives only in the external
  Google Patents claim text. Attributing it to "the published claims themselves (Google Patents)"
  is the same conservative external sourcing §5 already uses for bibliographic/status facts, and
  the essay still openly flags that the Example is broader. This narrows/labels; it does not
  assert the claim dependency as derivable from the [0138] anchor that contradicts it. The
  Google Patents URL is present in Sources (line 98). Fence-compliant.

### SKEP-03 (was low: "bridge roadmap" implied productization) — RESOLVED, clean
- **after (essay §4, line 73)**: "this filing is one of the places where the glass roadmap and
  the bridge work on file touch."
- **verdict**: fixed. "the bridge roadmap" → "the bridge work on file" removes the scheduling
  lean; "glass roadmap" (grounded in Intel's Sept-2023 glass-substrate announcement) is retained.
  No productization implication introduced.

---

## NEW-issue re-sweep (edits could have introduced overreach / filed≠roadmap / EMIB-fence / over-hedge)

- **New overreach from the narrowed lead**: none. The replacement is strictly narrower than the
  original and stays inside the filing's own scope (see SKEP-01 above).
- **New overreach from claim-17 re-sourcing**: none. "going by the published claims themselves"
  is a sourcing label, not a scope expansion; Sources carries the Google Patents entry.
- **EMIB-fence intact**: the edits touched no EMIB sentence. The double fence still stands — §4
  line 61 "The document never uses the word EMIB, and every link this essay draws to it rests on
  timeline and mechanism, not on anything Intel has said"; §5 line 81 "the document never mentions
  EMIB." Every EMIB/EMIB-T sentence carries a Source cite (Tom's Hardware / IEEE ECTC), never a
  `[dddd]` anchor. Honors the fact-check-log HARD GUARD.
- **Over-hedge (6G) under firm posture**: none introduced. No edit added a qualifier. The close
  still actively de-hedges — §6 line 93 "The limits priced in the previous section stand as
  written, and none of them moves the call." Single anti-hype guard ("nothing in it schedules a
  product") spent once. No safe-harbor mush.
- **Steelman still present (pass-7 #3)**: §5 concedes the THIS-patent objection at full strength —
  "Read cold, this is one filing among the hundreds Intel produces in a year ... No single claim
  contains the full architecture narrated above. And the document never mentions EMIB." — then
  refines to the singly-locked order-of-operations. Steelman PRESENT (not the banned generic
  truism).

---

## Grounding spot-checks (3+ sections, verbatim vs patent.md)

- **§1 [0142]** (line 19: "bonds the bridge straight onto the chips first, then tests the whole
  cluster before a board ever enters the picture"): Example 21 [0142] (patent line 200) —
  "attaching a bridge component ... testing the multi-die bridge assembly ... attaching a
  substrate ... when the multi-die bridge assembly passes." Faithful.
- **§2/§5 [0122]** (hybrid-bond "directly bonded ... no solder in between"): [0122] (patent line
  180) — "the first insulating material is directly bonded to the second insulating material and
  some first metal contacts are directly bonded to a respective second metal contact." Verbatim.
- **§4 [0035]** (power "is often used to enable power to be routed into the bridge component"
  from "a source located at a bottom of a cavity in a substrate"; routing "reduces the number of
  substrate routing layers and can improve product yield"): [0035] (patent line 91) — both spans
  verbatim.
- **§5 [0144]** ("placing the bridge component in the cavity"): Example 23 [0144] (patent line
  202) — "placing the bridge component in the cavity." Verbatim; correctly framed as one
  dependent claim (claim 20) away from the method spine (claim 19).
- **§3 [0061]/[0062]**: test-then-substrate order matches patent lines 118-119. Faithful.

### Claim-scope map honored (locked / open / pinned)
- Pitch 1-10 µm quarantined to description examples — §5 line 77 "The 1-to-10-micron pitch lives
  in the description's examples, and no claim carries it [0034]." [0034] (patent line 90) —
  "the HBI pitch on the bridge components 102 is smaller still, in a range of 1 to 10 microns."
  Open/description honored.
- Through-via claim quoted at its spare width — §5 line 77 "it locks in only 'at least one
  contact on the second surface that provides an electrical pathway to the first surface' [0123]";
  power purpose kept as description [0035]. Correct locked/open split.
- **Pinned value not described as a bound**: §4 line 73 "Example 17 even sizes it: 'a layer of
  glass having a thickness in a range of 20 microns to 1.4 millimeters' [0138]." Attributed to
  Example 17, described as sizing, never called a bound or a required cavity-story limit. [0138]
  (patent line 196) verbatim. Pin honored.

---

## Checks that PASSED (evidence-forced)

- Granted ≠ filed: "a set of claims Intel is asking for, not a product it has scheduled" (§1);
  "Every 'locks' above is a lock Intel is asking for: this is a pending application ... with no
  granted claim yet" (§5). Sought-locked vocabulary throughout. PASS.
- Timeline arithmetic: "Fifteen months before ... EMIB-T" (Feb 2024→May 2025 = 15 mo);
  "eighteen months after its February 2024 filing" (→Aug 2025 = 18 mo). PASS.
- Inventor count: "thirteen inventors" matches the 13-name Sources list; Mahajan framed as
  "mainline packaging organization," nothing stronger. PASS.
- KGD not sold as novelty; yield math labeled "the industry's and this essay's, not the
  patent's" (§3). PASS.

---

## Bottom line

The narrowed lead is clean: scoped to THIS filing, no survey superlative, firm without hype,
still a hook. Claim-17 re-sourcing is sound conservative labeling. No NEW medium+ overreach /
filed≠roadmap / EMIB-fence / over-hedge issue introduced. Round-1 findings resolved without
regression. Confirmation round is dry.
