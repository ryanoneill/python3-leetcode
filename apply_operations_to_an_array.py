from typing import List


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        for i in range(n):
            if i < n - 1:
                if nums[i] == nums[i + 1]:
                    nums[i] *= 2
                    nums[i + 1] = 0
            if nums[i] != 0:
                result.append(nums[i])

        while len(result) < n:
            result.append(0)

        return result
