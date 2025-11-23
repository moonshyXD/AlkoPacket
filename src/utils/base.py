from abc import ABC, abstractmethod
from typing import Any


class BaseQueue(ABC):
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


class BaseStack(ABC):
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
    def __init__(
        self, value: int, min_value: int, next_node: "Node | None" = None
    ) -> None:
        self.value: int = value
        self.cur_min: int = min_value
        self.next: Node | None = next_node


class BaseSort(ABC):
    @staticmethod
    @abstractmethod
    def execute(*args: Any, **kwargs: Any) -> Any:
        pass
