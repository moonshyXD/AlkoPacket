from abc import ABC, abstractmethod


class Queue(ABC):
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


class Sort(ABC):
    @staticmethod
    @abstractmethod
    def execute(cls, *argc, **kwargs):
        pass
