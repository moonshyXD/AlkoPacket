import time
from copy import deepcopy
from typing import Any, Callable


class Benchmarks:
    def timeit_once(
        self, func: Callable[..., Any], *args: Any, **kwargs: Any
    ) -> float:
        """
        Измеряет время выполнения функции один раз.
        :param func: Функция для измерения.
        :param args: Позиционные аргументы для функции.
        :param kwargs: Именованные аргументы для функции.
        :return: Время выполнения в секундах.
        """
        start = time.perf_counter()
        func(*args, **kwargs)
        end = time.perf_counter()
        return end - start

    def benchmark_sorts(
        self,
        arrays: dict[str, list[Any]],
        algos: dict[str, Callable[..., Any]],
    ) -> dict[str, dict[str, float]]:
        """
        Бенчмарк алгоритмов сортировки на нескольких наборах данных.
        :param arrays: Словарь, название набора данных - массив.
        :param algos: Словарь, название алгоритма - функция сортировки.
        :return: Словарь с результатами, название алгоритма - время выполнения.
        """
        results: dict[str, dict[str, float]] = {}
        for algo_name, algo_func in algos.items():
            results[algo_name] = {}
            for array_name, array in arrays.items():
                array_copy = deepcopy(array)
                time_spended = self.timeit_once(algo_func, array_copy)
                results[algo_name][array_name] = time_spended

        return results

    def benchmark_factorial_fibonacci(
        self,
        functions: dict[str, Callable[[int], int]],
        n_values: list[int],
    ) -> dict[str, dict[int, float]]:
        """
        Бенчмарк функций вычисления факториала и чисел Фибоначчи.
        :param functions: Словарь, название функции - функция вычисления.
        :param n_values: Список значений n для тестирования.
        :return: Словарь с результатами, название функции - словарь {n: время}.
        """
        results: dict[str, dict[int, float]] = {}
        for func_name, func in functions.items():
            results[func_name] = {}
            for n in n_values:
                time_spended = self.timeit_once(func, n)
                results[func_name][n] = time_spended

        return results

    def benchmark_data_structures(
        self, structures: dict[str, Callable[[], None]]
    ) -> dict[str, float]:
        """
        Бенчмарк структур данных.
        :param structures: Словарь, название структуры - функция тестирования.
        :return: Словарь с результатами, название структуры - время выполнения.
        """
        results: dict[str, float] = {}
        for struct_name, struct_func in structures.items():
            time_spended = self.timeit_once(struct_func)
            results[struct_name] = time_spended

        return results
