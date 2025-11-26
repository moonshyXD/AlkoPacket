from typing import Callable

import typer

from src.interface.config import queue_map, stack_map


def run_stack() -> None:
    """
    Запускает сессию для работы со стеком.
    :return: None.
    """
    stack_type = typer.prompt(
        "Реализация [linked-list/list/queue]",
        default="list",
        show_default=False,
    )
    stack_cls = stack_map.get(stack_type)
    if not stack_cls:
        typer.echo(f"Ошибка: Реализация {stack_type} не найдена", err=True)
        return

    stack = stack_cls()
    typer.echo(f"Создан стек: {stack_type}")
    typer.echo("Операции [push/pop/peek/min/len/empty/exit]")

    operations: dict[str, Callable[[], None]] = {
        "pop": lambda: typer.echo(f"Извлечено: {stack.pop()}"),
        "peek": lambda: typer.echo(f"Верхний элемент: {stack.peek()}"),
        "min": lambda: typer.echo(f"Минимум: {stack.min()}"),
        "len": lambda: typer.echo(f"Размер: {len(stack)}"),
        "empty": lambda: typer.echo(f"Пуст: {stack.is_empty()}"),
    }

    operation = None
    while operation != "exit":
        operation = typer.prompt("Операция")
        try:
            if operation == "push":
                value = typer.prompt("Значение", type=int)
                stack.push(value)
                typer.echo(f"Добавлено: {value}")
            elif operation in operations:
                operations[operation]()
            else:
                typer.echo("Неизвестная операция")
        except ValueError as e:
            typer.echo(f"Ошибка: {e}")


def run_queue() -> None:
    """
    Запускает интерактивную сессию для работы с очередью.
    :return: None.
    """
    queue_type = typer.prompt(
        "Реализация [linked-list/list/stack]",
        default="list",
        show_default=False,
    )
    queue_cls = queue_map.get(queue_type)
    if not queue_cls:
        typer.echo(f"Ошибка: Реализация {queue_type} не найдена", err=True)
        return

    queue = queue_cls()
    typer.echo(f"Создана очередь: {queue_type}")
    typer.echo("Операции [enqueue/dequeue/front/len/empty/exit]")

    operations: dict[str, Callable[[], None]] = {
        "dequeue": lambda: typer.echo(f"Извлечено: {queue.dequeue()}"),
        "front": lambda: typer.echo(f"Первый элемент: {queue.front()}"),
        "len": lambda: typer.echo(f"Размер: {len(queue)}"),
        "empty": lambda: typer.echo(f"Пуста: {queue.is_empty()}"),
    }

    operation = None
    while operation != "exit":
        operation = typer.prompt("Операция")
        try:
            if operation == "enqueue":
                value = typer.prompt("Значение", type=int)
                queue.enqueue(value)
                typer.echo(f"Добавлено: {value}")
            elif operation in operations:
                operations[operation]()
            else:
                typer.echo("Неизвестная операция")
        except ValueError as e:
            typer.echo(f"Ошибка: {e}")
