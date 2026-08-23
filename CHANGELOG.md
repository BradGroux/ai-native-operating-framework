# Changelog

All material framework releases and repository changes will be recorded here.

## 1.1.0 — 2026-08-22

### Changed

- Adopted
  [Open Framework Commons v1.1.0](https://github.com/BradGroux/open-framework-commons/releases/tag/v1.1.0)
  at exact release commit
  [f25a2b89b4aed95984fd235e2e229efe52c125d8](https://github.com/BradGroux/open-framework-commons/commit/f25a2b89b4aed95984fd235e2e229efe52c125d8).
  Commons adds Focus Operating Framework as a fifth independent product and
  adds repository-stewardship surfaces; its nine shared principles and product
  independence boundaries are unchanged.
- Changed the framework-application lead-in from "an existing process" to "a
  business process" so it agrees with the existing list of new and existing
  application targets. This resolves issue 17 without changing framework
  meaning.
- Replaced future same-version republication with forward-only semantic
  versioning. Published tags are immutable after v1.0.0; documentation-only
  corrections receive a new version. ADR-010 remains historical evidence of
  the bounded v1.0.0 republications, and ADR-011 governs releases from v1.1.0
  forward.
- Bumped the current framework, citation, governance, changelog, and release
  surfaces from 1.0.0 to 1.1.0. The v1.0.0 tag remains unchanged.

### Added

- A machine-readable `VERSION` file and validation that keeps it synchronized
  with citation and release metadata.
- ADR-011 for forward-only semantic versioning and ADR-012 for the accountable
  Commons v1.1.0 adoption.
- A maintained release index, a complete v1.1.0 release record, and an
  accountable disposition of issues 17 through 20.

### Compatibility and limits

Version 1.1.0 changes ecosystem context, release governance, and one editorial
sentence. It does not change framework business meaning, requirements,
professional boundaries, example status, licensing, or implementation
independence. All examples remain illustrative and not domain-validated. The
shared operating memory standard still has no human records, privacy, security,
legal, knowledge-management, or business-continuity review. Those limits are
not represented as completed validation or as blockers to publishing the
framework documentation.

## 1.0.0 — 2026-07-30; refreshed 2026-08-03 and 2026-08-11

### Visualization and readability refresh — 2026-08-11

- Reflowed wide Mermaid diagrams into document-width layouts so labels remain
  readable on normal repository and document surfaces.
- Added thirteen focused diagrams covering the charter, core terminology,
  example anatomy, and authority or handoff relationships in Examples 1–10.
- Increased the rendered diagram set from twenty-six to thirty-nine without
  changing framework requirements or imposing a universal business lifecycle.
- Added validation for rendered width, aspect ratio, and expected visualization
  coverage so unreadable layouts fail the repository gate.
- Recorded the bounded same-version documentation republication policy in
  [ADR-010](decisions/0010-same-version-documentation-republication.md).

This refresh changes presentation and repository validation only. It does not
change the charter's business meaning, the six concerns, the eight SOP content
areas, shared operating memory requirements, the six maintenance activities,
governance authority, example status, licensing, or professional boundaries.
The original 2026-07-30 effective date remains unchanged.

### Commons release-pin correction — 2026-08-03

- Repinned Open Framework Commons `v1.0.0` from the initially reviewed release
  commit
  `27870fb1d57d951b9ef5a3a86f33ef0`<wbr>`68ee557da`
  to corrected release commit
  [a0f0d384e9010a65d1a21a324b4c912433d5e0<wbr>31](https://github.com/BradGroux/open-framework-commons/commit/a0f0d384e9010a65d1a21a324b4c912433d5e031).
- Before this product's coordinated tag replacement, its annotated
  `v1.0.0` tag object was
  `3424738c1c3cfdcb1e009789f84a8a33`<wbr>`a1ae0bdb` and peeled to
  `2e402d89598849f37e12f6e54c9d7f24`<wbr>`ac5ca76c`.
- Confirmed that the corrected Commons tree leaves all nine shared principles
  and product-independence boundaries unchanged. It makes Relationship
  Operating Framework current, adds explanatory diagrams, and publishes
  product adoption links.
- Recorded the moved Commons tag, its conflict with the Commons immutability
  rule, the one-time no-downstream-use exception, and future release handling in
  [ADR-009](decisions/0009-correct-open-framework-commons-v1-0-0-release-pin.md).

The original ADR-008 decision body and adoption reviews remain intact as
point-in-time evidence of the first reviewed pin; ADR-008 now links to its
exact-pin supersession. Fresh reviews govern this corrected release pin.
AI-Native remains at `v1.0.0` and is republished after merge and final
verification.

The corrected candidate passed fresh independent
[standards](project/reviews/open-framework-commons-v1-0-0-final-pin-standards-review-2026-08-03.md)
and
[specification](project/reviews/open-framework-commons-v1-0-0-final-pin-specification-review-2026-08-03.md)
reviews with no unresolved findings.

### Documentation refresh — 2026-08-03

- Adopted
  [Open Framework Commons](https://github.com/BradGroux/open-framework-commons)
  [`v1.0.0`](https://github.com/BradGroux/open-framework-commons/tree/v1.0.0)
  at release commit
  [27870fb1d57d951b9ef5a3a86f33ef0<wbr>68ee557da](https://github.com/BradGroux/open-framework-commons/releases/tag/v1.0.0)
  as shared ecosystem context, with the principle dispositions and independent
  authority boundary recorded in Governance.
- Recorded the accountable adoption, interpretation, release treatment,
  limitations, and affected artifacts in
  [ADR-008](decisions/0008-adopt-open-framework-commons-v1-0-0.md).
- Published sanitized
  [standards](project/reviews/open-framework-commons-v1-0-0-adoption-standards-review-2026-08-03.md)
  and
  [specification](project/reviews/open-framework-commons-v1-0-0-adoption-specification-review-2026-08-03.md)
  review records for the corrected candidate.

This refresh is documentation-only. It does not amend the charter, business
method, framework vocabulary, examples, research, governance authority,
roadmap, or release ownership.

### Added

- Canonical repository hierarchy for framework, examples, decisions, and
  project records.
- Documented and linked the framework's place within
  [Digital Meld](https://digitalmeld.io)'s research arm and its relationship to
  the [AI Dev Days](https://github.com/bradgroux/ai-dev-days) research and
  education initiative, without changing framework governance or authority.
- Charter, operating framework, SOP content standard, shared operating memory
  standard, standards maintenance method, and approved glossary.
- Eleven complete illustrative examples.
- Framework-wide and example-specific contribution SOPs.
- Governance, repository instructions, navigation, and focused Mermaid
  diagrams, including SOP and community feedback loops.
- Stage 2 specification, completion report, and preserved project history.
- Sanitized independent framework application test and accountable finding
  disposition.
- Sanitized independent post-fix review.
- Domain-native employee lifecycle example structure, temporary-work
  clarification, and an operational appeal procedure.
- Domain-native construction incident-response structure with separate SOP
  content traceability and an explicit learning feedback loop.
- GitHub contribution and appeal intake, MIT licensing, and incoming
  contribution terms.
- A short community Code of Conduct.
- GitHub issue forms and a pull-request template aligned with the contribution
  SOP.
- A security and sensitive-disclosure policy, explicit code ownership, and a
  private-reporting contact link.
- A repeatable repository validation command and GitHub workflow covering local
  links, canonical invariants, example completeness, diagrams, YAML and CFF
  metadata, publication-safety markers, and secret scanning.
- Citation metadata for the version 1.0.0 release.
- A privacy-reviewed public-history baseline that excludes superseded working
  material and private development identifiers.
- ADR-007 establishing shared operating memory as a cross-cutting business
  capability without adding another concern or SOP content requirement.
- A sanitized, complete shared operating memory capture-and-handoff SOP.
- Five illustrative operating-memory file-structure patterns, including a
  federated alternative.
- Visuals for operating-memory layers, participant use, handoff acceptance,
  logical file roles, and federated systems.
- An integrated extension review and a source-bounded prompt for later
  independent application review.
- Sanitized independent shared operating memory application and adversarial
  AI-assisted reviews, with an accountable findings disposition.
- A standard dated naming convention and role-based reviewer attribution for
  public review records, with repository validation for required metadata,
  controlled role labels, and common identity-attribution forms.

### Status

- The version 1.0.0 framework baseline is complete and owner-approved for
  release.
- All examples are illustrative and not domain-validated.
- The framework and submitted contributions use the MIT License.
- The designated public location is
  `github.com/bradgroux/ai-native-operating-framework`.
