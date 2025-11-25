class Solution(object):
    def fib(self, n: int) -> int:
        """
        :type n: int
        :rtype: int
        """
        if n in (0, 1):
            return n

        a, b = 1, 0
        for _ in range(1, n):
            c = a + b
            b = a
            a = c

        return a
