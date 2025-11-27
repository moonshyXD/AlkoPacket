import typer

from src.interface.config import factorial_map, fibonacci_map
from src.utils.logger import Logger

Logger.setup_logging()


def run_factorial() -> None:
    """
    Вычисляет факториал числа.
    :return: None.
    """
    n = typer.prompt("Введите n", type=int)
    method = typer.prompt(
        "Метод [iterative/recursive]", default="iterative", show_default=False
    )
    factorial_type = factorial_map.get(method)
    if not factorial_type:
        typer.echo(f"Ошибка: Метод {method} не найден", err=True)
        Logger.failure_execution(ValueError(f"Unknown method: {method}"))
        return

    try:
        Logger.start_execution(f"Factorial-{method}({n})")
        result = factorial_type(n)
        typer.echo(f"Результат: {result}")
        Logger.success_execution(f"Factorial-{method}({n}) = {result}")
    except Exception as e:
        Logger.failure_execution(e)
        typer.echo(f"Ошибка: {e}", err=True)


def run_fibonacci() -> None:
    """
    Вычисляет число Фибоначчи.
    :return: None.
    """
    n = typer.prompt("Введите n", type=int)
    method = typer.prompt(
        "Метод [iterative/recursive]", default="iterative", show_default=False
    )
    fibonacci_type = fibonacci_map.get(method)
    if not fibonacci_type:
        typer.echo(f"Ошибка: Метод {method} не найден", err=True)
        Logger.failure_execution(ValueError(f"Unknown method: {method}"))
        return

    try:
        Logger.start_execution(f"Fibonacci-{method}({n})")
        result = fibonacci_type(n)
        typer.echo(f"Результат: {result}")
        Logger.success_execution(f"Fibonacci-{method}({n}) = {result}")
    except Exception as e:
        Logger.failure_execution(e)
        typer.echo(f"Ошибка: {e}", err=True)
