import argparse
from pathlib import Path

from evaluator.runner import evaluate, load_candidate


def main() -> int:
    parser = argparse.ArgumentParser(description="Evaluate interval-merging Python code.")
    parser.add_argument("--candidate", required=True, help="Path to candidate .py file")
    args = parser.parse_args()
    try:
        module = load_candidate(Path(args.candidate))
    except (FileNotFoundError, ImportError, AttributeError) as exc:
        parser.error(str(exc))
    results = evaluate(module.total_covered_length)
    passed = sum(r.passed for r in results)
    print(f"Results: {passed}/{len(results)} cases passed")
    for result in results:
        if not result.passed:
            print(
                f"\nFAIL: {result.name}\n"
                f"  expected: {result.expected!r}\n"
                f"  actual:   {result.actual!r}"
            )
            if result.error:
                print(f"  error:    {result.error}")
    return 0 if passed == len(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
