from unittest import TestCase

from Calculator import Calculator


class CalculatorTest(TestCase):
    def test_sum(self):
        self.assertEqual(Calculator().sum(""), 0, "Empty string")

    def test_sum_string(self):
        self.assertEqual(Calculator().sum("1"), 1, "A number")

    def test_sum_different_string(self):
        self.assertEqual(Calculator().sum("2"), 2, "A different number")
