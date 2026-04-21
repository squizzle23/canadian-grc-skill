# Canadian GRC & Cyber Law — Claude Skills

Expert-level Canadian regulatory compliance guidance for Claude, covering OSFI, FSRA, BCFSA, AMF/Loi 25, CIRO, AER, and the full Canadian privacy stack.

**Benchmarked across 35 test cases with 175 verifiable assertions. Skill scored 89.7% vs. a baseline of 42.9% — a +46.9 percentage point lift over baseline Claude Sonnet 4.6.**

[![Release: v1.0.0](https://img.shields.io/badge/Release-v1.0.0-brightgreen.svg)](https://github.com/squizzle23/canadian-grc-skill/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](./LICENSE)
[![Benchmark: 89.7%](https://img.shields.io/badge/Benchmark-89.7%25-success.svg)](./evals/results.html)
[![Baseline Lift: +46.9 pts](https://img.shields.io/badge/Baseline%20Lift-%2B46.9%20pts-blue.svg)](./evals/results.html)
[![Built with Claude](https://img.shields.io/badge/Built%20with-Claude-orange.svg)](https://claude.ai)

---

## Why this skill exists

There are mature, well-maintained Claude Skills for SOC 2, ISO 27001, NIST CSF, HIPAA, FedRAMP, GDPR, PCI DSS, and ISO 42001. None of them cover the Canadian regulatory stack — which is fragmented across federal and provincial regulators, layered with privacy law, and different again in Quebec (Loi 25) and in Alberta's OT/energy sector (AER Reg 84).

This skill fills that gap. It behaves the same way as the other GRC skills: it activates automatically when a conversation touches Canadian regulation, grounds every answer in authoritative regulator text, and refuses to fabricate section numbers or control IDs. The skill is evaluated against 175 verifiable assertions drawn directly from the regulator publications themselves.

## Coverage

- **OSFI** — B-10 (Third-Party Risk Management), B-13 (Technology and Cyber Risk Management), B-13 Incident Advisory, E-21 (Operational Risk Management and Resilience), I-CRT (Intelligence-led Cyber Resilience Testing)
- **FSRA** (Ontario) — IT Risk Management Guidance (GR0016INT), Operational Resilience (CU0088APP)
- **BCFSA** (British Columbia) — Third-Party Risk Management Guideline, Information Security Guideline
- **AMF** (Quebec) — ICT Risk Management Guideline, Information Security Incident Regulation
- **CIRO** (formerly IIROC) — Cyber Governance, Best Practices, Incident Management, Ransomware Playbook, IDPC Rules, Rule 3703
- **AER** (Alberta) — Regulation 84/2024 — Security Management for Critical Infrastructure
- **Privacy** — PIPEDA (federal), PHIPA (Ontario health), Loi 25 (Quebec), PIPA BC, PIPA AB
- **Emerging** — Bill C-26 (Critical Cyber Systems Protection Act), Bill C-27 (AIDA)

## Benchmark results

Methodology follows the approach described in the [LangChain skill-evaluation blog](https://blog.langchain.com/evaluating-skills/) and the [Sushegaad GRC skills repo](https://github.com/Sushegaad/Claude-Skills-Governance-Risk-and-Compliance). Each test case is run twice — once with the skill context injected, once without — and both responses are graded by an independent Claude Sonnet 4.6 instance against the test's 5 verifiable assertions.

| Configuration | Pass rate |
|---|---|
| **With skill installed** | **89.7% (157/175)** |
| Without skill (baseline Claude Sonnet 4.6) | 42.9% (75/175) |
| **Delta** | **+46.9 percentage points** |

### By regulator

| Regulator | With skill | Baseline | Delta |
|---|---|---|---|
| **AER** (Alberta energy) | 100% (25/25) | 12% (3/25) | **+88.0 pts** |
| **BCFSA** (BC financial) | 96% (24/25) | 32% (8/25) | **+64.0 pts** |
| **OSFI** (federal financial) | 84% (21/25) | 32% (8/25) | **+52.0 pts** |
| **CIRO** (investment dealers) | 84% (21/25) | 44% (11/25) | **+40.0 pts** |
| **FSRA** (Ontario financial) | 96% (24/25) | 60% (15/25) | **+36.0 pts** |
| **AMF + Loi 25** (Quebec) | 76% (19/25) | 48% (12/25) | **+28.0 pts** |
| **Canadian Privacy** (PIPEDA/PHIPA/PIPA) | 92% (23/25) | 72% (18/25) | **+20.0 pts** |

The skill adds the most measurable value where baseline Claude genuinely lacks the knowledge — Alberta Reg 84, the BCFSA guideline (published October 2025), and specific OSFI Advisory notification timelines. On broad Canadian privacy questions, baseline Claude already performs reasonably (72%); the skill lifts accuracy on specific statutory citations and jurisdictional routing.

📊 **[View full case-by-case results →](./evals/results.html)**

The eval harness (`evals/run_benchmark.py`) and test suite (`evals/evals.json`) are in this repository. Anyone can re-run the benchmark against their own account. See [`evals/README.md`](./evals/README.md) for instructions.

## Installation

### Option 1 — Claude Code marketplace (recommended for developers)

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

Once installed, the skill activates automatically when a conversation touches Canadian regulation. You do not need to invoke it by name.

## What's in the repository

```
canadian-grc-skill/
├── README.md                              # This file
├── LICENSE                                # MIT
├── CHANGELOG.md
├── CONTRIBUTING.md
├── .claude-plugin/
│   └── marketplace.json                   # Claude Code /plugin marketplace manifest
├── skill/                                 # The skill itself
│   ├── README.md                          # Per-skill README (design choices, trigger phrases, examples)
│   ├── SKILL.md                           # Entry point
│   └── references/
│       ├── index.md
│       ├── incident-playbook.md
│       ├── evidence-catalog.md
│       └── regulators/
│           ├── osfi.md
│           ├── fsra.md
│           ├── amf-loi25.md
│           ├── ciro.md
│           ├── aer-reg84.md
│           ├── privacy-federal.md
│           └── privacy-provincial.md
└── evals/                                 # Benchmark suite
    ├── README.md                          # How to re-run the benchmark
    ├── evals.json                         # 35 test cases, 175 assertions
    ├── run_benchmark.py                   # Self-contained Python harness
    ├── results.json                       # Latest run output (machine-readable)
    └── results.html                       # Latest run output (human-readable)
```

## Design choices

**Jurisdiction-first.** Every answer resolves jurisdiction and sector before citing requirements. The Jurisdictional Router prevents common mistakes like applying OSFI to a credit union or B-13 to an Alberta pipeline operator.

**Citations are grounded or absent.** The skill will say "I need to check the reference for the exact section" rather than invent a plausible-sounding one. Wrong section numbers collapse credibility with regulated buyers.

**Privacy always layered.** Sector-regulator questions involving personal information always append the applicable privacy commissioner obligation — OPC under PIPEDA, CAI under Loi 25, IPC Ontario under PHIPA, OIPC BC under PIPA BC, OIPC Alberta under PIPA AB.

**IT vs. OT distinction.** AER's Reg 84 is OT-scoped (SCADA, pipelines, substations). The skill does not apply IT-centric frameworks like B-13 to OT environments without a corporate-IT interconnect rationale.

**Framework ≠ regulation.** SOC 2, ISO 27001, and NIST CSF are assurance frameworks, not Canadian regulatory compliance. The skill is explicit about what each does and doesn't satisfy under Canadian law.

## Example prompts

Try these to see the skill in action:

- *"We're an Ontario credit union and had a ransomware incident yesterday involving member data. Walk me through every reporting obligation."*
- *"How does OSFI B-10 differ from the BCFSA Third-Party Risk Management Guideline?"*
- *"Does a SOC 2 Type 2 report from our cloud vendor satisfy our OSFI B-10 obligations?"*
- *"Build me a control documentation entry for patch management under B-13."*
- *"We operate a pipeline in Alberta. What does Reg 84/2024 require of us, and what isn't visible from the internet?"*
- *"Quebec FI holding personal information on Ontario residents — whose privacy law applies?"*
- *"A dealer got hit with ransomware — what CIRO resources exist specifically for this?"*

## Verification and dates

Citations reflect regulator publications current as of April 2026. Notable dates covered:

- OSFI B-10: April 30, 2023
- OSFI B-13: July 31, 2022
- OSFI B-13 Incident Advisory: August 13, 2021
- OSFI E-21: August 22, 2024
- OSFI I-CRT: April 1, 2023
- FSRA IT Risk Guidance (GR0016INT): effective April 1, 2024
- FSRA Operational Resilience (CU0088APP): effective March 1, 2024
- BCFSA Third-Party Risk Management Guideline: October 28, 2025 (effective January 1, 2028)
- BCFSA Information Security Guideline: March 2025
- AMF ICT Risk Management Guideline: February 2020
- AMF Incident Reg Application Guide: July 10, 2025
- Loi 25 consolidation: December 11, 2025
- AER Regulation 84/2024: effective May 31, 2025
- CIRO IDPC Rules: February 22, 2024

Full authoritative source URLs for every regulator are listed in [`skill/references/index.md`](./skill/references/index.md).

## Contributing

Found an error, an outdated citation, or a regulator this skill should cover? Open an issue or a pull request. See [`CONTRIBUTING.md`](./CONTRIBUTING.md) for guidelines.

**Coverage additions most wanted:**
- **FINTRAC** (AML/ATF) reporting obligations
- **OPC compliance agreements and findings** as precedent reference
- **Canadian Centre for Cyber Security (CCCS)** advisories relevant to Bill C-26
- **Provincial health privacy laws** beyond PHIPA — PIPA BC PHI, Alberta HIA, Quebec ARPPHS

## License

MIT — see [`LICENSE`](./LICENSE). This skill may be used, modified, and redistributed for any purpose, commercial or non-commercial. Attribution appreciated but not required.

The reference files contain original analytical summaries derived from public regulator publications. Where those publications are themselves the property of the Government of Canada or a provincial Crown, Crown copyright applies to the underlying text. The MIT license covers only the analytical summaries and structure in this repository — not the underlying regulatory text. Users who need verbatim regulator language should retrieve it directly from the regulator's website.

## Disclaimer

This skill provides **informational guidance** based on publicly available Canadian regulatory and legislative publications. It does **not** constitute legal, audit, or professional compliance advice. Outputs should be reviewed by qualified Canadian professionals — a licensed Canadian attorney, Chief Compliance Officer, Privacy Officer, or equivalent — before being relied on for any material decision (breach notification, regulatory filing, enforcement correspondence, certification submission, or similar).

Regulatory requirements evolve. Always verify guidance against the current publication on the regulator's own website before acting.

## Credits

Built in the spirit of the broader Claude Skills compliance ecosystem (SOC 2, ISO 27001, NIST CSF, HIPAA, FedRAMP, GDPR, PCI DSS, ISO 42001). These skills compose naturally — SOC 2 for buyer assurance, ISO 27001 for the ISMS, and Canadian GRC for the regulatory overlay that sits on top.

Benchmark methodology inspired by [Hemant Naik's Sushegaad GRC skills](https://github.com/Sushegaad/Claude-Skills-Governance-Risk-and-Compliance) and the [LangChain skill-evaluation approach](https://blog.langchain.com/evaluating-skills/).
