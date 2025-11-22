import time
from copy import deepcopy
from typing import Callable


class Benchmarks:
    def timeit_once(self, func: Callable, *args, **kwargs) -> float:
        start = time.perf_counter()
        func(*args, **kwargs)
        end = time.perf_counter()
        return end - start

    def benchmark_sorts(
        self, arrays: dict[str, list], algos: dict[str, Callable]
    ) -> dict[str, dict[str, float]]:
        results: dict[str, dict[str, float]] = {}

        for algo_name, algo_func in algos.items():
            results[algo_name] = {}

            for array_name, array in arrays.items():
                array_copy = deepcopy(array)
                time_spended = self.timeit_once(algo_func, array_copy)
                results[algo_name][array_name] = time_spended

        return results
