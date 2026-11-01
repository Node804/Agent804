"""Behavioral regressions for the distributed hook; Git commits exist only in fixtures."""

import json
import os
import shutil
import stat
import subprocess
import sys
import tempfile
import time
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HOOK = ROOT / "templates" / "stop_check.py"


class StopCheckTests(unittest.TestCase):
    def setUp(self):
        # Keep fixtures in the writable checkout, even when the system temp is restricted.
        self.base = Path(tempfile.mkdtemp(prefix="hook-test-", dir=ROOT))
        self.addCleanup(self.cleanup)
        self.repo = self.base / "project with spaces"
        self.repo.mkdir()
        self.env = {key: value for key, value in os.environ.items()
                    if not key.startswith("GIT_") and key not in ("AGENT_CHECK", "CLAUDE_PROJECT_DIR")}
        self.git(self.repo, "init", "--quiet")
        (self.repo / "app.py").write_text("value = 1\n", encoding="utf-8")
        (self.repo / ".gitignore").write_text("check-count\n", encoding="utf-8")
        (self.repo / ".agent-check").write_text(self.command(), encoding="utf-8")

    def cleanup(self):
        def writable(function, path, exc):
            os.chmod(path, stat.S_IWRITE | stat.S_IREAD)
            function(path)
        target = self.base.resolve()
        if target.parent != ROOT.resolve() or not target.name.startswith("hook-test-"):
            raise RuntimeError(f"Refusing fixture cleanup outside the allocated checkout: {target}")
        # Windows scanners can briefly hold a directory after Git has exited.
        for attempt in range(10):
            try:
                shutil.rmtree(target, onerror=writable)
                return
            except PermissionError:
                if attempt == 9:
                    raise
                time.sleep(0.1)

    def git(self, root, *args):
        return subprocess.run(["git", *args], cwd=root, env=self.env,
                              capture_output=True, check=True).stdout

    def commit_fixture(self):
        self.git(self.repo, "add", ".")
        self.git(self.repo, "-c", "user.name=Hook Test", "-c", "user.email=hook@example.invalid",
                 "-c", "commit.gpgsign=false", "-c", "core.hooksPath=", "commit", "--quiet", "-m", "fixture")

    def command(self, status=0):
        code = ("from pathlib import Path; p=Path('check-count'); "
                "p.write_text(str(int(p.read_text())+1) if p.exists() else '1'); "
                f"raise SystemExit({status})")
        return f'"{sys.executable}" -c "{code}"'

    def stop(self, root=None, command=None, active=False, expected=0):
        root = root or self.repo
        env = dict(self.env, CLAUDE_PROJECT_DIR=str(root))
        if command is not None:
            env["AGENT_CHECK"] = command
        result = subprocess.run([sys.executable, str(HOOK)], env=env,
                                input=json.dumps({"cwd": str(root), "stop_hook_active": active}),
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, expected, result.stderr)
        return result

    def count(self, root=None):
        path = (root or self.repo) / "check-count"
        return int(path.read_text()) if path.exists() else 0

    def test_success_is_cached_and_tracked_and_untracked_edits_invalidate(self):
        self.commit_fixture()
        self.stop()
        self.stop()
        self.assertEqual(self.count(), 1)
        (self.repo / "app.py").write_text("value = 2\n")
        self.stop()
        (self.repo / "new.txt").write_text("new")
        self.stop()
        (self.repo / "new.txt").write_text("changed")
        self.stop()
        self.assertEqual(self.count(), 4)

    def test_unborn_staged_edits_always_run(self):
        self.git(self.repo, "add", ".")
        self.stop()
        (self.repo / "app.py").write_text("value = 2\n")
        self.stop()
        self.assertEqual(self.count(), 2)

    def test_environment_command_invalidates_success(self):
        self.commit_fixture()
        self.stop()
        self.stop(command=self.command(1), expected=2)
        self.stop()
        self.assertEqual(self.count(), 3)

    def test_linked_worktree_failure_and_cache_are_independent(self):
        self.commit_fixture()
        other = self.base / "linked tree"
        self.git(self.repo, "worktree", "add", "--quiet", "-b", "other", str(other))
        self.assertTrue((other / ".git").is_file())
        self.stop()
        self.stop(other, command=self.command(1), expected=2)
        self.stop(other)
        self.stop(other)
        self.stop()
        self.assertEqual(self.count(), 1)
        self.assertEqual(self.count(other), 2)
        (other / "app.py").write_text("value = 3\n")
        self.stop(other)
        self.stop()
        self.assertEqual(self.count(other), 3)
        self.assertEqual(self.count(), 1)

    def test_subdirectory_discovers_project_root(self):
        subdir = self.repo / "nested"
        subdir.mkdir()
        self.stop(subdir)
        self.assertEqual(self.count(), 1)

    def test_failure_is_not_cached_and_active_stop_can_report(self):
        self.commit_fixture()
        self.stop(command=self.command(1), expected=2)
        self.stop(command=self.command(1), expected=2)
        self.stop(command=self.command(1), active=True)
        self.assertEqual(self.count(), 2)

    def test_missing_executable_and_missing_command_block(self):
        result = self.stop(command="agent804-nonexistent-check-executable", expected=2)
        self.assertIn("Cannot verify the check", result.stderr)
        (self.repo / ".agent-check").unlink()
        result = self.stop(expected=2)
        self.assertIn("No check command", result.stderr)

    def test_git_failure_blocks(self):
        outside = self.base / "not a repository"
        outside.mkdir()
        (outside / ".git").write_text("gitdir: missing-metadata\n")
        result = self.stop(outside, expected=2)
        self.assertIn("Cannot verify the check", result.stderr)


if __name__ == "__main__":
    unittest.main()
