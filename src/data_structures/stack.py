from collections import deque

from src.utils.base import Node, Stack
from src.utils.errors import StackIsEmpty


class StackOnLinkedList(Stack):
    def __init__(self) -> None:
        self.head: Node | None = None
        self.size: int = 0

    def push(self, value: int) -> None:
        if self.head is None:
            min_value = value
        else:
            min_value = min(value, self.head.cur_min)

        self.head = Node(value, min_value, self.head)
        self.size += 1

    def pop(self) -> int:
        if self.head is None:
            raise StackIsEmpty("Стэк пуст")

        result = self.head.value
        self.head = self.head.next
        self.size -= 1

        return result

    def is_empty(self) -> bool:
        return self.head is None

    def peek(self) -> int:
        if self.head is None:
            raise StackIsEmpty("Стэк пуст")

        return self.head.value

    def __len__(self) -> int:
        return self.size

    def min(self) -> int:
        if self.head is None:
            raise StackIsEmpty("Стэк пуст")

        return self.head.cur_min


class StackOnList(Stack):
    def __init__(self) -> None:
        self.stack: list[int] = []
        self.min_values: list[int] = []

    def push(self, value: int) -> None:
        if not self.min_values or value <= self.min_values[-1]:
            self.min_values.append(value)

        self.stack.append(value)

    def pop(self) -> int:
        if not self.stack:
            raise StackIsEmpty("Стэк пуст")

        if self.stack[-1] == self.min_values[-1]:
            self.min_values.pop()

        return self.stack.pop()

    def is_empty(self) -> bool:
        return len(self.stack) == 0

    def peek(self) -> int:
        if not self.stack:
            raise StackIsEmpty("Стэк пуст")

        return self.stack[-1]

    def __len__(self) -> int:
        return len(self.stack)

    def min(self) -> int:
        if not self.min_values:
            raise StackIsEmpty("Стэк пуст")

        return self.min_values[-1]


class StackOnQueue(Stack):
    def __init__(self) -> None:
        self.queue1: deque[int] = deque()
        self.queue2: deque[int] = deque()
        self.min_values: deque[int] = deque()

    def push(self, value: int) -> None:
        self.queue1.append(value)

        if not self.min_values or value <= self.min_values[-1]:
            self.min_values.append(value)

    def pop(self) -> int:
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
        return len(self.queue1) == 0

    def peek(self) -> int:
        if not self.queue1:
            raise StackIsEmpty("Стэк пуст")

        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())

        result = self.queue1.popleft()
        self.queue2.append(result)
        self.queue1, self.queue2 = self.queue2, self.queue1

        return result

    def __len__(self) -> int:
        return len(self.queue1)

    def min(self) -> int:
        if not self.min_values:
            raise StackIsEmpty("Стэк пуст")

        return self.min_values[-1]
