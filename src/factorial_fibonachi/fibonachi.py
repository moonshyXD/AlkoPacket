class Fibonachi:
    @staticmethod
    def fibo(n: int) -> int:
        f0 = 0
        f1 = 1
        result: int
        for _ in range(n):
            result = f0 + f1
            f0, f1 = f1, result

        return result

    @staticmethod
    def fibo_recursive(n: int) -> int:
        if n in [0, 1]:
            return n

        return Fibonachi.fibo(n - 1) + Fibonachi.fibo(n - 2)

    @staticmethod
    def fibo_O1(int: int) -> int:
        pass
