from collections import deque

from src.utils.base import BaseStack, Node


class StackOnLinkedList(BaseStack):
    def __init__(self) -> None:
        """
        Создает пустой стек на основе связного списка
        """
        self.head: Node | None = None
        self.size: int = 0

    def push(self, value: int) -> None:
        """
        Добавляет элемент на вершину стека
        :param value: элемент для добавления
        """
        if self.head is None:
            min_val = value
        else:
            min_val = min(value, self.head.cur_min)

        self.head = Node(value, min_val, self.head)
        self.size += 1

    def pop(self) -> int:
        """
        Удаляет и возвращает верхний элемент стека
        :return: верхний элемент стека
        :raises ValueError: если стек пуст
        """
        if self.head is None:
            raise ValueError("Стэк пуст")

        result = self.head.value
        self.head = self.head.next
        self.size -= 1
        return result

    def is_empty(self) -> bool:
        """
        Проверяет, пуст ли стек
        :return: True если пуст, иначе False
        """
        return self.head is None

    def peek(self) -> int:
        """
        Возвращает верхний элемент без удаления
        :return: верхний элемент стека
        :raises ValueError: если стек пуст
        """
        if self.head is None:
            raise ValueError("Стэк пуст")

        return self.head.value

    def __len__(self) -> int:
        """
        Возвращает количество элементов в стеке
        :return: размер стека
        """
        return self.size

    def min(self) -> int:
        """
        Возвращает минимальный элемент в стеке
        :return: минимальный элемент
        :raises ValueError: если стек пуст
        """
        if self.head is None:
            raise ValueError("Стэк пуст")

        return self.head.cur_min


class StackOnList(BaseStack):
    def __init__(self) -> None:
        """
        Создает пустой стек на основе списка
        """
        self.stack: list[int] = []
        self.min_values: list[int] = []

    def push(self, value: int) -> None:
        """
        Добавляет элемент на вершину стека
        :param value: элемент для добавления
        """
        if not self.min_values or value <= self.min_values[-1]:
            self.min_values.append(value)

        self.stack.append(value)

    def pop(self) -> int:
        """
        Удаляет и возвращает верхний элемент стека
        :return: верхний элемент стека
        :raises ValueError: если стек пуст
        """
        if not self.stack:
            raise ValueError("Стэк пуст")

        if self.stack[-1] == self.min_values[-1]:
            self.min_values.pop()

        return self.stack.pop()

    def is_empty(self) -> bool:
        """
        Проверяет, пуст ли стек
        :return: True если пуст, иначе False
        """
        return len(self.stack) == 0

    def peek(self) -> int:
        """
        Возвращает верхний элемент без удаления
        :return: верхний элемент стека
        :raises ValueError: если стек пуст
        """
        if not self.stack:
            raise ValueError("Стэк пуст")

        return self.stack[-1]

    def __len__(self) -> int:
        """
        Возвращает количество элементов в стеке
        :return: размер стека
        """
        return len(self.stack)

    def min(self) -> int:
        """
        Возвращает минимальный элемент в стеке
        :return: минимальный элемент
        :raises ValueError: если стек пуст
        """
        if not self.min_values:
            raise ValueError("Стэк пуст")

        return self.min_values[-1]


class StackOnQueue(BaseStack):
    def __init__(self) -> None:
        """
        Создает стек на основе двух очередей
        """
        self.queue1: deque[int] = deque()
        self.queue2: deque[int] = deque()
        self.min_values: deque[int] = deque()

    def push(self, value: int) -> None:
        """
        Добавляет элемент на вершину стека
        :param value: элемент для добавления
        """
        self.queue1.append(value)
        if not self.min_values or value <= self.min_values[-1]:
            self.min_values.append(value)

    def pop(self) -> int:
        """
        Удаляет и возвращает верхний элемент стека
        :return: верхний элемент стека
        :raises ValueError: если стек пуст
        """
        if not self.queue1:
            raise ValueError("Стэк пуст")

        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())

        result = self.queue1.popleft()
        self.queue1, self.queue2 = self.queue2, self.queue1
        if self.min_values and result == self.min_values[-1]:
            self.min_values.pop()

        return result

    def is_empty(self) -> bool:
        """
        Проверяет, пуст ли стек
        :return: True если пуст, иначе False
        """
        return len(self.queue1) == 0

    def peek(self) -> int:
        """
        Возвращает верхний элемент без удаления
        :return: верхний элемент стека
        :raises ValueError: если стек пуст
        """
        if not self.queue1:
            raise ValueError("Стэк пуст")

        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())

        result = self.queue1.popleft()
        self.queue2.append(result)
        self.queue1, self.queue2 = self.queue2, self.queue1
        return result

    def __len__(self) -> int:
        """
        Возвращает количество элементов в стеке
        :return: размер стека
        """
        return len(self.queue1)

    def min(self) -> int:
        """
        Возвращает минимальный элемент в стеке
        :return: минимальный элемент
        :raises ValueError: если стек пуст
        """
        if not self.min_values:
            raise ValueError("Стэк пуст")

        return self.min_values[-1]
