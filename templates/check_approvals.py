"""Check portable approval records mechanically; never authenticate or grant human consent.

Copy into an adopting project's scripts/. Default: validate flat docs/approvals/*.json and
preserved snapshot hashes, including historical records. --require ID additionally checks
selected records/dependencies for content freshness, decisions, conditions and expiry.
Success is necessary mechanical evidence only: verify the original human source, authority,
meaning and action scope through the project's trusted review mechanism before acting.
"""

import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path, PureWindowsPath

FIELDS = {"schema_version", "id", "kind", "decision", "subjects", "scope", "reviewer",
          "decided_at", "source", "conditions", "depends_on", "supersedes", "revokes",
          "expires_at", "trace"}
KINDS = {"feature", "spec", "architecture", "implementation", "action", "risk"}
DECISIONS = {"pending", "approved", "changes_requested", "rejected", "revoked"}


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def strings(value):
    return isinstance(value, list) and all(nonempty(item) for item in value)


def timestamp(value):
    if not nonempty(value):
        raise ValueError("timestamp requires an ISO date/time and timezone")
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.utcoffset() is None:
        raise ValueError("timestamp requires a timezone")
    return parsed


def local_path(root, value):
    if not nonempty(value) or "\\" in value:
        raise ValueError("use a nonempty repository-relative path with forward slashes")
    candidate = Path(value)
    if candidate.is_absolute() or PureWindowsPath(value).drive:
        raise ValueError("absolute paths are not portable approval references")
    resolved = (root / candidate).resolve()
    if not resolved.is_relative_to(root):
        raise ValueError("approval reference escapes the project root")
    return resolved


def _validate_header(record):
    if not isinstance(record, dict) or set(record) != FIELDS:
        raise ValueError("record fields must match the version-1 template")
    if type(record["schema_version"]) is not int or record["schema_version"] != 1:
        raise ValueError("unsupported schema_version")
    if not nonempty(record["id"]) or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]*", record["id"]):
        raise ValueError("id must be a stable portable identifier")
    if record["kind"] not in KINDS or record["decision"] not in DECISIONS:
        raise ValueError("unknown kind or decision")
    for key in ("scope", "depends_on", "supersedes", "revokes"):
        if not strings(record[key]) or len(set(record[key])) != len(record[key]):
            raise ValueError(f"{key} must be a list of unique nonempty strings")
    for key in ("subjects", "conditions", "trace"):
        if not isinstance(record[key], list):
            raise ValueError(f"{key} must be a list")


def _validate_reviewer(record):
    decided = record["decision"] != "pending"
    if decided and (not record["subjects"] or not record["scope"]):
        raise ValueError("a decision needs preserved subjects and explicit scope")
    reviewer = record["reviewer"]
    if reviewer is not None:
        if not isinstance(reviewer, dict) or set(reviewer) != {"identity", "role"} or not all(
            nonempty(value) for value in reviewer.values()
        ):
            raise ValueError("reviewer needs identity and authority role; this does not verify them")
    if decided and (reviewer is None or record["source"] is None or record["decided_at"] is None):
        raise ValueError("a decision needs reviewer, original-source reference and decided_at")


def _validate_timing(record):
    if record["decided_at"] is not None:
        timestamp(record["decided_at"])
    if record["expires_at"] is not None:
        expiry = timestamp(record["expires_at"])
        if record["decided_at"] is not None and expiry <= timestamp(record["decided_at"]):
            raise ValueError("expiry must be after the decision")
    if record["kind"] == "risk" and record["decision"] == "approved" and record["expires_at"] is None:
        raise ValueError("risk acceptance needs expiry")


def _validate_source(record, root):
    source = record["source"]
    if source is not None:
        if not isinstance(source, dict) or set(source) != {"kind", "reference", "evidence"}:
            raise ValueError("source needs kind, reference and optional local evidence")
        if source["kind"] not in {"host-review", "conversation", "signed-record", "other"} or not nonempty(source["reference"]):
            raise ValueError("source requires its real kind and original decision locator")
        if source["evidence"] is not None and not local_path(root, source["evidence"]).is_file():
            raise ValueError("preserved source evidence is missing")


def _validate_subjects(record, path, root):
    for subject in record["subjects"]:
        if not isinstance(subject, dict) or set(subject) != {"path", "snapshot", "sha256"}:
            raise ValueError("subject needs path, snapshot and sha256")
        current = local_path(root, subject["path"])
        snapshot = local_path(root, subject["snapshot"])
        if current == snapshot or path.resolve() in (current, snapshot):
            raise ValueError("snapshot and approval record must be outside the subject")
        if not isinstance(subject["sha256"], str) or not re.fullmatch(r"[0-9a-f]{64}", subject["sha256"]):
            raise ValueError("subject sha256 must be 64 lowercase hex characters")
        if not snapshot.is_file() or hashlib.sha256(snapshot.read_bytes()).hexdigest() != subject["sha256"]:
            raise ValueError("preserved subject is missing or its hash does not match")


def _validate_conditions(record):
    for condition in record["conditions"]:
        if not isinstance(condition, dict) or set(condition) != {"text", "status", "evidence"}:
            raise ValueError("condition needs text, status and evidence")
        if not nonempty(condition["text"]) or condition["status"] not in {"pending", "satisfied"}:
            raise ValueError("invalid condition")
        if condition["status"] == "satisfied" and not nonempty(condition["evidence"]):
            raise ValueError("a satisfied condition needs evidence to verify independently")


def _validate_lifecycle(record):
    if record["revokes"] and record["decision"] != "revoked":
        raise ValueError("revokes is only valid on a revocation decision")
    if record["decision"] == "revoked" and not record["revokes"]:
        raise ValueError("a revocation must name earlier decisions")
    if record["supersedes"] and record["decision"] not in {"approved", "changes_requested", "rejected"}:
        raise ValueError("only a completed replacement decision can supersede earlier ones")


def _validate_trace(record, root):
    for row in record["trace"]:
        if not isinstance(row, dict) or set(row) != {"requirement", "criterion", "tests", "implementation", "evidence"}:
            raise ValueError("trace needs requirement, criterion, tests, implementation and evidence")
        if not all(nonempty(row[key]) for key in ("requirement", "criterion")):
            raise ValueError("trace needs stable requirement and criterion IDs")
        for key in ("tests", "implementation", "evidence"):
            if not strings(row[key]) or not row[key]:
                raise ValueError(f"trace {key} needs at least one reference")
            for reference in row[key]:
                local_path(root, reference.split("::", 1)[0])


def validate_record(record, path, root):
    """Check schema and preserved references; source authenticity remains outside this check."""
    _validate_header(record)
    _validate_reviewer(record)
    _validate_timing(record)
    _validate_source(record, root)
    _validate_subjects(record, path, root)
    _validate_conditions(record)
    _validate_lifecycle(record)
    _validate_trace(record, root)


def validate(records_path, root, required=()):
    """Return mechanical errors only; no successful result authenticates human decisions."""
    root = Path(root).resolve()
    records_path = Path(records_path)
    paths = [records_path] if records_path.is_file() else sorted(records_path.glob("*.json"))
    errors, records = [], {}
    if not records_path.exists():
        return [f"Missing approval record location: {records_path}"]
    for path in paths:
        try:
            record = json.loads(path.read_text(encoding="utf-8"))
            validate_record(record, path, root)
            if record["id"] in records:
                raise ValueError("duplicate approval id")
            records[record["id"]] = record
        except (OSError, ValueError, TypeError) as exc:
            errors.append(f"{path.name}: {exc}")
    for key, record in records.items():
        for relation in ("depends_on", "supersedes", "revokes"):
            for target in record[relation]:
                if target == key or target not in records:
                    errors.append(f"{key}: {relation} refers to itself or missing record {target}")
    visiting, visited = set(), set()

    def visit(key):
        if key in visiting:
            errors.append(f"{key}: approval dependency cycle")
            return
        if key in visited or key not in records:
            return
        visiting.add(key)
        for dependency in records[key]["depends_on"]:
            visit(dependency)
        visiting.remove(key)
        visited.add(key)

    for key in records:
        visit(key)
    cancelled = {target for record in records.values()
                 for target in record["supersedes"] + record["revokes"]}
    checked = set()

    def require(key):
        if key in checked:
            return
        checked.add(key)
        if key not in records:
            errors.append(f"{key}: required decision missing")
            return
        record = records[key]
        if record["decision"] != "approved" or key in cancelled:
            errors.append(f"{key}: required decision is not approved, or is superseded/revoked")
        if any(item["status"] != "satisfied" for item in record["conditions"]):
            errors.append(f"{key}: approval conditions remain pending")
        if record["decided_at"] and timestamp(record["decided_at"]) > datetime.now(timezone.utc):
            errors.append(f"{key}: decision time is in the future")
        if record["expires_at"] and timestamp(record["expires_at"]) <= datetime.now(timezone.utc):
            errors.append(f"{key}: approval expired")
        for subject in record["subjects"]:
            path = local_path(root, subject["path"])
            try:
                matches = path.is_file() and hashlib.sha256(path.read_bytes()).hexdigest() == subject["sha256"]
            except OSError:
                matches = False
            if not matches:
                errors.append(f"{key}: subject changed/missing: {subject['path']}; review freshness")
        for row in record["trace"]:
            for field in ("tests", "implementation", "evidence"):
                for reference in row[field]:
                    if not local_path(root, reference.split("::", 1)[0]).is_file():
                        errors.append(f"{key}: current trace reference missing: {reference}")
        for dependency in record["depends_on"]:
            require(dependency)

    for key in required:
        require(key)
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--records", type=Path, default=Path("docs/approvals"))
    parser.add_argument("--require", action="append", default=[])
    args = parser.parse_args()
    errors = validate(args.root / args.records, args.root, args.require)
    for error in errors:
        print(error)
    if errors:
        print("Fix approval-record integrity/freshness; never fabricate or rewrite human consent.")
    else:
        print("Mechanical approval checks passed. Human provenance, authority and action scope are NOT verified; no action is authorized by this result.")
    return int(bool(errors))


if __name__ == "__main__":
    raise SystemExit(main())
