from abc import ABC, abstractmethod

from utils.errors import StackIsEmpty


class Stack(ABC):
    @abstractmethod
    def push(self, value: int) -> None:
        pass

    @abstractmethod
    def pop(self) -> int:
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        pass

    @abstractmethod
    def peek(self) -> int:
        pass

    @abstractmethod
    def __len__(self) -> int:
        pass

    @abstractmethod
    def min(self) -> int:
        pass


class Node:
    def __init__(self, value: int, min_value: int, next_node=None):
        self.value = value
        self.cur_min = min_value
        self.next = next_node


class StackOnLinkedList(Stack):
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, value: int) -> None:
        if self.head is None:
            min_value = value
        else:
            min_value = min(value, self.head.cur_min)

        node = Node(value, min_value, self.head)
        self.head = node
        self.size += 1

    def pop(self) -> int:
        if self.head is None:
            raise StackIsEmpty

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
    def __init__(self):
        self.stack = []
        self.min_values = []

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
    def __init__(self):
        from collections import deque

        self.queue1 = deque()
        self.queue2 = deque()
        self.min_values = deque()

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
