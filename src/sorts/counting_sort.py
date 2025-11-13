class Counting_sort:
    def execute(self, arr: list[int]) -> list[int]:
        n = max(arr)
        lst = [0] * (n + 1)
        for i in arr:
            lst[i] += 1

        result: list[int] = []
        for i in range(n + 1):
            while lst[i] != 0:
                result.append(i)
                lst[i] -= 1

        return result
