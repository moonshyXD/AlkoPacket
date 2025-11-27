from typing import Any

import pytest

from src.utils.test_cases import TestCases


@pytest.fixture
def sample_array() -> list[int]:
    """
    Фикстура с тестовым массивом
    :return: массив случайных чисел
    """
    return TestCases.rand_int_array(8, 1, 9, seed=42)


@pytest.fixture
def sorted_array() -> list[int]:
    """
    Фикстура с отсортированным массивом
    :return: массив от 1 до 5
    """
    return list(range(1, 6))


@pytest.fixture
def reverse_sorted_array() -> list[int]:
    """
    Фикстура с обратно отсортированным массивом
    :return: массив в обратном порядке
    """
    return TestCases.reverse_sorted(5)


@pytest.fixture
def empty_array() -> list[Any]:
    """
    Фикстура с пустым массивом
    :return: пустой массив
    """
    return []


@pytest.fixture
def single_element_array() -> list[int]:
    """
    Фикстура с одним элементом
    :return: массив [42]
    """
    return [42]


@pytest.fixture
def duplicates_array() -> list[int]:
    """
    Фикстура с массивом с дубликатами
    :return: массив с повторяющимися элементами
    """
    return TestCases.many_duplicates(7, k_unique=3, seed=42)


@pytest.fixture
def negative_numbers() -> list[int]:
    """
    Фикстура с отрицательными числами
    :return: массив отрицательных чисел
    """
    return TestCases.rand_int_array(5, -5, -1, seed=42)


@pytest.fixture
def mixed_numbers() -> list[int]:
    """
    Фикстура со смешанными числами
    :return: массив с положительными и отрицательными числами
    """
    return TestCases.rand_int_array(5, -3, 3, seed=42)
