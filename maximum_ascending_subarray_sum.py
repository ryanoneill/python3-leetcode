from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        n = len(nums)

        last = nums[0]
        current = nums[0]
        result = current

        for i in range(1, n):
            num = nums[i]
            if num > last:
                current += num
            else:
                current = num
            last = num
            result = max(result, current)

        return result
