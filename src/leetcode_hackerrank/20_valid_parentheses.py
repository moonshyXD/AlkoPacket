class Solution(object):
    def isValid(self, s: str) -> bool:
        """
        :type s: str
        :rtype: bool
        """
        brackets = []
        matching = {")": "(", "}": "{", "]": "["}

        for i in s:
            if i in "({[":
                brackets.append(i)
            elif i in ")}]":
                if not brackets or brackets[-1] != matching[i]:
                    return False
                brackets.pop()

        return not brackets
