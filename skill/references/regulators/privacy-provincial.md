# Provincial Privacy — PHIPA, PIPA BC, PIPA AB

Canada has three provincial private-sector privacy laws that are deemed substantially similar to PIPEDA (Quebec's Loi 25, BC's PIPA, Alberta's PIPA) plus sector-specific health privacy regimes. This reference covers PHIPA (Ontario health) in depth because the skill library has a dedicated PHIPA guide; it covers PIPA BC and PIPA AB at the orientation level. For Loi 25, see `amf-loi25.md`.

## Document set (verified)

| Document | File | What it is |
|---|---|---|
| IPC Ontario Guide to PHIPA | `hguide-e.pdf` | IPC's guide to the Personal Health Information Protection Act, published Dec 2004 |

**Caveat on the PHIPA guide:** Published December 2004. PHIPA has been amended materially since (notably in 2016 and 2019). The guide is useful for orientation and core concepts but should not be cited for provisions that post-date 2004. For current statutory language, go to the Act directly (not in the library — confirm current consolidation on e-Laws Ontario).

---

## PHIPA — Personal Health Information Protection Act (Ontario)

Ontario's health privacy statute. Administered by the Information and Privacy Commissioner of Ontario (IPC). Governs collection, use, and disclosure of personal health information (PHI) by health information custodians (HICs) and their agents.

### Who is a health information custodian (HIC)?

Seven broad categories from the statutory definition:
1. Health care practitioners — anyone who provides health care for payment, whether or not publicly funded (physicians, nurses, dentists, pharmacists, psychologists, physiotherapists, chiropractors, midwives, etc.)
2. Long-term care service providers
3. Community care access corporations (legacy term; restructured in Ontario — confirm current equivalent)
4. Hospitals and other facilities (independent health facilities, laboratories, specimen collection centres, pharmacies)
5. Medical officers of health and boards of health
6. The Ministry of Health (Ontario)
7. Others added by regulation (e.g., Canadian Blood Services has been designated)

### Who is an agent of a custodian?

Under PHIPA, an "agent" is a person who:
- Is authorized to act on behalf of a custodian
- Performs activities for the purposes of the custodian rather than their own purposes
- Whether or not they have the authority to bind the custodian
- Whether or not they are employed by the custodian
- Whether or not they are receiving remuneration

**Examples of agents:** Employees, volunteers, information processors, information managers, third-party vendors acting for a custodian's purposes.

**Critical implication for SaaS vendors serving Ontario clinics:** If a SaaS vendor processes PHI on behalf of a clinic, the vendor is an agent under PHIPA and is bound by PHIPA obligations through the custodian relationship — even without a direct statutory privity with the individual. The custodian remains accountable for the agent's conduct.

### Health Information Network Providers (HINPs) and electronic service providers

PHIPA has specific provisions for service providers who enable a custodian to collect/use/modify/disclose/retain/dispose of PHI electronically. These are covered in regulations that accompany the Act. Key points:
- Electronic service providers are subject to statutory restrictions on use and disclosure even if they are not formally "agents."
- Health Information Network Providers — entities enabling custodians to share PHI electronically with each other — have additional duties set out in regulation.
- Obligations include audit logging, breach notification to the custodian, and restrictions on secondary use.

### What is personal health information (PHI)?

PHI is information identifying an individual (or that with other information could identify the individual) that relates to:
- Physical or mental health
- Provision of health care (including identification of provider)
- Payments or eligibility for health care
- Donation of body parts or bodily substances
- Health card numbers
- Substitute decision-makers

PHI is a specific statutory subset of personal information. Non-PHI personal information held by a custodian may fall under PIPEDA or other law.

### Core custodian obligations (overview)

1. **Consent** — generally required for collection, use, and disclosure of PHI, with specific exceptions for circle-of-care disclosures, emergencies, research, and legal requirements.
2. **Limited collection** — only what is reasonably necessary for the purpose.
3. **Information practices** — written statement of information practices, privacy contact person.
4. **Safeguards** — reasonable administrative, technical, and physical safeguards against theft, loss, unauthorized use, disclosure, copying, modification, disposal.
5. **Accuracy** — reasonable efforts for accuracy in the context of use.
6. **Individual access and correction** — rights of individuals to access their records and request correction.
7. **Breach notification** — at the first reasonable opportunity to individuals; to IPC in prescribed circumstances.
8. **Audit trail / logging** — PHIPA and its regulations impose logging obligations on electronic PHI systems (who accessed, what, when). This is heavily scrutinized by the IPC, especially after incidents of unauthorized snooping.

### Breach handling under PHIPA

- **Notify individuals at the first reasonable opportunity.**
- **Notify the IPC** in prescribed circumstances — PHIPA has thresholds (certain categories of breaches, repeat breaches, failure to notify, etc.). Check regulation O. Reg. 329/04 and subsequent amendments for current mandatory-reporting triggers.
- **Annual statistics** — custodians report certain breach statistics to the IPC annually.
- **IPC orders** are the enforcement mechanism; the Commissioner can order specific remedial steps.

**Operational implication for clinics:** PHIPA audit trails and breach handling are often the weakest link in small-clinic operations. Jane EMR, other EMR/EHR platforms, and any downstream photo/records systems must maintain logs that meet PHIPA expectations. If an agent (vendor) strips or loses metadata, the custodian may be unable to meet its audit-trail duties — this has been flagged historically in clinic work.

### Enforcement

- **IPC investigations** are triggered by individual complaints, self-reports, referrals, or own-motion.
- **IPC orders** can require corrective action, notification, or cessation of specific practices.
- **Offences** — willful violations can be prosecuted under the Act's offence provisions, including fines.
- **Civil action** — PHIPA provides a statutory cause of action for certain breaches (section 65 for actions in Superior Court regarding orders).

---

## PIPA BC — Personal Information Protection Act (British Columbia)

BC's private-sector privacy law. Administered by the Office of the Information and Privacy Commissioner for BC. Deemed substantially similar to PIPEDA for BC commercial activity.

**Core orientation:**
- Applies to private-sector organizations conducting activity in BC.
- Covers personal information (similar scope to PIPEDA) — not limited to commercial activity.
- Includes employee personal information (broader than PIPEDA in some respects).
- Consent framework similar to PIPEDA with some BC-specific provisions.
- Complaint-driven enforcement model through the OIPC BC.
- Mandatory breach notification provisions exist (amended in recent cycles; confirm current language).

**Relationship with BCFSA:** BC credit unions and provincial insurers are subject to PIPA BC for their personal information processing, layered on top of their BCFSA obligations. A cyber incident at a BC credit union can trigger both a BCFSA incident notification and a PIPA BC breach notification simultaneously.

**Documents not in library:** PIPA BC statute and OIPC BC guidance are not in the current reference library. When advising on PIPA BC specifics, confirm current statutory language against the BC e-Laws source rather than relying on memory.

---

## PIPA AB — Personal Information Protection Act (Alberta)

Alberta's private-sector privacy law. Administered by the Office of the Information and Privacy Commissioner of Alberta. Deemed substantially similar to PIPEDA for Alberta commercial activity.

**Core orientation:**
- Applies to organizations collecting, using, or disclosing personal information in Alberta.
- Structure similar to PIPEDA (consent, limited use, safeguards, access).
- Mandatory breach notification to the Commissioner and affected individuals where there is a **real risk of significant harm** (parallel language to PIPEDA 10.1).
- Employee personal information covered.

**Relationship with AER Reg 84:** AER-regulated Alberta energy operators are NOT directly regulated on privacy by the AER — privacy overlay for customer, employee, and third-party data is PIPA AB (for private-sector commercial activity) or PIPEDA (for federal-works context or inter-provincial activity). A cyber incident at an energy operator can trigger AER Reg 84 (under SMP requirements), PIPA AB (if personal information affected), and potentially Bill C-26 (when in force).

**Documents not in library:** PIPA AB statute and OIPC AB guidance are not in the current reference library. Confirm current statutory language against Alberta's Queen's Printer before citing specific sections.

---

## Jurisdictional map for privacy questions

Use this decision table:

| Scenario | Applicable privacy law(s) |
|---|---|
| Ontario clinic, Jane EMR, patient records | **PHIPA** (clinic is HIC) |
| Ontario SaaS vendor processing PHI for clinic | **PHIPA** (vendor is agent of HIC) |
| Ontario marketing agency processing Ontario consumer data | **PIPEDA** (PHI-out-of-scope; commercial activity, no Ontario general private-sector law) |
| BC credit union, member records | **PIPA BC** (provincial commercial activity) |
| BC credit union breach affecting BC members | **PIPA BC** + **BCFSA** incident notification |
| Alberta energy operator, customer contact data | **PIPA AB** |
| Alberta energy operator cyber incident | **AER Reg 84** (operations) + **PIPA AB** (if PI affected) |
| Federal bank (Schedule I), customer data | **PIPEDA** (federal work) |
| Federal bank breach in Ontario | **PIPEDA** + **OSFI** + (if Ontario health data involved) **PHIPA** |
| Quebec FI with Quebec customer data | **Loi 25** + **AMF** (see `amf-loi25.md`) |
| SaaS operating in multiple provinces | **PIPEDA** federally + Loi 25 for Quebec data + PIPA BC for BC data + PIPA AB for Alberta data + PHIPA if health data in Ontario |

---

## Output patterns for provincial privacy questions

**When asked about Ontario health privacy:**
1. Confirm custodian status using the seven categories.
2. If vendor-side, confirm agent status under PHIPA.
3. Cite PHIPA (not PIPEDA) for PHI-specific obligations. Note that non-PHI personal information collected by a custodian for non-health purposes may fall under PIPEDA.
4. Flag audit-trail and logging requirements — these are high-scrutiny items for IPC.
5. **Always append: "Breach notification to individuals at the first reasonable opportunity; IPC in prescribed circumstances. If the custodian is also engaged in regulated financial activity (e.g., HSP under FSRA), sector clocks may apply in parallel."**

**When asked about BC or Alberta private-sector privacy:**
1. Note that PIPA BC / PIPA AB apply in place of PIPEDA for intra-provincial commercial activity.
2. Use plain-language guidance unless the question requires statutory-level detail — in that case, flag that the library does not contain the BC or Alberta statutes and confirm current language is needed.
3. Real risk of significant harm is the breach trigger in both PIPA BC and PIPA AB (parallel to PIPEDA 10.1).

**When asked about multi-provincial operations:**
1. Map the jurisdictional table above.
2. The organization should design for the strictest applicable regime per category of data (Loi 25 is the strictest for consent and cross-border; PHIPA is the strictest for health; PIPA AB/BC have distinct employee-data treatment).
3. A single enterprise privacy program can meet all regimes if built to the highest bar and jurisdictionally tagged.

**When advising clinic work (Ontario medical aesthetics context):**
1. Clinics are HICs under PHIPA. Staff and vendors are agents.
2. Jane EMR is the system of record; metadata stripping on photo exports is a PHIPA audit-trail concern.
3. Any downstream system (photo editor, attribution tool, analytics platform) handling patient data is an agent/service provider with its own obligations under PHIPA and its regulations.
4. Breach notification is to individuals at first reasonable opportunity and to the IPC per prescribed circumstances.
5. Marketing data (pre-consultation leads, non-patient prospects) may fall under PIPEDA rather than PHIPA because it is not yet PHI.

**Privacy overlay reminders (use these in sector-regulator answers):**
- OSFI answer → "PIPEDA privacy overlay: section 10.1 breach notification to OPC and affected individuals with 24-month record retention under 10.3."
- FSRA answer → "PIPEDA privacy overlay (Ontario provincially regulated entities); add PHIPA if health data is involved (some credit unions serve health-sector customers)."
- AMF answer → "Loi 25 privacy overlay: section 23.5 confidentiality incident notification to CAI and affected individuals; section 23.8 register."
- AER answer → "PIPA AB privacy overlay: real risk of significant harm triggers notification to the OIPC AB and affected individuals."
- CIRO answer → "PIPEDA privacy overlay applies nationally; Loi 25 for Quebec personal information; PIPA BC and PIPA AB for BC/Alberta intra-provincial."
