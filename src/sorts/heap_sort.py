from src.utils.base import BaseSort


class HeapSort(BaseSort):
    @staticmethod
    def execute(arr: list[int]) -> list[int]:
        arr = arr.copy()
        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            HeapSort._heapify(arr, n, i)

        for i in range(n - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            HeapSort._heapify(arr, i, 0)

        return arr

    @staticmethod
    def _heapify(arr: list[int], heap_size: int, root_index: int) -> None:
        largest = root_index
        left = 2 * root_index + 1
        right = 2 * root_index + 2
        if left < heap_size and arr[left] > arr[largest]:
            largest = left

        if right < heap_size and arr[right] > arr[largest]:
            largest = right

        if largest != root_index:
            arr[largest], arr[root_index] = arr[root_index], arr[largest]
            HeapSort._heapify(arr, heap_size, largest)
