from functools import partial
from typing import Any, Callable

import typer

from src.interface.config import sort_command_map
from src.sorts.bucket_sort import BucketSort
from src.utils.benchmarks import Benchmarks
from src.utils.logger import Logger
from src.utils.test_cases import TestCases

Logger.setup_logging()


def run_benchmark() -> None:
    """
    Запускает бенчмарк сортировок
    """
    n = typer.prompt(
        "Размер массивов", type=int, default=1000, show_default=False
    )

    Logger.start_execution(f"Benchmark (n={n})")

    int_arrays = {
        "Случайные целые": TestCases.rand_int_array(n, 0, 10000),
        "Обратно отсортированные": TestCases.reverse_sorted(n),
        "Почти отсортированные": TestCases.nearly_sorted(n, n // 10),
        "С дубликатами": TestCases.many_duplicates(n),
    }

    float_arrays = {
        "Случайные вещественные": TestCases.rand_float_array(n, 0.0, 10000.0),
    }

    bench = Benchmarks()

    int_algos: dict[str, Callable[[list[Any]], list[Any]]] = {}
    for name, func in sort_command_map.items():
        if name == "Bucket-sort":
            continue
        if name in ["Radix-sort", "Counting-sort"]:
            int_algos[name] = func
        else:
            int_algos[name] = partial(func, key=None, cmp=None)

    typer.echo(f"Запуск бенчмарка на {n} элементах...")
    typer.echo(
        f"\n{'Алгоритм':<20} | {'Тип массива':<30} | {'Время (сек)':<15}"
    )
    typer.echo("-" * 70)

    try:
        int_results = bench.benchmark_sorts(int_arrays, int_algos)
        for algo, dataset_res in int_results.items():
            for data_name, time_sec in dataset_res.items():
                typer.echo(f"{algo:<20} | {data_name:<30} | {time_sec:.6f}")

        bucket_results = bench.benchmark_sorts(
            float_arrays, {"Bucket-sort": BucketSort.execute}
        )
        for algo, dataset_res in bucket_results.items():
            for data_name, time_sec in dataset_res.items():
                typer.echo(f"{algo:<20} | {data_name:<30} | {time_sec:.6f}")

        Logger.success_execution(f"Benchmark (n={n})")
    except Exception as e:
        Logger.failure_execution(e)
        typer.echo(f"Ошибка при выполнении бенчмарка: {e}", err=True)

    typer.echo("-" * 70)
