from src.data_structures.stack import StackOnList
from src.utils.base import BaseQueue, Node
from src.utils.errors import QueueIsEmpty


class QueueOnLinkedList(BaseQueue):
    def __init__(self) -> None:
        """
        Инициализирует очередь на основе связного списка.
        :return: None.
        """
        self.head: Node | None = None
        self.tail: Node | None = None
        self.size: int = 0

    def enqueue(self, x: int) -> None:
        """
        Добавляет элемент в конец очереди.
        :param x: Элемент для добавления.
        :return: None.
        """
        new_node = Node(x, x)
        if self.tail:
            self.tail.next = new_node
        self.tail = new_node
        if not self.head:
            self.head = new_node
        self.size += 1

    def dequeue(self) -> int:
        """
        Извлекает и удаляет первый элемент из очереди.
        :return: Первый элемент очереди.
        """
        if self.head is None:
            raise QueueIsEmpty("Очередь пуста")
        result = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.size -= 1
        return result

    def front(self) -> int:
        """
        Возвращает первый элемент очереди без удаления.
        :return: Первый элемент очереди.
        """
        if self.head is None:
            raise QueueIsEmpty("Очередь пуста")
        return self.head.value

    def is_empty(self) -> bool:
        """
        Проверяет, пуста ли очередь.
        :return: True, если очередь пуста, иначе False.
        """
        return self.head is None

    def __len__(self) -> int:
        """
        Возвращает размер очереди.
        :return: Количество элементов в очереди.
        """
        return self.size


class QueueOnList(BaseQueue):
    def __init__(self) -> None:
        """
        Инициализирует очередь на основе списка.
        :return: None.
        """
        self.queue: list[int] = []

    def enqueue(self, x: int) -> None:
        """
        Добавляет элемент в конец очереди.
        :param x: Элемент для добавления.
        :return: None.
        """
        self.queue.append(x)

    def dequeue(self) -> int:
        """
        Извлекает и удаляет первый элемент из очереди.
        :return: Первый элемент очереди.
        """
        if not self.queue:
            raise QueueIsEmpty("Очередь пуста")
        return self.queue.pop(0)

    def front(self) -> int:
        """
        Возвращает первый элемент очереди без удаления.
        :return: Первый элемент очереди.
        """
        if not self.queue:
            raise QueueIsEmpty("Очередь пуста")
        return self.queue[0]

    def is_empty(self) -> bool:
        """
        Проверяет, пуста ли очередь.
        :return: True, если очередь пуста, иначе False.
        """
        return len(self.queue) == 0

    def __len__(self) -> int:
        """
        Возвращает размер очереди.
        :return: Количество элементов в очереди.
        """
        return len(self.queue)


class QueueOnStack(BaseQueue):
    def __init__(self) -> None:
        """
        Инициализирует очередь на основе двух стеков.
        :return: None.
        """
        self.stack_in: StackOnList = StackOnList()
        self.stack_out: StackOnList = StackOnList()

    def enqueue(self, x: int) -> None:
        """
        Добавляет элемент в конец очереди.
        :param x: Элемент для добавления.
        :return: None.
        """
        self.stack_in.push(x)

    def dequeue(self) -> int:
        """
        Извлекает и удаляет первый элемент из очереди.
        :return: Первый элемент очереди.
        """
        if self.stack_out.is_empty():
            if self.stack_in.is_empty():
                raise QueueIsEmpty("Очередь пуста")
            while not self.stack_in.is_empty():
                self.stack_out.push(self.stack_in.pop())
        return self.stack_out.pop()

    def front(self) -> int:
        """
        Возвращает первый элемент очереди без удаления.
        :return: Первый элемент очереди.
        """
        if self.stack_out.is_empty():
            if self.stack_in.is_empty():
                raise QueueIsEmpty("Очередь пуста")
            while not self.stack_in.is_empty():
                self.stack_out.push(self.stack_in.pop())
        return self.stack_out.peek()

    def is_empty(self) -> bool:
        """
        Проверяет, пуста ли очередь.
        :return: True, если очередь пуста, иначе False.
        """
        return self.stack_in.is_empty() and self.stack_out.is_empty()

    def __len__(self) -> int:
        """
        Возвращает размер очереди.
        :return: Количество элементов в очереди.
        """
        return len(self.stack_in) + len(self.stack_out)
