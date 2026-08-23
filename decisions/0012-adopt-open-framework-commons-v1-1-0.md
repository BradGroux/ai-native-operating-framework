# ADR-012 — Adopt Open Framework Commons v1.1.0

- **Status:** accepted
- **Date:** 2026-08-22
- **Owner:** Brad Groux

## Question

Should the AI-Native Operating Framework adopt Open Framework Commons v1.1.0,
and what changes locally if it does?

## Context and Evidence

AI-Native adopted Commons v1.0.0 through ADR-008 and corrected that release pin
through ADR-009. Commons v1.1.0 is an annotated release whose tag object
`79e5f06dab46f262cad1d1daf7840e683ffc3880` peels to exact commit
`f25a2b89b4aed95984fd235e2e229efe52c125d8`.

The v1.1.0 comparison shows that Commons:

- recognizes Focus Operating Framework as a fifth independent ecosystem
  product through an explicit Charter decision;
- updates the complete product lists and shared-applicability test from four
  products to five;
- corrects point-in-time review indexing and stable downstream adoption links;
  and
- adds contribution, conduct, security, citation, ownership, validation, and
  release surfaces for Commons itself.

The nine shared principles are unchanged. Commons remains documentation, does
not become a parent framework or implementation layer, and cannot amend a
product automatically.

## Alternatives Considered

### Remain on Commons v1.0.0

AI-Native could retain its existing adoption because Commons does not require
downstream updates. That would omit the current five-product ecosystem context.

### Reference Commons v1.1.0 without adopting it

This would make discovery current but leave the product's accountable
disposition ambiguous.

### Adopt the exact v1.1.0 release

This records a clear product-local decision while preserving AI-Native's own
authority and release lifecycle.

## Decision

Adopt Open Framework Commons v1.1.0 at exact commit
`f25a2b89b4aed95984fd235e2e229efe52c125d8`.

AI-Native continues to adopt all nine shared principles, with none deferred and
no deviations. The charter, six concerns, eight SOP content areas, shared
operating memory standard, six maintenance activities, terminology, examples,
research, governance, roadmap, releases, licensing, and implementation choices
remain product-local.

The Focus scope addition is accepted as ecosystem context. It does not change
AI-Native framework meaning or create a dependency on Focus. Commons repository
stewardship surfaces govern Commons only and are not copied into this product.

Adopting a new external release pin changes product release scope, so AI-Native
advances to version 1.1.0 under ADR-011.

## Consequences

- README and Governance point to the exact Commons v1.1.0 tag and commit.
- ADR-008 and ADR-009 remain historical evidence for the v1.0.0 adoption and
  correction.
- Future Commons releases still require separate product review and an explicit
  adopt, defer, or deviate decision.
- The AI-Native `v1.0.0` tag does not move.

## Dissent and Uncertainty

No material conflict or dissent is recorded. The review is documentation and
release-integrity evidence only. It does not establish compatibility testing,
field validation, certification, legal or professional review, or real-world
effectiveness for Commons, AI-Native, Focus, or another ecosystem product.

## Affected Artifacts

- `README.md`
- `GOVERNANCE.md`
- `CHANGELOG.md`
- `CITATION.cff`
- `VERSION`
- `decisions/README.md`
- version 1.1.0 release records

## Sources

- [Open Framework Commons v1.1.0](https://github.com/BradGroux/open-framework-commons/releases/tag/v1.1.0)
- [Commons Decision 0001](https://github.com/BradGroux/open-framework-commons/blob/v1.1.0/decisions/0001-recognize-focus-operating-framework.md)
- [Issue 21](https://github.com/BradGroux/ai-native-operating-framework/issues/21)
- [ADR-008](0008-adopt-open-framework-commons-v1-0-0.md)
- [ADR-009](0009-correct-open-framework-commons-v1-0-0-release-pin.md)
- [ADR-011](0011-forward-only-semantic-versioning.md)
