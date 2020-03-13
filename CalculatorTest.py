from unittest import TestCase

from Calculator import Calculator


class CalculatorTest(TestCase):
    def test_sum(self):
        self.assertEqual(Calculator().sum(""), 0, "Empty string")

    def test_sum_string(self):
        self.assertEqual(Calculator().sum("1"), 1, "A number")

    def test_sum_different_string(self):
        self.assertEqual(Calculator().sum("2"), 2, "A different number")

    def test_sum_concatenated_numbers(self):
        self.assertEqual(Calculator().sum("1,3"), 4, "Numbers concatenated by comma")

    def test_sum_more_concatenated_numbers(self):
        self.assertEqual(Calculator().sum("1,2,3,4"), 10, "More numbers concatenated by comma")

    def test_sum_numbers_separated_by_colon(self):
        self.assertEqual(Calculator().sum("5:6&7:8&9"), 35, "Numbers separated by colons and ampersand")
