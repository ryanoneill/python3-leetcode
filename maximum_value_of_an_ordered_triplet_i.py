from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0
        i_max = 0
        difference_max = 0
        for k in range(n):
            num = nums[k]
            current = difference_max * num
            result = max(result, current)

            difference_max = max(difference_max, i_max - num)
            i_max = max(i_max, num)

        return result
