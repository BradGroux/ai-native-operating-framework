# Independent Framework Application Test

**Status:** Complete independent review<br>
**Accountable role:** Framework owner<br>
**Review role:** Independent AI reviewer<br>
**Review date:** 2026-07-30<br>
**Repository state:** Pre-publication development snapshot; private commit
identifier removed during public-history sanitization<br>
**Sanitization status:** Reviewed for repository inclusion; contains no real
person, organization, vendor, transaction, contact detail, credential,
confidential source material, or private operating record

> **Scope note:** This review predates the shared operating memory extension
> accepted under
> [ADR-007](../../decisions/0007-shared-operating-memory.md). References to ten
> examples and the reviewed framework state remain point-in-time findings.

## Review Scope and Method

This review tested the AI-Native Operating Framework as a business operating
framework and method. It did not treat the framework as a software
specification, agent harness, technical protocol, product, or conformance
system.

The review used only repository content. The core documents were read in this
order:

1. [Charter](../../framework/charter.md)
2. [Operating framework](../../framework/operating-framework.md)
3. [SOP content standard](../../framework/sop-content-standard.md)
4. [Standards maintenance method](../../framework/standards-maintenance-method.md)
5. [Glossary](../../framework/glossary.md)
6. [Governance](../../GOVERNANCE.md)
7. [Framework contribution SOP](../../CONTRIBUTING.md)

The illustrative vendor-management SOP was drafted from those core documents
before any example SOP was read. The example review then covered:

- [Example collection guidance](../../examples/README.md);
- [Example contribution SOP](../../examples/CONTRIBUTING.md);
- [Accounts-payable invoice processing](../../examples/01-accounts-payable-invoice-processing.md);
- [Construction field-incident response](../../examples/03-construction-field-incident-response.md);
  and
- [Patient referral and care transition](../../examples/10-patient-referral-care-transition.md).

No prior project memory, author briefing, or external source informed the test.

## Executive Verdict

**Usable with clarifications.**

The core is coherent and usable as a business operating framework and method.
It provided enough direction to write a complete illustrative vendor-management
SOP without prescribing software, a universal lifecycle, or a mandatory
document template. It also forced unresolved vendor-domain decisions into the
open instead of supplying invented precision.

There are no blockers. Two material issues remain:

1. The example collection creates a strong de facto template signal even though
   the core explicitly says headings are not prescribed.
2. The framework contribution loop explains triage and decision handling but
   does not identify the current intake channel or an operational appeal path.

The corpus is visibly draft and pending owner approval, so "usable" here means
usable for application, evaluation, and organizational adaptation. It does not
mean the repository is already an approved operational standard
(`README.md:70-83`; `framework/charter.md:3-5`).

## Core Understanding

### What the Framework Requires

- Examine business work through six concurrent concerns: Intent,
  Responsibility, Work, Control, Assurance, and Learning. They are concerns
  around the work, not phases
  (`framework/operating-framework.md:20-31,59-61`).
- Preserve explicit accountable human ownership, identify participants, and
  bound decision, approval, separation-of-duty, and escalation authority. AI
  participation cannot create an accountability gap
  (`framework/charter.md:65-74`;
  `framework/operating-framework.md:91-106`).
- Make all eight SOP content areas clear regardless of layout: outcome and
  scope; roles and authority; trigger and sources; work and handoffs; controls
  and risk; exceptions and recovery; completion and evidence; and maintenance
  and change (`framework/sop-content-standard.md:25-38,73-196`).
- Describe normal work, decisions, dependencies, handoffs, authoritative work
  state, resumability, exceptions, escalation, stop conditions, recovery,
  verification, and evidence
  (`framework/sop-content-standard.md:106-180`).
- Maintain standards through Understand, Document, Validate, Approve, Use, and
  Improve. Those activities maintain documentation and operating standards;
  they are not a lifecycle imposed on the business process
  (`framework/standards-maintenance-method.md:7-22`).
- Validate against realistic normal, exception, failure, and recovery scenarios
  before approval (`framework/standards-maintenance-method.md:178-238`).
- Make feedback consequential through a named maintainer, review triggers,
  accountable change decisions, communication, and preserved history
  (`framework/sop-content-standard.md:182-220`).

### What the Framework Permits

- Any structure, language, medium, or supporting material that communicates the
  required business meaning
  (`framework/sop-content-standard.md:7-14,222-235`).
- Proportionate depth, controls, review, and role separation based on
  consequence, reversibility, exposure, complexity, and reliance
  (`framework/sop-content-standard.md:237-254`).
- Existing domain lifecycles and governance rather than a framework-imposed
  universal sequence or parallel bureaucracy
  (`framework/charter.md:88-97`;
  `framework/standards-maintenance-method.md:63-66`).
- People, AI, or both as participants under the same approved business
  standard. AI is optional; authority must be explicit
  (`framework/operating-framework.md:7-16,213-227`).
- Tool-specific instructions in an organization's current SOP when needed,
  without turning them into framework requirements
  (`framework/operating-framework.md:246-259`).
- Combining roles when scale, risk, and separation-of-duty needs permit
  (`framework/standards-maintenance-method.md:78-110`).

### What the Framework Excludes

- Software specifications, schemas, APIs, protocols, harnesses, adapters,
  models, machine representations, or technical conformance
  (`framework/charter.md:127-141`; `framework/glossary.md:95-99`).
- A universal business lifecycle, mandatory SOP template, or separate AI
  operating model (`framework/charter.md:127-141`;
  `framework/operating-framework.md:63-71`).
- Replacement of law, professional judgment, management systems, or
  organizational policy; certification; or a guarantee that a procedure is
  lawful, safe, or effective (`framework/charter.md:127-141`;
  `framework/sop-content-standard.md:330-335`).
- A requirement to use AI in every process (`framework/charter.md:127-141`).

### Contradictions and Interpretation Limits

No direct contradiction was found among the seven core documents.

Three items require interpretation:

- **Proportionality** is intentionally judgment-based. The documents give
  factors, not universal thresholds. An organization must supply its own risk
  appetite and authority matrix.
- **Authoritative source**, acceptable evidence, and bounded AI decision
  authority are clear concepts but necessarily organization- and
  domain-specific.
- The charter includes temporary and exceptional programs in scope
  (`framework/charter.md:45-53`), while the glossary defines an SOP as a
  procedure for recurring work (`framework/glossary.md:69-75`). A reasonable
  interpretation is that temporary work may use a business standard while
  reusable activities use an SOP, but the distinction is not stated directly.

## Application Result

# SOP: Govern a Third-Party Business Vendor from Need Through Exit

**Status:** Illustrative draft; not approved and not domain-validated<br>
**Accountable owner:** A named human Accountable Vendor Owner for each
vendor<br>
**Procedure maintainer:** Human Vendor Governance Owner<br>
**Approval status:** Pending organizational, legal, financial, privacy,
security, safety, compliance, and procurement review as applicable<br>
**Technology:** Tool-independent; named records may be kept in any approved
medium

## Illustrative Assumptions and Unresolved Domain Decisions

The following are invented scenario choices, not framework requirements:

- The organization assigns a human Accountable Vendor Owner and a Vendor
  Coordinator.
- Vendors are classified into locally defined risk bands. The bands, criteria,
  and approval thresholds are not supplied here and must come from approved
  organizational policy.
- Legal, finance, procurement, privacy, security, safety, compliance, records,
  accessibility, and continuity authorities participate only when the vendor's
  scope invokes their domain.
- AI may assist with collection, comparison, drafting, monitoring, and anomaly
  detection, but this illustrative SOP does not grant AI authority to bind the
  organization, approve an exception, sign a contract, authorize high-impact
  access, or attest final completion.
- Monitoring frequency, renewal lead time, evidence retention, spending
  thresholds, competitive-selection rules, and segregation requirements are
  organization-specific decisions that must be recorded before operational use.
- This SOP assumes an authoritative vendor record and an authoritative
  agreement record exist. It does not prescribe their format or system.

## Operating Outcome and Boundaries

This procedure ensures a third-party vendor is used only for a justified
business need, selected against stated criteria, approved within delegated
authority, contractually and operationally bounded, monitored for performance
and risk, and exited without leaving uncontrolled access, data, assets,
obligations, or service dependencies.

It begins when a vendor need, renewal, material scope change, performance or
risk event, or exit need is identified. It ends only when the applicable stage
has a verified disposition and accountable ownership of every residual
obligation.

In scope:

- need definition;
- candidate evaluation;
- due diligence;
- approval;
- contracting handoff;
- onboarding;
- access and data enablement;
- performance and risk monitoring;
- material change;
- renewal;
- suspension;
- termination;
- transition; and
- closure.

Out of scope:

- employee or contingent-worker management;
- payment execution;
- legal opinions;
- professional risk determinations; and
- technical configuration instructions governed by separate approved
  procedures.

Those processes may be dependencies and must return evidence to the vendor
record.

Governing requirements are the organization's current delegation of authority,
procurement, finance, conflicts, contracting, privacy, security, safety,
records, business continuity, accessibility, ethics, and regulatory policies,
plus the executed agreement and applicable law. If a required policy or
authority is missing or contradictory, the affected decision stops;
participants do not invent a substitute.

## Who Owns the Outcome and Who May Decide

| Role | Responsibility and bounded authority |
|---|---|
| Accountable Vendor Owner — human | Owns the business outcome from request through closure; defines need, recommends selection, accepts operational performance, and owns remediation and continuity. Cannot waive another control authority's requirement or bind the organization outside delegated authority. |
| Vendor Coordinator | Maintains work state, gathers evidence, coordinates reviews and handoffs, checks completeness, and tracks conditions. May not convert missing approval into implied approval. |
| Requester and practitioners | Define operational requirements, evaluate suitability, and report performance. They may not approve their own conflict or exceed delegated spend authority. |
| Procurement or commercial authority | Determines required sourcing practice, evaluates commercial terms, and approves within delegated authority. |
| Budget or finance authority | Confirms funding, financial exposure, tax and payment prerequisites, and spend approval. |
| Legal or contract authority | Determines acceptable legal terms and who may execute an agreement. Only an authorized human signatory may bind the organization under this illustrative SOP. |
| Control authorities | Decide matters within their assigned privacy, security, safety, compliance, records, accessibility, continuity, or other professional authority. Review does not transfer their decision authority to the Vendor Owner. |
| Access, asset, and data owners | Grant, verify, change, and revoke only the approved minimum access, assets, and data use. |
| Independent verifier | Verifies controlled actions and stage completion when separation of duties or risk requires independence. The organization must define when independence is mandatory. |
| Vendor contact | Supplies vendor evidence, accepts obligations, coordinates delivery, and confirms return, deletion, or transition actions. Has no internal approval authority. |
| AI participant | May collect and compare approved facts, draft records, flag missing evidence, monitor defined measures, and recommend actions. It must identify uncertainty, preserve source references, remain within an explicit assignment, and escalate outside criteria. It may not make binding, exception, professional, or final-assurance decisions reserved above. |

Decision boundaries:

- The Vendor Owner may open an evaluation and recommend a candidate.
- Designated budget, procurement, contract, and control authorities make
  decisions only within their domains and delegations.
- Activation requires the Vendor Owner plus every required approval and control
  condition. No coordinator may infer collective approval.
- The Vendor Owner may direct routine corrective action within the agreement
  and approved policy. Material scope, data, access, price, subcontractor,
  location, service, control, or risk changes return to proportionate review and
  approval.
- The Vendor Owner or an authority responsible for an affected control may
  order suspension. Termination and external notice require the contract and
  business authorities designated by policy.
- Only the authority that owns a requirement decides an exception. AI, the
  requester, and the coordinator cannot approve their own exception.

## Starting Packet and Sources of Truth

Before candidate evaluation, record:

- the business need and expected outcome;
- accountable owner and recipients of the outcome;
- scope, service, data, access, asset, location, dependency, and exit
  expectations;
- alternatives considered, including not buying or using an existing approved
  vendor;
- budget and intended term;
- proposed evaluation criteria;
- known conflicts of interest;
- initial risk questions and required domain reviewers;
- timing constraints; and
- unresolved decisions with a named human owner and due point.

Authoritative sources are, in order appropriate to the fact:

1. approved organizational policy and delegation records for requirements and
   authority;
2. executed agreements and approved amendments for obligations;
3. records owned by the responsible control authority for risk or professional
   decisions;
4. verified vendor submissions and independent evidence for vendor claims;
5. approved operational records for access, data, assets, incidents, service,
   spend, and performance; and
6. the vendor record for current stage, owner, decisions, conditions, evidence
   references, open issues, next action, and closure state.

A proposal, chat, AI summary, unsigned draft, stale certification, verbal
instruction, or vendor marketing claim may prompt work but is not authoritative
unless an authorized owner records and adopts it through the relevant process.
Missing, conflicting, outdated, or inaccessible input is recorded as a gap,
assigned to its source owner, and pauses any decision that depends on it.

Every handoff carries the vendor identity, current stage, responsible owner,
decision requested, applicable criteria, evidence references, unresolved
conditions, deadlines, and the authority expected to act. A receiver rejects an
incomplete handoff rather than silently reconstructing it.

## The Vendor Path

### Define and Select

1. The Vendor Owner defines outcome-based requirements and approves evaluation
   criteria before comparing candidates.
2. The Vendor Coordinator identifies candidate and non-vendor alternatives
   through the sourcing practice required by policy.
3. Participants collect comparable evidence on capability, capacity, cost,
   contractual fit, financial viability, privacy, security, safety, compliance,
   resilience, accessibility, subcontracting, conflicts, reputation, and exit
   feasibility only where relevant.
4. Each authoritative reviewer records findings, limitations, required
   conditions, and the scope of their review. AI-generated or vendor-supplied
   analysis is labeled and traced to sources.
5. The evaluation compares candidates against the preapproved criteria and
   records tradeoffs, exceptions, dependencies, residual risks, and the
   no-selection alternative.
6. The Vendor Owner records a recommendation. The designated selection
   authority records approve, approve with conditions, return for more work,
   reject, or defer. Selection is not contractual authority.
7. The handoff to approval includes the need, requirements, comparison,
   due-diligence evidence, conflicts, risk decisions, required conditions,
   proposed scope and price, dependencies, and exit expectations.

### Approve and Establish the Agreement

1. Procurement, finance, legal, and invoked control authorities review only
   within their authority and record decisions and conditions.
2. Confirm the authorized budget, contracting entity, signatory, vendor
   identity, scope, price, term, renewal, performance expectations, incident and
   escalation duties, data and access restrictions, records, audit or assurance
   rights, continuity, subcontractor controls, change control, termination,
   transition, and return or deletion obligations as applicable.
3. Resolve every condition or assign it as an explicitly accepted residual risk
   to an authorized owner. An unresolved required approval is not acceptance.
4. Only an authorized human signatory executes the agreement under this
   illustrative assumption.
5. Record the approved agreement version, effective dates, required reviews,
   named owners, monitoring plan, onboarding conditions, and exit obligations.
6. Do not allow vendor work, organizational data, privileged access, or binding
   commitment before the required agreement and approvals exist, except through
   a time-bounded emergency exception approved by the authorities who own the
   affected requirements.

### Onboard and Authorize Use

1. Confirm the exact service, users, data, assets, facilities, connections,
   dependencies, contacts, escalation route, metrics, review dates, renewal and
   termination dates, and exit plan.
2. Translate approval conditions into assigned onboarding tasks with owners and
   evidence.
3. Provide only the minimum approved access, data, assets, information, and
   authority. Access and data owners independently verify high-impact grants
   where policy requires.
4. Give the vendor and internal participants the approved operating, privacy,
   security, safety, incident, communication, record, and change expectations
   relevant to their work.
5. Test service acceptance, critical controls, support and escalation paths,
   monitoring evidence, continuity arrangements, and offboarding feasibility
   proportionately.
6. Record a baseline inventory of access, data, assets, obligations,
   dependencies, measures, conditions, and responsible owners.
7. The Vendor Owner authorizes operational use only after required verifiers
   confirm readiness. A successful account creation, data transfer, or first
   transaction is activity, not proof of complete onboarding.
8. Handoff to ongoing operation includes the agreement, current scope, contacts,
   inventory, measures, risks, conditions, evidence locations, issue route,
   change controls, next review, renewal decision date, and exit plan.

### Monitor, Correct, Change, and Renew

1. At the approved risk-based cadence, review business outcome, service quality,
   agreement performance, spend, complaints, incidents, control evidence,
   access, data and asset inventory, financial or continuity concerns, expiring
   evidence, subcontractor or ownership changes, and unresolved conditions.
2. Compare results to approved criteria and classify them as within tolerance,
   correctable deviation, material breach or risk, or changed scope. Record the
   basis and authority.
3. Assign corrective actions with owner, due point, verification, escalation,
   and consequence. Repeated or overdue deviations trigger earlier risk and SOP
   review.
4. A material change to scope, price, term, data, access, assets, location,
   subcontracting, control, service dependency, or risk must not take effect
   until proportionately reevaluated, approved, and incorporated into the
   authoritative agreement and vendor record.
5. Incidents follow the responsible incident process. The Vendor Owner preserves
   the link, resulting decision, vendor action, and impact on continued use.
6. Before renewal or material extension, reassess continuing need, alternatives,
   accumulated evidence, open conditions, performance, risk, agreement terms,
   transition cost, and exit readiness. Record continue, remediate, renegotiate,
   replace, offboard, or defer. Renewal requires the authority appropriate to
   the resulting commitment and risk.

### Suspend, Offboard, and Close

1. Trigger offboarding upon end of need, expiry, non-renewal, replacement,
   termination, material breach, unacceptable risk, vendor failure, or an
   authorized business decision.
2. The Vendor Owner establishes the continuity and transition plan, service stop
   point, affected people and processes, communications, contractual notice,
   data and work transfer, residual obligations, and responsible authorities.
3. Only an authorized role sends binding termination or external notice. Urgent
   containment may suspend affected use while formal decisions proceed.
4. Stop new work and scope growth; revoke access and authority at the approved
   time; recover organizational assets; disable dependencies and connections;
   transfer required work and records; and settle only authorized financial
   obligations.
5. Obtain and evaluate required evidence of data return, deletion, retention, or
   continuing lawful custody. Unverified vendor assertion is not sufficient
   where independent evidence is required by policy or risk.
6. Communicate the approved transition to affected participants and recipients,
   including the current owner of any service, data, dispute, claim, retention,
   confidentiality, audit, or regulatory obligation.
7. A verifier checks the final access, data and asset inventory, service
   transition, agreement disposition, outstanding financial items, records,
   notifications, and residual obligations.
8. Close the vendor only when all completion criteria are met. Any residual
   obligation remains open with a named human owner, evidence, due point, and
   review trigger. The Vendor Owner remains accountable until transfer or
   closure is verified.
9. Record outcome, failures, exceptions, lessons, and required improvements.

## When Work Diverges

| Condition | Required response and authority |
|---|---|
| Missing, conflicting, stale, or inaccessible source | Pause the dependent decision; record the gap; source owner resolves or an authorized authority accepts a documented limitation. |
| Required approver unavailable | Use only a formally delegated alternate. Do not infer approval, substitute a reviewer, or let timing pressure weaken the gate. |
| Urgent vendor need | The authorities owning the affected requirements may approve a restricted, time-bounded exception with scope, controls, evidence, expiry, and recovery. Full review is required before extension. |
| Vendor refuses required evidence or terms | The owning authority decides whether to reject, seek alternatives, or grant a documented exception. The coordinator and AI cannot waive it. |
| Material control failure, suspected illegality, unsafe condition, fraud, data or security incident, or falsified evidence | Stop activation or suspend affected use, contain exposure, preserve evidence, invoke the responsible incident and escalation process, and reassess continued use. |
| Performance breach | Record impact, require an authorized remediation plan, verify correction, and escalate repeated, severe, or time-critical failure to suspension, replacement, or termination authority. |
| Unapproved vendor change | Hold the change or restore the last approved scope; reassess risk and approval before use. |
| Offboarding action fails | Contain continuing access, data, asset, or service exposure; keep the vendor open; escalate to the responsible control and contract authorities; retry from the last verified state; and preserve discrepancy evidence. |
| AI output is uncertain, unsupported, conflicting, or outside delegation | Do not rely on it for the decision. Route the source material and uncertainty to the responsible human authority. |
| Authorities disagree | Record both positions and the affected risk; escalate to the organizational authority empowered to resolve the conflict. The Vendor Owner may not override a control authority they do not own. |

Stop the affected stage when:

- there is no accountable owner;
- required authority is absent;
- a material identity, conflict, contract, or risk issue is unresolved;
- required evidence appears false;
- work would exceed approved scope;
- continuing may be unlawful or unsafe; or
- recovery or offboarding cannot be controlled.

For interruption or recovery, the vendor record must preserve the last verified
stage, completed decisions, evidence, unresolved conditions, current owner,
affected parties, containment, next authorized action, and due point. Resume
only after the cause is resolved or an authorized limitation is recorded.
Restore the last approved scope when practical. Reverify any decision or control
whose evidence may have been lost or invalidated.

## Proof That the Stage Is Complete

| Stage | Business completion claim | Minimum evidence and verifier |
|---|---|---|
| Selection | A suitable candidate or no-selection outcome was chosen against approved need and criteria, with tradeoffs and unresolved risk visible. | Requirements, alternatives, comparison, due diligence, conflict disclosure, reviewer limits, recommendation, and selection decision; verified by the designated selection authority. |
| Approval and agreement | The organization is authorized and prepared to enter the defined commitment. | Domain approvals, conditions, accepted risks, budget, executed agreement, signatory authority, monitoring and exit obligations; verified by contract or process authority. |
| Onboarding | The vendor can operate within approved scope and controls, and responsible participants can monitor and exit it. | Readiness decisions, access, data and asset inventory, tests, communications, contacts, measures, dependencies, conditions, and operational authorization; verified by the Vendor Owner plus required control verifiers. |
| Monitoring, change, and renewal | Current use remains justified, controlled, and within approved terms, or an authorized corrective or exit decision exists. | Measures, reviews, incidents, exceptions, corrective actions, current inventories, change and renewal decisions, approvals, and next review; verified by the Vendor Owner and invoked authorities. |
| Offboarding | Vendor activity is ended or transferred without ownerless access, data, assets, obligations, or dependencies. | Notice and decision, service transition, revocation, asset recovery, data disposition, agreement and financial disposition, communications, residual-obligation register, and final verification; verified by the Vendor Owner and required independent or control verifiers. |

Quality means records are current and attributable; sources support the
decision; approvals match delegated authority; no unauthorized commitment,
access, data use, or scope remains; conditions have owners; recipients can rely
on the stated status; and retained evidence supports the business outcome rather
than merely proving that an activity occurred.

The authoritative result is the approved stage and disposition in the vendor
record, linked to the controlling agreement and evidence. A discrepancy reopens
the affected stage, marks the claim incomplete, contains reliance where
necessary, assigns correction, and requires reverification before handoff or
closure.

Retention periods and record locations come from the organization's
authoritative policy, agreement, and law. This illustrative SOP does not invent
them.

## Keeping the Standard Current

The human Vendor Governance Owner maintains this SOP. The accountable
organizational authority approves it. Affected control authorities approve
changes to requirements they own.

The maintainer reviews:

- outcomes and stage evidence;
- practitioner and vendor feedback;
- repeated questions;
- exceptions and approval delays;
- incidents and complaints;
- audit findings;
- monitoring failures;
- renewal outcomes;
- failed offboarding;
- organizational and authority changes; and
- changed policy, law, contract practice, risk, or business need.

Review occurs at the organization-approved cadence and earlier after a material
incident, repeated exception, failed handoff or closure, control or authority
change, audit finding, evidence that vendors are not producing the intended
outcome, or participant confusion about authority or completion.

Each feedback item has context, evidence, requested outcome, owner, and
disposition. The maintainer records whether change is needed and why. Changed
business meaning reopens Understand. Revisions proceed through Document,
proportionate Validate and Approve, communication, use, and later review.
Superseded guidance is withdrawn or clearly marked. Material change history
preserves the decision, approver, effective date, affected roles and vendors,
transition conditions, and any unresolved limitation.

AI may assist with trend analysis, draft comparisons, and gap detection. It does
not approve the revision or replace practitioner, control-authority, or domain
review.

## Traceability

### Six Concerns

| Concern | Where addressed |
|---|---|
| Intent | Operating Outcome and Boundaries; stage completion claims; governing requirements. |
| Responsibility | Role and authority table; decision boundaries; stage-specific verifiers; residual ownership. |
| Work | Starting packet, sources, handoff packet, five-stage vendor path, and recorded resumable state. |
| Control | Decision boundaries, proportional reviews, minimum access and data, change control, exceptions, stop rules, and recovery. |
| Assurance | Stage completion table, quality criteria, evidence, named verifiers, and discrepancy and reopening rule. |
| Learning | Maintainer, evidence and feedback inputs, early triggers, accountable dispositions, revision, approval, communication, and history loop. |

### Eight Content Areas

| Content area | Where addressed |
|---|---|
| Purpose, scope, and expected outcome | Operating Outcome and Boundaries; Illustrative Assumptions and Unresolved Domain Decisions. |
| Ownership, participation, responsibility, and authority | Role and authority table and decision boundaries. |
| Trigger, prerequisites, inputs, and authoritative sources | Starting Packet and Sources of Truth. |
| Activities, decisions, dependencies, handoffs, and outputs | Vendor Path, handoff packet, stage dispositions, and interruption state. |
| Policies, controls, approvals, and risks | Governing requirements, authority boundaries, due diligence, change control, and control conditions. |
| Exceptions, escalation, recovery, and stop conditions | When Work Diverges table plus stop and recovery rules. |
| Completion, verification, quality, and evidence | Stage completion table, quality rule, authoritative result, discrepancy handling, and retention boundary. |
| Review ownership, triggers, and change history | Keeping the Standard Current. |

## Example Review

The examples clarified the framework by showing:

- why a business outcome must go beyond "the action happened": invoice closure
  includes the downstream result
  (`examples/01-accounts-payable-invoice-processing.md:242-246`), and referral
  completion goes beyond transmission
  (`examples/10-patient-referral-care-transition.md:91-94,281-298`);
- how domain authority can remain explicit in high-stakes work
  (`examples/03-construction-field-incident-response.md:89-112`;
  `examples/10-patient-referral-care-transition.md:96-121`);
- how authoritative work state supports resumption and prevents responsibility
  gaps (`examples/01-accounts-payable-invoice-processing.md:145-158`;
  `examples/10-patient-referral-care-transition.md:246-263`); and
- how provenance, review status, and domain boundaries prevent illustrative
  detail from becoming professional guidance (`examples/README.md:41-78`;
  `examples/CONTRIBUTING.md:191-227`).

The examples did not contradict the core in prose. No example-specific
financial, safety, clinical, timing, role, or control requirement was imported
into the vendor SOP.

The examples did expose a presentation problem: every one of the ten examples
uses the same numbered top-level sequence matching the eight content areas.
Representative instances are:

- `examples/01-accounts-payable-invoice-processing.md:65-316`;
- `examples/03-construction-field-incident-response.md:62-333`; and
- `examples/10-patient-referral-care-transition.md:69-389`.

That repeated shape conflicts with the collection's stated intent to use a
domain-appropriate layout (`examples/README.md:21-39`) and creates a de facto
template cue even though the core says matching headings are not required
(`framework/sop-content-standard.md:25-38,70-71`). The vendor SOP therefore
remains organized around its business work rather than copying that skeleton.

## Friction Log

| What was attempted | What was clear | What required interpretation | What required external domain judgment | What the framework did not answer |
|---|---|---|---|---|
| Identify core meaning before examples | Authority order, six concerns, eight areas, same standards for people and AI, human accountability, and technology independence | How much specificity is proportionate | None for understanding the method | Exact organizational thresholds, correctly outside the framework |
| Define vendor scope and outcome | Start with business outcome, boundaries, requirements, and accountable owner | Whether closure can retain residual obligations; resolved by keeping a named owner until closure | Applicable vendor law, professional duties, procurement policy, and retention | Which vendor risks and reviews the organization requires |
| Assign roles and AI authority | Roles by responsibility; explicit authority; AI cannot hide accountability | What low-impact decisions might be delegable to AI | Delegation matrix, separation of duties, and signatory authority | A universal AI permission list, correctly not supplied |
| Describe selection through offboarding | Actual lifecycle should be domain-native; include handoffs and resumable state | Stage gates and risk-based review depth | Due-diligence criteria, competitive sourcing, contract clauses, monitoring cadence, renewal lead time, and exit evidence | No vendor-specific lifecycle, correctly not supplied |
| Specify exceptions and recovery | A happy path alone is incomplete; stop, contain, restore, retry, and record | What constitutes a material change or risk | Emergency procurement authority, incident requirements, and unacceptable risk | Thresholds and escalation titles, correctly organizational |
| Define assurance | Completion must prove outcome, with verifier and evidence | When independent verification is mandatory | Audit and retention rules and acceptable assurance evidence | A universal evidence list, correctly domain-specific |
| Use the SOP feedback loop | Named maintainer, triggers, dispositions, reapproval, communication, and history | Fixed cadence versus event-driven review | Operational metrics and review cadence | No issue; the loop is actionable once roles are named |
| Report framework feedback | Classification, evidence, accountable decision, release, and disposition | Whether this evaluation is an editorial, example, or material contribution | None | Current contribution intake channel and operational appeal procedure |

## Findings

### Blockers

None.

### Material

#### M1 — The Examples Create a De Facto Mandatory-Template Signal

**Class:** Example-collection design issue, not a core framework requirement.

The core says SOPs need not use six matching headings and the content standard
says matching headings are not required
(`framework/operating-framework.md:200-211`;
`framework/sop-content-standard.md:25-38`). The example guidance says the layout
should fit the domain and annotations do not add requirements
(`examples/README.md:21-39`). Yet all ten example files use the same numbered
eight-area top-level structure. The three fully reviewed examples show it
directly at the ranges cited in the Example Review.

A reader learning by imitation could reasonably conclude that the numbered
eight-section structure is the expected template. This is material because
"meaning over templates" is a founding commitment
(`framework/charter.md:94-97`).

#### M2 — The Contribution Loop Lacks an Operational Intake and Appeal Path

**Class:** Framework and repository governance gap, not missing vendor-domain
information.

The contribution SOP says to submit through a channel designated by the
maintainer but names no current channel (`CONTRIBUTING.md:323-339`). Governance
likewise says feedback may arrive through any designated channel and then
describes what happens after it is recorded (`GOVERNANCE.md:116-146`).
"Conflicts and Appeals" says conflicts are recorded and escalated but does not
explain how a contributor initiates an appeal, who receives it, or how its
disposition is recorded (`GOVERNANCE.md:162-166`).

The internal decision flow is clear once an item exists, but a reader using only
the repository cannot complete the first operational handoff or a formal appeal
without an author or maintainer briefing.

### Editorial

#### E1 — Temporary Work Is in Scope, but the SOP or Business-Standard Choice Is Implicit

**Class:** Core terminology clarification, not a vendor-domain gap.

The charter includes temporary or exceptional programs
(`framework/charter.md:45-53`), while the glossary defines an SOP around
recurring work (`framework/glossary.md:69-75`). The framework also uses both
"business standard" and "SOP," but does not directly state when temporary work
should use one rather than the other. This did not affect the recurring
vendor-management procedure, but one clarifying sentence would remove the
edge-case ambiguity.

### Domain-Specific Unknowns That Are Not Findings

The repository cannot and should not decide the organization's vendor-risk
classes, approval and spending thresholds, required competition, applicable
laws, mandatory due diligence, signatory authority, separation of duties,
review cadence, retention periods, incident duties, contract clauses, or
acceptable residual risk. Those are missing organizational and domain inputs.
The framework correctly made them visible and prohibited silent guessing
(`framework/standards-maintenance-method.md:112-145`;
`framework/sop-content-standard.md:256-268,330-335`).

## Feedback-Loop Assessment

### SOP-Level Loop

**Actionable.**

The content standard requires a maintainer, feedback and evidence inputs, review
triggers, approval, communication, and history. It explicitly requires a
recorded accountable response rather than passive collection
(`framework/sop-content-standard.md:198-220`).

The vendor SOP assigns all of those. Decision authority and completion evidence
remain clear: the maintainer decides whether review is needed, affected
authorities approve changes they own, and a revision is not complete until
approved, communicated, in use, and historically recorded.

### Framework Contribution Loop

**Conceptually clear, operationally incomplete.**

Classification, review scope, accountable decision options, integration,
release, evidence, and disposition are strong
(`CONTRIBUTING.md:216-231,306-370,452-482`). Decision authority is explicit, and
completion is evidence-based. The missing current intake destination and thin
appeal section break end-to-end usability for an unbriefed contributor.

## Smallest Recommendations

1. **Reformat one existing example into a genuinely domain-native top-level
   structure** while retaining a concise traceability annotation. One
   counterexample is more persuasive than another disclaimer and directly fixes
   the most important risk.
2. **Add the current contribution intake route and a minimal appeal instruction**
   to `CONTRIBUTING.md` and `GOVERNANCE.md`: where to file, who acknowledges, who
   decides, and that the disposition is recorded. This is process
   documentation, not a technical protocol.
3. **Add one sentence distinguishing temporary business standards from
   recurring SOPs** in the framework's SOP relationship section or glossary.

No schema, protocol, adapter, harness integration, conformance test, or
universal vendor or business lifecycle is recommended. Missing vendor-specific
decisions belong in organization and domain documentation, not the framework.

## Direct Answers

- **Could the framework be applied without an author briefing?** Yes, for an
  illustrative, reviewable SOP. No briefing was needed to understand or apply
  the core. A briefing or repository update is still needed to know the current
  contribution intake and formal appeal route.
- **Did it help expose missing business decisions rather than encourage
  invention?** Yes. Readiness rules, assumption labeling, authoritative-source
  requirements, and the instruction to give unresolved questions owners made
  missing vendor policy, authority, thresholds, and evidence visible instead of
  inviting fabrication.
- **Did it remain independent of technology choices?** Yes. Records, sources,
  handoffs, monitoring, recovery, and evidence could be defined without
  selecting a platform, model, schema, protocol, or tool.
- **Did the examples remain illustrations rather than become requirements?**
  Textually, yes. Practically, not fully: their uniform numbered eight-section
  structure creates a template signal that can be mistaken for a requirement.
- **What is the single most important improvement?** Publish one structurally
  different, domain-native example so the collection demonstrates, rather than
  merely states, that required meaning is independent of document template.
