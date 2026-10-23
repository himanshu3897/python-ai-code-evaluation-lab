import unittest

from evaluator.cases import build_cases
from evaluator.reference import total_covered_length
from evaluator.runner import evaluate
from examples.candidate_buggy import total_covered_length as buggy
from examples.candidate_good import total_covered_length as good


class EvaluationTests(unittest.TestCase):
    def test_reference_edges(self):
        self.assertEqual(total_covered_length([]), 0)
        self.assertEqual(total_covered_length([(0, 3), (3, 7)]), 7)
        self.assertEqual(total_covered_length([(0, 10), (2, 4)]), 10)
        self.assertEqual(total_covered_length([(5, 1), (2, 2)]), 0)

    def test_good_candidate_passes_all_cases(self):
        self.assertTrue(all(result.passed for result in evaluate(good, build_cases())))

    def test_buggy_candidate_is_detected(self):
        self.assertTrue(any(not result.passed for result in evaluate(buggy, build_cases())))


if __name__ == "__main__":
    unittest.main()
