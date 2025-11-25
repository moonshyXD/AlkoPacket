from typing import Callable

import typer

from src.interface import (
    run_benchmark,
    run_factorial,
    run_fibonacci,
    run_queue,
    run_sorts,
    run_stack,
)

app = typer.Typer(help="Интерактивный менеджер для работы с алгоритмами.")


def show_help() -> None:
    """
    Показывает справку по командам.
    :return: None.
    """
    typer.echo("\nСправка по командам:")
    typer.echo("  sorts     - Интерактивный выбор и запуск сортировок")
    typer.echo("  benchmark - Замер скорости работы сортировок")
    typer.echo("  factorial - Вычисление факториала")
    typer.echo("  fibonacci - Вычисление чисел Фибоначчи")
    typer.echo("  stack     - Работа со стеком")
    typer.echo("  queue     - Работа с очередью")
    typer.echo("  exit      - Выход из программы")


@app.command()
def hello() -> None:
    """
    Запускает интерактивный менеджер для работы с алгоритмами.
    :return: None.
    """
    typer.echo(
        "Приветствуем вас в интерактивном менеджере "
        "сортировок и структур данных"
    )

    command_map: dict[str, Callable[[], None]] = {
        "sorts": run_sorts,
        "benchmark": run_benchmark,
        "factorial": run_factorial,
        "fibonacci": run_fibonacci,
        "stack": run_stack,
        "queue": run_queue,
        "help": show_help,
        "--help": show_help,
    }

    while True:
        typer.echo("\nЧто вы хотите использовать (введите только название):")
        typer.echo("1. sorts")
        typer.echo("2. benchmark")
        typer.echo("3. factorial")
        typer.echo("4. fibonacci")
        typer.echo("5. stack")
        typer.echo("6. queue")
        typer.echo("7. exit (для выхода)")
        typer.echo("Введите 'help' для справки\n")

        command = typer.prompt("Команда")

        if command == "exit":
            typer.echo("До свидания!")
            break

        handler = command_map.get(command)
        if handler:
            handler()
        else:
            typer.echo("Неизвестная команда")
