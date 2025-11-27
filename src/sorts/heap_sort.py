from typing import Any, Callable

from src.utils.base import BaseSort


class HeapSort(BaseSort):
    @staticmethod
    def execute(
        arr: list[Any],
        key: Callable[[Any], Any] | None = None,
        cmp: Callable[[Any, Any], int] | None = None,
    ) -> list[Any]:
        """
        Сортирует пирамидой
        :param arr: массив для сортировки
        :param key: ключ сравнения
        :param cmp: компаратор
        :return: отсортированный массив
        """
        arr = arr.copy()
        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            HeapSort._heapify(arr, n, i, key, cmp)

        for i in range(n - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            HeapSort._heapify(arr, i, 0, key, cmp)

        return arr

    @staticmethod
    def _heapify(
        arr: list[Any],
        heap_size: int,
        root_index: int,
        key: Callable[[Any], Any] | None = None,
        cmp: Callable[[Any, Any], int] | None = None,
    ) -> None:
        """
        Делает кучу из поддерева
        :param arr: массив
        :param heap_size: размер кучи
        :param root_index: корень поддерева
        :param key: ключ сравнения
        :param cmp: компаратор
        """
        largest = root_index
        left = 2 * root_index + 1
        right = 2 * root_index + 2
        if (
            left < heap_size
            and HeapSort.compare(arr[left], arr[largest], key, cmp) > 0
        ):
            largest = left

        if (
            right < heap_size
            and HeapSort.compare(arr[right], arr[largest], key, cmp) > 0
        ):
            largest = right

        if largest != root_index:
            arr[largest], arr[root_index] = arr[root_index], arr[largest]
            HeapSort._heapify(arr, heap_size, largest, key, cmp)
