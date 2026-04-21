#!/usr/bin/env python3
"""Fill in missing eval results by running only specified case IDs."""

import json
import os
import sys
from pathlib import Path

# Reuse everything from the main script
sys.path.insert(0, str(Path(__file__).parent))
from run_benchmark import (
    Anthropic, load_skill, load_references, build_full_skill_context,
    run_one_eval, aggregate, render_html,
)


def main():
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        sys.exit("Set ANTHROPIC_API_KEY")

    missing_ids = [int(x) for x in sys.argv[1].split(",")]
    print(f"Running missing cases: {missing_ids}", flush=True)

    with open("evals.json") as f:
        all_cases = json.load(f)["evals"]
    with open("results.json") as f:
        existing = json.load(f)

    to_run = [c for c in all_cases if c["id"] in missing_ids]
    skill_md = load_skill(Path("../skill/SKILL.md"))
    refs = load_references(Path("../skill"))
    skill_ctx = build_full_skill_context(skill_md, refs)

    client = Anthropic(api_key=api_key)
    new_results = []
    for i, case in enumerate(to_run, 1):
        print(f"[{i}/{len(to_run)}] Case {case['id']} ({case.get('regulator','?')})... ", end="", flush=True)
        try:
            r = run_one_eval(client, case, skill_ctx)
            new_results.append(r)
            print(f"skill={r['with_skill']['passed']}/{r['with_skill']['total']} "
                  f"base={r['baseline']['passed']}/{r['baseline']['total']}", flush=True)
        except Exception as e:
            print(f"FAILED: {e}", flush=True)

    merged = existing["results"] + new_results
    merged.sort(key=lambda r: r["id"])
    summary = aggregate(merged)

    with open("results.json", "w") as f:
        json.dump({"summary": summary, "results": merged}, f, indent=2)
    with open("results.html", "w") as f:
        f.write(render_html(merged, summary))

    print(f"\nFINAL: {summary['with_skill']['rate']*100:.1f}% with skill "
          f"vs {summary['baseline']['rate']*100:.1f}% baseline "
          f"(+{summary['delta']*100:.1f} pts)")


if __name__ == "__main__":
    main()
