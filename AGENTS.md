# Repository Instructions

## Purpose

This repository contains the AI-Native Operating Framework: a business operating
framework and method for work performed by people and AI.

## Authority

Apply this order:

1. Direct current owner instruction.
2. `framework/charter.md`.
3. Accepted records under `decisions/`.
4. Canonical documents under `framework/`.
5. Repository governance and contribution guidance.
6. Examples.
7. Project records and history.

Lower-authority material must not silently redefine higher-authority material.

## Content Boundaries

- Keep framework core independent of software, models, protocols, schemas,
  harnesses, adapters, and machine-specific representations.
- Treat AI as a possible participant in business work, not as a separate
  operating system.
- Preserve explicit human accountability.
- Apply the framework to existing business lifecycles; do not impose a
  universal lifecycle.
- Require business meaning, not a universal SOP template.
- Treat shared operating memory as a controlled business capability spanning
  Work, Control, Assurance, and Learning; do not turn it into a prescribed
  repository, schema, retrieval system, or model-memory design.
- Examples illustrate the framework and never create requirements.
- Keep Digital Meld, AI Dev Days, implementation, and marketing material out of
  framework core.

## Structure

- Canonical framework: `framework/`
- Illustrative examples: `examples/`
- Accepted rationale: `decisions/`
- Development records and history: `project/`

Do not recreate `deliverables/` or `framework-workspace/` staging layers in this
repository.

## Documentation

- Use clear Markdown and kebab-case filenames inside content directories.
- Use one canonical document body for people and machines.
- Add diagrams only when relationships, sequence, or hierarchy are materially
  clearer visually.
- Prefer Mermaid diagrams that remain understandable with their surrounding
  prose.
- Keep links relative and repository-portable.
- State status, ownership, provenance, review limits, and professional
  boundaries honestly.

## Verification

Before reporting a change complete:

- run `scripts/validate-repository.sh`;
- verify all local Markdown links and heading references;
- confirm canonical vocabulary remains consistent;
- check examples against all eight SOP content areas and six concerns;
- confirm operating-memory guidance preserves authority, provenance, handoff,
  privacy, retention, correction, recovery, and technology independence;
- inspect publication safety and domain-review status;
- confirm diagrams parse and do not imply a universal lifecycle;
- review changes separately against repository standards and the originating
  specification or decision; and
- report remaining owner, domain, licensing, and publication decisions.
