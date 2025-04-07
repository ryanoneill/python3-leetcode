from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1 for i in range(amount + 1)]
        dp[0] = 0

        for i in range(amount + 1):
            if dp[i] != -1:
                count = dp[i] + 1

                for coin in coins:
                    current = i + coin
                    if current <= amount:
                        if dp[current] == -1:
                            dp[current] = count
                        else:
                            dp[current] = min(dp[current], count)

        result = dp[amount]
        return result
