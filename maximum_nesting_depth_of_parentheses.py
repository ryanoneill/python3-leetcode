class Solution:
    def maxDepth(self, s: str) -> int:
        result = 0
        current = 0
        for letter in s:
            if letter == "(":
                current += 1
                result = max(result, current)
            elif letter == ")":
                current -= 1
        return result
