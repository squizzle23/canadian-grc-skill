# Contributing to the Canadian GRC Skill

Thank you for considering a contribution. Canadian regulatory coverage is fragmented and evolves constantly, so well-grounded additions and corrections are genuinely welcome.

## What kind of contributions are welcome

- **Citation corrections** — section numbers, effective dates, publisher identities, or URL changes.
- **Coverage additions** — new regulators, statutes, or guidance documents not yet covered. High-priority gaps are listed in the README.
- **Clearer explanations** — reworded summaries that make a regulation easier to navigate without losing precision.
- **Structural improvements** — better task routing, clearer audience adaptation, improved jurisdictional coverage.
- **Real-world examples** — anonymized prompts and expected-behaviour notes that help the skill trigger and perform reliably.

## What is NOT welcome

- Verbatim reproduction of copyrighted third-party commentary (law firm memos, paid research reports, paywalled standards like CSA Z246.1).
- Client-specific or identifying information in examples.
- Speculative regulatory interpretation presented as fact. This skill's credibility rests on never fabricating citations.
- Sales or marketing content. The skill is an advisory tool, not a positioning asset for any vendor.

## How to contribute

### Reporting an issue

Open a GitHub issue including:

1. What's wrong — the specific file, line, or claim.
2. The correct information.
3. A source reference — regulator publication URL, statute citation, or official guidance.

### Submitting a pull request

1. Fork the repository.
2. Create a feature branch.
3. Make your changes. Keep them surgical — one coherent change per PR.
4. Update the `references/index.md` if you've added a regulator or authoritative source.
5. Open the PR with a clear description of what changed and why.

## Style guide for reference content

- **Ground every section number in a real regulator publication.** If the guideline uses plain-language expectations, use plain-language expectations — do not invent section numbers to make the text look more structured.
- **Distinguish mandatory from recommended language.** "Must" and "shall" are enforcement hooks; "should" and "expected" are guidance. Keep the distinction visible.
- **Identify jurisdiction and sector first.** Every regulator file should open with "Who this applies to" — no implicit assumptions.
- **Always map the privacy overlay.** Any sector-regulator question about incidents or personal information needs the applicable privacy commissioner obligation appended.
- **Never frame content as sales or positioning material.** This is an advisor skill, not a pitch asset.
- **Keep it dense but skimmable.** Compliance professionals are reading to act, not to admire your prose.

## Verifying regulator references

Current URLs for primary sources (verify before publishing):

- OSFI — https://www.osfi-bsif.gc.ca/en/guidance
- FSRA — https://www.fsrao.ca
- BCFSA — https://www.bcfsa.ca
- AMF — https://lautorite.qc.ca
- CIRO — https://www.ciro.ca
- AER — https://www.aer.ca (regulation text at Alberta King's Printer)
- OPC (PIPEDA) — https://www.priv.gc.ca
- IPC Ontario (PHIPA) — https://www.ipc.on.ca
- OIPC BC — https://www.oipc.bc.ca
- OIPC Alberta — https://www.oipc.ab.ca
- CAI Quebec (Loi 25) — https://www.cai.gouv.qc.ca
- Statutes (federal) — https://laws-lois.justice.gc.ca
- Statutes (Ontario) — https://www.ontario.ca/laws
- Statutes (Quebec) — https://www.legisquebec.gouv.qc.ca
- Statutes (BC) — https://www.bclaws.gov.bc.ca
- Statutes (Alberta) — Alberta King's Printer

## Licensing

By contributing, you agree that your contributions will be licensed under the MIT License of this repository. You retain your attribution rights and may be added to a CONTRIBUTORS file on request.
