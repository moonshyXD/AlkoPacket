from typing import Any

from src.wrappers.benchmarks import Benchmarks


class TestBenchmarks:
    def test_timeit_once(self) -> None:
        bench = Benchmarks()
        time_taken = bench.timeit_once(lambda x: x * 2, 5)
        assert time_taken >= 0
        assert isinstance(time_taken, float)

    def test_timeit_once_with_kwargs(self) -> None:
        bench = Benchmarks()

        def func(a: int, b: int) -> int:
            return a + b

        time_taken = bench.timeit_once(func, 1, 2)
        assert time_taken >= 0

    def test_benchmark_sorts(self) -> None:
        bench = Benchmarks()

        arrays: dict[str, list[int]] = {
            "test1": [3, 1, 2],
            "test2": [5, 4, 3, 2, 1],
        }

        algos: dict[str, Any] = {"sorted": sorted}

        results = bench.benchmark_sorts(arrays, algos)

        assert "sorted" in results
        assert "test1" in results["sorted"]
        assert "test2" in results["sorted"]
        assert isinstance(results["sorted"]["test1"], float)
        assert isinstance(results["sorted"]["test2"], float)

    def test_benchmark_empty_arrays(self) -> None:
        bench = Benchmarks()
        arrays: dict[str, list[Any]] = {"empty": []}
        algos: dict[str, Any] = {"sorted": sorted}
        results = bench.benchmark_sorts(arrays, algos)
        assert results["sorted"]["empty"] >= 0
