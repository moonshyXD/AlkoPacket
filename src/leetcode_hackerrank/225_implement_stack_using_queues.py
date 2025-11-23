class MyStack(object):
    def __init__(self):
        from collections import deque

        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.q1.append(x)

    def pop(self):
        """
        :rtype: int
        """
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())

        result = self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1

        return result

    def top(self):
        """
        :rtype: int
        """
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())

        result = self.q1.popleft()
        self.q2.append(result)
        self.q1, self.q2 = self.q2, self.q1

        return result

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.q1) == 0
