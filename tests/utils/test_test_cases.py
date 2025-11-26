import pytest

from src.utils.errors import TestCasesError
from src.wrappers.test_cases import TestCases


class TestTestCases:
    def test_rand_int_array(self) -> None:
        arr = TestCases.rand_int_array(10, 0, 100)
        assert len(arr) == 10
        assert all(0 <= x <= 100 for x in arr)

    def test_rand_int_array_distinct(self) -> None:
        arr = TestCases.rand_int_array(5, 0, 10, distinct=True)
        assert len(arr) == 5
        assert len(set(arr)) == 5

    def test_rand_int_array_distinct_impossible(self) -> None:
        with pytest.raises(TestCasesError):
            TestCases.rand_int_array(20, 0, 10, distinct=True)

    def test_rand_int_array_with_seed(self) -> None:
        arr1 = TestCases.rand_int_array(10, 0, 100, seed=42)
        arr2 = TestCases.rand_int_array(10, 0, 100, seed=42)
        assert arr1 == arr2

    def test_rand_float_array(self) -> None:
        arr = TestCases.rand_float_array(10, 0.0, 1.0)
        assert len(arr) == 10
        assert all(0.0 <= x <= 1.0 for x in arr)

    def test_nearly_sorted(self) -> None:
        arr = TestCases.nearly_sorted(10, 2)
        assert len(arr) == 10
        assert set(arr) == set(range(10))

    def test_reverse_sorted(self) -> None:
        arr = TestCases.reverse_sorted(5)
        assert arr == [4, 3, 2, 1, 0]

    def test_many_duplicates(self) -> None:
        arr = TestCases.many_duplicates(10, 3)
        assert len(arr) == 10
        assert len(set(arr)) <= 3
