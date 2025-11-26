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
        s = stack_class()
        s.push(1)
        s.push(2)
        assert s.pop() == 2
        assert s.pop() == 1

    def test_is_empty(self, stack_class: Any) -> None:
        s = stack_class()
        assert s.is_empty()
        s.push(1)
        assert not s.is_empty()

    def test_len(self, stack_class: Any) -> None:
        s = stack_class()
        assert len(s) == 0
        s.push(1)
        assert len(s) == 1

    def test_min(self, stack_class: Any) -> None:
        s = stack_class()
        s.push(3)
        s.push(1)
        assert s.min() == 1

    def test_pop_empty_raises(self, stack_class: Any) -> None:
        with pytest.raises(ValueError):
            stack_class().pop()
