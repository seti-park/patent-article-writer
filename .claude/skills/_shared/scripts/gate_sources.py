#!/usr/bin/env python3
"""Sources-block gate for the patent-essay pipeline.

Aligned with the real X-Articles Sources spec (see
essay-en-composer/references/x-articles-format-en.md §"Sources block structure"
and editorial-review/references/pass-6-lead-conclusion-format.md §6C):

  - The block header is `# Sources` (h1). It must appear EXACTLY ONCE.
  - Categories, when subgrouped, are `##` (h2) sub-headings inside the block.
  - The category enum is EXACTLY these 5 labels:
        Patents, Papers, Official statements, News & media, Technical specs
  - Subgrouping is all-or-nothing: either every source sits under a `##`
    category heading, or none do (flat list).
  - Flat-vs-subgroup heuristic: 0-3 entries may be flat; 4+ entries (which the
    spec expects to span 2+ categories) should be subgrouped (warn, not fail).

The real format puts the category on the `##` sub-heading and lists bare entries
beneath it (it does NOT put the category inline on each entry), so this gate
parses sub-headings as the category source-of-truth.

Checks:
  SOURCES-001 (fail): `# Sources` block missing, or present more than once.
  SOURCES-002 (fail): a `##` sub-group category not in the 5-label enum.
  SOURCES-003 (fail): partial subgrouping -- some entries under a `##` category
                      heading and some bare (all-or-nothing violated).
  SOURCES-004 (warn): 4+ entries left as a flat list (should be subgrouped).
"""

import argparse
import re
import sys

# ---------------------------------------------------------------------------
# Tunable constants
# ---------------------------------------------------------------------------
GATE_ID = "sources"
# The 5-label enum, verbatim (matched case-insensitively, canon casing kept).
ALLOWED_CATEGORIES = [
    "Patents",
    "Papers",
    "Official statements",
    "News & media",
    "Technical specs",
]
SUBGROUP_FLAT_MAX = 3  # 0-3 flat entries are fine

SOURCES_HEADER_RE = re.compile(r"^#\s+Sources\s*$")      # exactly h1 "# Sources"
ANY_HEADER_RE = re.compile(r"^(#{1,6})\s+(.*\S)\s*$")
LIST_ITEM_RE = re.compile(r"^\s*(?:[-*]|\d+\.)\s+(.*)$")

_ALLOWED_LOWER = {c.lower(): c for c in ALLOWED_CATEGORIES}


def _find_sources_headers(lines):
    """Return list of line indices where a `# Sources` h1 header appears."""
    return [i for i, line in enumerate(lines) if SOURCES_HEADER_RE.match(line)]


def check(draft_text: str, context: dict) -> dict:
    findings = []
    lines = draft_text.splitlines()

    headers = _find_sources_headers(lines)
    if len(headers) == 0:
        findings.append({
            "check_id": "SOURCES-001",
            "severity": "fail",
            "message": "no `# Sources` block found",
            "location": "(global)",
        })
        return {"gate": GATE_ID, "passed": False, "findings": findings}
    if len(headers) > 1:
        findings.append({
            "check_id": "SOURCES-001",
            "severity": "fail",
            "message": "`# Sources` header appears %d times (expected exactly 1)" % len(headers),
            "location": "lines %s" % ", ".join(str(h + 1) for h in headers),
        })
        # keep going against the last block for additional diagnostics

    start = headers[-1] + 1
    # Block runs until the next h1 (or EOF).
    end = len(lines)
    for j in range(start, len(lines)):
        hm = ANY_HEADER_RE.match(lines[j])
        if hm and len(hm.group(1)) == 1:
            end = j
            break

    # Walk the block: track `##`+ category sub-headings; record, per entry,
    # whether it falls under a category heading.
    under_category = False
    entries = []  # list of (lineno, body, under_category_bool)
    for idx in range(start, end):
        raw = lines[idx]
        hm = ANY_HEADER_RE.match(raw)
        if hm and len(hm.group(1)) >= 2:
            label = hm.group(2).strip()
            under_category = True
            if label.lower() not in _ALLOWED_LOWER:
                findings.append({
                    "check_id": "SOURCES-002",
                    "severity": "fail",
                    "message": "Sources category %r not in 5-label enum %s"
                               % (label, ALLOWED_CATEGORIES),
                    "location": "line %d" % (idx + 1),
                })
            continue
        lm = LIST_ITEM_RE.match(raw)
        if lm:
            entries.append((idx + 1, lm.group(1).strip(), under_category))

    # SOURCES-003: all-or-nothing subgrouping.
    if entries:
        under = sum(1 for _l, _b, u in entries if u)
        if 0 < under < len(entries):
            findings.append({
                "check_id": "SOURCES-003",
                "severity": "fail",
                "message": "partial subgrouping: %d of %d entries under a `##` category "
                           "heading (all-or-nothing required)" % (under, len(entries)),
                "location": "Sources block (lines %d-%d)" % (start, end),
            })

        # SOURCES-004: flat list that should be subgrouped (warn).
        if under == 0 and len(entries) > SUBGROUP_FLAT_MAX:
            findings.append({
                "check_id": "SOURCES-004",
                "severity": "warn",
                "message": "%d entries left as a flat list; 4+ entries across 2+ "
                           "categories should be subgrouped (verify category spread)"
                           % len(entries),
                "location": "Sources block (lines %d-%d)" % (start, end),
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
    p = argparse.ArgumentParser(description="Sources gate (%s)" % GATE_ID)
    p.add_argument("draft", help="path to the draft Markdown file")
    args = p.parse_args(argv)
    with open(args.draft, "r", encoding="utf-8") as fh:
        text = fh.read()
    result = check(text, {})
    _report(result)
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
