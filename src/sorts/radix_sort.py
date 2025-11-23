from src.utils.base import Sort


class RadixSort(Sort):
    @staticmethod
    def execute(arr: list[int]) -> list[int]:
        max_num = max(arr)
        step = 1

        while max_num // step > 0:
            n = len(arr)
            res = [0] * n
            count = [0] * 10

            for num in arr:
                index = (num // step) % 10
                count[index] += 1

            for i in range(1, 10):
                count[i] += count[i - 1]

            for i in range(n - 1, -1, -1):
                index = (arr[i] // step) % 10
                res[count[index] - 1] = arr[i]
                count[index] -= 1

            for i in range(n):
                arr[i] = res[i]

            step *= 10
