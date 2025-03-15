from typing import List

class Solution:
    def run(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            yes = nums[i] + dp[i-2]
            no = dp[i-1]
            dp[i] = max(yes, no)

        return dp[-1]

    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        result = 0
        if n == 1:
            result = nums[0]
        elif n == 2:
            result = max(nums[0], nums[1])
        elif n > 2:
            first = self.run(nums[:-1])
            second = self.run(nums[1:])
            result = max(first, second)

        return result

