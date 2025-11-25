from typing import Any, Callable

from src.utils.base import BaseSort


class BubbleSort(BaseSort):
    @staticmethod
    def execute(
        arr: list[Any],
        key: Callable[[Any], Any] | None = None,
        cmp: Callable[[Any, Any], int] | None = None,
    ) -> list[Any]:
        """
        Выполняет сортировку пузырьком.
        :param arr: Массив для сортировки.
        :param key: Функция извлечения ключа сравнения из элемента.
        :param cmp: Функция-компаратор для сравнения двух элементов.
        :return: Отсортированный массив.
        """
        n = len(arr)
        for i in range(n):
            for j in range(n - i - 1):
                if BaseSort.compare(arr[j], arr[j + 1], key, cmp) > 0:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr
