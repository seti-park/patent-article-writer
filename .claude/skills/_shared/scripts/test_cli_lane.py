#!/usr/bin/env python3
"""Stdlib unittest suite for the multi-vendor CLI-lane helper (cli_lane.py).

No network. Never invokes the real codex/grok binaries — stubs on a restricted
PATH only. Run with:

    python test_cli_lane.py

Exits nonzero if any test fails.
"""

from __future__ import annotations

import json
import os
import stat
import subprocess
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path

HERE = os.path.dirname(os.path.abspath(__file__))
CLI_LANE = os.path.join(HERE, "cli_lane.py")

# Import GROK_DOC_SCHEMA from cli_lane so argv assertions cannot drift.
if HERE not in sys.path:
    sys.path.insert(0, HERE)
from cli_lane import GROK_DOC_SCHEMA  # noqa: E402

# Canned content for success cases (non-grounding).
GPT_CANNED = "GPT verifier output here.\n"
GROK_CANNED = "Grok compose output here.\n"

# Valid grounding output for --validate grounding.
VALID_GROUNDING = textwrap.dedent("""\
    verifier: gpt-5.6-sol high (cli-lane)
    mode: self-audit grounding
    round: 1

    | sentence ref | anchor | verdict | evidence | recommended fix |
    |---|---|---|---|---|
    | s1 | [0001] | SUPPORTED | span ok | — |

    tally: SUPPORTED 1 / MISREAD 0 / OVERREACHED-BEYOND-ANCHOR 0 / UNSUPPORTED 0
""")

# Has verifier: + |--- but no verdict token from the required set.
INVALID_GROUNDING = textwrap.dedent("""\
    verifier: gpt-5.6-sol high (cli-lane)
    mode: self-audit grounding

    | sentence ref | anchor | verdict | evidence | recommended fix |
    |---|---|---|---|---|
    | s1 | [0001] | MAYBE | span | — |
""")

# Valid drift-check output for --validate drift (mode-B vocabulary).
VALID_DRIFT = textwrap.dedent("""\
    verifier: gpt-5.6-sol high (cli-lane, drift mode)
    round: 1

    | pair | verdict | evidence |
    |---|---|---|
    | p1 | MEANING-PRESERVED | rewrite restates same claim; anchors intact |

    tally: MEANING-PRESERVED 1 / MEANING-CHANGED 0 / PROTECTED-TOUCHED 0
""")

# Has verifier: + |--- but no drift-mode verdict token from the required set.
INVALID_DRIFT = textwrap.dedent("""\
    verifier: gpt-5.6-sol high (cli-lane, drift mode)
    round: 1

    | pair | verdict | evidence |
    |---|---|---|
    | p1 | UNCHANGED | rewrite looks similar |
""")

# Valid voice pre-gate output for --validate pregate.
VALID_PREGATE = textwrap.dedent("""\
    pregate: voice-drift (guardrail 2)
    generator: grok-4.5 (cli-lane)
    round: 1
    verdict: VOICE-PASS

    tells:
    - none

    notes: clean draft, no repeated tells, register matches the exemplars.
""")

# Has pregate: line but no VOICE-PASS / VOICE-FAIL verdict substring.
INVALID_PREGATE = textwrap.dedent("""\
    pregate: voice-drift (guardrail 2)
    generator: grok-4.5 (cli-lane)
    round: 1
    verdict: MAYBE

    tells:
    - none

    notes: malformed verdict for validator exercise.
""")

# Valid safe-claims+AI-tell judge output for --validate safeclaims.
VALID_SAFECLAIMS = textwrap.dedent("""\
    check: safe-claims+ai-tell (gpt lane)
    generator: claude inherit (promo-composer)
    verdict: SAFE-PASS
    aitell: CLEAN

    violations:
    - none
    tells:
    - none
    trace-notes: hem geometry -> essay-final ¶2; equipment list may-claim -> publication; application-stage hedge as final sentence only.
""")

# Has check: + SAFE-PASS verdict but MISSING the aitell: line entirely.
INVALID_SAFECLAIMS = textwrap.dedent("""\
    check: safe-claims+ai-tell (gpt lane)
    generator: claude inherit (promo-composer)
    verdict: SAFE-PASS

    violations:
    - none
    tells:
    - none
    trace-notes: malformed output missing aitell line for validator exercise.
""")

# Valid review-lane output for --validate review.
VALID_REVIEW = textwrap.dedent("""\
    reviewer: gpt-5.6-sol high (cli-lane)
    round: 1
    round_type: confirmation
    posture_applied: measured
    grounding: PASS
    goal-2: PASS
    verdict: PASS
    assessment: pass

    findings:
    - id: r1-F1
      pass: pass-1-voice-anti-ai
      severity: low
      quote: "The architecture routes vision data upstream."
      why: Minor cadence drift in §2 supporting prose; not publication-blocking.
      fix-direction: Tighten the opening clause to land the mechanism first.

    warn_dispositions:
    - gate_surface SURF-003: noted; surface already within band after pre-gate.
""")

# Same shape (round_type + hard-gate labels + findings list) but no valid assessment token.
INVALID_REVIEW = textwrap.dedent("""\
    reviewer: gpt-5.6-sol high (cli-lane)
    round: 1
    round_type: confirmation
    posture_applied: measured
    grounding: PASS
    goal-2: PASS
    verdict: PASS
    assessment: needs-work

    findings:
    - id: r1-F1
      pass: pass-1-voice-anti-ai
      severity: low
      quote: "The architecture routes vision data upstream."
      why: Minor cadence drift in §2 supporting prose.
      fix-direction: Tighten the opening clause.

    warn_dispositions:
    - gate_surface SURF-003: noted.
""")

# Valid compose draft for --validate compose: frontmatter fence, [dddd] anchor, >=800 stripped chars.
VALID_COMPOSE = textwrap.dedent("""\
    ---
    essay_id: 044-tesla-rcm-vindication
    patent_reference: US 2026/0125022 A1
    spine_source: handoff/01-design/thesis-spine.md
    draft_version: 1
    mode_used: walkthrough
    posture_used: measured
    closing_posture: firm
    ---

    # Tesla Filed the 70ms Airbag Patent Before It Announced the 70ms Airbag

    ## When the Announcement Arrived Late

    This spring, Tesla described its predictive restraint system as an unprecedented
    pre-impact response. The description was accurate. It was also roughly eleven months
    late: the patent that explains the response had already been on file since October
    2024. The announcement did not reveal the architecture. It caught up to it.

    ## What the Patent Actually Routes

    The restraint-control module does not wait for the crash. The vision sensor array
    computes a pre-impact prediction and routes it to the vehicle control unit, which
    arms the airbag module before an accelerometer would register the impact. The patent
    is explicit that this is not a backup channel: it describes the vision sensor
    providing pre-impact prediction to the airbag controller [0016], and notes that the
    vision sensor functions as a predictive input rather than a redundant sensor.

    Conventional restraint systems are reactive by construction. Industry
    accelerometer-based ECUs reach a deployment decision within roughly ten milliseconds
    of crash detection. Tesla's architecture moves that decision upstream of the crash
    entirely, so the deployment decision is made approximately seventy milliseconds
    before traditional accelerometer-based systems would respond. Both figures describe
    the same thing, a pre-deployment-decision latency, which is what makes the comparison
    fair rather than rhetorical. Read against the filing date, the announcement stops
    being a product reveal and becomes a confirmation of an architecture already
    committed to silicon and to the patent record before the public ever heard the number.

    # Sources

    ## Patents
    - US 2026/0125022 A1, Predictive Airbag Deployment using Vehicle Vision Data.
""")

# Same shape/length/fence as VALID_COMPOSE but no [dddd] anchor.
COMPOSE_NO_ANCHOR = textwrap.dedent("""\
    ---
    essay_id: 044-tesla-rcm-vindication
    patent_reference: US 2026/0125022 A1
    spine_source: handoff/01-design/thesis-spine.md
    draft_version: 1
    mode_used: walkthrough
    posture_used: measured
    closing_posture: firm
    ---

    # Tesla Filed the 70ms Airbag Patent Before It Announced the 70ms Airbag

    ## When the Announcement Arrived Late

    This spring, Tesla described its predictive restraint system as an unprecedented
    pre-impact response. The description was accurate. It was also roughly eleven months
    late: the patent that explains the response had already been on file since October
    2024. The announcement did not reveal the architecture. It caught up to it.

    ## What the Patent Actually Routes

    The restraint-control module does not wait for the crash. The vision sensor array
    computes a pre-impact prediction and routes it to the vehicle control unit, which
    arms the airbag module before an accelerometer would register the impact. The patent
    is explicit that this is not a backup channel: it describes the vision sensor
    providing pre-impact prediction to the airbag controller, and notes that the
    vision sensor functions as a predictive input rather than a redundant sensor.

    Conventional restraint systems are reactive by construction. Industry
    accelerometer-based ECUs reach a deployment decision within roughly ten milliseconds
    of crash detection. Tesla's architecture moves that decision upstream of the crash
    entirely, so the deployment decision is made approximately seventy milliseconds
    before traditional accelerometer-based systems would respond. Both figures describe
    the same thing, a pre-deployment-decision latency, which is what makes the comparison
    fair rather than rhetorical. Read against the filing date, the announcement stops
    being a product reveal and becomes a confirmation of an architecture already
    committed to silicon and to the patent record before the public ever heard the number.

    # Sources

    ## Patents
    - US 2026/0125022 A1, Predictive Airbag Deployment using Vehicle Vision Data.
""")

# Starts with ---, has [dddd], but well under 800 stripped chars.
COMPOSE_TOO_SHORT = textwrap.dedent("""\
    ---
    essay_id: short-draft
    closing_posture: firm
    ---

    # Short Draft

    A brief body with one patent cite [0016] that is far under the length floor.
""")

# Long enough + has anchor, but first non-whitespace line is not ---.
COMPOSE_NO_FENCE = textwrap.dedent("""\
    # Tesla Filed the 70ms Airbag Patent Before It Announced the 70ms Airbag

    ## When the Announcement Arrived Late

    This spring, Tesla described its predictive restraint system as an unprecedented
    pre-impact response. The description was accurate. It was also roughly eleven months
    late: the patent that explains the response had already been on file since October
    2024. The announcement did not reveal the architecture. It caught up to it.

    ## What the Patent Actually Routes

    The restraint-control module does not wait for the crash. The vision sensor array
    computes a pre-impact prediction and routes it to the vehicle control unit, which
    arms the airbag module before an accelerometer would register the impact. The patent
    is explicit that this is not a backup channel: it describes the vision sensor
    providing pre-impact prediction to the airbag controller [0016], and notes that the
    vision sensor functions as a predictive input rather than a redundant sensor.

    Conventional restraint systems are reactive by construction. Industry
    accelerometer-based ECUs reach a deployment decision within roughly ten milliseconds
    of crash detection. Tesla's architecture moves that decision upstream of the crash
    entirely, so the deployment decision is made approximately seventy milliseconds
    before traditional accelerometer-based systems would respond. Both figures describe
    the same thing, a pre-deployment-decision latency, which is what makes the comparison
    fair rather than rhetorical. Read against the filing date, the announcement stops
    being a product reveal and becomes a confirmation of an architecture already
    committed to silicon and to the patent record before the public ever heard the number.

    The next continuation filing, or the next safety disclosure, will either carry the
    same vision-first decision path or quietly walk it back. The patent is the more
    durable record. Companies announce when it is convenient; they file when they have
    already decided. That timing gap is the essay's entire point, and the architecture
    that made the seventy-millisecond claim possible was committed before the public
    number arrived.

    # Sources

    ## Patents
    - US 2026/0125022 A1, Predictive Airbag Deployment using Vehicle Vision Data.
""")

# Valid revision-round compose: DISPOSITIONS comment, then --- fence, [dddd], >=800 chars.
VALID_COMPOSE_REVISION = textwrap.dedent("""\
    <!-- DISPOSITIONS
    f1: applied
    f2: rejected: span already covers the claim
    -->
    ---
    essay_id: 044-tesla-rcm-vindication
    patent_reference: US 2026/0125022 A1
    spine_source: handoff/01-design/thesis-spine.md
    draft_version: 2
    mode_used: walkthrough
    posture_used: measured
    closing_posture: firm
    ---

    # Tesla Filed the 70ms Airbag Patent Before It Announced the 70ms Airbag

    ## When the Announcement Arrived Late

    This spring, Tesla described its predictive restraint system as an unprecedented
    pre-impact response. The description was accurate. It was also roughly eleven months
    late: the patent that explains the response had already been on file since October
    2024. The announcement did not reveal the architecture. It caught up to it.

    ## What the Patent Actually Routes

    The restraint-control module does not wait for the crash. The vision sensor array
    computes a pre-impact prediction and routes it to the vehicle control unit, which
    arms the airbag module before an accelerometer would register the impact. The patent
    is explicit that this is not a backup channel: it describes the vision sensor
    providing pre-impact prediction to the airbag controller [0016], and notes that the
    vision sensor functions as a predictive input rather than a redundant sensor.

    Conventional restraint systems are reactive by construction. Industry
    accelerometer-based ECUs reach a deployment decision within roughly ten milliseconds
    of crash detection. Tesla's architecture moves that decision upstream of the crash
    entirely, so the deployment decision is made approximately seventy milliseconds
    before traditional accelerometer-based systems would respond. Both figures describe
    the same thing, a pre-deployment-decision latency, which is what makes the comparison
    fair rather than rhetorical. Read against the filing date, the announcement stops
    being a product reveal and becomes a confirmation of an architecture already
    committed to silicon and to the patent record before the public ever heard the number.

    # Sources

    ## Patents
    - US 2026/0125022 A1, Predictive Airbag Deployment using Vehicle Vision Data.
""")

# Same shape/length/---/anchor as VALID_COMPOSE_REVISION but no DISPOSITIONS substring.
COMPOSE_REVISION_NO_DISPOSITIONS = textwrap.dedent("""\
    <!-- NOTES
    f1: applied
    f2: rejected: span already covers the claim
    -->
    ---
    essay_id: 044-tesla-rcm-vindication
    patent_reference: US 2026/0125022 A1
    spine_source: handoff/01-design/thesis-spine.md
    draft_version: 2
    mode_used: walkthrough
    posture_used: measured
    closing_posture: firm
    ---

    # Tesla Filed the 70ms Airbag Patent Before It Announced the 70ms Airbag

    ## When the Announcement Arrived Late

    This spring, Tesla described its predictive restraint system as an unprecedented
    pre-impact response. The description was accurate. It was also roughly eleven months
    late: the patent that explains the response had already been on file since October
    2024. The announcement did not reveal the architecture. It caught up to it.

    ## What the Patent Actually Routes

    The restraint-control module does not wait for the crash. The vision sensor array
    computes a pre-impact prediction and routes it to the vehicle control unit, which
    arms the airbag module before an accelerometer would register the impact. The patent
    is explicit that this is not a backup channel: it describes the vision sensor
    providing pre-impact prediction to the airbag controller [0016], and notes that the
    vision sensor functions as a predictive input rather than a redundant sensor.

    Conventional restraint systems are reactive by construction. Industry
    accelerometer-based ECUs reach a deployment decision within roughly ten milliseconds
    of crash detection. Tesla's architecture moves that decision upstream of the crash
    entirely, so the deployment decision is made approximately seventy milliseconds
    before traditional accelerometer-based systems would respond. Both figures describe
    the same thing, a pre-deployment-decision latency, which is what makes the comparison
    fair rather than rhetorical. Read against the filing date, the announcement stops
    being a product reveal and becomes a confirmation of an architecture already
    committed to silicon and to the patent record before the public ever heard the number.

    # Sources

    ## Patents
    - US 2026/0125022 A1, Predictive Airbag Deployment using Vehicle Vision Data.
""")

# Has DISPOSITIONS + anchor + length, but no line that is exactly --- after strip.
COMPOSE_REVISION_NO_FENCE_LINE = textwrap.dedent("""\
    <!-- DISPOSITIONS
    f1: applied
    f2: rejected: span already covers the claim
    -->
    essay_id: 044-tesla-rcm-vindication
    patent_reference: US 2026/0125022 A1
    spine_source: handoff/01-design/thesis-spine.md
    draft_version: 2
    mode_used: walkthrough
    posture_used: measured
    closing_posture: firm

    # Tesla Filed the 70ms Airbag Patent Before It Announced the 70ms Airbag

    ## When the Announcement Arrived Late

    This spring, Tesla described its predictive restraint system as an unprecedented
    pre-impact response. The description was accurate. It was also roughly eleven months
    late: the patent that explains the response had already been on file since October
    2024. The announcement did not reveal the architecture. It caught up to it.

    ## What the Patent Actually Routes

    The restraint-control module does not wait for the crash. The vision sensor array
    computes a pre-impact prediction and routes it to the vehicle control unit, which
    arms the airbag module before an accelerometer would register the impact. The patent
    is explicit that this is not a backup channel: it describes the vision sensor
    providing pre-impact prediction to the airbag controller [0016], and notes that the
    vision sensor functions as a predictive input rather than a redundant sensor.

    Conventional restraint systems are reactive by construction. Industry
    accelerometer-based ECUs reach a deployment decision within roughly ten milliseconds
    of crash detection. Tesla's architecture moves that decision upstream of the crash
    entirely, so the deployment decision is made approximately seventy milliseconds
    before traditional accelerometer-based systems would respond. Both figures describe
    the same thing, a pre-deployment-decision latency, which is what makes the comparison
    fair rather than rhetorical. Read against the filing date, the announcement stops
    being a product reveal and becomes a confirmation of an architecture already
    committed to silicon and to the patent record before the public ever heard the number.

    The next continuation filing, or the next safety disclosure, will either carry the
    same vision-first decision path or quietly walk it back. The patent is the more
    durable record. Companies announce when it is convenient; they file when they have
    already decided. That timing gap is the essay's entire point, and the architecture
    that made the seventy-millisecond claim possible was committed before the public
    number arrived.

    # Sources

    ## Patents
    - US 2026/0125022 A1, Predictive Airbag Deployment using Vehicle Vision Data.
""")

# Valid promo-pack for --validate promo: Verification Status substring + >=600 stripped chars.
VALID_PROMO = textwrap.dedent("""\
    ---
    essay_id: intel-us20260191095-backend-hbm
    essay_source: essays/intel-us20260191095-backend-hbm/essay-final.md
    closing_posture: measured
    promo_posture: D
    promo_version: 1
    owner_briefing: read
    ---

    # Promo pack: intel-us20260191095-backend-hbm

    === Verification Status (promo-composer, promo-pack) ===
    sources: essay-final.md (draft_version 6) + publication.md + owner-briefing.md
    fact_trace: PASS (every factual phrase mapped; dropped facts: none)
    subrules: 1 sequence PASS / 2 arithmetic PASS / 3 anchors PASS
    bold_selection: KR lead = signature line 2, insurance 1 clause; P1 = reader_sentence, insurance 1 clause; process narration 0
    kr_long: 612자/400-800, 4 단락, 아티클 포인터 있음, 의문형 0, 느낌표 0
    thread: 3 posts, message-unit (X Premium, no char cap), 439/775/552 chars, link slot in final post
    hygiene: em-dash 0, bold 0, emoji 0/1, hashtags 0, banned terms 0
    attachments: cover-5x2.png (KR post, post 1), alt verbatim from posting-checklist.md
    suspected_essay_defects: none
    === Deliverables ===

    ## 1. Korean long-form promo post (X, 400-800자)

    ```text
    인텔은 메모리에서 손을 뗀 회사입니다. 2021년에 NAND 사업을 SK하이닉스에 팔았고, 이듬해에는 Optane 라인도 정리했습니다. 지금 세계의 HBM은 SK하이닉스, 삼성, 마이크론 세 회사가 만들고, 인텔의 몫은 없습니다.

    그런 인텔이 최근 DRAM 출원을 하나 냈습니다. 특이한 것은 셀을 만드는 위치입니다. 청구항 1이 실제로 요구하는 것도 이 한 단어, backend입니다. [ARTICLE-LINK]
    ```

    - 자수: 612 (공백 포함, [ARTICLE-LINK]=23자)
    - attach: publication-package/cover-5x2.png
    - alt: "FIG. 1B: the claimed eight-high memory stack on its base die."

    ## 2. English thread (2-4 message-unit posts)

    ```text
    Intel walked away from memory. It sold its NAND business to SK hynix in 2021 and wound down Optane the year after. Three companies make the world's HBM today, and Intel is not one of them.
    ```

    - chars: 439 (message: the story; first sentence is the collapsed-preview hook)
""")

# Contains Verification Status but well under 600 stripped characters.
PROMO_TOO_SHORT = textwrap.dedent("""\
    ---
    essay_id: short-promo
    promo_version: 1
    ---

    === Verification Status (promo-composer, promo-pack) ===
    fact_trace: PASS
    === Deliverables ===

    ## 1. Korean long-form promo post

    ```text
    짧은 프로모입니다. [ARTICLE-LINK]
    ```
""")

# Same overall length/shape as VALID_PROMO but no "Verification Status" substring.
PROMO_NO_VERIFICATION_STATUS = textwrap.dedent("""\
    ---
    essay_id: intel-us20260191095-backend-hbm
    essay_source: essays/intel-us20260191095-backend-hbm/essay-final.md
    closing_posture: measured
    promo_posture: D
    promo_version: 1
    owner_briefing: read
    ---

    # Promo pack: intel-us20260191095-backend-hbm

    === Pack Header (promo-composer, promo-pack) ===
    sources: essay-final.md (draft_version 6) + publication.md + owner-briefing.md
    fact_trace: PASS (every factual phrase mapped; dropped facts: none)
    subrules: 1 sequence PASS / 2 arithmetic PASS / 3 anchors PASS
    bold_selection: KR lead = signature line 2, insurance 1 clause; P1 = reader_sentence, insurance 1 clause; process narration 0
    kr_long: 612자/400-800, 4 단락, 아티클 포인터 있음, 의문형 0, 느낌표 0
    thread: 3 posts, message-unit (X Premium, no char cap), 439/775/552 chars, link slot in final post
    hygiene: em-dash 0, bold 0, emoji 0/1, hashtags 0, banned terms 0
    attachments: cover-5x2.png (KR post, post 1), alt verbatim from posting-checklist.md
    suspected_essay_defects: none
    === Deliverables ===

    ## 1. Korean long-form promo post (X, 400-800자)

    ```text
    인텔은 메모리에서 손을 뗀 회사입니다. 2021년에 NAND 사업을 SK하이닉스에 팔았고, 이듬해에는 Optane 라인도 정리했습니다. 지금 세계의 HBM은 SK하이닉스, 삼성, 마이크론 세 회사가 만들고, 인텔의 몫은 없습니다.

    그런 인텔이 최근 DRAM 출원을 하나 냈습니다. 특이한 것은 셀을 만드는 위치입니다. 청구항 1이 실제로 요구하는 것도 이 한 단어, backend입니다. [ARTICLE-LINK]
    ```

    - 자수: 612 (공백 포함, [ARTICLE-LINK]=23자)
    - attach: publication-package/cover-5x2.png
    - alt: "FIG. 1B: the claimed eight-high memory stack on its base die."

    ## 2. English thread (2-4 message-unit posts)

    ```text
    Intel walked away from memory. It sold its NAND business to SK hynix in 2021 and wound down Optane the year after. Three companies make the world's HBM today, and Intel is not one of them.
    ```

    - chars: 439 (message: the story; first sentence is the collapsed-preview hook)
""")


def _write_stub(path: str, body: str) -> None:
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(body)
    os.chmod(path, os.stat(path).st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)


def _restricted_env(bin_dir: str) -> dict:
    """PATH = bin_dir:/usr/bin:/bin — never leak real codex/grok from user PATH."""
    env = os.environ.copy()
    env["PATH"] = "%s:/usr/bin:/bin" % bin_dir
    return env


def _run_cli(args: list[str], env: dict, timeout: int = 30) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, CLI_LANE] + args,
        capture_output=True,
        text=True,
        env=env,
        timeout=timeout,
    )


def _parse_json_line(stdout: str) -> dict:
    lines = [ln.strip() for ln in stdout.splitlines() if ln.strip()]
    assert lines, "expected one JSON line on stdout, got empty"
    # Last non-empty line (in case of incidental noise)
    return json.loads(lines[-1])


class CliLaneTestBase(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix="test_cli_lane_")
        self.bin_dir = os.path.join(self.tmp, "bin")
        os.makedirs(self.bin_dir)
        self.prompt_path = os.path.join(self.tmp, "prompt.md")
        self.output_path = os.path.join(self.tmp, "out.md")
        with open(self.prompt_path, "w", encoding="utf-8") as fh:
            fh.write("test prompt body\n")
        self.env = _restricted_env(self.bin_dir)
        # Sanity: with empty bin_dir, neither CLI should resolve.
        which_env = self.env.copy()
        # Ensure empty bin has no stubs yet for this check on a fresh setUp
        # (stubs added per-test). First assert PATH construction is isolation-safe.
        self.assertIsNone(
            self._which_with_env("codex", _restricted_env(os.path.join(self.tmp, "empty_never"))),
            "PATH isolation broken: real codex visible",
        )
        empty = os.path.join(self.tmp, "empty_never")
        os.makedirs(empty, exist_ok=True)
        self.assertIsNone(
            self._which_with_env("grok", _restricted_env(empty)),
            "PATH isolation broken: real grok visible",
        )

    def tearDown(self):
        # Best-effort cleanup of temp tree.
        for root, dirs, files in os.walk(self.tmp, topdown=False):
            for name in files:
                try:
                    os.remove(os.path.join(root, name))
                except OSError:
                    pass
            for name in dirs:
                try:
                    os.rmdir(os.path.join(root, name))
                except OSError:
                    pass
        try:
            os.rmdir(self.tmp)
        except OSError:
            pass

    @staticmethod
    def _which_with_env(name: str, env: dict):
        path = env.get("PATH", "")
        for d in path.split(os.pathsep):
            cand = os.path.join(d, name)
            if os.path.isfile(cand) and os.access(cand, os.X_OK):
                return cand
        return None

    def _install_codex(self, mode: str = "success", content: str = GPT_CANNED) -> None:
        """Install stub codex. mode: success|nonzero|timeout|empty|grounding|invalid."""
        # Escape content for embedding in a bash heredoc with quoted EOF.
        if mode == "nonzero":
            body = "#!/bin/bash\nexit 1\n"
        elif mode == "timeout":
            body = "#!/bin/bash\nsleep 5\nexit 0\n"
        elif mode == "empty":
            body = textwrap.dedent("""\
                #!/bin/bash
                out=""
                while [ $# -gt 0 ]; do
                  if [ "$1" = "-o" ]; then out="$2"; shift 2; continue; fi
                  shift
                done
                printf '   \\n\\n  ' > "$out"
                exit 0
            """)
        else:
            # success / grounding / invalid — write content to -o file
            # Use a base64-ish approach via printf %s with escaped content in a
            # quoted heredoc so binary-safety is not required (text only).
            body = (
                "#!/bin/bash\n"
                "out=\"\"\n"
                "while [ $# -gt 0 ]; do\n"
                "  if [ \"$1\" = \"-o\" ]; then out=\"$2\"; shift 2; continue; fi\n"
                "  shift\n"
                "done\n"
                "if [ -z \"$out\" ]; then echo 'no -o' >&2; exit 1; fi\n"
                "cat > \"$out\" <<'EOF'\n"
                + content
                + ("\n" if not content.endswith("\n") else "")
                + "EOF\n"
                "exit 0\n"
            )
        _write_stub(os.path.join(self.bin_dir, "codex"), body)

    def _grok_envelope_fixture(self, content: str, name: str = "grok_stdout.json") -> str:
        """Write a grok JSON envelope fixture; return its path for the bash stub to cat."""
        envelope = json.dumps({
            "structuredOutput": {"document": content},
            "text": json.dumps({"document": content}),
        })
        fixture_path = os.path.join(self.tmp, name)
        with open(fixture_path, "w", encoding="utf-8") as fh:
            fh.write(envelope)
        return fixture_path

    def _install_grok(self, mode: str = "success", content: str = GROK_CANNED) -> None:
        if mode == "nonzero":
            body = "#!/bin/bash\nexit 1\n"
        elif mode == "timeout":
            body = "#!/bin/bash\nsleep 5\nexit 0\n"
        elif mode == "empty":
            # Whitespace-only document inside a valid JSON envelope so empty-output
            # still fires after extraction (not invalid-output from parse failure).
            fixture_path = self._grok_envelope_fixture("   \n\n  ", name="grok_stdout_empty.json")
            body = "#!/bin/bash\ncat '%s'\nexit 0\n" % fixture_path
        else:
            # success — cat a pre-built JSON envelope (document = content).
            fixture_path = self._grok_envelope_fixture(content)
            body = "#!/bin/bash\ncat '%s'\nexit 0\n" % fixture_path
        _write_stub(os.path.join(self.bin_dir, "grok"), body)

    def _install_grok_argv_recorder(self, record_path: str, content: str = GROK_CANNED) -> None:
        """Install a grok stub that records full argv (one arg per line) then succeeds."""
        # Single-quote record_path for the shell (escape embedded single quotes).
        rec = record_path.replace("'", "'\\''")
        fixture_path = self._grok_envelope_fixture(content, name="grok_argv_stdout.json")
        fix = fixture_path.replace("'", "'\\''")
        body = (
            "#!/bin/bash\n"
            "printf '%%s\\n' \"$@\" > '%s'\n"
            "cat '%s'\n"
            "exit 0\n"
        ) % (rec, fix)
        _write_stub(os.path.join(self.bin_dir, "grok"), body)


class TestGptSuccess(CliLaneTestBase):
    def test_gpt_success(self):
        self._install_codex(mode="success", content=GPT_CANNED)
        proc = _run_cli(
            ["--vendor", "gpt", "--prompt-file", self.prompt_path, "--output", self.output_path],
            self.env,
        )
        self.assertEqual(proc.returncode, 0, proc.stderr)
        data = _parse_json_line(proc.stdout)
        self.assertTrue(data["ok"])
        self.assertEqual(data["vendor"], "gpt")
        self.assertEqual(data["output"], self.output_path)
        self.assertIn("duration_s", data)
        self.assertTrue(os.path.isfile(self.output_path))
        with open(self.output_path, encoding="utf-8") as fh:
            self.assertEqual(fh.read(), GPT_CANNED if GPT_CANNED.endswith("\n") else GPT_CANNED + "\n")


class TestGrokSuccess(CliLaneTestBase):
    def test_grok_success(self):
        self._install_grok(mode="success", content=GROK_CANNED)
        proc = _run_cli(
            ["--vendor", "grok", "--prompt-file", self.prompt_path, "--output", self.output_path],
            self.env,
        )
        self.assertEqual(proc.returncode, 0, proc.stderr)
        data = _parse_json_line(proc.stdout)
        self.assertTrue(data["ok"])
        self.assertEqual(data["vendor"], "grok")
        self.assertEqual(data["output"], self.output_path)
        self.assertTrue(os.path.isfile(self.output_path))
        with open(self.output_path, encoding="utf-8") as fh:
            got = fh.read()
        self.assertEqual(got, GROK_CANNED if GROK_CANNED.endswith("\n") else GROK_CANNED + "\n")


class TestGrokCwdAbsolutized(CliLaneTestBase):
    def test_relative_cwd_and_prompt_file_forwarded_as_absolute(self):
        """Relative --cwd and --prompt-file must arrive on grok argv as absolute paths.

        Use os.path.relpath against the real process cwd so both values are
        genuinely relative (no os.chdir, no subprocess cwd= on _run_cli).
        Without absolutizing --prompt-file, grok would resolve it against the
        already-changed subprocess cwd and double-apply the path prefix.
        """
        target_dir = os.path.join(self.tmp, "compose_cwd")
        os.makedirs(target_dir)
        relative_cwd = os.path.relpath(target_dir, os.getcwd())
        self.assertFalse(
            os.path.isabs(relative_cwd),
            "test setup must pass a relative --cwd: %r" % relative_cwd,
        )
        relative_prompt = os.path.relpath(self.prompt_path, os.getcwd())
        self.assertFalse(
            os.path.isabs(relative_prompt),
            "test setup must pass a relative --prompt-file: %r" % relative_prompt,
        )

        record_path = os.path.join(self.tmp, "grok_argv.txt")
        self._install_grok_argv_recorder(record_path)

        proc = _run_cli(
            [
                "--vendor", "grok",
                "--prompt-file", relative_prompt,
                "--output", self.output_path,
                "--cwd", relative_cwd,
            ],
            self.env,
        )
        self.assertEqual(proc.returncode, 0, proc.stderr + proc.stdout)
        data = _parse_json_line(proc.stdout)
        self.assertTrue(data["ok"])

        with open(record_path, encoding="utf-8") as fh:
            argv_lines = [ln.rstrip("\n") for ln in fh.readlines()]
        self.assertIn("--cwd", argv_lines)
        cwd_idx = argv_lines.index("--cwd")
        self.assertLess(cwd_idx + 1, len(argv_lines), "missing value after --cwd")
        recorded_cwd = argv_lines[cwd_idx + 1]
        self.assertTrue(os.path.isabs(recorded_cwd), recorded_cwd)

        self.assertIn("--prompt-file", argv_lines)
        pf_idx = argv_lines.index("--prompt-file")
        self.assertLess(pf_idx + 1, len(argv_lines), "missing value after --prompt-file")
        recorded_prompt = argv_lines[pf_idx + 1]
        self.assertTrue(os.path.isabs(recorded_prompt), recorded_prompt)

        # Default --max-turns (not passed on cli_lane.py) must forward 16 to grok
        # (runaway-turn guard only; isolation is tool-less, not turn-cap).
        self.assertIn("--max-turns", argv_lines)
        mt_idx = argv_lines.index("--max-turns")
        self.assertLess(mt_idx + 1, len(argv_lines), "missing value after --max-turns")
        self.assertEqual(argv_lines[mt_idx + 1], "16")

        # Constrained capture: --json-schema document envelope replaces --output-format.
        self.assertIn("--json-schema", argv_lines)
        js_idx = argv_lines.index("--json-schema")
        self.assertLess(js_idx + 1, len(argv_lines), "missing value after --json-schema")
        self.assertEqual(argv_lines[js_idx + 1], GROK_DOC_SCHEMA)
        self.assertNotIn("--output-format", argv_lines)

        # Isolation flags: always applied unconditionally on every grok invoke.
        self.assertIn("--tools", argv_lines)
        tools_idx = argv_lines.index("--tools")
        self.assertLess(tools_idx + 1, len(argv_lines), "missing value after --tools")
        self.assertEqual(argv_lines[tools_idx + 1], "")
        self.assertIn("--no-subagents", argv_lines)
        self.assertIn("--disable-web-search", argv_lines)

    def test_explicit_max_turns_forwarded(self):
        """Explicit --max-turns N must appear on grok argv as that N."""
        record_path = os.path.join(self.tmp, "grok_argv_max_turns.txt")
        self._install_grok_argv_recorder(record_path)

        proc = _run_cli(
            [
                "--vendor", "grok",
                "--prompt-file", self.prompt_path,
                "--output", self.output_path,
                "--max-turns", "3",
            ],
            self.env,
        )
        self.assertEqual(proc.returncode, 0, proc.stderr + proc.stdout)
        data = _parse_json_line(proc.stdout)
        self.assertTrue(data["ok"])

        with open(record_path, encoding="utf-8") as fh:
            argv_lines = [ln.rstrip("\n") for ln in fh.readlines()]
        self.assertIn("--max-turns", argv_lines)
        mt_idx = argv_lines.index("--max-turns")
        self.assertLess(mt_idx + 1, len(argv_lines), "missing value after --max-turns")
        self.assertEqual(argv_lines[mt_idx + 1], "3")


class TestCliMissing(CliLaneTestBase):
    def test_cli_missing_real_run(self):
        # bin_dir empty — no stubs
        proc = _run_cli(
            ["--vendor", "gpt", "--prompt-file", self.prompt_path, "--output", self.output_path],
            self.env,
        )
        self.assertEqual(proc.returncode, 3, proc.stdout + proc.stderr)
        data = _parse_json_line(proc.stdout)
        self.assertFalse(data["ok"])
        self.assertTrue(data["substituted"])
        self.assertEqual(data["reason"], "cli-missing")
        self.assertEqual(data["vendor"], "gpt")
        self.assertFalse(os.path.exists(self.output_path))

    def test_cli_missing_check(self):
        proc = _run_cli(["--vendor", "gpt", "--check"], self.env)
        self.assertEqual(proc.returncode, 3, proc.stdout + proc.stderr)
        data = _parse_json_line(proc.stdout)
        self.assertFalse(data["ok"])
        self.assertTrue(data["substituted"])
        self.assertEqual(data["reason"], "cli-missing")
        self.assertIn("codex", data.get("detail", ""))


class TestCheckPresent(CliLaneTestBase):
    def test_check_gpt_present(self):
        self._install_codex(mode="success")
        proc = _run_cli(["--vendor", "gpt", "--check"], self.env)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        data = _parse_json_line(proc.stdout)
        self.assertEqual(data, {"ok": True, "vendor": "gpt", "check": True})

    def test_check_grok_present(self):
        self._install_grok(mode="success")
        proc = _run_cli(["--vendor", "grok", "--check"], self.env)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        data = _parse_json_line(proc.stdout)
        self.assertEqual(data, {"ok": True, "vendor": "grok", "check": True})


class TestNonzero(CliLaneTestBase):
    def test_gpt_nonzero(self):
        self._install_codex(mode="nonzero")
        # Pre-create a partial output file to confirm cleanup
        with open(self.output_path, "w", encoding="utf-8") as fh:
            fh.write("partial")
        proc = _run_cli(
            ["--vendor", "gpt", "--prompt-file", self.prompt_path, "--output", self.output_path],
            self.env,
        )
        self.assertEqual(proc.returncode, 3, proc.stdout + proc.stderr)
        data = _parse_json_line(proc.stdout)
        self.assertEqual(data["reason"], "nonzero")
        self.assertTrue(data["substituted"])
        self.assertFalse(os.path.exists(self.output_path))

    def test_grok_nonzero(self):
        self._install_grok(mode="nonzero")
        proc = _run_cli(
            ["--vendor", "grok", "--prompt-file", self.prompt_path, "--output", self.output_path],
            self.env,
        )
        self.assertEqual(proc.returncode, 3)
        data = _parse_json_line(proc.stdout)
        self.assertEqual(data["reason"], "nonzero")
        self.assertFalse(os.path.exists(self.output_path))


class TestTimeout(CliLaneTestBase):
    def test_gpt_timeout(self):
        self._install_codex(mode="timeout")
        proc = _run_cli(
            [
                "--vendor", "gpt",
                "--prompt-file", self.prompt_path,
                "--output", self.output_path,
                "--timeout", "1",
            ],
            self.env,
            timeout=15,
        )
        self.assertEqual(proc.returncode, 3, proc.stdout + proc.stderr)
        data = _parse_json_line(proc.stdout)
        self.assertEqual(data["reason"], "timeout")
        self.assertFalse(os.path.exists(self.output_path))

    def test_grok_timeout(self):
        self._install_grok(mode="timeout")
        proc = _run_cli(
            [
                "--vendor", "grok",
                "--prompt-file", self.prompt_path,
                "--output", self.output_path,
                "--timeout", "1",
            ],
            self.env,
            timeout=15,
        )
        self.assertEqual(proc.returncode, 3, proc.stdout + proc.stderr)
        data = _parse_json_line(proc.stdout)
        self.assertEqual(data["reason"], "timeout")
        self.assertFalse(os.path.exists(self.output_path))


class TestGptStdinNotInherited(CliLaneTestBase):
    def test_codex_child_gets_devnull_not_parent_pipe(self):
        """cli_lane must not forward its own (possibly never-EOF) stdin to codex.

        Background/piped orchestrator runs leave stdin as an open pipe; codex
        exec appends stdin when not a TTY. With stdin=DEVNULL on the child, a
        stub that does extra="$(cat)" returns immediately; if the open pipe
        were inherited, the stub (and this test) would hang until timeout.
        """
        content = GPT_CANNED
        body = (
            "#!/bin/bash\n"
            "extra=\"$(cat)\"\n"
            "out=\"\"\n"
            "while [ $# -gt 0 ]; do\n"
            "  if [ \"$1\" = \"-o\" ]; then out=\"$2\"; shift 2; continue; fi\n"
            "  shift\n"
            "done\n"
            "if [ -z \"$out\" ]; then echo 'no -o' >&2; exit 1; fi\n"
            "cat > \"$out\" <<'EOF'\n"
            + content
            + ("\n" if not content.endswith("\n") else "")
            + "EOF\n"
            "exit 0\n"
        )
        _write_stub(os.path.join(self.bin_dir, "codex"), body)

        # Outer cli_lane stdin is a never-EOF pipe (live background hang shape).
        # If cli_lane inherited/forwarded it to codex, the stub's cat would block.
        r_fd, w_fd = os.pipe()
        try:
            proc = subprocess.run(
                [
                    sys.executable,
                    CLI_LANE,
                    "--vendor", "gpt",
                    "--prompt-file", self.prompt_path,
                    "--output", self.output_path,
                    "--timeout", "5",
                ],
                stdin=r_fd,
                capture_output=True,
                text=True,
                env=self.env,
                timeout=8,
            )
        finally:
            try:
                os.close(r_fd)
            except OSError:
                pass
            try:
                os.close(w_fd)
            except OSError:
                pass

        self.assertEqual(proc.returncode, 0, proc.stderr + proc.stdout)
        data = _parse_json_line(proc.stdout)
        self.assertTrue(data["ok"])


class TestEmptyOutput(CliLaneTestBase):
    def test_gpt_empty(self):
        self._install_codex(mode="empty")
        proc = _run_cli(
            ["--vendor", "gpt", "--prompt-file", self.prompt_path, "--output", self.output_path],
            self.env,
        )
        self.assertEqual(proc.returncode, 3, proc.stdout + proc.stderr)
        data = _parse_json_line(proc.stdout)
        self.assertEqual(data["reason"], "empty-output")
        self.assertFalse(os.path.exists(self.output_path))

    def test_grok_empty(self):
        self._install_grok(mode="empty")
        proc = _run_cli(
            ["--vendor", "grok", "--prompt-file", self.prompt_path, "--output", self.output_path],
            self.env,
        )
        self.assertEqual(proc.returncode, 3, proc.stdout + proc.stderr)
        data = _parse_json_line(proc.stdout)
        self.assertEqual(data["reason"], "empty-output")
        self.assertFalse(os.path.exists(self.output_path))


class TestGrokNonJsonStdout(CliLaneTestBase):
    def test_non_json_stdout_invalid_output(self):
        """Plain narration stdout (no JSON envelope) must substitute as invalid-output."""
        body = (
            "#!/bin/bash\n"
            "cat <<'EOF'\n"
            "I'll compose the essay now.\n"
            "---\n"
            "some content\n"
            "EOF\n"
            "exit 0\n"
        )
        _write_stub(os.path.join(self.bin_dir, "grok"), body)
        proc = _run_cli(
            ["--vendor", "grok", "--prompt-file", self.prompt_path, "--output", self.output_path],
            self.env,
        )
        self.assertEqual(proc.returncode, 3, proc.stdout + proc.stderr)
        data = _parse_json_line(proc.stdout)
        self.assertEqual(data["reason"], "invalid-output")
        self.assertTrue(data["substituted"])
        self.assertFalse(os.path.exists(self.output_path))
        self.assertIn("json envelope", data.get("detail", "").lower())


class TestValidateGrounding(CliLaneTestBase):
    def test_valid_grounding(self):
        self._install_codex(mode="success", content=VALID_GROUNDING)
        proc = _run_cli(
            [
                "--vendor", "gpt",
                "--prompt-file", self.prompt_path,
                "--output", self.output_path,
                "--validate", "grounding",
            ],
            self.env,
        )
        self.assertEqual(proc.returncode, 0, proc.stderr + proc.stdout)
        data = _parse_json_line(proc.stdout)
        self.assertTrue(data["ok"])
        self.assertTrue(os.path.isfile(self.output_path))
        with open(self.output_path, encoding="utf-8") as fh:
            body = fh.read()
        self.assertIn("verifier:", body)
        self.assertIn("SUPPORTED", body)
        self.assertIn("|---", body)

    def test_invalid_grounding_no_verdict(self):
        self._install_codex(mode="success", content=INVALID_GROUNDING)
        proc = _run_cli(
            [
                "--vendor", "gpt",
                "--prompt-file", self.prompt_path,
                "--output", self.output_path,
                "--validate", "grounding",
            ],
            self.env,
        )
        self.assertEqual(proc.returncode, 3, proc.stdout + proc.stderr)
        data = _parse_json_line(proc.stdout)
        self.assertEqual(data["reason"], "invalid-output")
        self.assertTrue(data["substituted"])
        self.assertFalse(os.path.exists(self.output_path))


class TestValidateCompose(CliLaneTestBase):
    def test_valid_compose(self):
        self._install_grok(mode="success", content=VALID_COMPOSE)
        proc = _run_cli(
            [
                "--vendor", "grok",
                "--prompt-file", self.prompt_path,
                "--output", self.output_path,
                "--validate", "compose",
            ],
            self.env,
        )
        self.assertEqual(proc.returncode, 0, proc.stderr + proc.stdout)
        data = _parse_json_line(proc.stdout)
        self.assertTrue(data["ok"])
        self.assertTrue(os.path.isfile(self.output_path))
        with open(self.output_path, encoding="utf-8") as fh:
            body = fh.read()
        expected = VALID_COMPOSE if VALID_COMPOSE.endswith("\n") else VALID_COMPOSE + "\n"
        self.assertEqual(body, expected)

    def test_compose_missing_anchor(self):
        self._install_grok(mode="success", content=COMPOSE_NO_ANCHOR)
        proc = _run_cli(
            [
                "--vendor", "grok",
                "--prompt-file", self.prompt_path,
                "--output", self.output_path,
                "--validate", "compose",
            ],
            self.env,
        )
        self.assertEqual(proc.returncode, 3, proc.stdout + proc.stderr)
        data = _parse_json_line(proc.stdout)
        self.assertEqual(data["reason"], "invalid-output")
        self.assertTrue(data["substituted"])
        self.assertFalse(os.path.exists(self.output_path))
        self.assertIn("anchor", data.get("detail", "").lower())

    def test_compose_too_short(self):
        self._install_grok(mode="success", content=COMPOSE_TOO_SHORT)
        proc = _run_cli(
            [
                "--vendor", "grok",
                "--prompt-file", self.prompt_path,
                "--output", self.output_path,
                "--validate", "compose",
            ],
            self.env,
        )
        self.assertEqual(proc.returncode, 3, proc.stdout + proc.stderr)
        data = _parse_json_line(proc.stdout)
        self.assertEqual(data["reason"], "invalid-output")
        self.assertTrue(data["substituted"])
        self.assertFalse(os.path.exists(self.output_path))
        detail = data.get("detail", "").lower()
        self.assertTrue("800" in detail or "length" in detail)

    def test_compose_no_fence(self):
        self._install_grok(mode="success", content=COMPOSE_NO_FENCE)
        proc = _run_cli(
            [
                "--vendor", "grok",
                "--prompt-file", self.prompt_path,
                "--output", self.output_path,
                "--validate", "compose",
            ],
            self.env,
        )
        self.assertEqual(proc.returncode, 3, proc.stdout + proc.stderr)
        data = _parse_json_line(proc.stdout)
        self.assertEqual(data["reason"], "invalid-output")
        self.assertTrue(data["substituted"])
        self.assertFalse(os.path.exists(self.output_path))
        detail = data.get("detail", "").lower()
        self.assertTrue("---" in detail or "fence" in detail)


class TestValidateComposeRevision(CliLaneTestBase):
    def test_valid_compose_revision(self):
        self._install_grok(mode="success", content=VALID_COMPOSE_REVISION)
        proc = _run_cli(
            [
                "--vendor", "grok",
                "--prompt-file", self.prompt_path,
                "--output", self.output_path,
                "--validate", "compose-revision",
            ],
            self.env,
        )
        self.assertEqual(proc.returncode, 0, proc.stderr + proc.stdout)
        data = _parse_json_line(proc.stdout)
        self.assertTrue(data["ok"])
        self.assertTrue(os.path.isfile(self.output_path))
        with open(self.output_path, encoding="utf-8") as fh:
            body = fh.read()
        expected = (
            VALID_COMPOSE_REVISION
            if VALID_COMPOSE_REVISION.endswith("\n")
            else VALID_COMPOSE_REVISION + "\n"
        )
        self.assertEqual(body, expected)

    def test_compose_revision_missing_dispositions(self):
        self._install_grok(mode="success", content=COMPOSE_REVISION_NO_DISPOSITIONS)
        proc = _run_cli(
            [
                "--vendor", "grok",
                "--prompt-file", self.prompt_path,
                "--output", self.output_path,
                "--validate", "compose-revision",
            ],
            self.env,
        )
        self.assertEqual(proc.returncode, 3, proc.stdout + proc.stderr)
        data = _parse_json_line(proc.stdout)
        self.assertEqual(data["reason"], "invalid-output")
        self.assertTrue(data["substituted"])
        self.assertFalse(os.path.exists(self.output_path))

    def test_compose_revision_no_fence_line(self):
        self._install_grok(mode="success", content=COMPOSE_REVISION_NO_FENCE_LINE)
        proc = _run_cli(
            [
                "--vendor", "grok",
                "--prompt-file", self.prompt_path,
                "--output", self.output_path,
                "--validate", "compose-revision",
            ],
            self.env,
        )
        self.assertEqual(proc.returncode, 3, proc.stdout + proc.stderr)
        data = _parse_json_line(proc.stdout)
        self.assertEqual(data["reason"], "invalid-output")
        self.assertTrue(data["substituted"])
        self.assertFalse(os.path.exists(self.output_path))


class TestValidatePromo(CliLaneTestBase):
    def test_valid_promo(self):
        self._install_grok(mode="success", content=VALID_PROMO)
        proc = _run_cli(
            [
                "--vendor", "grok",
                "--prompt-file", self.prompt_path,
                "--output", self.output_path,
                "--validate", "promo",
            ],
            self.env,
        )
        self.assertEqual(proc.returncode, 0, proc.stderr + proc.stdout)
        data = _parse_json_line(proc.stdout)
        self.assertTrue(data["ok"])
        self.assertTrue(os.path.isfile(self.output_path))
        with open(self.output_path, encoding="utf-8") as fh:
            body = fh.read()
        expected = VALID_PROMO if VALID_PROMO.endswith("\n") else VALID_PROMO + "\n"
        self.assertEqual(body, expected)

    def test_promo_too_short(self):
        self._install_grok(mode="success", content=PROMO_TOO_SHORT)
        proc = _run_cli(
            [
                "--vendor", "grok",
                "--prompt-file", self.prompt_path,
                "--output", self.output_path,
                "--validate", "promo",
            ],
            self.env,
        )
        self.assertEqual(proc.returncode, 3, proc.stdout + proc.stderr)
        data = _parse_json_line(proc.stdout)
        self.assertEqual(data["reason"], "invalid-output")
        self.assertTrue(data["substituted"])
        self.assertFalse(os.path.exists(self.output_path))
        detail = data.get("detail", "").lower()
        self.assertTrue("600" in detail or "length" in detail)

    def test_promo_missing_verification_status(self):
        self._install_grok(mode="success", content=PROMO_NO_VERIFICATION_STATUS)
        proc = _run_cli(
            [
                "--vendor", "grok",
                "--prompt-file", self.prompt_path,
                "--output", self.output_path,
                "--validate", "promo",
            ],
            self.env,
        )
        self.assertEqual(proc.returncode, 3, proc.stdout + proc.stderr)
        data = _parse_json_line(proc.stdout)
        self.assertEqual(data["reason"], "invalid-output")
        self.assertTrue(data["substituted"])
        self.assertFalse(os.path.exists(self.output_path))
        self.assertIn("verification status", data.get("detail", "").lower())


class TestValidateDrift(CliLaneTestBase):
    def test_valid_drift(self):
        self._install_codex(mode="success", content=VALID_DRIFT)
        proc = _run_cli(
            [
                "--vendor", "gpt",
                "--prompt-file", self.prompt_path,
                "--output", self.output_path,
                "--validate", "drift",
            ],
            self.env,
        )
        self.assertEqual(proc.returncode, 0, proc.stderr + proc.stdout)
        data = _parse_json_line(proc.stdout)
        self.assertTrue(data["ok"])
        self.assertTrue(os.path.isfile(self.output_path))
        with open(self.output_path, encoding="utf-8") as fh:
            body = fh.read()
        self.assertIn("verifier:", body)
        self.assertIn("MEANING-PRESERVED", body)
        self.assertIn("|---", body)

    def test_invalid_drift_no_verdict(self):
        self._install_codex(mode="success", content=INVALID_DRIFT)
        proc = _run_cli(
            [
                "--vendor", "gpt",
                "--prompt-file", self.prompt_path,
                "--output", self.output_path,
                "--validate", "drift",
            ],
            self.env,
        )
        self.assertEqual(proc.returncode, 3, proc.stdout + proc.stderr)
        data = _parse_json_line(proc.stdout)
        self.assertEqual(data["reason"], "invalid-output")
        self.assertTrue(data["substituted"])
        self.assertFalse(os.path.exists(self.output_path))


class TestValidatePregate(CliLaneTestBase):
    def test_valid_pregate(self):
        self._install_codex(mode="success", content=VALID_PREGATE)
        proc = _run_cli(
            [
                "--vendor", "gpt",
                "--prompt-file", self.prompt_path,
                "--output", self.output_path,
                "--validate", "pregate",
            ],
            self.env,
        )
        self.assertEqual(proc.returncode, 0, proc.stderr + proc.stdout)
        data = _parse_json_line(proc.stdout)
        self.assertTrue(data["ok"])
        self.assertTrue(os.path.isfile(self.output_path))
        with open(self.output_path, encoding="utf-8") as fh:
            body = fh.read()
        self.assertIn("pregate:", body)
        self.assertIn("verdict: VOICE-PASS", body)

    def test_invalid_pregate_no_verdict(self):
        self._install_codex(mode="success", content=INVALID_PREGATE)
        proc = _run_cli(
            [
                "--vendor", "gpt",
                "--prompt-file", self.prompt_path,
                "--output", self.output_path,
                "--validate", "pregate",
            ],
            self.env,
        )
        self.assertEqual(proc.returncode, 3, proc.stdout + proc.stderr)
        data = _parse_json_line(proc.stdout)
        self.assertEqual(data["reason"], "invalid-output")
        self.assertTrue(data["substituted"])
        self.assertFalse(os.path.exists(self.output_path))


class TestValidateReview(CliLaneTestBase):
    def test_valid_review(self):
        self._install_codex(mode="success", content=VALID_REVIEW)
        proc = _run_cli(
            [
                "--vendor", "gpt",
                "--prompt-file", self.prompt_path,
                "--output", self.output_path,
                "--validate", "review",
            ],
            self.env,
        )
        self.assertEqual(proc.returncode, 0, proc.stderr + proc.stdout)
        data = _parse_json_line(proc.stdout)
        self.assertTrue(data["ok"])
        self.assertTrue(os.path.isfile(self.output_path))
        with open(self.output_path, encoding="utf-8") as fh:
            body = fh.read()
        self.assertIn("round_type:", body)
        self.assertIn("assessment: pass", body)
        self.assertIn("grounding", body)
        self.assertIn("goal-2", body)
        self.assertIn("verdict", body)

    def test_invalid_review_no_assessment(self):
        self._install_codex(mode="success", content=INVALID_REVIEW)
        proc = _run_cli(
            [
                "--vendor", "gpt",
                "--prompt-file", self.prompt_path,
                "--output", self.output_path,
                "--validate", "review",
            ],
            self.env,
        )
        self.assertEqual(proc.returncode, 3, proc.stdout + proc.stderr)
        data = _parse_json_line(proc.stdout)
        self.assertEqual(data["reason"], "invalid-output")
        self.assertTrue(data["substituted"])
        self.assertFalse(os.path.exists(self.output_path))


class TestValidateSafeclaims(CliLaneTestBase):
    def test_valid_safeclaims(self):
        self._install_codex(mode="success", content=VALID_SAFECLAIMS)
        proc = _run_cli(
            [
                "--vendor", "gpt",
                "--prompt-file", self.prompt_path,
                "--output", self.output_path,
                "--validate", "safeclaims",
            ],
            self.env,
        )
        self.assertEqual(proc.returncode, 0, proc.stderr + proc.stdout)
        data = _parse_json_line(proc.stdout)
        self.assertTrue(data["ok"])
        self.assertTrue(os.path.isfile(self.output_path))
        with open(self.output_path, encoding="utf-8") as fh:
            body = fh.read()
        self.assertIn("check:", body)
        self.assertIn("verdict: SAFE-PASS", body)
        self.assertIn("aitell:", body)

    def test_invalid_safeclaims_missing_aitell(self):
        self._install_codex(mode="success", content=INVALID_SAFECLAIMS)
        proc = _run_cli(
            [
                "--vendor", "gpt",
                "--prompt-file", self.prompt_path,
                "--output", self.output_path,
                "--validate", "safeclaims",
            ],
            self.env,
        )
        self.assertEqual(proc.returncode, 3, proc.stdout + proc.stderr)
        data = _parse_json_line(proc.stdout)
        self.assertEqual(data["reason"], "invalid-output")
        self.assertTrue(data["substituted"])
        self.assertFalse(os.path.exists(self.output_path))


def _run():
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(sys.modules[__name__])
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    total = result.testsRun
    failed = len(result.failures) + len(result.errors)
    print("\n%s" % ("=" * 50))
    print("SUMMARY: %d run, %d passed, %d failed" % (total, total - failed, failed))
    print("%s" % ("=" * 50))
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    sys.exit(_run())
