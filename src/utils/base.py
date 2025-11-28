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
        Сравнивает два элемента
        :param a: первый элемент
        :param b: второй элемент
        :param key: функция для ключа сравнения
        :param cmp: компаратор
        :return: -1 если a < b, 0 если равны, 1 если a > b
        """
        if key:
            a_key = key(a)
            b_key = key(b)
            if cmp:
                return cmp(a_key, b_key)
            return -1 if a_key < b_key else (1 if a_key > b_key else 0)

        if cmp:
            return cmp(a, b)

        return -1 if a < b else (1 if a > b else 0)

    @staticmethod
    @abstractmethod
    def execute(
        arr: list[Any],
        key: Callable[[Any], Any] | None = None,
        cmp: Callable[[Any, Any], int] | None = None,
    ) -> list[Any]:
        """
        Выполняет сортировку массива
        :param arr: массив для сортировки
        :param key: ключ сравнения элементов
        :param cmp: компаратор сравнения
        :return: отсортированный массив
        """
        raise NotImplementedError


class BaseStack(ABC):
    @abstractmethod
    def push(self, item: Any) -> None:
        """
        Добавляет элемент в стек
        :param item: элемент для добавления
        """
        raise NotImplementedError

    @abstractmethod
    def pop(self) -> Any:
        """
        Извлекает верхний элемент стека
        :return: верхний элемент
        """
        raise NotImplementedError

    @abstractmethod
    def peek(self) -> Any:
        """
        Смотрит верхний элемент без удаления
        :return: верхний элемент
        """
        raise NotImplementedError

    @abstractmethod
    def min(self) -> Any:
        """
        Находит минимальный элемент в стеке
        :return: минимальный элемент
        """
        raise NotImplementedError

    @abstractmethod
    def is_empty(self) -> bool:
        """
        Проверяет пустоту стека
        :return: True если пуст, False иначе
        """
        raise NotImplementedError

    @abstractmethod
    def __len__(self) -> int:
        """
        Возвращает размер стека
        :return: количество элементов
        """
        raise NotImplementedError


class BaseQueue(ABC):
    @abstractmethod
    def enqueue(self, item: Any) -> None:
        """
        Добавляет элемент в очередь
        :param item: элемент для добавления
        """
        raise NotImplementedError

    @abstractmethod
    def dequeue(self) -> Any:
        """
        Извлекает первый элемент очереди
        :return: первый элемент
        """
        raise NotImplementedError

    @abstractmethod
    def front(self) -> Any:
        """
        Смотрит первый элемент без удаления
        :return: первый элемент
        """
        raise NotImplementedError

    @abstractmethod
    def is_empty(self) -> bool:
        """
        Проверяет пустоту очереди
        :return: True если пуста, False иначе
        """
        raise NotImplementedError

    @abstractmethod
    def __len__(self) -> int:
        """
        Возвращает размер очереди
        :return: количество элементов
        """
        raise NotImplementedError


class Node:
    def __init__(
        self, value: int, cur_min: int, next: "Node | None" = None
    ) -> None:
        """
        Создаёт узел связного списка
        :param value: значение узла
        :param cur_min: текущее минимальное значение
        :param next: следующий узел
        """
        self.value = value
        self.cur_min = cur_min
        self.next = next
