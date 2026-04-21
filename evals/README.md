# Benchmark Suite — Canadian GRC Skill

This directory contains the eval harness used to benchmark the Canadian GRC skill against baseline Claude performance.

## What's in here

- `evals.json` — 35 test cases across 7 regulator groups (OSFI, FSRA, BCFSA, AMF/Loi 25, CIRO, AER, Canadian Privacy), with 5 verifiable assertions per case = 175 total assertions.
- `run_benchmark.py` — Self-contained benchmark script. Calls the Anthropic API directly. No Claude Code required.
- `results.json` — Latest benchmark run output (machine-readable).
- `results.html` — Latest benchmark run output (human-readable, Sushegaad-style).

## Methodology

Each test case is run twice:

- **With skill** — The full `SKILL.md` plus all reference files (`references/*.md`) are injected into the subject Claude's system prompt.
- **Baseline** — Plain Claude with no skill context.

Both responses are then passed to an **independent grader Claude instance** which evaluates each of the test's 5 assertions and returns a pass/fail judgment with evidence.

This mirrors the approach described in the [LangChain skill-eval blog post](https://blog.langchain.com/evaluating-skills/) and matches the methodology used by the Sushegaad GRC skills repository (94% ± 4% vs. 93% ± 7% baseline).

## Running the benchmark

### Prerequisites

```bash
pip install anthropic
export ANTHROPIC_API_KEY=sk-ant-...
```

### Quick sanity check (2 cases, ~30 seconds, ~$0.10)

```bash
python3 run_benchmark.py --limit 2
```

### Full benchmark (35 cases, ~5 minutes, ~$2–4)

```bash
python3 run_benchmark.py
```

### Alternative: run against a specific skill version

```bash
python3 run_benchmark.py --skill ../skill/SKILL.md --out v1.0.0-results.json --html v1.0.0-results.html
```

## Cost estimates

At current Sonnet 4.6 pricing:

- Each test case = 2 subject calls + 2 grader calls = 4 API calls.
- Average ~25K input tokens (skill context is ~40KB = ~10K tokens; reference files add more when loaded) + ~2K output tokens.
- Estimated ~$0.08–0.12 per test case.
- Full 35-case run: **~$3–4**.

To reduce cost, swap the subject model to Haiku in `run_benchmark.py`:

```python
MODEL_SUBJECT = "claude-haiku-4-5"
```

This tests whether the skill lifts a weaker model; keep `MODEL_GRADER` as Sonnet or Opus for grading rigor.

## Test case design

Each test is structured as:

```json
{
  "id": 1,
  "regulator": "osfi",
  "prompt": "We're a Schedule I bank...",
  "expectations": [
    "References the OSFI Technology and Cyber Security Incident Reporting Advisory dated August 13, 2021",
    "States the 24-hour initial notification timeline",
    "Identifies that notification goes to both the Technology Risk Division and the Lead Supervisor",
    "Appends the PIPEDA privacy overlay obligation to notify the OPC",
    "Mentions that PIPEDA requires 24-month record retention"
  ]
}
```

Assertions are written to be **objectively verifiable** — the grader can determine pass/fail from the response text alone, no subjective judgment about quality or style. This keeps grading reliable across runs.

## Interpreting results

The headline number is **overall pass rate with skill vs. baseline**. A meaningful lift is +5 percentage points or more; smaller deltas indicate the skill is reinforcing things Claude already knows, which is still useful but less differentiating.

**Per-regulator breakdown** is where the skill usually earns its keep. Expect:

- Large lifts (+15 points or more) on specific-citation tasks: exact section numbers, exact effective dates, exact notification timelines.
- Moderate lifts (+5–15 points) on jurisdictional routing and privacy overlay mapping.
- Small lifts or ties on broad conceptual questions that general Claude already handles well.

**Failure modes worth watching for:**

- Baseline scoring higher than with-skill on a specific case — usually indicates the skill's instructions on that topic are unclear or contradictory.
- Grader disagreement across re-runs — assertions may be ambiguous; tighten the language.
- Variance between runs — the script doesn't set `temperature=0` (defaults to model default) so there's some natural spread. Run 2–3 times for stable numbers.

## Re-running after skill changes

When you modify the skill, re-run the benchmark to verify you haven't regressed. Compare `results.json` files before and after.

A good upgrade path: if a specific assertion fails consistently, the fix usually belongs in the relevant `references/regulators/*.md` file, not in `SKILL.md` itself.
