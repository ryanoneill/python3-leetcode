from typing import List

class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        counts = {}
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        result = -1
        for key, value in counts.items():
            if value == 1:
                result = max(result, key)
        return result
