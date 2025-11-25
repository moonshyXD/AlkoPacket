import random

from src.utils.errors import TestCasesError


class TestCases:
    @staticmethod
    def _set_seed(seed: int | None = None) -> None:
        """
        Устанавливает seed для генератора случайных чисел.
        :param seed: Значение seed или None, если менять seed не нужно.
        :return: None.
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
        Генерирует массив случайных целых чисел.
        :param n: Размер массива.
        :param lo: Нижняя граница значений (включительно).
        :param hi: Верхняя граница значений (включительно).
        :param distinct: Требовать ли уникальность элементов.
        :param seed: Значение seed для детерминированной генерации.
        :return: Список случайных целых чисел.
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
        Генерирует массив случайных вещественных чисел.
        :param n: Размер массива.
        :param lo: Нижняя граница значений.
        :param hi: Верхняя граница значений.
        :param seed: Значение seed для детерминированной генерации.
        :return: Список случайных вещественных чисел.
        """
        TestCases._set_seed(seed)
        return [random.uniform(lo, hi) for _ in range(n)]

    @staticmethod
    def nearly_sorted(
        n: int, swaps: int, seed: int | None = None
    ) -> list[int]:
        """
        Генерирует почти отсортированный массив.
        :param n: Размер массива.
        :param swaps: Количество случайных перестановок.
        :param seed: Значение seed для детерминированной генерации.
        :return: Почти отсортированный список целых чисел.
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
        Генерирует массив, отсортированный по убыванию.
        :param n: Размер массива.
        :return: Список целых чисел в порядке от n до 1.
        """
        return list(range(n - 1, -1, -1))

    @staticmethod
    def many_duplicates(
        n: int, k_unique: int = 5, seed: int | None = None
    ) -> list[int]:
        """
        Генерирует массив с большим количеством повторяющихся значений.
        :param n: Размер массива.
        :param k_unique: Количество уникальных значений.
        :param seed: Значение seed для детерминированной генерации.
        :return: Список целых чисел с дубликатами.
        """
        TestCases._set_seed(seed)
        values = list(range(k_unique))
        return [random.choice(values) for _ in range(n)]
