from src.data_structures.stack import StackOnList
from src.utils.base import Node, Queue
from src.utils.errors import QueueIsEmpty


class QueueOnLinkedList(Queue):
    def __init__(self) -> None:
        self.head: Node | None = None
        self.tail: Node | None = None
        self.size: int = 0

    def enqueue(self, x: int) -> None:
        new_node = Node(x, x)
        if self.tail:
            self.tail.next = new_node

        self.tail = new_node
        if not self.head:
            self.head = new_node

        self.size += 1

    def dequeue(self) -> int:
        if self.head is None:
            raise QueueIsEmpty("Очередь пуста")

        result = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None

        self.size -= 1
        return result

    def front(self) -> int:
        if self.head is None:
            raise QueueIsEmpty("Очередь пуста")

        return self.head.value

    def is_empty(self) -> bool:
        return self.head is None

    def __len__(self) -> int:
        return self.size


class QueueOnList(Queue):
    def __init__(self) -> None:
        self.queue: list[int] = []

    def enqueue(self, x: int) -> None:
        self.queue.append(x)

    def dequeue(self) -> int:
        if not self.queue:
            raise QueueIsEmpty("Очередь пуста")

        return self.queue.pop(0)

    def front(self) -> int:
        if not self.queue:
            raise QueueIsEmpty("Очередь пуста")

        return self.queue[0]

    def is_empty(self) -> bool:
        return len(self.queue) == 0

    def __len__(self) -> int:
        return len(self.queue)


class QueueOnStack(Queue):
    def __init__(self) -> None:
        self.stack_in: StackOnList = StackOnList()
        self.stack_out: StackOnList = StackOnList()

    def enqueue(self, x: int) -> None:
        self.stack_in.push(x)

    def dequeue(self) -> int:
        if self.stack_out.is_empty():
            if self.stack_in.is_empty():
                raise QueueIsEmpty("Очередь пуста")

            while not self.stack_in.is_empty():
                self.stack_out.push(self.stack_in.pop())

        return self.stack_out.pop()

    def front(self) -> int:
        if self.stack_out.is_empty():
            if self.stack_in.is_empty():
                raise QueueIsEmpty("Очередь пуста")

            while not self.stack_in.is_empty():
                self.stack_out.push(self.stack_in.pop())

        return self.stack_out.peek()

    def is_empty(self) -> bool:
        return self.stack_in.is_empty() and self.stack_out.is_empty()

    def __len__(self) -> int:
        return len(self.stack_in) + len(self.stack_out)
