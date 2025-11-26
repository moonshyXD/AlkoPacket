from typing import Any

import pytest

from src.factorial_fibonachi.factorial import Factorial


@pytest.mark.parametrize(
    "func,n,expected",
    [
        (Factorial.factorial, 0, 1),
        (Factorial.factorial, 5, 120),
        (Factorial.factorial_recursive, 0, 1),
        (Factorial.factorial_recursive, 5, 120),
    ],
)
def test_factorial(func: Any, n: int, expected: int) -> None:
    assert func(n) == expected
