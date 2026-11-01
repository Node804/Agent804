"""Draft native wire/installed-pair regressions; no Grok model invocation."""

import json
import os
import shlex
import subprocess
import sys

import test_stop_check as shared


class GrokStopCheckTests(shared.StopCheckTests):
    def setUp(self):
        super().setUp()
        self.hooks = self.repo / ".grok" / "hooks"
        self.hooks.mkdir(parents=True)
        for name in ("stop_check.py", "grok_stop_check.py"):
            (self.hooks / name).write_bytes((shared.ROOT / "templates" / name).read_bytes())
        with (self.repo / ".gitignore").open("a", encoding="utf-8") as target:
            target.write("__pycache__/\n")

    def invoke(self, event, command=None, root=None):
        env = dict(self.env, GROK_WORKSPACE_ROOT=str(self.base / "wrong-root"),
                   CLAUDE_PROJECT_DIR=str(self.base / "wrong-claude-root"))
        if command is not None:
            env["AGENT_CHECK"] = command
        script = (root or self.repo) / ".grok" / "hooks" / "grok_stop_check.py"
        if not script.exists():
            script = self.hooks / "grok_stop_check.py"
        return subprocess.run([sys.executable, str(script)], env=env, input=json.dumps(event),
                              capture_output=True, text=True)

    def stop(self, root=None, command=None, active=False, expected=0):
        root = root or self.repo
        result = self.invoke({"hookEventName": "stop", "cwd": str(root),
                              "stopHookActive": active}, command, root)
        self.assertEqual(result.returncode, expected, result.stderr)
        self.assertEqual(result.stdout, "")
        return result

    def test_invalid_or_foreign_events_request_continuation(self):
        for event in ([], {}, {"hookEventName": "stop"},
                      {"hookEventName": "stop", "cwd": str(self.repo), "stopHookActive": "false"},
                      {"hookEventName": "stop", "cwd": str(self.repo), "stop_hook_active": True}):
            with self.subTest(event=event):
                result = self.invoke(event)
                self.assertEqual(result.returncode, 2)
                self.assertIn("Cannot verify", result.stderr)

    def test_camel_case_reporting_escape_runs_no_new_check(self):
        self.stop(command=self.command(1), expected=2)
        result = self.stop(active=True)
        self.assertIn("not a passing check", result.stderr)
        self.assertEqual(self.count(), 1)

    def test_missing_shared_engine_requests_continuation(self):
        (self.hooks / "stop_check.py").unlink()
        result = self.stop(expected=2)
        self.assertIn("Cannot verify", result.stderr)

    def test_malformed_json_requests_continuation(self):
        result = subprocess.run([sys.executable, str(self.hooks / "grok_stop_check.py")],
                                env=self.env, input="{", capture_output=True, text=True)
        self.assertEqual(result.returncode, 2)
        self.assertIn("Cannot verify", result.stderr)

    def test_rendered_hook_command_from_subdirectory(self):
        config = json.loads((shared.ROOT / "templates" / "grok-hooks.json").read_text())
        command = config["hooks"]["Stop"][0]["hooks"][0]["command"]
        command = command.replace("/ABSOLUTE/CHECKOUT", self.repo.as_posix())
        command = f'"{sys.executable}" ' + command.partition(" ")[2]
        nested = self.repo / "nested"
        nested.mkdir()
        result = subprocess.run(command if os.name == "nt" else shlex.split(command),
                                cwd=nested, env=self.env, capture_output=True, text=True,
                                input=json.dumps({"hookEventName": "stop", "cwd": str(nested)}))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout, "")
        self.assertEqual(self.count(), 1)


if __name__ == "__main__":
    import unittest
    unittest.main()
