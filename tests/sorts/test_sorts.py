from typing import Any

import pytest

from src.sorts.bubble_sort import BubbleSort
from src.sorts.bucket_sort import BucketSort
from src.sorts.counting_sort import CountingSort
from src.sorts.heap_sort import HeapSort
from src.sorts.quick_sort import QuickSort
from src.sorts.radix_sort import RadixSort


@pytest.mark.parametrize(
    "sort_class",
    [BubbleSort, HeapSort, QuickSort],
)
class TestSortsWithKeyAndCmp:
    def test_empty(self, sort_class: Any, empty_array: list[Any]) -> None:
        """
        Тест сортировки пустого массива
        :param sort_class: класс сортировки
        :param empty_array: пустой массив
        """
        assert sort_class.execute(empty_array) == []

    def test_single(
        self, sort_class: Any, single_element_array: list[int]
    ) -> None:
        """
        Тест сортировки массива с одним элементом
        :param sort_class: класс сортировки
        :param single_element_array: массив с одним элементом
        """
        assert sort_class.execute(single_element_array) == [42]

    def test_sorted(self, sort_class: Any, sorted_array: list[int]) -> None:
        """
        Тест сортировки отсортированного массива
        :param sort_class: класс сортировки
        :param sorted_array: отсортированный массив
        """
        result = sort_class.execute(sorted_array.copy())
        assert result == [1, 2, 3, 4, 5]

    def test_reverse(
        self, sort_class: Any, reverse_sorted_array: list[int]
    ) -> None:
        """
        Тест сортировки массива в обратном порядке
        :param sort_class: класс сортировки
        :param reverse_sorted_array: массив в обратном порядке
        """
        result = sort_class.execute(reverse_sorted_array.copy())
        assert result == [0, 1, 2, 3, 4]

    def test_random(self, sort_class: Any, sample_array: list[int]) -> None:
        """
        Тест сортировки случайного массива
        :param sort_class: класс сортировки
        :param sample_array: случайный массив
        """
        result = sort_class.execute(sample_array.copy())
        assert result == sorted(sample_array)

    def test_duplicates(
        self, sort_class: Any, duplicates_array: list[int]
    ) -> None:
        """
        Тест сортировки массива с дубликатами
        :param sort_class: класс сортировки
        :param duplicates_array: массив с дубликатами
        """
        result = sort_class.execute(duplicates_array.copy())
        assert result == sorted(duplicates_array)

    def test_negative(
        self, sort_class: Any, negative_numbers: list[int]
    ) -> None:
        """
        Тест сортировки отрицательных чисел
        :param sort_class: класс сортировки
        :param negative_numbers: массив отрицательных чисел
        """
        result = sort_class.execute(negative_numbers.copy())
        assert result == sorted(negative_numbers)

    def test_mixed(self, sort_class: Any, mixed_numbers: list[int]) -> None:
        """
        Тест сортировки смешанных чисел
        :param sort_class: класс сортировки
        :param mixed_numbers: массив со смешанными числами
        """
        result = sort_class.execute(mixed_numbers.copy())
        assert result == sorted(mixed_numbers)

    def test_with_key(self, sort_class: Any) -> None:
        """
        Тест сортировки с ключом
        :param sort_class: Класс сортировки
        """
        arr = [-3, -1, 2, -4]
        result = sort_class.execute(arr, key=abs)
        assert result == [-1, 2, -3, -4]

    def test_with_cmp(self, sort_class: Any) -> None:
        """
        Тест сортировки с компаратором
        :param sort_class: класс сортировки
        """

        def cmp(a: int, b: int) -> int:
            return (b > a) - (b < a)

        result = sort_class.execute([1, 3, 2], cmp=cmp)
        assert result == [3, 2, 1]


@pytest.mark.parametrize("sort_class", [CountingSort, RadixSort])
class TestSortsWithoutKeyAndCmp:
    def test_empty(self, sort_class: Any, empty_array: list[Any]) -> None:
        """
        Тест сортировки пустого массива
        :param sort_class: класс сортировки
        :param empty_array: пустой массив
        """
        assert sort_class.execute(empty_array) == []

    def test_single(
        self, sort_class: Any, single_element_array: list[int]
    ) -> None:
        """
        Тест сортировки массива с одним элементом
        :param sort_class: класс сортировки
        :param single_element_array: массив с одним элементом
        """
        assert sort_class.execute(single_element_array) == [42]

    def test_sorted(self, sort_class: Any, sorted_array: list[int]) -> None:
        """
        Тест сортировки отсортированного массива
        :param sort_class: класс сортировки
        :param sorted_array: атсортированный массив
        """
        result = sort_class.execute(sorted_array.copy())
        assert result == [1, 2, 3, 4, 5]

    def test_reverse(
        self, sort_class: Any, reverse_sorted_array: list[int]
    ) -> None:
        """
        Тест сортировки массива в обратном порядке
        :param sort_class: класс сортировки
        :param reverse_sorted_array: массив в обратном порядке
        """
        result = sort_class.execute(reverse_sorted_array.copy())
        assert result == [0, 1, 2, 3, 4]

    def test_random(self, sort_class: Any, sample_array: list[int]) -> None:
        """
        Тест сортировки случайного массива
        :param sort_class: класс сортировки
        :param sample_array: случайный массив
        """
        result = sort_class.execute(sample_array.copy())
        assert result == sorted(sample_array)

    def test_duplicates(
        self, sort_class: Any, duplicates_array: list[int]
    ) -> None:
        """
        Тест сортировки массива с дубликатами
        :param sort_class: класс сортировки
        :param duplicates_array: массив с дубликатами
        """
        result = sort_class.execute(duplicates_array.copy())
        assert result == sorted(duplicates_array)


class TestRadixSort:
    def test_multi_digit(self) -> None:
        """
        Тест сортировки многозначных чисел
        """
        arr = [32, 457, 8309, 657]
        assert RadixSort.execute(arr) == [32, 457, 657, 8309]


class TestBucketSort:
    def test_empty(self) -> None:
        """
        Тест сортировки пустого массива
        """
        assert BucketSort.execute([]) == []

    def test_sorted(self) -> None:
        """
        Тест сортировки отсортированного массива
        """
        arr = [1.0, 2.0, 3.0, 4.0, 5.0]
        assert BucketSort.execute(arr.copy()) == arr

    def test_random(self) -> None:
        """
        Тест сортировки случайного массива
        """
        arr = [3.2, 1.5, 4.8, 2.1, 5.9]
        assert BucketSort.execute(arr.copy()) == sorted(arr)
