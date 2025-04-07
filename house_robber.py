from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        result = 0
        n = len(nums)

        if n == 0:
            result = 0
        elif n == 1:
            result = nums[0]
        else:
            dp = [0] * n

            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])

            for i in range(2, n):
                yes = nums[i] + dp[i - 2]
                no = dp[i - 1]
                dp[i] = max(yes, no)

            result = dp[-1]

        return result
