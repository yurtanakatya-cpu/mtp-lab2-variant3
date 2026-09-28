"""Задания повышенной сложности."""

import re
from pathlib import Path


def fibonacci_sequence(count: int) -> list[int]:
    """Вернуть первые ``count`` чисел последовательности Фибоначчи."""
    if isinstance(count, bool) or not isinstance(count, int):
        raise TypeError("Количество элементов должно быть целым числом")
    if count < 0:
        raise ValueError("Количество элементов не должно быть отрицательным")

    sequence = []
    first, second = 0, 1
    for _ in range(count):
        sequence.append(first)
        first, second = second, first + second
    return sequence


def word_frequencies(file_path: str | Path) -> dict[str, int]:
    """Подсчитать частоту слов в текстовом файле."""
    text = Path(file_path).read_text(encoding="utf-8")
    words = re.findall(r"[^\W\d_]+", text.casefold())

    frequencies = {}
    for word in words:
        frequencies[word] = frequencies.get(word, 0) + 1
    return dict(sorted(frequencies.items()))
