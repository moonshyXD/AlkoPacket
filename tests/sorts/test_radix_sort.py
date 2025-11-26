from src.sorts.radix_sort import RadixSort
from tests.base_test import BaseSortTest


class TestRadixSort(BaseSortTest):
    sort_class = RadixSort

    def test_large_numbers(self) -> None:
        arr = [170, 45, 75, 90, 802, 24, 2, 66]
        result = self.sort_class.execute(arr)
        assert result == [2, 24, 45, 66, 75, 90, 170, 802]

    def test_multi_digit(self) -> None:
        arr = [329, 457, 657, 839]
        assert self.sort_class.execute(arr) == [329, 457, 657, 839]
