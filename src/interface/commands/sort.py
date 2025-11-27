import time
from typing import Any

import typer

from src.interface.config import cmp_map, key_map, sort_command_map
from src.utils.logger import Logger
from src.utils.test_cases import TestCases

Logger.setup_logging()


def _get_array() -> list[Any] | None:
    """
    Спрашивает массив у пользователя
    """
    typer.echo("Как получить массив?")
    typer.echo("1. Ввести вручную")
    typer.echo("2. Сгенерировать")
    choice = typer.prompt("Выбор", type=int)

    if choice == 1:
        arr_str = typer.prompt("Массив через пробел")
        try:
            return [int(x) for x in arr_str.split()]
        except ValueError:
            typer.echo("Нужны числа", err=True)
            return None
    elif choice == 2:
        typer.echo("Тип генерации:")
        typer.echo("1. Случайные int")
        typer.echo("2. Случайные float")
        typer.echo("3. Почти отсортированный")
        typer.echo("4. Обратный порядок")
        typer.echo("5. Много дублей")
        gen = typer.prompt("Номер", type=int)
        n = typer.prompt("Размер", type=int)

        seed = None
        if typer.confirm("С seed?"):
            seed = typer.prompt("Seed", type=int, default=42)

        if gen == 1:
            lo = typer.prompt("lo", type=int, default=0)
            hi = typer.prompt("hi", type=int, default=100)
            distinct = typer.confirm("Уникальные?")
            try:
                return TestCases.rand_int_array(n, lo, hi, distinct, seed)
            except Exception as e:
                typer.echo(f"Ошибка генерации: {e}", err=True)
                return None
        elif gen == 2:
            lo = typer.prompt("lo", type=float, default=0.0)
            hi = typer.prompt("hi", type=float, default=1.0)
            return TestCases.rand_float_array(n, lo, hi, seed)
        elif gen == 3:
            swaps = typer.prompt("Перестановок", type=int, default=n // 10)
            return TestCases.nearly_sorted(n, swaps, seed)
        elif gen == 4:
            return TestCases.reverse_sorted(n)
        elif gen == 5:
            k = typer.prompt("Уникальных значений", type=int, default=5)
            return TestCases.many_duplicates(n, k, seed)

    typer.echo("Неправильный выбор", err=True)
    return None


def run_sorts() -> None:
    """
    Выбирает и запускает сортировку
    """
    sort_name = typer.prompt(
        "Сортировка [Bubble/Bucket/Counting/Heap/Quick/Radix]"
    )
    sort_func = sort_command_map.get(sort_name)
    if not sort_func:
        typer.echo(f"{sort_name} не найдена", err=True)
        return

    needs_key_cmp = sort_name not in ["Radix-sort", "Counting-sort"]
    key, cmp_func = None, None

    if needs_key_cmp:
        key_name = typer.prompt("Ключ [default/abs/len]", default="default")
        cmp_name = typer.prompt("Cmp [default/reverse]", default="default")
        key = key_map.get(key_name)
        cmp_func = cmp_map.get(cmp_name)

    arr = _get_array()
    if not arr:
        return

    if sort_name == "Bucket-sort":
        try:
            arr = [float(x) for x in arr]
        except ValueError:
            typer.echo("Bucket нужен float", err=True)
            return

    try:
        Logger.start_execution(f"{sort_name} (n={len(arr)})")
        start = time.perf_counter()

        if needs_key_cmp:
            result = sort_func(arr, key=key, cmp=cmp_func)
        else:
            result = sort_func(arr)

        elapsed = time.perf_counter() - start

        Logger.success_execution(f"{sort_name} ({elapsed:.3f}s)")
        typer.echo(f"Результат (первые 20): {result[:20]}")
        typer.echo(f"Время: {elapsed:.6f}с")
    except Exception as e:
        Logger.failure_execution(e)
        typer.echo(f"Ошибка: {e}", err=True)
