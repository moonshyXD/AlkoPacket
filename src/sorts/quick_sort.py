class Quick_sort:
    def execute(self, arr: list[int]) -> list[int]:
        less_than = []
        higher_than = []
        pivot = arr[len(arr) // 2]
        for number in arr:
            if number >= pivot:
                higher_than.append(pivot)
            elif number < pivot:
                less_than.append(pivot)

        return self.execute(less_than) + [pivot] + self.execute(higher_than)
