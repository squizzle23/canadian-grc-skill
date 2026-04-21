# Incident Playbook — The "We Had a Breach" Decision Tree

When a user says "we had a breach" or asks about incident reporting, this is the decision tree. Never assume which clocks apply. Ask structured questions, then map every applicable obligation.

## Step 1 — Triage questions (ask these first)

Before giving ANY reporting advice, establish:

1. **Who is the organization?**
   - Sector (bank, insurer, credit union, investment dealer, energy operator, clinic, SaaS vendor, other)
   - Jurisdiction of incorporation and operation
   - Any regulatory registrations (OSFI, FSRA, BCFSA, AMF, CIRO, AER)

2. **What data is involved?**
   - Personal information? Whose? From where?
   - Personal health information (Ontario)?
   - Payment card data?
   - Employee data?
   - Confidential business/trading information?

3. **What happened?**
   - Unauthorized access/disclosure/use/loss
   - System compromise
   - Third-party incident affecting us
   - Ransomware / extortion
   - Physical loss (theft, misplacement)

4. **Who else is involved?**
   - Customers who are themselves regulated (their clocks may trigger through our notification)
   - Third-party vendors (their incident, our obligations)
   - Sub-processors, affiliates, parent entities

5. **What has happened so far?**
   - When was it discovered (starts multiple clocks)
   - What internal escalations have occurred (officer/manager awareness triggers AMF clock)
   - Has it been contained?
   - Has a BCP/DR been invoked (CIRO trigger)?

**If these answers are unclear, do not give reporting advice — ask first.**

## Step 2 — Apply the clocks

Based on Step 1, map every applicable clock. Use this lookup:

### Sector regulator clocks

| Sector | Regulator | Trigger | Timeline |
|---|---|---|---|
| Federal bank, insurer, trust & loan | OSFI | Technology or cyber security incident meeting B-13 Advisory criteria | **24 hours** initial to TRD-DRT@osfi-bsif.gc.ca + Lead Supervisor |
| Ontario credit union, provincial insurer | FSRA | Material IT risk incident | **72 hours or sooner** to ITriskinbox@fsrao.ca |
| BC credit union, provincial insurer | BCFSA | Per BCFSA guidance | Per BCFSA (confirm current expectation) |
| Quebec FI | AMF | Any Incident per Incident Reporting Regulation | **24 hours** from officer/manager awareness via E-Services |
| National investment dealer | CIRO | Cybersecurity incident per Rule 3703(1) | **3 calendar days** initial + **30 calendar days** follow-up |
| Alberta critical energy operator | AER | Security incident at critical facility | Per SMP requirements under Reg 84 |
| Federal critical infrastructure (when in force) | CCCS | Per Bill C-26 / CCSPA | Per CCCS designation |

### Privacy clocks (always check — these are layered on top of sector)

| Privacy regime | Trigger | Timeline |
|---|---|---|
| PIPEDA | Breach of security safeguards creating real risk of significant harm (10.1) | **"As soon as feasible"** to OPC + affected individuals + other organizations (10.2) |
| PIPEDA record-keeping | **Every** breach, not just reportable (10.3) | 24-month record retention |
| Loi 25 (Quebec) | Confidentiality incident presenting risk of serious injury | **"Promptly"** to CAI + affected individuals |
| Loi 25 register | All confidentiality incidents | Ongoing register; CAI access on request |
| PHIPA (Ontario) | Loss, theft, unauthorized use/disclosure of PHI | **"At the first reasonable opportunity"** to affected individuals; to IPC in prescribed circumstances |
| PIPA BC | Real risk of significant harm | To OIPC BC + affected individuals (confirm current statutory language) |
| PIPA AB | Real risk of significant harm | To OIPC AB + affected individuals |

### Customer / contractual clocks (don't forget)

- Customer contracts often impose notification timelines shorter than regulation.
- MSAs with regulated entities commonly include 24-hour or 48-hour notification clauses.
- If a customer is a regulated entity (OSFI bank, FSRA CU, etc.), your delay in notifying may cause their clock to run out — creating a breach of contract and a regulatory exposure.

### Other stakeholders to consider

- **Cyber insurance carrier** — notification is typically required within a short window (24–72 hours) per policy terms; failure can void coverage.
- **Law enforcement** — RCMP, OPP, or local police for extortion, theft, or major incidents.
- **Canadian Centre for Cyber Security (CCCS)** — voluntary reporting; becomes mandatory under Bill C-26 for designated operators.
- **External counsel** — attach privilege early if litigation or investigation is likely.
- **Board of directors** — most governance charters require board notification for material incidents.

## Step 3 — Map a concrete timeline example

**Example: OSFI-regulated federal bank in Ontario, cyber incident affecting customer data including some Quebec residents.**

Starting clock: incident discovered at T+0.

| Obligation | Clock | Recipient |
|---|---|---|
| OSFI initial notification | T+24 hours | TRD-DRT@osfi-bsif.gc.ca + Lead Supervisor (B-13 Advisory) |
| Cyber insurance notification | T+24–72 hours (policy-dependent) | Carrier per policy |
| Customer contractual notification | T+varies (contract-dependent) | Affected customers per MSA |
| PIPEDA OPC report | "As soon as feasible" | Office of the Privacy Commissioner |
| PIPEDA individual notification | "As soon as feasible" | Each affected individual |
| PIPEDA record | Created immediately, retained 24 months | Internal register |
| Loi 25 CAI notification (Quebec residents) | "Promptly" | Commission d'accès à l'information |
| Loi 25 individual notification (Quebec residents) | "Promptly" | Each affected Quebec individual |
| Loi 25 register entry | Immediate, ongoing | Internal register |
| OSFI subsequent reports | Daily updates until resolved | OSFI Lead Supervisor |

That's **seven to nine** distinct obligations from a single incident. Missing any one of them is a compliance failure.

## Step 4 — Composing the advice response

Use this format when advising on "we had a breach":

```
## Your reporting obligations

### Sector regulator(s)
[List each applicable sector regulator, trigger, timeline, method, content requirements]

### Privacy overlay(s)
[List each applicable privacy regime, trigger, timeline, method, record retention]

### Contractual and other
[Insurance, customer contracts, law enforcement, CCCS]

## Priority sequence (first 24 hours)
1. [Fastest clock — usually OSFI, AMF, or contractual]
2. [Privacy regime if personal information is involved]
3. [Cyber insurance carrier]
4. [Internal escalations per incident management policy]

## What you need to gather NOW
- Incident timeline (discovered, occurred, contained)
- Systems, data, and people affected
- Initial severity and impact assessment
- Names of potentially affected individuals and where they reside (jurisdiction of residence determines privacy clocks)
- Third-party involvement
- Whether BCP/DR has been invoked

## What can wait 24–48 hours
- Full cause analysis
- Full scope determination (may be partial at first report)
- Remediation plan detail

## Caveats
- This analysis is based on [stated facts]; change in facts may change obligations.
- Legal counsel should be engaged for regulatory notifications — they often hold privilege and timing considerations are adversarial.
- I am not a lawyer; this is compliance guidance, not legal advice.
```

## Step 5 — What NOT to do

- **Do not** advise that SOC 2 or ISO 27001 certification affects breach notification obligations — it doesn't.
- **Do not** say "report within X hours" without stating which regulator — different regulators have different clocks.
- **Do not** assume the organization is not subject to a regulator because they don't self-identify — ask for certainty.
- **Do not** suggest waiting for full information before initial notification — most regimes accept "information not yet available" in the initial report and require updates as information develops.
- **Do not** forget the privacy overlay when answering a sector-regulator question.
- **Do not** name the organization's specific breach details in generic advice — treat hypothetical patterns.

## Quick reference — clock speed ranking (fastest to slowest)

1. **Contractual notifications to regulated customers** — often 24 hours or less, sometimes 4–8 hours
2. **OSFI B-13 Advisory** — 24 hours (federal FRFIs)
3. **AMF Incident Regulation** — 24 hours from officer/manager awareness
4. **Cyber insurance** — 24–72 hours typical
5. **CIRO Rule 3703** — 3 calendar days initial
6. **FSRA Practice 7** — 72 hours or sooner
7. **PIPEDA / Loi 25 / PIPA BC / PIPA AB / PHIPA** — "as soon as feasible," "promptly," "first reasonable opportunity" (intent is prompt, not next-quarter)
8. **CIRO Rule 3703 follow-up** — 30 calendar days
9. **AMF end-of-incident report** — 30 days after control re-established

When multiple clocks apply, the fastest drives the initial response timeline even if the slower clocks are more detailed.
