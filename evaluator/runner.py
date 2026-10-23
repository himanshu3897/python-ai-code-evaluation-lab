import importlib.util
from dataclasses import dataclass
from pathlib import Path

from evaluator.cases import TestCase, build_cases
from evaluator.reference import total_covered_length


@dataclass(frozen=True)
class CaseResult:
    name: str
    passed: bool
    expected: object
    actual: object
    error: str | None = None


def load_candidate(path: str | Path):
    candidate_path = Path(path).resolve()
    if not candidate_path.is_file():
        raise FileNotFoundError(f"Candidate file not found: {candidate_path}")
    spec = importlib.util.spec_from_file_location("portfolio_candidate", candidate_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not load candidate module: {candidate_path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    if not callable(getattr(module, "total_covered_length", None)):
        raise AttributeError("Candidate must define total_covered_length(intervals).")
    return module


def evaluate(candidate, cases: list[TestCase] | None = None) -> list[CaseResult]:
    results = []
    for case in cases or build_cases():
        expected = total_covered_length(case.intervals)
        try:
            actual = candidate(list(case.intervals))
            valid = type(actual) is int
            passed = valid and actual == expected
            error = None if valid else f"Expected int, got {type(actual).__name__}"
            results.append(CaseResult(case.name, passed, expected, actual, error))
        except Exception as exc:
            results.append(
                CaseResult(case.name, False, expected, None, f"{type(exc).__name__}: {exc}")
            )
    return results
