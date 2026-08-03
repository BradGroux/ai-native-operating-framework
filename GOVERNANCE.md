# Governance

**Status:** Approved initial repository governance<br>
**Founding steward:** Brad Groux<br>
**Last reviewed:** 2026-07-30

## Purpose

This document governs how the AI-Native Operating Framework is maintained
without allowing examples, implementations, teaching, commercial work, or
technology choices to redefine it implicitly.

The [charter](framework/charter.md) is the highest-authority framework document.
Accepted [decision records](decisions/README.md) explain material interpretations
and changes. Canonical framework language lives under
[`framework/`](framework/README.md).

The [framework contribution SOP](CONTRIBUTING.md) governs how proposed changes
are prepared, reviewed, decided, incorporated, and maintained.

## Current Stewardship

Brad Groux is the creator and founding steward. Until a broader governing body
is established, the founding steward:

- approves material framework changes;
- protects the charter and framework boundaries;
- accepts or rejects decision records;
- approves release baselines;
- appoints or confirms maintainers;
- records dissent and unresolved risk; and
- determines when governance should expand.

The framework is developed through
[Digital Meld](https://digitalmeld.io)'s research arm, alongside the related
[AI Dev Days](https://github.com/bradgroux/ai-dev-days) research and education
initiative. These affiliations do not grant either organization decision
authority outside this governance process.

Stewardship does not create professional authority over the domains represented
by framework examples.

## Open Framework Commons Adoption

The AI-Native Operating Framework adopts
[Open Framework Commons](https://github.com/BradGroux/open-framework-commons)
[`v1.0.0`](https://github.com/BradGroux/open-framework-commons/tree/v1.0.0),
release commit
[27870fb1d57d951b9ef5a3a86f33ef0&#54;8ee557da](https://github.com/BradGroux/open-framework-commons/commit/27870fb1d57d951b9ef5a3a86f33ef0%368ee557da).
Commons is shared ecosystem context, not a parent framework, certification,
implementation layer, or governing authority over this framework.

| Disposition | AI-Native alignment |
|---|---|
| Adopted shared principles | All nine Commons principles are adopted: people first; own the method and rent the tool; play the long game; contribute before extracting; steward what matters; keep products independent; build in the open; learn honestly; and use technology as an amplifier. |
| Product-local guidance | The charter, six concerns, eight SOP content areas, shared operating memory standard, six maintenance activities, terminology, examples, research, contribution process, governance, roadmap, releases, and implementation choices remain owned here. |
| Deferred shared principles | None for Commons `v1.0.0`. |
| Explicit deviations | None for Commons `v1.0.0`. |

The people-first principle means that people supply business purpose, judgment,
and accountability. It does not narrow this framework's approved meaning of
AI-native work: people and AI may both perform work under the same standards,
with explicit accountable human ownership. The contribute-before-extracting
principle is an ecosystem value, not an additional contribution prerequisite,
commercial restriction, business concern, SOP content requirement, or method
activity.

No material conflict with Commons `v1.0.0` is recorded. If a later Commons
revision appears to conflict with this framework, the conflict must remain
visible until the responsible authority decides whether to adopt, defer, or
deviate. A Commons change never amends this framework automatically.

## Decision Flow

```mermaid
flowchart LR
    P["Written proposal"]
    R["Review against charter,<br/>framework, and evidence"]
    D{"Decision"}
    A["Accept<br/>record rationale"]
    V["Revise or defer<br/>name unresolved work"]
    X["Reject<br/>record reason"]
    U["Update canonical documents<br/>and affected examples"]
    L["Release through an<br/>identifiable version"]

    P --> R --> D
    D --> A --> U --> L
    D --> V --> P
    D --> X
```

No document changes framework meaning merely by being published. A material
change requires an explicit decision and corresponding update to the canonical
documents.

## Decision Classes

### Charter Amendment

A charter amendment follows the amendment requirements in the
[charter](framework/charter.md). It requires a written proposal, review against
the mission and commitments, an accountable decision, disclosure of material
dissent, an effective date, and change history.

### Material Framework Decision

A material decision changes or interprets:

- the six business concerns;
- the SOP content standard;
- the shared operating memory standard;
- the standards maintenance method;
- approved framework language;
- framework scope or non-goals;
- accountability or authority expectations; or
- the relationship between framework core and examples.

It requires a decision record under [`decisions/`](decisions/README.md).

### Governance Change

A material change to stewardship, decision authority, contribution, conflict or
appeal handling, release approval, or governance review requires a written
decision by the founding steward or future governing body. The decision records
the reason, affected responsibilities, effective date, transition conditions,
and material dissent.

### Example Decision

Examples follow [`examples/CONTRIBUTING.md`](examples/CONTRIBUTING.md). The
framework maintainer may accept an example only as an illustration. Domain
review affects the example's stated review status; it does not amend the
framework.

### Editorial Decision

A maintainer may accept non-material corrections without a decision record.
When the effect on meaning is uncertain, use the material decision path.

## Review Participation

Review should involve the people needed for the consequence of the change:

- accountable framework ownership;
- affected standards authors and maintainers;
- practitioners who understand the represented work;
- domain or control authorities for professional claims;
- and contributors or readers affected by compatibility or clarity changes.

AI may assist with drafting, comparison, link checking, and review. It does not
hold governance authority or substitute for domain expertise.

## Community Feedback Loop

```mermaid
flowchart LR
    F["Feedback received"]
    T["Record context, evidence,<br/>and requested outcome"]
    C{"Triage"}
    E["Editorial or<br/>example matter"]
    P["Material framework<br/>proposal"]
    X["Outside scope or<br/>insufficiently supported"]
    D{"Accountable decision"}
    U["Update canonical material<br/>and affected examples"]
    R["Record disposition<br/>and respond"]
    O["Observe effects<br/>and new evidence"]

    F --> T --> C
    C --> E --> D
    C --> P --> D
    C --> X --> R
    D -- "Accept" --> U --> R
    D -- "Revise, defer,<br/>or reject" --> R
    R --> O
    O -. "new feedback" .-> T
```

Feedback may arrive through any channel designated by the steward, but it
enters framework governance only when its context, evidence, and requested
outcome are recorded. Every reviewed item receives a recorded disposition.
Accepted changes follow the appropriate decision class, return through an
identifiable release, and are observed for their effects. Rejection or deferral
also records the reason so the same question is not repeatedly rediscovered.

## Releases and Versions

An approved release identifies:

- the exact repository version;
- effective date;
- material changes;
- known limitations and review status;
- superseded versions;
- and the responsible steward.

Draft work must remain visibly distinct from an approved release. Publication
requires explicit authorization. Repository content and submitted contributions
are licensed under the [MIT License](LICENSE.md).

Before release, verify local links and headings, canonical framework invariants,
example coverage, diagrams, release metadata, publication safety, and secret
scanning through the repository's repeatable validation gate. Record any
unavailable check and its consequence rather than representing it as passed.
The version 1.0.0 transition is recorded in the approved
[prepublication release-hardening decision](project/planning/prepublication-release-hardening-decision-2026-07-30.md).

The current intake destination, responsible maintainer, receipt method, and
alternate route are maintained in the
[framework contribution SOP](CONTRIBUTING.md) and surfaced in the repository
[README](README.md).

### Prepared Release Baseline

The approved initial release baseline is:

- **Version:** 1.0.0
- **Effective date:** 2026-07-30
- **Repository version:** annotated tag `v1.0.0`
- **Material changes:** recorded in the [changelog](CHANGELOG.md)
- **Known limitations:** all examples are illustrative and not
  domain-validated; two source-bounded independent AI reviews of the shared
  operating memory extension are complete, but the standard has not received
  human records, privacy, security, legal, knowledge-management, or
  business-continuity review; organizational use and broader governance have
  not been exercised
- **Superseded public version:** none
- **Responsible steward:** Brad Groux
- **Publication destination:**
  [`github.com/bradgroux/ai-native-operating-framework`](https://github.com/bradgroux/ai-native-operating-framework)

## Conflicts and Appeals

Conflicting interpretations are recorded and escalated to the founding steward
or future governing body. Material dissent should remain visible with the
decision rather than being removed from history.

An appeal follows the [framework contribution SOP](CONTRIBUTING.md). It
identifies the disputed contribution and decision, grounds, evidence, and
requested resolution. The appeal and original decision remain visible together.

Appeals of maintainer decisions go to the founding steward or future governing
body. When the founding steward made the disputed decision and no broader
governing body exists, the steward conducts a documented reconsideration with
an uninvolved reviewer when practical and records that governance limitation.
The appeal disposition identifies the authority, reasoning, date, and resulting
action and is communicated to the contributor and affected maintainers.

## Governance Review

Review this document when:

- participation materially expands;
- maintainers or decision authorities change;
- repeated contribution or appeal problems occur;
- a release exposes unclear authority;
- licensing or publication changes;
- or the founding steward proposes a broader governing body.
