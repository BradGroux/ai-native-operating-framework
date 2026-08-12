# ADR-010 — Same-Version Documentation Republication

- **Status:** accepted
- **Date:** 2026-08-11
- **Owner:** Brad Groux

## Question

May an approved framework release keep its semantic version when a later change
improves only documentation presentation or repository validation, and if so,
what release-integrity controls apply?

## Context and Evidence

Version 1.0.0 is a documentation-based business framework. The visualization
refresh merged through pull request 14 improves diagram readability, adds views
of relationships already stated in prose, and adds a rendered-legibility gate.
It does not change framework or operating meaning.

Treating every presentation correction as a new framework version would imply a
semantic change that did not occur. Moving a published tag without strict
controls would instead make release identity unreliable. The repository
therefore needs a narrow distinction between an authorized same-version
documentation republication and a semantic framework release.

## Alternatives Considered

### Create a new semantic version for every merged documentation change

This keeps tags immutable but makes semantic versions describe repository
activity rather than changes to the framework's business meaning.

### Never republish documentation until a semantic framework change occurs

This preserves the existing tag but leaves the published release with known
readability and accessibility defects after those defects have been corrected.

### Permit bounded same-version documentation republication

This keeps the semantic identity truthful while requiring explicit authority,
visible history, exact validation, lease protection, and release readback.

## Decision

The steward may explicitly authorize republication under the current semantic
version only when every change is limited to one or more of these categories:

- presentation, layout, visualization, or accessibility;
- navigation, links, or explanatory orientation;
- publication hygiene or correction of non-substantive public metadata; or
- repository validation that protects the same approved content.

A same-version republication is not permitted when a change alters:

- charter or framework business meaning;
- a framework requirement, concern, SOP content area, memory requirement, or
  maintenance activity;
- governance authority or accountable ownership;
- substantive operating guidance or the operational meaning of an example;
- licensing, professional boundaries, review status, or release scope; or
- an adopted external release pin governed by ADR-009.

Any such change requires a new semantic version and its appropriate review.

Before a same-version republication:

1. the owner authorizes the specific refresh;
2. the changelog records its date, scope, and semantic boundary;
3. the exact candidate passes the complete repository validation gate;
4. the merged tree is compared with the validated candidate tree;
5. the current remote annotated tag object and peeled commit are recorded;
6. the replacement annotated tag is pushed only with an exact old-object
   lease;
7. release notes preserve relevant republication history and identify the new
   release commit and tree; and
8. the remote tag, release body, authorship, generated archives, and archive
   contents receive direct readback.

## Consequences

- The visualization and readability refresh remains version 1.0.0.
- The original effective date remains 2026-07-30; the changelog records the
  later refresh date.
- Consumers can distinguish semantic framework evolution from corrections to
  how the same framework is presented and validated.
- Published tags remain expected to be immutable by default. Same-version
  movement is a controlled, visible republication, not routine branch
  publication.
- ADR-009 remains unchanged: future corrections to adopted external release
  pins normally require a new semantic version.

## Dissent and Uncertainty

No dissent is recorded. Even with lease protection and visible history, moving
a published tag may surprise consumers who cached the previous object. Release
notes must continue to tell those consumers to refresh the tag explicitly.

This decision does not claim field validation, certification, professional
review, or real-world effectiveness for the framework or its examples.

## Affected Artifacts

- `CHANGELOG.md`
- `GOVERNANCE.md`
- `decisions/README.md`
- version 1.0.0 annotated tag and GitHub release

## Sources

- [Issue 15](https://github.com/BradGroux/ai-native-operating-framework/issues/15)
- [Pull request 14](https://github.com/BradGroux/ai-native-operating-framework/pull/14)
- [ADR-009](0009-correct-open-framework-commons-v1-0-0-release-pin.md)
