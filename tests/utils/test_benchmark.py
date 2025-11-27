from src.utils.benchmarks import Benchmarks


class TestBenchmarks:
    def test_benchmark_sorts(self) -> None:
        """
        Тест запуска бенчмарков сортировок
        """
        arrays = {"test": [3, 1, 2]}
        algorithms = {"goose": sorted}
        bench = Benchmarks()
        results = bench.benchmark_sorts(arrays, algorithms)
        assert "goose" in results
        assert "test" in results["goose"]
        assert results["goose"]["test"] > 0
