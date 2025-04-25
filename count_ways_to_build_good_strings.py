class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10**9 + 7

        dp = [0] * (high + 1)
        dp[0] = 1

        for i in range(1, high + 1):
            value = 0
            if i >= zero:
                value += dp[i - zero]
            if i >= one:
                value += dp[i - one]
            dp[i] = value % MOD

        result = 0
        for i in range(low, high + 1):
            result += dp[i]
            result = result % MOD

        return result
