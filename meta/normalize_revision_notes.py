#!/usr/bin/env python3
"""Normalize a revision-notes.md into findings-ledger.jsonl records.

The **revision-delta capture channel**. Post-acceptance human edits (the delta from the
edit-log-applied draft to the published final) are logged as `## delta` blocks in
`handoff/03-edit/revision-notes.md` (schema: `handoff-template/03-edit/revision-notes.md`).
This deterministic normalizer turns each block into a ledger record tagged with the
appropriate `origin` / `source`, so `pipeline-retro` can score recurrence over editorial
blind-spots a human (or self-audit) catches AFTER the loop says "pass" — and over process
failures that never produce an archive.

Also accepts `## incident` blocks for orchestration-protocol failures (checkpoint-skipped,
stage-order violations, confirm-file misuse) on any run — completed or aborted.

`origin` distinguishes:
  - `inner-loop` — a pass/gate should have caught it
  - `self-audit` / `self-post-accept` — autonomous adversarial catch post-accept
  - `human-post-accept` — only a human caught it
  - `polish` — prose-polish surface pass
  - `orchestration-protocol` — process failure, not content

Per-block `origin:` and optional `finding_id:` override CLI defaults for that block.
CLI `--origin` remains a default-only fallback when the block omits origin.

Usage:
  python meta/normalize_revision_notes.py --notes handoff/03-edit/revision-notes.md \
      --essay-id 045-agility-638-last-mile-moat [--timestamp 2026-06-26T00:00:00Z]
  python meta/normalize_revision_notes.py --notes NOTES.md --essay-id ID --append meta/findings-ledger.jsonl
  python meta/normalize_revision_notes.py --notes NOTES.md --essay-id ID --origin self-post-accept
  python meta/normalize_revision_notes.py --selftest

Per-block keys (optional unless noted): class (required), round, before, after, rationale,
goal, origin, finding_id. Block types: ## delta | ## incident.
"""

import argparse
import json
import re
import sys
from datetime import datetime, timezone

# class (pattern_tag) -> (goal, root_cause_stage, root_cause_artifact). Mirrors the
# human-revision / incident rows in meta/attribution-table.md. Unknown classes fall through
# to a flag so a new attribution-table row gets proposed.
CLASS_MAP = {
    "lead-thesis-deferral": ("4a", "compose", "section-blueprint lead block / thesis-spine arc"),
    "nonclaim-section-header": ("4a", "compose", "section-blueprint header / x-articles-format-en"),
    "meta-reader-instruction": ("4b", "canon", "anti-ai-writing.md -> gate_meta"),
    "jargon-overdepth": ("3", "compose", "deliverable-voice-rules.md"),
    "steelman-absent": ("1", "design", "thesis-spine adversarial-defense -> phase2-handoff-notes"),
    "section-stub-imbalance": ("4a", "compose", "section-blueprint word_target balance"),
    "thesis-restatement-redundancy": ("3", "compose", "section-blueprint (redundancy-bloat sub-mechanism)"),
    "revision-induced-duplication": ("4b", "compose", "essay-en-composer revision-mode re-scan"),
    "venue-ticker-convention": ("4a", "compose", "x-articles-format-en.md"),
    # --- self-audit channel additions (classes the autonomous adversarial pass surfaces) ---
    "claim-scope-misattribution": ("1", "design", "thesis-architect invention-summary claim-scope map (locked/open/pinned)"),
    "legal-posture-language-slip": ("1", "compose", "deliverable-voice-rules.md legal register + fact-check-log"),
    "prosecution-record-overstatement": ("1", "compose", "fact-check-log prosecution-record discipline"),
    "figure-caption-scope-deferral": ("2", "compose", "caption-roles.md scope-first ordering"),
    "figure-cover-undervalued": ("2", "design", "invention-summary-schema Figure relationships + SKILL Step 9"),
    "anchor-incomplete": ("1", "compose", "essay-en-composer/citation-format.md range anchors for multi-paragraph spans"),
    "anchor-offbyone": ("1", "design", "thesis-architect invention-summary Quotable-spans paragraph labeling"),
    # --- human-post-accept channel additions ---
    "procedure-overweight-lead": ("5", "design + compose", "thesis-spine arc + spine->section trace / section-blueprint lead block + reader-energy.md"),
    "promo-safe-harbor-overweight": ("5", "promo", "promo-composer promo-format.md bold-selection rule + briefing-vocabulary-only reuse"),
    "plain-language-gap": ("3", "edit + architecture", "pass-5 reader-perspective calibration + (new) prose-polish stage"),
    # --- orchestration-protocol / incident channel ---
    "checkpoint-skipped": ("all", "orchestrator", "patent-essay SKILL checkpoint protocol + check_run RUN-010"),
    "stage-order-violation": ("all", "orchestrator", "patent-essay SKILL stage graph + check_run RUN-010"),
    "confirm-file-misuse": ("all", "orchestrator", "patent-essay SKILL checkpoint protocol + understand-confirmed.md"),
    "post-hoc-confirmation": ("all", "orchestrator", "patent-essay SKILL checkpoint protocol + check_run RUN-010"),
}

ORIGIN_CHOICES = (
    "human-post-accept",
    "self-post-accept",
    "self-audit",
    "inner-loop",
    "polish",
    "orchestration-protocol",
)

_KEYS = ("class", "round", "before", "after", "rationale", "goal", "origin", "finding_id")
_KV_RE = re.compile(r"\s*([A-Za-z_]+)\s*:\s*(.*)$")
_BLOCK_HEAD_RE = re.compile(r"^##\s+(delta|incident)\b", re.I)


def parse_notes(text):
    """Parse `## delta` / `## incident` blocks into a list of dicts (each must carry `class`).

    Returns list of dicts; each has `_block_type` in {delta, incident}.
    """
    blocks, cur = [], None
    for raw in text.splitlines():
        stripped = raw.strip()
        hm = _BLOCK_HEAD_RE.match(stripped)
        if hm:
            if cur is not None:
                blocks.append(cur)
            cur = {"_block_type": hm.group(1).lower()}
            continue
        if cur is None:
            continue
        if stripped.startswith("#"):          # any other heading closes the block
            blocks.append(cur)
            cur = None
            continue
        m = _KV_RE.match(raw)
        if m and m.group(1).lower() in _KEYS:
            cur[m.group(1).lower()] = m.group(2).strip()
    if cur is not None:
        blocks.append(cur)
    return [d for d in blocks if d.get("class")]


def _default_source_for_origin(origin):
    if origin == "orchestration-protocol":
        return "incident"
    if origin in ("self-post-accept", "self-audit"):
        return "self-audit"
    if origin == "polish":
        return "editorial"
    if origin == "inner-loop":
        return "editorial"
    return "human-revision"


def _finding_verb(origin, block_type):
    if block_type == "incident" or origin == "orchestration-protocol":
        return "orchestration incident"
    if origin == "self-post-accept":
        return "self-audit revision"
    if origin == "self-audit":
        return "self-audit revision"
    if origin == "polish":
        return "polish revision"
    if origin == "inner-loop":
        return "inner-loop revision"
    return "post-accept revision"


def to_record(d, essay_id, ts, origin="human-post-accept", source="human-revision"):
    """Build one ledger record. Per-block origin overrides the CLI/default origin."""
    cls = d["class"]
    block_type = d.get("_block_type", "delta")
    block_origin = (d.get("origin") or "").strip() or origin
    if block_type == "incident" and not (d.get("origin") or "").strip():
        # bare incidents default to orchestration-protocol unless CLI/block set otherwise
        if origin == "human-post-accept":
            block_origin = "orchestration-protocol"
    block_source = source
    if (d.get("origin") or "").strip() or block_type == "incident":
        # re-pair source when origin came from the block (or incident default)
        if source == "human-revision" or block_type == "incident":
            block_source = _default_source_for_origin(block_origin)

    if cls in CLASS_MAP:
        goal, stage, artifact = CLASS_MAP[cls]
    else:
        goal = d.get("goal", "?")
        stage, artifact = "edit", "(unmapped class -- add a meta/attribution-table.md row)"
        if block_type == "incident":
            stage, artifact = (
                "orchestrator",
                "(unmapped incident class -- add a meta/attribution-table.md orchestration/protocol row)",
            )
    if d.get("goal"):
        goal = d["goal"]

    rnd = d.get("round", "").strip()
    verb = _finding_verb(block_origin, block_type)
    before = d.get("before", "").strip()
    after = d.get("after", "").strip()
    rationale = d.get("rationale", "").strip()
    if block_type == "incident":
        finding = "%s%s: %s" % (
            verb,
            (" (" + rnd + ")") if rnd else "",
            rationale or (cls + (": " + before if before else "")),
        )
        if before or after:
            finding = "%s%s: %r -> %r. %s" % (
                verb,
                (" (" + rnd + ")") if rnd else "",
                before,
                after,
                rationale,
            )
    else:
        finding = "%s%s: %r -> %r. %s" % (
            verb,
            (" (" + rnd + ")") if rnd else "",
            before,
            after,
            rationale,
        )

    rec = {
        "essay_id": essay_id,
        "iter": None,
        "run_timestamp": ts,
        "source": block_source,
        "origin": block_origin,
        "pass": None,
        "check_id": None,
        "severity": "warn" if block_type != "incident" else "fail",
        "goal": goal,
        "root_cause_stage": stage,
        "root_cause_artifact": artifact,
        "pattern_tag": cls,
        "finding": finding,
        "recommendation": (
            "captured via the incident channel; owner artifact + lever per attribution-table."
            if block_type == "incident"
            else "captured via the revision-delta channel; owner artifact + lever per attribution-table."
        ),
        "status": "watch",
    }
    fid = (d.get("finding_id") or "").strip()
    if fid:
        rec["finding_id"] = fid
    return rec


def normalize(text, essay_id, ts, origin="human-post-accept", source="human-revision"):
    return [to_record(d, essay_id, ts, origin, source) for d in parse_notes(text)]


_SELFTEST_NOTES = """# Revision notes — test
## delta
class: meta-reader-instruction
round: v2.2
before: Read it the way an examiner would.
after: removed
rationale: stage direction, not insight.

## delta
class: brand-new-unmapped-class
before: x
after: y
rationale: z

## delta
class: lead-thesis-deferral
origin: polish
finding_id: PL-01
before: long nested sentence
after: two short sentences
rationale: surface polish only

## incident
class: checkpoint-skipped
origin: orchestration-protocol
finding_id: ORCH-01
rationale: design started without understand-confirmed.md; by:/date: later than design artifacts

# Sources
- not a delta
"""


def _selftest():
    recs = normalize(_SELFTEST_NOTES, "test-essay", "2026-01-01T00:00:00Z")
    assert len(recs) == 4, "expected 4 blocks, got %d" % len(recs)
    a = recs[0]
    assert a["pattern_tag"] == "meta-reader-instruction"
    assert a["origin"] == "human-post-accept" and a["source"] == "human-revision"
    assert a["goal"] == "4b" and a["root_cause_stage"] == "canon"
    assert "Read it the way an examiner would" in a["finding"]
    assert "finding_id" not in a, "finding_id optional — omit when absent"
    b = recs[1]
    assert "unmapped" in b["root_cause_artifact"], "unknown class must flag for a new row"
    # per-block origin overrides CLI default
    c = recs[2]
    assert c["origin"] == "polish", "per-block origin must override CLI default"
    assert c.get("finding_id") == "PL-01"
    # incident channel
    d = recs[3]
    assert d["origin"] == "orchestration-protocol"
    assert d["source"] == "incident"
    assert d["pattern_tag"] == "checkpoint-skipped"
    assert d["root_cause_stage"] == "orchestrator"
    assert d.get("finding_id") == "ORCH-01"
    assert d["severity"] == "fail"
    # self-audit channel: --origin self-post-accept flips origin/source + the finding verb,
    # while the default path above stays human-post-accept (backward compatible).
    srecs = normalize(_SELFTEST_NOTES, "test-essay", "2026-01-01T00:00:00Z",
                      origin="self-post-accept", source="self-audit")
    assert srecs[0]["origin"] == "self-post-accept" and srecs[0]["source"] == "self-audit"
    assert srecs[0]["finding"].startswith("self-audit revision")
    assert a["origin"] == "human-post-accept", "default origin must remain human-post-accept"
    # per-block origin still wins under CLI self-post-accept
    assert srecs[2]["origin"] == "polish"
    # bare incident without origin: defaults to orchestration-protocol
    bare = normalize(
        "## incident\nclass: stage-order-violation\nrationale: compose before design\n",
        "test-essay", "2026-01-01T00:00:00Z",
    )
    assert len(bare) == 1 and bare[0]["origin"] == "orchestration-protocol"
    assert bare[0]["source"] == "incident"
    # every record must be valid JSON round-trip
    for r in recs + srecs + bare:
        json.loads(json.dumps(r))
    print(
        "selftest OK: %d records, schema + class-map + unknown-flag + origin-flag "
        "+ per-block origin + incident channel verified" % len(recs)
    )
    return 0


def main(argv=None):
    p = argparse.ArgumentParser(description="Normalize revision-notes.md -> ledger records.")
    p.add_argument("--notes", help="path to revision-notes.md")
    p.add_argument("--essay-id", default="unknown-essay")
    p.add_argument("--timestamp", help="ISO-8601; default = now (UTC)")
    p.add_argument("--append", help="ledger path to append JSONL records to")
    p.add_argument("--origin", default="human-post-accept",
                   choices=list(ORIGIN_CHOICES),
                   help="default provenance when a block omits origin: "
                        "(default: human-post-accept). "
                        "Use self-post-accept / self-audit for autonomous deltas; "
                        "orchestration-protocol for process incidents.")
    p.add_argument("--source", help="source tag; default paired to --origin "
                   "(human-revision, self-audit, incident, editorial)")
    p.add_argument("--selftest", action="store_true")
    args = p.parse_args(argv)

    if args.selftest:
        return _selftest()
    if not args.notes:
        p.error("--notes is required (or use --selftest)")

    ts = args.timestamp or datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    source = args.source or _default_source_for_origin(args.origin)
    with open(args.notes, "r", encoding="utf-8") as fh:
        recs = normalize(fh.read(), args.essay_id, ts, args.origin, source)

    lines = [json.dumps(r, ensure_ascii=False) for r in recs]
    if args.append:
        with open(args.append, "a", encoding="utf-8") as fh:
            for line in lines:
                fh.write(line + "\n")
        print("appended %d records to %s" % (len(lines), args.append))
    else:
        for line in lines:
            print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
