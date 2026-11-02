"""The check keeps what agents load small: skill budgets, people-only pages, the template."""

import tempfile
import unittest
from pathlib import Path

from check import SKILL_CHARS, agent_read_problems


class AgentReadsTest(unittest.TestCase):
    def setUp(self) -> None:
        self.dir = tempfile.TemporaryDirectory()
        self.root = Path(self.dir.name)

    def tearDown(self) -> None:
        self.dir.cleanup()

    def skill(self, name: str, text: str) -> None:
        folder = self.root / "skills" / name
        folder.mkdir(parents=True)
        (folder / "SKILL.md").write_text(text, encoding="utf-8")

    def test_skill_over_budget_is_reported(self) -> None:
        self.skill("spec", "x" * (SKILL_CHARS + 1))
        self.assertEqual(len(agent_read_problems(self.root)), 1)

    def test_setup_skills_get_a_larger_budget(self) -> None:
        self.skill("assess", "x" * (SKILL_CHARS + 1))
        self.assertEqual(agent_read_problems(self.root), [])

    def test_people_pages_are_refused(self) -> None:
        self.skill("spec", "Read `framework/testing.md` first.\n")
        problems = agent_read_problems(self.root)
        self.assertEqual(len(problems), 1)
        self.assertIn("framework/testing.md", problems[0])

    def test_tables_and_playbooks_are_allowed(self) -> None:
        self.skill(
            "start",
            "framework/levels.md framework/modules.md framework/worktrees.md "
            "framework/profiles/django.md framework/agents/README.md\n",
        )
        self.assertEqual(agent_read_problems(self.root), [])

    def test_template_comments_are_reported(self) -> None:
        (self.root / "templates").mkdir()
        (self.root / "templates" / "AGENTS.md").write_text("# X\n<!-- note -->\n", encoding="utf-8")
        self.assertEqual(len(agent_read_problems(self.root)), 1)


if __name__ == "__main__":
    unittest.main()
