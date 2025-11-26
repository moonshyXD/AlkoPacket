import pytest

from src.utils.errors import TestCasesError
from src.utils.test_cases import TestCases


class TestTestCases:
    def test_rand_int_array(self) -> None:
        """
        Тест генерации случайного массива целых чисел.
        :return: None.
        """
        arr = TestCases.rand_int_array(10, 0, 100, seed=42)
        assert len(arr) == 10
        assert all(0 <= x <= 100 for x in arr)

    def test_rand_int_array_distinct(self) -> None:
        """
        Тест генерации массива с уникальными элементами.
        :return: None.
        """
        arr = TestCases.rand_int_array(5, 0, 10, distinct=True, seed=42)
        assert len(arr) == 5
        assert len(set(arr)) == 5

    def test_rand_int_array_distinct_error(self) -> None:
        """
        Тест ошибки при невозможности генерации уникальных элементов.
        :return: None.
        :raises TestCasesError: Если невозможно создать уникальные элементы.
        """
        with pytest.raises(TestCasesError):
            TestCases.rand_int_array(100, 0, 10, distinct=True)

    def test_rand_float_array(self) -> None:
        """
        Тест генерации случайного массива вещественных чисел.
        :return: None.
        """
        arr = TestCases.rand_float_array(10, seed=42)
        assert len(arr) == 10
        assert all(0.0 <= x <= 1.0 for x in arr)

    def test_nearly_sorted(self) -> None:
        """
        Тест генерации почти отсортированного массива.
        :return: None.
        """
        arr = TestCases.nearly_sorted(10, 2, seed=42)
        assert len(arr) == 10

    def test_reverse_sorted(self) -> None:
        """
        Тест генерации обратно отсортированного массива.
        :return: None.
        """
        arr = TestCases.reverse_sorted(5)
        assert arr == [4, 3, 2, 1, 0]

    def test_many_duplicates(self) -> None:
        """
        Тест генерации массива с дубликатами.
        :return: None.
        """
        arr = TestCases.many_duplicates(20, k_unique=3, seed=42)
        assert len(arr) == 20
        assert len(set(arr)) <= 3
