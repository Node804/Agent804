"""Acceptance checks for deterministic modeled context sizes, not live token use."""

import json
import math
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from context_load import build_report, measure


ROOT = Path(__file__).resolve().parent.parent


class MeasureTest(unittest.TestCase):
    def setUp(self) -> None:
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)

    def write(self, path: str, text: str) -> None:
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(text.encode("utf-8"))

    def assert_size(self, report: dict, expected: str, path: str) -> None:
        characters = len(expected)
        self.assertEqual(report["characters"], characters)
        self.assertEqual(report["estimated_tokens"], math.ceil(characters / 4))
        self.assertEqual(report["files"], [{
            "path": path,
            "characters": characters,
            "estimated_tokens": math.ceil(characters / 4),
        }])

    def test_whole_file_counts_normalized_unicode_characters(self) -> None:
        self.write("sample.md", "é🙂\r\n123\r\n")
        self.assert_size(measure(self.root, [("sample.md", None)]), "é🙂\n123\n", "sample.md")

    def test_heading_includes_descendants_and_stops_at_peer(self) -> None:
        selected = "## Target\nbody\n### Child\nchild\n#### Deep\ndeep\n"
        self.write("sample.md", "# Title\npreamble\n" + selected + "## Peer\nexcluded\n")
        self.assert_size(measure(self.root, [("sample.md", "Target")]), selected, "sample.md")

    def test_heading_stops_at_higher_level_and_can_reach_eof(self) -> None:
        self.write("sample.md", "# First\n## Target\nbody\n# Second\nlast")
        self.assert_size(measure(self.root, [("sample.md", "Target")]), "## Target\nbody\n", "sample.md")
        self.assert_size(measure(self.root, [("sample.md", "Second")]), "# Second\nlast", "sample.md")

    def test_overlapping_headings_are_counted_once(self) -> None:
        selected = "## Target\nbody\n### Child\nchild\n"
        self.write("sample.md", "# Title\n" + selected + "## Peer\nother\n")
        selections = [("sample.md", "Target"), ("sample.md", "Child"), ("sample.md", "Target")]
        self.assert_size(measure(self.root, selections), selected, "sample.md")

    def test_whole_file_subsumes_selected_section(self) -> None:
        content = "# Title\n## Target\nbody\n"
        self.write("sample.md", content)
        self.assert_size(measure(self.root, [("sample.md", "Target"), ("sample.md", None)]), content, "sample.md")

    def test_identical_text_in_different_files_counts_separately(self) -> None:
        self.write("a.md", "12345")
        self.write("b.md", "12345")
        report = measure(self.root, [("a.md", None), ("b.md", None)])
        self.assertEqual(report["characters"], 10)
        self.assertEqual(report["estimated_tokens"], 3)
        self.assertEqual({entry["path"] for entry in report["files"]}, {"a.md", "b.md"})
        self.assertTrue(all(entry["estimated_tokens"] == 2 for entry in report["files"]))

    def test_rule_selection_retains_interpretive_context(self) -> None:
        preamble = "# Rules\n\nGlobal meaning.\n\n"
        context = "## CK: Checks\n\nSome checks are optional.\n\n| ID | Rule | Check |\n|---|---|---|\n"
        rule = "| CK-1 | One command. | Run it. |\n"
        suffix = "\nFamily qualification.\n\n"
        self.write("framework/rules.md", preamble + "## IN: Instructions\n| IN-1 | Other. | Other. |\n"
                   + context + rule + "| CK-2 | Excluded. | Excluded. |\n" + suffix
                   + "## ST: Style\n| ST-1 | Other. | Other. |\n")
        self.assert_size(measure(self.root, [("framework/rules.md", "rule:CK-1")]),
                         preamble + context + rule + suffix, "framework/rules.md")

    def test_rule_plus_family_deduplicates_preamble_and_rows(self) -> None:
        preamble = "# Rules\nGlobal.\n"
        family = "## CK: Checks\n| ID | Rule | Check |\n|---|---|---|\n| CK-1 | A | B |\n| CK-2 | C | D |\n"
        self.write("framework/rules.md", preamble + family + "## ST: Style\nother\n")
        self.assert_size(measure(self.root, [("framework/rules.md", "rule:CK-1"),
                                            ("framework/rules.md", "CK: Checks")]),
                         preamble + family, "framework/rules.md")

    def test_missing_file_heading_and_rule_fail_loudly(self) -> None:
        self.write("sample.md", "# Present\nbody\n")
        self.write("framework/rules.md", "# Rules\n## CK: Checks\n| CK-1 | A | B |\n")
        for selection in [("missing.md", None), ("sample.md", "Absent"),
                          ("framework/rules.md", "rule:CK-999")]:
            with self.subTest(selection=selection), self.assertRaises((ValueError, FileNotFoundError)):
                measure(self.root, [selection])

    def test_ambiguous_heading_fails_even_when_whole_file_also_selected(self) -> None:
        self.write("sample.md", "# Duplicate\na\n# Duplicate\nb\n")
        with self.assertRaises(ValueError):
            measure(self.root, [("sample.md", None), ("sample.md", "Duplicate")])


class ReportTest(unittest.TestCase):
    def test_scenario_scope_and_host_filtering(self) -> None:
        scenarios = {"small-fix", "check-adoption", "full-assessment", "resumed-planning", "new-project"}
        hosts = {"codex", "claude-code", "grok-build", "chatgpt"}
        for host in sorted(hosts):
            with self.subTest(host=host):
                report = build_report(ROOT, host=host)
                self.assertTrue({"startup", "skills", "workflows", "limits"} <= report.keys())
                self.assertEqual(set(report["workflows"]), scenarios)
                for scenario, workflow in report["workflows"].items():
                    paths = {entry["path"] for entry in workflow["files"]}
                    self.assertTrue(workflow["assumptions"], scenario)
                    self.assertGreater(workflow["characters"], 0)
                    self.assertEqual(workflow["estimated_tokens"], math.ceil(workflow["characters"] / 4))
                    self.assertFalse(paths & {f"framework/agents/{other}.md" for other in hosts - {host}})
                small_paths = {entry["path"] for entry in report["workflows"]["small-fix"]["files"]}
                self.assertIn("skills/spec/SKILL.md", small_paths)
                self.assertFalse(small_paths & {"framework/rules.md", "framework/levels.md", "framework/modules.md"})
                full = report["workflows"]["full-assessment"]
                full_files = {entry["path"]: entry for entry in full["files"]}
                for path in ("framework/rules.md", "framework/levels.md", "framework/modules.md"):
                    self.assertEqual(full_files[path]["characters"], len((ROOT / path).read_text(encoding="utf-8")))
                self.assertIn("framework/agents/README.md", full_files)
                self.assertIn(f"framework/agents/{host}.md", full_files)

    def test_limits_make_estimate_and_omitted_context_explicit(self) -> None:
        limits = build_report(ROOT)["limits"].lower()
        self.assertIsInstance(limits, str)
        for concept in ("estimat", "project", "host", "history", "log"):
            self.assertIn(concept, limits)

    def test_cli_json_and_readable_default(self) -> None:
        command = [sys.executable, str(ROOT / "scripts" / "context_load.py")]
        result = subprocess.run(command + ["--json", "--host", "chatgpt"], cwd=ROOT,
                                capture_output=True, text=True, encoding="utf-8", check=True)
        report = json.loads(result.stdout)
        self.assertEqual(report, build_report(ROOT, host="chatgpt"))
        readable = subprocess.run(command, cwd=ROOT, capture_output=True, text=True,
                                  encoding="utf-8", check=True)
        self.assertIn("small-fix", readable.stdout)
        self.assertIn("full-assessment", readable.stdout)
        self.assertIn("estimat", readable.stdout.lower())


if __name__ == "__main__":
    unittest.main()
