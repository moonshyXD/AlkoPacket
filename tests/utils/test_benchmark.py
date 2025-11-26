from typing import Callable

from src.utils.benchmarks import Benchmarks


class TestBenchmarks:
    def test_benchmark_sorts(self) -> None:
        """
        Тест запуска бенчмарков сортировок.
        :return: None.
        """
        arrays = {"test": [3, 1, 2]}
        algorithms = {"goose": sorted}
        bench = Benchmarks()
        results = bench.benchmark_sorts(arrays, algorithms)
        assert "goose" in results
        assert "test" in results["goose"]
        assert results["goose"]["test"] > 0

    def test_benchmark_data_structures(self) -> None:
        """
        Тест запуска бенчмарков очереди и стека.
        :return: None.
        """
        def test_ds() -> None:
            stack = []
            for i in range(100):
                stack.append(i)
            for _ in range(100):
                stack.pop()

        bench = Benchmarks()
        structures = {"test_structure": test_ds}
        results = bench.benchmark_data_structures(structures)
        assert "test_structure" in results
        assert results["test_structure"] > 0

    def test_benchmark_factorial_fibonacci(self) -> None:
        """
        Тест запуска бенчмарков факториала и Фибоначчи.
        :return: None.
        """
        def test_factorial(n: int) -> int:
            if n <= 1:
                return 1
            return n * test_factorial(n - 1)

        bench = Benchmarks()
        functions: dict[str, Callable[[int], int]] = {"goose": test_factorial}
        n_values = [5, 10]
        results = bench.benchmark_factorial_fibonacci(functions, n_values)
        assert "goose" in results
        assert 5 in results["goose"]
        assert 10 in results["goose"]
