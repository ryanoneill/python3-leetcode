from typing import List


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        dp = [[0, 0, 0] for _ in range(n)]

        for i, cost in enumerate(reversed(costs)):
            red, blue, green = cost
            if i == 0:
                dp[i][0] = red
                dp[i][1] = blue
                dp[i][2] = green
            else:
                dp[i][0] = red + min(dp[i - 1][1], dp[i - 1][2])
                dp[i][1] = blue + min(dp[i - 1][0], dp[i - 1][2])
                dp[i][2] = green + min(dp[i - 1][0], dp[i - 1][1])

        return min(dp[n - 1])
