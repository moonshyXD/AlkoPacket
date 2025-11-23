class Solution(object):
    def climbStairs(self, n: int) -> int:
        """
        :type n: int
        :rtype: int
        """
        a, b = 1, 1
        for _ in range(1, n):
            c = a + b
            b = a
            a = c

        return a
