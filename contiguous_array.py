from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        result = 0
        count = 0

        counts = {}
        counts[0] = -1
        for i, item in enumerate(nums):
            value = 1 if item == 1 else -1
            count += value
            if count in counts:
                result = max(result, i - counts[count])
            else:
                counts[count] = i

        return result
