"""Командный интерфейс для заданий лабораторной работы №2."""

import argparse
import sys
from collections.abc import Sequence
from pathlib import Path

from lab2_tasks import (
    factorial,
    fibonacci_sequence,
    find_minimum,
    prime_numbers_up_to,
    word_frequencies,
)


def build_parser() -> argparse.ArgumentParser:
    """Создать парсер аргументов командной строки."""
    parser = argparse.ArgumentParser(description="Лабораторная работа №2")
    commands = parser.add_subparsers(dest="command", required=True)

    factorial_parser = commands.add_parser(
        "factorial", help="вычислить факториал числа"
    )
    factorial_parser.add_argument("number", type=int)

    commands.add_parser("primes", help="вывести простые числа до 100")

    minimum_parser = commands.add_parser(
        "minimum", help="найти минимальное число в списке"
    )
    minimum_parser.add_argument("numbers", nargs="+", type=float)

    fibonacci_parser = commands.add_parser(
        "fibonacci", help="сгенерировать числа Фибоначчи"
    )
    fibonacci_parser.add_argument("count", type=int)

    words_parser = commands.add_parser(
        "words", help="подсчитать частоту слов в файле"
    )
    words_parser.add_argument("file", type=Path)

    return parser


def run_command(arguments: argparse.Namespace) -> None:
    """Выполнить выбранную команду и вывести результат."""
    if arguments.command == "factorial":
        print(factorial(arguments.number))
    elif arguments.command == "primes":
        print(*prime_numbers_up_to())
    elif arguments.command == "minimum":
        print(f"{find_minimum(arguments.numbers):g}")
    elif arguments.command == "fibonacci":
        print(*fibonacci_sequence(arguments.count))
    elif arguments.command == "words":
        for word, count in word_frequencies(arguments.file).items():
            print(f"{word}: {count}")


def main(argv: Sequence[str] | None = None) -> int:
    """Запустить программу и вернуть код завершения."""
    parser = build_parser()
    arguments = parser.parse_args(argv)

    try:
        run_command(arguments)
    except (OSError, TypeError, ValueError) as error:
        print(f"Ошибка: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
