from typing import List


class Solution:
    # j - i != nums[j] - nums[i]
    # is the same as
    # nums[i] - i != nums[j] - j
    def countBadPairs(self, nums: List[int]) -> int:
        result = 0
        counts = {}
        n = len(nums)
        for i in range(n):
            diff = nums[i] - i
            if diff in counts:
                counts[diff] += 1
            else:
                counts[diff] = 1
            result += (i + 1) - counts[diff]
        return result
