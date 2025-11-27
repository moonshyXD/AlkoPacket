from typing import Any, Callable

from src.utils.base import BaseSort


class RadixSort(BaseSort):
    @staticmethod
    def execute(
        arr: list[Any],
        key: Callable[[Any], int] | None = None,
        cmp: Callable[[Any, Any], int] | None = None,
    ) -> list[Any]:
        """
        Делает поразрядную сортировку
        :param arr: массив чисел или объектов с целочисленным ключом
        :param key: ключ сравнения элементов
        :param cmp: компаратор
        :return: отсортированный массив
        """
        if not arr:
            return []

        keys = [key(item) if key else item for item in arr]
        max_num = max(keys)
        step = 1
        pairs: list[tuple[Any, int]] = list(zip(arr, keys, strict=True))
        while max_num // step > 0:
            n = len(pairs)
            res: list[tuple[Any, int]] = [(None, 0)] * n
            count = [0] * 10
            for _, k in pairs:
                index = (k // step) % 10
                count[index] += 1

            for i in range(1, 10):
                count[i] += count[i - 1]

            for i in range(n - 1, -1, -1):
                item, k = pairs[i]
                index = (k // step) % 10
                res[count[index] - 1] = (item, k)
                count[index] -= 1

            pairs = res
            step *= 10

        return [item for item, _ in pairs]
