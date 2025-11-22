class Fibonachi:
    def fibo(self, n: int) -> int:
        f0 = 0
        f1 = 1
        result: int
        for _ in range(n):
            result = f0 + f1
            f0, f1 = f1, result

        return result

    def fibo_recursive(self, n: int) -> int:
        if n in [0, 1]:
            return n

        return self.fibo(n - 1) + self.fibo(n - 2)

    def fibo_O1(self, int: int) -> int:
        pass
