from typing import Any, Callable

import typer

from src.interface.config import cmp_map, key_map, sort_command_map
from src.utils.test_cases import TestCases


def _get_array() -> list[Any] | None:
    """
    Получает массив от пользователя.
    :return: Массив данных или None при ошибке ввода.
    """
    typer.echo("Как получить массив для сортировки (введите цифру)?")
    typer.echo("1. Ввести вручную")
    typer.echo("2. Сгенерировать из тест-кейса")
    input_choice = typer.prompt("Ваш выбор", type=int)

    if input_choice == 1:
        array_str = typer.prompt("Введите массив (через пробел)")
        try:
            return [int(x) for x in array_str.split()]
        except ValueError:
            typer.echo("Ошибка: Элементы должны быть числами", err=True)
            return None

    elif input_choice == 2:
        typer.echo("Выберите тип генерации массива (введите цифру):")
        typer.echo("1. Случайный массив целых чисел")
        typer.echo("2. Случайный массив вещественных чисел")
        typer.echo("3. Почти отсортированный")
        typer.echo("4. Отсортированный в обратном порядке")
        typer.echo("5. Много дубликатов")
        gen_choice = typer.prompt("Номер", type=int)
        n = typer.prompt("Размер массива (n)", type=int)

        use_seed_input = typer.prompt(
            "Использовать seed для воспроизводимости? [y/n]",
            default="n",
            show_default=False,
        )
        seed = None
        if use_seed_input.lower() in ["y", "yes"]:
            seed = typer.prompt(
                "Введите seed", type=int, default=42, show_default=False
            )

        if gen_choice == 1:
            lo = typer.prompt(
                "Минимальное значение (lo)",
                type=int,
                default=0,
                show_default=False,
            )
            hi = typer.prompt(
                "Максимальное значение (hi)",
                type=int,
                default=100,
                show_default=False,
            )

            distinct_input = typer.prompt(
                "Генерировать только уникальные элементы? [y/n]",
                default="n",
                show_default=False,
            )
            distinct = distinct_input.lower() in ["y", "yes"]

            try:
                return TestCases.rand_int_array(
                    n, lo, hi, distinct=distinct, seed=seed
                )
            except Exception as e:
                typer.echo(f"Ошибка генерации: {e}", err=True)
                return None

        elif gen_choice == 2:
            lo = typer.prompt(
                "Минимальное значение (lo)",
                type=float,
                default=0.0,
                show_default=False,
            )
            hi = typer.prompt(
                "Максимальное значение (hi)",
                type=float,
                default=1.0,
                show_default=False,
            )
            return TestCases.rand_float_array(n, lo, hi, seed=seed)

        elif gen_choice == 3:
            swaps = typer.prompt(
                "Количество перестановок",
                type=int,
                default=n // 10,
                show_default=False,
            )
            return TestCases.nearly_sorted(n, swaps, seed=seed)

        elif gen_choice == 4:
            return TestCases.reverse_sorted(n)

        elif gen_choice == 5:
            k_unique = typer.prompt(
                "Количество уникальных значений",
                type=int,
                default=5,
                show_default=False,
            )
            return TestCases.many_duplicates(n, k_unique, seed=seed)

    typer.echo("Неверный выбор", err=True)
    return None


def run_sorts() -> None:
    """
    Запускает выбор и выполнение сортировки.
    :return: None.
    """
    sort_type = typer.prompt(
        "Введите название сортировки "
        "[Bubble-sort/Bucket-sort/Counting-sort/"
        "Heap-sort/Quick-sort/Radix-sort]"
    )
    sort_command = sort_command_map.get(sort_type)
    if not sort_command:
        typer.echo(f"Ошибка: Сортировка {sort_type} не найдена", err=True)
        return

    supports_key_cmp = sort_type not in ["Radix-sort", "Counting-sort"]
    key: Callable[[Any], Any] | None = None
    cmp: Callable[[Any, Any], int] | None = None

    if supports_key_cmp:
        typer.echo("\nВведите ключ [default, abs, len]")
        typer.echo("default - без ключа (по умолчанию)")
        typer.echo("abs     - по абсолютному значению (для чисел)")
        typer.echo("len     - по длине (только для строк/списков)")
        key_type = typer.prompt(
            "Введите название ключа",
            default="default",
            show_default=False,
        )

        typer.echo("\nВведите компаратор [default, reverse]")
        typer.echo("default - по возрастанию (по умолчанию)")
        typer.echo("reverse - по убыванию")
        cmp_type = typer.prompt(
            "Введите название компаратора",
            default="default",
            show_default=False,
        )

        key = key_map.get(key_type or "default")
        cmp = cmp_map.get(cmp_type or "default")

        if key is None and key_type not in ["", "default"]:
            typer.echo(
                f"Ключ '{key_type}' не найден, используется default",
                err=True,
            )

        if cmp is None and cmp_type not in ["", "default"]:
            typer.echo(
                f"Компаратор '{cmp_type}' не найден, используется default",
                err=True,
            )

    arr = _get_array()
    if arr is None:
        return

    if sort_type == "Bucket-sort":
        try:
            arr = [float(x) for x in arr]
        except (ValueError, TypeError):
            typer.echo("Bucket-sort требует числовые данные.", err=True)
            return

    try:
        if supports_key_cmp:
            result = sort_command(arr, key=key, cmp=cmp)
        else:
            result = sort_command(arr)

        typer.echo(
            f"Результат сортировки (первые 20 элементов): {result[:20]}"
        )
    except TypeError as e:
        typer.echo(f"Ошибка сортировки: {e}", err=True)
