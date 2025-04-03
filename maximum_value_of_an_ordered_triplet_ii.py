from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        result = 0
        diff_max = 0
        i_max = 0

        for num in nums:
            current = diff_max * num
            result = max(result, current)
            diff_max = max(diff_max, i_max - num)
            i_max = max(i_max, num)

        return result
