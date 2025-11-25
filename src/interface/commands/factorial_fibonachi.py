import typer

from src.interface.config import factorial_map, fibonacci_map


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
        return

    result = factorial_type(n)
    typer.echo(f"Результат: {result}")


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
        return

    result = fibonacci_type(n)
    typer.echo(f"Результат: {result}")
