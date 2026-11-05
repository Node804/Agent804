"""Preserve core membership and keep opt-in completion automation outside it in 0.6."""

import unittest
from collections import Counter
from pathlib import Path

import check
from check import gating_ids


EXPECTED_GATES = {
    1: {
        "IN-1", "IN-3", "CK-2", "CK-1", "ST-1", "MT-2", "SE-2",
        "TS-10", "TS-12",
    },
    2: {
        "GR-1", "GR-2", "GR-3", "GR-4", "GR-7", "SE-3", "SK-1",
        "SK-2", "CK-8", "RV-1", "MT-1",
    },
    3: {
        "TS-1", "TS-2", "TS-3", "TS-4", "TS-8", "TS-9", "AR-1",
        "AR-2", "AR-3", "AR-4", "AR-6", "CK-4", "MT-3", "DC-1",
        "DC-2", "DC-3",
    },
    4: {"MS-1", "MS-2"},
}

EXPECTED_PRACTICES = [
    ("Instructions in the repository", 1, {"IN-1", "IN-3", "CK-2"}),
    ("One check command", 1, {"CK-1", "ST-1", "MT-2", "SE-2", "TS-10", "TS-12"}),
    ("Guardrails", 2, {"GR-1", "GR-2", "GR-3", "GR-4", "GR-7", "SE-3"}),
    ("Walking skeleton and CI", 2, {"SK-1", "SK-2", "CK-8", "RV-1", "MT-1"}),
    ("Tests before code", 3, {"TS-1", "TS-2", "TS-3", "TS-4", "TS-8", "TS-9"}),
    ("Architecture and maintainability as checks", 3,
     {"AR-1", "AR-2", "AR-3", "AR-4", "AR-6", "CK-4", "MT-3"}),
    ("Decisions with evidence", 3, {"DC-1", "DC-2", "DC-3"}),
    ("Measure and garden", 4, {"MS-1", "MS-2"}),
]


class LevelGatesTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = (Path(__file__).resolve().parent.parent / "framework" / "levels.md").read_text(
            encoding="utf-8"
        )

    def test_each_core_level_is_defined_once(self) -> None:
        levels = []
        in_overview = False
        for line in self.text.splitlines():
            cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
            if cells == ["#", "Level", "Prevents", "At it when"]:
                in_overview = True
            elif in_overview and len(cells) == 4 and cells[0].isdigit():
                levels.append(int(cells[0]))
            elif in_overview and not line.startswith("|"):
                in_overview = False
        self.assertEqual(levels, [1, 2, 3, 4])

    def test_practices_preserve_exact_membership_and_introduction_level(self) -> None:
        rows = check.practice_gates(self.text)
        self.assertEqual(len(rows), len(EXPECTED_PRACTICES))
        self.assertCountEqual(rows, EXPECTED_PRACTICES)

    def test_gate_groups_preserve_existing_protections(self) -> None:
        # Includes conditional gates AR-2, AR-4 and TS-9. Applicability remains
        # a judgement from the rule and evidence, not a blanket removal here.
        # Exact membership also prevents module and trial rules becoming core gates.
        by_level = {level: set() for level in EXPECTED_GATES}
        for _, level, gates in check.practice_gates(self.text):
            by_level[level].update(gates)
        self.assertEqual(by_level, EXPECTED_GATES)

    def test_every_core_gate_belongs_to_exactly_one_practice(self) -> None:
        counts = Counter(gate for _, _, gates in check.practice_gates(self.text) for gate in gates)
        expected = Counter({gate: 1 for gates in EXPECTED_GATES.values() for gate in gates})
        self.assertEqual(counts, expected)

    def test_alignment_check_extracts_every_core_gate(self) -> None:
        self.assertEqual(gating_ids(self.text), set().union(*EXPECTED_GATES.values()))

    def test_completion_automation_is_trial_and_separate_from_core(self) -> None:
        modules = (Path(__file__).resolve().parent.parent / "framework" / "modules.md").read_text(
            encoding="utf-8"
        )
        trial_rules = set()
        memberships = Counter()
        for line in modules.splitlines():
            if not line.startswith("|"):
                continue
            cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
            if len(cells) == 4 and cells[-1] in ("Trial", "Scored", "Scored, levels O1 to O3"):
                rules = check.cited_ids(cells[2])
                memberships.update(rules)
                if cells[-1] == "Trial":
                    trial_rules.update(rules)
        core = gating_ids(self.text)
        self.assertIn("GR-4", core)
        self.assertIn("GR-8", trial_rules)
        self.assertEqual(memberships["GR-8"], 1)
        self.assertTrue(trial_rules.isdisjoint(core))

    def test_extractors_ignore_overview_prose_and_unrelated_tables(self) -> None:
        text = """Prose cites OP-1 and AR-5, neither of which is a core gate.

| # | Level | Prevents | At it when |
|---|---|---|---|
| 1 | First | OP-2 | SE-1 |

| Practice | Introduced at | Gating rules |
|---|---|---|
| Sample checks | Level 2 | GR-1 to GR-3; AR-2 where applicable |
| Later checks | Level 4 | MS-1, MS-2 |

Non-gating discussion mentions TS-9.

| # | Topic | Detail | References | Note |
|---|---|---|---|---|
| 3 | Other | x | OP-3 | x |

| Practice | Notes | References |
|---|---|---|
| Other practice | Level 1 | CK-4 |
"""
        expected = [
            ("Sample checks", 2, {"GR-1", "GR-2", "GR-3", "AR-2"}),
            ("Later checks", 4, {"MS-1", "MS-2"}),
        ]
        self.assertEqual(check.practice_gates(text), expected)
        self.assertEqual(gating_ids(text), set().union(*(gates for _, _, gates in expected)))


if __name__ == "__main__":
    unittest.main()
