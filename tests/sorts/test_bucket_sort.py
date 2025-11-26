from src.sorts.bucket_sort import BucketSort


class TestBucketSort:
    def test_empty(self) -> None:
        assert BucketSort.execute([]) == []

    def test_sorted(self) -> None:
        arr = [1.0, 2.0, 3.0, 4.0, 5.0]
        assert BucketSort.execute(arr.copy()) == arr

    def test_random(self) -> None:
        arr = [3.2, 1.5, 4.8, 2.1, 5.9]
        assert BucketSort.execute(arr.copy()) == sorted(arr)
