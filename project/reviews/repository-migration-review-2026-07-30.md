# Repository Migration Review

**Status:** Complete<br>
**Review date:** 2026-07-30<br>
**Accountable role:** Release maintainer<br>
**Scope:** Migration from the iCloud delivery workspace into the canonical
`ai-native-operating-framework` repository

> **Scope note:** This review predates the shared operating memory extension.
> References to ten examples and the migrated package describe the repository
> state reviewed at that time.

## Outcome

The completed Stage 2 package has been reorganized as a durable framework
repository. Canonical framework content, illustrative examples, accepted
decisions, and development records now have distinct locations and authority.

The migration changes organization and navigation. It does not change the
approved definition, six concerns, eight SOP content areas, six maintenance
activities, or the meaning of any example.

## Placement

| Content | Canonical location | Role |
|---|---|---|
| Framework charter, standard, method, and glossary | `framework/` | Defines the framework |
| Complete example SOPs and contribution SOP | `examples/` | Illustrates the framework |
| Accepted decision records | `decisions/` | Preserves material rationale |
| Specifications, planning, reviews, research, and superseded material | `project/` | Preserves development context |
| Framework contribution SOP and governance policy | Repository root | Governs changes |

## Visualization Layer

Mermaid diagrams are embedded only where a visual makes a relationship,
sequence, branch, or handoff materially easier to understand:

- repository and framework hierarchy;
- framework-contribution, community-feedback, and example-contribution flows;
- the six framework concerns;
- the eight SOP content areas and the SOP feedback loop;
- the standards maintenance method; and
- one procedure overview in each of the ten examples.

The surrounding prose remains authoritative. Diagrams summarize the documents;
they do not create requirements or prescribe a universal business lifecycle.

## Verification Results

- The repository contains 49 Markdown documents across the canonical framework,
  examples, decisions, contribution and governance policy, and project records.
- All current local Markdown links and heading references resolve. Superseded
  history is intentionally excluded from the portability gate.
- The canonical framework retains the approved vocabulary and explicitly keeps
  technology implementation outside its scope.
- All ten examples contain the eight SOP content areas, six-concern annotation,
  provenance, review status, and domain-specific boundary.
- All 20 Mermaid blocks rendered successfully with Mermaid CLI 11.12.0 and
  Google Chrome.
- The repository is initialized on `main`, and the complete repository tree is
  preserved in reviewable local Git history.

## Remaining Decisions

- Final owner approval is pending.
- All examples remain illustrative and not domain-validated.
- No public license has been selected or granted.
- No remote repository has been configured.
- Publication has not been authorized or performed.
