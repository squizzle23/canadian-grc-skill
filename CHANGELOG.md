# Changelog

All notable changes to the Canadian GRC Skill will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] — 2026-04-21

### Added
- Initial public release.
- **Benchmark suite** — 35 test cases across 7 regulator groups with 175 verifiable assertions. Skill scored **89.7% vs. 42.9% baseline (+46.9 pts)** against Claude Sonnet 4.6. Benchmark harness (`evals/run_benchmark.py`) ships with the repo; anyone can re-run against their own account.
- Coverage of OSFI B-10, B-13 (+ Incident Advisory), E-21, and I-CRT.
- Coverage of FSRA IT Risk Management Guidance (GR0016INT) and Operational Resilience (CU0088APP).
- Coverage of BCFSA Third-Party Risk Management Guideline and Information Security Guideline.
- Coverage of AMF ICT Risk Management Guideline, Information Security Incident Regulation Implementation Guide, and Loi 25 (Quebec Law 25).
- Coverage of CIRO (formerly IIROC) Cyber Governance Guide, Cybersecurity Best Practices Guide, Cyber Incident Management Planning Guide, Ransomware Response Playbook, Fundamentals of Technology Risk Management, IDPC Rules, and Rule 3703.
- Coverage of Alberta Regulation 84/2024 — Security Management for Critical Infrastructure.
- Coverage of PIPEDA (federal) and PHIPA (Ontario).
- Orientation coverage of PIPA BC and PIPA AB.
- Cross-cutting coverage of Bill C-26 (CCSPA) and Bill C-27 (AIDA) — flagged as not-yet-in-force where applicable.
- Jurisdictional Router, Incident Reporting Matrix, Framework Adjacency table, Control Documentation Format, Evidence Principles, and Audience Adaptation guidance.
- `references/incident-playbook.md` — cross-regime breach decision tree.
- `references/evidence-catalog.md` — per-regulator examination evidence expectations.
- `references/index.md` — inventory with authoritative regulator source URLs.
- `.claude-plugin/marketplace.json` for Claude Code `/plugin marketplace` installation.

### Notes
- Citations reflect regulator publications current as of April 2026.
- CSA Z246.1 is not bundled — it is copyrighted by CSA Group and must be licensed separately for verbatim section work.
- Bill C-26 and AIDA status should be independently verified against Parliament of Canada before any reliance.
