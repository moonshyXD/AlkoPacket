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
        Выполняет блочную сортировку.
        :param arr: Массив для сортировки.
        :param key: Ключ сравнения эелементов.
        :param cmp: Компаратор сравнения элементов.
        :param buckets: Количество блоков для разделения массива.
        :return: Отсортированный массив.
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

        sorted_array: list[float] = []
        for bucket in array_buckets:
            sorted_array.extend(BucketSort._insertion_sort(bucket, key, cmp))

        return sorted_array

    @staticmethod
    def _insertion_sort(
        arr: list[float],
        key: Callable[[Any], Any] | None = None,
        cmp: Callable[[Any, Any], int] | None = None,
    ) -> list[float]:
        """
        Сортирует массив внутри одного блока методом вставок.
        :param arr: Список чисел для сортировки внутри блока.
        :param key: Функция извлечения ключа сравнения из элемента.
        :param cmp: Функция-компаратор для сравнения двух элементов.
        :return: Отсортированный список.
        """
        for a in range(1, len(arr)):
            b = a
            while (
                b > 0 and BucketSort.compare(arr[b - 1], arr[b], key, cmp) > 0
            ):
                arr[b - 1], arr[b] = arr[b], arr[b - 1]
                b -= 1

        return arr
