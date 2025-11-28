from typing import Callable

import typer

from src.interface.config import queue_map, stack_map
from src.utils.logger import Logger

Logger.setup_logging()


def run_stack() -> None:
    """
    Запускает интерактивную сессию для работы со стеком
    """
    stack_type = typer.prompt(
        "Реализация [linked-list/list/queue]",
        default="list",
        show_default=False,
    )

    stack_cls = stack_map.get(stack_type)

    if not stack_cls:
        typer.echo(f"Ошибка: Реализация {stack_type} не найдена", err=True)
        Logger.failure_execution(ValueError(f"Неизвестный тип: {stack_type}"))
        return

    s = stack_cls()
    typer.echo(f"Создан стек: {stack_type}")
    typer.echo("Операции [push/pop/peek/min/len/empty/exit]")

    Logger.start_execution(f"Stack-{stack_type}")

    operations: dict[str, Callable[[], None]] = {
        "pop": lambda: typer.echo(f"Извлечено: {s.pop()}"),
        "peek": lambda: typer.echo(f"Верхний элемент: {s.peek()}"),
        "min": lambda: typer.echo(f"Минимум: {s.min()}"),
        "len": lambda: typer.echo(f"Размер: {len(s)}"),
        "empty": lambda: typer.echo(f"Пуст: {s.is_empty()}"),
    }

    while (operation := typer.prompt("Операция")) != "exit":
        if operation == "exit":
            Logger.success_execution(f"Stack-{stack_type}")
            break

        try:
            if operation == "push":
                value = typer.prompt("Значение", type=int)
                s.push(value)
                typer.echo(f"Добавлено: {value}")
            elif operation in operations:
                operations[operation]()
            else:
                typer.echo("Неизвестная операция")
        except ValueError as e:
            typer.echo(f"Ошибка: {e}")
            Logger.failure_execution(e)


def run_queue() -> None:
    """
    Запускает интерактивную сессию для работы с очередью
    """
    queue_type = typer.prompt(
        "Реализация [linked-list/list/stack]",
        default="list",
        show_default=False,
    )

    queue_cls = queue_map.get(queue_type)

    if not queue_cls:
        typer.echo(f"Ошибка: Реализация {queue_type} не найдена", err=True)
        Logger.failure_execution(ValueError(f"Неизвестный тип: {queue_type}"))
        return

    q = queue_cls()
    typer.echo(f"Создана очередь: {queue_type}")
    typer.echo("Операции [enqueue/dequeue/front/len/empty/exit]")

    Logger.start_execution(f"Queue-{queue_type}")

    operations: dict[str, Callable[[], None]] = {
        "dequeue": lambda: typer.echo(f"Извлечено: {q.dequeue()}"),
        "front": lambda: typer.echo(f"Первый элемент: {q.front()}"),
        "len": lambda: typer.echo(f"Размер: {len(q)}"),
        "empty": lambda: typer.echo(f"Пуста: {q.is_empty()}"),
    }

    while (operation := typer.prompt("Операция")) != "exit":
        if operation == "exit":
            Logger.success_execution(f"Queue-{queue_type}")
            break

        try:
            if operation == "enqueue":
                value = typer.prompt("Значение", type=int)
                q.enqueue(value)
                typer.echo(f"Добавлено: {value}")
            elif operation in operations:
                operations[operation]()
            else:
                typer.echo("Неизвестная операция")
        except ValueError as e:
            typer.echo(f"Ошибка: {e}")
            Logger.failure_execution(e)
