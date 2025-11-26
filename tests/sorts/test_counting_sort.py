from src.sorts.counting_sort import CountingSort
from tests.base_test import BaseSortTest


class TestCountingSort(BaseSortTest):
    sort_class = CountingSort

    def test_large_numbers(self) -> None:
        arr = [100, 50, 75, 25]
        assert self.sort_class.execute(arr) == [25, 50, 75, 100]
