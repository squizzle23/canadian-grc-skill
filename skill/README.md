# Canadian GRC & Cyber Law — Claude Skill

[![Release: v1.0.0](https://img.shields.io/badge/Release-v1.0.0-brightgreen.svg)](https://github.com/squizzle23/canadian-grc-skill/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../LICENSE)
[![Benchmark: 89.7%](https://img.shields.io/badge/Benchmark-89.7%25-success.svg)](../evals/results.html)
[![Delta: +46.9 pts](https://img.shields.io/badge/Baseline%20Lift-%2B46.9%20pts-blue.svg)](../evals/results.html)

**File:** `canadian-grc.skill`

A Claude Skill that turns Claude into an expert Canadian Governance, Risk, and Compliance advisor grounded in the authoritative federal and provincial regulatory publications. Covers the overlapping regulatory landscape that other compliance skills (SOC 2, ISO 27001, NIST CSF, HIPAA, FedRAMP, GDPR, PCI-DSS) leave out.

---

## What it does

- Runs **jurisdictional routing** to identify the correct regulator before answering any question — OSFI vs. FSRA vs. BCFSA vs. AMF vs. CIRO vs. AER — a common failure mode of baseline LLMs on Canadian compliance questions.
- Maps **incident reporting obligations** across overlapping regimes. A single breach at an Ontario credit union typically triggers FSRA notification plus PIPEDA notification to the OPC plus potentially Loi 25 for Quebec personal information — the skill surfaces every applicable clock and timeline.
- Grounds every citation in the **actual regulator publication**. Section numbers, effective dates, and control references are drawn from the source text, not inferred. The skill is explicit about what it doesn't know (e.g., CSA Z246.1 is paywalled) rather than fabricating.
- Distinguishes **IT from OT**. AER-regulated Alberta energy operators are OT-scoped (SCADA, pipelines, substations) — not corporate IT. The skill does not apply IT-centric frameworks like B-13 to OT environments.
- Separates **frameworks from regulation**. SOC 2, ISO 27001, and NIST CSF are assurance frameworks, not Canadian regulatory compliance. The skill is explicit about what each does and doesn't satisfy under Canadian law.
- Produces **auditor-ready output**: structured gap assessments with 🔴/🟡/🟢 grading, control documentation in the standard examination format, evidence catalogs per regulator, and breach-notification decision trees.

## Coverage

| Regulator | Scope | Curated reference |
|---|---|---|
| **OSFI** | Federal FRFIs — banks, insurers, trust and loan | B-10 (Apr 2023), B-13 (Jul 2022), B-13 Incident Advisory (Aug 2021), E-21 (Aug 2024), I-CRT (Apr 2023) |
| **FSRA** | Ontario credit unions, provincial insurers, pensions | IT Risk Management Guidance (GR0016INT, Apr 2024) + Operational Resilience (CU0088APP, Mar 2024) |
| **BCFSA** | BC credit unions, provincial insurers, trusts | Third-Party Risk Management Guideline (Oct 2025, eff. Jan 2028) + Information Security Guideline (Mar 2025) |
| **AMF** | Quebec financial institutions | ICT Risk Management Guideline (Feb 2020) + Information Security Incident Regulation Implementation Guide (Jul 2025) + Loi 25 (updated Dec 2025) |
| **CIRO** | Canadian investment dealers (formerly IIROC) | Cyber Governance Guide, Best Practices, Incident Management Planning, Ransomware Playbook, IDPC Rules (Feb 2024), Rule 3703 |
| **AER** | Alberta energy critical infrastructure operators | Regulation 84/2024 — Security Management for Critical Infrastructure (eff. May 2025) |
| **Privacy** | Federal and provincial private-sector and health privacy | PIPEDA, PHIPA (Ontario), Loi 25 (Quebec), PIPA BC, PIPA AB |
| **Emerging** | Federal cyber law in progress | Bill C-26 (Critical Cyber Systems Protection Act), Bill C-27 (AIDA) |

## Architecture

```
skill/
├── SKILL.md                               # Loaded into context when the skill triggers
└── references/
    ├── index.md                           # Reference inventory with authoritative source URLs
    ├── incident-playbook.md               # Cross-regime breach decision tree
    ├── evidence-catalog.md                # Per-regulator examination evidence expectations
    └── regulators/
        ├── osfi.md                        # B-10, B-13 + Incident Advisory, E-21, I-CRT (+ BCFSA alignment)
        ├── fsra.md                        # IT Risk Guidance + CU Operational Resilience
        ├── amf-loi25.md                   # AMF ICT Guideline, Incident Reg, Loi 25 statute
        ├── ciro.md                        # Cyber Governance, Best Practices, Rule 3703, IDPC Rules
        ├── aer-reg84.md                   # AER Reg 84/2024 + CSA Z246.1 pointers
        ├── privacy-federal.md             # PIPEDA + OPC guidance
        └── privacy-provincial.md          # PHIPA, PIPA BC, PIPA AB
```

Uses Anthropic's progressive-disclosure pattern — `SKILL.md` is always loaded when the skill triggers, but reference files are loaded on-demand only when Claude needs to go deeper. For example, `references/regulators/osfi.md` loads for any OSFI question; `references/incident-playbook.md` loads for any "we had a breach" scenario.

## Design choices

**Jurisdiction-first routing.** Every answer begins by resolving jurisdiction and sector. The Jurisdictional Router in `SKILL.md` is a lookup table mapping entity types to applicable regulators, so the skill doesn't invent OSFI authority over a credit union or apply B-13 to an AER operator.

**Citations are grounded or absent.** If a specific section number is needed and the skill doesn't have it, it says so — "I need to check the reference document for the exact section" — rather than making one up. Regulator-facing work collapses on wrong section numbers.

**Privacy always layered.** Every sector-regulator answer that touches personal information appends the applicable privacy commissioner obligation. A breach at an OSFI bank triggers both OSFI reporting AND OPC notification under PIPEDA; the skill maps both.

**OT vs. IT separation.** AER's Reg 84 is the only Canadian regulation in scope that applies primarily to operational technology. The skill explicitly flags this and refuses to apply IT-centric controls (TLS, DMARC, patching cadence) to OT environments without a corporate-IT interconnect rationale.

**Audience-adaptive output.** The skill detects whether the user is a compliance officer, board member, technical implementer, or regulator-facing counsel, and calibrates register accordingly. Compliance officers get section numbers and grading; board members get risk and consequence; technical staff get system-level translations.

## Skill evaluation

This skill was benchmarked using an independent Claude-as-grader methodology aligned with the [LangChain skill-evaluation approach](https://blog.langchain.com/evaluating-skills/) and matching the design used by the Sushegaad GRC skills repository.

**Setup:** 35 test cases across 7 regulator groups (5 cases each), with 5 verifiable assertions per case = **175 total assertions**. Each case runs twice — once with the full skill context (SKILL.md plus all reference files) injected into Claude's system prompt, once without — and both responses are graded by an independent Claude Sonnet 4.6 instance against the case's assertions.

| Configuration | Pass rate |
|---|---|
| **With skill installed** | **89.7% (157/175)** |
| Without skill (baseline Claude Sonnet 4.6) | 42.9% (75/175) |
| **Delta** | **+46.9 percentage points** |

### Results by regulator

| Regulator | With skill | Baseline | Delta |
|---|---|---|---|
| **AER** (Alberta energy) | 100% (25/25) | 12% (3/25) | **+88.0 pts** |
| **BCFSA** (BC financial) | 96% (24/25) | 32% (8/25) | **+64.0 pts** |
| **OSFI** (federal financial) | 84% (21/25) | 32% (8/25) | **+52.0 pts** |
| **CIRO** (investment dealers) | 84% (21/25) | 44% (11/25) | **+40.0 pts** |
| **FSRA** (Ontario financial) | 96% (24/25) | 60% (15/25) | **+36.0 pts** |
| **AMF + Loi 25** (Quebec) | 76% (19/25) | 48% (12/25) | **+28.0 pts** |
| **Canadian Privacy** (PIPEDA/PHIPA/PIPA) | 92% (23/25) | 72% (18/25) | **+20.0 pts** |

The skill adds the most measurable value where **baseline Claude genuinely doesn't have the knowledge**: Alberta Regulation 84/2024 (issued 2024, pre-cutoff but specialized), the BCFSA Third-Party Risk Management Guideline (issued October 2025, post-cutoff for most training corpora), and specific OSFI Advisory notification timelines. On broad Canadian privacy questions, baseline Claude already performs reasonably (72%) — the skill lifts accuracy on specific statutory citations and jurisdictional routing.

### Methodology notes

- **Subject and grader models:** Claude Sonnet 4.6 for both, avoiding same-family bias where possible. A grader model stronger than the subject (e.g., Opus) is a reasonable future direction.
- **Verifiable assertions only.** Each assertion is written to be pass/fail from the response text alone — no subjective quality judgments. "States the 24-hour notification timeline," not "writes clearly."
- **Prompt caching.** The full skill context (~145KB / ~36K tokens) is cached across all with-skill calls via Anthropic's prompt-caching feature. This keeps per-case cost around $0.10 rather than $1+.
- **Known variance.** Model responses are non-deterministic. Running the benchmark twice will produce slightly different numbers (±3 points in our testing). The directional finding — substantial, consistent lift on Canadian-specific regulatory knowledge — is stable.

📊 **[View full case-by-case results →](../evals/results.html)**

### Reproducing the benchmark

From the repo root:

```bash
cd evals
export ANTHROPIC_API_KEY=sk-ant-...
pip install anthropic
python3 run_benchmark.py
```

Cost: approximately $3–4 in API usage. Runtime: ~30 minutes at default settings (CONCURRENCY=1, which respects the default 30K TPM input limit on new Anthropic accounts).

## Installation

### Option 1 — Claude Code marketplace

```
/plugin marketplace add squizzle23/canadian-grc-skill
/plugin install canadian-grc@canadian-grc
```

### Option 2 — Local clone

```bash
git clone https://github.com/squizzle23/canadian-grc-skill.git
cp -r canadian-grc-skill/skill ~/.claude/skills/canadian-grc
```

### Option 3 — Claude.ai skill upload

1. Download this repository as a zip.
2. Create a new zip from the contents of the `skill/` folder (so `SKILL.md` is at the root of the archive).
3. Upload it under **Settings → Skills** in Claude.ai.

## Example prompts

Try these to see the skill in action:

- *"We're an Ontario credit union and had a ransomware incident yesterday involving member data. Walk me through every reporting obligation."*
- *"How does OSFI B-10 differ from the BCFSA Third-Party Risk Management Guideline?"*
- *"Does a SOC 2 Type 2 report from our cloud vendor satisfy our OSFI B-10 obligations?"*
- *"Build me a control documentation entry for patch management under B-13."*
- *"We operate a pipeline in Alberta. What does Reg 84/2024 require of us, and what isn't visible from the internet?"*
- *"Quebec FI holding personal information on Ontario residents — whose privacy law applies?"*
- *"A dealer got hit with ransomware, what CIRO resources exist specifically for this?"*

## Trigger phrases

The skill activates automatically on: `OSFI`, `B-10`, `B-13`, `E-21`, `I-CRT`, `FSRA`, `BCFSA`, `AMF`, `Loi 25`, `Law 25`, `CIRO`, `IIROC`, `Rule 3703`, `AER`, `Regulation 84`, `CSA Z246.1`, `PIPEDA`, `PHIPA`, `PIPA BC`, `PIPA AB`, `Canadian cyber`, `Canadian TPRM`, `Canadian privacy`, `Canadian breach notification`, `FRFI`, `Canadian credit union compliance`, `Ontario credit union`, `Quebec financial institution`, `Alberta energy security`, `Bill C-26`, `CCSPA`, `AIDA`.

## Disclaimer

This skill provides **informational guidance** based on publicly available Canadian regulatory and legislative publications. It does **not** constitute legal, audit, or professional compliance advice. Outputs should be reviewed by qualified Canadian professionals — a licensed Canadian attorney, Chief Compliance Officer, Privacy Officer, or equivalent — before being relied on for any material decision (breach notification, regulatory filing, enforcement correspondence, certification submission, or similar).

Regulatory requirements evolve. Always verify guidance against the current publication on the regulator's own website before acting. Authoritative source URLs for each regulator are listed in `skill/references/index.md`.

Citations in this skill reflect regulator publications current as of April 2026.
