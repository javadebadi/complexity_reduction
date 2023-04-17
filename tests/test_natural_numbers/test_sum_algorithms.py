from unittest import TestCase
from complexity_reduction.natural_numbers import NaturalNumbersSum
import pytest


class TestNaturalNumbersSum(TestCase):

    def test_sum_1_to_n(self):
        self.assertEqual(
            0,
            NaturalNumbersSum.sum_from_1_to_n(0)
        )
        self.assertEqual(
            1,
            NaturalNumbersSum.sum_from_1_to_n(1)
        )
        self.assertEqual(
            500500,
            NaturalNumbersSum.sum_from_1_to_n(1000)
        )

        # very large numbers
        x = int(float(1E20)) + 1
        expected_result = 5000000000000000000150000000000000000001
        self.assertEqual(
            expected_result,
            NaturalNumbersSum.sum_from_1_to_n(x)
        )