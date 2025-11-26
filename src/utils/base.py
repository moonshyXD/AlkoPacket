from abc import ABC, abstractmethod
from typing import Any, Callable


class BaseSort(ABC):
    @staticmethod
    def compare(
        a: Any,
        b: Any,
        key: Callable[[Any], Any] | None = None,
        cmp: Callable[[Any, Any], int] | None = None,
    ) -> int:
        """
        Сравнивает два элемента с использованием ключа/компаратора.
        :param a: Первый элемент для сравнения.
        :param b: Второй элемент для сравнения.
        :param key: Функция для извлечения ключа сравнения.
        :param cmp: Внешняя функция-компаратор.
        :return: -1 если a < b, 0 если a == b, 1 если a > b.
        """
        if cmp:
            return cmp(a, b)

        a_key = key(a) if key else a
        b_key = key(b) if key else b
        if a_key < b_key:
            return -1

        if a_key > b_key:
            return 1

        return 0

    @staticmethod
    @abstractmethod
    def execute(
        arr: list[Any],
        key: Callable[[Any], Any] | None = None,
        cmp: Callable[[Any, Any], int] | None = None,
    ) -> list[Any]:
        """
        Абстрактный метод для выполнения сортировки.
        :param arr: Массив для сортировки.
        :param key: Ключ сравнения эелементов.
        :param cmp: Компаратор сравнения элементов.
        :return: Отсортированный массив.
        """
        raise NotImplementedError


class BaseStack(ABC):
    @abstractmethod
    def push(self, item: Any) -> None:
        """
        Абстрактный метод добавления элемента в стек.
        :param item: Элемент для добавления.
        :return: None.
        """
        raise NotImplementedError

    @abstractmethod
    def pop(self) -> Any:
        """
        Абстрактный метод извлечения элемента из стека.
        :return: Верхний элемент стека.
        """
        raise NotImplementedError

    @abstractmethod
    def peek(self) -> Any:
        """
        Абстрактный метод просмотра верхнего элемента стека.
        :return: Верхний элемент стека.
        """
        raise NotImplementedError

    @abstractmethod
    def min(self) -> Any:
        """
        Абстрактный метод для поиска минимального элемента.
        :return: Минимальный элемент в стеке.
        """
        raise NotImplementedError

    @abstractmethod
    def is_empty(self) -> bool:
        """
        Абстрактный метод для проверки пустоты стека.
        :return: True, если пуст, False, если не пуст.
        """
        raise NotImplementedError

    @abstractmethod
    def __len__(self) -> int:
        """
        Абстрактный метод для получения размера стека.
        :return: Количество элементов в стеке.
        """
        raise NotImplementedError


class BaseQueue(ABC):
    @abstractmethod
    def enqueue(self, item: Any) -> None:
        """
        Абстрактный метод добавления элемента в очередь.
        :param item: Элемент для добавления.
        :return: None.
        """
        raise NotImplementedError

    @abstractmethod
    def dequeue(self) -> Any:
        """
        Абстрактный метод извлечения элемента из очереди.
        :return: Первый элемент очереди.
        """
        raise NotImplementedError

    @abstractmethod
    def front(self) -> Any:
        """
        Абстрактный метод просмотра первого элемента очереди.
        :return: Первый элемент очереди.
        """
        raise NotImplementedError

    @abstractmethod
    def is_empty(self) -> bool:
        """
        Абстрактный метод для проверки пустоты очереди.
        :return: True, если пуста, False, если не пуст.
        """
        raise NotImplementedError

    @abstractmethod
    def __len__(self) -> int:
        """
        Абстрактный метод для получения размера очереди.
        :return: Количество элементов в очереди.
        """
        raise NotImplementedError


class Node:
    def __init__(
        self, value: int, cur_min: int, next: "Node | None" = None
    ) -> None:
        """
        Инициализирует узел связного списка.
        :param value: Значение узла.
        :param cur_min: Текущее минимальное значение.
        :param next: Ссылка на следующий узел.
        :return: None.
        """
        self.value = value
        self.cur_min = cur_min
        self.next = next
