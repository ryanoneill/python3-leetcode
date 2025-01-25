from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        result = int(n * (n + 1) / 2)
        for num in nums:
            result -= num
        return result
