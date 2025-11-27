import random

from src.utils.errors import TestCasesError


class TestCases:
    @staticmethod
    def _set_seed(seed: int | None = None) -> None:
        """
        Устанавливает seed для random
        :param seed: значение seed или None
        """
        if seed is not None:
            random.seed(seed)

    @staticmethod
    def rand_int_array(
        n: int,
        lo: int,
        hi: int,
        distinct: bool = False,
        seed: int | None = None,
    ) -> list[int]:
        """
        Генерирует случайные целые числа
        :param n: размер массива
        :param lo: нижняя граница
        :param hi: верхняя граница
        :param distinct: делать ли все уникальными
        :param seed: seed для воспроизводимости
        :return: список случайных чисел
        """
        TestCases._set_seed(seed)
        if distinct and n > (hi - lo + 1):
            raise TestCasesError(
                f"Невозможно сгенерировать {n}",
                f"неповторяющихся элементов в промежутке [{lo}, {hi}]",
            )

        if distinct:
            return random.sample(range(lo, hi + 1), n)

        return [random.randint(lo, hi) for _ in range(n)]

    @staticmethod
    def rand_float_array(
        n: int, lo: float = 0.0, hi: float = 1.0, seed: int | None = None
    ) -> list[float]:
        """
        Генерирует случайные float-ы
        :param n: размер массива
        :param lo: нижняя граница
        :param hi: верхняя граница
        :param seed: seed для воспроизводимости
        :return: список случайных вещественных чисел
        """
        TestCases._set_seed(seed)
        return [random.uniform(lo, hi) for _ in range(n)]

    @staticmethod
    def nearly_sorted(
        n: int, swaps: int, seed: int | None = None
    ) -> list[int]:
        """
        Создаёт почти отсортированный массив
        :param n: размер массива
        :param swaps: количество случайных перестановок
        :param seed: seed для воспроизводимости
        :return: почти отсортированный список
        """
        TestCases._set_seed(seed)
        array = list(range(n))
        for _ in range(swaps):
            i = random.randint(0, n - 1)
            j = random.randint(0, n - 1)
            array[i], array[j] = array[j], array[i]

        return array

    @staticmethod
    def reverse_sorted(n: int) -> list[int]:
        """
        Создаёт массив отсортированный по убыванию
        :param n: размер массива
        :return: числа от n-1 до 0
        """
        return list(range(n - 1, -1, -1))

    @staticmethod
    def many_duplicates(
        n: int, k_unique: int = 5, seed: int | None = None
    ) -> list[int]:
        """
        Много дублей в массиве
        :param n: размер массива
        :param k_unique: сколько уникальных значений
        :param seed: seed для воспроизводимости
        :return: список с повторениями
        """
        TestCases._set_seed(seed)
        values = list(range(k_unique))
        return [random.choice(values) for _ in range(n)]
