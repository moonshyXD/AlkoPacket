from typing import Any, Callable

from src.utils.base import BaseSort


class CountingSort(BaseSort):
    @staticmethod
    def execute(
        arr: list[Any],
        key: Callable[[Any], int] | None = None,
        cmp: Callable[[Any, Any], int] | None = None,
    ) -> list[Any]:
        """
        Выполняет сортировку подсчетом.
        :param arr: Массив целых чисел для сортировки.
        :param key: Не используется в данной реализации.
        :param cmp: Не используется в данной реализации.
        :return: Отсортированный массив целых чисел.
        """
        if not arr:
            return []
        keys = [key(item) if key else item for item in arr]
        min_val = min(keys)
        max_val = max(keys)
        count_range = max_val - min_val + 1
        count: list[list[Any]] = [[] for _ in range(count_range)]
        for i, item in enumerate(arr):
            k = keys[i] - min_val
            count[k].append(item)
        result: list[Any] = []
        for bucket in count:
            result.extend(bucket)
        return result
