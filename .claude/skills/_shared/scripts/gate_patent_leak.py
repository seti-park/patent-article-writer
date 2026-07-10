#!/usr/bin/env python3
"""Patent-leak gate: draft must not paste raw patent text outside Quotable spans.

Enforces invariant 3 (composer never reads the raw patent): any maximal
token n-gram (n >= MIN_NGRAM_WORDS) that appears verbatim in both the draft
and the patent must also appear inside a Quotable span / quote-anchor block
of the invention-summary. A match not covered by any authorized span is a
hard fail.

Legitimate path: a draft that quotes a span already recorded in the
invention-summary (the only authorized verbatim path) must NOT fire.
Blockquotes that cite an anchor `[dddd]` present in the summary are also
exempt (the anchor proves the quote was mediated through the summary).

Context keys consumed:
  - invention_summary_text (str, optional)
  - patent_text (str, optional)

Standalone CLI (stdlib only; same exit conventions as gate_quotes):
  gate_patent_leak.py --draft DRAFT --patent PATENT --invention-summary SUMMARY

Checks:
  LEAK-000 (warn): patent_text or invention_summary_text missing -- leak
                   check skipped (never a vacuous pass claim).
  LEAK-001 (fail): a maximal n-gram (n >= 12 words) appears verbatim in both
                   the draft and the patent but is not covered by any Quotable
                   span / quote-anchor block of the invention-summary.
"""

import argparse
import re
import sys

GATE_ID = "patent_leak"
MIN_NGRAM_WORDS = 12

# Reuse the same span-line / table extractors shape as gate_quotes (independent
# copy so this gate stays stdlib-self-contained and does not import sibling
# modules at check time beyond optional registration).
SPAN_LINE_RE = re.compile(
    r"^\s*-\s*`\[(\d{4})\]`\s*:\s*\"([^\"]*)\"")
TABLE_QID_RE = re.compile(r"^q-(\d{4})-\d+$")
ANCHOR_RE = re.compile(r"\[(\d{4})\]")
# Tokenization: alphanumeric runs (case-folded later) — punctuation-insensitive.
TOKEN_RE = re.compile(r"[A-Za-z0-9]+")


def _normalize_tokens(text):
    """Return list of lowercased alphanumeric tokens (punct/ws-insensitive)."""
    if not text:
        return []
    return [t.lower() for t in TOKEN_RE.findall(text)]


def _token_string(tokens):
    return " ".join(tokens)


def _extract_authorized_spans(summary_text):
    """Return list of normalized token-lists from Quotable spans / table rows."""
    spans = []
    anchors = set()
    for raw in (summary_text or "").splitlines():
        m = SPAN_LINE_RE.match(raw)
        if m:
            anchors.add(m.group(1))
            toks = _normalize_tokens(m.group(2))
            if toks:
                spans.append(toks)
            continue
        if raw.lstrip().startswith("|"):
            cells = [c.strip() for c in raw.strip().strip("|").split("|")]
            if len(cells) >= 3 and TABLE_QID_RE.match(cells[0]):
                anchor_m = re.search(r"\[(\d{4})\]", cells[1])
                if anchor_m:
                    anchors.add(anchor_m.group(1))
                verbatim = cells[2].strip().strip('"')
                toks = _normalize_tokens(verbatim)
                if toks:
                    spans.append(toks)
        for a in ANCHOR_RE.findall(raw):
            anchors.add(a)
    return spans, anchors


def _span_covers(ngram_tokens, authorized_spans):
    """True if the n-gram token sequence appears inside any authorized span."""
    if not ngram_tokens:
        return False
    needle = _token_string(ngram_tokens)
    for span in authorized_spans:
        if len(span) < len(ngram_tokens):
            # n-gram longer than span cannot be covered by it as a whole,
            # but a shorter authorized span may still be a sub-sequence —
            # coverage means the leak n-gram is a sub-sequence of an
            # authorized span (draft quotes a recorded span), OR the
            # authorized span is a sub-sequence of the n-gram (draft
            # elaborates slightly around a recorded quote). Both count.
            hay = needle
            sub = _token_string(span)
            if sub and sub in hay:
                return True
            continue
        hay = _token_string(span)
        if needle in hay:
            return True
    return False


def _blockquote_regions(draft_text):
    """Yield (start_char, end_char, region_text) for contiguous blockquote blocks."""
    lines = (draft_text or "").splitlines(keepends=True)
    regions = []
    buf = []
    start = 0
    pos = 0
    for line in lines:
        is_bq = line.lstrip().startswith(">")
        if is_bq:
            if not buf:
                start = pos
            buf.append(line)
        else:
            if buf:
                text = "".join(buf)
                regions.append((start, start + len(text), text))
                buf = []
        pos += len(line)
    if buf:
        text = "".join(buf)
        regions.append((start, start + len(text), text))
    return regions


def _char_spans_for_tokens(text, tokens):
    """Map token index → (start, end) char offsets in original text.

    Walks the original text with TOKEN_RE so offsets stay aligned.
    """
    spans = []
    for m in TOKEN_RE.finditer(text or ""):
        spans.append((m.start(), m.end()))
    # tokens were derived the same way; lengths should match.
    if len(spans) != len(tokens):
        # Defensive: rebuild tokens from the same scan.
        tokens = [t.lower() for t in TOKEN_RE.findall(text or "")]
        spans = [(m.start(), m.end()) for m in TOKEN_RE.finditer(text or "")]
    return tokens, spans


def _find_maximal_shared_ngrams(draft_tokens, patent_token_set_join, patent_tokens):
    """Find maximal n-grams (n >= MIN) in draft that appear in patent.

    Returns list of (start_idx, end_idx_exclusive, tokens_slice).
    Maximal = not extendable left or right while remaining a patent match.
    """
    if not draft_tokens or not patent_tokens:
        return []
    # Sliding window over patent for membership of n-gram strings.
    patent_ngrams = set()
    pt = patent_tokens
    # Precompute all patent n-grams of length >= MIN for membership tests.
    # For long patents this is O(P * avg_len); patents are tens of KB — fine.
    for i in range(len(pt)):
        # Build incrementally from MIN length upward for each start.
        if i + MIN_NGRAM_WORDS > len(pt):
            break
        # Store all suffixes from this start of length >= MIN
        acc = []
        for j in range(i, len(pt)):
            acc.append(pt[j])
            if len(acc) >= MIN_NGRAM_WORDS:
                patent_ngrams.add(" ".join(acc))

    matches = []
    n = len(draft_tokens)
    i = 0
    while i < n:
        if i + MIN_NGRAM_WORDS > n:
            break
        # Grow the longest match starting at i.
        longest_end = None
        for end in range(i + MIN_NGRAM_WORDS, n + 1):
            key = " ".join(draft_tokens[i:end])
            if key in patent_ngrams:
                longest_end = end
            else:
                break
        if longest_end is not None:
            matches.append((i, longest_end, draft_tokens[i:longest_end]))
            i = longest_end  # non-overlapping maximal scan
        else:
            i += 1
    return matches


def check(draft_text: str, context: dict) -> dict:
    findings = []
    context = context or {}
    summary = context.get("invention_summary_text")
    patent = context.get("patent_text")

    if summary is None or patent is None:
        missing = "patent" if summary is not None else (
            "invention-summary" if patent is not None
            else "patent + invention-summary")
        findings.append({
            "check_id": "LEAK-000",
            "severity": "warn",
            "message": "no %s provided, patent-leak check skipped" % missing,
            "location": "(global)",
        })
        return {"gate": GATE_ID, "passed": True, "findings": findings}

    authorized_spans, summary_anchors = _extract_authorized_spans(summary)
    draft_tokens, draft_char_spans = _char_spans_for_tokens(
        draft_text, _normalize_tokens(draft_text))
    patent_tokens = _normalize_tokens(patent)

    # Blockquote regions whose text cites a summary anchor → exempt.
    exempt_char_ranges = []
    for start, end, region_text in _blockquote_regions(draft_text):
        region_anchors = set(ANCHOR_RE.findall(region_text))
        if region_anchors & summary_anchors:
            exempt_char_ranges.append((start, end))

    def _in_exempt(char_start, char_end):
        for a, b in exempt_char_ranges:
            if char_start >= a and char_end <= b:
                return True
        return False

    shared = _find_maximal_shared_ngrams(
        draft_tokens, None, patent_tokens)

    for start_i, end_i, ngram in shared:
        if _span_covers(ngram, authorized_spans):
            continue
        # Map token indices to char offsets for exemption + reporting.
        if start_i >= len(draft_char_spans) or end_i - 1 >= len(draft_char_spans):
            continue
        c_start = draft_char_spans[start_i][0]
        c_end = draft_char_spans[end_i - 1][1]
        if _in_exempt(c_start, c_end):
            continue
        excerpt = " ".join(ngram)
        if len(excerpt) > 120:
            excerpt = excerpt[:117] + "..."
        # Patent offset: first occurrence of the n-gram in patent tokens.
        patent_offset = -1
        needle = ngram
        for pi in range(len(patent_tokens) - len(needle) + 1):
            if patent_tokens[pi:pi + len(needle)] == needle:
                patent_offset = pi
                break
        findings.append({
            "check_id": "LEAK-001",
            "severity": "fail",
            "message": (
                "raw-patent n-gram (n=%d) appears in draft but is not covered "
                "by any invention-summary Quotable span: \"%s\" "
                "(patent token offset %d)"
                % (len(ngram), excerpt, patent_offset)
            ),
            "location": "draft chars %d-%d" % (c_start, c_end),
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
    p = argparse.ArgumentParser(
        description="Patent-leak gate (%s): draft must not paste raw patent "
                    "text outside Quotable spans" % GATE_ID)
    p.add_argument("--draft", required=True,
                   help="path to essay-draft.md or essay-final.md")
    p.add_argument("--patent", help="path to input/patent.md")
    p.add_argument("--invention-summary",
                   help="path to invention-summary.md")
    # Positional draft kept optional for run_gates symmetry; CLI uses --draft.
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
