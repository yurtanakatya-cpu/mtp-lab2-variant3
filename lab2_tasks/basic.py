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


def prime_numbers_up_to(limit: int = 100) -> list[int]:
    """Вернуть простые числа от 2 до ``limit`` включительно."""
    if isinstance(limit, bool) or not isinstance(limit, int):
        raise TypeError("Граница должна быть целым числом")
    if limit < 2:
        return []

    prime_numbers = []
    for candidate in range(2, limit + 1):
        is_prime = True
        for divisor in range(2, int(candidate ** 0.5) + 1):
            if candidate % divisor == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(candidate)
    return prime_numbers
