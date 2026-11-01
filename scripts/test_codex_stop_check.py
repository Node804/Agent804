"""Wire-protocol and shared engine regressions; not a live Codex host trial."""

import json
import os
import shlex
import subprocess
import sys

import test_stop_check as shared


class CodexStopCheckTests(shared.StopCheckTests):
    # Inherit the eight real Git/worktree/cache failure scenarios through the Codex adapter.
    def setUp(self):
        super().setUp()
        self.hooks = self.repo / ".codex" / "hooks"
        self.hooks.mkdir(parents=True)
        for name in ("stop_check.py", "codex_stop_check.py"):
            (self.hooks / name).write_bytes((shared.ROOT / "templates" / name).read_bytes())
        with (self.repo / ".gitignore").open("a", encoding="utf-8") as target:
            target.write("__pycache__/\n")

    def invoke(self, event, command=None, root=None):
        env = dict(self.env, CLAUDE_PROJECT_DIR=str(self.base / "wrong-claude-root"))
        if command is not None:
            env["AGENT_CHECK"] = command
        # Linked worktrees receive the committed hook pair; use their actual installed copy.
        script = (root or self.repo) / ".codex" / "hooks" / "codex_stop_check.py"
        if not script.exists():
            script = self.hooks / "codex_stop_check.py"
        return subprocess.run([sys.executable, str(script)], env=env,
                              input=json.dumps(event), capture_output=True, text=True)

    def stop(self, root=None, command=None, active=False, expected=0):
        root = root or self.repo
        result = self.invoke({"cwd": str(root), "hook_event_name": "Stop",
                              "stop_hook_active": active}, command, root)
        self.assertEqual(result.returncode, expected, result.stderr)
        if expected == 0:
            self.assertIsInstance(json.loads(result.stdout), dict)
        return result

    def test_invalid_events_request_continuation(self):
        for event in ([], {}, {"hook_event_name": "Stop"},
                      {"hook_event_name": "Stop", "cwd": str(self.repo),
                       "stop_hook_active": "false"}):
            with self.subTest(event=event):
                result = self.invoke(event)
                self.assertEqual(result.returncode, 2)
                self.assertIn("Cannot verify", result.stderr)

    def test_continuation_reports_no_new_success(self):
        self.stop(command=self.command(1), expected=2)
        result = self.stop(active=True)
        self.assertIn("not a passing check", json.loads(result.stdout)["systemMessage"])
        self.assertEqual(self.count(), 1)

    def test_missing_shared_engine_requests_continuation(self):
        (self.hooks / "stop_check.py").unlink()
        result = self.stop(expected=2)
        self.assertIn("Cannot verify", result.stderr)

    def test_rendered_config_runs_installed_pair_from_subdirectory(self):
        config = json.loads((shared.ROOT / "templates" / "codex-hooks.json").read_text())
        handler = config["hooks"]["Stop"][0]["hooks"][0]
        command = handler["commandWindows"] if os.name == "nt" else handler["command"]
        placeholder = "C:/ABSOLUTE/CHECKOUT" if os.name == "nt" else "/ABSOLUTE/CHECKOUT"
        command = command.replace(placeholder, self.repo.as_posix())
        # Choose the actual fixture interpreter, as the adoption recipe requires.
        command = f'"{sys.executable}" ' + command.partition(" ")[2]
        nested = self.repo / "nested"
        nested.mkdir()
        result = subprocess.run(command if os.name == "nt" else shlex.split(command),
                                cwd=nested, env=self.env, capture_output=True, text=True,
                                input=json.dumps({"hook_event_name": "Stop", "cwd": str(nested)}))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout), {})
        self.assertEqual(self.count(), 1)

    def test_malformed_json_requests_continuation(self):
        result = subprocess.run([sys.executable, str(self.hooks / "codex_stop_check.py")],
                                env=self.env, input="{", capture_output=True, text=True)
        self.assertEqual(result.returncode, 2)
        self.assertIn("Cannot verify", result.stderr)


if __name__ == "__main__":
    import unittest
    unittest.main()
