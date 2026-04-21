# CIRO — Curated Reference

Canadian Investment Regulatory Organization — the national self-regulatory organization for investment dealers and mutual fund dealers, formed in January 2023 from the merger of IIROC and the MFDA. Most cybersecurity documents in the library were published under the IIROC name before the merger but remain in force under CIRO.

## Document set (verified)

| Document | PDF | Date |
|---|---|---|
| IIROC Cyber Governance Guide | `IIROCCyberGovernanceGuide_en-compressed.pdf` | Jan 31, 2020 |
| IIROC Cyber Governance Guide (duplicate) | `Cyber-Governance-Guide-EN-compressed.pdf` | Jan 31, 2020 |
| IIROC Cybersecurity Best Practices Guide | `Cybersecurity-Best-Practices-Guide-EN.pdf` | — |
| IIROC Cyber Incident Management Planning Guide | `Cyber-Incident-Management-Planning-Guide-EN.pdf` | — |
| CIRO Ransomware Response Playbook | `CIRO-Ransomware-Response-Playbook-EN.pdf` | — |
| IIROC Fundamentals of Technology Risk Management | `Fundamentals-of-Technology-Risk-Management-EN.pdf` | — |
| CIRO Investment Dealer and Partially Consolidated (IDPC) Rules | `IDPC-Rules-022224-EN-compressed.pdf` | Feb 22, 2024 |
| IIROC Rule 3703 Amendments (Appendix 5) — Mandatory Reporting of Cybersecurity Incidents | `06f7ed23-017d-4046-9038-4a86b54a0071_en_0.pdf` | Per IIROC Notice 19-0194 |

**Naming note:** IIROC-branded guides from 2020 remain CIRO-applicable; use "CIRO (formerly IIROC)" when citing to avoid confusion. The cybersecurity incident reporting rule (Rule 3703) is codified in the IDPC Rules.

---

## Rule 3703 — Mandatory Reporting of Cybersecurity Incidents (the hard rule)

This is the statutory obligation. Everything else (Governance Guide, Best Practices, Incident Management Planning) is supportive guidance. **Rule 3703 is the enforceable citation.**

### Definition of "cybersecurity incident" (Rule 3703(1))

A cybersecurity incident includes any act to gain unauthorized access to, disrupt, or misuse a Dealer Member's information system, or information stored on such information system, that has resulted in, or has a reasonable likelihood of resulting in:

1. Substantial harm to any person,
2. A material impact on any part of the normal operations of the Dealer Member,
3. Invoking the Dealer Member's business continuity plan or disaster recovery plan, or
4. The Dealer Member being required under any applicable laws to provide notice to any government body, securities regulatory authority or other self-regulatory organization.

### Reporting timeline (Rule 3703(2)(vii))

Reporting is in two stages, both in writing:

**Stage 1 — Within 3 calendar days from discovery:**
- A description of the cybersecurity incident
- The date on which or time period during which the incident occurred, and the date it was discovered
- A preliminary assessment — risk of harm to any person and/or impact on operations
- A description of immediate incident response steps taken to mitigate risk and impact
- Name and contact information for an individual who can answer CIRO follow-up questions

**Stage 2 — Within 30 calendar days from discovery (unless otherwise agreed by CIRO):**
- A description of the cause of the incident
- An assessment of the scope — number of persons harmed and operational impact
- Details of mitigation steps taken
- Details of remediation steps for any harm to persons
- Actions the Dealer Member has or will take to improve cybersecurity incident preparedness

### Rule 3704 — Failure to report

Failure to report as required by sections 3702 and 3703 may result in CIRO imposing an administrative fee or other penalties permitted under CIRO requirements, against the Dealer Member or Approved Person.

### Citation format

When advising on CIRO cyber obligations, cite: **Rule 3703(1)** for the definition, **Rule 3703(2)(vii)(a)** for 3-day initial reporting, **Rule 3703(2)(vii)(b)** for 30-day follow-up. The Rules themselves live in the IDPC Rules document.

---

## IIROC Cyber Governance Guide (January 31, 2020, still applicable under CIRO)

Structured around NIST Cybersecurity Framework (NIST CSF) — CIRO explicitly adopts NIST as its operating model.

### Structure

1. **Introduction**
   - 1.1 Document structure
   - 1.2 The challenge
   - 1.3 The approach

2. **Threat Environment**
   - 2.1 What constitutes a threat?
   - 2.2 Threat actors
   - 2.3 Human-oriented tradecraft
   - 2.4 Cyber-oriented tradecraft

3. **Security Policy & Program Governance**
   - 3.1 Leadership and fiduciary responsibility
   - 3.2 Key cybersecurity program elements
   - 3.3 Insurance against cyber-related risks
   - 3.4 Key legal considerations
   - 3.5 Policies & procedures

4. **Operating Tier Framework**
   - 4.1 The NIST Cybersecurity Framework
   - 4.2 Why rely on NIST?
   - 4.3 Phased approach
   - 4.4 Appreciating cost / difficulty / time frame
   - 4.5 Profile descriptions

5. **Operational Program Implementation Guidance**
   - 5.1 Due diligence & duty of care
   - 5.2 Preparedness
   - 5.3 Assessing threats and vulnerabilities
   - 5.4 Comprehensive program development

6. **Best Practice Recommendations**
   - 6.1 Personnel screening and the insider threat
   - 6.2 Physical and environmental security
   - 6.3 Cybersecurity awareness and training

### Key themes

- **NIST CSF alignment** — CIRO's expected control reference model is NIST CSF. Dealer Members mapping to NIST CSF can represent alignment with CIRO's expected framework.
- **Board fiduciary duty** — Section 3.1 frames cybersecurity oversight as a fiduciary-level responsibility.
- **Tiered approach** — Section 4 uses NIST's four-tier implementation maturity model (Tier 1 Partial → Tier 4 Adaptive).
- **Not a minimum standard** — it is guidance, not mandate. The only mandate is Rule 3703 reporting.

---

## IIROC Cybersecurity Best Practices Guide

Companion to the Governance Guide, providing specific operational controls. Structured by control domain — network security, endpoint protection, identity and access management, email security, data protection, vulnerability management, security monitoring, incident response.

Where the Governance Guide answers "how should we organize our program?", the Best Practices Guide answers "what controls should the program include?"

Content is consistent with NIST CSF subcategories and CIS Controls.

---

## IIROC Cyber Incident Management Planning Guide

Guidance on building and exercising an incident response program, distinct from the mandatory incident reporting obligation (which is Rule 3703).

### Structure

1. Executive summary
2. An overview of cybersecurity incident management
3. Information sharing
4. Planning for incident management
5. Exercise and test scenarios

### Key concepts

- Incident management is a lifecycle: preparation → detection and analysis → containment, eradication, and recovery → post-incident activity.
- Tabletop exercises are recommended practice.
- Information sharing with industry peers (e.g., through CIRO or FS-ISAC) is encouraged.
- This guide is guidance (not mandate) — Rule 3703 reporting is mandatory.

---

## CIRO Ransomware Response Playbook

Dealer-member-specific ransomware playbook. Designed for dealer members facing ransomware attacks with material impact on continuity of business operations.

Content typically includes:
- Decision tree for initial response (contain, communicate, consult)
- Law-enforcement coordination guidance
- Ransom payment considerations (regulatory, legal, ethical)
- Communication templates for clients and regulators
- Recovery milestones

**Regulatory interaction:** Ransomware incidents meeting the Rule 3703(1) definition are reportable — substantial harm to persons, material impact on operations, or invocation of BCP/DR all typically apply.

---

## IIROC Fundamentals of Technology Risk Management

IIROC's general technology risk framework for dealer members. Broader than cybersecurity — covers architecture, change management, operations, vendor management, resilience.

Not a rule; supervisory guidance. CIRO considers this document in its technology risk assessments of dealer members.

---

## IDPC Rules (February 22, 2024)

CIRO Investment Dealer and Partially Consolidated Rules — the full rulebook for dealer members. Structure:

- **Rule 1100 — Interpretation** (introduction, general interpretation, delegation, electronic signatures, transitional)
- **Rule 1200 — Definitions**
- **Rule 1300 — Exemptive Powers of the Corporation**
- **Rule 1400 — Standards of Conduct** (including 1402 Standards of conduct, 1404 Policies and procedures, 1405 Evidence of compliance, 1406 Compliance with all applicable laws, 1407 Training)
- **Rule 1500 — Managing Significant Areas of Risk** (1502 Responsibility for significant areas of risk — where technology and cyber risk sit as significant areas)
- ...
- **Rule 3700 series — Reporting and Handling of Complaints, Internal Investigations and Other Reportable Matters**
  - **Rule 3703 — Reporting by a Dealer Member to IIROC [CIRO]** — the cybersecurity incident reporting rule (amended by IIROC Notice 19-0194)
  - **Rule 3704 — Failure to report**

**Key point:** Cybersecurity reporting is codified inside Rule 3703 alongside other mandatory reporting matters (complaints, internal investigations, disciplinary actions). It's not a separate cyber rule — it's folded into the existing reportable-matters framework.

---

## Output patterns for CIRO questions

**When asked about CIRO cyber incident reporting:**
1. Cite **Rule 3703(1)** for the definition (note the four triggers).
2. Cite **Rule 3703(2)(vii)(a)** for the 3-day initial report and specify required content.
3. Cite **Rule 3703(2)(vii)(b)** for the 30-day follow-up report.
4. Cite **Rule 3704** for failure-to-report penalties.
5. **Always append: "If personal information is involved, PIPEDA creates a separate notification obligation to the OPC and affected individuals 'as soon as feasible' with 24-month record retention. If Quebec personal information is involved, Loi 25 adds a 'promptly' notification to the CAI."**

**When asked about CIRO cyber governance:**
1. Reference the IIROC Cyber Governance Guide (2020), noting it remains applicable under CIRO.
2. Emphasize NIST CSF alignment — CIRO explicitly adopts it.
3. Use the four-tier maturity model for gap analysis framing.
4. Note that the Governance Guide is guidance, not mandate — only Rule 3703 is enforceable.

**When asked about CIRO program controls:**
1. Reference the Cybersecurity Best Practices Guide for control-level detail.
2. Map to NIST CSF subcategories for clean traceability.
3. Fundamentals of Technology Risk Management covers broader tech risk beyond cyber.

**Naming sensitivity:** When documents predate the 2023 merger and were published under IIROC, cite them as "IIROC [document] (2020, still applicable under CIRO)" to preempt questions about whether pre-merger guidance is still current. The cybersecurity documents are still in force; the MFDA side has its own merger-era guidance that is less cyber-relevant.

**Common external-finding → CIRO control mappings:**

These are analytical mappings from externally observable security signals (TLS/SSH/DMARC/patching findings from any attack-surface tool) to the CIRO control domains they implicate.

| External finding | CIRO reference | Rationale |
|---|---|---|
| Missing or permissive DMARC policy | Best Practices Guide — Email security + Governance Guide 2.3 Human-oriented tradecraft | Phishing is a primary human-oriented tradecraft vector |
| Weak TLS protocol / weak SSH cipher | Best Practices Guide — Network security | Direct control domain |
| Critical patching cadence lag | Best Practices Guide — Vulnerability management | Patching cadence is a core metric |
| Compromised credentials exposed externally | Governance Guide 5.3 Assessing threats + Best Practices Guide — IAM | External evidence of credential exposure |
| Missing `Secure` cookie attribute | Best Practices Guide — Data protection + Web security | Session/transport protection |

**Key discovery questions when assessing a dealer's readiness:**
- Rule 3703 gives dealer members 3 calendar days from discovery to notify CIRO of a cybersecurity incident, then 30 days for the full report. What is the entity's current detection-to-reporting capability?
- CIRO aligns its cyber governance expectations to NIST CSF. How is the entity operationalizing the Identify and Detect functions in a way the board can see?
