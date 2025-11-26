from src.sorts.heap_sort import HeapSort
from tests.base_test import BaseSortWithKeyTest


class TestHeapSort(BaseSortWithKeyTest):
    sort_class = HeapSort
