from typing import List


class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n

        seen = set()
        for i, num in enumerate(nums):
            seen.add(num)
            result[i] = len(seen)

        seen.clear()
        for i in range(n - 1, -1, -1):
            num = nums[i]
            seen.add(num)
            if i > 0:
                result[i - 1] -= len(seen)

        return result
