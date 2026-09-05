# Edition validation and release procedure

This is repository operation, not a required business SOP or downstream toolchain.
Content decisions, authority and evidence come first; a passing script supplies
none of them. Use [Governance](../GOVERNANCE.md) and the current decision/review.

## Prepare

1. Verify the current remote, main branch, account and clean or isolated checkout.
   Preserve unrelated work. Use complete Git history for the history secret scan.
2. Audit changed reader decisions against the charter, decisions, canonical
   method, examples, adverse cases and originating request. Record issues and
   disposition, independent content/specification and standards reviews, evidence
   limits and companion teaching consequences. No simultaneous adoption required.
3. Choose actual UTC publication date using `date -u +%Y.%m.%d`. Set `VERSION`
   to YYYY.MM.DD, or the next unused positive numeric same-day suffix. Update
   quoted CFF version/date, README, Governance, changelog, current status and
   `project/releases/v<VERSION>.md`. If publication crosses UTC midnight, revise
   metadata through a PR before tagging. Compatibility is separate from the date.
4. Stage intended public files before checking links; untracked and ignored files
   cannot satisfy a public link. Run:

   ```sh
   scripts/validate-repository.sh
   git diff --check
   ```

   Requires Bash, Git, Python 3, Ruby, curl, tar, Node/npm and a usable Chromium
   browser for Mermaid. The existing gate downloads checksum-verified actionlint
   1.7.12 and Gitleaks 8.30.1 only when absent, uses Mermaid CLI 11.16.0 and
   cffconvert 2.0.0, and scans working tree and full history with redaction.
   It runs the focused regression tests automatically. Record unavailable checks
   honestly. Top-level tool pins do not lock all transitive dependencies; inspect
   the actually resolved npm/Python environments and audit them before release.
   No production dependency or application runtime is present.
5. Review the exact diff and historical preservation. Merge a PR only after the
   required `Documentation, framework, and publication safety` check passes.
   Do not bypass executed failures or remove existing protections/signing rules.
6. Check out the clean merged target, confirm it equals remote main, and rerun
   the repository gate. Diagram compilation is not a visual review: inspect
   rendered output when meaning or layout changed. Unchanged diagrams need no
   new aesthetic redesign. Keep evidence outside the clean release tree.

## Publish

The following commands assume the clean merged target passed the preceding
checks and publication was authorized. The preflight is read-only and checks
account, clean state, remote main, UTC edition, committed VERSION and tag collision.
Existing signing policy remains in effect; `git tag -a` honors configured signing.
If signing is required, use the configured signing mechanism and verify it before
pushing. Do not disable it to get a release through.

```sh
(
set -eu
gh auth status --hostname github.com
test "$(gh api --hostname github.com user --jq .login)" = BradGroux
edition="$(cat VERSION)"
python3 scripts/release.py preflight "$edition"
git tag -a "v$edition" -m "AI-Native Operating Framework v$edition"
git push https://github.com/BradGroux/ai-native-operating-framework.git "refs/tags/v$edition"
gh release create "v$edition" --repo BradGroux/ai-native-operating-framework --verify-tag --title "AI-Native Operating Framework v$edition" --notes-file "project/releases/v$edition.md"
python3 scripts/release.py verify "$edition"
)
```

No uploaded assets are required. The verifier compares local/remote/API annotated
tag objects and peeled commits, VERSION at the tag, release author, final state,
UTC publication date and committed release body. Only CRLF and trailing newlines
are normalized. A branch name in GitHub target_commitish is not proof; the peeled
tag commit is the release identity. Record tag object, commit, PR, checks and
release URL after readback. No credentials or private evidence belong in notes.

## Recovery and historical verification

If preflight, tagging, publication or readback fails, stop and inspect exact
remote state. Never force a tag, delete/recreate a release or relabel history.
A retry after a failed publication may reuse only the identical reviewed tag;
preflight deliberately rejects collisions so recovery requires inspection.
Correct a published error through a new calendar edition and explain its effect.

From a clean checkout with the current scripts and historical tags fetched:

```sh
python3 scripts/release.py verify 1.0.0
python3 scripts/release.py verify 1.1.0
```

These verify existing identities without reinterpreting old citations or requiring
old files to pass new calendar rules. Version 1.0.0 predates a committed release
note, so its body comparison is unavailable; its documented tag republications
remain historical limits. Version 1.1.0 has a committed release note, but inspection on 2026-09-05
confirmed its public body differs (release-date/type summary versus committed
approved-status/effective-date summary). Verification deliberately fails that
body comparison; neither historical text is rewritten. Its tag/commit and author
can still be read back separately. Old metadata records an effective date, which need not equal
the later UTC publication timestamp. Never claim old validators performed checks
that did not exist. Neither historical nor current readback proves field validity.
