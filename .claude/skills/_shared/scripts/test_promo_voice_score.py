#!/usr/bin/env python3
"""Stdlib unittest suite for promo_voice_score.py (KR + EN mechanical modes).

No network. Invokes the scorer as a subprocess against canned fixtures.
Run with:

    python test_promo_voice_score.py

Exits nonzero if any test fails.
"""

from __future__ import annotations

import os
import re
import subprocess
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPT = os.path.join(HERE, "promo_voice_score.py")

# Case 1 — KR calibration: expect exactly 8.0/8
KR_PASS = """\
흥미롭게도 이번 출원(US 2026/0196678 A1)은 탭을 없앤 대신 접는 방식을 택했다. 우선 적층체 최외각부의 집전 포일을 분리막과 함께 감고, 그 접힌 가장자리를 컬렉터(collector)에 그대로 붙인다.

방법은 두 가지로 나뉜다. 첫 번째는 기존처럼 탭(tab)을 용접하는 방식이고, 두 번째는 포일 가장자리를 접어 그 자체를 단자(terminal)로 쓰는 방식이다. 나아가 세 가지 장비, 즉 슬리팅과 노칭과 플래그 삽입 장비가 이 구조에서는 필요하지 않을 수 있다고 문서는 말한다.

또한 저항이 개선될 수 있고 굽힘 강성도 함께 좋아질 수 있다고 적혀 있다. 짧다.

전극 필름과 양극, 음극 구조 모두에 같은 접기 방식이 적용될 수 있다. [ARTICLE-LINK]
"""

# Case 2 — EN calibration: expect exactly 6.0/6
EN_PASS = """\
[Post 1]
Every sealed battery module faces the same problem: heat generated at the core has to reach the case wall efficiently, or the pack degrades faster than the warranty allows.

[Post 2]
The filing describes a wound busbar that threads directly through the can's center, carrying current out through a hemmed collar instead of a welded tab. The collar folds flush against the foil, and the fold itself becomes the electrical and mechanical joint. No tab is welded on.

[Post 3]
The document lists slitting, notching, and flag-interleaving equipment as machines a hemmed line may not require. It also states that internal resistance can improve and that structural integrity under bending loads can increase, mirroring the same tradeoff Tesla described for tabless cells at Battery Day 2020.

[Post 4]
Whether this becomes the next production step is outside the document. US 2027/1234567 A1 is a pending application, filed 3 March 2026 and published 12 July 2026. What the claims actually require versus what the description merely illustrates is in the article. [ARTICLE-LINK]
"""

# Case 3 — EN failure: status clause in post 1 → EN-M5=0, EN-M3=0
EN_STATUS_IN_P1 = """\
[Post 1]
This remains a pending application, so nothing here is granted yet. Every sealed battery module faces the same problem: heat generated at the core has to reach the case wall efficiently, or the pack degrades faster than the warranty allows.

[Post 2]
The filing describes a wound busbar that threads directly through the can's center, carrying current out through a hemmed collar instead of a welded tab. The collar folds flush against the foil, and the fold itself becomes the electrical and mechanical joint. No tab is welded on.

[Post 3]
The document lists slitting, notching, and flag-interleaving equipment as machines a hemmed line may not require. It also states that internal resistance can improve and that structural integrity under bending loads can increase, mirroring the same tradeoff Tesla described for tabless cells at Battery Day 2020.

[Post 4]
Whether this becomes the next production step is outside the document. US 2027/1234567 A1 is a pending application, filed 3 March 2026 and published 12 July 2026. What the claims actually require versus what the description merely illustrates is in the article. [ARTICLE-LINK]
"""

# Case 4 — KR failure: no English glosses → C2=0.0, subtotal 7.0/8
KR_NO_GLOSS = """\
흥미롭게도 이번 출원 US 2026/0196678 A1 은 탭을 없앤 대신 접는 방식을 택했다. 우선 적층체 최외각부의 집전 포일을 분리막과 함께 감고, 그 접힌 가장자리를 컬렉터에 그대로 붙인다.

방법은 두 가지로 나뉜다. 첫 번째는 기존처럼 탭을 용접하는 방식이고, 두 번째는 포일 가장자리를 접어 그 자체를 단자로 쓰는 방식이다. 나아가 세 가지 장비, 즉 슬리팅과 노칭과 플래그 삽입 장비가 이 구조에서는 필요하지 않을 수 있다고 문서는 말한다.

또한 저항이 개선될 수 있고 굽힘 강성도 함께 좋아질 수 있다고 적혀 있다. 짧다.

전극 필름과 양극, 음극 구조 모두에 같은 접기 방식이 적용될 수 있다. [ARTICLE-LINK]
"""

_ITEM_RE = re.compile(r"^([A-Za-z0-9\-]+)\s*\|\s*([0-9.]+)\s*\|")
_SUBTOTAL_RE = re.compile(r"^MECH_SUBTOTAL:\s*([0-9.]+)/([0-9]+)\s*$")


def _run_scorer(fixture_text, en=False):
    """Write fixture to a temp file, run promo_voice_score.py, parse stdout.

    Returns (scores_dict, subtotal_float, denom_int, raw_stdout).
    """
    with tempfile.NamedTemporaryFile(
        mode="w", encoding="utf-8", suffix=".md", delete=False
    ) as fh:
        fh.write(fixture_text)
        path = fh.name
    try:
        argv = [sys.executable, SCRIPT]
        if en:
            argv.append("--en")
        argv.append(path)
        proc = subprocess.run(
            argv,
            capture_output=True,
            text=True,
            check=False,
        )
        out = proc.stdout
        if proc.returncode != 0:
            raise AssertionError(
                "scorer exited %s\nstdout:\n%s\nstderr:\n%s"
                % (proc.returncode, out, proc.stderr)
            )
        scores = {}
        subtotal = None
        denom = None
        for line in out.splitlines():
            m = _ITEM_RE.match(line)
            if m:
                scores[m.group(1)] = float(m.group(2))
                continue
            m = _SUBTOTAL_RE.match(line)
            if m:
                subtotal = float(m.group(1))
                denom = int(m.group(2))
        return scores, subtotal, denom, out
    finally:
        try:
            os.unlink(path)
        except OSError:
            pass


class TestPromoVoiceScore(unittest.TestCase):
    def test_kr_calibration_full_score(self):
        scores, subtotal, denom, out = _run_scorer(KR_PASS, en=False)
        self.assertEqual(denom, 8, out)
        self.assertEqual(subtotal, 8.0, out)
        expected = {
            "A4p": 1.0,
            "B2": 1.0,
            "B3": 1.0,
            "B4": 1.0,
            "C1": 1.0,
            "C2": 1.0,
            "C4": 1.0,
            "E1": 1.0,
        }
        for name, val in expected.items():
            self.assertIn(name, scores, out)
            self.assertEqual(scores[name], val, "%s: %s\n%s" % (name, scores.get(name), out))
        self.assertIn("MECH_SUBTOTAL: 8.0/8", out)

    def test_en_calibration_full_score(self):
        scores, subtotal, denom, out = _run_scorer(EN_PASS, en=True)
        self.assertEqual(denom, 6, out)
        self.assertEqual(subtotal, 6.0, out)
        for name in ("EN-M1", "EN-M2", "EN-M3", "EN-M4", "EN-M5", "EN-M6"):
            self.assertIn(name, scores, out)
            self.assertEqual(scores[name], 1.0, "%s: %s\n%s" % (name, scores.get(name), out))
        self.assertIn("MECH_SUBTOTAL: 6.0/6", out)

    def test_en_status_in_post1_fails_m3_m5(self):
        scores, subtotal, denom, out = _run_scorer(EN_STATUS_IN_P1, en=True)
        self.assertEqual(denom, 6, out)
        self.assertEqual(scores["EN-M1"], 1.0, out)
        self.assertEqual(scores["EN-M2"], 1.0, out)
        self.assertEqual(scores["EN-M3"], 0.0, out)
        self.assertEqual(scores["EN-M4"], 1.0, out)
        self.assertEqual(scores["EN-M5"], 0.0, out)
        self.assertEqual(scores["EN-M6"], 1.0, out)
        self.assertEqual(subtotal, 4.0, out)

    def test_kr_no_glosses_c2_zero(self):
        scores, subtotal, denom, out = _run_scorer(KR_NO_GLOSS, en=False)
        self.assertEqual(denom, 8, out)
        self.assertEqual(scores["C2"], 0.0, out)
        self.assertEqual(scores["C4"], 1.0, out)
        self.assertEqual(subtotal, 7.0, out)
        self.assertIn("MECH_SUBTOTAL: 7.0/8", out)


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
