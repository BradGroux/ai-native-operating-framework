# ADR-001 — Business framework, not technology specification

- **Status:** accepted
- **Date:** 2026-07-30
- **Owner:** Brad Groux

## Question

Does the AI-Native Operating Framework define business operating standards and
a method, or does it also specify how technology represents, exchanges, or
implements them?

## Decision

The AI-Native Operating Framework defines business operating standards and a
method for applying them. Technology may use the framework, but tools, models,
harnesses, protocols, adapters, schemas, machine-specific representations, and
technical conformance are outside its scope.

The framework has one canonical body of documentation for people and machines.
Machines are expected to understand well-written business documentation; the
framework will not create a parallel machine-oriented design.

## Consequences

- Applying the framework means organizing business work according to its
  standards, not adapting it to software.
- Machine understanding is treated as an outcome of documentation quality.
- Technical interoperability and harness migration are not framework
  deliverables.
- Earlier proposals for framework schemas, protocol mappings, harness profiles,
  adapters, capability declarations, and migration manifests are superseded as
  framework requirements.
- Examples may mention technology used during work, but that technology cannot
  define or alter the framework.

## Dissent and uncertainty

The original planning bundle proposed several technology-oriented discovery and
delivery requirements. Brad explicitly rejected that framing during discovery
on 2026-07-30.

## Affected artifacts

- `project/planning/context.md`
- `project/planning/open-questions.md`
- `project/planning/status.md`
- `framework/charter.md`
- `framework/operating-framework.md`
- `framework/sop-content-standard.md`
- `framework/standards-maintenance-method.md`
- `framework/glossary.md`
