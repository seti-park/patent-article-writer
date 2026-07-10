#!/usr/bin/env python3
"""Run-completeness checker: did the Compose↔Edit loop actually run?

The inner loop's historical escape hatches were all "the model said so": a
round-1 `pass` graded by the same context that composed, findings applied
without verification, promotion at the cap without a trace. This script makes
the loop's SHAPE mechanically checkable. The orchestrator must run it (and it
must pass) before archiving a run; the /goal acceptance string can require it.

Artifact contract (written by the orchestrator each round N = 1..K):
  handoff/03-edit/edit-log.round-N.md          review round N (feedback-format.md;
                                               findings carry finding_id rN-F<k>)
  handoff/03-edit/gate-result.round-N.json     run_gates.py --json output for round N
  handoff/02-compose/revision-response.round-N.md   composer dispositions for round N
                                               (required for every round FOLLOWED by
                                               another round)
  handoff/03-edit/essay-final.md               promotion target (acceptance only)
  handoff/03-edit/score-history.md             must contain "CAP HIT" if promoted at cap
  handoff/03-edit/revision-notes.md            self-audit deltas (essay mode)
  handoff/01-design/owner-briefing.md          Phase-1 Korean owner briefing --
                                               one-time, not per-round (RUN-008)
  handoff/00-understand/understand-confirmed.md  owner (or --yes) confirm (RUN-010)
  handoff/run-manifest.md                      optional run bootstrap (RUN-012)

Checks:
  RUN-001 (fail): round artifacts missing or non-contiguous (edit-log/gate-result
                  for rounds 1..K; revision-response for rounds 1..K-1) -- UNLESS
                  round N -> N+1 is a confirmation transition (see below), which
                  by spec takes no revision and so has no response to trace.
  RUN-002 (fail): an edit-log has no parsable overall_assessment, or a gate
                  result JSON is unreadable.
  RUN-003 (fail): a medium/high/critical finding in round N has no disposition
                  block in revision-response.round-N.md, or a failing gate
                  check_id has none (rounds followed by another round only;
                  skipped entirely across a confirmation transition).
  RUN-004 (fail): a medium+ finding_id from round N-1 is never mentioned in
                  round N's edit-log (silently dropped instead of ruled on).
                  Runs across every transition, confirmation or not.
  RUN-005 (fail): essay-final.md exists but the acceptance rule is not met:
                  --acceptance double-clean (default): the LAST TWO rounds must
                  both be clean (assessment acceptable per --threshold AND gates
                  passed) — a round-1 pass is a hypothesis, not a verdict, until
                  a fresh review confirms it —
                  --acceptance single-clean: K>=1 and the last round is clean
                  (still fails if the sole/last round is dirty or gates failed);
                  UNLESS score-history.md declares "CAP HIT" (explicit
                  ship-best-round decision, surfaced to the user).
  RUN-006 (warn): promoted via CAP HIT (informational — unresolved findings ship).
  RUN-007 (fail): --self-audit on and essay-final.md exists, but
                  revision-notes.md is missing or has neither a "## delta"
                  block nor an explicit no-findings statement.
  RUN-008 (fail): essay-final.md exists but owner-briefing.md is missing or empty
                  from handoff/01-design/ AND handoff/00-understand/ -- the Korean
                  owner briefing was never produced. Unconditional.
  RUN-009 (fail): essay-final.md exists but handoff/00-understand/ is missing the
                  understand triad (owner-study-pack.md empty/missing, or
                  invention-summary.md missing). Understand-first control plane.
                  (Legacy no-00-understand path still warns when
                  --no-require-understand; with --require-understand, RUN-011
                  covers the five required_outputs hard fail.)
  RUN-010 (fail): --owner-confirm is not off, the run has design output or
                  beyond, and handoff/00-understand/understand-confirmed.md is
                  missing or INVALID (status confirmed; by ∈ {owner,
                  orchestrator-yes-flag}; real YYYY-MM-DD date not placeholder;
                  patent matches run patent id). yes-flag mode additionally
                  requires by: orchestrator-yes-flag.
  RUN-011 (fail): --require-understand is on (default) and the five understand
                  required_outputs are not all present and non-empty under
                  handoff/00-understand/ (invention-summary, owner-study-pack,
                  owner-briefing, figure-primer, open-questions). Replaces the
                  legacy warn-and-pass bypass. --no-require-understand is for
                  legacy archive re-verification only.
  RUN-012 (fail): handoff/run-manifest.md exists and its patent_sha256 does not
                  equal sha256(input/patent.md), or essays/<id>/patent.md
                  snapshot (when present) does not hash-match. Manifest absent
                  → skip with a warn line (RUN-000).
  RUN-000 (warn): informational skips (incl. a confirmation transition, below;
                  run-manifest absent → RUN-012 skipped; confirm patent set
                  but no run-side patent id derivable → patent-match clause
                  skipped for legacy archive re-verification).

Confirmation-transition model (2026-07-03-check-run-confirmation-round-model
proposal + its 2026-07-04 amendment + 2026-07-06 veto):
  Prefer explicit markers, then fall back to the phrase/score-history heuristic.
  Detected (any one positive signal, then veto may demote):
    1. edit-log.round-<next_round>.md declares `round_type: confirmation`
    2. That file's first 40 lines contain the phrase "confirmation round"
    3. score-history.md's row for round N+1 labels it "confirmation" (incl.
       round_type column)
  VETO (2026-07-06): a round N that already has revision-response.round-N.md
  can NEVER count as a confirmation transition into N+1, regardless of markers.
  Across a (non-vetoed) confirmation transition, RUN-001/RUN-003 never require
  a revision-response; RUN-004 id-continuity still runs.

Severity harvesting (`_findings_with_severity`) only counts a finding_id as
THIS round's own finding when a plain `severity:` line follows it within a
few lines. The re-review protocol's carried/verification ruling blocks use
`prior_severity:` notation to re-affirm an OLDER id's severity while ruling on
it -- that notation is a citation, not a new finding, and must not manufacture
a phantom RUN-003/RUN-004 obligation for the round that merely re-verified it
(second, compounding manifestation of the same proposal, 2026-07-04 amendment,
etched-us20240378175).

Usage:
  check_run.py [--handoff handoff] [--threshold pass|revise-recommended]
               [--self-audit on|off]
               [--acceptance single-clean|double-clean]
               [--owner-confirm required|yes-flag|off]
               [--require-understand | --no-require-understand]
               [--json]
Exit code 0 iff no fail-severity finding.
"""

import argparse
import glob
import hashlib
import json
import os
import re
import sys

ASSESS_RE = re.compile(r"^\s*overall_assessment:\s*(\S+)", re.M)
FINDING_ID_RE = re.compile(r"^\s*-\s*finding_id:\s*(r\d+-F\d+)", re.M)
SEVERITY_RE = re.compile(r"^\s*severity:\s*(\S+)", re.M)
CAP_HIT_RE = re.compile(r"\bCAP\s+HIT\b", re.I)
DELTA_RE = re.compile(r"^##\s+delta\b", re.M | re.I)
NO_FINDINGS_RE = re.compile(r"self-audit[^\n]*no[^\n]*finding", re.I)

# Confirmation-transition signals (2026-07-03-check-run-confirmation-round-model).
ROUND_TYPE_CONFIRMATION_RE = re.compile(r"^\s*round_type:\s*confirmation", re.M | re.I)
ROUND_TYPE_REVISION_RE = re.compile(r"^\s*round_type:\s*revision", re.M | re.I)
CONFIRMATION_PHRASE_RE = re.compile(r"confirmation\s+round", re.I)
FINDING_BLOCK_LOOKAHEAD = 6  # lines searched after `finding_id:` for a plain `severity:`

# understand-confirmed.md field parsers
# Horizontal whitespace only ([^\S\n]) so empty fields cannot swallow the
# following line's leading "-" under re.M (WS-B follow-up 2).
CONFIRM_STATUS_RE = re.compile(
    r"^[^\S\n]*-[^\S\n]*\*\*status\*\*[^\S\n]*:[^\S\n]*(\S+)", re.M | re.I)
CONFIRM_BY_RE = re.compile(
    r"^[^\S\n]*-[^\S\n]*\*\*by\*\*[^\S\n]*:[^\S\n]*(\S+)", re.M | re.I)
CONFIRM_DATE_RE = re.compile(
    r"^[^\S\n]*-[^\S\n]*\*\*date\*\*[^\S\n]*:[^\S\n]*(\S+)", re.M | re.I)
CONFIRM_PATENT_RE = re.compile(
    r"^[^\S\n]*-[^\S\n]*\*\*patent\*\*[^\S\n]*:[^\S\n]*(\S+)", re.M | re.I)
CONFIRM_NOTES_RE = re.compile(
    r"^[^\S\n]*-[^\S\n]*\*\*notes\*\*[^\S\n]*:[^\S\n]*(.+)$", re.M | re.I)
REAL_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
PLACEHOLDER_DATE_RE = re.compile(r"^<[^>]+>$")

# run-manifest.md — same horizontal-only whitespace (empty values must not
# absorb the next line via \s matching \n under re.M).
MANIFEST_FIELD_RE = re.compile(
    r"^[^\S\n]*-[^\S\n]*\*\*(\w+)\*\*[^\S\n]*:[^\S\n]*(.+?)[^\S\n]*$", re.M)

# Patent identifier patterns in input/patent.md (publication / application numbers)
PATENT_ID_PATTERNS = [
    re.compile(r"\b(US\s*\d{4}/\d{6,}\s*[A-Z]\d?)\b", re.I),
    re.compile(r"\b(US\d{10,11}[A-Z]\d?)\b", re.I),
    re.compile(r"\b(US\s*\d{1,2},?\d{3},?\d{3}\s*[A-Z]\d?)\b", re.I),
    re.compile(r"\b(US\d{7,8}[A-Z]\d?)\b", re.I),
    re.compile(r"\b((?:EP|WO|CN|JP|KR)\s*\d[\d/\s,]*[A-Z]?\d?)\b", re.I),
]

UNDERSTAND_REQUIRED_OUTPUTS = (
    "invention-summary.md",
    "owner-study-pack.md",
    "owner-briefing.md",
    "figure-primer.md",
    "open-questions.md",
)

ACCEPTABLE = {
    "pass": {"pass"},
    "revise-recommended": {"pass", "revise-recommended"},
}

VALID_CONFIRM_BY = frozenset({"owner", "orchestrator-yes-flag"})


def _read(path):
    with open(path, "r", encoding="utf-8") as fh:
        return fh.read()


def _sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def _dir_has_content(path):
    if not os.path.isdir(path):
        return False
    return any(name != ".gitkeep" for name in os.listdir(path))


def _normalize_patent_id(s):
    """Collapse whitespace/slashes/commas for loose patent-id equality."""
    if not s:
        return ""
    s = s.strip().strip('"').strip("'")
    s = re.sub(r"[\s/,]+", "", s)
    return s.upper()


def _patent_ids_match(a, b):
    """Exact or kind-code-core equality after normalize (no substring arm).

    Kind-code core: US9999999 ≡ US9999999B2. Truncated prefixes do not match
    (US999 ≉ US9999999B2). Separators are already stripped by normalize.
    """
    na, nb = _normalize_patent_id(a), _normalize_patent_id(b)
    if not na or not nb:
        return False
    if na == nb:
        return True
    # One may omit kind code suffix (B2/A1)
    def core(x):
        return re.sub(r"[A-Z]\d?$", "", x)
    return core(na) == core(nb)


def _derive_patent_id(run_root, handoff_dir):
    """Best-effort patent identifier from run-manifest and/or input/patent.md."""
    ids = []
    manifest_path = os.path.join(handoff_dir, "run-manifest.md")
    if not os.path.exists(manifest_path):
        # also accept handoff/../handoff sibling? primary is handoff/run-manifest.md
        pass
    if os.path.exists(manifest_path):
        fields = _parse_manifest(manifest_path)
        if fields.get("patent"):
            ids.append(fields["patent"].strip())
    patent_path = os.path.join(run_root, "input", "patent.md")
    if os.path.exists(patent_path):
        text = _read(patent_path)[:8000]
        for pat in PATENT_ID_PATTERNS:
            m = pat.search(text)
            if m:
                ids.append(re.sub(r"\s+", "", m.group(1)))
                break
    return ids


def _parse_manifest(path):
    text = _read(path)
    fields = {}
    for m in MANIFEST_FIELD_RE.finditer(text):
        fields[m.group(1).lower()] = m.group(2).strip()
    return fields


def _findings_with_severity(edit_log_text):
    """Return list of (finding_id, severity) DECLARED by this round's log.

    A `finding_id:` block counts as this round's own finding only when a
    plain `severity:` line follows it within FINDING_BLOCK_LOOKAHEAD lines
    (or before the next `finding_id:` block, whichever comes first). This
    deliberately does NOT match `prior_severity:` -- the re-review protocol's
    carried/verification-ruling notation, used when a round re-affirms an
    OLDER id's severity while ruling on it. A block that only ever carries
    `prior_severity:` is a citation of a previous round's finding, not a new
    finding of this round, and is excluded entirely here (not even counted as
    "unspecified") so it cannot manufacture a phantom RUN-003/RUN-004
    obligation for the round that merely re-verified it.
    """
    lines = edit_log_text.splitlines()
    out = []
    i = 0
    while i < len(lines):
        m = re.match(r"^\s*-\s*finding_id:\s*(r\d+-F\d+)", lines[i])
        if not m:
            i += 1
            continue
        fid = m.group(1)
        limit = min(i + 1 + FINDING_BLOCK_LOOKAHEAD, len(lines))
        for j in range(i + 1, limit):
            if re.match(r"^\s*-\s*finding_id:\s*(r\d+-F\d+)", lines[j]):
                break  # next block opened first -- no plain severity: for this id
            s = re.match(r"^\s*severity:\s*(\S+)", lines[j])
            if s:
                out.append((fid, s.group(1).strip()))
                break
        i += 1
    return out


def _is_confirmation_transition(edit_dir, score_path, next_round):
    """True when round `next_round` is a confirmation round for its predecessor.

    Prefer explicit markers, then fall back to the phrase/score-history heuristic
    (2026-07-03; do not tighten the heuristic alone — veto handles over-fire).
    Detected (any one signal suffices):
      1. edit-log.round-<next_round>.md declares `round_type: confirmation`
         (explicit `round_type: revision` is a negative signal for that file).
      2. That file's first 40 lines contain the phrase "confirmation round"
         (case-insensitive), only when no explicit round_type: revision.
      3. score-history.md's row for round `next_round` labels it "confirmation".
    Caller applies the revision-response veto after this returns True.
    """
    log_path = os.path.join(edit_dir, "edit-log.round-%d.md" % next_round)
    if os.path.exists(log_path):
        text = _read(log_path)
        if ROUND_TYPE_CONFIRMATION_RE.search(text):
            return True
        if ROUND_TYPE_REVISION_RE.search(text):
            # Explicit revision marker: do not treat phrase "confirmation round"
            # elsewhere in the file as making this a confirmation round.
            pass
        else:
            first_40 = "\n".join(text.splitlines()[:40])
            if CONFIRMATION_PHRASE_RE.search(first_40):
                return True
    if os.path.exists(score_path):
        for line in _read(score_path).splitlines():
            if re.search(r"\|\s*%d\s*\|" % next_round, line) and re.search(
                    r"confirmation", line, re.I):
                return True
    return False


def _validate_understand_confirmed(text, patent_ids, owner_confirm_mode):
    """Return (ok: bool, message: str, warn: str|None).

    patent_ids is a list of acceptable run-side ids. Empty patent_ids with a
    non-empty confirm patent cannot perform the match clause: ok stays True and
    warn carries a RUN-000 message for the caller (legacy archive re-verification
    has no input/). Empty/missing confirm patent is always a fail.
    """
    status_m = CONFIRM_STATUS_RE.search(text)
    by_m = CONFIRM_BY_RE.search(text)
    date_m = CONFIRM_DATE_RE.search(text)
    patent_m = CONFIRM_PATENT_RE.search(text)
    notes_m = CONFIRM_NOTES_RE.search(text)

    status = status_m.group(1).strip().lower() if status_m else ""
    by = by_m.group(1).strip() if by_m else ""
    date = date_m.group(1).strip() if date_m else ""
    patent = patent_m.group(1).strip() if patent_m else ""
    notes = notes_m.group(1).strip() if notes_m else ""

    if status != "confirmed":
        return False, "status is %r (need confirmed)" % (status or "missing"), None
    if by not in VALID_CONFIRM_BY:
        return False, "by is %r (need owner or orchestrator-yes-flag)" % (by or "missing"), None
    if owner_confirm_mode == "yes-flag" and by != "orchestrator-yes-flag":
        return False, "owner-confirm=yes-flag requires by: orchestrator-yes-flag (got %r)" % by, None
    if not date or PLACEHOLDER_DATE_RE.match(date) or not REAL_DATE_RE.match(date):
        return False, "date is %r (need real YYYY-MM-DD, not placeholder)" % (date or "missing"), None
    if not patent:
        return False, "patent field missing", None
    warn = None
    if not patent_ids:
        warn = (
            "confirm patent %s unverifiable — no input/patent.md and no "
            "run-manifest patent id" % patent
        )
    elif not any(_patent_ids_match(patent, pid) for pid in patent_ids):
        return False, "patent %r does not match run patent id(s) %s" % (patent, patent_ids), None
    if by == "owner" and not notes.strip().strip('"').strip("'"):
        return False, "notes required when by: owner", None
    return True, "ok", warn


def check(handoff_dir, threshold="pass", self_audit="on",
          acceptance="double-clean", owner_confirm="required",
          require_understand=True):
    findings = []
    edit_dir = os.path.join(handoff_dir, "03-edit")
    compose_dir = os.path.join(handoff_dir, "02-compose")
    design_dir = os.path.join(handoff_dir, "01-design")
    understand_dir = os.path.join(handoff_dir, "00-understand")
    score_path = os.path.join(edit_dir, "score-history.md")
    run_root = os.path.dirname(os.path.abspath(handoff_dir))

    def add(check_id, severity, message, location):
        findings.append({"check_id": check_id, "severity": severity,
                         "message": message, "location": location})

    # --- discover rounds --------------------------------------------------
    logs = glob.glob(os.path.join(edit_dir, "edit-log.round-*.md"))
    rounds = sorted(int(m.group(1)) for p in logs
                    for m in [re.search(r"edit-log\.round-(\d+)\.md$", p)] if m)
    if not rounds:
        add("RUN-001", "fail",
            "no edit-log.round-N.md artifacts found — the loop left no trace",
            edit_dir)
        return _result(findings)
    K = max(rounds)
    if rounds != list(range(1, K + 1)):
        add("RUN-001", "fail",
            "rounds are non-contiguous: found %s (expected 1..%d)" % (rounds, K),
            edit_dir)

    # --- per-round artifacts + parses -------------------------------------
    assessments = {}
    gates_passed = {}
    round_findings = {}
    for n in range(1, K + 1):
        log_path = os.path.join(edit_dir, "edit-log.round-%d.md" % n)
        gate_path = os.path.join(edit_dir, "gate-result.round-%d.json" % n)
        if not os.path.exists(log_path):
            continue  # RUN-001 already covers gaps
        text = _read(log_path)
        m = ASSESS_RE.search(text)
        if not m:
            add("RUN-002", "fail",
                "edit-log.round-%d.md has no parsable overall_assessment" % n, log_path)
        else:
            assessments[n] = m.group(1).strip()
        round_findings[n] = _findings_with_severity(text)

        if not os.path.exists(gate_path):
            add("RUN-001", "fail", "gate-result.round-%d.json missing" % n, edit_dir)
        else:
            try:
                gates_passed[n] = bool(json.loads(_read(gate_path)).get("passed"))
            except (ValueError, OSError) as e:
                add("RUN-002", "fail",
                    "gate-result.round-%d.json unreadable: %s" % (n, e), gate_path)

        # response required for every round followed by another round --
        # UNLESS round n -> n+1 is a confirmation transition (spec: the
        # confirmation round takes no revision, so there is nothing to
        # disposition or trace at this transition).
        # VETO (2026-07-06): presence of revision-response.round-n.md means a
        # real revision happened; never treat as confirmation regardless of
        # markers (proposal: ship veto alone; do not tighten phrase heuristic).
        if n < K:
            resp_path = os.path.join(compose_dir, "revision-response.round-%d.md" % n)
            resp_exists = os.path.exists(resp_path)
            confirmation = _is_confirmation_transition(edit_dir, score_path, n + 1)
            if resp_exists:
                if confirmation:
                    add("RUN-000", "warn",
                        "round %d -> %d carries BOTH a revision-response and a "
                        "'confirmation' marker; the revision-response is dispositive "
                        "(a confirmation round takes no revision) -- treating as a REAL "
                        "revision and running disposition checks" % (n, n + 1), edit_dir)
                resp = _read(resp_path)
                for fid, sev in round_findings.get(n, []):
                    if sev in ("medium", "high", "critical", "unspecified") and fid not in resp:
                        add("RUN-003", "fail",
                            "finding %s (%s) has no disposition in "
                            "revision-response.round-%d.md" % (fid, sev, n), resp_path)
                gate_json = gates_passed.get(n)
                if gate_json is False:
                    try:
                        gate_data = json.loads(_read(os.path.join(
                            edit_dir, "gate-result.round-%d.json" % n)))
                        failing = {f["check_id"] for g in gate_data.get("gates", [])
                                   for f in g.get("findings", [])
                                   if f.get("severity") == "fail"}
                    except (ValueError, OSError):
                        failing = set()
                    for cid in sorted(failing):
                        if cid not in resp:
                            add("RUN-003", "fail",
                                "failing gate %s has no disposition in "
                                "revision-response.round-%d.md" % (cid, n), resp_path)
            elif confirmation:
                add("RUN-000", "warn",
                    "round %d -> %d is a confirmation transition (no revision "
                    "in between); revision-response/disposition requirements "
                    "skipped for this transition" % (n, n + 1), edit_dir)
            else:
                add("RUN-001", "fail",
                    "revision-response.round-%d.md missing (round %d was revised "
                    "without a disposition trace)" % (n, n), compose_dir)

        # carried-id rule: every medium+ id from round n-1 must appear in round n's log
        if n > 1:
            prev = round_findings.get(n - 1, [])
            for fid, sev in prev:
                if sev in ("medium", "high", "critical", "unspecified") and fid not in text:
                    add("RUN-004", "fail",
                        "finding %s (round %d, %s) is never ruled on in round %d's "
                        "edit-log (silently dropped)" % (fid, n - 1, sev, n), log_path)

    # --- progressed past understand? (design or beyond) -------------------
    final_path = os.path.join(edit_dir, "essay-final.md")
    design_or_beyond = (
        os.path.exists(final_path)
        or _dir_has_content(design_dir)
        or _dir_has_content(compose_dir)
    )

    # --- RUN-012: patent hash lock when run-manifest present ---------------
    manifest_path = os.path.join(handoff_dir, "run-manifest.md")
    if os.path.exists(manifest_path):
        fields = _parse_manifest(manifest_path)
        expected = (fields.get("patent_sha256") or "").strip().lower()
        patent_path = os.path.join(run_root, "input", "patent.md")
        if not expected:
            add("RUN-012", "fail",
                "run-manifest.md present but patent_sha256 field missing/empty",
                manifest_path)
        elif not os.path.exists(patent_path):
            add("RUN-012", "fail",
                "run-manifest.md patent_sha256 set but input/patent.md missing",
                patent_path)
        else:
            actual = _sha256_file(patent_path)
            if actual != expected:
                add("RUN-012", "fail",
                    "patent_sha256 mismatch: manifest=%s input/patent.md=%s"
                    % (expected, actual),
                    patent_path)
            else:
                # essays/<id>/patent.md snapshot if present
                run_id = (fields.get("run_id") or "").strip()
                if run_id:
                    snap = os.path.join(run_root, "essays", run_id, "patent.md")
                    if os.path.exists(snap):
                        snap_hash = _sha256_file(snap)
                        if snap_hash != actual:
                            add("RUN-012", "fail",
                                "essays/%s/patent.md sha256=%s does not match "
                                "input/patent.md=%s" % (run_id, snap_hash, actual),
                                snap)
    else:
        add("RUN-000", "warn",
            "handoff/run-manifest.md absent — patent hash lock (RUN-012) skipped",
            handoff_dir)

    # --- RUN-010: owner confirm -------------------------------------------
    if owner_confirm != "off" and design_or_beyond:
        confirm_path = os.path.join(understand_dir, "understand-confirmed.md")
        patent_ids = _derive_patent_id(run_root, handoff_dir)
        if not os.path.exists(confirm_path):
            add("RUN-010", "fail",
                "understand-confirmed.md missing under handoff/00-understand/ "
                "(owner confirm required; use --owner-confirm off only for "
                "legacy archive re-verification)",
                understand_dir)
        else:
            ok, msg, warn = _validate_understand_confirmed(
                _read(confirm_path), patent_ids, owner_confirm)
            if not ok:
                add("RUN-010", "fail",
                    "understand-confirmed.md invalid: %s" % msg, confirm_path)
            if warn:
                add("RUN-000", "warn", warn, confirm_path)

    # --- RUN-011: five understand required_outputs ------------------------
    if require_understand and design_or_beyond:
        missing = []
        for name in UNDERSTAND_REQUIRED_OUTPUTS:
            path = os.path.join(understand_dir, name)
            if not os.path.exists(path) or not _read(path).strip():
                missing.append(name)
        if missing:
            add("RUN-011", "fail",
                "understand required_outputs missing or empty under "
                "handoff/00-understand/: %s (--no-require-understand for legacy "
                "archive re-verification only)" % ", ".join(missing),
                understand_dir)

    # --- acceptance rule ----------------------------------------------------
    if os.path.exists(final_path):
        ok = ACCEPTABLE.get(threshold, {"pass"})

        def clean(n):
            return assessments.get(n) in ok and gates_passed.get(n) is True

        if acceptance == "single-clean":
            accepted_clean = K >= 1 and clean(K)
            accept_desc = "single-clean acceptance (last round clean)"
        else:
            accepted_clean = K >= 2 and clean(K) and clean(K - 1)
            accept_desc = "double-clean acceptance (last two rounds clean)"

        cap_hit = os.path.exists(score_path) and bool(CAP_HIT_RE.search(_read(score_path)))
        if not accepted_clean and not cap_hit:
            add("RUN-005", "fail",
                "essay-final.md promoted without %s and without an explicit CAP HIT "
                "in score-history.md — a single self-graded pass is not acceptance "
                "under double-clean (K=%d, assessments=%s, gates=%s, "
                "acceptance=%s)" % (accept_desc, K, assessments, gates_passed,
                                    acceptance), final_path)
        elif cap_hit and not accepted_clean:
            add("RUN-006", "warn",
                "promoted via CAP HIT — unresolved findings ship; surface them to the user",
                score_path)

        if self_audit == "on":
            notes_path = os.path.join(edit_dir, "revision-notes.md")
            if not os.path.exists(notes_path):
                add("RUN-007", "fail",
                    "self-audit is on but revision-notes.md is missing (no evidence "
                    "the post-acceptance audit ran)", edit_dir)
            else:
                notes = _read(notes_path)
                if not DELTA_RE.search(notes) and not NO_FINDINGS_RE.search(notes):
                    add("RUN-007", "fail",
                        "revision-notes.md has neither a '## delta' block nor an "
                        "explicit 'self-audit: no unresolved findings' statement",
                        notes_path)

        # RUN-008: Korean owner briefing (compat: 01-design or 00-understand).
        briefing_design = os.path.join(design_dir, "owner-briefing.md")
        briefing_understand = os.path.join(understand_dir, "owner-briefing.md")
        briefing_path = None
        for candidate in (briefing_design, briefing_understand):
            if os.path.exists(candidate) and _read(candidate).strip():
                briefing_path = candidate
                break
        if briefing_path is None:
            add("RUN-008", "fail",
                "owner-briefing.md missing or empty under handoff/01-design/ and "
                "handoff/00-understand/ (the Korean owner briefing was never produced)",
                design_dir)

        # RUN-009: understand-first triad (study pack + invention-summary).
        # With require_understand, RUN-011 already hard-fails the five files;
        # RUN-009 still checks the triad shape when 00-understand is present.
        # Legacy archives without 00-understand/: when --no-require-understand,
        # accept 01-design invention-summary with RUN-000 warn.
        study_pack = os.path.join(understand_dir, "owner-study-pack.md")
        inv_u = os.path.join(understand_dir, "invention-summary.md")
        inv_d = os.path.join(design_dir, "invention-summary.md")
        understand_present = _dir_has_content(understand_dir)
        if understand_present:
            if not os.path.exists(study_pack) or not _read(study_pack).strip():
                add("RUN-009", "fail",
                    "owner-study-pack.md missing or empty under handoff/00-understand/ "
                    "(Problem·Solution·Benefits triad was never produced)",
                    study_pack)
            if not os.path.exists(inv_u) or not _read(inv_u).strip():
                if not os.path.exists(inv_d) or not _read(inv_d).strip():
                    add("RUN-009", "fail",
                        "invention-summary.md missing under 00-understand/ and 01-design/",
                        understand_dir)
        else:
            if require_understand:
                # RUN-011 already reported the five missing files; still note triad.
                if not os.path.exists(inv_d) or not _read(inv_d).strip():
                    add("RUN-009", "fail",
                        "invention-summary.md missing from handoff/01-design/ and no "
                        "00-understand/ bundle (no frozen patent model)",
                        design_dir)
            else:
                if not os.path.exists(inv_d) or not _read(inv_d).strip():
                    add("RUN-009", "fail",
                        "invention-summary.md missing from handoff/01-design/ and no "
                        "00-understand/ bundle (no frozen patent model)",
                        design_dir)
                else:
                    add("RUN-000", "warn",
                        "legacy layout: no handoff/00-understand/ (pre understand-first); "
                        "01-design invention-summary accepted (--no-require-understand)",
                        design_dir)
    else:
        add("RUN-000", "warn",
            "essay-final.md not present — acceptance checks skipped (run in progress?)",
            edit_dir)

    return _result(findings)


def _result(findings):
    passed = not any(f["severity"] == "fail" for f in findings)
    return {"gate": "check_run", "passed": passed, "findings": findings}


def _report(result):
    status = "PASS" if result["passed"] else "FAIL"
    print("[%s] %s" % (status, result["gate"]))
    for f in result["findings"]:
        print("  %-5s %-8s %s  (%s)" % (
            f["severity"].upper(), f["check_id"], f["message"], f["location"]))
    if not result["findings"]:
        print("  (no findings)")


def main(argv=None):
    p = argparse.ArgumentParser(description="Loop run-completeness checker")
    p.add_argument("--handoff", default="handoff", help="handoff directory (default: handoff)")
    p.add_argument("--threshold", choices=["pass", "revise-recommended"], default="pass")
    p.add_argument("--self-audit", choices=["on", "off"], default="on")
    p.add_argument("--acceptance", choices=["single-clean", "double-clean"],
                   default="double-clean",
                   help="acceptance rule for RUN-005 (default: double-clean)")
    p.add_argument("--owner-confirm", choices=["required", "yes-flag", "off"],
                   default="required",
                   help="RUN-010 owner-confirm policy (default: required)")
    p.add_argument("--require-understand", dest="require_understand",
                   action="store_true", default=True,
                   help="require five understand outputs (RUN-011; default on)")
    p.add_argument("--no-require-understand", dest="require_understand",
                   action="store_false",
                   help="disable RUN-011 (legacy archive re-verification only)")
    p.add_argument("--json", action="store_true")
    args = p.parse_args(argv)

    result = check(
        args.handoff,
        threshold=args.threshold,
        self_audit=args.self_audit,
        acceptance=args.acceptance,
        owner_confirm=args.owner_confirm,
        require_understand=args.require_understand,
    )
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        _report(result)
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
