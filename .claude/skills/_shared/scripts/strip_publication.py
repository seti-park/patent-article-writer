#!/usr/bin/env python3
"""Strip pipeline: essay-draft.md -> publication.md (reader-facing deliverable).

Replaces the legacy sed/awk/perl one-liner (see
essay-en-composer/references/strip-pipeline.md) with one portable stdlib script,
and adds the paragraph-rejoin step from proposal
2026-06-26-publication-line-wrap:

  1. strip YAML frontmatter (first --- ... --- block at the top of the file)
  2. cut everything from the `# Footnotes` heading (exclusive boundary at the
     heading so it doesn't bleed into publication.md as an empty section)
  3. strip inline [^fact-entry-id] markers, including the preceding whitespace
     (avoids the "claim text ." space-before-period artifact); IDs may contain
     uppercase (LiOH, NiRich)
  4. collapse residual multi-space runs
  5. paragraph rejoin: reflow hard-wrapped body paragraphs to ONE LINE PER
     PARAGRAPH (X Articles honors single newlines, so a mid-sentence wrap
     renders as a ragged break). Structural lines are never joined to
     neighbors: headings, blockquotes, tables, images, list items, fenced
     code, and full-line italic captions.

The `# Sources` block is preserved (it sits above `# Footnotes`).

Usage:
  strip_publication.py DRAFT.md [-o publication.md]

With no -o, writes to stdout.
"""

import argparse
import re
import sys

FOOTNOTE_MARKER_RE = re.compile(r"\s*\[\^[A-Za-z0-9-]+\]")
MULTISPACE_RE = re.compile(r" {2,}")
FENCE_RE = re.compile(r"^\s*(```|~~~)")
BULLET_RE = re.compile(r"^\s*(?:[-*+]|\d+\.)\s+")


def strip_frontmatter(lines):
    """Remove a leading --- ... --- YAML frontmatter block, if present."""
    if not lines or lines[0].strip() != "---":
        return lines
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return lines[i + 1:]
    return lines  # unterminated frontmatter: leave untouched


def cut_footnotes(lines):
    """Drop the `# Footnotes` heading and everything after it."""
    out = []
    for ln in lines:
        if re.match(r"^#\s+Footnotes\s*$", ln):
            break
        out.append(ln)
    return out


def _is_structural(line):
    s = line.strip()
    if not s:
        return True
    if s[0] in "#>|!":
        return True
    if BULLET_RE.match(line):
        return True
    # Full-line italic caption: *FIG. 3, [0042]: caption text.*
    if s.startswith("*") and s.endswith("*"):
        return True
    return False


def rejoin_paragraphs(lines):
    """Reflow hard-wrapped body paragraphs to one line per paragraph."""
    out, buf = [], []
    in_fence = False

    def flush():
        if buf:
            out.append(" ".join(buf))
            del buf[:]

    for ln in lines:
        if FENCE_RE.match(ln):
            flush()
            in_fence = not in_fence
            out.append(ln)
            continue
        if in_fence:
            out.append(ln)
            continue
        if not ln.strip():
            flush()
            out.append("")
        elif _is_structural(ln):
            flush()
            out.append(ln.rstrip())
        else:
            buf.append(ln.strip())
    flush()
    return out


def strip_publication(draft_text):
    lines = draft_text.splitlines()
    lines = strip_frontmatter(lines)
    lines = cut_footnotes(lines)
    text = "\n".join(lines)
    text = FOOTNOTE_MARKER_RE.sub("", text)
    text = MULTISPACE_RE.sub(" ", text)
    lines = rejoin_paragraphs(text.splitlines())
    # Trim leading/trailing blank lines, keep exactly one trailing newline.
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    return "\n".join(lines) + "\n"


def main(argv=None):
    p = argparse.ArgumentParser(
        description="Strip essay-draft.md to publication.md (frontmatter/"
                    "footnotes removed, paragraphs rejoined to one line each).")
    p.add_argument("draft", help="path to essay-draft.md")
    p.add_argument("-o", "--out", help="output path (default: stdout)")
    args = p.parse_args(argv)

    with open(args.draft, "r", encoding="utf-8") as fh:
        result = strip_publication(fh.read())

    if args.out:
        with open(args.out, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(result)
    else:
        sys.stdout.write(result)
    return 0


if __name__ == "__main__":
    sys.exit(main())
