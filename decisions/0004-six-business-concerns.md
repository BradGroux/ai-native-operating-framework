# ADR-004 — Six business concerns

- **Status:** accepted
- **Date:** 2026-07-30
- **Owner:** Brad Groux

## Question

Which essential subjects must the framework standardize across business
processes?

## Decision

The framework organizes its standards around six business concerns:

1. **Intent** — purpose, scope, expected outcomes, and governing requirements.
2. **Responsibility** — ownership, roles, authority, and accountability.
3. **Work** — inputs, activities, outputs, dependencies, and handoffs.
4. **Control** — policies, decisions, approvals, risks, exceptions, escalation,
   and recovery.
5. **Assurance** — evidence, verification, quality, and completion.
6. **Learning** — review, feedback, change, and continual improvement.

These concerns define what business operations must make explicit without
prescribing a lifecycle.

## Consequences

- The framework is organized by business meaning rather than document types.
- Different processes and domains may use different documents and lifecycles
  while addressing the same concerns.
- Standards, methods, SOP guidance, and examples should trace back to one or
  more of the six concerns.
- Concepts that do not serve one of these concerns require explicit
  justification before entering the framework.

## Alternatives considered

Organizing the framework around artifact types was rejected because it would
define the framework by documents rather than the business concerns those
documents serve.

## Affected artifacts

- `project/planning/context.md`
- `project/planning/open-questions.md`
- `project/planning/status.md`
- `framework/charter.md`
- `framework/operating-framework.md`
- `framework/sop-content-standard.md`
- `framework/standards-maintenance-method.md`
- `framework/glossary.md`
- `examples/`
