from typing import List


class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        result = -1

        # O(n) for entire sum
        total = sum(nums)

        running = 0
        for i in range(len(nums)):
            value = nums[i]
            if running == (total - running - value):
                result = i
                break
            else:
                running += value

        return result
