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
        """
        Тест добавления и извлечения элементов
        :param queue_class: класс очереди для тестирования
        """
        q = queue_class()
        q.enqueue(1)
        q.enqueue(2)
        assert q.dequeue() == 1
        assert q.dequeue() == 2

    def test_front(self, queue_class: Any) -> None:
        """
        Тест просмотра первого элемента
        :param queue_class: класс очереди для тестирования
        """
        q = queue_class()
        q.enqueue(1)
        q.enqueue(2)
        assert q.front() == 1
        assert q.front() == 1

    def test_is_empty(self, queue_class: Any) -> None:
        """
        Тест проверки на пустоту
        :param queue_class: класс очереди для тестирования
        """
        q = queue_class()
        assert q.is_empty()
        q.enqueue(1)
        assert not q.is_empty()

    def test_len(self, queue_class: Any) -> None:
        """
        Тест получения размера очереди
        :param queue_class: класс очереди для тестирования
        """
        q = queue_class()
        assert len(q) == 0
        q.enqueue(1)
        assert len(q) == 1

    def test_dequeue_empty(self, queue_class: Any) -> None:
        """
        Тест извлечения из пустой очереди
        :param queue_class: класс очереди для тестирования
        :raises ValueError: если очередь пуста
        """
        with pytest.raises(ValueError):
            queue_class().dequeue()

    def test_front_empty(self, queue_class: Any) -> None:
        """
        Тест просмотра пустой очереди
        :param queue_class: класс очереди для тестирования
        :raises ValueError: если очередь пуста
        """
        with pytest.raises(ValueError):
            queue_class().front()
