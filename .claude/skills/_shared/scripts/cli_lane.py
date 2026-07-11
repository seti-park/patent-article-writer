#!/usr/bin/env python3
"""Shared CLI-lane helper for multi-vendor stage workers.

Drives an external vendor CLI (codex for GPT, grok for Grok) with a prompt file
and captures structured output for the orchestrator. Used first by the self_audit
GPT grounding-verifier lane (docs/architecture/multi-vendor-lanes.md §8 P1);
later phases reuse the same entry point for compose/review lanes.

Contract (orchestrator keys on exit codes + one JSON line on stdout):

  exit 0  success  {"ok": true, "vendor": "...", "output": "<path>", "duration_s": N}
  exit 3  substitute  {"ok": false, "substituted": true, "vendor": "...",
                       "reason": "cli-missing|nonzero|timeout|empty-output|invalid-output",
                       "detail": "..."}
  exit 2  usage error (argparse)

  --check  presence-only (shutil.which); no network, no CLI invoke.
  --validate grounding  post-capture shape check (verifier line + verdict token + |---).
  --validate drift  post-capture shape check (verifier line + drift-verdict token + |---).
  --validate pregate  post-capture shape check (pregate line + VOICE-PASS/FAIL verdict).
  --max-turns N  grok runaway-turn guard only (default 16); NOT the isolation mechanism.
  Isolation is tool-less grok: every grok invoke always gets --tools "" --no-subagents
  --disable-web-search (prompts inline everything; no tool use required).
  Grok capture uses constrained --json-schema (document envelope); extract
  structuredOutput.document (fallback: json.loads(text)["document"]).

Stdlib only. Never shell=True — argv lists only.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

VENDOR_CLI = {
    "gpt": "codex",
    "grok": "grok",
}

GROK_DOC_SCHEMA = '{"type":"object","properties":{"document":{"type":"string"}},"required":["document"]}'

VERDICT_TOKENS = (
    "SUPPORTED",
    "MISREAD",
    "OVERREACHED-BEYOND-ANCHOR",
    "UNSUPPORTED",
)

# Drift-mode vocabulary (polish drift check / mode B) — distinct from mode-A above.
DRIFT_VERDICT_TOKENS = (
    "MEANING-PRESERVED",
    "MEANING-CHANGED",
    "PROTECTED-TOUCHED",
)


def _emit(payload: dict) -> None:
    print(json.dumps(payload, ensure_ascii=False), flush=True)


def _substitute(vendor: str, reason: str, detail: str, output_path: str | None) -> int:
    """Emit substitute JSON, remove partial output, exit 3."""
    if output_path:
        try:
            if os.path.exists(output_path):
                os.remove(output_path)
        except OSError:
            pass
    _emit({
        "ok": False,
        "substituted": True,
        "vendor": vendor,
        "reason": reason,
        "detail": detail,
    })
    return 3


def _validate_grounding(text: str) -> str | None:
    """Return None if valid; else a short detail string."""
    has_verifier = any(line.lstrip().startswith("verifier:") for line in text.splitlines())
    has_verdict = any(tok in text for tok in VERDICT_TOKENS)
    has_table_sep = any("|---" in line for line in text.splitlines())
    missing = []
    if not has_verifier:
        missing.append("no line starting with 'verifier:'")
    if not has_verdict:
        missing.append("no verdict token from %s" % (VERDICT_TOKENS,))
    if not has_table_sep:
        missing.append("no markdown table separator (|---)")
    if missing:
        return "; ".join(missing)
    return None


def _validate_compose(text: str) -> str | None:
    """Return None if valid; else a short detail string."""
    has_anchor = re.search(r"\[\d{4}\]", text) is not None
    has_length = len(text.strip()) >= 800
    first_line = ""
    for line in text.splitlines():
        if line.strip():
            first_line = line.strip()
            break
    has_fence = first_line == "---"
    missing = []
    if not has_anchor:
        missing.append("no [dddd] anchor (regex \\[\\d{4}\\])")
    if not has_length:
        missing.append("stripped length < 800 characters")
    if not has_fence:
        missing.append("first non-whitespace line is not exactly '---'")
    if missing:
        return "; ".join(missing)
    return None


def _validate_compose_revision(text: str) -> str | None:
    """Return None if valid; else a short detail string."""
    first_line = ""
    for line in text.splitlines():
        if line.strip():
            first_line = line.strip()
            break
    has_dispositions = first_line.startswith("<!--") and ("DISPOSITIONS" in text)
    has_fence = any(line.strip() == "---" for line in text.splitlines())
    has_anchor = re.search(r"\[\d{4}\]", text) is not None
    has_length = len(text.strip()) >= 800
    missing = []
    if not has_dispositions:
        missing.append(
            "first non-whitespace line does not start with '<!--' or text missing 'DISPOSITIONS'"
        )
    if not has_fence:
        missing.append("no line found that is exactly '---'")
    if not has_anchor:
        missing.append("no [dddd] anchor (regex \\[\\d{4}\\])")
    if not has_length:
        missing.append("stripped length < 800 characters")
    if missing:
        return "; ".join(missing)
    return None


def _validate_promo(text: str) -> str | None:
    """Return None if valid; else a short detail string."""
    has_length = len(text.strip()) >= 600
    has_verification = "Verification Status" in text
    missing = []
    if not has_length:
        missing.append("stripped length < 600 characters")
    if not has_verification:
        missing.append("missing 'Verification Status' substring")
    if missing:
        return "; ".join(missing)
    return None


def _validate_drift(text: str) -> str | None:
    """Return None if valid; else a short detail string."""
    has_verifier = any(line.lstrip().startswith("verifier:") for line in text.splitlines())
    has_verdict = any(tok in text for tok in DRIFT_VERDICT_TOKENS)
    has_table_sep = any("|---" in line for line in text.splitlines())
    missing = []
    if not has_verifier:
        missing.append("no line starting with 'verifier:'")
    if not has_verdict:
        missing.append("no verdict token from %s" % (DRIFT_VERDICT_TOKENS,))
    if not has_table_sep:
        missing.append("no markdown table separator (|---)")
    if missing:
        return "; ".join(missing)
    return None


def _validate_pregate(text: str) -> str | None:
    """Return None if valid; else a short detail string."""
    has_pregate = any(line.lstrip().startswith("pregate:") for line in text.splitlines())
    has_verdict = (
        "verdict: VOICE-PASS" in text or "verdict: VOICE-FAIL" in text
    )
    missing = []
    if not has_pregate:
        missing.append("no line starting with 'pregate:'")
    if not has_verdict:
        missing.append(
            "no 'verdict: VOICE-PASS' or 'verdict: VOICE-FAIL' substring"
        )
    if missing:
        return "; ".join(missing)
    return None


def _cli_missing_detail(vendor: str) -> str:
    return "%s CLI '%s' not found on PATH" % (vendor, VENDOR_CLI[vendor])


def run_check(vendor: str) -> int:
    cli = VENDOR_CLI[vendor]
    if shutil.which(cli):
        _emit({"ok": True, "vendor": vendor, "check": True})
        return 0
    return _substitute(vendor, "cli-missing", _cli_missing_detail(vendor), None)


def _build_gpt_argv(cwd: str, prompt_text: str, last_message_path: str) -> list[str]:
    return [
        "codex", "exec",
        "--skip-git-repo-check",
        "-s", "read-only",
        "-C", cwd,
        "-m", "gpt-5.6-sol",
        "-c", "model_reasoning_effort=high",
        "-o", last_message_path,
        prompt_text,
    ]


def _build_grok_argv(cwd: str, prompt_file: str, max_turns: int) -> list[str]:
    return [
        "grok",
        "--prompt-file", prompt_file,
        "-m", "grok-4.5",
        "--json-schema", GROK_DOC_SCHEMA,
        "--max-turns", str(max_turns),
        "--tools", "",
        "--no-subagents",
        "--disable-web-search",
        "--cwd", cwd,
    ]


def run_lane(
    vendor: str,
    prompt_file: str,
    output_path: str,
    timeout: int,
    cwd: str,
    validate: str | None,
    max_turns: int,
) -> int:
    cwd = os.path.abspath(cwd)
    cli = VENDOR_CLI[vendor]
    if not shutil.which(cli):
        return _substitute(vendor, "cli-missing", _cli_missing_detail(vendor), output_path)

    prompt_path = Path(prompt_file)
    if not prompt_path.is_file():
        return _substitute(
            vendor, "nonzero",
            "prompt file not found: %s" % prompt_file,
            output_path,
        )
    prompt_path = prompt_path.resolve()

    tmp_last = None
    try:
        if vendor == "gpt":
            prompt_text = prompt_path.read_text(encoding="utf-8")
            fd, tmp_last = tempfile.mkstemp(prefix="cli_lane_gpt_", suffix=".txt")
            os.close(fd)
            argv = _build_gpt_argv(cwd, prompt_text, tmp_last)
        else:
            argv = _build_grok_argv(cwd, str(prompt_path), max_turns)

        t0 = time.monotonic()
        try:
            proc = subprocess.run(
                argv,
                capture_output=True,
                text=True,
                timeout=timeout,
                cwd=cwd if vendor == "grok" else None,
                stdin=subprocess.DEVNULL,
            )
        except subprocess.TimeoutExpired as exc:
            detail = "timeout after %ss" % timeout
            if exc.stderr:
                err = exc.stderr if isinstance(exc.stderr, str) else exc.stderr.decode(
                    "utf-8", errors="replace"
                )
                detail = (detail + ": " + err)[-200:]
            return _substitute(vendor, "timeout", detail, output_path)
        duration = time.monotonic() - t0

        if proc.returncode != 0:
            err = (proc.stderr or proc.stdout or "exit %s" % proc.returncode)
            detail = err[-200:] if len(err) > 200 else err
            detail = detail.strip() or "exit %s" % proc.returncode
            return _substitute(vendor, "nonzero", detail, output_path)

        if vendor == "gpt":
            try:
                content = Path(tmp_last).read_text(encoding="utf-8")
            except OSError as exc:
                return _substitute(
                    vendor, "empty-output",
                    "could not read codex -o file: %s" % exc,
                    output_path,
                )
        else:
            try:
                obj = json.loads(proc.stdout)
                doc = (obj.get("structuredOutput") or {}).get("document")
                if doc is None:
                    doc = json.loads(obj["text"])["document"]
                content = doc
            except Exception as exc:
                detail = "grok json envelope parse failed: %s" % repr(exc)
                if len(detail) > 200:
                    detail = detail[:200]
                return _substitute(vendor, "invalid-output", detail, output_path)

        if not content.strip():
            return _substitute(vendor, "empty-output", "captured output empty after strip", output_path)

        if validate == "grounding":
            bad = _validate_grounding(content)
            if bad:
                # Write then remove so the contract (remove partial --output) is uniform;
                # never leave invalid content for the orchestrator to consume.
                try:
                    Path(output_path).write_text(content, encoding="utf-8")
                except OSError:
                    pass
                return _substitute(vendor, "invalid-output", bad, output_path)
        elif validate == "compose":
            bad = _validate_compose(content)
            if bad:
                try:
                    Path(output_path).write_text(content, encoding="utf-8")
                except OSError:
                    pass
                return _substitute(vendor, "invalid-output", bad, output_path)
        elif validate == "compose-revision":
            bad = _validate_compose_revision(content)
            if bad:
                try:
                    Path(output_path).write_text(content, encoding="utf-8")
                except OSError:
                    pass
                return _substitute(vendor, "invalid-output", bad, output_path)
        elif validate == "promo":
            bad = _validate_promo(content)
            if bad:
                try:
                    Path(output_path).write_text(content, encoding="utf-8")
                except OSError:
                    pass
                return _substitute(vendor, "invalid-output", bad, output_path)
        elif validate == "drift":
            bad = _validate_drift(content)
            if bad:
                try:
                    Path(output_path).write_text(content, encoding="utf-8")
                except OSError:
                    pass
                return _substitute(vendor, "invalid-output", bad, output_path)
        elif validate == "pregate":
            bad = _validate_pregate(content)
            if bad:
                try:
                    Path(output_path).write_text(content, encoding="utf-8")
                except OSError:
                    pass
                return _substitute(vendor, "invalid-output", bad, output_path)

        try:
            Path(output_path).parent.mkdir(parents=True, exist_ok=True)
            Path(output_path).write_text(content, encoding="utf-8")
        except OSError as exc:
            return _substitute(
                vendor, "nonzero",
                "failed to write output: %s" % exc,
                output_path,
            )

        _emit({
            "ok": True,
            "vendor": vendor,
            "output": output_path,
            "duration_s": round(duration, 3),
        })
        return 0
    finally:
        if tmp_last:
            try:
                os.remove(tmp_last)
            except OSError:
                pass


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Multi-vendor CLI lane helper (gpt via codex, grok via grok)."
    )
    parser.add_argument(
        "--vendor",
        required=True,
        choices=["gpt", "grok"],
        help="Vendor CLI lane to invoke",
    )
    parser.add_argument("--prompt-file", help="Path to prompt file")
    parser.add_argument("--output", help="Path to write captured CLI output")
    parser.add_argument(
        "--check",
        action="store_true",
        help="Presence-only check (shutil.which); no CLI invoke",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=900,
        help="Subprocess timeout in seconds (default 900)",
    )
    parser.add_argument(
        "--cwd",
        default=None,
        help="Working directory for the vendor CLI (default: current dir)",
    )
    parser.add_argument(
        "--validate",
        choices=["grounding", "compose", "compose-revision", "promo", "drift", "pregate"],
        default=None,
        help="Optional post-capture output validation",
    )
    parser.add_argument(
        "--max-turns",
        type=int,
        default=16,
        help=(
            "Grok runaway-turn guard (default 16); NOT the isolation mechanism — "
            "see --tools/--no-subagents/--disable-web-search, which are always "
            "applied unconditionally"
        ),
    )
    args = parser.parse_args(argv)

    if args.check:
        if args.prompt_file or args.output:
            # --check is exclusive of a real run; allow only --vendor + --check (+ optional noise)
            pass  # still OK — check ignores prompt/output; presence is all
        return run_check(args.vendor)

    if not args.prompt_file or not args.output:
        parser.error("either --check, or both --prompt-file and --output, are required")

    cwd = args.cwd if args.cwd is not None else os.getcwd()
    try:
        return run_lane(
            vendor=args.vendor,
            prompt_file=args.prompt_file,
            output_path=args.output,
            timeout=args.timeout,
            cwd=cwd,
            validate=args.validate,
            max_turns=args.max_turns,
        )
    except Exception as exc:
        detail = repr(exc)
        if len(detail) > 200:
            detail = detail[:200]
        return _substitute(args.vendor, "nonzero", detail, args.output)


if __name__ == "__main__":
    sys.exit(main())
