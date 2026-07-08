# Post-Acceptance Grounding Verification — essay-final.md

Essay: `/home/user/patent-essayist/handoff/03-edit/essay-final.md`
Patent: `/home/user/patent-essayist/input/patent.md` (US 2025/0266395 A1)
Invention summary: `/home/user/patent-essayist/handoff/01-design/invention-summary.md`
Fact-check log: `/home/user/patent-essayist/handoff/01-design/fact-check-log.md`

## Mechanical layer

```
$ python .claude/skills/_shared/scripts/gate_quotes.py handoff/03-edit/essay-final.md \
    --invention-summary handoff/01-design/invention-summary.md --patent input/patent.md
[PASS] gate=quotes
  (no findings)

$ python .claude/skills/_shared/scripts/gate_anchors.py handoff/03-edit/essay-final.md
[PASS] gate=anchors
  WARN  ANCHOR-000   no invention-summary provided, anchor-chain check skipped  ((global))
  WARN  FIGREF-000   no figures_index provided, figure-ref check skipped  ((global))
```
(Both gates PASS mechanically; the two WARNs are informational — this invocation of `gate_anchors.py` was
run without the optional `--invention-summary` / figures-index flags, not a defect in the essay.)

## Anchor-by-anchor verdict table

Every `[dddd]` occurrence in essay-final.md (19 distinct paragraphs, 30 total anchor tokens), every block
quote, and the claim-scope statements. All patent quotes below were checked as verbatim substrings against
the actual patent.md paragraph text (paragraph line numbers cited from input/patent.md).

| # | Essay sentence (anchor) | Source span cited | Verdict | Note |
|---|---|---|---|---|
| 1 | "The filed method bonds the bridge straight onto the chips first, then tests the whole cluster before a board ever enters the picture [0142]." | Ex.21 [0142]: "...attaching a bridge component...to thereby create a multi-die bridge assembly; testing the multi-die bridge assembly...attaching a substrate...when...passes the performance metrics..." | SUPPORTED | Paraphrase asserts no more than the span; EMIB-T clause in same passage carries no anchor (fence intact). |
| 2 | "set two chips on a temporary carrier, mold them into one rigid piece, peel the carrier away, and bond a bridge across the two chips [0060], [0061]." | [0060] assemble+mold; [0061] "the carrier is detached...a bridge component is attached to a first portion of the first IC and a first portion of the second IC" | SUPPORTED | Four clauses map 1:1 onto the two cited paragraphs' four method steps. |
| 3 | "better 'bump density, power efficiency, speed and bandwidth' [0001]" | [0001]: "improve bump density, power efficiency, speed and bandwidth in semiconductor packaging" | SUPPORTED | Verbatim quoted fragment matches exactly. |
| 4 | Block quote: "attaching a bridge component to a first portion of the first IC and a first portion of the second IC, to thereby create a multi-die bridge assembly" — attributed "Example 21 [0142]" | [0142] Example 21, verbatim | SUPPORTED | Exact verbatim substring; correctly labeled "Example 21" (not "Claim 19") per invention-summary's attribution rule, since claim 19's actual wording differs trivially ("to the first IC die and the second IC die" vs Example's "to a first portion of..."). |
| 5 | Block quote: "testing the multi-die bridge assembly to determine whether it passes performance metrics; and attaching a substrate...to thereby create a package assembly" — "Example 21 [0142]" | [0142], verbatim, immediately following quote #4 in source | SUPPORTED | Verbatim-contiguous with quote #4 in the original paragraph (only the intervening "; " separator, correctly represented as two separate quoted blocks rather than falsely stitched into one span). |
| 6 | "In the drawings, the assembly is two dies joined by one bridge slung underneath them, a self-contained object with no substrate in sight [0030]." | [0030]: FIG.1 cross-section, bridge 102 + die 106/110, no substrate mentioned | SUPPORTED | Bridge-beneath-dies orientation matches [0032]/[0034] (dies' I/O structures face the bridge from above). |
| 7 | "the apparatus claim carries it in claim text: insulating material 'directly bonded' to insulating material, metal contacts bonded straight to metal contacts, with no solder in between [0122]." | [0122]/Claim 1: "...the first insulating material is directly bonded to the second insulating material and some first metal contacts are directly bonded to a respective second metal contact..." | SUPPORTED | Verified against actual Claim 1 text (line 209) — identical wording to Example 1. "No solder in between" is a fair characterization of a direct-bond interface (consistent with [0043]'s "There is no solder material at this HB interface"), not an overreach. |
| 8 | "The description's example numbers put that contact spacing, the pitch, 'in a range of 1 to 10 microns' on the bridge [0034]." | [0034]: "...the HBI pitch on the bridge components 102 is smaller still, in a range of 1 to 10 microns." | SUPPORTED | Exact quote; correctly labeled "description" not claim (matches claim-scope map: pitch is description-only). |
| 9 | "because 'many substrates remain solder-attach components' [0025]" | [0025]: "...many substrates remain solder-attach components, having solder-based interconnects..." | SUPPORTED | Exact quoted fragment. |
| 10 | "'the multi-die bridge assembly is subjected to testing to determine whether it passes performance metrics' [0061]" | [0061], verbatim | SUPPORTED | Exact substring. |
| 11 | "'a substrate is attached to the multi-die bridge assembly after the multi-die bridge assembly passes the performance metrics' [0062]" | [0062], verbatim | SUPPORTED | Exact substring. |
| 12 | "Those numbers belong to the EMIB-T roadmap, not to this filing, whose drawings show a modest two dies on one bridge [0030]." | [0030] | SUPPORTED | Anchor correctly attached only to the patent-drawing clause; the EMIB-T-roadmap clause (120x120mm claim) is unanchored and sourced separately to fact-check-log `emib-package-roadmap-120mm`. Fence intact. |
| 13 | "'Passive bridge components are easier to fabricate and lower cost but cannot achieve the maximum current (Imax) that many applications require' [0024]." | [0024], verbatim | SUPPORTED | Exact quote. |
| 14 | "'technical challenges, such as drilling, alignment, cavity filling and soldering remain' [0024]." | [0024], verbatim | SUPPORTED | Exact quote. |
| 15 | "it 'is often used to enable power to be routed into the bridge component' from 'a source located at a bottom of a cavity in a substrate' [0035]." | [0035]: "...the optional cartoon arrow 123 is often used to enable power to be routed into the bridge component 102 from a source located at a bottom of a cavity in a substrate." | SUPPORTED | Split-quote verbatim-contiguity check: the two quoted fragments are genuinely adjacent in the source paragraph, separated only by the reference numeral "102" and the connector "from" (both correctly left outside quotation marks, not silently stitched across non-adjacent text). No fabricated contiguity. |
| 16 | "Even here the attach options stay open: solder at the cavity floor as drawn in FIG. 8, direct bonding in the FIG. 9 variant [0057], or a no-cavity version that solder-attaches the flipped assembly's die backsides instead, FIG. 10 [0058]." | [0057] FIG.9 hybrid-bond-in-cavity; [0058] FIG.10 inverted solder attach | SUPPORTED | Matches description of both variants. |
| 17 | "The claimed structure behind the power path is spare, just 'at least one contact on the second surface that provides an electrical pathway to the first surface' [0123]." | [0123]/Claim 2, verbatim, identical wording | SUPPORTED | Exact match; correctly labeled "claimed" since Claim 2 text is identical to Example 2. |
| 18 | "The payoff on offer is the one stated-effect sentence in the document: the routing 'reduces the number of substrate routing layers and can improve product yield' [0035]." | [0035], verbatim | SUPPORTED | Exact quote; correctly framed as the *description's* stated effect, distinct from the claim (see #17, #24). |
| 19 | "the bridge itself may be silicon, organic, or glass [0033]." | [0033]: "...may be embodied as a conventional silicon bridge, an organic bridge, a glass bridge, or some combination thereof." | SUPPORTED | Accurate paraphrase. |
| 20 | "A glass frame...is there 'to provide structural stability' [0049]." | [0049]: "...is to provide structural stability for the die 606 and die 610." | SUPPORTED | Verbatim truncated quote (dropped trailing "for the die 606 and die 610"), no meaning change. |
| 21 | "the receiving substrate can be built on a layer of glass shot through with through-glass vias, TGVs...[0054]." | [0054] TGV description | SUPPORTED | Accurate paraphrase. |
| 22 | "Example 17 even sizes it: 'a layer of glass having a thickness in a range of 20 microns to 1.4 millimeters' [0138]." | [0138]/Example 17, verbatim (also identical in actual Claim 17 text, line 225) | SUPPORTED | Exact quote. |
| 23 | "assemblies like these may provide 'the functionality conventionally associated with a monolithic system on chip (SoC)' [0059]." | [0059], verbatim | SUPPORTED | Exact quote. |
| 24 | "The 1-to-10-micron pitch lives in the description's examples, and no claim carries it [0034]." | [0034] + claim-scope map (pitch absent from Claim 1 text) | SUPPORTED | Verified directly against actual Claim 1 text (line 209) — no pitch value appears in the claim. Honors the "1-10 µm is description-only, not a claim limit" instruction precisely. |
| 25 | "The hybrid-bonding language sits in the apparatus claim, which requires the 'directly bonded' stack but attaches no pitch to it [0122]." | [0122]/Claim 1 | SUPPORTED | Same verification as #24/#7 — claim 1 requires direct bonding, states no pitch. |
| 26 | "The through-via claim never says power, TSV, or cavity; it locks in only 'at least one contact on the second surface that provides an electrical pathway to the first surface' [0123], and the power-from-the-floor purpose is the description talking [0035]." | [0123]/Claim 2 (verified verbatim against actual Claim 2 text, line 210) + [0035] (description purpose) | SUPPORTED | Precisely separates claim scope (bare electrical-pathway limitation) from description-only purpose — the exact discipline the claim-scope map requires; not an overreach. |
| 27 | "The glass-and-TGV claim, claim 17 as filed, hangs off the no-cavity inverted package of claim 16, not off the cavity packages described above. The parallel Example paragraph is written broader [0138]." | Actual Claims text (lines 224-225): Claim 17 "The semiconductor package of claim 16..."; Example 17 [0138]: "the semiconductor package of any one of Examples 12-16..." | SUPPORTED | Verified directly against the patent's actual Claims section — Claim 17 depends ONLY on Claim 16 (no-cavity inverted package), while Example 17 is written broader ("any one of Examples 12-16"). This is exactly the special-attention item in the task brief, and the essay states it correctly. |
| 28 | "Bridge to dies first, then 'testing the multi-die bridge assembly', then a substrate 'when the multi-die bridge assembly passes the performance metrics' [0142], with the cavity seating one dependent claim away, 'placing the bridge component in the cavity' [0144]." | [0142] Ex.21 (both fragments verbatim substrings); [0144] Ex.23, verbatim | SUPPORTED | All three quoted fragments verified verbatim; "one dependent claim away" correctly describes Claim 20 depending directly on Claim 19 (verified against actual Claims text, line 227-228). |

## Claim-scope / claim-1 block-quote verification

- No standalone "Claim 1" block quote appears in the essay; the two block quotes (rows #4, #5) are drawn
  from Example 21 (mirrors Claim 19, the method claim) and are correctly labeled "Example 21 [0142]" rather
  than "Claim 19" — the invention-summary's required attribution convention, honored because Example 21's
  wording differs trivially from the actual Claim 19 text ("a first portion of the first IC and a first
  portion of the second IC" vs. claim 19's "the first IC die and the second IC die").
- Every claim-scope statement in the essay (rows #24-#27) was cross-checked directly against the patent's
  actual `### Claims` section (input/patent.md lines 207-228), not just the mirroring Examples, and each
  is accurate: pitch is claim-1-absent, claim 2 is bare (no power/TSV/cavity), claim 17 depends on claim 16
  only (not the broader Example numbering), and claim 20 depends on claim 19.

## EMIB / EMIB-T fence check (external facts)

All EMIB and EMIB-T sentences were located and checked for (a) a fact-check-log match and (b) absence of
any `[dddd]` patent anchor on the EMIB-bearing clause itself:

| External fact in essay | Fact-check-log ID | Anchor present on the EMIB clause? |
|---|---|---|
| "Fifteen months before Intel put EMIB-T on a conference stage..." / ECTC May 2025 detail | `emib-t-ectc-2025`, `us20250266395-bibliographic` | No — the only anchor in that sentence ([0142]) sits on the trailing patent-based clause, not the EMIB-T clause. |
| "the little bridge die is buried in the board, and the chips land on top" / "the bridge is embedded in a cavity in the substrate first, and build-up layers are laminated over it" | `emib-chips-last-flow` | No |
| "EMIB-T, unveiled in May 2025, keeps that chips-last order and gives the embedded bridge TSVs, so power arrives from the package bottom" | `emib-t-ectc-2025` | No |
| "Intel has discussed rolling out EMIB packages up to roughly 120 by 120 millimeters from 2026, carrying as many as twelve HBM memory stacks" | `emib-package-roadmap-120mm` (tier-3, correctly labeled "single-outlet report") | No |
| "Intel announced glass-core substrates...in September 2023" | `intel-glass-substrate-2023` | No |
| "Among the thirteen inventors is Ravindranath Mahajan...foundation of EMIB" / "This came out of Intel's mainline packaging organization" | `mahajan-intel-fellow` | No — wording matches the fact-log's stated ceiling exactly ("nothing stronger"). |
| "published in August 2025, eighteen months after its February 2024 filing, with no granted claim yet" / "filed counterparts in Japan, Korea, China and Germany" | `us20250266395-bibliographic` | No |
| "At 95 percent per die, a four-die package comes out about 81 percent good, and a twenty-die package about 35 percent" | `kgd-yield-multiplier` (tier-4, explicitly disclaimed as "the industry's and this essay's, not the patent's") | No |

Inventor count verified independently: the patent's bibliographic inventor list (13 names) matches the
essay's "thirteen inventors" exactly. No fence breach found anywhere — every EMIB/EMIB-T-bearing clause
traces to a fact-check-log entry and carries no patent paragraph anchor.

## Summary

- **SUPPORTED: 28 / 28** anchored sentences, quoted spans, and claim-scope statements checked.
- **UNSUPPORTED: 0**
- **MISREAD: 0**
- **OVERREACHED-BEYOND-ANCHOR: 0**
- EMIB/EMIB-T fence: 8/8 external-fact clusters checked, all traced to fact-check-log entries, zero anchor
  breaches.
- Special-attention items all verified directly against the patent's actual Claims section (not just the
  mirroring Examples): the split [0035] quote is genuinely contiguous (numeral-only gap); claim 17 hangs
  off claim 16 (not the broader Example numbering); the 1-10 µm pitch is confirmed absent from Claim 1 text;
  the two glass-thickness ranges ([0054] description "~20 µm-1.5 mm" vs. [0138]/Claim 17 "20 µm-1.4 mm")
  are never conflated or harmonized by the essay — it only ever cites the claim/Example range.
