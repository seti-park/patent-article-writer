<!--
  handoff/02-compose/revision-response.round-2.md
  Produced by: essay-en-composer (revision mode, references/revision-mode.md)
  Consumed by: editorial-review round 3 (re-review protocol) + _shared/scripts/check_run.py

  One disposition block per medium/high/critical finding_id from
  handoff/03-edit/edit-log.round-2.md, plus low findings batched where noted.
-->

# Revision response — round 2

draft_version: 3  <!-- the version this revision produced -->

Round-2 review verdict was `revise-recommended`: 1 medium (r2-F1) + 2 low (r2-F2, r2-F3),
no high, no critical. All three are surface/precision findings; none touches grounding,
scope, or the verdict. Every one is dispositioned `applied` below. The two round-1 signature
lines are preserved byte-identical; `closing_posture: firm` is unchanged; no [dddd] anchor or
verbatim blockquote was altered.

## r2-F1 (medium) — cover-caption density (pass-5 / 6H cover-caption clause)

- disposition: applied
- change: Trimmed the FIG. 4 cover caption from ~86 words / 5 sentences to 52 words / 3
  sentences. Dropped the reference number "(426)" (pure inventory for the target retail
  reader) and cut the shift-arithmetic narration ("a shift-calculation block subtracts that
  product's exponent from the block's largest ... and shifts the mantissa by that amount" +
  the standalone two's-complement sentence), which carried the density the finding flagged and
  which the LONGSENT-001 splitter merged into the 72-word artifact. Kept the grounded core
  intact and anchor-for-anchor: the align-once / adder-tree idea, Emax at most 22 fitting a
  5-bit integer [0199], integer-domain accumulation on the adder tree [0011], a 35-bit integer
  result per column [0145], and the thesis-tie last sentence verbatim ("This is claim 1's
  align-then-integer-accumulate step, made literal."). The caption still describes only what
  FIG. 4 draws (shift-onto-largest-exponent → integer adder tree → 35-bit result); no claim
  beyond the drawing, no grant-status overreach. New caption:
  "FIG. 4: the align-once core, drawn as circuitry. Each product's mantissa shifts onto the
  block's largest exponent (at most 22 here, a 5-bit integer [0199]), and the column adder tree
  sums the aligned mantissas as plain integers [0011], one 35-bit result per column [0145].
  This is claim 1's align-then-integer-accumulate step, made literal."
- location: header / cover, the FIG. 4 caption block (was line 15)
- grounding fix priority: N/A — this is a pass-5 surface-density finding, not a pass-3
  grounding finding. Fix is "narrow / cut inventory", never a hedge. Grounding chain preserved
  ([0199] q-0199-1, [0011] q-0011-3, [0145] q-0145-1 all still present and verbatim-traceable).

## r2-F2 (low) — un-shown figure pointers FIG. 38 / FIG. 45

- disposition: applied
- change: Removed both prose cross-references to figures the article does not display.
  (a) §2 ¶4: deleted "; FIG. 4 draws that back end as a functional block, and FIG. 38 shows it
  as physical circuitry." — the sentence now ends at "Here the lining up is a bit shift." and
  continues cleanly into the max-exponent sentence. The FIG. 4 token remains present in the
  header image + caption, so FIG. 4 is not orphaned; only the redundant in-prose FIG. 4/FIG. 38
  pointer is gone. (b) §5 ¶3: deleted "; FIG. 45 draws one such scan-wired double bitcell.",
  keeping the [0118] verbatim scan-test quote ("serve both compute storage and scan-test
  roles") and closing the sentence with a period before "Concept filings rarely carry...".
  Both deletions also remove the two "slightly mechanical" prose semicolon joins the reviewer
  noted (pass-1 residue). No [dddd] anchor and no verbatim quote was removed. After the edit,
  the only figure tokens in the draft are FIG. 1, FIG. 3, FIG. 4, FIG. 43 — the four
  selected + placed figures.
- location: §2 ¶4 (was line 42); §5 ¶3 (was line 79)
- upstream note: the composer-flagged upstream fix in figures-rationale.md (design-architect
  reword the unselected-figure discussion in figure-selection.md so "FIG. 38/42" / "FIG. 45/46"
  no longer tokenize as selected) is what allows this removal without re-triggering a
  FIGUSE-001 orphan. The orchestrator reports the tokenization was corrected upstream, so the
  cross-references are no longer load-bearing and are dropped here.

## r2-F3 (low) — date-arithmetic uniformity in §6

- disposition: applied
- change: §6 closing — "priority date eleven months older" → "priority date about eleven months
  older", matching the hedged "about eleven months later" established in §1 ¶1 (r1-F6) and the
  fact-check-log's "about eleven months" (true gap ~10 months 21 days). This is a precision
  qualifier on date arithmetic, NOT a hedge on the verdict: the surrounding call ("'OpenAI-
  designed' is literal engineering, and this filing is the primary evidence") is untouched, and
  §6 still states the raw dates two sentences later ("The announcement is from October 2025. The
  engineering is dated November 2024."), so the ~11-month gap stays reader-verifiable. Jurisdiction
  fence honored; gate_hedge posture unaffected.
- location: §6 ¶1 (was line 83)

## Recount after structural edits

- §2 ¶4 (bit-shift paragraph): 3 sentences after removing the FIG. clause — in the 3-7 band; no
  neighbor regressed.
- §5 ¶3 (tape-out-depth paragraph): 5 sentences after removing the FIG. 45 clause — in band; no
  neighbor regressed.
- FIG. 4 cover caption: 3 sentences (caption, not a body paragraph); no orphan created — FIG. 4
  still referenced in the header image + caption.
- Figure-token audit: FIG. 1, FIG. 3, FIG. 4, FIG. 43 only. No orphaned selected figure.
- Both declared signature lines present exactly once and byte-identical.

## Volunteered changes (beyond findings)

- None. All three findings applied as specified; no additional prose moved. thesis-trace.md and
  figures-rationale.md updated to drop the FIG. 38 / FIG. 45 cross-references and to note the
  trimmed FIG. 4 caption.
