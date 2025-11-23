from src.factorial_fibonachi.fibonachi import Fibonachi
from src.sorts.heap_sort import HeapSort


class Lab3:
    def __init__(self):
        self.fib = Fibonachi()

    def run(self) -> None:
        test = [10, 1, 20, 20, 5, 100]
        result = HeapSort.execute(test)
        print(result)


if __name__ == "__main__":
    obj = Lab3()
    obj.run()
