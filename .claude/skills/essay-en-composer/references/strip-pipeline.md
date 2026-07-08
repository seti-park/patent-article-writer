# Strip pipeline

Referenced by tech-essay-en SKILL.md Step 7 (Emit draft + publication.md). Two-file output workflow with reproducible regex pipeline.

## Two-file design

Step 7 emits two markdown files.

### draft.md (verification anchor)

- Frontmatter present with mode and posture metadata
- Inline `[^fact-entry-id]` markers at every cited claim
- Sources block listing referenced patents, papers, posts
- Footnote definitions block at the bottom: `[^fact-entry-id]: fact-base entry — <brief context>`

draft.md is the file deterministic-gate consumes for CheckID 2, 4, and 6 verification.

### publication.md (reader-facing)

- Frontmatter stripped
- `[^...]` inline markers stripped from body prose
- Footnote definitions block stripped (boundary at `# Footnotes` heading)
- Sources block preserved (sits above the Footnotes heading)
- Figure markdown and italic captions preserved per `figure-rendering.md` rules

publication.md is the file SETI pastes into X Articles at publication time.

## Reproducible pipeline

Canonical (portable, includes the paragraph-rejoin step):

```bash
python .claude/skills/_shared/scripts/strip_publication.py draft.md -o publication.md
```

Legacy shell equivalent (no rejoin step; reference only):

```bash
sed '/^---$/,/^---$/d' draft.md \
  | awk '/^# Footnotes/ { exit } { print }' \
  | perl -pe 's/\s*\[\^[A-Za-z0-9-]+\]//g' \
  | sed -E 's/ +/ /g' \
  > publication.md
```

### Paragraph rejoin (publication only)

The hand-wrapped draft is reflowed to one line per paragraph as the last strip step. A blank line
separates paragraphs; lines that begin with `#`, `>`, `!` (image), or `|` (table), list items
(`-` / `*` / `+` / `N.` followed by a space), fenced code, and full-line italic captions are
structural and are NOT joined to neighbors; everything else in a block is joined with a single
space. Rationale: X Articles honors single newlines, so an intra-paragraph hard wrap renders as a
ragged mid-sentence break (proposal `2026-06-26-publication-line-wrap`).

## Pipeline notes

Validated on the 050 Tesla CAM essay (2026-05). Three regex decisions worth preserving.

### awk boundary at heading, not first definition

`awk '/^# Footnotes/ { exit }'` exits at the `# Footnotes` heading, not at the first `[^id]:` definition line. If the boundary were the first definition line, the `# Footnotes` heading itself would bleed into publication.md as an empty section.

### perl regex character class

`perl -pe 's/\s*\[\^[A-Za-z0-9-]+\]//g'` covers two cases.

- **Case-insensitive entry IDs**: uppercase letters allowed (`LiOH`, `NiRich`). A lowercase-only character class would skip these.
- **Preceding whitespace strip**: `\s*` before the marker prevents the `claim text [^cite].` → `claim text .` artifact (space-before-period).

### Final sed multi-space collapse

`sed -E 's/ +/ /g'` collapses any residual multi-space sequences from edge cases.

## Why two files

The two-file split keeps verification anchors auditable while delivering a clean reader artifact. draft.md preserves the full citation chain for deterministic-gate, retrospective audit, and downstream Korean adaptation. publication.md is the deliverable.

Pattern validated: 368 Tesla cutting essay pilot (2026-05).
