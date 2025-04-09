from typing import List

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        result = -1
        smallest = nums[0]

        for num in nums:
            if num > smallest:
                diff = num - smallest
                result = max(result, diff)
            smallest = min(smallest, num)

        return result
