"""Задания повышенной сложности."""


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
