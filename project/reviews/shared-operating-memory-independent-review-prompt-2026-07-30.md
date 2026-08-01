# Independent Shared Operating Memory Review Prompt

**Status:** Reusable review prompt<br>
**Record date:** 2026-07-30<br>
**Intended review role:** Independent clean-context reviewer

Use this prompt with a clean-context reviewer that has access only to the
repository being reviewed.

> **Execution status:** Completed in two independent AI-assisted variations: an
> application review and an adversarial review. See the
> [application review](shared-operating-memory-independent-application-review-2026-07-30.md),
> [adversarial review](shared-operating-memory-independent-adversarial-review-2026-07-30.md),
> and [accountable disposition](shared-operating-memory-independent-reviews-disposition-2026-07-30.md).
> The prompt remains reusable for later clean-context review.

---

You are conducting an independent, source-bounded review of the AI-Native
Operating Framework's shared operating memory extension.

Do not use prior project memory, an author briefing, external conversation
history, or private source material. Treat the repository as your only source
of framework meaning.

## Purpose

Determine whether the extension gives people and AI enough clear business
guidance to establish, use, control, and improve shared operating memory without
prescribing a technology architecture or changing the framework's six concerns,
eight SOP content requirements, or six maintenance activities.

## Required Reading Order

Read these canonical documents first:

1. `framework/charter.md`
2. `framework/operating-framework.md`
3. `framework/sop-content-standard.md`
4. `framework/shared-operating-memory-standard.md`
5. `framework/standards-maintenance-method.md`
6. `framework/glossary.md`
7. `decisions/0007-shared-operating-memory.md`

Do not read the shared operating memory example or file structures until after
the application exercise below.

## Application Exercise

Using only the canonical documents, prepare a concise but complete operating
memory practice for this fictional scenario:

- A professional-services organization has four teams and several concurrent
  client engagements.
- Approved policies live in a controlled document system.
- Current work lives in a project system.
- Formal decisions live in a decision register.
- Client source files live in access-controlled engagement storage.
- Completion records live in a system of record.
- People and AI may both participate under the same controls.
- The organization does not use Git or a single knowledge repository.
- One engagement must be handed from one team to another after an unexpected
  staff absence.
- A summary conflicts with an authoritative client source.
- One AI-generated project note contains an unsupported claim.
- A privacy authority orders containment and authorized deletion of
  unnecessarily retained personal information.

Your practice must make clear:

- purpose, scope, and expected outcome;
- accountable ownership and participant authority;
- what deserves durable capture;
- memory classes and minimum business meaning;
- how authoritative sources and synthesis differ;
- how current work state and the cross-team handoff are preserved;
- how people and AI find, assess, use, capture, verify, and share memory;
- how access, privacy, rights, retention, correction, deletion, and recovery
  work;
- how the source conflict and unsupported AI claim are handled;
- how completion is verified;
- and how lessons reach maintained standards and SOPs.

Do not invent organizational authority, legal requirements, retention periods,
technology capabilities, or facts not provided by the scenario. Identify
unresolved decisions and their responsible authorities.

## Example Review

After completing the application exercise, read:

1. `examples/11-shared-operating-memory-capture-and-handoff.md`
2. `examples/shared-operating-memory-file-structures.md`
3. `examples/README.md`
4. `examples/CONTRIBUTING.md`

Assess whether:

- the full example satisfies all eight SOP content areas;
- its annotation addresses all six concerns accurately;
- its sanitized-from-real-work provenance and review limits are honest;
- its Git-and-document choices are unmistakably example-specific;
- the five structure patterns demonstrate meaningful implementation
  alternatives;
- the federated pattern supports the fictional no-Git scenario;
- people and AI receive the same business guidance;
- visuals clarify relationships without implying a universal workflow,
  lifecycle, repository, or schema;
- and no private, identifying, credential, or confidential source detail is
  present.

## Repository Consistency Review

Review all repository navigation, governance, contribution, release, planning,
specification, and review material affected by the extension.

Confirm:

- ADR-007 and the canonical standard agree;
- the charter amendment is explicit and supported by the decision record;
- the operating framework connects memory only to existing concerns;
- the SOP content standard still has exactly eight requirements;
- the maintenance method still has exactly six activities;
- the collection has eleven full examples and one non-SOP structure companion;
- original Stage 2 and independent reports remain visibly point-in-time rather
  than claiming later review;
- the public source contains no private paths, internal identities, private
  commit identifiers, secrets, or organization-specific source detail;
- internal links and Mermaid diagrams resolve;
- and version 1.0.0 status and limitations are honest.

## Required Report

Write a Markdown report with:

1. repository state reviewed;
2. review scope and method;
3. executive verdict;
4. your independently drafted fictional practice;
5. what the canonical extension communicates clearly;
6. blockers;
7. material findings;
8. editorial findings;
9. technology-neutrality assessment;
10. human-and-AI understandability assessment;
11. example and structure assessment;
12. privacy and publication-safety assessment;
13. repository-consistency assessment;
14. recommended dispositions;
15. and an explicit statement of what you did not validate.

Classify findings:

- **Blocker** — unsafe, contradictory, unusable, private, or materially outside
  framework boundaries.
- **Material** — meaningful ambiguity or incompleteness that should be corrected
  before publication.
- **Editorial** — limited clarity, navigation, or wording issue.

Do not describe the example as a validation suite, proof, certification, or
implementation requirement. Do not claim domain validation from your review.

Sanitize the report before sharing it. Do not include local filesystem paths,
usernames, credentials, private source material, or unrelated repository
content.
