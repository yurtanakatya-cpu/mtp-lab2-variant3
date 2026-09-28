"""Задания средней сложности."""


def factorial(number: int) -> int:
    """Вычислить факториал неотрицательного целого числа."""
    if isinstance(number, bool) or not isinstance(number, int):
        raise TypeError("Факториал определён только для целых чисел")
    if number < 0:
        raise ValueError("Число не должно быть отрицательным")

    result = 1
    for factor in range(2, number + 1):
        result *= factor
    return result
