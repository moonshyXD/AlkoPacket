from typing import Any, Callable

from src.utils.base import BaseSort


class QuickSort(BaseSort):
    @staticmethod
    def execute(
        arr: list[Any],
        key: Callable[[Any], Any] | None = None,
        cmp: Callable[[Any, Any], int] | None = None,
    ) -> list[Any]:
        """
        Выполняет быструю сортировку.
        :param arr: Массив для сортировки.
        :param key: Ключ сравнения эелементов.
        :param cmp: Компаратор сравнения элементов.
        :return: Отсортированный массив.
        """
        if len(arr) <= 1:
            return arr

        less_than = []
        higher_than = []
        equal = []
        pivot = arr[len(arr) // 2]
        for number in arr:
            cmp_res = QuickSort.compare(number, pivot, key, cmp)
            if cmp_res > 0:
                higher_than.append(number)
            elif cmp_res < 0:
                less_than.append(number)
            else:
                equal.append(number)

        return (
            QuickSort.execute(less_than, key, cmp)
            + equal
            + QuickSort.execute(higher_than, key, cmp)
        )
