from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[0] * (i + 1) for i in range(n)]

        for i, row in enumerate(reversed(triangle)):
            index = n - 1 - i
            for j, value in enumerate(row):
                if i == 0:
                    dp[index][j] = value
                else:
                    dp[index][j] = value + min(dp[index + 1][j], dp[index + 1][j + 1])

        return dp[0][0]
