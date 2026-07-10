#!/usr/bin/env python3
"""Keep meta/improvement-proposals/README.md's status index honest.

Each proposal file carries a `status:` in its YAML frontmatter (the source of
truth). README.md holds a table index (`| proposal_id | status | recurrence |
date |`). This script checks the two agree, so the index cannot silently rot the
way it did (2 applied proposals still shown pending until 2026-07-11).

Stdlib-only.

Usage:
  python meta/proposals_index.py            # print a reconciliation report
  python meta/proposals_index.py --check    # exit non-zero if index != files
  python meta/proposals_index.py --selftest

Status normalization: comments after `#` are stripped; spaces -> hyphens;
lowercased (so "recommended apply" == "recommended-apply").
"""

from __future__ import annotations

import argparse
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PROPOSALS_DIR = os.path.join(HERE, "improvement-proposals")
README = os.path.join(PROPOSALS_DIR, "README.md")

STATUS_RE = re.compile(r"^status:\s*(.+?)\s*$", re.M)
ROW_RE = re.compile(r"^\|\s*(20\d\d-\d\d-\d\d-[^\s|]+)\s*\|\s*([^|]+?)\s*\|", re.M)


def _norm(status):
    """Normalize a status: strip '# comment' and '(annotation)', lower, spaces->-.

    Keeps two-word statuses intact ("recommended apply" -> "recommended-apply")
    while dropping trailing annotations ("applied (run-045, ...)" -> "applied").
    """
    status = status.split("#", 1)[0]
    status = re.sub(r"\(.*?\)", "", status)       # drop parenthetical annotations
    status = status.strip().lower()
    return re.sub(r"\s+", "-", status)


def file_status(path):
    """Return the normalized `status:` from a proposal file's frontmatter, or None."""
    m = STATUS_RE.search(open(path, "r", encoding="utf-8").read())
    return _norm(m.group(1)) if m else None


def index_rows(readme=README):
    """Return {proposal_id: normalized_status} from the README table."""
    text = open(readme, "r", encoding="utf-8").read()
    return {pid: _norm(st) for pid, st in ROW_RE.findall(text)}


def reconcile(proposals_dir=PROPOSALS_DIR, readme=README):
    """Return (ok, messages). Compares every proposal file to its index row."""
    msgs = []
    rows = index_rows(readme)
    files = {}
    for name in sorted(os.listdir(proposals_dir)):
        if not name.endswith(".md") or name == "README.md":
            continue
        pid = name[:-3]
        files[pid] = file_status(os.path.join(proposals_dir, name))

    ok = True
    for pid, fst in sorted(files.items()):
        if pid not in rows:
            ok = False
            msgs.append("MISSING from index: %s (file status: %s)" % (pid, fst))
        elif fst is not None and rows[pid] != fst:
            ok = False
            msgs.append("MISMATCH %s: index=%s file=%s" % (pid, rows[pid], fst))
    for pid in sorted(rows):
        if pid not in files:
            ok = False
            msgs.append("STALE index row (no such proposal file): %s" % pid)

    msgs.append("%s: %d proposal file(s), %d index row(s)"
                % ("OK" if ok else "FAIL", len(files), len(rows)))
    return ok, msgs


def _selftest():
    import tempfile
    td = tempfile.mkdtemp(prefix="proposals_index_")
    os.makedirs(os.path.join(td, "improvement-proposals"))
    d = os.path.join(td, "improvement-proposals")
    open(os.path.join(d, "2026-01-01-alpha.md"), "w").write("---\nstatus: applied  # c\n---\n")
    open(os.path.join(d, "2026-01-02-beta.md"), "w").write("---\nstatus: recommended apply\n---\n")
    # index agrees (note space vs hyphen normalization on beta)
    open(os.path.join(d, "README.md"), "w").write(
        "| proposal_id | status | recurrence | date |\n|---|---|---|---|\n"
        "| 2026-01-01-alpha | applied | 1 | 2026-01-01 |\n"
        "| 2026-01-02-beta | recommended-apply | 1 | 2026-01-02 |\n")
    ok, msgs = reconcile(d, os.path.join(d, "README.md"))
    assert ok, msgs
    # break it: flip alpha's index status
    open(os.path.join(d, "README.md"), "w").write(
        "| proposal_id | status | recurrence | date |\n|---|---|---|---|\n"
        "| 2026-01-01-alpha | proposed | 1 | 2026-01-01 |\n"
        "| 2026-01-02-beta | recommended-apply | 1 | 2026-01-02 |\n")
    ok2, msgs2 = reconcile(d, os.path.join(d, "README.md"))
    assert not ok2 and any("MISMATCH 2026-01-01-alpha" in m for m in msgs2), msgs2
    print("selftest OK: agree passes; mismatch + normalization (space==hyphen) verified")
    return 0


def main(argv=None):
    p = argparse.ArgumentParser(description="Reconcile the proposals status index with the files.")
    p.add_argument("--check", action="store_true", help="exit non-zero on any disagreement")
    p.add_argument("--selftest", action="store_true")
    args = p.parse_args(argv)
    if args.selftest:
        return _selftest()
    ok, msgs = reconcile()
    for m in msgs:
        print(m)
    return (0 if ok else 1) if args.check else 0


if __name__ == "__main__":
    sys.exit(main())
