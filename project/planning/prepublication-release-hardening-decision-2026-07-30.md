# Prepublication Release-Hardening Decision

**Status:** Approved<br>
**Decision authority:** Brad Groux, founding steward<br>
**Decision date:** 2026-07-30<br>
**Effective date:** 2026-07-30<br>
**Scope:** Repository contribution, release verification, ownership,
sensitive-disclosure handling, and publication staging

## Reason

The version 1.0.0 framework package passed extensive manual validation, but the
checks were not yet reproducible by contributors or enforced for later
repository changes. The local development repository also retained review
branches and linked worktrees that must not become part of the public
repository.

The release therefore needed repeatable validation, explicit repository
ownership, a safe route for sensitive disclosures, and a publication source
that cannot accidentally expose development history.

## Decision

The founding steward approves the following repository controls:

1. A contribution or release must pass the repository validation command, or
   explicitly record any unavailable check and its consequence.
2. The GitHub workflow runs the same validation gate for pull requests and
   changes to `main`.
3. Repository ownership remains with the founding steward until governance
   delegates it differently.
4. Sensitive disclosures use the private routes and containment process in
   `SECURITY.md`; public intake must never request sensitive details.
5. Public version 1.0.0 must be staged from an isolated Git repository
   containing only the sanitized `main` baseline and annotated `v1.0.0` tag.
   Review branches, worktrees, unreachable objects, and superseded development
   history are not publication sources.
6. Publication must push explicit approved references. `--all` and `--mirror`
   publication are prohibited.

This decision changes repository contribution and release controls. It does not
change the framework charter, six concerns, eight SOP content requirements, six
maintenance activities, shared operating memory meaning, or any example's
illustrative status.

## Affected Responsibilities

- **Contributors** run the validation command and report unavailable checks.
- **Framework maintainers** review validation evidence, publication safety, and
  affected repository material.
- **Release maintainers** verify the approved version and tag from the isolated
  publication checkout before any external action.
- **The founding steward** owns repository review and private sensitive-report
  intake until those responsibilities are delegated.

## Transition

- These controls apply immediately to the prepared version 1.0.0 release.
- The sanitized one-root commit and annotated tag are rebuilt after the
  controls are integrated and verified.
- The isolated publication checkout is created and validated before the GitHub
  repository is created.
- GitHub-hosted settings, including private vulnerability reporting and branch
  protection, are enabled during the separately authorized publication step.
- Earlier review records remain accurate point-in-time evidence and are not
  rewritten to claim checks that were added later.

## Material Dissent

No material dissent was recorded. The independent standards review identified
the need for this written governance decision before the release baseline was
rebuilt. That review was performed by an AI agent and did not supply human,
professional, organizational, or governance approval.

## Verification Evidence

The repeatable gate is
[`scripts/validate-repository.sh`](../../scripts/validate-repository.sh).
Current release state and remaining external actions are maintained in the
[project status](status.md).
