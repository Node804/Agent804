"""Mechanical approval regressions. Synthetic fixtures do not represent human consent."""

import contextlib
import hashlib
import io
import json
import runpy
import shutil
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parent.parent
MODULE = runpy.run_path(str(ROOT / "templates/check_approvals.py"))
VALIDATE = MODULE["validate"]


class ApprovalChecks(unittest.TestCase):
    def setUp(self):
        self.root = Path(tempfile.mkdtemp(prefix="approval-test-", dir=ROOT)).resolve()
        self.addCleanup(self.cleanup)
        self.records = self.root / "docs/approvals"
        self.records.mkdir(parents=True)
        (self.records / "snapshots").mkdir()
        (self.root / "feature.md").write_bytes(b"Reviewed feature\n")
        (self.records / "snapshots/feature.md").write_bytes(b"Reviewed feature\n")
        self.record = json.loads((ROOT / "templates/approval.json").read_text(encoding="utf-8"))
        self.record.update({
            "decision": "approved", "scope": ["Synthetic fixture implementation only"],
            "subjects": [{"path": "feature.md", "snapshot": "docs/approvals/snapshots/feature.md",
                          "sha256": hashlib.sha256(b"Reviewed feature\n").hexdigest()}],
            "reviewer": {"identity": "Synthetic fixture reviewer", "role": "test fixture"},
            "decided_at": "2000-01-01T00:00:00Z",
            "source": {"kind": "other", "reference": "Synthetic test data; no real consent", "evidence": None},
        })
        self.save()

    def cleanup(self):
        if self.root.parent != ROOT.resolve() or not self.root.name.startswith("approval-test-"):
            raise RuntimeError("Unsafe test fixture cleanup target")
        shutil.rmtree(self.root)

    def save(self, record=None):
        record = record or self.record
        (self.records / f"{record['id']}.json").write_text(json.dumps(record), encoding="utf-8")

    def errors(self, required=("APP-0001",)):
        return VALIDATE(self.records, self.root, required)

    def test_current_content_and_unrelated_changes_preserve_mechanical_result(self):
        self.assertEqual(self.errors(), [])
        (self.root / "unrelated.md").write_text("Other work")
        self.assertEqual(self.errors(), [])

    def test_changed_subject_is_stale_but_history_remains_valid(self):
        (self.root / "feature.md").write_text("Changed requirements")
        self.assertTrue(any("subject changed" in item for item in self.errors()))
        self.assertEqual(self.errors(required=()), [])

    def test_snapshot_tampering_is_rejected_even_for_history(self):
        (self.records / "snapshots/feature.md").write_text("Rewritten review")
        self.assertTrue(any("hash does not match" in item for item in self.errors(required=())))

    def test_pending_template_is_valid_history_but_cannot_satisfy_a_gate(self):
        self.record = json.loads((ROOT / "templates/approval.json").read_text(encoding="utf-8"))
        self.save()
        self.assertEqual(self.errors(required=()), [])
        self.assertTrue(any("not approved" in item for item in self.errors()))

    def test_missing_source_and_duplicate_ids_fail(self):
        self.record["source"] = None
        self.save()
        self.assertTrue(any("original-source" in item for item in self.errors()))
        self.setUp_record_source()
        (self.records / "duplicate.json").write_text(json.dumps(self.record))
        self.assertTrue(any("duplicate approval id" in item for item in self.errors()))

    def setUp_record_source(self):
        self.record["source"] = {"kind": "other", "reference": "Synthetic fixture only", "evidence": None}
        self.save()

    def test_revoked_and_superseded_records_cannot_satisfy_a_gate(self):
        other = dict(self.record, id="APP-0002", decision="revoked", revokes=["APP-0001"])
        self.save(other)
        self.assertTrue(any("superseded/revoked" in item for item in self.errors()))
        other.update(decision="approved", revokes=[], supersedes=["APP-0001"])
        self.save(other)
        self.assertTrue(any("superseded/revoked" in item for item in self.errors()))
        self.assertEqual(self.errors(required=("APP-0002",)), [])

    def test_dependencies_are_checked_for_freshness_and_cycles(self):
        other = dict(self.record, id="APP-0002", depends_on=["APP-0001"])
        self.save(other)
        self.assertEqual(self.errors(required=("APP-0002",)), [])
        (self.root / "feature.md").write_text("Changed dependency")
        self.assertTrue(self.errors(required=("APP-0002",)))
        self.record["depends_on"] = ["APP-0002"]
        self.save()
        self.assertTrue(any("cycle" in item for item in self.errors(required=())))

    def test_pending_conditions_expiry_and_risk_expiry_requirement(self):
        self.record["conditions"] = [{"text": "Fixture condition", "status": "pending", "evidence": None}]
        self.save()
        self.assertTrue(any("conditions remain" in item for item in self.errors()))
        self.record.update(conditions=[], expires_at="2001-01-01T00:00:00Z")
        self.save()
        self.assertTrue(any("expired" in item for item in self.errors()))
        self.record.update(kind="risk", expires_at=None)
        self.save()
        self.assertTrue(any("needs expiry" in item for item in self.errors()))

    def test_paths_cannot_escape_or_use_mutable_subject_as_snapshot(self):
        self.record["subjects"][0]["snapshot"] = "../outside.md"
        self.save()
        self.assertTrue(any("escapes" in item for item in self.errors()))
        self.record["subjects"][0]["snapshot"] = "feature.md"
        self.save()
        self.assertTrue(any("outside the subject" in item for item in self.errors()))

    def test_missing_relations_and_current_trace_paths_fail(self):
        self.record["depends_on"] = ["APP-missing"]
        self.save()
        self.assertTrue(any("missing record" in item for item in self.errors()))
        self.record["depends_on"] = []
        self.record["trace"] = [{"requirement": "REQ-1", "criterion": "AC-1",
                                 "tests": ["tests/missing.py::test_case"],
                                 "implementation": ["feature.md"], "evidence": ["feature.md"]}]
        self.save()
        self.assertTrue(any("trace reference missing" in item for item in self.errors()))
        self.assertEqual(self.errors(required=()), [])

    def test_future_decision_cannot_satisfy_a_gate(self):
        self.record["decided_at"] = "2999-01-01T00:00:00Z"
        self.save()
        self.assertTrue(any("future" in item for item in self.errors()))

    def test_cli_success_disclaims_provenance_and_action_authority(self):
        output = io.StringIO()
        args = ["check_approvals.py", "--root", str(self.root), "--records", str(self.records),
                "--require", "APP-0001"]
        with patch("sys.argv", args), contextlib.redirect_stdout(output):
            result = MODULE["main"]()
        self.assertEqual(result, 0)
        self.assertIn("NOT verified", output.getvalue())
        self.assertIn("no action is authorized", output.getvalue())


if __name__ == "__main__":
    unittest.main()
