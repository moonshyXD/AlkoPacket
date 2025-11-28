from typing import Any

import pytest

from src.factorial_fibonacci.fibonacci import Fibonacci


@pytest.mark.parametrize(
    "func,n,expected",
    [
        (Fibonacci.fibo, 0, 0),
        (Fibonacci.fibo, 5, 5),
        (Fibonacci.fibo, 10, 55),
        (Fibonacci.fibo_recursive, 0, 0),
        (Fibonacci.fibo_recursive, 5, 5),
    ],
)
def test_fibonacci(func: Any, n: int, expected: int) -> None:
    """
    Проверка результатов для итеративных и рекурсивных чисел Фибоначчи
    :param func: функция вычисления чисел Фибоначчи
    :param n: входное число
    :param expected: ожидаемый результат
    """
    assert func(n) == expected
