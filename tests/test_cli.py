"""Проверка командного интерфейса."""

import io
import unittest
from contextlib import redirect_stderr, redirect_stdout

from main import main


class CommandLineTests(unittest.TestCase):
    def run_cli(self, arguments: list[str]) -> tuple[int, str, str]:
        output = io.StringIO()
        errors = io.StringIO()
        with redirect_stdout(output), redirect_stderr(errors):
            exit_code = main(arguments)
        return exit_code, output.getvalue(), errors.getvalue()

    def test_factorial_command(self) -> None:
        exit_code, output, errors = self.run_cli(["factorial", "6"])
        self.assertEqual(exit_code, 0)
        self.assertEqual(output, "720\n")
        self.assertEqual(errors, "")

    def test_fibonacci_command(self) -> None:
        exit_code, output, errors = self.run_cli(["fibonacci", "7"])
        self.assertEqual(exit_code, 0)
        self.assertEqual(output, "0 1 1 2 3 5 8\n")
        self.assertEqual(errors, "")

    def test_invalid_value_returns_error(self) -> None:
        exit_code, output, errors = self.run_cli(["factorial", "-2"])
        self.assertEqual(exit_code, 1)
        self.assertEqual(output, "")
        self.assertIn("Ошибка:", errors)


if __name__ == "__main__":
    unittest.main()
