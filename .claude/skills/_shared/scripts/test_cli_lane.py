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

    def _install_grok(self, mode: str = "success", content: str = GROK_CANNED) -> None:
        if mode == "nonzero":
            body = "#!/bin/bash\nexit 1\n"
        elif mode == "timeout":
            body = "#!/bin/bash\nsleep 5\nexit 0\n"
        elif mode == "empty":
            body = "#!/bin/bash\nprintf '   \\n\\n  '\nexit 0\n"
        else:
            body = (
                "#!/bin/bash\n"
                "cat <<'EOF'\n"
                + content
                + ("\n" if not content.endswith("\n") else "")
                + "EOF\n"
                "exit 0\n"
            )
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
