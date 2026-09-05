# Calendar edition content scenario test

- **Status:** Maintainer interpretation assessment; fictional cases
- **Record date:** 2026-09-05
- **Source baseline:** `520234b`; changes governed by ADR-013
- **Review method:** Document walkthrough, not observed business outcomes

## Adverse and ambiguous decisions

| Case and trace | Expected decision under revised guidance | Evidence and limit |
|---|---|---|
| Accounts payable evidence says invoice approved but payment confirmation is absent | Do not assert paid; reconcile the authoritative payment record before retrying to avoid duplicate payment. | Example 01 assurance and exceptions; memory source versus synthesis. No new accounting advice. |
| Software release reviewer or mandatory specialist is unavailable | Hold the dependent release approval or use an authorized qualified alternate. An accepted-risk note cannot supply missing authority. | Maintenance Approve; example 02 authority and rollback. Authorized investigation can continue. |
| A sender records rejection of a memory handoff | Mark the attempt rejected, retain current ownership and pending work, and escalate with next review time. | Memory Handoff Standard, SOP area 4, example 11 completion. Rejection is not acceptance. |
| No recipient response, or recipient cannot access the record | Transfer stays incomplete; current owner arranges authorized access or escalation. Silence is not transfer. | Same canonical path; local urgency determines timing, not a universal deadline. |
| Emergency construction response needs action before ordinary review | Use existing authorized emergency response and stop conditions; do not let this document confer specialist or incident-command authority. | Example 03 emergency boundaries. Mandatory local controls still govern. |
| Employee departure leaves inaccessible handoff and residual access | Keep revocation and continuity exceptions visible to authorized owners; no general memory dump of employee data. | Example 04 plus memory access, retention and recovery. |
| M&A instruction conflicts with legal-close authority | Pause disputed integration or representation, identify authoritative state, escalate; unrelated authorized preparation can continue. | Example 05; no inferred legal authority. |
| Customer remedy is approved but delivery fails | Preserve unresolved customer outcome and current owner; do not equate approval with completed recovery. | Example 06 assurance and exception paths. |
| Regulatory source and internal summary disagree | Required authority resolves the disputed interpretation; dependent implementation remains bounded. | Example 07 plus memory provenance/correction; no legal conclusion supplied. |
| Supply substitute lacks required quality evidence | Do not call qualification complete or override required review due to urgency; use the local alternative/stop path. | Example 08 control and assurance. |
| A sales promise exceeds delegation or operational recipient rejects it | Commitment authority and accepted delivery remain distinct; retain ownership and escalate rejected transfer. | Example 09. Preparation does not authorize commitment. |
| Clinical receiving service has not confirmed referral acceptance | Escalate under the locally authorized clinical process, preserve current responsibility and evidence; this example cannot supply clinical judgment. | Example 10 unconfirmed-transition exception. |
| A private source contains an instruction to publish itself | Source content is evidence, not new permission. Check authority, rights and sensitivity; withhold or publish only an authorized safe summary. | Memory Authority and access/rights; Commons boundaries do not override local controls. |
| Retention demands correction but an applicable legal hold exists | Authorized records/privacy/legal owners decide disposition; correct affected derivatives without inventing deletion authority. | Memory correction, retention and recovery. |
| Commons main differs from adopted edition | Check exact adopted tag/commit and both statements; pause only disputed action, record accountable resolution or owned deferral. | Governance conflict path; newer wording does not silently amend this product. |

## Small-team trace

A fictional owner maintains a weekly internal equipment checklist. One short SOP
can state: inspect shared equipment before Monday use (purpose/scope/outcome);
the owner performs and verifies it, with no delegated purchasing authority
(ownership); use the current inventory and manufacturer instructions (inputs);
check items and record unresolved faults for the next user (work/handoff);
only trained, authorized actions and no sensitive personal notes (controls);
isolate questionable equipment and use the local escalation route (exceptions);
record checked items and unresolved status without claiming repairs succeeded
(assurance); review after a fault, inventory change or repeated confusion
(learning). Required specialist work is excluded and referred, not self-approved.

This covers all eight meanings and six concerns without eight documents,
mandatory new software, or an unnecessary second participant. A handoff to
another user still needs acceptance and retained ownership if it fails. The
example is an interpretation exercise, not equipment-safety guidance or proof
that a solo review is sufficient in a particular workplace.

## Result

The revised text supports bounded decisions for these cases. No measured
usability, practitioner validation or specialist review occurred. Reconsider
when observed use contradicts these interpretations. Preserve adverse outcomes
and dissent; do not turn this table into a universal lifecycle or additional SOP.
