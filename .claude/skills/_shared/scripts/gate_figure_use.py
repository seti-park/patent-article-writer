#!/usr/bin/env python3
"""Figure-use gate for the patent-essay pipeline (north-star goal 2 support).

Goal 2 -- "the essay must make sufficient use of the patent's figures and
specification" -- has a deterministic component: every figure the Phase 1 Design
selected (`handoff/01-design/figure-selection.md`) must actually be referenced
in the composed draft. A selected-but-unused figure is an ORPHAN and fails.

The reverse is also flagged: a figure the draft references that the design never
selected means the composer pulled in an off-plan figure (warn -- the figure may
be legitimate but the selection record is now out of sync).

This complements gate_anchors' FIGREF-001 (which checks refs against the set of
AVAILABLE figures); this gate checks refs against the set of SELECTED figures and
checks for orphans in the other direction.

Context keys consumed:
  - figure_selection_text (str, optional): text of figure-selection.md. The
    selected set is taken from the "## Selected figures" section only (up to
    the next H2); if that heading is absent, the whole file is scanned
    (legacy bare-list fallback).

Figure numbers are parsed from any of: "fig-07", "FIG. 7", "Figure 7", "Fig 7"
(case-insensitive), N an integer.

Checks:
  FIGUSE-000 (warn): no figure-selection provided -- check skipped.
  FIGUSE-001 (fail): a SELECTED figure is never referenced in the draft (orphan).
  FIGUSE-002 (warn): a figure REFERENCED in the draft is not in the selection.
"""

import argparse
import re
import sys

# ---------------------------------------------------------------------------
# Tunable constants
# ---------------------------------------------------------------------------
GATE_ID = "figure_use"
# Matches "fig-07", "FIG. 7", "Figure 7", "Fig 7", and panel-suffixed "FIG. 7C".
# The optional single panel letter is needed because a trailing letter removes the
# \b word boundary after the digits, making "FIG. 4B" invisible and falsely
# orphaning figure 4 (ledger: figure-token-regex-blindspot, 3 recurrences).
FIG_RE = re.compile(r"\bfig(?:ure|\.|-)?\s*0*(\d+)[a-z]?\b", re.IGNORECASE)
# The selected set must come ONLY from the "## Selected figures" section, not from any
# later section ("Reviewed but NOT selected", "Paired-figure relationships (acknowledged)",
# "Figure relationships") that also names the dropped figures.
# Ledger: figuse-selection-scope-overread / figure-selection-parse-overreach
# (2026-07-05-figuse-selection-scope-promote).
_SEL_HEADING_RE = re.compile(r"^##\s+Selected figures\s*$", re.IGNORECASE | re.MULTILINE)
_NEXT_H2_RE = re.compile(r"^##\s+", re.MULTILINE)


def _selected_region(text):
    """Substring from the '## Selected figures' heading to the next '## ' heading.

    If that heading is absent (legacy/bare-list selection), return the whole text so
    behavior is unchanged for un-sectioned inputs. Section-name-agnostic for the
    dropped-figure region: it stops at ANY next H2, whatever it is called.
    """
    if not text:
        return text or ""
    m = _SEL_HEADING_RE.search(text)
    if not m:
        return text
    start = m.end()
    nxt = _NEXT_H2_RE.search(text, start)
    return text[start:nxt.start()] if nxt else text[start:]


def _figure_numbers(text):
    """Return the set of figure numbers mentioned in text."""
    return {int(m.group(1)) for m in FIG_RE.finditer(text or "")}


def check(draft_text: str, context: dict) -> dict:
    findings = []
    context = context or {}

    selection_text = context.get("figure_selection_text")
    if selection_text is None:
        findings.append({
            "check_id": "FIGUSE-000",
            "severity": "warn",
            "message": "no figure-selection provided, figure-use check skipped",
            "location": "(global)",
        })
        return {"gate": GATE_ID, "passed": True, "findings": findings}

    # Only "## Selected figures" defines the selected set; later sections name dropped
    # figures and must not be counted as selected (else they false-orphan).
    selected = _figure_numbers(_selected_region(selection_text))
    used = _figure_numbers(draft_text)

    # FIGUSE-001: selected but never used (orphan).
    for num in sorted(selected - used):
        findings.append({
            "check_id": "FIGUSE-001",
            "severity": "fail",
            "message": "selected figure %d is never referenced in the draft (orphan)" % num,
            "location": "figure-selection",
        })

    # FIGUSE-002: used but not selected (off-plan figure).
    for num in sorted(used - selected):
        findings.append({
            "check_id": "FIGUSE-002",
            "severity": "warn",
            "message": "draft references figure %d, which is not in figure-selection" % num,
            "location": "draft",
        })

    passed = not any(f["severity"] == "fail" for f in findings)
    return {"gate": GATE_ID, "passed": passed, "findings": findings}


def _report(result):
    status = "PASS" if result["passed"] else "FAIL"
    print("[%s] gate=%s" % (status, result["gate"]))
    for f in result["findings"]:
        print("  %-5s %-12s %s  (%s)" % (
            f["severity"].upper(), f["check_id"], f["message"], f["location"]))
    if not result["findings"]:
        print("  (no findings)")


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description="Figure-use gate (%s)" % GATE_ID)
    p.add_argument("draft", help="path to the draft Markdown file")
    p.add_argument("--figure-selection", help="path to figure-selection.md")
    args = p.parse_args(argv)
    with open(args.draft, "r", encoding="utf-8") as fh:
        text = fh.read()
    ctx = {}
    if args.figure_selection:
        with open(args.figure_selection, "r", encoding="utf-8") as fh:
            ctx["figure_selection_text"] = fh.read()
    result = check(text, ctx)
    _report(result)
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
