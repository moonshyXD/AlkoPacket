from src.factorial_fibonachi.fibonachi import Fibonachi
from src.sorts.counting_sort import Counting_sort


class Lab3:
    def __init__(self):
        self.fib = Fibonachi()
        self.c_sort = Counting_sort()

    def run(self) -> None:
        test = [10, 1, 20, 20, 5, 100]
        result = self.c_sort.execute(test)
        print(result)


if __name__ == "__main__":
    obj = Lab3()
    obj.run()
