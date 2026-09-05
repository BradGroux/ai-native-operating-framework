# ADR-013 — Calendar editions, bounded continuity and Commons adoption

- **Status:** accepted
- **Date:** 2026-09-05
- **Owner:** Brad Groux
- **Authority:** Direct owner instruction to audit, remediate and release this edition

## Decision and rationale

Adopt prospective UTC calendar editions under Governance. This supersedes only
ADR-011's numbering rule; preserve all historical content and tag identities.
An edition date is easier to locate chronologically but cannot communicate
compatibility alone. Retaining semantic numbering was considered; relabeling
historical releases was rejected because it obscures cited identities.

Independently adopt Open Framework Commons `v2026.09.05`, annotated object
`67914a6e305768206f1ead83dfcbc4325b951168`, peeled commit
`8868a248457dd7b663563beb243c5ebcbb8ac360`, from
[the Commons release](https://github.com/BradGroux/open-framework-commons/releases/tag/v2026.09.05).
Authenticated GitHub ref/tag readback and Git agree on both identities. The tag
is annotated and unsigned; no signature claim is made.

## Adoption scope and limits

Reviewed its principles, boundaries, governance, research/review guidance,
Decision 0002, adverse cases, audit disposition and release procedure at that
identity. Adopt all nine shared principles and clarified consent, legitimate
help, privacy, stopping, honest evidence and explicit conflict/adoption boundaries.
No shared principle is deferred and no local deviation is taken. Product-local
charter, method, terminology, governance and professional authority remain here.
Commons' validator, dependency stack, all-product review duties and protection
configuration are Commons-local operations and are not adopted requirements.

The strongest counterexample is treating openness or continuity as a duty to
retain or publish private operational records. Existing memory rights, retention
and containment controls reject that reading; Governance now makes the shared
boundary explicit. A second is requiring contribution before a beginner asks
for help; no such prerequisite is created here. These are reasoned commitment
and interpretation decisions, not evidence of measured benefit.

## Local method clarification

Resolve #25 by separating a successful transfer from a recorded failed attempt:
current ownership continues until acceptance or authorized reassignment. Resolve
#26 by bounding deferrals and prohibiting waiver of required review, controls or
missing authority. Clarify that low-risk owner-led review does not universally
require a second person. Preserve required separation of duties.

These are substantive clarifications: adopters who counted sending or rejection
as completion, waived required specialist review, or imposed peer review on every
routine must reconsider those choices. The six concerns, eight SOP areas, six
maintenance activities and technology independence stay unchanged. No universal
lifecycle, new template or additional mandatory role is introduced.

## Consequences and downstream disposition

AI Dev Days remains an independent education/application companion. Its inspected
teaching alignment at `8c1d80d` targets AI-Native v1.0.0 and its own Commons pin
is v1.0.0. Neither is changed here. A future teaching update should distinguish
accepted transfer, attempted transfer and retained ownership; exercise absent
mandatory review and a small-team routine; label the selected edition. It does
not need a simultaneous release. Influence, Relationship and Focus have no
local runtime or content consumer that this change requires migrating.

No runtime/package/schema version exists here. CFF treats the quoted edition as
a string; validators and release commands must parse calendar identifiers, not
SemVer. Historical CFF files are preserved.

## Evidence, dissent and reconsideration

See the [audit disposition](../project/reviews/calendar-edition-audit-disposition-2026-09-05.md)
and [fictional cases](../project/reviews/calendar-edition-content-test-2026-09-05.md).
No substantive dissent is recorded. Revisit when actual use exposes unresolved
ownership, inappropriate burdens, missing authority or unsafe interpretations.
Human specialist and practitioner reviews have not occurred; earlier reviews
and issue 19/20 closure dispositions are preserved without reinterpreting them.
