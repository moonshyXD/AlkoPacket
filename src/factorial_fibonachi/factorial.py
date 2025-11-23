class Factorial:
    @staticmethod
    def factorial(n: int) -> int:
        result = 1
        for i in range(2, n):
            result *= i

        return result

    @staticmethod
    def factorial_recursive(n: int) -> int:
        if n == 1:
            return 1

        return Factorial.factorial_recursive(n - 1) * n

    @staticmethod
    def factorial_O1(n: int) -> int:
        pass
