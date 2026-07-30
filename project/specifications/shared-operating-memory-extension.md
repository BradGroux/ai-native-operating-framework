# Shared Operating Memory Extension Specification

**Status:** Approved by owner<br>
**Owner:** Brad Groux<br>
**Approval date:** 2026-07-30<br>
**Release target:** Version 1.0.0 before public publication

## Purpose

Extend the AI-Native Operating Framework with a clear, technology-independent
business standard for how organizations preserve and share the sources,
context, decisions, work state, evidence, handoffs, and lessons needed for
people and AI to continue work over time.

The extension must make operating memory explicit without turning the
framework into a software architecture, data platform, machine-memory design,
folder convention, or records-management substitute.

## Source and Publication Boundary

The owner supplied an internal Git-and-Markdown operating-memory procedure as
source context and authorized its concepts to be adapted.

The public framework must not reproduce private paths, identities,
organization-specific names, client or product names, helper commands,
credentials, or internal source references. The resulting example must state
its sanitized provenance and distinguish its implementation choices from
framework requirements.

## Accepted Design

1. Add **shared operating memory** as a cross-cutting framework capability.
2. Define it through a canonical business standard under `framework/`.
3. Keep the six framework concerns unchanged.
4. Keep the eight SOP content requirements unchanged.
5. Connect shared operating memory to Work, Control, Assurance, and Learning.
6. Require organizations to establish a proportionate operating-memory
   practice or equivalent existing control.
7. Keep technology, repository layout, file format, retrieval method, and
   machine-specific representation outside the framework requirement.
8. Add one complete sanitized example SOP and several illustrative operational
   file-structure patterns.
9. Use visuals where they clarify memory layers, flow, authority, handoffs, or
   improvement.
10. Update all affected canonical, explanatory, governance, contribution,
    navigation, release, planning, specification, and review material.

## Required Deliverables

- `decisions/0007-shared-operating-memory.md`
- `framework/shared-operating-memory-standard.md`
- amendments to the charter, operating framework, SOP content standard,
  standards maintenance method, glossary, and framework navigation
- `examples/11-shared-operating-memory-capture-and-handoff.md`
- `examples/shared-operating-memory-file-structures.md`
- amendments to example collection and contribution guidance
- repository-wide navigation, governance, release, citation, and status updates
- a targeted integrated review record
- a prompt suitable for a later clean-context independent reviewer

## Canonical Standard Requirements

The shared operating memory standard must make clear:

- what shared operating memory means and why it is a business capability;
- how it relates to the existing framework without becoming a new concern or
  SOP content area;
- what information deserves durable capture;
- what minimum business meaning a durable memory item communicates;
- how sources, synthesis, decisions, work state, handoffs, evidence, standards,
  and learning differ;
- how authority, provenance, confidence, uncertainty, and conflicts are
  handled;
- how people and AI locate, assess, use, capture, verify, share, and maintain
  operating memory;
- how access, privacy, confidentiality, security, rights, retention, deletion,
  and recovery are governed;
- how stale, incorrect, duplicated, unavailable, or superseded memory is
  contained and corrected;
- and how lessons are promoted into maintained standards and SOPs.

## Example Requirements

The complete SOP example must:

- satisfy all eight SOP content requirements;
- annotate all six framework concerns;
- state sanitized-from-real-work provenance and owner permission;
- remain illustrative and not domain-validated;
- use a concrete version-controlled document repository as an example-specific
  operating choice;
- define human accountability and bounded AI participation;
- include normal, exception, failure, correction, handoff, and recovery paths;
- include a minimum note example without imposing a framework template;
- and contain no private or organization-identifying source detail.

The structure companion must:

- show at least four operational file-structure patterns;
- include a minimal team, multi-team or portfolio, controlled or regulated, and
  time-bounded initiative pattern;
- explain when each pattern fits;
- show logical relationships visually;
- include a federated alternative that does not require one repository;
- and state that the patterns are illustrative implementation choices.

## Repository Review

Every existing document must be assessed for one of three dispositions:

1. **Update** — current meaning, navigation, release state, example count, or
   authoritative references are affected.
2. **Historical note** — the document correctly reports an earlier scope or
   review and needs only a later-extension notice.
3. **No change** — the document remains accurate and gains no useful clarity
   from another reference.

Historical specifications and review reports must not be silently rewritten to
claim they reviewed material that did not yet exist.

## Acceptance Criteria

- The standard is understandable without an author briefing.
- People and AI receive the same business guidance.
- The core prescribes no tool, schema, protocol, folder tree, model-memory
  mechanism, or technical conformance requirement.
- The example and structure patterns are publication-safe.
- The six concerns, eight SOP content areas, and six maintenance activities
  retain their approved names and meanings.
- All local Markdown links and heading references resolve.
- All Mermaid diagrams render.
- All eleven full examples satisfy collection requirements.
- Citation and GitHub metadata remain valid.
- Privacy and secret scans report no public findings.
- Standards and specification reviews have no unresolved blocker.
- A later independent reviewer has a complete, source-bounded test prompt.
