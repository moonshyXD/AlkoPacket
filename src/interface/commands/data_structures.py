from typing import Callable

import typer

from src.interface.config import queue_map, stack_map


def run_stack() -> None:
    """
    Запускает интерактивную сессию для работы со стеком.
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

    s = stack_cls()
    typer.echo(f"Создан стек: {stack_type}")
    typer.echo("Операции [push/pop/peek/min/len/empty/exit]")

    def handle_push() -> None:
        """
        Обрабатывает операцию добавления элемента в стек.
        :return: None.
        """
        value = typer.prompt("Значение", type=int)
        s.push(value)
        typer.echo(f"Добавлено: {value}")

    def handle_pop() -> None:
        """
        Обрабатывает операцию извлечения элемента из стека.
        :return: None.
        """
        try:
            value = s.pop()
            typer.echo(f"Извлечено: {value}")
        except ValueError:
            typer.echo("Стек пуст")

    def handle_peek() -> None:
        """
        Обрабатывает операцию просмотра верхнего элемента стека.
        :return: None.
        """
        try:
            value = s.peek()
            typer.echo(f"Верхний элемент: {value}")
        except ValueError:
            typer.echo("Стек пуст")

    def handle_min() -> None:
        """
        Обрабатывает операцию получения минимального элемента стека.
        :return: None.
        """
        try:
            value = s.min()
            typer.echo(f"Минимум: {value}")
        except ValueError:
            typer.echo("Стек пуст")

    def handle_len() -> None:
        """
        Обрабатывает операцию получения размера стека.
        :return: None.
        """
        typer.echo(f"Размер: {len(s)}")

    def handle_empty() -> None:
        """
        Обрабатывает операцию проверки стека на пустоту.
        :return: None.
        """
        typer.echo(f"Пуст: {s.is_empty()}")

    operations_map: dict[str, Callable[[], None]] = {
        "push": handle_push,
        "pop": handle_pop,
        "peek": handle_peek,
        "min": handle_min,
        "len": handle_len,
        "empty": handle_empty,
    }

    while True:
        operation = typer.prompt("Операция")
        if operation == "exit":
            break
        handler = operations_map.get(operation)
        if handler:
            handler()
        else:
            typer.echo("Неизвестная операция")


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

    q = queue_cls()
    typer.echo(f"Создана очередь: {queue_type}")
    typer.echo("Операции [enqueue/dequeue/front/len/empty/exit]")

    def handle_enqueue() -> None:
        """
        Обрабатывает операцию добавления элемента в очередь.
        :return: None.
        """
        value = typer.prompt("Значение", type=int)
        q.enqueue(value)
        typer.echo(f"Добавлено: {value}")

    def handle_dequeue() -> None:
        """
        Обрабатывает операцию извлечения элемента из очереди.
        :return: None.
        """
        try:
            value = q.dequeue()
            typer.echo(f"Извлечено: {value}")
        except ValueError:
            typer.echo("Очередь пуста")

    def handle_front() -> None:
        """
        Обрабатывает операцию просмотра первого элемента очереди.
        :return: None.
        """
        try:
            value = q.front()
            typer.echo(f"Первый элемент: {value}")
        except ValueError:
            typer.echo("Очередь пуста")

    def handle_len() -> None:
        """
        Обрабатывает операцию получения размера очереди.
        :return: None.
        """
        typer.echo(f"Размер: {len(q)}")

    def handle_empty() -> None:
        """
        Обрабатывает операцию проверки очереди на пустоту.
        :return: None.
        """
        typer.echo(f"Пуста: {q.is_empty()}")

    operations_map: dict[str, Callable[[], None]] = {
        "enqueue": handle_enqueue,
        "dequeue": handle_dequeue,
        "front": handle_front,
        "len": handle_len,
        "empty": handle_empty,
    }

    while True:
        operation = typer.prompt("Операция")
        if operation == "exit":
            break
        handler = operations_map.get(operation)
        if handler:
            handler()
        else:
            typer.echo("Неизвестная операция")
