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
        Сортирует подсчётом
        :param arr: массив для сортировки
        :param key: функция ключа
        :param cmp: компаратор
        :return: отсортированный массив
        """
        if not arr:
            return []

        keys: list[int] = []
        for i in arr:
            if key:
                keys.append(key(i))
            else:
                keys.append(i)

        min_val = min(keys)
        max_val = max(keys)
        count_range = max_val - min_val + 1
        count: list[list[Any]] = [[] for _ in range(count_range)]
        for index, item in enumerate(arr):
            k = keys[index] - min_val
            count[k].append(item)

        result: list[Any] = []
        for bucket in count:
            result.extend(bucket)

        return result
