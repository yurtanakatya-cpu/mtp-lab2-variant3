"""Тесты заданий повышенной сложности."""

import tempfile
import unittest
from pathlib import Path

from lab2_tasks import fibonacci_sequence, word_frequencies


class FibonacciTests(unittest.TestCase):
    def test_fibonacci_sequence(self) -> None:
        self.assertEqual(fibonacci_sequence(0), [])
        self.assertEqual(fibonacci_sequence(1), [0])
        self.assertEqual(fibonacci_sequence(8), [0, 1, 1, 2, 3, 5, 8, 13])

    def test_negative_count_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            fibonacci_sequence(-1)

    def test_non_integer_count_is_rejected(self) -> None:
        with self.assertRaises(TypeError):
            fibonacci_sequence(4.5)
        with self.assertRaises(TypeError):
            fibonacci_sequence(False)


class WordFrequenciesTests(unittest.TestCase):
    def test_word_frequencies_ignore_case_and_punctuation(self) -> None:
        text = "Код, код и ещё КОД! Python — python."
        with tempfile.TemporaryDirectory() as directory:
            file_path = Path(directory) / "text.txt"
            file_path.write_text(text, encoding="utf-8")

            self.assertEqual(
                word_frequencies(file_path),
                {"ещё": 1, "и": 1, "код": 3, "python": 2},
            )

    def test_empty_file_has_no_words(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            file_path = Path(directory) / "empty.txt"
            file_path.write_text("", encoding="utf-8")
            self.assertEqual(word_frequencies(file_path), {})

    def test_missing_file_is_reported(self) -> None:
        with self.assertRaises(FileNotFoundError):
            word_frequencies("missing-file.txt")


if __name__ == "__main__":
    unittest.main()
