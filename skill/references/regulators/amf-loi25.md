# AMF + Loi 25 — Curated Reference

Quebec regulatory and privacy environment. Two interlocking regimes:
- **AMF** (Autorité des marchés financiers) — sector regulator for Quebec financial institutions, insurers, deposit institutions, and related intermediaries. Covers ICT risk and incident reporting.
- **Loi 25** — Quebec's modernized private-sector privacy law. Applies to ALL Quebec organizations handling personal information, including AMF-regulated FIs.

Quebec FIs face a dual-track obligation: AMF for sector-level ICT and incidents, Loi 25 for any incident or processing involving personal information.

## Document set (verified)

| Document | PDF | Date |
|---|---|---|
| AMF Guideline on ICT Risk Management | `ld-gestion-tic_an.pdf` | February 2020 |
| AMF Application and Implementation Guide — Information Security Incident Regulation | `Guide_ApplicationImplementationRegulationInformationSecurityIncidents.pdf` | July 10, 2025 |
| Act Respecting the Protection of Personal Information in the Private Sector (Loi 25, chapter P-39.1) | `law25.pdf` | Consolidation updated December 11, 2025 |

---

## AMF Guideline on ICT Risk Management (February 2020)

Principles-based ICT risk guideline for AMF-regulated organizations (financial institutions, insurers, deposit institutions). Published in French as "Ligne directrice sur la gestion des risques liés aux TIC."

### Structure

**1. Types of ICT risks** — taxonomy AMF uses to classify ICT-related risk (cyber, availability, integrity, confidentiality, project, third-party, legal/regulatory, etc.)

**2. ICT governance**
- 2.1 Roles and responsibilities
- 2.2 Integrity and competency
- 2.3 ICT documentation

**3. ICT risk management**
- 3.1 Preparation (risk identification, assessment)
- 3.2 Treatment (controls, mitigation)
- 3.3 Follow-up (monitoring, review)

**Appendix:** Complementary standards to the AMF's guidelines (references ISO 27001, ISO 31000, and similar frameworks as supporting references).

### Key characteristics

- **Principles-based** — no detailed control specifications; AMF expects organizations to select appropriate industry standards.
- **Proportionate** — applies scaled to organization size, nature, and complexity.
- **French-first** — the primary authoritative version is French; English is translation. Quebec organizations should be prepared for French-first regulatory communications.
- **Predates modern cyber-specific guidance** — issued 2020, narrower than OSFI B-13 (2022) in specifics; AMF's incident reporting is handled separately through the Incident Regulation (below).

---

## AMF Incident Reporting Regulation — Application and Implementation Guide (July 10, 2025)

Regulation respecting the management and reporting of information security incidents by certain financial institutions and by credit assessment agents, with a separate Application and Implementation Guide.

### Structure of the Guide

1. Introduction
2. Purpose of the guide
3. Organizations subject to the Regulation
4. Incident management policy
5. Procedures and mechanisms for detecting, assessing and responding to Incidents
6. Incident reporting
7. Incident register
8. Process for reporting Incidents to the AMF
9. Assistance

### Section 4 — Incident management policy (mandatory)

Every subject Organization must have an incident management policy that includes criteria for internal reporting (escalation) to officers or managers, as well as reporting to the AMF and stakeholders (clients, third parties, consumers, other regulatory bodies such as OSFI).

### Section 6 — Incident reporting criteria

Good practice recommends reporting decisions consider:
- **Categorization** — grouping by incident type (data theft, outage) or cause (cyberattack, human error).
- **Severity** — urgency and importance, considering: time to return to normal, impact on clients, extent of financial/reputational/regulatory impact, time of incident and estimated resolution.
- **Classification** — qualifying the incident to confirm status and prioritize management, taking into account categorization, severity, and impacts to the Organization, clients, and the financial system.

**Third-party incidents:** When determining reporting, the Organization must consider incidents that occur at a third party to which any part of an activity has been entrusted, if the incident affects that activity.

**Policy requirement:** The Organization must appoint a person responsible for Incident management and reporting (can delegate reporting but remains responsible for compliance).

### Section 7 — Incident register

Every Organization must maintain an up-to-date Incident register.
- **Retention period:** 5 years from the date of the end-of-Incident report.
- **Security:** kept in a secure and confidential manner.
- **Content:** all information relating to the Incident management lifecycle — must support assessments, decisions, and actions taken.
- **AMF access:** a copy of the register must be sent to the AMF at its request.

### Section 8 — Process for reporting Incidents to the AMF

**Timeline for initial notification:** no later than **24 hours** from the time an officer or manager is informed of the situation.

**Method:** E-Services portal (AMF's online reporting system).

**Ongoing reporting:**
- Subsequent reports must be made for every Incident within no more than **3 calendar days**, even if there are no new developments.
- Corrections and new information submitted via E-Services.
- AMF may request clarifications at any time.

**End-of-Incident report:** Final report confirming Incident has been brought under control and normal operations resumed must be submitted **no later than 30 days** after the Incident has been brought under control.

**Definition:** "Brought under control" generally means operations have resumed, though management of the Incident may not be totally complete.

**Financial group simplification:** If an Incident affects multiple Organizations in the same financial group, a single report may cover all affected Organizations, but each Organization remains individually responsible for its reporting obligation.

---

## Loi 25 — Act Respecting the Protection of Personal Information in the Private Sector (chapter P-39.1)

Quebec's private-sector privacy law, modernized through Bill 64 rolled out in three phases (September 2022, September 2023, September 2024). Consolidation updated December 11, 2025.

Applies to any person carrying on an enterprise in Quebec who collects, holds, uses, or communicates personal information.

### Key concepts

**Personal information (Division I, section 2):** any information which relates to a natural person and directly or indirectly allows that person to be identified.

**Confidentiality incident (Division I.1, section 23.6):**
1. Access not authorized by law to personal information
2. Use not authorized by law of personal information
3. Communication not authorized by law of personal information
4. Loss of personal information or any other breach of the protection of such information

### Division I.1 — Protection of personal information (the core obligations)

**Section 23.1** — Any person carrying on an enterprise is responsible for protecting the personal information held by the enterprise.

**Section 23.3** — **Privacy Impact Assessments are mandatory.** Any person carrying on an enterprise must conduct a privacy impact assessment (PIA) for any project to acquire, develop, or redesign an information system or electronic service delivery involving personal information.

**Section 23.5 — Confidentiality incident notification (the central incident provision):**

> Any person carrying on an enterprise who has cause to believe that a confidentiality incident involving personal information the person holds has occurred must take reasonable measures to reduce the risk of injury and to prevent new incidents of the same nature.
>
> If the incident presents a risk of serious injury, the person carrying on an enterprise must **promptly notify** the Commission d'accès à l'information (CAI). He must also notify any person whose personal information is concerned by the incident, failing which the Commission may order him to do so. He may also notify any person or body that could reduce the risk.

Three-part obligation when risk of serious injury is present:
1. Promptly notify the CAI
2. Promptly notify each affected individual (the CAI can order this if the Organization fails to do so)
3. May notify any third party that could help reduce harm (without consent, logged by privacy officer)

**Exception:** Individual notification may be withheld if doing so could hamper an investigation by a body responsible for prevention, detection, or prosecution of crime or statutory offences.

**Section 23.7 — Risk assessment criteria.** When assessing risk of injury, the Organization must consider:
- Sensitivity of the information concerned
- Anticipated consequences of its use
- Likelihood that the information will be used for injurious purposes
- Must consult the person in charge of the protection of personal information within the enterprise

**Section 23.8 — Incident register obligation.** A person carrying on an enterprise must keep a register of confidentiality incidents. A government regulation may determine the content of the register. A copy of the register must be sent to the CAI at its request.

### Other Division I.1 obligations (referenced briefly)

- **Section 14** — Consent must be clear, free and informed, and given for specific purposes.
- **Section 12.1** — Automated decision-making disclosure: if a decision is based exclusively on automated processing, the Organization must inform the individual and give them an opportunity to submit observations.
- **Section 28.2** — Organizations collecting PI through technological means must publish their privacy practices on their website (transparency).
- **Cross-border transfer** (earlier in statute) — requires prior assessment considering protection in the destination jurisdiction.

### Privacy officer requirement

Every Organization must designate a person in charge of the protection of personal information. By default, this is the person with the highest authority in the Organization, but it can be delegated.

---

## Dual-track decisions (the Quebec domino)

When a Quebec FI has an incident involving personal information, two clocks start:

| Clock | Regulator | Timeline | Trigger |
|---|---|---|---|
| AMF incident notification | AMF | **24 hours** from officer/manager awareness | Any Incident per the Incident Regulation |
| Loi 25 confidentiality incident | CAI | **"Promptly"** (no fixed hours, but intent is immediate) | Risk of serious injury to individuals |
| Loi 25 individual notification | Affected individuals | **"Promptly"** | Same as CAI notification |

Additional overlays may apply:
- **OSFI** (if federally regulated) — 24 hours to Technology Risk Division.
- **PIPEDA** (for non-Quebec personal information or inter-provincial commercial activity) — "as soon as feasible" to OPC and individuals, 24-month record retention.
- **Other sector regulators** — FSRA, BCFSA, CIRO if operations cross provincial/SRO lines.

---

## Output patterns for AMF + Loi 25 questions

**When asked about AMF incident reporting:**
1. 24-hour initial notification to AMF via E-Services portal.
2. Subsequent reports every 3 calendar days.
3. End-of-Incident report within 30 days of control being re-established.
4. Incident register retained for 5 years.
5. **Always append: "If personal information is involved, Loi 25 creates a parallel obligation to notify the CAI and affected individuals 'promptly' where risk of serious injury exists. The Loi 25 incident register (section 23.8) is separate from the AMF incident register (section 7 of the Implementation Guide)."**

**When asked about Loi 25 compliance:**
1. Confirm whether the question is about: (a) individual obligations (consent, transparency, PIA), (b) incident handling (sections 23.5–23.8), or (c) cross-border / third-party aspects.
2. Cite the specific section number from chapter P-39.1.
3. Note that the statute was updated December 11, 2025 — if the question depends on a specific amendment, verify against the current consolidation.
4. Distinguish "serious injury" threshold (triggers CAI notification) from the general confidentiality-incident definition (triggers the register and mitigation duties).

**When asked about PIA requirements (section 23.3):**
1. Triggered by: project to acquire, develop, or redesign an information system or electronic service delivery involving personal information.
2. Not optional — statutory requirement.
3. Must be documented and retainable.
4. Involves the person in charge of the protection of personal information.

**When asked about vendor / cross-border for Quebec entities:**
1. Loi 25 requires assessment of protection in the destination jurisdiction before transferring personal information outside Quebec.
2. US-hosted vendors are not prohibited, but require documented assessment and equivalent-protection demonstration.
3. Third-party incidents that affect activities entrusted to the third party are reportable events under both the AMF Incident Regulation (section 6) and Loi 25 (where PI is involved).
4. French-first communications expected for Quebec-based customers and regulators.

**Sales context opener lines:**
- AMF: "AMF's Incident Regulation — 24 hours to notify via E-Services, 5-year register, 30-day end-of-incident report. And Loi 25 layers on a separate 'promptly' notification to the CAI whenever personal information is involved. What's your current detection-to-notification capability?"
- Loi 25: "Section 23.3 mandates a PIA for every new system touching personal information. Section 23.8 requires an incident register accessible to the CAI on demand. Both are testable on audit. Are those being maintained continuously?"
