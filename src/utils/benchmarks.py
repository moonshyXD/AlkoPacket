import time
from copy import deepcopy
from typing import Any, Callable


class Benchmarks:
    def timeit_once(
        self, func: Callable[..., Any], *args: Any, **kwargs: Any
    ) -> float:
        """
        Замеряет время работы функции один раз
        :param func: функция для замера
        :param args: позиционные аргументы
        :param kwargs: именованные аргументы
        :return: время в секундах
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
        Бенчмаркит сортировки на разных массивах
        :param arrays: словарь название_массива -> массив
        :param algos: словарь название_алгоритма -> функция
        :return: результаты алгоритм -> массив -> время
        """
        results: dict[str, dict[str, float]] = {}
        for algo_name, algo_func in algos.items():
            results[algo_name] = {}
            for array_name, array in arrays.items():
                array_copy = deepcopy(array)
                time_spended = self.timeit_once(algo_func, array_copy)
                results[algo_name][array_name] = time_spended

        return results
