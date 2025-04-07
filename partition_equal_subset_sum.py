from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)

        if s % 2 != 0:
            return False

        target = s // 2
        dp = [False for _ in range(target + 1)]
        dp[0] = True

        for num in nums:
            for i in reversed(range(target + 1)):
                if dp[i]:
                    value = i + num
                    if value <= target:
                        dp[value] = True

        return dp[target]

