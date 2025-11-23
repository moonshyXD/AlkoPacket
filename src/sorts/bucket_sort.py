from src.utils.base import BaseSort


class BucketSort(BaseSort):
    @staticmethod
    def execute(arr: list[float], buckets: int | None = None) -> list[float]:
        if buckets is None:
            buckets = 10

        array_buckets: list[list[float]] = [[] for _ in range(buckets)]
        for i in range(len(arr)):
            normalized = arr[i] / (max(arr) + 1)
            bucket_number = int(i * normalized)
            array_buckets[bucket_number].append(arr[i])

        sorted_array: list[float] = []
        for bucket in array_buckets:
            sorted_array.extend(BucketSort._insertion_sort(bucket))

        return sorted_array

    @staticmethod
    def _insertion_sort(arr: list[float]) -> list[float]:
        for a in range(1, len(arr)):
            b = a
            while b > 0 and arr[b - 1] > arr[b]:
                arr[b - 1], arr[b] = arr[b], arr[b - 1]
                b -= 1

        return arr
