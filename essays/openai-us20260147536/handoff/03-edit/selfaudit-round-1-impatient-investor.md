# Self-audit — Round 1 — Persona: IMPATIENT INVESTOR

- essay: `handoff/03-edit/essay-final.md` (essay_id: openai-us20260147536, closing_posture: firm)
- reader: busy retail investor, HS-to-early-undergrad technical comprehension, wants the payoff
  fast, distrusts hype.
- method: pass-7 adversarial checklist read through the persona + grounding spot-checks.
- isolation: blind to other self-audit readers and prior rounds.

## Verdict summary

3 findings, all severity LOW. No high/medium. No grounding findings. No over-hedge finding
(verdict is firm and evidence-proportionate). Essay is fundamentally clean for this persona.

## Grounding spot-checks (all PASS — recorded, not findings)

- Anchors verified verbatim against `input/patent.md` in 4+ sections (well past the 3-section
  bar): `[0011]` (claim-triad quotes), `[0012]`/`[0015]` (double-buffer summary), `[0199]`/
  `[0200]` (Emax=22, shift computation), `[0145]` (INT35+INT5→FP22), `[0147]` (VMM/cycle),
  `[0154]` (256 VMM, 100% util), `[0005]`/`[0006]` (conversion-cost quotes), `[0130]`/`[0131]`
  (FP8/6/4 formats), `[0133]` (von Neumann), `[0139]` (synthesizable integer adder tree),
  `[0141]`/`[0142]` (MX block, input buffer), `[0183]` (64×64 adders saved).
- Claim-scope statements vs actual claims (patent lines 505/516/525): claims 1, 20, 29 are
  independent; each carries the multiply-align-add triad; claim 20 folds in the "shift
  calculation and select decoding unit," claim 29 the "shift register." Essay's §3 statements
  match exactly. "not the mode decoding unit and not the format switching" — confirmed: none
  of claims 1/20/29 recite a mode decoding unit or format switching. Claim scope map "open"
  items honored.
- Pins: Claim scope map lists all pins as "none." Essay presents `22`/`5-bit` scoped to
  "FP8 activation times an FP6 weight" and `256 VMM` as "the description's example" — no
  pinned/example value narrated as a claim bound. PASS.
- Dual-bitcell / double-buffering correctly labeled "in its summary passages rather than in
  the claims it is seeking" (§4), honoring the map's "not in the pending claim set" note. PASS.

## Checklist results

| # | Check | Verdict | Evidence |
|---|---|---|---|
| 1 | Hook / lead earns scroll; two-sided call by lead end | PASS (w/ LOW note IABI-02) | ¶1 "There is a published OpenAI patent that designs an AI chip down to the individual memory cell." → declarative; two-sided call lands: "The filing is primary evidence that 'OpenAI-designed' is literal... It is also a pending application rather than a granted patent, which prices the evidence without changing what it shows." |
| 2 | Header-as-claim | PASS | All six `##` headers are assertions; header-only skim reconstructs the argument (design predates news → mechanism → described vs claimed → per-cycle target → pending but deep → literal engineering + two dates). |
| 3 | Steelman present + specific + not overweight | PASS | "A skeptic can fairly call the core a known technique, implemented." THIS-patent objection (format agility is description-only; MX standardized 2023, before priority). Rebutted at ≥ equal weight: "What this filing claims is machinery that executes those blocks natively inside a memory macro." |
| 4 | No meta / filler | PASS | No say-nothing sentence found. "The registry facts, stated once." is a mild self-reference but functions as a scope signpost (exempt). |
| 5 | Jargon as signpost | PARTIAL → IABI-01 | Most terms glossed (mantissa/exponent/primitive product/VMM/CIM/activations/weights/FP8-6-4). "bitcell" left un-glossed. |
| 6 | No stub / rhythm break | PASS | No section markedly shorter than siblings; lead 2¶ is a normal lead. |
| 7 | Thesis not over-restated; repeatable sentence | PASS (w/ LOW note IABI-03) | Repeatable closer present: "The chip story was told in 2025. The design record says the work started earlier, and the record is the harder document to argue with." |
| — | Over-hedge (first-class, symmetric) | PASS | Verdict firm: "The bounds priced in the previous section scope that call, and they do not reverse it." One patent-specific guard only (Jalapeño/no-silicon). No safe-harbor boilerplate. |

## Findings

### IABI-01 — jargon-overdepth (LOW)
- **location**: §1 lead, ¶2 ("The Design Was on File Before It Was News"); recurs in FIG. 43
  caption and §4.
- **quoted span**: "the math engine was already on file, **written to the bitcell**."
- **why**: "bitcell" is on the pass-7 explicit jargon list and is never glossed. The lead
  earlier says "down to the individual memory cell," but §4 later reveals a memory cell is
  "built from two bitcells each" — so bitcell ≠ memory cell, and the impatient investor meets
  the undefined term in the lead where the money thread is forming. Minor because context makes
  it roughly parseable ("smallest hardware level").
- **fix (tighten/gloss)**: on first use, either use "memory cell" in the lead or add a
  3-word gloss (e.g., "the single-bit storage cell"). Do NOT add a hedge.

### IABI-02 — lead attention-budget / caption density (LOW)
- **location**: top-of-essay figure caption (the literal first text block under the title,
  ahead of ¶1).
- **quoted span**: "Each product's mantissa shifts onto the block's largest exponent (at most
  22 here, a 5-bit integer [0199]), and the column adder tree sums the aligned mantissas as
  plain integers [0011], one 35-bit result per column [0145]."
- **why**: for the impatient investor this is the first thing on screen, and it front-loads
  un-glossed "mantissa"/"exponent" plus five semantic numerals (22, 5-bit, claim 1, 35-bit)
  and three anchors — the glosses for mantissa/exponent do not arrive until §2. Taxes the
  attention budget before the hook paragraph earns the scroll (goal-5 SURF-003 neighborhood).
  Low because the hook paragraph immediately below is strong and recovers momentum.
- **fix (tighten/cut)**: trim the caption to the align-once idea and defer the bit-width
  numerals to §2 where the terms are glossed; keep "This is claim 1's align-then-integer-
  accumulate step, made literal." Do NOT add a hedge.

### IABI-03 — thesis-restatement motif (LOW)
- **location**: recurs across lead, §3 close, §5 close, closing.
- **quoted spans**: lead "the filing is primary evidence that 'OpenAI-designed' is literal";
  §5 "this one reads like engineering rather than positioning"; closing "'OpenAI-designed' is
  literal engineering, and this filing is the primary evidence."
- **why**: the "literal engineering / not positioning / the record is the harder document"
  verdict beat is asserted in ~3-4 sections, sitting at the ≤3-section restatement ceiling
  (some may be declared signature lines and exempt — cannot confirm without thesis-trace.md).
  For the impatient investor it edges toward feeling hammered.
- **fix (tighten)**: if the §5 "reads like engineering rather than positioning" clause is not
  a declared signature line, compress it so the depth evidence carries the point without
  re-asserting the headline verdict. Do NOT add a hedge.

## Note (not a finding)
Money-relevance thread is present but implicit (chip-program credibility, "OpenAI-designed"
is literal). It is never tied to valuation/stock, which is appropriate for an evidence-
posture essay — flagging explicitly would risk hype and is out of jurisdiction. No action.
