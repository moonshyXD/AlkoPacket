from src.factorial_fibonachi.fibonachi import Fibonachi
from src.sorts.heap_sort import HeapSort


class AlgoPacket:
    def __init__(self):
        self.fib = Fibonachi()

    @staticmethod
    def run() -> None:
        test = [10, 1, 20, 20, 5, 100]
        result = HeapSort.execute(test)
        print(result)


if __name__ == "__main__":
    AlgoPacket.run()
