import random
from dataclasses import dataclass


@dataclass(frozen=True)
class TestCase:
    name: str
    intervals: list[tuple[int, int]]


def build_cases() -> list[TestCase]:
    cases = [
        TestCase("empty input", []),
        TestCase("single interval", [(2, 8)]),
        TestCase("disjoint intervals", [(0, 2), (5, 9)]),
        TestCase("overlapping intervals", [(1, 5), (3, 8)]),
        TestCase("nested interval", [(0, 10), (2, 4), (3, 7)]),
        TestCase("unsorted input", [(8, 12), (0, 3), (2, 9)]),
        TestCase("touching intervals", [(0, 3), (3, 7)]),
        TestCase("negative coordinates", [(-8, -2), (-4, 2)]),
        TestCase("zero-length intervals", [(2, 2), (2, 5), (5, 5)]),
        TestCase("invalid interval ignored", [(1, 4), (9, 3), (6, 8)]),
        TestCase("duplicate intervals", [(1, 6), (1, 6), (1, 6)]),
        TestCase("all invalid or empty", [(5, 1), (3, 3), (9, 4)]),
        TestCase("large coordinates", [(-10**9, 10**9), (0, 2)]),
    ]
    rng = random.Random(20261023)
    for i in range(40):
        values = []
        for _ in range(rng.randint(0, 12)):
            a, b = rng.randint(-25, 25), rng.randint(-25, 25)
            values.append((a, b))
        cases.append(TestCase(f"seeded random case {i + 1:02d}", values))
    return cases
