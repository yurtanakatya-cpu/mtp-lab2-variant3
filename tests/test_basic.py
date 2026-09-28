"""Тесты заданий средней сложности."""

import unittest

from lab2_tasks import factorial, find_minimum, prime_numbers_up_to


class FactorialTests(unittest.TestCase):
    def test_factorial(self) -> None:
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)

    def test_factorial_rejects_negative_number(self) -> None:
        with self.assertRaises(ValueError):
            factorial(-1)

    def test_factorial_rejects_non_integer(self) -> None:
        with self.assertRaises(TypeError):
            factorial(3.5)
        with self.assertRaises(TypeError):
            factorial(True)


class PrimeNumbersTests(unittest.TestCase):
    def test_prime_numbers_up_to_one_hundred(self) -> None:
        expected = [
            2,
            3,
            5,
            7,
            11,
            13,
            17,
            19,
            23,
            29,
            31,
            37,
            41,
            43,
            47,
            53,
            59,
            61,
            67,
            71,
            73,
            79,
            83,
            89,
            97,
        ]
        self.assertEqual(prime_numbers_up_to(), expected)

    def test_prime_numbers_below_two(self) -> None:
        self.assertEqual(prime_numbers_up_to(1), [])


class MinimumTests(unittest.TestCase):
    def test_minimum(self) -> None:
        self.assertEqual(find_minimum([5, -4, 12, 0]), -4)
        self.assertEqual(find_minimum([2.5, 2.25, 3.0]), 2.25)

    def test_minimum_of_single_element(self) -> None:
        self.assertEqual(find_minimum([7]), 7)

    def test_empty_list_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            find_minimum([])


if __name__ == "__main__":
    unittest.main()
