from src.utils.base import Sort


class QuickSort(Sort):
    def execute(self, arr: list[int]) -> list[int]:
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

        return self.execute(less_than) + equal + self.execute(higher_than)
