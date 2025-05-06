from typing import List

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        results = []
        for i in range(n):
            value = nums[nums[i]]
            results.append(value)

        return results

