class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10 ** 9 + 7
        result = 0

        if n * k >= target:
            dp = [[0] * (target + 1) for _ in range(n + 1)]
            dp[0][0] = 1

            # For each roll of the die
            for roll in range(1, n + 1):
                # Loop through the possible outcomes (lowest, highest+1)
                for current_sum in range(roll, min(roll * k, target) + 1):
                    ways = 0

                    # Calculate how many ways we got there based on the different
                    # values of the die
                    for die in range(1, min(k, current_sum) + 1):
                        ways += dp[roll - 1][current_sum - die] % MOD

                    # Store that result
                    dp[roll][current_sum] = ways % MOD

            # Return how many different ways we could reach the target on n rolls
            result = dp[n][target]

        return result
