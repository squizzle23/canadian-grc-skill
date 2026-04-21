# AER Regulation 84/2024 — Curated Reference

Alberta Regulation 84/2024 — Security Management for Critical Infrastructure Regulation, made under the Responsible Energy Development Act. Applies to Alberta energy operators (licensees and approval holders) whose facilities are named on the AER's critical infrastructure list.

**Critical fact:** The regulation came into force **May 31, 2025**. It repealed the prior Security Management for Critical Upstream Petroleum and Coal Infrastructure Regulation (AR 91/2013).

**This is OT regulation, not IT.** Do not apply B-13, FSRA IT Risk, or other corporate IT frameworks to AER-scoped operators unless you are specifically discussing their corporate IT environment (which is out of scope of Reg 84).

## Document set (verified)

| Document | File | Date |
|---|---|---|
| Alberta Regulation 84/2024 — Security Management for Critical Infrastructure | `2024_084 (2).docx` | Made 2024; came into force May 31, 2025 |

**Referenced standard:** CSA Z246.1 — Security Management for Petroleum and Natural Gas Industry Systems (published by the Canadian Standards Association). **This standard is paywalled.** If the standard is not in the project knowledge, cite only what Reg 84 itself says about it. Do not fabricate Z246.1 section numbers.

---

## Section-by-section summary (full text verified)

### Section 1 — Definitions

- **Approval holder:** An approval holder under an energy resource enactment.
- **Coal processing plant:** As defined in the Coal Conservation Act.
- **Critical facility:** Any of the following that is named in the critical infrastructure list, **including any related facility of a critical facility**:
  - Coal processing plant
  - In situ operation
  - Mine
  - Mining operation
  - Pipeline
  - Processing plant
  - Well
- **Critical infrastructure list:** The list established under section 2.
- **CSA Z246.1:** CSA Z246.1: Security Management for Petroleum and Natural Gas Industry Systems, as amended or replaced from time to time.
- **In situ operation:** An in situ operation as defined in the Oil Sands Conservation Act, or an in situ coal scheme as defined in the Coal Conservation Act.
- **Licensee:** A licensee under an energy resource enactment.
- **Mine:** As defined in the Coal Conservation Act or the Mineral Resource Development Act.
- **Mining operation:** As defined in the Oil Sands Conservation Act.
- **Pipeline:** As defined in the Pipeline Act.
- **Processing plant:** As defined in the Mineral Resource Development Act, the Oil and Gas Conservation Act, or the Oil Sands Conservation Act.
- **Regulator:** The Alberta Energy Regulator (AER).
- **Security management:** A process that addresses security in respect of terrorist activity or the threat of terrorist activity against a critical facility for the purposes of section 80 of the Responsible Energy Development Act.
- **Well:** As defined in the Geothermal Resource Development Act, the Mineral Resource Development Act, or the Oil and Gas Conservation Act.

**Implication of "security management" definition:** The regulation is framed around *terrorist activity or threat of terrorist activity* — a specific threat model. While the CSA Z246.1 standard covers broader security including cyber, the regulatory trigger is narrower than a general infosec regime.

### Section 2 — Critical Infrastructure List

**2(1)** For the purposes of security management, the Regulator must establish and maintain a critical infrastructure list of critical facilities.

**2(2)** In identifying critical facilities, the Regulator may consider:
- (a) the size and type of the facility;
- (b) the proximity of the facility to people, property and environmental factors;
- (c) facility throughput;
- (d) the interdependency of the facility with other infrastructure;
- (e) any other relevant factors.

**2(3)** The Regulator must notify the licensee or approval holder of a critical facility that the critical facility is on the critical infrastructure list.

**2(4)** Subject to subsection (3), the critical infrastructure list is **confidential and may not be accessed except as permitted by the Regulator**.

**2(5)** The Regulator may update the critical infrastructure list from time to time.

**Operational implications:**
- Operators do not self-identify as in-scope. The AER notifies them.
- The list is confidential — operators cannot confirm to third parties (including vendors) whether a specific facility is in-scope, except with AER permission.
- "Any relevant factors" in 2(2)(e) gives the AER broad discretion.

### Section 3 — Security Management Program (the core obligation)

**3(1) — the mandate:**

> A licensee or approval holder of a critical facility **must** establish and implement a security management program for the critical facility in accordance with CSA Z246.1.

**3(2) — enforcement:** If the Regulator is of the opinion that the licensee or approval holder has failed to establish and implement a security management program under subsection (1), the Regulator may:
- (a) order the licensee or approval holder to establish and implement a security management program under subsection (1), OR
- (b) **order the licensee or approval holder to shut down or shut in the critical facility**, with terms under which the order may cease to have effect.

**3(3) — information filing:** The Regulator may require a licensee or approval holder to file with the Regulator all information or any specified information in relation to the security management of the critical facility.

**3(4) — confidentiality:** Any information filed under subsection (3) is confidential and may not be accessed except as permitted by the Regulator.

**3(5) — audit authority:** The Regulator may audit the security management program of a licensee or approval holder to ensure that:
- (a) the security management program is in compliance with the applicable provisions in CSA Z246.1, and
- (b) the licensee or approval holder has capacity to implement the security management program.

**Critical operational implications:**
- **Shut-in authority** — Section 3(2)(b) is the hard enforcement tool. The AER can order a facility to cease operations for non-compliance. This is significantly more severe than a monetary penalty and reframes non-compliance as a continuity risk for the operator.
- **Mandatory standard alignment** — Reg 84 does not define security controls itself; it incorporates CSA Z246.1 by reference. Compliance requires meeting CSA Z246.1 as interpreted by the AER.
- **Audit discretion** — The AER decides when and how to audit; there is no fixed cadence in the regulation.
- **Capacity-to-implement test** — 3(5)(b) adds a capacity dimension: the operator must not only have a program on paper but have the resources and capability to implement it.

### Section 4 — Repeal

Repeals AR 91/2013 (Security Management for Critical Upstream Petroleum and Coal Infrastructure Regulation).

### Section 5 — Expiry

The regulation will be reviewed for ongoing relevancy and necessity before expiry.

### Section 6 — Coming into Force

**May 31, 2025.**

---

## CSA Z246.1 — what Reg 84 says about it

The regulation references CSA Z246.1 as the substantive security-management standard, but the standard itself is paywalled and not in the library. The regulation tells us:
- Full title: CSA Z246.1 — Security Management for Petroleum and Natural Gas Industry Systems.
- It is published by the Canadian Standards Association.
- "As amended or replaced from time to time" — operators must track amendments.
- Reg 84 section 3(5)(a) anchors audit to "compliance with the applicable provisions in CSA Z246.1" — meaning AER audits will inspect against CSA Z246.1 directly.

**Scope of CSA Z246.1 (general knowledge, not a citation from the standard):** The standard covers a security management framework for petroleum and natural gas operations including physical security, cyber security, personnel security, threat and risk assessment, and incident management. It uses a plan-do-check-act cycle. Operators establish a Security Management Plan (SMP) per facility or group of facilities.

**When advising operators:** Do not quote Z246.1 section numbers unless the standard is in front of you. Confirm the operator has a current copy — if not, direct them to CSA. An SMP aligned to Z246.1 is the deliverable; Reg 84 is the legal obligation to have one.

---

## OT vs. IT — a critical scoping note

AER Reg 84 applies to **operational technology** environments (OT/SCADA, ICS, industrial automation, pipeline control, well-site telemetry). These are:

- **Not corporate IT** — different architectures (Purdue model zones), different protocols (Modbus, DNP3, OPC, BACnet), different vendors (Rockwell, Siemens, Schneider, Honeywell, Emerson).
- **Not usually reachable from the internet** — OT networks are typically air-gapped or segmented behind DMZs, though IT/OT convergence has increased exposure.
- **Different threat model** — Reg 84 specifically targets terrorist activity; beyond that, operators face nation-state, insider, and ransomware threats against OT that can cause physical harm and environmental damage.
- **Regulatory framing** — Reg 84 is grounded in public safety and critical infrastructure protection, not financial consumer protection or personal information.

Implications for any external attack-surface analysis of an AER-regulated operator:
- Corporate IT findings (TLS, patching, DMARC) may still matter for the operator's corporate environment, but **do not map directly to Reg 84 obligations** without a corporate-IT-to-OT interconnect story.
- Relevant vendor categories include OT integrators (Rockwell, Siemens, Schneider, Honeywell, Emerson, Wonderware, GE) and cellular carriers (used for SCADA telemetry) — these signal OT exposure even when the operator's IT surface looks clean.
- The internet-facing surface of an operator (VPN gateways, remote access, corporate cloud connected to OT through IT/OT DMZs) is what an external signal can see — the rest is only visible to an insider or on-site assessment.

---

## Output patterns for AER Reg 84 questions

**When asked for Reg 84 compliance obligations:**
1. Cite **Section 3(1)** — mandatory security management program per CSA Z246.1.
2. Cite **Section 3(5)** — AER audit authority.
3. Note **Section 3(2)(b)** shut-in risk as the consequence of non-compliance.
4. Note the critical infrastructure list is confidential (Section 2(4)) — operators may not know the full list applicable to them outside their own notifications (Section 2(3)).

**When asked whether a specific facility is in scope:**
1. The answer is: "Only the AER knows the current list. The operator is notified under 2(3). The list is confidential under 2(4)."
2. Do not attempt to infer scope from facility type alone — 2(2) uses multi-factor discretion.

**When asked for a Reg 84 gap analysis:**
1. Confirm the operator has been notified under 2(3).
2. Assess program maturity against CSA Z246.1 — Reg 84 itself has no prescriptive controls.
3. Assess implementation capacity under 3(5)(b) — a paper program without operational capability is insufficient.
4. Note that AER audit is at the Regulator's discretion (3(5)) — readiness is continuous, not calendar-driven.

**When building a gap-analysis or readiness view for an AER operator:**
1. Focus on what's externally observable — internet-facing assets at the operator (corporate IT + any IT/OT gateways). OT and physical security are not visible externally; flag this limitation explicitly.
2. Use CSA Z246.1 alignment language, not specific section numbers you don't have.
3. Any vendor review should call out OT integrators and cellular carriers as elevated-attention categories.
4. Frame discovery questions against "the Security Management Plan under Reg 84 s. 3(1)" and "CSA Z246.1 alignment."
5. Always include these guardrails:
   - This analysis does not establish Reg 84 non-compliance; an AER audit under s. 3(5) is the authoritative source.
   - Findings from externally observable signals reflect only the internet-facing, IT-layer surface. OT and physical security are scoped separately under CSA Z246.1 and are not visible from outside the operator's network.

**Privacy overlay note:** Reg 84 does not directly engage personal information. The privacy overlay for AER-regulated operators is **PIPA Alberta** (Alberta's private-sector privacy law) — separately applicable for customer, employee, and third-party personal information. A cyber incident at an operator may trigger Reg 84 reporting, PIPA Alberta notifications (if personal information is affected), PIPEDA (if federal-works or inter-provincial commercial activity), and potentially Bill C-26 obligations (when in force, for designated operators in federally regulated energy pipelines).
