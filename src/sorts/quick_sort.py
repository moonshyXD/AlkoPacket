from src.utils.base import BaseSort


class QuickSort(BaseSort):
    @staticmethod
    def execute(arr: list[int]) -> list[int]:
        if len(arr) <= 1:
            return arr

        less_than = []
        higher_than = []
        equal = []
        pivot = arr[len(arr) // 2]
        for number in arr:
            if number > pivot:
                higher_than.append(number)
            elif number < pivot:
                less_than.append(number)
            else:
                equal.append(number)

        return (
            QuickSort.execute(less_than)
            + equal
            + QuickSort.execute(higher_than)
        )
