class Factorial:
    @staticmethod
    def factorial(n: int) -> int:
        """
        Вычисляет факториал числа итеративно
        :param n: неотрицательное целое число
        :return: факториал n
        """
        if n == 0:
            return 1

        result = 1
        for i in range(1, n + 1):
            result *= i

        return result

    @staticmethod
    def factorial_recursive(n: int) -> int:
        """
        Вычисляет факториал рекурсивно
        :param n: неотрицательное целое число
        :return: факториал n
        """
        if n in [0, 1]:
            return 1

        return Factorial.factorial_recursive(n - 1) * n
