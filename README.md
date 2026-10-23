# Python AI Code Evaluation Lab

**Independent portfolio demo — not client work.** No employer code, confidential data, or proprietary material is included.

A small, dependency-free Python harness demonstrating problem design, adversarial edge cases, reference implementations, and repeatable evaluation of candidate code.

## Challenge
Given integer half-open intervals `[start, end)`, return their total covered length. Intervals with `start > end` are ignored; zero-length intervals contribute zero.

This catches common mistakes around unsorted input, overlaps, nested ranges, touching boundaries, duplicates, negative coordinates, and invalid ranges.

## Run
Requires Python 3.10+.

```bash
python -m unittest discover -s tests -v
python -m evaluator.cli --candidate examples/candidate_good.py
python -m evaluator.cli --candidate examples/candidate_buggy.py
```

Candidate interface:
```python
def total_covered_length(intervals: list[tuple[int, int]]) -> int:
    ...
```

The suite contains explicit edge cases plus 40 seeded, deterministic generated cases. The intentionally buggy candidate demonstrates how a plausible implementation can fail hidden-style tests.

**Security note:** this imports candidate code in the current Python process. It is a correctness demo, not a secure sandbox for untrusted code. A production system should run submissions in an isolated container or restricted worker with resource limits and no network access.

## Walkthrough
1. Explain the input contract and half-open intervals.
2. Show the reference solution and sorting/merging strategy.
3. Run both candidate implementations.
4. Discuss failures and how test cases expose assumptions.
5. Explain why deterministic generated cases help reproducibility.

Possible extensions: JSON reports, more problem families, mutation testing, timeouts, and isolated execution.
