class Fibonachi:
    @staticmethod
    def fibo(n: int) -> int:
        """
        Вычисляет n-е число Фибоначчи итеративно.
        :param n: Номер искомого числа в последовательности.
        :return: n-е число Фибоначчи.
        """
        if n == 0:
            return 0
        if n == 1:
            return 1

        f0 = 0
        f1 = 1
        result = 0
        for _ in range(n - 1):
            result = f0 + f1
            f0, f1 = f1, result

        return result

    @staticmethod
    def fibo_recursive(n: int) -> int:
        """
        Вычисляет n-е число Фибоначчи рекурсивно.
        :param n: Номер искомого числа в последовательности.
        :return: n-е число Фибоначчи.
        """
        if n in [0, 1]:
            return n

        return Fibonachi.fibo_recursive(n - 1) + Fibonachi.fibo_recursive(
            n - 2
        )
