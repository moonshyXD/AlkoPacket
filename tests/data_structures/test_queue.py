from typing import Any

import pytest

from src.data_structures.queue import (
    QueueOnLinkedList,
    QueueOnList,
    QueueOnStack,
)


@pytest.mark.parametrize(
    "queue_class", [QueueOnList, QueueOnLinkedList, QueueOnStack]
)
class TestQueue:
    def test_enqueue_dequeue(self, queue_class: Any) -> None:
        q = queue_class()
        q.enqueue(1)
        q.enqueue(2)
        assert q.dequeue() == 1
        assert q.dequeue() == 2

    def test_is_empty(self, queue_class: Any) -> None:
        q = queue_class()
        assert q.is_empty()
        q.enqueue(1)
        assert not q.is_empty()

    def test_len(self, queue_class: Any) -> None:
        q = queue_class()
        assert len(q) == 0
        q.enqueue(1)
        assert len(q) == 1

    def test_dequeue_empty_raises(self, queue_class: Any) -> None:
        with pytest.raises(ValueError):
            queue_class().dequeue()
