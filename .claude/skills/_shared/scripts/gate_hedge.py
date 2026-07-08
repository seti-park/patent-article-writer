#!/usr/bin/env python3
"""Over-hedge gate: the verdict section must not collapse into safe-harbor boilerplate.

Mechanical half of the editorial 6G over-hedge sub-check (proposal
2026-06-24-conclusion-over-hedge-check). Passes 3/4 defend against claiming too
much; this gate defends against concluding too little — the recurring failure
where the closing drifts to "a patent does not guarantee production / a rising
stock price" no matter what the body established.

Scope: ONLY the verdict section — the last `##` body section before the
`# Sources` h1. Limits belong in a dedicated limits section earlier in the
essay; stating them there is correct and this gate never reads that section.

Posture coupling: the draft frontmatter may declare `closing_posture: firm`
(pinned from `thesis-spine.md` for verdict/investor editions). When firm,
boilerplate and qualifier-led verdicts are HARD FAILS; otherwise they warn.

Quoted text (double quotes / `>` blockquotes) is exempt, consistent with the
other gates (a quoted executive or patent sentence is not the essay's verdict).

Context keys consumed: (none — self-contained; reads the draft frontmatter).

Checks:
  HEDGE-000 (warn): no `##` body section found before `# Sources` — skipped.
  HEDGE-001 (fail if closing_posture == firm, else warn): safe-harbor
             boilerplate pattern in the verdict section ("does not guarantee",
             "only time will tell", "remains to be seen", "not investment
             advice", ...).
  HEDGE-002 (fail if firm, else warn): qualifier-led verdict ("a qualified
             yes", "a cautious no") — the call must lead, the bound follows.
  HEDGE-003 (warn): hedge-word density — more than half of the verdict
             section's sentences carry a hedge token (may / might / could /
             perhaps / possibly / potentially / seems / appears / arguably),
             with at least MIN_SENTENCES sentences.
"""

import argparse
import re
import sys

# ---------------------------------------------------------------------------
# Tunable constants
# ---------------------------------------------------------------------------
GATE_ID = "hedge"

BOILERPLATE_PATTERNS = [
    (re.compile(r"\bpatents?\s+(?:do(?:es)?\s+not|don't|doesn't|never|cannot|can't)\s+guarantee", re.I),
     "patent-does-not-guarantee boilerplate"),
    (re.compile(r"\bno\s+guarantees?\b", re.I), "no-guarantee boilerplate"),
    (re.compile(r"\bnot\s+(?:financial|investment)\s+advice\b", re.I), "investment-advice disclaimer"),
    (re.compile(r"\b(?:only\s+)?time\s+will\s+tell\b", re.I), "time-will-tell boilerplate"),
    (re.compile(r"\bremains?\s+to\s+be\s+seen\b", re.I), "remains-to-be-seen boilerplate"),
    (re.compile(r"\btoo\s+early\s+to\s+(?:say|tell|know|call)\b", re.I), "too-early-to-say boilerplate"),
    (re.compile(r"\bit\s+is\s+(?:unclear|uncertain)\s+whether\b", re.I), "unclear-whether hedge"),
    (re.compile(r"\bwhether\s+[^.!?]{0,80}\bremains?\s+(?:an\s+open\s+question|unclear|uncertain)", re.I),
     "open-question hedge"),
    (re.compile(r"\bonly\s+the\s+market\s+(?:will|can)\s+(?:decide|tell)\b", re.I),
     "market-will-decide boilerplate"),
]

QUALIFIER_LED_RE = re.compile(
    r"\b(?:a|the)\s+(?:qualified|cautious|tentative|partial|hedged)\s+(?:yes|no)\b", re.I)

HEDGE_TOKEN_RE = re.compile(
    r"\b(?:may|might|could|perhaps|possibly|potentially|seems?|appears?|arguably|presumably)\b", re.I)
HEDGE_DENSITY_MAX = 0.5   # HEDGE-003: fraction of sentences carrying a hedge token
MIN_SENTENCES = 4         # HEDGE-003 needs at least this many sentences to judge

SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?])\s+")
CLOSING_POSTURE_RE = re.compile(r"^closing_posture:\s*(\S+)", re.M)
DQUOTE_SPAN_RE = re.compile(r'"[^"]*"')


def _frontmatter(draft_text):
    lines = draft_text.splitlines()
    if not lines or lines[0].strip() != "---":
        return ""
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return "\n".join(lines[1:i])
    return ""


def _closing_posture(draft_text):
    m = CLOSING_POSTURE_RE.search(_frontmatter(draft_text))
    return m.group(1).lower() if m else None


def _verdict_section(draft_text):
    """Return (start_lineno, text) of the last ## section before # Sources."""
    lines = draft_text.splitlines()
    sources_idx = len(lines)
    for i, ln in enumerate(lines):
        if re.match(r"^#\s+Sources\s*$", ln):
            sources_idx = i
            break
    section_start = None
    for i in range(sources_idx - 1, -1, -1):
        if re.match(r"^##\s+\S", lines[i]):
            section_start = i
            break
    if section_start is None:
        return None, None
    body = lines[section_start + 1:sources_idx]
    return section_start + 1, "\n".join(body)


def _strip_quoted(text):
    """Remove blockquote lines and double-quoted spans (exempt from checks)."""
    kept = [ln for ln in text.splitlines() if not ln.lstrip().startswith(">")]
    return DQUOTE_SPAN_RE.sub("", "\n".join(kept))


def check(draft_text: str, context: dict) -> dict:
    findings = []
    posture = _closing_posture(draft_text)
    firm = posture == "firm"

    start, section = _verdict_section(draft_text)
    if section is None:
        findings.append({
            "check_id": "HEDGE-000",
            "severity": "warn",
            "message": "no `##` body section found before `# Sources`; over-hedge check skipped",
            "location": "(global)",
        })
        return {"gate": GATE_ID, "passed": True, "findings": findings}

    scan = _strip_quoted(section)
    sev = "fail" if firm else "warn"

    # HEDGE-001: safe-harbor boilerplate in the verdict section.
    for pat, label in BOILERPLATE_PATTERNS:
        m = pat.search(scan)
        if m:
            findings.append({
                "check_id": "HEDGE-001",
                "severity": sev,
                "message": "verdict section contains %s: \"%s\" (state limits once in the "
                           "limits section; the verdict lands the call)" % (label, m.group(0)),
                "location": "verdict section (from line %d)" % start,
            })

    # HEDGE-002: qualifier-led verdict.
    m = QUALIFIER_LED_RE.search(scan)
    if m:
        findings.append({
            "check_id": "HEDGE-002",
            "severity": sev,
            "message": "qualifier-led verdict \"%s\" — lead with the call, then bound it"
                       % m.group(0),
            "location": "verdict section (from line %d)" % start,
        })

    # HEDGE-003: hedge-word density.
    prose = " ".join(
        ln for ln in scan.splitlines()
        if ln.strip() and not ln.lstrip().startswith(("#", "*", "-", "|", "!")))
    sentences = [s for s in SENTENCE_SPLIT_RE.split(prose) if s.strip()]
    if len(sentences) >= MIN_SENTENCES:
        hedged = sum(1 for s in sentences if HEDGE_TOKEN_RE.search(s))
        frac = hedged / float(len(sentences))
        if frac > HEDGE_DENSITY_MAX:
            findings.append({
                "check_id": "HEDGE-003",
                "severity": "warn",
                "message": "hedge-word density in verdict section: %d of %d sentences "
                           "(%.0f%%, max %.0f%%)" % (hedged, len(sentences),
                                                     frac * 100, HEDGE_DENSITY_MAX * 100),
                "location": "verdict section (from line %d)" % start,
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
    p = argparse.ArgumentParser(description="Over-hedge gate (%s)" % GATE_ID)
    p.add_argument("draft", help="path to the draft Markdown file")
    args = p.parse_args(argv)
    with open(args.draft, "r", encoding="utf-8") as fh:
        text = fh.read()
    result = check(text, {})
    _report(result)
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
