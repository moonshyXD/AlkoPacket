from typing import Any, Callable

from src.utils.base import BaseSort


class BucketSort(BaseSort):
    @staticmethod
    def execute(
        arr: list[Any],
        key: Callable[[Any], Any] | None = None,
        cmp: Callable[[Any, Any], int] | None = None,
        buckets: int | None = None,
    ) -> list[Any]:
        """
        Выполняет блочную сортировку
        :param arr: массив для сортировки
        :param key: ключ сравнения элементов
        :param cmp: компаратор сравнения элементов
        :param buckets: количество блоков для разделения массива
        :return: отсортированный массив
        """
        if buckets is None:
            buckets = 10
        if not arr:
            return []

        float_arr = [float(x) for x in arr]
        array_buckets: list[list[float]] = [[] for _ in range(buckets)]
        max_item = max(float_arr, key=key) if key else max(float_arr)
        max_val = key(max_item) if key else max_item

        for item in float_arr:
            val = key(item) if key else item
            normalized = float(val) / (float(max_val) + 1)
            bucket_number = min(int(normalized * buckets), buckets - 1)
            array_buckets[bucket_number].append(item)

        sorted_arr: list[float] = []
        for bucket in array_buckets:
            sorted_arr.extend(BucketSort._insertion_sort(bucket, key, cmp))

        return sorted_arr

    @staticmethod
    def _insertion_sort(
        arr: list[float],
        key: Callable[[Any], Any] | None = None,
        cmp: Callable[[Any, Any], int] | None = None,
    ) -> list[float]:
        """
        Сортирует блок вставками
        :param arr: числа для сортировки в блоке
        :param key: функция ключа сравнения
        :param cmp: функция компаратора
        :return: отсортированный список
        """
        for a in range(1, len(arr)):
            b = a
            while (
                b > 0 and BucketSort.compare(arr[b - 1], arr[b], key, cmp) > 0
            ):
                arr[b - 1], arr[b] = arr[b], arr[b - 1]
                b -= 1

        return arr
