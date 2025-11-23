from src.utils.base import BaseSort


class CountingSort(BaseSort):
    @staticmethod
    def execute(arr: list[int]) -> list[int]:
        n = max(arr)
        lst = [0] * (n + 1)
        for i in arr:
            lst[i] += 1

        result: list[int] = []
        for i in range(n + 1):
            result.extend([i] * lst[i])

        return result
