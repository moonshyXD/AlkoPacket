from typing import Any

import pytest

from src.wrappers.test_cases import TestCases


@pytest.fixture
def sample_array() -> list[int]:
    return TestCases.rand_int_array(8, 1, 9, seed=42)


@pytest.fixture
def sorted_array() -> list[int]:
    return list(range(1, 6))


@pytest.fixture
def reverse_sorted_array() -> list[int]:
    return TestCases.reverse_sorted(5)


@pytest.fixture
def empty_array() -> list[Any]:
    return []


@pytest.fixture
def single_element_array() -> list[int]:
    return [42]


@pytest.fixture
def duplicates_array() -> list[int]:
    return TestCases.many_duplicates(7, k_unique=3, seed=42)


@pytest.fixture
def negative_numbers() -> list[int]:
    return TestCases.rand_int_array(5, -5, -1, seed=42)


@pytest.fixture
def mixed_numbers() -> list[int]:
    return TestCases.rand_int_array(5, -3, 3, seed=42)


@pytest.fixture
def nearly_sorted_array() -> list[int]:
    return TestCases.nearly_sorted(10, swaps=2, seed=42)


@pytest.fixture
def large_array() -> list[int]:
    return TestCases.rand_int_array(100, 0, 1000, seed=42)


@pytest.fixture
def float_array() -> list[float]:
    return TestCases.rand_float_array(10, 0.0, 10.0, seed=42)


@pytest.fixture
def distinct_array() -> list[int]:
    return TestCases.rand_int_array(10, 0, 50, distinct=True, seed=42)
