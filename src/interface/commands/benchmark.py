from typing import Any, Callable

import typer

from src.interface.config import sort_command_map
from src.sorts.bucket_sort import BucketSort
from src.wrappers.benchmarks import Benchmarks
from src.wrappers.test_cases import TestCases


def _make_sort_wrapper(
    func: Callable[..., list[Any]],
) -> Callable[[list[Any]], list[Any]]:
    """
    Создает обертку для функции сортировки с параметрами key и cmp.
    :param func: Функция сортировки.
    :return: Обернутая функция сортировки.
    """

    def wrapper(arr: list[Any]) -> list[Any]:
        return func(arr, None, None)

    return wrapper


def run_benchmark() -> None:
    """
    Запускает бенчмарк сортировок.
    :return: None.
    """
    n = typer.prompt(
        "Размер массивов", type=int, default=1000, show_default=False
    )

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
            int_algos[name] = _make_sort_wrapper(func)

    typer.echo(f"Запуск бенчмарка на {n} элементах...")
    typer.echo(
        f"\n{'Алгоритм':<20} | {'Тип массива':<30} | {'Время (сек)':<15}"
    )
    typer.echo("-" * 70)

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

    typer.echo("-" * 70)
