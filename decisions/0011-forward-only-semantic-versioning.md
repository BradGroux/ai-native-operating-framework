# ADR-011 — Forward-Only Semantic Versioning

- **Status:** accepted
- **Date:** 2026-08-22
- **Owner:** Brad Groux

## Question

Should a published AI-Native Operating Framework tag ever move again, or should
all future release changes use a new semantic version?

## Context and Evidence

The annotated `v1.0.0` tag moved during controlled documentation
republications. ADR-010 required explicit authority, full validation, lease
protection, preserved history, and release readback, but consumers that cached
an earlier tag object could still receive surprising results.

Issue 18 correctly identifies that an immutable historical tag gives consumers
a clearer and more reliable release identity. Version 1.1.0 is the first normal
forward release after the bounded v1.0.0 republications and provides a clean
point at which to end the exception.

## Alternatives Considered

### Continue bounded same-version republication

This would preserve the distinction between semantic meaning and presentation,
but it would retain the cache and release-identity risk.

### Allow tag movement only for emergencies

This narrows the risk but leaves "emergency" open to interpretation and still
makes a published reference mutable.

### Require a new version for every published release change

This makes every published tag immutable and uses semantic-version scope to
communicate the consequence of a change.

## Decision

Beginning with version 1.1.0, release versioning is forward-only. A published
annotated tag is immutable. Any later public release change receives a new
semantic version:

- a patch for backward-compatible editorial, presentation, validation, or
  metadata corrections;
- a minor version for backward-compatible additions or changes to governance,
  adopted ecosystem context, release scope, or framework capability; and
- a major version for incompatible framework meaning or requirements.

The steward still decides the appropriate version and records the rationale.
Branch updates do not create a release, and correcting an unpublished candidate
does not require a version change.

ADR-010 remains accepted historical evidence for the v1.0.0 republications but
is superseded by this decision for every release beginning with v1.1.0.

## Consequences

- The current `v1.0.0` tag and its republication history remain unchanged.
- Version 1.1.0 receives a new annotated tag instead of moving v1.0.0.
- Consumers can treat every tag from v1.1.0 forward as an immutable release
  identity.
- Even a documentation-only published correction now requires a patch release.

## Dissent and Uncertainty

No dissent is recorded. Patch releases may increase the visible version count,
but that cost is lower than ambiguity about the content identified by a tag.

This decision does not establish field validation, certification,
professional review, or real-world effectiveness.

## Affected Artifacts

- `GOVERNANCE.md`
- `CHANGELOG.md`
- `decisions/README.md`
- future annotated tags and GitHub releases

## Sources

- [Issue 18](https://github.com/BradGroux/ai-native-operating-framework/issues/18)
- [ADR-010](0010-same-version-documentation-republication.md)
