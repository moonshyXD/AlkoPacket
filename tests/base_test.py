from typing import Any

import pytest


class BaseSortTest:
    """Базовый класс для тестирования сортировок."""

    sort_class: Any = None

    def test_empty(self, empty_array: list[Any]) -> None:
        assert self.sort_class.execute(empty_array) == []

    def test_single(self, single_element_array: list[int]) -> None:
        assert self.sort_class.execute(single_element_array) == [42]

    def test_sorted(self, sorted_array: list[int]) -> None:
        result = self.sort_class.execute(sorted_array.copy())
        assert result == [1, 2, 3, 4, 5]

    def test_reverse(self, reverse_sorted_array: list[int]) -> None:
        result = self.sort_class.execute(reverse_sorted_array.copy())
        assert result == [
            0,
            1,
            2,
            3,
            4,
        ]

    def test_random(self, sample_array: list[int]) -> None:
        result = self.sort_class.execute(sample_array.copy())
        assert result == sorted(sample_array)

    def test_duplicates(self, duplicates_array: list[int]) -> None:
        result = self.sort_class.execute(duplicates_array.copy())
        assert result == sorted(duplicates_array)


class BaseSortWithKeyTest(BaseSortTest):
    """Базовый класс для тестирования сортировок с key и cmp."""

    def test_negative(self, negative_numbers: list[int]) -> None:
        result = self.sort_class.execute(negative_numbers.copy())
        assert result == sorted(negative_numbers)

    def test_mixed(self, mixed_numbers: list[int]) -> None:
        result = self.sort_class.execute(mixed_numbers.copy())
        assert result == sorted(mixed_numbers)

    def test_with_key(self) -> None:
        arr = [-3, -1, 2, -4]
        result = self.sort_class.execute(arr, key=abs)
        assert result == [-1, 2, -3, -4]

    def test_with_cmp(self) -> None:
        def cmp(a: int, b: int) -> int:
            return (b > a) - (b < a)

        result = self.sort_class.execute([1, 3, 2], cmp=cmp)
        assert result == [3, 2, 1]


class BaseErrorTest:
    """Базовый класс для тестирования пользовательских исключений."""

    error_class: Any = None
    error_message: str = "Test error"

    def test_raise_error(self) -> None:
        """Проверка, что исключение выбрасывается."""
        with pytest.raises(self.error_class):
            raise self.error_class(self.error_message)

    def test_error_message(self) -> None:
        """Проверка сообщения об ошибке."""
        try:
            raise self.error_class(self.error_message)
        except self.error_class as e:
            assert str(e) == self.error_message

    def test_error_inheritance(self) -> None:
        """Проверка наследования от Exception."""
        assert issubclass(self.error_class, Exception)

    def test_catch_as_exception(self) -> None:
        """Проверка, что ошибка ловится как Exception."""
        try:
            raise self.error_class(self.error_message)
        except Exception as e:
            assert isinstance(e, self.error_class)
