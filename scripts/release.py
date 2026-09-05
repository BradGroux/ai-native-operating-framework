#!/usr/bin/env python3
"""Read-only preflight and published-release verification for this repository."""

from __future__ import annotations

import argparse
from datetime import date, datetime, timezone
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
REPOSITORY = "BradGroux/ai-native-operating-framework"
REMOTE = f"https://github.com/{REPOSITORY}.git"
LEGACY_EDITIONS = {"1.0.0", "1.1.0"}


class ReleaseError(Exception):
    """A release condition could not be verified."""


def run(*command: str) -> str:
    try:
        result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, timeout=60)
    except subprocess.TimeoutExpired as error:
        raise ReleaseError(f"{command[0]} command timed out; no release verification claim is made") from error
    if result.returncode:
        raise ReleaseError(f"{command[0]} command failed (exit {result.returncode}); no release verification claim is made")
    return result.stdout


def api(endpoint: str) -> object:
    return json.loads(run("gh", "api", "--hostname", "github.com", endpoint))


def edition_date(edition: str) -> date | None:
    if edition in LEGACY_EDITIONS:
        return None
    match = re.fullmatch(r"(\d{4})\.(\d{2})\.(\d{2})(?:\.([1-9]\d*))?", edition)
    if not match:
        raise ReleaseError("Expected YYYY.MM.DD with optional positive .N correction, or a recognized legacy edition")
    try:
        return date(*(int(value) for value in match.groups()[:3]))
    except ValueError as error:
        raise ReleaseError("Edition contains an invalid calendar date") from error


def identity() -> None:
    run("gh", "auth", "status", "--hostname", "github.com")
    if api("user").get("login") != "BradGroux":
        raise ReleaseError("Authenticated github.com identity must be exactly BradGroux")


def clean_tree() -> None:
    if run("git", "status", "--porcelain").strip():
        raise ReleaseError("Worktree must be clean, including untracked files")


def remote_refs(*refs: str) -> dict[str, str]:
    lines = run("git", "ls-remote", REMOTE, *refs).splitlines()
    return {name: value for value, name in (line.split() for line in lines)}


def assert_tag_identity(local_object: str, local_commit: str, remote_object: str | None,
                        remote_commit: str | None, api_object: str, api_commit: str) -> None:
    if not remote_object or not remote_commit:
        raise ReleaseError("Remote annotated tag and peeled commit must both exist")
    if not (local_object == remote_object == api_object):
        raise ReleaseError("Local, remote Git, and GitHub tag objects differ")
    if not (local_commit == remote_commit == api_commit):
        raise ReleaseError("Local, remote Git, and GitHub peeled commits differ")


def normalize_body(body: str) -> str:
    """GitHub may normalize line endings or omit the final notes-file newline."""
    return body.replace("\r\n", "\n").rstrip("\n")


def committed_notes(ref: str, edition: str) -> str | None:
    path = f"project/releases/v{edition}.md"
    if not run("git", "ls-tree", "--name-only", ref, "--", path).strip():
        if edition == "1.0.0":
            return None
        raise ReleaseError("Release tag is missing its committed release notes")
    return run("git", "show", f"{ref}:{path}")


def committed_version(ref: str, edition: str) -> None:
    version_present = bool(run("git", "ls-tree", "--name-only", ref, "--", "VERSION").strip())
    if not version_present:
        if edition != "1.0.0":
            raise ReleaseError("Release tag is missing VERSION")
        print("LIMIT: Legacy v1.0.0 has no committed VERSION; no VERSION equality claim is made")
    elif run("git", "show", f"{ref}:VERSION").strip() != edition:
        raise ReleaseError("VERSION at release tag differs from tag edition")


def check_release(release: dict, expected_body: str | None, publication_date: date | None) -> None:
    if release.get("author", {}).get("login") != "BradGroux":
        raise ReleaseError("Release author must be exactly BradGroux")
    if release.get("draft") is not False or release.get("prerelease") is not False:
        raise ReleaseError("Release must be published and neither draft nor prerelease")
    if release.get("performed_via_github_app") is not None:
        raise ReleaseError("Unexpected GitHub App attribution")
    if release.get("assets") != []:
        raise ReleaseError("This documentation release expects no uploaded assets")
    if expected_body is not None and normalize_body(release.get("body") or "") != normalize_body(expected_body):
        raise ReleaseError("Published release body differs from committed release notes")
    if not release.get("published_at"):
        raise ReleaseError("Release has no publication timestamp")
    if publication_date:
        try:
            actual = datetime.fromisoformat(release["published_at"].replace("Z", "+00:00")).astimezone(timezone.utc).date()
        except (TypeError, ValueError) as error:
            raise ReleaseError("Invalid release publication timestamp") from error
        if actual != publication_date:
            raise ReleaseError("Edition date differs from actual UTC publication date")


def preflight(edition: str) -> None:
    publication_date = edition_date(edition)
    if publication_date != datetime.now(timezone.utc).date():
        raise ReleaseError("New editions must use the actual current UTC date")
    identity()
    clean_tree()
    head = run("git", "rev-parse", "HEAD").strip()
    refs = remote_refs("refs/heads/main", f"refs/tags/v{edition}", f"refs/tags/v{edition}^{{}}")
    if refs.get("refs/heads/main") != head:
        raise ReleaseError("Committed HEAD must equal remote main")
    if any(name.startswith("refs/tags/") for name in refs):
        raise ReleaseError("Remote tag already exists; never replace a published tag")
    if run("git", "tag", "--list", f"v{edition}").strip():
        raise ReleaseError("Local tag already exists; inspect it instead of replacing it")
    if run("git", "show", "HEAD:VERSION").strip() != edition:
        raise ReleaseError("Committed VERSION differs from requested edition")
    print(f"PASS: read-only release preflight for v{edition} at {head}")
    print("Full repository validation, independent reviews, required checks and signing policy remain separate gates.")


def verify(edition: str) -> None:
    publication_date = edition_date(edition)
    identity()
    clean_tree()
    tag = f"v{edition}"
    ref = f"refs/tags/{tag}"
    if run("git", "cat-file", "-t", ref).strip() != "tag":
        raise ReleaseError("Local release tag must be annotated")
    local_object = run("git", "rev-parse", ref).strip()
    local_commit = run("git", "rev-parse", f"{ref}^{{commit}}").strip()
    refs = remote_refs(ref, f"{ref}^{{}}")
    api_ref = api(f"repos/{REPOSITORY}/git/ref/tags/{tag}")
    if api_ref.get("object", {}).get("type") != "tag":
        raise ReleaseError("GitHub release tag must be annotated")
    api_object = api_ref["object"]["sha"]
    api_tag = api(f"repos/{REPOSITORY}/git/tags/{api_object}")
    if api_tag.get("object", {}).get("type") != "commit":
        raise ReleaseError("Annotated release tag must point directly to a commit")
    assert_tag_identity(local_object, local_commit, refs.get(ref), refs.get(f"{ref}^{{}}"),
                        api_object, api_tag["object"]["sha"])
    committed_version(ref, edition)
    release = api(f"repos/{REPOSITORY}/releases/tags/{tag}")
    if release.get("tag_name") != tag:
        raise ReleaseError("GitHub release points to an unexpected tag")
    expected_body = committed_notes(ref, edition)
    check_release(release, expected_body, publication_date)
    print(f"PASS: {tag}; annotated object {local_object}; commit {local_commit}")
    print(f"PASS: published release by BradGroux; no uploaded assets; {release['html_url']}")
    if expected_body is None:
        print("LIMIT: Legacy v1.0.0 tag has no committed release note file, so its body was not verified; historical tag identity is checked against current remote state, not every past republication.")
    else:
        print("PASS: published body equals committed release notes (CRLF and trailing newlines normalized)")
    print("Signature policy and historical validation-tool availability are separate checks; this command does not prove either.")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("preflight", "verify"))
    parser.add_argument("edition", help="Edition without the v prefix")
    args = parser.parse_args()
    try:
        if args.mode == "preflight":
            preflight(args.edition)
        else:
            verify(args.edition)
    except (ReleaseError, OSError, json.JSONDecodeError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
