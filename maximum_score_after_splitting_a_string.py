class Solution:
    def maxScore(self, s: str) -> int:
        zeros = 0
        ones = 0

        n = len(s)
        for i in range(n):
            if s[i] == "1":
                ones += 1

        current = 0
        result = 0

        for i in range(0, n - 1):
            if s[i] == "0":
                zeros += 1
            else:
                ones -= 1
            current = zeros + ones
            result = max(result, current)

        return result
