---
proposal_id: 2026-06-26-publication-line-wrap
created: 2026-06-26T00:00:00Z
status: applied  # 2026-07-02 architecture refactor; shipped as _shared/scripts/strip_publication.py + reference edits
lever: reference-edit + pipeline
goal: "4a"
root_cause_artifact: essay-en-composer/references/x-articles-format-en.md (no line-wrap convention) + references/strip-pipeline.md (no paragraph-rejoin step)
recurrence_count: 1
confidence: high
triggering_findings:
  - essay_id: us12560948b2, pattern_tag: publication-hard-wrap (mid-paragraph hard wraps render ragged in X Articles)
---

## Problem

The deliverable was hard-wrapped at ~95 columns. In X Articles (and any renderer that treats a
single newline as a line break) the mid-sentence wraps render as ragged breaks. Publication
markdown wants **one line per paragraph**, blank line between paragraphs. Nothing in the format
reference states this, and the strip pipeline (which already removes frontmatter and footnote
markers) does not normalize wrapping, so the convention depends on whoever drafts.

## Proposed change (exact diff)

**File 1: `.claude/skills/essay-en-composer/references/x-articles-format-en.md`** — add under
"Markdown rendering":

```markdown
**Line wrapping (publication.md)**. One line per paragraph, blank line between paragraphs. No
intra-paragraph hard wraps (X Articles honors single newlines, so a mid-sentence wrap renders as a
ragged break). A block quote is one `>` line for the quote plus one `>` line for the attribution.
Headings, list items, and italic captions each stay on their own line.
```

**File 2: `.claude/skills/essay-en-composer/references/strip-pipeline.md`** — add a rejoin step so
the convention is enforced mechanically, not by hand. Append after the existing pipeline:

```markdown
### Paragraph rejoin (publication only)

The hand-wrapped draft is reflowed to one line per paragraph as the last strip step. A blank line
separates paragraphs; lines that begin with `#`, `>`, `-`, `*`, digits+`.`, `!` (image), or `|`
(table) are structural and are NOT joined to neighbors; everything else in a block is joined with a
single space.
```

Reference reflow helper (Python, mirrors the existing pipeline's reproducibility):

```python
import sys
out, buf = [], []
def flush():
    if buf: out.append(" ".join(buf)); buf.clear()
for ln in sys.stdin.read().splitlines():
    s = ln.strip()
    if not s: flush(); out.append("")
    elif s[0] in "#>-*|!" or (s[:2].rstrip(".").isdigit()):
        flush(); out.append(ln)
    else: buf.append(s)
flush(); print("\n".join(out))
```

## Why this lever

- Half rule, half mechanics. The format reference states intent (so the composer drafts right); the
  strip step guarantees it on `publication.md` regardless of draft wrapping, the same way the
  pipeline already guarantees marker/frontmatter removal.
- Not a gate: a mid-paragraph wrap is not wrong in `essay-draft.md` (the verification anchor) and a
  regex gate would false-positive on legitimate short lines (headings, captions). The strip step is
  the right enforcement point.

## Regression expectation

- Docs + an optional helper script; `test_gates.py` and `meta/regression.py` unchanged (gates do
  not read wrapping). Success criterion: `publication.md` from the next run has one line per body
  paragraph; pasting into X Articles shows no ragged mid-sentence breaks.
