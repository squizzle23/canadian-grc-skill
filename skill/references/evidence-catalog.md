# Evidence Catalog — Per-Regulator Examination Expectations

Regulatory examinations are not SOC 2 audits, but the evidentiary logic is the same. This catalog gives you a concrete inventory of what each regulator typically expects in an examination or audit, so you can prepare clients to be ready before the supervisory letter lands.

## Universal principles (apply to every regulator)

Evidence must be:

1. **Contemporaneous** — generated at the time the control operated. A log entry created at 10:47 AM on the day the access review happened is contemporaneous. A retroactive certification "the access review was done in Q2" reconstructed after an examination notice is not.

2. **Complete** — covers the full examination period, with no unexplained gaps. If monthly vulnerability scans are a control, the examiner expects 12 months of scan records — missing September is an issue.

3. **Attributable** — shows who performed the action and when, with immutable or signed records. "The patch was applied" is insufficient. "Engineer J. Smith applied patch KB5034123 to host PROD-DB01 on March 14, 2025 at 14:22 UTC per change record CR-2025-0314-007" is attributable.

4. **Consistent** — demonstrates the control is repeatable and routinely operated, not staged for the examination. A sudden spike in access reviews starting two weeks before an examination announcement is a red flag.

## OSFI examination evidence

OSFI supervisors are among the most sophisticated in Canada. Evidence expectations are shaped by the specific guideline (B-10, B-13, E-21) and by the FRFI's size and complexity.

### For B-10 third-party risk

- **Third-party inventory** with risk tier, criticality, and service description for every arrangement (not just material).
- **Due diligence files** for every material arrangement, with documented risk assessments and decision records.
- **Continuous monitoring records** for all arrangements — this is the post-2023 change. Monitoring frequency should match criticality.
- **Contract review evidence** showing contractual provisions for security, privacy, exit, subcontracting, right-to-audit.
- **Concentration risk analysis** at the portfolio level.
- **Subcontracting records** showing visibility into n-tier supply chain.
- **Exit and contingency plan documentation** for critical arrangements.
- **Board and executive reporting** on TPRM — quarterly cadence typical; annual minimum.

### For B-13 technology and cyber risk

- **Cyber risk register** with threats, vulnerabilities, likelihood, impact, and treatment.
- **Board/executive reporting cadence** — typically quarterly board briefings with material incidents reported immediately.
- **Asset inventory** — covering all technology assets in scope, with classification and ownership.
- **Patch and vulnerability records** — scan results, remediation timelines, exceptions with risk acceptance.
- **Incident log** with B-13 Advisory classification, timeline, and reporting evidence (notifications to OSFI and OPC).
- **Tabletop exercise records** and lessons-learned documentation.
- **I-CRT test reports** (if applicable) with RTP and TIP deliverables.
- **Change and release records** demonstrating control gates per 2.5.
- **DR test results** demonstrating 2.9 recovery capability.

### For E-21 operational resilience

- **Critical operations list** with rationale.
- **Impact tolerance statements** for each critical operation (the maximum tolerable disruption).
- **Scenario test results** testing against impact tolerances.
- **Dependency mapping** — technology, third-party, and process dependencies for each critical operation.
- **BCM and DR test evidence** coordinated with E-21 framing.

### For I-CRT (where applicable)

- **I-CRT scope documentation** — CBFs in scope.
- **Control Group records** — minutes, decisions, operational secrecy evidence.
- **TIP deliverables** — threat scenarios, TTPs, attack paths.
- **RTP execution logs and findings.**
- **Closure phase replay** — purple team exercise evidence.

## FSRA examination evidence

FSRA applies proportional supervision. Larger Ontario credit unions can expect OSFI-level scrutiny; smaller entities get lighter treatment. Evidence expectations align with the seven Practices.

### Practice 1 — Governance
- Board charter or policy assigning IT risk oversight.
- Evidence of board reporting on IT risk.
- Organizational chart with IT risk roles defined.

### Practice 2 — Risk management
- Written IT risk management framework.
- IT risk register.
- Risk appetite statement covering IT risk.
- Periodic risk assessments with sign-off.

### Practice 3 — Data management
- Data classification policy and inventory.
- Data lifecycle management evidence (retention, destruction).
- Access controls evidence.

### Practice 4 — Outsourcing
- Vendor inventory with risk tiering.
- Vendor due diligence files.
- Vendor performance monitoring records.
- Exit arrangements for critical vendors.

### Practice 5 — Incident preparedness
- Incident response plan.
- Incident log with classification.
- Tabletop exercise records.
- Training and awareness records.

### Practice 6 — Continuity and resiliency
- BCP and DR plans.
- BCP test results.
- RPO/RTO definitions.

### Practice 7 — Notification of material IT risk incidents
- Internal materiality determination records.
- Evidence of timely notification to FSRA (email or portal records).
- Subsequent update communications.

## AMF examination evidence

AMF supervision combines ICT Guideline expectations with Incident Regulation specifics.

### For ICT Guideline
- ICT governance structure and roles documentation.
- ICT risk register with categorization per Section 1.
- ICT risk management framework covering Preparation, Treatment, Follow-up.
- Evidence of ongoing monitoring and review.

### For Incident Regulation
- **Incident management policy** (mandatory per Section 4) with escalation criteria, reporting criteria, and responsible person designation.
- **Procedures for detection, assessment, response** (Section 5).
- **Incident register** retained 5 years from end-of-incident report (Section 7).
- **E-Services submissions** for each reportable Incident.
- **End-of-incident reports** submitted within 30 days of control being re-established.
- **Board and senior management reporting** records.

### For Loi 25 (parallel)
- **Privacy officer designation** documentation.
- **PIA register** (Section 23.3) for every project triggering the PIA requirement.
- **Confidentiality incident register** (Section 23.8).
- **Consent records** per Section 14 standards.
- **Cross-border transfer assessments** (where applicable).
- **Automated decision-making disclosures** (Section 12.1).
- **Public privacy practices** publication evidence (Section 28.2).

## CIRO examination evidence

### For Rule 3703 (reportable incidents)
- Incident log with Rule 3703(1) classification determination.
- Evidence of 3-day initial notification to CIRO per 3703(2)(vii)(a).
- Evidence of 30-day follow-up per 3703(2)(vii)(b).
- Preliminary assessment, mitigation steps, contact information records.

### For broader cyber governance (guidance, not mandate)
- NIST CSF alignment mapping.
- Board cyber reporting cadence evidence.
- Tabletop and tabletop-exercise records.
- Policies aligned to the Cyber Governance Guide structure.
- Training and awareness records.
- Ransomware-specific runbook and tabletop.

## AER examination evidence

AER audits are discretionary under Reg 84 Section 3(5). Operators should be continuously ready.

- **Security Management Plan (SMP)** aligned with CSA Z246.1 for each critical facility.
- **Critical facility inventory** matching the AER's critical infrastructure list notifications.
- **Risk assessments** for each facility covering physical, cyber, and personnel security.
- **Implementation evidence** — controls actually operating, not just documented.
- **Capacity evidence** (Section 3(5)(b)) — trained personnel, budget allocation, equipment, response capability.
- **Incident records** for security incidents at critical facilities.
- **Training and drill records** covering SMP procedures.
- **Contractor and vendor SMP alignment** for third parties with physical or cyber access.
- **IT/OT segmentation evidence** for the boundary between corporate IT and OT environments.
- **Privacy overlay** (not AER-scoped but concurrent) — PIPA AB records if personal information is processed.

## PIPEDA / OPC examination evidence

- **Privacy officer designation** (Schedule 1 Principle 1).
- **Privacy policy** covering all ten principles (Schedule 1 + section 10.1).
- **Privacy notices** (Schedule 1 Principle 8 — Openness; Principle 2 — Identifying Purposes).
- **Consent records** appropriate to sensitivity (Schedule 1 Principle 3).
- **Access request log** (Schedule 1 Principle 9).
- **Complaint log** (Schedule 1 Principle 10).
- **Breach register** (Section 10.3 — every breach, not just reportable, 24-month retention).
- **Breach notifications** to OPC (10.1), individuals (10.1(3)), other organizations (10.2).
- **Safeguard documentation** per sensitivity (Schedule 1 Principle 7).
- **Retention and destruction records** (Schedule 1 Principle 5).
- **Vendor and third-party processing agreements** demonstrating continued accountability (Principle 1).

## PHIPA / IPC examination evidence

- **Custodian designation** and information practices statement.
- **Privacy officer / contact person** designation.
- **Agent agreements** for vendors and service providers (including IT/SaaS vendors handling PHI).
- **Consent records** or reliance on implied consent with documented rationale.
- **Access logs** for electronic PHI — who accessed, what record, when, why. This is a high-scrutiny item.
- **Breach register** with individual and IPC notifications where applicable.
- **Annual IPC statistics submission** records.
- **Patient access and correction request logs.**
- **HINP or electronic service provider agreements** where applicable, with audit logging.
- **Staff training records** on PHIPA duties.

## Preparation ladder (readiness model)

Use this to assess client readiness:

| Tier | Description | Indicators |
|---|---|---|
| 🔴 **Unprepared** | Evidence is not being collected systematically. Could not demonstrate a single control's operation for 12 months. | No central evidence repository; controls documented but not evidenced; last internal audit >2 years ago |
| 🟡 **Partial** | Some evidence is collected but coverage is inconsistent. Some periods have gaps; some controls have no evidence. | Quarterly-or-less evidence cadence; evidence in siloed systems; no central tracking of what evidence supports what control |
| 🟢 **Ready** | Evidence is contemporaneous, complete, attributable, and consistent. Could produce full 12-month coverage for any in-scope control within 48 hours. | Central evidence repository; control-to-evidence mapping; automated collection for most technical controls; quarterly internal audits |
| 🔵 **Mature** | As above, plus continuous improvement and predictive indicators. Could demonstrate trend and improvement over multiple years. | Control effectiveness metrics; predictive indicators; third-party attestations; cross-framework mappings maintained |

A typical readiness engagement moves clients from 🔴 / 🟡 to 🟢 before an anticipated examination.
