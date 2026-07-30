# Stage 2 Specification — AI-Native Operating Framework

**Status:** Approved for delivery planning<br>
**Owner:** Brad Groux<br>
**Approved:** 2026-07-30

> **Later extension:** This specification governs the original Stage 2 package
> and its ten examples. The owner later approved shared operating memory as a
> version 1.0.0 extension under
> [ADR-007](../../decisions/0007-shared-operating-memory.md) and the
> [shared operating memory extension specification](shared-operating-memory-extension.md).
> The original scope below is retained as a point-in-time delivery record.

## Problem Statement

The source bundle contains a strong strategic thesis but repeatedly frames the
framework as a technology product, interoperability protocol, migration system,
or future standard. That framing obscures the simpler objective: define a clear
business operating framework and method for work performed by people and AI.

At the time this specification was approved, the active workspace recorded the
discovery decisions but did not yet contain the finished framework documents or
examples.

## Solution

Produce a concise, internally consistent documentation package that defines:

- the framework's purpose, scope, commitments, and non-goals;
- six business concerns: Intent, Responsibility, Work, Control, Assurance, and
  Learning;
- an SOP content standard with eight required content areas and no mandatory
  document layout;
- a six-activity method for maintaining standards and SOPs: Understand,
  Document, Validate, Approve, Use, and Improve;
- ten complete, annotated business-process examples;
- and an SOP for contributing and maintaining additional examples.

The finished package will include:

1. `framework/charter.md`
2. `framework/operating-framework.md`
3. `framework/sop-content-standard.md`
4. `framework/standards-maintenance-method.md`
5. `framework/glossary.md`
6. `examples/CONTRIBUTING.md`
7. `examples/README.md`
8. Ten individual example documents
9. Existing discovery context and accepted decision records

## User Stories

1. As a business owner, I want a clear statement of the framework's purpose so
   that I can decide whether it fits how my organization operates.
2. As a business owner, I want the framework separated from technology choices
   so that changing tools does not change our operating standards.
3. As a process owner, I want a small set of business concerns so that I can
   identify what a process must make explicit.
4. As a process owner, I want the framework to work with existing business
   lifecycles so that I do not have to replace a sound management system.
5. As a process owner, I want a content standard for SOPs so that I can judge
   completeness without enforcing one template.
6. As a process owner, I want purpose, scope, and outcomes made explicit so that
   people understand why a procedure exists.
7. As a process owner, I want accountable ownership and decision authority made
   explicit so that responsibility cannot disappear between people and AI.
8. As a practitioner, I want triggers, prerequisites, inputs, and authoritative
   sources documented so that I know when and how work begins.
9. As a practitioner, I want activities, decisions, dependencies, handoffs, and
   outputs documented so that I can perform the work consistently.
10. As a control owner, I want policies, controls, approvals, and risks
    documented so that work remains within business requirements.
11. As a practitioner, I want exceptions, escalation, recovery, and stop
    conditions documented so that the SOP remains useful off the happy path.
12. As a reviewer, I want completion criteria, verification, and evidence
    documented so that I can determine whether work was done properly.
13. As a maintainer, I want review responsibility and change history documented
    so that standards remain current.
14. As an accountable human owner, I want AI participation governed by the same
    business standards as human participation so that accountability remains
    clear.
15. As an AI performing work, I want the same clear context and procedure
    available to people so that no parallel machine instructions are required.
16. As a standards author, I want a practical maintenance method so that I can
    move from observed work to an approved and usable SOP.
17. As a standards author, I want validation to cover normal, exceptional, and
    failure scenarios so that procedures reflect real operations.
18. As an approver, I want changes routed through accountable ownership so that
    standards are not silently overwritten.
19. As a practitioner, I want approved standards easy to find and understand so
    that written procedures can guide actual work.
20. As a process owner, I want evidence and incidents to feed improvement so
    that the operating standard learns from experience.
21. As a reader, I want complete examples from different business domains so
    that I can see how the same framework applies without forcing one workflow.
22. As a reader, I want every example's provenance stated so that I understand
    whether it is fictional, generalized, sanitized, or directly sourced.
23. As a reader, I want domain-specific choices clearly separated from framework
    requirements so that examples do not accidentally redefine the framework.
24. As a contributor, I want an SOP for adding examples so that I know the
    quality, safety, review, and maintenance expectations.
25. As a contributor, I want flexible document layouts so that an example can
    use language and structure appropriate to its domain.
26. As a maintainer, I want duplicate or low-value examples identified before
    acceptance so that the collection stays useful.
27. As a domain reviewer, I want professional-accuracy claims bounded by review
    status so that illustrative material is not mistaken for expert guidance.
28. As a maintainer, I want contributor attribution and maintenance ownership so
    that examples can be reviewed and updated over time.
29. As an educator, I want a coherent framework package so that I can teach the
    method without making tools the subject.
30. As an independent organization, I want the framework to remain open and
    vendor-neutral so that I can adopt it without adopting Digital Meld or any
    particular technology.

## Implementation Decisions

- The framework is a business operating framework and method.
- Technology may consume the framework but cannot define or alter it.
- People and AI work under the same business standards and SOPs.
- Human accountability remains explicit.
- The framework applies to existing business lifecycles.
- The six approved business concerns are the framework's organizing structure.
- SOP quality is based on eight required content areas, not template headings.
- The standards maintenance method contains six practical activities.
- Examples are explanatory business SOPs, not tests, proofs, implementations,
  tutorials, or launch gates.
- Each example contains a scenario overview, complete SOP, six-concern
  annotation, provenance label, and domain-specific boundary note.
- The ten approved example domains are:
  1. accounts-payable invoice processing;
  2. software-change delivery;
  3. construction field-incident response;
  4. employee onboarding and offboarding;
  5. M&A Day 1 transition;
  6. customer complaint and service recovery;
  7. regulatory-change implementation;
  8. supply-chain disruption response;
  9. sales proposal and contract approval;
  10. patient referral and care transition.
- The contribution SOP requires publication safety, provenance, completeness,
  annotations, review status, attribution, maintenance, and maintainer
  acceptance.
- Clear prose and useful document structure serve people and machines together.
  No machine-specific format or parallel representation will be created.

## Testing Decisions

Review the finished documentation at the highest reader-visible seams:

1. **Core coherence:** Charter, framework, SOP standard, method, glossary, and
   decisions use the same definitions and boundaries.
2. **SOP completeness:** Each example makes all eight required content areas
   clear, regardless of layout.
3. **Concern traceability:** Each example annotation explains Intent,
   Responsibility, Work, Control, Assurance, and Learning.
4. **Boundary integrity:** No core document introduces technology specifications,
   harnesses, protocols, adapters, machine-specific formats, mandatory universal
   lifecycles, or mandatory SOP templates.
5. **Example clarity:** Every example states its provenance, domain assumptions,
   review status, and domain-specific boundaries.
6. **Publication safety:** Examples contain no confidential, personal,
   proprietary, unsafe, or improperly licensed information.
7. **Navigation:** Internal links resolve and a reader can move from the
   framework to the method, standard, examples, and contribution SOP.
8. **Plain-language review:** Documents are understandable without product,
   software, or standards-industry jargon.

These reviews assess documentation quality and internal consistency. They do not
turn the examples into a framework-validation suite.

## Out of Scope

- Software, services, APIs, schemas, protocols, or machine-specific formats.
- Harness adapters, capability profiles, or tool integrations.
- Tool-to-tool migration requirements or migration manifests.
- Technical interoperability or conformance certification.
- A universal lifecycle imposed on business processes.
- A mandatory SOP document template.
- Product-market discovery, target-user selection, or adoption wedges.
- Digital Meld sales, delivery, marketing, or commercial operating systems.
- AI Dev Days curriculum or event production.
- Public launch, publication, deployment, or external messaging.
- Claims that the framework is an industry standard.

## Further Notes

- The authoritative source bundle remains immutable.
- Discovery context and accepted ADRs control where they supersede earlier
  proposed technology-oriented requirements.
- Examples involving medicine, law, safety, regulation, or other professional
  domains must be labeled appropriately and must not claim domain validation
  without relevant review.
- Publication is a separate owner-approved action after the finished package is
  reviewed.
