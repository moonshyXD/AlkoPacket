from collections import deque

from src.utils.base import BaseStack, Node
from src.utils.errors import StackIsEmpty


class StackOnLinkedList(BaseStack):
    def __init__(self) -> None:
        """
        Инициализирует стек на основе связного списка.
        :return: None.
        """
        self.head: Node | None = None
        self.size: int = 0

    def push(self, value: int) -> None:
        """
        Добавляет элемент на вершину стека.
        :param value: Элемент для добавления.
        :return: None.
        """
        if self.head is None:
            min_value = value
        else:
            min_value = min(value, self.head.cur_min)
        self.head = Node(value, min_value, self.head)
        self.size += 1

    def pop(self) -> int:
        """
        Извлекает и удаляет элемент с вершины стека.
        :return: Верхний элемент стека.
        """
        if self.head is None:
            raise StackIsEmpty("Стэк пуст")
        result = self.head.value
        self.head = self.head.next
        self.size -= 1
        return result

    def is_empty(self) -> bool:
        """
        Проверяет, пуст ли стек.
        :return: True, если стек пуст, иначе False.
        """
        return self.head is None

    def peek(self) -> int:
        """
        Возвращает верхний элемент стека без удаления.
        :return: Верхний элемент стека.
        """
        if self.head is None:
            raise StackIsEmpty("Стэк пуст")
        return self.head.value

    def __len__(self) -> int:
        """
        Возвращает размер стека.
        :return: Количество элементов в стеке.
        """
        return self.size

    def min(self) -> int:
        """
        Возвращает минимальный элемент в стеке.
        :return: Минимальный элемент в стеке.
        """
        if self.head is None:
            raise StackIsEmpty("Стэк пуст")
        return self.head.cur_min


class StackOnList(BaseStack):
    def __init__(self) -> None:
        """
        Инициализирует стек на основе списка.
        :return: None.
        """
        self.stack: list[int] = []
        self.min_values: list[int] = []

    def push(self, value: int) -> None:
        """
        Добавляет элемент на вершину стека.
        :param value: Элемент для добавления.
        :return: None.
        """
        if not self.min_values or value <= self.min_values[-1]:
            self.min_values.append(value)
        self.stack.append(value)

    def pop(self) -> int:
        """
        Извлекает и удаляет элемент с вершины стека.
        :return: Верхний элемент стека.
        """
        if not self.stack:
            raise StackIsEmpty("Стэк пуст")
        if self.stack[-1] == self.min_values[-1]:
            self.min_values.pop()
        return self.stack.pop()

    def is_empty(self) -> bool:
        """
        Проверяет, пуст ли стек.
        :return: True, если стек пуст, иначе False.
        """
        return len(self.stack) == 0

    def peek(self) -> int:
        """
        Возвращает верхний элемент стека без удаления.
        :return: Верхний элемент стека.
        """
        if not self.stack:
            raise StackIsEmpty("Стэк пуст")
        return self.stack[-1]

    def __len__(self) -> int:
        """
        Возвращает размер стека.
        :return: Количество элементов в стеке.
        """
        return len(self.stack)

    def min(self) -> int:
        """
        Возвращает минимальный элемент в стеке.
        :return: Минимальный элемент в стеке.
        """
        if not self.min_values:
            raise StackIsEmpty("Стэк пуст")
        return self.min_values[-1]


class StackOnQueue(BaseStack):
    def __init__(self) -> None:
        """
        Инициализирует стек на основе двух очередей.
        :return: None.
        """
        self.queue1: deque[int] = deque()
        self.queue2: deque[int] = deque()
        self.min_values: deque[int] = deque()

    def push(self, value: int) -> None:
        """
        Добавляет элемент на вершину стека.
        :param value: Элемент для добавления.
        :return: None.
        """
        self.queue1.append(value)
        if not self.min_values or value <= self.min_values[-1]:
            self.min_values.append(value)

    def pop(self) -> int:
        """
        Извлекает и удаляет элемент с вершины стека.
        :return: Верхний элемент стека.
        """
        if not self.queue1:
            raise StackIsEmpty("Стэк пуст")
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())
        result = self.queue1.popleft()
        self.queue1, self.queue2 = self.queue2, self.queue1
        if self.min_values and result == self.min_values[-1]:
            self.min_values.pop()
        return result

    def is_empty(self) -> bool:
        """
        Проверяет, пуст ли стек.
        :return: True, если стек пуст, иначе False.
        """
        return len(self.queue1) == 0

    def peek(self) -> int:
        """
        Возвращает верхний элемент стека без удаления.
        :return: Верхний элемент стека.
        """
        if not self.queue1:
            raise StackIsEmpty("Стэк пуст")
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())
        result = self.queue1.popleft()
        self.queue2.append(result)
        self.queue1, self.queue2 = self.queue2, self.queue1
        return result

    def __len__(self) -> int:
        """
        Возвращает размер стека.
        :return: Количество элементов в стеке.
        """
        return len(self.queue1)

    def min(self) -> int:
        """
        Возвращает минимальный элемент в стеке.
        :return: Минимальный элемент в стеке.
        """
        if not self.min_values:
            raise StackIsEmpty("Стэк пуст")
        return self.min_values[-1]
