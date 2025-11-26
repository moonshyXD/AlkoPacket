from typing import Any

import pytest

from src.data_structures.stack import (
    StackOnLinkedList,
    StackOnList,
    StackOnQueue,
)


@pytest.mark.parametrize(
    "stack_class", [StackOnList, StackOnLinkedList, StackOnQueue]
)
class TestStack:
    def test_push_pop(self, stack_class: Any) -> None:
        """
        Тест добавления и извлечения элементов.
        :param stack_class: Класс стека для тестирования.
        :return: None.
        """
        s = stack_class()
        s.push(1)
        s.push(2)
        assert s.pop() == 2
        assert s.pop() == 1

    def test_peek(self, stack_class: Any) -> None:
        """
        Тест просмотра верхнего элемента.
        :param stack_class: Класс стека для тестирования.
        :return: None.
        """
        s = stack_class()
        s.push(1)
        assert s.peek() == 1
        assert s.peek() == 1

    def test_is_empty(self, stack_class: Any) -> None:
        """
        Тест проверки на пустоту.
        :param stack_class: Класс стека для тестирования.
        :return: None.
        """
        s = stack_class()
        assert s.is_empty()
        s.push(1)
        assert not s.is_empty()

    def test_min(self, stack_class: Any) -> None:
        """
        Тест получения минимального элемента.
        :param stack_class: Класс стека для тестирования.
        :return: None.
        """
        s = stack_class()
        s.push(3)
        s.push(1)
        s.push(2)
        assert s.min() == 1

    def test_len(self, stack_class: Any) -> None:
        """
        Тест получения размера стека.
        :param stack_class: Класс стека для тестирования.
        :return: None.
        """
        s = stack_class()
        assert len(s) == 0
        s.push(1)
        s.push(2)
        assert len(s) == 2
        s.pop()
        assert len(s) == 1

    def test_pop_empty(self, stack_class: Any) -> None:
        """
        Тест извлечения из пустого стека.
        :param stack_class: Класс стека для тестирования.
        :return: None.
        :raises ValueError: Если стек пуст.
        """
        with pytest.raises(ValueError):
            stack_class().pop()

    def test_peek_empty(self, stack_class: Any) -> None:
        """
        Тест просмотра пустого стека.
        :param stack_class: Класс стека для тестирования.
        :return: None.
        :raises ValueError: Если стек пуст.
        """
        with pytest.raises(ValueError):
            stack_class().peek()

    def test_min_empty(self, stack_class: Any) -> None:
        """
        Тест получения минимума из пустого стека.
        :param stack_class: Класс стека для тестирования.
        :return: None.
        :raises ValueError: Если стек пуст.
        """
        with pytest.raises(ValueError):
            stack_class().min()
