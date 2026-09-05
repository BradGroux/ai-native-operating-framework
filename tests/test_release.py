"""Regression coverage for read-only release identity and preflight checks."""

import importlib.util
from datetime import date, datetime, timezone
from pathlib import Path
import unittest
from unittest.mock import patch

SPEC = importlib.util.spec_from_file_location("release", Path(__file__).resolve().parents[1] / "scripts/release.py")
release = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(release)


class ReleaseTests(unittest.TestCase):
    def test_calendar_and_preserved_legacy_editions(self):
        self.assertEqual(release.edition_date("2026.09.05.2"), date(2026, 9, 5))
        self.assertIsNone(release.edition_date("1.0.0"))
        self.assertIsNone(release.edition_date("1.1.0"))
        for value in ("2026.02.30", "2026.9.05", "2026.09.05.0", "2026.09.05.01", "1.2.0", "v2026.09.05"):
            with self.subTest(value=value), self.assertRaises(release.ReleaseError):
                release.edition_date(value)

    def test_tag_objects_and_peeled_commit_must_all_match(self):
        release.assert_tag_identity("object", "commit", "object", "commit", "object", "commit")
        for values in (("object", "commit", "moved", "commit", "object", "commit"),
                       ("object", "commit", "object", None, "object", "commit"),
                       ("object", "commit", "object", "commit", "object", "other")):
            with self.subTest(values=values), self.assertRaises(release.ReleaseError):
                release.assert_tag_identity(*values)

    def test_final_release_and_exact_body(self):
        record = {"author": {"login": "BradGroux"}, "draft": False, "prerelease": False,
                  "assets": [], "body": "Exact notes\n", "published_at": "2026-09-05T00:05:00Z"}
        release.check_release(record, "Exact notes\n", date(2026, 9, 5))
        for changed in ({"body": "Altered notes"}, {"draft": True}, {"prerelease": True},
                        {"author": {"login": "another-account"}}, {"assets": [{"name": "unexpected"}]},
                        {"performed_via_github_app": {"name": "unexpected"}},
                        {"published_at": "2026-09-06T00:01:00Z"}):
            with self.subTest(changed=changed), self.assertRaises(release.ReleaseError):
                release.check_release(record | changed, "Exact notes\n", date(2026, 9, 5))

    def test_preflight_rejects_dirty_or_non_main_target_and_collision(self):
        edition = datetime.now(timezone.utc).strftime("%Y.%m.%d")
        def git(*args):
            if args == ("git", "status", "--porcelain"):
                return ""
            if args == ("git", "rev-parse", "HEAD"):
                return "head\n"
            if args == ("git", "tag", "--list", f"v{edition}"):
                return ""
            if args == ("git", "show", "HEAD:VERSION"):
                return edition
            self.fail(f"Unexpected command {args}")
        with patch.object(release, "identity"), patch.object(release, "run", side_effect=git):
            for refs in ({"refs/heads/main": "other"},
                         {"refs/heads/main": "head", f"refs/tags/v{edition}": "exists"}):
                with patch.object(release, "remote_refs", return_value=refs), self.assertRaises(release.ReleaseError):
                    release.preflight(edition)
        with patch.object(release, "run", return_value="?? unpublished.md\n"), self.assertRaises(release.ReleaseError):
            release.clean_tree()

    def test_committed_current_and_legacy_notes(self):
        for edition in ("2026.09.05", "1.1.0"):
            path = f"project/releases/v{edition}.md"
            with patch.object(release, "run", side_effect=[path, "Committed notes\n"]) as command:
                self.assertEqual(release.committed_notes(f"refs/tags/v{edition}", edition), "Committed notes\n")
                self.assertEqual(command.call_args.args, ("git", "show", f"refs/tags/v{edition}:{path}"))
            with patch.object(release, "run", return_value=""), self.assertRaises(release.ReleaseError):
                release.committed_notes(f"refs/tags/v{edition}", edition)
        with patch.object(release, "run", return_value=""):
            self.assertIsNone(release.committed_notes("refs/tags/v1.0.0", "1.0.0"))

    def test_legacy_missing_version_is_narrowly_disclosed(self):
        with patch.object(release, "run", return_value=""), patch("builtins.print") as output:
            release.committed_version("refs/tags/v1.0.0", "1.0.0")
            self.assertIn("LIMIT", output.call_args.args[0])
        for edition in ("1.1.0", "2026.09.05"):
            with patch.object(release, "run", return_value=""), self.assertRaises(release.ReleaseError):
                release.committed_version(f"refs/tags/v{edition}", edition)
        with patch.object(release, "run", side_effect=["VERSION", "other"]), self.assertRaises(release.ReleaseError):
            release.committed_version("refs/tags/v1.0.0", "1.0.0")

    def test_only_line_ending_and_trailing_newlines_normalize(self):
        self.assertEqual(release.normalize_body("First\r\nSecond\r\n"), release.normalize_body("First\nSecond"))
        self.assertNotEqual(release.normalize_body("First \nSecond"), release.normalize_body("First\nSecond"))

    def test_identity_fails_closed(self):
        with patch.object(release, "run", return_value=""), patch.object(release, "api", return_value={"login": "dm-bradgroux"}), self.assertRaises(release.ReleaseError):
            release.identity()


if __name__ == "__main__":
    unittest.main()
