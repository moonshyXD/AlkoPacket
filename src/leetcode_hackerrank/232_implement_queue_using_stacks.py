from collections import deque


class MyQueue:
    def __init__(self) -> None:
        self.stack1: deque[int] = deque()
        self.stack2: deque[int] = deque()

    def push(self, x: int) -> None:
        """
        :type x: int
        :rtype: None
        """
        self.stack1.append(x)

    def pop(self) -> int:
        """
        :rtype: int
        """
        while len(self.stack1) > 1:
            self.stack2.append(self.stack1.pop())

        result = self.stack1.pop()

        while len(self.stack2) > 0:
            self.stack1.append(self.stack2.pop())

        return result

    def peek(self) -> int:
        """
        :rtype: int
        """
        while len(self.stack1) > 1:
            self.stack2.append(self.stack1.pop())

        result = self.stack1[-1]

        while len(self.stack2) > 0:
            self.stack1.append(self.stack2.pop())

        return result

    def empty(self) -> bool:
        """
        :rtype: bool
        """
        return len(self.stack1) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
