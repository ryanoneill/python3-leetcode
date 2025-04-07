class Solution:
    def scoreOfString(self, s: str) -> int:
        n = len(s)
        result = 0
        for i in range(1, n):
            previous = s[i - 1]
            current = s[i]
            result += abs(ord(previous) - ord(current))

        return result
