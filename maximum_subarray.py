from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)

        current = nums[0]
        result = current

        for i in range(1, n):
            num = nums[i]
            current = max(num, current + num)
            result = max(result, current)

        return result
