#!/usr/bin/env python3
"""Verbatim-quote gate: invention-summary quotes must exist in the patent text.

Closes the mechanical gap in the grounding chain (north-star goal 1):

    draft [dddd] anchors  --gate_anchors-->  invention-summary  --THIS GATE-->  patent.md

gate_anchors verifies every draft anchor exists in the invention-summary; until
this gate, nothing mechanical verified that the invention-summary's "verbatim"
quotes actually appear in the patent — a hallucinated Quotable span passed every
gate and was caught only by the editorial pass-3 judgment. This gate makes the
verbatim discipline of `thesis-architect/references/quote-anchor-conventions.md`
a hard check.

Sources checked (both parsed from invention_summary_text):
  1. `**Quotable spans:**` block entries:   - `[0016]`: "verbatim text"
  2. Quote anchor table rows:               | q-0016-1 | `[0016]` | "verbatim text" | ... |

Normalizations applied to BOTH sides before matching (the Allowed list of
quote-anchor-conventions.md, plus whitespace-run collapse so markdown re-wrapping
of the patent text cannot break a match):
  - NBSP (U+00A0) -> space
  - markdown bold markers ** stripped
  - smart double quotes (U+201C/U+201D) -> straight ", smart apostrophe
    (U+2019/U+2018) -> '
  - any whitespace run (incl. newlines) -> single space
Em dash (U+2014) is preserved as-is (patent verbatim).

Context keys consumed:
  - invention_summary_text (str, optional)
  - patent_text (str, optional): full text of input/patent.md.

Checks:
  QUOTE-000 (warn): no patent_text or no invention_summary_text provided --
                    verbatim check skipped (warn-only; cannot verify without
                    the patent).
  QUOTE-001 (fail): a quote recorded as verbatim in the invention-summary does
                    not appear in the patent text (fabricated or mutated span).
  QUOTE-002 (fail|warn): target text yields zero extractable quote anchors.
                    FAIL when patent_text is available AND anchors are required
                    (invention-summary always; essay/draft when mode is essay,
                    the default). WARN only when mode is wire (anchors optional)
                    or when the severity would otherwise be fail but we still
                    surface the gap. Invoked without a patent → QUOTE-000, not
                    this rule (vacuous pass closed — GATE-05/HARNESS-02).
"""

import argparse
import re
import sys

# ---------------------------------------------------------------------------
# Tunable constants
# ---------------------------------------------------------------------------
GATE_ID = "quotes"
# - `[0016]`: "verbatim text"
SPAN_LINE_RE = re.compile(r"^\s*-\s*`\[(\d{4})\]`\s*:\s*\"(.+)\"\s*$")
# | q-0016-1 | `[0016]` | "verbatim text" | significance |
TABLE_QID_RE = re.compile(r"^q-(\d{4})-\d+$")
MIN_QUOTE_CHARS = 8  # ignore degenerate captures shorter than this

NBSP = " "
SMART_DQUOTES = ("“", "”")
SMART_SQUOTES = ("‘", "’")


def _normalize(text):
    """Apply the allowed normalizations + whitespace collapse to one side."""
    if text is None:
        return ""
    text = text.replace(NBSP, " ")
    text = text.replace("**", "")
    for q in SMART_DQUOTES:
        text = text.replace(q, '"')
    for q in SMART_SQUOTES:
        text = text.replace(q, "'")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def _extract_quotes(summary_text):
    """Return list of (anchor, quote_text, source_desc) from the summary."""
    quotes = []
    for lineno, raw in enumerate((summary_text or "").splitlines(), start=1):
        m = SPAN_LINE_RE.match(raw)
        if m:
            quotes.append((m.group(1), m.group(2),
                           "Quotable span line %d" % lineno))
            continue
        # Table row: split on pipes; a quote-anchor row has a q-dddd-N first cell.
        if raw.lstrip().startswith("|"):
            cells = [c.strip() for c in raw.strip().strip("|").split("|")]
            if len(cells) >= 3 and TABLE_QID_RE.match(cells[0]):
                anchor_m = re.search(r"\[(\d{4})\]", cells[1])
                anchor = anchor_m.group(1) if anchor_m else cells[0][2:6]
                verbatim = cells[2].strip().strip('"')
                verbatim = verbatim.strip(SMART_DQUOTES[0] + SMART_DQUOTES[1])
                quotes.append((anchor, verbatim,
                               "Quote anchor table row %s (line %d)" % (cells[0], lineno)))
    return [(a, q, s) for a, q, s in quotes if len(q.strip()) >= MIN_QUOTE_CHARS]


def check(draft_text: str, context: dict) -> dict:
    findings = []
    context = context or {}

    summary = context.get("invention_summary_text")
    patent = context.get("patent_text")

    if summary is None or patent is None:
        missing = "patent" if summary is not None else (
            "invention-summary" if patent is not None else "patent + invention-summary")
        findings.append({
            "check_id": "QUOTE-000",
            "severity": "warn",
            "message": "no %s provided, verbatim-quote check skipped" % missing,
            "location": "(global)",
        })
        return {"gate": GATE_ID, "passed": True, "findings": findings}

    quotes = _extract_quotes(summary)
    if not quotes:
        # Vacuous zero-anchor pass is closed when anchors are required and the
        # patent is available so a match could have been verified (GATE-05).
        # mode=wire keeps warn (anchors optional). No patent → QUOTE-000 above.
        mode = (context.get("mode") or "essay").strip().lower()
        requires_anchors = mode != "wire"
        sev = "fail" if requires_anchors else "warn"
        findings.append({
            "check_id": "QUOTE-002",
            "severity": sev,
            "message": "invention-summary contains no extractable Quotable spans "
                       "or Quote anchor table rows (Phase 2 has nothing to cite)",
            "location": "invention-summary",
        })
        passed = not any(f["severity"] == "fail" for f in findings)
        return {"gate": GATE_ID, "passed": passed, "findings": findings}

    patent_norm = _normalize(patent)
    for anchor, quote, source in quotes:
        if _normalize(quote) not in patent_norm:
            findings.append({
                "check_id": "QUOTE-001",
                "severity": "fail",
                "message": "quote for [%s] not found verbatim in the patent text: \"%s%s\""
                           % (anchor, quote[:60], "..." if len(quote) > 60 else ""),
                "location": source,
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
    p = argparse.ArgumentParser(description="Verbatim-quote gate (%s)" % GATE_ID)
    p.add_argument("draft", help="path to the draft Markdown file (unused; kept for the shared contract)")
    p.add_argument("--invention-summary", help="path to invention-summary.md")
    p.add_argument("--patent", help="path to patent.md")
    args = p.parse_args(argv)

    with open(args.draft, "r", encoding="utf-8") as fh:
        text = fh.read()
    ctx = {}
    if args.invention_summary:
        with open(args.invention_summary, "r", encoding="utf-8") as fh:
            ctx["invention_summary_text"] = fh.read()
    if args.patent:
        with open(args.patent, "r", encoding="utf-8") as fh:
            ctx["patent_text"] = fh.read()

    result = check(text, ctx)
    _report(result)
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
