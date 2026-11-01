"""Actual distributed resources survive a move; a skills-only copy is incomplete."""

import shutil
import tempfile
import unittest
from pathlib import Path

from check_skill_resources import check_resources

ROOT = Path(__file__).resolve().parent.parent


class SkillResourcesTests(unittest.TestCase):
    def test_relocated_intact_kit_resolves(self):
        # No Git metadata or read-only objects; cleanup is limited to this allocated directory.
        with tempfile.TemporaryDirectory(prefix="skill-layout-", dir=ROOT) as directory:
            self.assertEqual(Path(directory).resolve().parent, ROOT.resolve())
            kit = Path(directory) / "original kit"
            for name in ("skills", "framework", "templates"):
                shutil.copytree(ROOT / name, kit / name, ignore=shutil.ignore_patterns("__pycache__"))
            moved = kit.with_name("relocated kit with spaces")
            kit.rename(moved)
            self.assertEqual(check_resources(moved), [])

    def test_skill_folder_without_kit_dependencies_is_rejected(self):
        with tempfile.TemporaryDirectory(prefix="skill-layout-", dir=ROOT) as directory:
            self.assertEqual(Path(directory).resolve().parent, ROOT.resolve())
            kit = Path(directory)
            shutil.copytree(ROOT / "skills" / "assess", kit / "skills" / "assess")
            failures = check_resources(kit)
            self.assertTrue(any("framework" in failure for failure in failures))
            self.assertTrue(any("unavailable resource" in failure for failure in failures))


if __name__ == "__main__":
    unittest.main()
