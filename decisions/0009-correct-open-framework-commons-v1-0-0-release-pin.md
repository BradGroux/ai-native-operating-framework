# ADR-009 — Correct Open Framework Commons v1.0.0 Release Pin

- **Status:** accepted
- **Date:** 2026-08-03
- **Owner:** Brad Groux

## Question

How should the AI-Native Operating Framework respond after the Open Framework
Commons `v1.0.0` annotated tag moved from the commit reviewed in ADR-008 to a
corrected release commit?

## Decision

AI-Native now pins Open Framework Commons
[`v1.0.0`](https://github.com/BradGroux/open-framework-commons/tree/v1.0.0)
to corrected release commit
[a0f0d384e9010a65d1a21a324b4c912433d5e0<wbr>31](https://github.com/BradGroux/open-framework-commons/commit/a0f0d384e9010a65d1a21a324b4c912433d5e031).
This decision supersedes only the exact Commons release pin in
[ADR-008](0008-adopt-open-framework-commons-v1-0-0.md). The original decision
body and its review records remain point-in-time evidence rather than being
rewritten.

The source comparison found:

- all nine shared principles are unchanged;
- product independence and local authority remain unchanged;
- Relationship Operating Framework is now treated as an existing ecosystem
  product rather than a future product;
- explanatory ecosystem, content-location, and adoption-flow diagrams were
  added; and
- public links to each product's adoption record were added.

These changes do not alter AI-Native's charter, six concerns, eight SOP content
areas, shared operating memory standard, six maintenance activities,
terminology, examples, research, governance, roadmap, releases, or
implementation choices.

## Release-Integrity Exception

Commons Governance says published revisions use immutable annotated Git tags,
but the Commons `v1.0.0` tag moved from
`27870fb1d57d951b9ef5a3a86f33ef0`<wbr>`68ee557da` to
`a0f0d384e9010a65d1a21a324b4c912433d5e0`<wbr>`31` after AI-Native's initial
review.

The founding steward accepts the corrected pin as a one-time exception because
no downstream organizational use of the AI-Native Operating Framework is
recorded. This exception does not make a moving release tag acceptable
practice. A future correction to an adopted Commons release should use a new
semantic version; any unexpected tag movement must stop dependent publication
until it receives a visible product decision.

## Consequences

- Current discovery and governance surfaces identify the corrected commit.
- The previous pin remains visible in ADR-008, the original reviews, and the
  changelog.
- Fresh standards and specification reviews evaluate the corrected Commons
  tree and this release-integrity exception.
- AI-Native `v1.0.0` is republished from the verified merged commit under the
  no-downstream-use decision.
- Before replacement, the product's annotated `v1.0.0` tag object was
  `3424738c1c3cfdcb1e009789f84a8a33`<wbr>`a1ae0bdb` and its peeled commit
  was `2e402d89598849f37e12f6e54c9d7f24`<wbr>`ac5ca76c`.
- Later Commons revisions or tag movements never amend AI-Native automatically.

## Material Dissent and Limitations

The tag movement is a material release-integrity exception and remains visible.
No dissent from accepting the corrected pin is recorded. This decision does not
establish field validation, certification, compatibility, legal or professional
review, or real-world effectiveness.

## Affected Artifacts

- `README.md`
- `GOVERNANCE.md`
- `CHANGELOG.md`
- `decisions/0008-adopt-open-framework-commons-v1-0-0.md`
- `decisions/README.md`
- repository review and release records
