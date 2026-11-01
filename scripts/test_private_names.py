"""The check fails on private project names and ignores the git-ignored files that hold them."""

import tempfile
import unittest
from pathlib import Path

from check import private_name_hits


class PrivateNamesTest(unittest.TestCase):
    def setUp(self) -> None:
        self.dir = tempfile.TemporaryDirectory()
        self.root = Path(self.dir.name)

    def tearDown(self) -> None:
        self.dir.cleanup()

    def test_name_in_a_page_is_reported_with_its_line(self) -> None:
        (self.root / "page.md").write_text("intro\nTried on Widgetco first.\n", encoding="utf-8")
        hits = private_name_hits(self.root, ["widgetco"])
        self.assertEqual(len(hits), 1)
        self.assertTrue(hits[0].startswith("page.md:2:"))

    def test_whole_words_only(self) -> None:
        (self.root / "page.md").write_text("an area of the code\n", encoding="utf-8")
        self.assertEqual(private_name_hits(self.root, ["rea"]), [])

    def test_local_files_are_skipped(self) -> None:
        (self.root / "HANDOVER.local.md").write_text("Widgetco notes\n", encoding="utf-8")
        (self.root / "private-names.local.md").write_text("Widgetco\n", encoding="utf-8")
        self.assertEqual(private_name_hits(self.root, ["widgetco"]), [])

    def test_no_names_means_no_hits(self) -> None:
        (self.root / "page.md").write_text("anything\n", encoding="utf-8")
        self.assertEqual(private_name_hits(self.root, []), [])


if __name__ == "__main__":
    unittest.main()
