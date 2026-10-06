"""Regression tests for numeric values written to strict JSON snapshots."""
import math
import unittest

from data_utils import number


class NumberTests(unittest.TestCase):
    def test_valid_numbers_are_converted_to_float(self):
        for value, expected in ((0, 0.0), (-3, -3.0), (2.5, 2.5), ("12.5", 12.5)):
            with self.subTest(value=value):
                result = number(value)
                self.assertIsInstance(result, float)
                self.assertEqual(result, expected)

    def test_booleans_are_not_treated_as_numbers(self):
        for value in (True, False):
            with self.subTest(value=value):
                self.assertIsNone(number(value))

    def test_invalid_and_nonfinite_values_become_none(self):
        for value in (None, "", "not a number", [], {}, math.nan, math.inf,
                      -math.inf, "NaN", "Infinity", "-Infinity"):
            with self.subTest(value=value):
                self.assertIsNone(number(value))


if __name__ == "__main__":
    unittest.main()
