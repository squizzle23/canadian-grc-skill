#!/usr/bin/env python3
"""
Benchmark harness for the Canadian GRC skill.

Runs each eval twice — once with the SKILL.md injected into the system prompt,
once without — and grades both responses with an independent Claude call against
the test's 5 verifiable assertions.

Usage:
    export ANTHROPIC_API_KEY=sk-ant-...
    python run_benchmark.py --evals evals.json --skill ../skill/SKILL.md --out results.json

Outputs:
    results.json         — machine-readable results for every test and assertion
    results.html         — human-readable report (Sushegaad-style)

No external dependencies beyond `anthropic` Python SDK and `jinja2` for HTML.
"""

import argparse
import json
import os
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from pathlib import Path

try:
    from anthropic import Anthropic
except ImportError:
    sys.exit(
        "Missing dependency. Install with:\n"
        "    pip install anthropic jinja2\n"
    )

# Model choice — using Sonnet for balance of cost and capability.
# If you want maximum rigor, swap to claude-opus-4-7.
MODEL_SUBJECT = "claude-sonnet-4-6"
MODEL_GRADER = "claude-sonnet-4-6"

# How many concurrent requests. Set to 1 by default because the skill context is
# ~36K tokens and free/low-tier API accounts have 30K TPM input limits.
# Raise this if you have higher rate limits.
CONCURRENCY = 1

# Seconds to sleep between sequential calls (basic rate-limit buffer)
SLEEP_BETWEEN_CALLS = 2

SUBJECT_SYSTEM_PROMPT_BASELINE = (
    "You are Claude, a helpful AI assistant. Respond to the user's question using your general knowledge."
)

GRADER_SYSTEM_PROMPT = """You are an expert grader evaluating whether a model's response satisfies specific factual assertions about Canadian regulatory compliance.

You will be given:
1. The original user question
2. The model's response
3. A list of verifiable assertions

For each assertion, determine whether the response satisfies it. Be strict — the assertion must be substantively addressed in the response, not merely adjacent. Regulatory content requires precision: wrong section numbers, wrong dates, wrong regulators, or wrong jurisdictions are failures.

Grading rules:
- "Identifies X as Y" passes if the response correctly identifies X as Y.
- "States the X timeline" passes only if the response states the correct timeline.
- "References section X" passes if the specific section is named; "references the regulation generally" is not enough.
- "Appends the privacy overlay" passes only if the response actually mentions the applicable privacy commissioner obligation.
- If the response is factually wrong about the assertion's subject, mark FAIL even if something related is mentioned.

Return your grading as JSON only, with no prose before or after:

{
  "assertions": [
    {"text": "<assertion text>", "passed": true/false, "evidence": "<brief quote or explanation>"},
    ...
  ]
}
"""


def load_skill(skill_path: Path) -> str:
    """Load the SKILL.md content."""
    text = skill_path.read_text()
    # Strip YAML frontmatter — Claude doesn't need it at runtime
    if text.startswith("---"):
        end = text.find("---", 3)
        if end != -1:
            text = text[end + 3:].lstrip()
    return text


def load_references(skill_dir: Path) -> dict:
    """Load every reference file so the skill has full context."""
    refs = {}
    ref_dir = skill_dir / "references"
    if not ref_dir.exists():
        return refs
    for path in ref_dir.rglob("*.md"):
        rel = path.relative_to(skill_dir)
        refs[str(rel)] = path.read_text()
    return refs


def build_full_skill_context(skill_md: str, references: dict) -> str:
    """Assemble SKILL.md + all references into a single string for system prompt."""
    parts = [skill_md, "\n\n---\n\n# Reference Files\n\n"]
    for rel_path, content in sorted(references.items()):
        parts.append(f"## File: {rel_path}\n\n{content}\n\n---\n\n")
    return "".join(parts)


def call_subject(client: Anthropic, prompt: str, system_parts: list, max_retries: int = 5) -> str:
    """Run a single subject-arm query and return the response text.

    system_parts is a list of system prompt blocks. The first block (skill context)
    is cached with Anthropic's prompt caching feature to avoid billing repeat input.
    Retries with exponential backoff on 429 rate-limit errors.
    """
    for attempt in range(max_retries):
        try:
            resp = client.messages.create(
                model=MODEL_SUBJECT,
                max_tokens=2000,
                system=system_parts,
                messages=[{"role": "user", "content": prompt}],
            )
            return "\n".join(b.text for b in resp.content if b.type == "text")
        except Exception as e:
            msg = str(e)
            if "429" in msg or "rate_limit" in msg.lower():
                wait = min(60, (2 ** attempt) * 5)
                print(f"    Rate limit hit, waiting {wait}s...", flush=True)
                time.sleep(wait)
                continue
            raise
    raise RuntimeError(f"call_subject exhausted {max_retries} retries")


def call_grader(client: Anthropic, prompt: str, response: str, expectations: list, max_retries: int = 5) -> dict:
    """Grade a response against its expectations. Returns dict with 'assertions' list.

    Retries on JSON parse failures with a corrective follow-up, and on rate-limit
    errors with exponential backoff.
    """
    assertions_text = "\n".join(f"{i+1}. {e}" for i, e in enumerate(expectations))
    user_msg = (
        f"ORIGINAL QUESTION:\n{prompt}\n\n"
        f"MODEL RESPONSE:\n{response[:6000]}\n\n"
        f"ASSERTIONS TO GRADE:\n{assertions_text}\n\n"
        f"Return valid JSON only. Keep evidence strings under 200 chars and do not use unescaped quotes inside them."
    )

    last_error = None
    for attempt in range(max_retries):
        try:
            resp = client.messages.create(
                model=MODEL_GRADER,
                max_tokens=3000,
                system=GRADER_SYSTEM_PROMPT,
                messages=[{"role": "user", "content": user_msg}],
            )
            text = "\n".join(b.text for b in resp.content if b.type == "text").strip()
            text = re.sub(r"^```json\s*|^```\s*|\s*```$", "", text, flags=re.MULTILINE).strip()

            try:
                return json.loads(text)
            except json.JSONDecodeError as e:
                match = re.search(r"\{.*\}", text, re.DOTALL)
                if match:
                    try:
                        return json.loads(match.group())
                    except json.JSONDecodeError:
                        pass
                last_error = e
                user_msg = (
                    f"Your previous response was not valid JSON. Error: {e}\n\n"
                    f'Return ONLY a JSON object shaped like {{"assertions": [{{"text": "...", "passed": true, "evidence": "..."}}]}}\n\n'
                    f"ORIGINAL QUESTION:\n{prompt}\n\n"
                    f"MODEL RESPONSE:\n{response[:3000]}\n\n"
                    f"ASSERTIONS TO GRADE:\n{assertions_text}\n\n"
                    f"Keep evidence under 100 chars. Escape all quotes."
                )
        except Exception as e:
            msg = str(e)
            if "429" in msg or "rate_limit" in msg.lower():
                wait = min(60, (2 ** attempt) * 5)
                print(f"    Grader rate limit, waiting {wait}s...", flush=True)
                time.sleep(wait)
                continue
            last_error = e

    return {
        "assertions": [
            {"text": e_text, "passed": False, "evidence": f"grader error: {last_error}"}
            for e_text in expectations
        ]
    }


def run_one_eval(client: Anthropic, eval_case: dict, skill_context: str) -> dict:
    """Execute both arms of one eval and grade both. Returns aggregated result."""
    prompt = eval_case["prompt"]
    expectations = eval_case["expectations"]

    # Build cached system blocks for with-skill arm.
    # The skill context is identical across every call, so we cache it.
    with_skill_system = [
        {
            "type": "text",
            "text": "You are Claude, responding to a user question. The following skill instructions apply — follow them exactly.",
        },
        {
            "type": "text",
            "text": skill_context,
            "cache_control": {"type": "ephemeral"},
        },
        {
            "type": "text",
            "text": "Respond to the user's question using the skill above.",
        },
    ]
    baseline_system = [
        {
            "type": "text",
            "text": "You are Claude, a helpful AI assistant. Respond to the user's question using your general knowledge.",
        }
    ]

    # Arm 1: with skill
    try:
        with_skill_response = call_subject(client, prompt, with_skill_system)
        time.sleep(SLEEP_BETWEEN_CALLS)
        with_skill_grading = call_grader(client, prompt, with_skill_response, expectations)
        time.sleep(SLEEP_BETWEEN_CALLS)
    except Exception as e:
        with_skill_response = f"[ERROR: {e}]"
        with_skill_grading = {
            "assertions": [
                {"text": e_text, "passed": False, "evidence": f"subject error: {e}"}
                for e_text in expectations
            ]
        }

    # Arm 2: baseline
    try:
        baseline_response = call_subject(client, prompt, baseline_system)
        time.sleep(SLEEP_BETWEEN_CALLS)
        baseline_grading = call_grader(client, prompt, baseline_response, expectations)
        time.sleep(SLEEP_BETWEEN_CALLS)
    except Exception as e:
        baseline_response = f"[ERROR: {e}]"
        baseline_grading = {
            "assertions": [
                {"text": e_text, "passed": False, "evidence": f"subject error: {e}"}
                for e_text in expectations
            ]
        }

    with_skill_passed = sum(1 for a in with_skill_grading["assertions"] if a["passed"])
    baseline_passed = sum(1 for a in baseline_grading["assertions"] if a["passed"])

    return {
        "id": eval_case["id"],
        "regulator": eval_case.get("regulator"),
        "prompt": prompt,
        "expectations": expectations,
        "with_skill": {
            "response": with_skill_response,
            "assertions": with_skill_grading["assertions"],
            "passed": with_skill_passed,
            "total": len(expectations),
        },
        "baseline": {
            "response": baseline_response,
            "assertions": baseline_grading["assertions"],
            "passed": baseline_passed,
            "total": len(expectations),
        },
    }


def aggregate(results: list) -> dict:
    """Produce summary statistics."""
    total_assertions = sum(r["with_skill"]["total"] for r in results)
    with_skill_passed = sum(r["with_skill"]["passed"] for r in results)
    baseline_passed = sum(r["baseline"]["passed"] for r in results)

    # Per-regulator breakdown
    by_reg = {}
    for r in results:
        reg = r["regulator"] or "unknown"
        if reg not in by_reg:
            by_reg[reg] = {"with_skill_passed": 0, "baseline_passed": 0, "total": 0, "cases": 0}
        by_reg[reg]["with_skill_passed"] += r["with_skill"]["passed"]
        by_reg[reg]["baseline_passed"] += r["baseline"]["passed"]
        by_reg[reg]["total"] += r["with_skill"]["total"]
        by_reg[reg]["cases"] += 1

    for reg, d in by_reg.items():
        d["with_skill_rate"] = d["with_skill_passed"] / d["total"] if d["total"] else 0
        d["baseline_rate"] = d["baseline_passed"] / d["total"] if d["total"] else 0
        d["delta"] = d["with_skill_rate"] - d["baseline_rate"]

    return {
        "total_cases": len(results),
        "total_assertions": total_assertions,
        "with_skill": {
            "passed": with_skill_passed,
            "rate": with_skill_passed / total_assertions if total_assertions else 0,
        },
        "baseline": {
            "passed": baseline_passed,
            "rate": baseline_passed / total_assertions if total_assertions else 0,
        },
        "delta": (with_skill_passed - baseline_passed) / total_assertions if total_assertions else 0,
        "by_regulator": by_reg,
        "timestamp": datetime.now(datetime.now().astimezone().tzinfo).isoformat(),
        "model_subject": MODEL_SUBJECT,
        "model_grader": MODEL_GRADER,
    }


def render_html(results: list, summary: dict) -> str:
    """Generate a standalone HTML report (no external CSS)."""
    overall_with = summary["with_skill"]["rate"] * 100
    overall_base = summary["baseline"]["rate"] * 100
    delta_pts = summary["delta"] * 100

    # Build regulator rows
    reg_rows = []
    for reg, d in sorted(summary["by_regulator"].items()):
        reg_rows.append(
            f"<tr><td><strong>{reg}</strong></td>"
            f"<td>{d['cases']}</td>"
            f"<td>{d['total']}</td>"
            f"<td class='pass'>{d['with_skill_passed']}/{d['total']} ({d['with_skill_rate']*100:.0f}%)</td>"
            f"<td class='base'>{d['baseline_passed']}/{d['total']} ({d['baseline_rate']*100:.0f}%)</td>"
            f"<td class='delta'>{'+' if d['delta'] >= 0 else ''}{d['delta']*100:.0f} pts</td></tr>"
        )

    # Build case detail rows
    case_rows = []
    for r in results:
        ws = r["with_skill"]
        bl = r["baseline"]
        assertions_html = "".join(
            f"<li class='{'pass' if a['passed'] else 'fail'}'>"
            f"<strong>{'✓' if a['passed'] else '✗'}</strong> {a['text']}"
            f"<br><em>{a.get('evidence', '')}</em></li>"
            for a in ws["assertions"]
        )
        case_rows.append(
            f"<div class='case'>"
            f"<h3>Case {r['id']} — {r['regulator']}</h3>"
            f"<p class='prompt'><strong>Prompt:</strong> {r['prompt']}</p>"
            f"<p class='score'>With skill: <strong class='pass'>{ws['passed']}/{ws['total']}</strong> · "
            f"Baseline: <strong class='base'>{bl['passed']}/{bl['total']}</strong></p>"
            f"<details><summary>With-skill grading detail</summary><ul>{assertions_html}</ul></details>"
            f"</div>"
        )

    html = f"""<!DOCTYPE html>
<html><head><meta charset='utf-8'><title>Canadian GRC Skill — Benchmark Results</title>
<style>
body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; max-width: 960px; margin: 2em auto; padding: 0 1em; color: #1a1a1a; }}
h1 {{ border-bottom: 3px solid #c00; padding-bottom: 0.3em; }}
.summary {{ background: #f5f5f5; padding: 1em 1.5em; border-radius: 8px; margin: 1em 0; }}
.headline {{ font-size: 1.3em; margin: 0.5em 0; }}
table {{ width: 100%; border-collapse: collapse; margin: 1em 0; }}
th, td {{ text-align: left; padding: 0.5em 0.75em; border-bottom: 1px solid #e0e0e0; }}
th {{ background: #fafafa; }}
.pass {{ color: #008000; }}
.base {{ color: #666; }}
.fail {{ color: #b00020; }}
.delta {{ color: #0060b0; font-weight: 600; }}
.case {{ margin: 1em 0; padding: 1em; border-left: 3px solid #ddd; }}
.case h3 {{ margin-top: 0; }}
.prompt {{ color: #555; font-style: italic; }}
.score {{ font-weight: 500; }}
details summary {{ cursor: pointer; color: #0060b0; }}
ul {{ padding-left: 1.5em; }}
li.pass {{ color: #008000; }}
li.fail {{ color: #b00020; }}
li em {{ color: #666; font-weight: normal; }}
footer {{ margin-top: 3em; padding-top: 1em; border-top: 1px solid #e0e0e0; color: #666; font-size: 0.9em; }}
</style></head><body>

<h1>Canadian GRC Skill — Benchmark Results</h1>

<div class='summary'>
  <p class='headline'>
    <strong>With skill:</strong> <span class='pass'>{overall_with:.1f}%</span> &nbsp;|&nbsp;
    <strong>Baseline:</strong> <span class='base'>{overall_base:.1f}%</span> &nbsp;|&nbsp;
    <strong>Delta:</strong> <span class='delta'>{'+' if delta_pts >= 0 else ''}{delta_pts:.1f} pts</span>
  </p>
  <p>{summary['total_cases']} test cases · {summary['total_assertions']} verifiable assertions · graded by independent {summary['model_grader']} instance</p>
  <p>Subject model: <code>{summary['model_subject']}</code> · Grader model: <code>{summary['model_grader']}</code> · Run: {summary['timestamp']}</p>
</div>

<h2>Results by Regulator</h2>
<table>
  <thead><tr><th>Regulator</th><th>Cases</th><th>Assertions</th><th>With skill</th><th>Baseline</th><th>Delta</th></tr></thead>
  <tbody>{''.join(reg_rows)}</tbody>
</table>

<h2>Case-by-Case Detail</h2>
{''.join(case_rows)}

<footer>
  <p>Canadian GRC Skill v1.0.0 · Benchmarked {summary['timestamp']} · MIT License</p>
</footer>
</body></html>"""
    return html


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--evals", default="evals.json", help="Path to evals.json")
    parser.add_argument("--skill", default="../skill/SKILL.md", help="Path to SKILL.md")
    parser.add_argument("--out", default="results.json", help="Output JSON path")
    parser.add_argument("--html", default="results.html", help="Output HTML path")
    parser.add_argument("--limit", type=int, default=None, help="Only run first N cases (for debugging)")
    args = parser.parse_args()

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        sys.exit("Set ANTHROPIC_API_KEY environment variable.")

    evals_path = Path(args.evals)
    skill_path = Path(args.skill)
    skill_dir = skill_path.parent

    with open(evals_path) as f:
        eval_suite = json.load(f)
    cases = eval_suite["evals"]
    if args.limit:
        cases = cases[: args.limit]

    skill_md = load_skill(skill_path)
    references = load_references(skill_dir)
    skill_context = build_full_skill_context(skill_md, references)

    print(f"Loaded {len(cases)} test cases", flush=True)
    print(f"Skill context: {len(skill_context):,} characters", flush=True)
    print(f"Running benchmark with {CONCURRENCY} concurrent workers...\n", flush=True)

    client = Anthropic(api_key=api_key)

    # Resume mode: if results.json exists, load previously completed cases
    # and skip them. This makes the benchmark restartable across interruptions.
    existing_results = {}
    if Path(args.out).exists():
        try:
            with open(args.out) as f:
                prev = json.load(f)
            for r in prev.get("results", []):
                existing_results[r["id"]] = r
            if existing_results:
                print(f"Resuming: {len(existing_results)} cases already completed", flush=True)
        except Exception as e:
            print(f"Couldn't load previous results ({e}), starting fresh", flush=True)

    results = list(existing_results.values())

    for i, case in enumerate(cases, 1):
        if case["id"] in existing_results:
            print(f"[{i}/{len(cases)}] Case {case['id']} ({case.get('regulator', '?')})... SKIP (already done)", flush=True)
            continue
        print(f"[{i}/{len(cases)}] Case {case['id']} ({case.get('regulator', '?')})... ", end="", flush=True)
        try:
            result = run_one_eval(client, case, skill_context)
            results.append(result)
            ws = result["with_skill"]
            bl = result["baseline"]
            print(f"skill={ws['passed']}/{ws['total']} base={bl['passed']}/{bl['total']}", flush=True)

            # Checkpoint after every case so we don't lose progress
            results.sort(key=lambda r: r["id"])
            partial_summary = aggregate(results)
            with open(args.out, "w") as f:
                json.dump({"summary": partial_summary, "results": results}, f, indent=2)
        except Exception as e:
            print(f"FAILED: {e}", flush=True)

    results.sort(key=lambda r: r["id"])
    summary = aggregate(results)

    with open(args.out, "w") as f:
        json.dump({"summary": summary, "results": results}, f, indent=2)

    with open(args.html, "w") as f:
        f.write(render_html(results, summary))

    print(f"\n{'=' * 60}")
    print(f"OVERALL: {summary['with_skill']['rate']*100:.1f}% with skill vs "
          f"{summary['baseline']['rate']*100:.1f}% baseline "
          f"(+{summary['delta']*100:.1f} pts)")
    print(f"{'=' * 60}")
    print(f"Wrote {args.out} and {args.html}")


if __name__ == "__main__":
    main()
