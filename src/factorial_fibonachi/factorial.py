class Factorial:
    def factorial(self, n: int) -> int:
        result = 1
        for i in range(2, n):
            result *= i

        return result

    def factorial_recursive(self, n: int) -> int:
        if n == 1:
            return 1

        return self.factorial_recursive(n - 1) * n

    def factorial_O1(self, n: int) -> int:
        pass
