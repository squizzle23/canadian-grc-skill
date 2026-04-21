# OSFI — Curated Reference

Federally Regulated Financial Institutions (FRFIs) — banks, foreign bank branches, life/P&C insurers, trust and loan companies, and (where applicable) federal pensions.

This reference curates the key structure and section citations from the OSFI guidelines in the library. Use this first; load the original PDFs only when you need verbatim language for a specific section not quoted here.

## Document set (verified)

| Guideline | PDF | Date |
|---|---|---|
| B-10 — Third-Party Risk Management | `ThirdParty Risk Management Guideline.pdf` | Apr 30, 2023 |
| B-13 — Technology and Cyber Risk Management | `Technology and Cyber Risk Management.pdf` | Jul 31, 2022 |
| Advisory — Technology and Cyber Security Incident Reporting | `Technology and Cyber Security Incident Reporting.pdf` | Aug 13, 2021 |
| E-21 — Operational Risk Management and Resilience | `Operational Risk Management and Resilience  Guideline.pdf` | Aug 22, 2024 |
| I-CRT — Intelligence-led Cyber Resilience Testing Framework | `OSFIs Intelligenceled Cyber Resilience Testing ICRT Framework.pdf` | Apr 1, 2023 |

Related (BCFSA versions of OSFI guidelines, covered in their own section at the bottom):
- BCFSA Third-Party Risk Management Guideline — `third-party-risk-management-b-10.pdf`
- BCFSA Information Security Guideline — `information-security-guideline-credit-unions-insurance-trust.pdf`

---

## B-10 — Third-Party Risk Management

**Six expected outcomes (A4):**
1. Governance and accountability structures are clear with comprehensive risk management strategies and frameworks in place.
2. Risks posed by third parties are identified and assessed.
3. Risks posed by third parties are managed and mitigated within the FRFI's risk appetite framework.
4. Third party performance is monitored and assessed, and risks and incidents are proactively addressed.
5. The FRFI's third-party risk management program allows the FRFI to identify and manage a range of third-party relationships on an ongoing basis.
6. Technology and cyber operations carried out by third parties are transparent, reliable and secure.

**Section structure and principles:**

### 1. Governance

- **1.1 Accountability** — Principle 1: The FRFI is ultimately accountable for managing the risks arising from all types of third-party arrangements.
  - 1.1.1 The FRFI retains accountability for services outsourced to a third party and manages risk arising.

- **1.2 Third-Party Risk Management Framework (TPRMF)** — Principle 2: The FRFI should establish a TPRMF that sets out clear accountabilities, responsibilities, policies, and processes.
  - 1.2.1 The TPRMF is enterprise-wide and governs the lifecycle of third-party arrangements.
  - 1.2.2 The TPRMF establishes accountabilities, policies and processes for identifying, monitoring and managing third-party risks.

### 2. Management of third-party risk

- **2.1 Risk-based approach**
  - 2.1.1 Risk assessment criteria are comprehensive and scalable.
  - 2.1.2 Level of risk of third-party arrangements is assessed.
  - 2.1.3 Rigor of risk management activities matches the level of risk and criticality.

- **2.2 Risk identification and assessment** — Principles 3 (pre-arrangement risk assessment), 4 (due diligence), 5 (subcontracting risk).
  - 2.2.1 Risk assessment — including 2.2.1.1 Risk and criticality of the arrangement throughout its lifecycle.
  - 2.2.2 Due diligence — including 2.2.2.1 process, 2.2.2.2 proportionality, **2.2.2.3 Out-of-Canada arrangements are considered**.
  - 2.2.3 Concentration risk — 2.2.3.1 Concentration risk is assessed.
  - 2.2.4 Subcontracting risk — 2.2.4.1 Risks introduced by subcontracting practices are identified and understood.

- **2.3 Risk management and mitigation** — covers contractual provisions, BCM, exit strategies.

- **2.4 Monitoring and reporting** — continuous monitoring expectation. This is the core change from prior B-10: continuous monitoring applies to all arrangements, not just material ones.

### 3. Special arrangements

- **3.1 Standardized contracts** — click-through or non-negotiable contracts still require risk management.
- **3.2 No written contract** — risk management applies even without a contract.
- **3.3 Third-party arrangements with the external auditor** — special treatment.

### 4. Technology and cyber risk in third-party arrangements

- **4.1** Clear roles and responsibilities are established for technology and cyber controls.
- **4.2** Third parties comply with the FRFI's technology and cyber standards.
- **4.3** Cloud-specific requirements are established.
- **4.4** Cloud portability is considered.

**Key citable provisions:**
- Section 2.2.2.3 — Out-of-Canada arrangements (cross-border data residency)
- Section 2.2.4 / Principle 5 — FRFI is responsible for managing risk arising from subcontracting (including subcontractors of subcontractors)
- Section 2.4 — Continuous monitoring mandate
- Section 4.3 — Cloud-specific requirements

---

## B-13 — Technology and Cyber Risk Management

**Three desired outcomes (A.3):**
1. Technology and cyber risks are governed through clear accountabilities and structures, and comprehensive strategies and frameworks.
2. A technology environment that is stable, scalable and resilient. The environment is kept current and supported by robust and sustainable technology operating and recovery processes.
3. A secure technology posture that maintains the confidentiality, integrity and availability of the FRFI's technology assets.

### Domain 1 — Governance and risk management

- **1.1 Accountability and organizational structure** — roles, reporting lines, board/executive accountability.
- **1.2 Technology and cyber strategy** — strategy aligned with enterprise strategy.
- **1.3 Technology and cyber risk management framework** — enterprise-wide, comprehensive.

### Domain 2 — Technology operations and resilience

- 2.1 Technology architecture
- 2.2 Technology asset management
- 2.3 Technology project management
- 2.4 System Development Life Cycle
- 2.5 Change and release management
- 2.6 Patch management
- 2.7 Incident and problem management
- 2.8 Technology service measurement and monitoring
- 2.9 Disaster recovery

### Domain 3 — Cyber security

**Principle 14 (opens 3.1):** FRFIs should maintain a range of practices, capabilities, processes and tools to identify and assess cyber security for weaknesses that could be exploited by external and insider threat actors.

- **3.0** Confidentiality, integrity and availability of technology assets is maintained
- **3.1 Identify**
  - 3.1.1 Security risks are identified
  - 3.1.2 Intelligence-led threat assessment and testing is conducted
  - 3.1.3 Vulnerabilities are identified, assessed and ranked
  - 3.1.4 Data are identified, classified and protected
  - 3.1.5 Continuous situational awareness and information sharing are maintained
  - 3.1.6 Threat modelling and hunting are conducted
  - 3.1.7 Cyber awareness is promoted and tested
  - 3.1.8 Cyber risk profile is monitored and reported on
- **3.2 Defend**
- **3.3 Detect**
- **3.4 Respond, recover and learn**

**Common external-finding → B-13 control reference mappings:**

These are analytical mappings from externally observable security signals (TLS/SSH/DMARC/patching findings from any attack-surface tool) to the B-13 control domains they implicate.

| External finding | B-13 reference | Rationale |
|---|---|---|
| Weak TLS protocol / weak SSH cipher | 3.2 Defend | Cryptographic controls are part of the defend domain |
| Critical patching cadence lag | 2.6 Patch management | Direct match — dedicated section |
| Compromised credentials exposed externally | 3.1.5 Continuous situational awareness + 3.2 Defend | External threat intelligence + identity controls |
| Missing or permissive DMARC policy | 3.2 Defend | Email authentication is a defend-domain control |
| Expired or self-signed TLS certificate | 3.2 Defend + 2.6 Patch management | Certificate lifecycle is both a defensive and operational control |
| HTTPS missing on customer-facing domain | 3.2 Defend | Transport protection |
| Missing `Secure` cookie attribute | 3.2 Defend + 3.1.4 Data classification and protection | Session protection + data-in-transit |
| Missing Subresource Integrity (SRI) | 3.2 Defend | Supply-chain integrity |

**Related guidance (from A.4 Related guidance and information):**
- OSFI Corporate Governance Guideline
- OSFI Guideline E-21 (Operational Risk Management)
- OSFI Guideline B-10 (Outsourcing)
- OSFI Cyber Security Self-Assessment Tool
- OSFI Technology and Cyber Security Incident Reporting Advisory

---

## OSFI Advisory — Technology and Cyber Security Incident Reporting (Aug 13, 2021)

**Scope:** Applies to all FRFIs.

**Definition:** A technology or cyber security incident is "an incident that has an impact, or the potential to have an impact on the operations of a FRFI, including its confidentiality, integrity or the availability of its systems and information."

**Criteria for reporting — a reportable incident may have any one or more of:**

- Impact has potential consequences to other FRFIs or the Canadian financial system.
- Impact to FRFI systems affecting financial market settlement, confirmations or payments (e.g., Financial Market Infrastructure), or impact to payment services.
- Impact to FRFI operations, infrastructure, data and/or systems, including but not limited to the confidentiality, integrity or availability of customer information.
- Disruptions to business systems and/or operations, including but not limited to utility or data centre outages or loss or degradation of connectivity.
- Operational impact to key/critical systems, infrastructure or data.
- Disaster recovery teams or plans have been activated or a disaster declaration has been made by a third-party vendor that impacts the FRFI.
- Operational impact to internal users, and that poses an impact to external customers or business operations.
- Number of external customers impacted is growing; negative reputational impact is imminent (e.g., public and/or media disclosure).
- Impact to a third party affecting the FRFI.
- A FRFI's technology or cyber incident management team or protocols have been activated.
- An incident that has been reported to the Board of Directors or Senior/Executive Management.
- A FRFI incident has been reported to:
  - the Office of the Privacy Commissioner;
  - another federal government department (e.g., the Canadian Center for Cyber Security);
  - other local or foreign supervisory or regulatory organizations or agencies;
  - any law enforcement agencies;
  - has invoked internal or external counsel.
- A FRFI incident for which a Cyber insurance claim has been initiated.
- An incident assessed by a FRFI to be of high or critical severity, or ranked Priority/Severity/Tier 1 or 2 based on the FRFI's internal assessment.
- Technology or cyber security incidents that breach internal risk appetite or thresholds.

**When in doubt:** notification to OSFI is encouraged as a precaution.

**Initial notification timeline:** FRFIs must report to OSFI's Technology Risk Division AND their Lead Supervisor **within 24 hours, or sooner if possible**.

**Method:** in writing (electronic) to TRD-DRT@osfi-bsif.gc.ca, using the Incident Reporting and Resolution Form (Appendix II). Where details are unavailable, indicate "information not yet available" and provide best estimates.

**Subsequent reporting:** regular updates (e.g., daily) until all details provided. OSFI may change frequency based on severity, impact, and velocity.

---

## E-21 — Operational Risk Management and Resilience (Aug 22, 2024)

**Three outcomes:**
1. Operational risk management practices support operational resilience.
2. Operational risks are managed within approved risk appetite and risk limits.
3. Critical operations continue to be delivered through disruptions.

### 1. Governance
- 1.1 Senior management
- 1.2 Business and central functions
- 1.3 Independent oversight
- 1.4 Independent assurance
- Principle 1: An effective operational risk management framework and approach to operational resilience are in place.

### 2. Operational risk management
- 2.1 Operational risk management framework (Principle 2 — effective enterprise-wide ORM framework)
- 2.2 Operational risk appetite (Principle 3 — defined and adhered to)
- 2.3 Operational risk management tools (Principle 4 — comprehensive identification and assessment)
  - 2.3.1 Risk and control assessments
  - 2.3.2 Key risk indicators
- 2.4 Monitoring and reporting

### 3. Operational resilience
- 3.1 Identification and mapping
- 3.2 Establishing tolerances for disruption
- 3.3 Scenario testing

### 4. Key areas of operational risk management that strengthen operational resilience
- 4.1 Business continuity risk management
- 4.2 Disaster recovery risk management
- 4.3 Crisis management
- 4.4 Change management
- 4.5 Technology and cyber risk management (links back to B-13)
- 4.6 Third-party risk management (links back to B-10)
- 4.7 Data risk management

**Key concept:** E-21 introduces the concept of *impact tolerances* for critical operations — FRFIs must define how much disruption a critical operation can sustain before causing intolerable harm to the FRFI, its customers, or the financial system, and must test that tolerance.

---

## I-CRT — Intelligence-led Cyber Resilience Testing Framework (Apr 1, 2023)

**Applicability:** Systemically important FRFIs. Smaller FRFIs use proportionate alternatives.

**Purpose:** Threat-led red-team testing conducted using real-world TTPs to assess cyber resilience.

### Structure

- **2.1 Purpose** — framework objectives
- **2.2 I-CRT**
  - 2.2.1 What is I-CRT?
  - 2.2.2 Penetration testing vs. Red teaming vs. I-CRT
  - 2.2.3 Targeted threat intelligence
  - 2.2.4 Advanced tools, techniques and procedures
  - 2.2.5 Critical Business Functions (CBFs) in I-CRT scope
  - 2.2.6 I-CRT assessment criteria and cadence

### 3. Roles and responsibilities
- 3.1 FRFI and FRFI Control Group (CG)
- 3.2 Control Group Coordinator (CGC)
- 3.3 Regulator
- 3.4 Threat Intelligence service Provider (TIP)
- 3.5 Red Team service Provider (RTP)
- 3.6 Role of other regulators

### 4. Risk management
- 4.1 I-CRT risk owner
- 4.2 Risk considerations
- 4.3 Operational secrecy
- 4.4 Independent service providers

### 5. I-CRT process (phases)
- 5.1 Initiation phase
- 5.2 Threat Intelligence phase
- 5.3 Execution
- 5.4 Closure phase

**Key distinction (2.2.2):** I-CRT differs from standard penetration testing in that it is threat-intelligence-led (real-world adversary TTPs), covers Critical Business Functions (not just a single system), and is conducted with operational secrecy (only the Control Group knows).

---

## BCFSA Equivalents

BCFSA explicitly publishes its TPRM guideline as "a BCFSA version of a guideline published by [OSFI] titled B-10 Third-party Risk Management" adapted for BC. When advising BC-incorporated credit unions and provincial insurers:

### BCFSA Third-Party Risk Management Guideline (Oct 28, 2025, effective Jan 1, 2028)

Same outcomes and structure as OSFI B-10, adapted for BC-incorporated insurance companies. Key sections mirror federal:
- Section 1 — Governance (1.1 Accountability, 1.2 TPRMF)
- Section 2 — Management of Third-Party Risk (2.1 Risk-based, 2.2 Risk identification/assessment, 2.3 Risk management/mitigation, 2.4 Monitoring/reporting)
- Section 3 — Special Arrangements (3.1 Standardized contracts, 3.2 No written contract, 3.3 External auditor)
- Section 4 — Technology and Cyber Risk in Third-Party Arrangements
- Appendix 1 — Due diligence considerations
- Appendix 2 — Provisions for third-party agreements

**Note on effective date:** This BCFSA guideline doesn't take effect until January 1, 2028. Until then, check what BCFSA expectation currently applies and distinguish between "current" and "upcoming effective" obligations when advising.

### BCFSA Information Security Guideline (March 2025)

BCFSA-issued infosec guideline for BC credit unions, insurance companies, and trust companies. Standalone BCFSA document — not shared with FSRA as the SKILL.md previously stated.

---

## Output patterns for OSFI questions

**When asked for a B-13 gap analysis:**
1. Identify which of the three domains the question falls under (Governance, Technology Ops, Cyber Security).
2. Cite the specific sub-section (e.g., 2.6 Patch management, 3.1.3 Vulnerabilities).
3. Quote the relevant principle number if one applies (Principles 14–17 cover Domain 3).
4. Distinguish "should" (expected) from "must" language.

**When asked for B-10 continuous monitoring:**
1. Cite Section 2.4 Monitoring and reporting.
2. Note this applies to ALL arrangements, not just material — this is the post-2023 change.
3. Continuous external attack-surface monitoring tools (any vendor) can feed this requirement, but do not substitute for the broader monitoring program required by 2.4.

**When asked about incident reporting:**
1. Cite the Advisory (August 13, 2021) — 24-hour initial notification to Technology Risk Division + Lead Supervisor.
2. List the criteria that make an incident reportable (use the bullet list from the Advisory).
3. Note the Incident Reporting and Resolution Form (Appendix II) is the prescribed format.
4. **Always append: "Privacy overlay — if personal information is involved, PIPEDA breach notification to OPC and affected individuals is a separate obligation with its own timeline ('as soon as feasible') and 24-month record retention."**

**When asked about cross-border data:**
1. Cite B-10 Section 2.2.2.3 — Out-of-Canada arrangements.
2. Map vendor flags (US-hosted, etc.) to this section.
3. Note that B-10 doesn't prohibit out-of-Canada — it requires consideration and risk management.
