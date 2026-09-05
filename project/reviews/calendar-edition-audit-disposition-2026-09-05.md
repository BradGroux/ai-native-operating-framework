# Calendar edition audit disposition

- **Status:** Remediated candidate; final merge and publication require readback
- **Record date:** 2026-09-05
- **Baseline:** `520234b` (released v1.1.0)
- **Accountable authority:** Brad Groux; direct audit, remediation and release instruction
- **Review method:** Source inspection, fictional adverse cases, independent document reviews and executable checks

## Scope and priority

Inspected the tracked public repository: charter, canonical method and memory,
all eleven examples and structural companion, contribution/research/decision
templates, governance/security/conduct, accepted decisions, historical reviews,
planning/history, citation/release records, scripts and CI. Remote releases,
issue 17–21 dispositions, earlier tag-correction PRs and latest release PRs were
checked against Git history. A dirty primary checkout was preserved; changes
start from released remote main in an isolated worktree.

Substantive content came first. No application, service, API, database, business
runtime, concurrent worker, production package or deployment exists here.
Runtime architecture/performance/resource/persistence categories are therefore
not applicable. The actual executable surface is documentation validation and
release operations; Git supplies persistence, local artifacts are temporary,
GitHub supplies CI and publication, and the scripts hold no business credentials.

## Issue disposition

| Issue | Evidence, priority and disposition | Acceptance evidence |
|---|---|---|
| [24](https://github.com/BradGroux/ai-native-operating-framework/issues/24) | Requested migration/adoption: hardcoded 1.1.0 and semantic governance at baseline. Prospective calendar editions and exact Commons adoption under ADR-013. | Active metadata, release runbook and verifier; final release readback is separate. |
| [25](https://github.com/BradGroux/ai-native-operating-framework/issues/25) | Verified P2 contradiction: example 11 completion accepted rejection, while its rejection branch retained sender ownership. | Canonical memory/SOP and example now distinguish attempt from accepted transfer; rejection, no-response and access-failure cases. |
| [26](https://github.com/BradGroux/ai-native-operating-framework/issues/26) | P2 plausible ambiguity: maintenance Validate permitted deferral but did not bound use when mandatory review is missing. | Owned deferral, affected-use restriction, qualified alternate or hold, no invented waiver authority. P3 solo peer-review ambiguity also clarified. |
| [27](https://github.com/BradGroux/ai-native-operating-framework/issues/27) | Verified P2: CFF prefix values passed exact-version intent; existing unpublished link targets could pass. | Exact scalar/date and current-surface checks, indexed link targets, fenced-heading exclusion and negative/future-edition regressions. |
| Historical 17, 18, 21 | Resolved by v1.1.0; application wording and forward-only immutability retained. Only prospective numbering superseded. | Original decisions and release records unchanged. |
| Historical 19, 20 | Closed as accountable governance dispositions, explicitly not completed specialist or practitioner validation. Preserve that reason; do not claim the unmet evidence exists. | All examples retain status. Future engagement remains externally dependent on qualified reviewers, scope, authority and publication consent. |

## Content assessment

The [fictional scenario trace](calendar-edition-content-test-2026-09-05.md) covers
incomplete evidence, conflicting authority, delegated actions, unavailable
specialists, failed handoffs, privacy, retention, correction and recovery. The
low-risk trace shows all eight meanings without extra documents or mandatory
peer ceremony. Canonical six concerns and six maintenance activities remain
coherent; examples retain distinct lifecycles and all eight SOP areas.

Operating memory retains authority, provenance, controlled handoff, privacy,
rights, retention, derivatives, correction, recovery and technology independence.
No additional template, seventh concern or machine schema was introduced.
Existing claims are chosen commitments or bounded interpretations; no new
empirical effectiveness assertion is made. Historical reviews retain their
original limits and verdicts.

## Commons and downstream

Commons v2026.09.05 was verified through authenticated GitHub annotated-tag
readback and Git, at the exact expected commit recorded in ADR-013. Principles,
boundaries, governance, research/review, Decision 0002, adverse cases, disposition
and release procedure informed independent adoption. Shared human boundaries
align locally; no deviations or deferred shared principles. Commons-specific
implementation, all-product review duties and repository controls are not imported.

AI Dev Days master `8c1d80d` README and teaching alignment were inspected. Its
AI-Native teaching baseline and Commons adoption remain v1.0.0. Teaching
consequences are recorded in ADR-013 and release notes; no other repository is
changed. Other ecosystem methods have no direct executable consumer here and
are not imported to fill audit categories.

## Security, maintainability and accessibility

No secret exposure was identified in source inspection; redacted current/history
scans are required. Public/private reporting forms explicitly prohibit sensitive
content. Sources and synthesis never grant permission, and examples cannot
supply professional authority. CI retains read-only contents, immutable action
SHAs, full history, concurrency cancellation and a 20-minute bound. Existing
main protection requires the validation check and PR, enforces administrators,
blocks force pushes/deletion, and requires conversation resolution. No signing
requirement was found in repository policy or local tag configuration.

Validation tools have exact top-level versions and fallback archive checksums,
but transitive npm/Python resolution is not fully locked. This is a residual
reproducibility/supply-chain risk, not an established vulnerability. The resolved Mermaid CLI npm environment audit reported zero known
vulnerabilities, and pip-audit of the resolved cffconvert 2.0.0 environment
reported no known vulnerabilities on 2026-09-05. These are point-in-time
advisory checks, not locked-resolution or absence-of-vulnerability guarantees. Importing the
entire Commons toolchain was rejected as unnecessary local ceremony.

Prose, headings, portable links and surrounding diagram explanations serve
readers without depending on color or a single visual lifecycle. No diagram
meaning/layout changed; rendering and existing legibility checks remain required.
Regex link checks cover the repository's existing Markdown subset; they are not
a general CommonMark conformance claim. New link forms require review/tests.

## Review and release evidence

Independent baseline content/specification review confirmed the handoff defect,
bounded-deferral ambiguity and solo-review improvement; standards review confirmed
metadata mismatch. Final candidate review and checks will be recorded here before
merge. Review is document and source analysis, not domain/practitioner validation.
Candidate repository gate passed 13 focused tests, 82 Markdown documents,
418 local references, all 11 examples, 39 compiled/legibility-checked diagrams,
CFF schema, workflow validation and working-tree/full-history redacted Gitleaks
scans. No new diagram meaning or layout required visual inspection.

Historical readback found v1.1.0 public release notes differ from the tagged
release record. The verifier fails this comparison honestly; no historical
content is replaced. v1.0.0 has neither VERSION nor committed release notes;
its verifier reports those limits. Both annotated historical identities remain
preserved. Publication must follow the clean merged-target gate and exact
tag/release readback.
