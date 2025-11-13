class Bubble_sort:
    def execute(self, arr: list[int]) -> list[int]:
        n = len(arr)
        result = arr.copy()
        for i in range(n):
            if result[i - 1] < result[i]:
                result[i - 1], result[i] = result[i], result[i - 1]

        return result
