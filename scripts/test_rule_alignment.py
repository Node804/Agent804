"""The check finds rules no skill or template acts on, and gating rules nothing sets up."""

import tempfile
import unittest
from pathlib import Path

from check import cited_ids, gating_ids, rule_alignment_gaps

RULES = "| ID | Rule | Check |\n|---|---|---|\n| WK-1 | One. | x |\n| WK-2 | Two. | x |\n"
RUNGS = "| # | Rung | Prevents | Gating rules | On it when |\n|---|---|---|---|---|\n" \
        "| 1 | First | x | WK-1 | x |\n"


class RuleAlignmentTest(unittest.TestCase):
    def setUp(self) -> None:
        self.dir = tempfile.TemporaryDirectory()
        self.root = Path(self.dir.name)
        (self.root / "framework").mkdir()
        (self.root / "framework" / "rules.md").write_text(RULES, encoding="utf-8")
        (self.root / "framework" / "rungs.md").write_text(RUNGS, encoding="utf-8")

    def tearDown(self) -> None:
        self.dir.cleanup()

    def skill(self, name: str, text: str) -> None:
        folder = self.root / "skills" / name
        folder.mkdir(parents=True)
        (folder / "SKILL.md").write_text(text, encoding="utf-8")

    def test_ranges_are_expanded(self) -> None:
        self.assertEqual(cited_ids("see TS-1 to TS-3"), {"TS-1", "TS-2", "TS-3"})

    def test_gating_ids_come_from_the_rung_table(self) -> None:
        self.assertEqual(gating_ids(RUNGS), {"WK-1"})

    def test_uncited_rules_are_reported(self) -> None:
        gaps = rule_alignment_gaps(self.root)
        self.assertEqual(len(gaps), 2)

    def test_assess_alone_does_not_set_up_a_gating_rule(self) -> None:
        self.skill("assess", "Grade WK-1 and WK-2.\n")
        gaps = rule_alignment_gaps(self.root)
        self.assertEqual(gaps, ["WK-1: gating rule cited by no skill or template that sets it up"])

    def test_a_setup_skill_closes_the_gap(self) -> None:
        self.skill("assess", "Grade WK-2.\n")
        self.skill("start", "Set up WK-1.\n")
        self.assertEqual(rule_alignment_gaps(self.root), [])


if __name__ == "__main__":
    unittest.main()
