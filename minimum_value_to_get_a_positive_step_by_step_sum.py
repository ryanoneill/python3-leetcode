from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        result = 1
        min_sum = 0
        sum = 0
        for num in nums:
            sum += num
            min_sum = min(sum, min_sum)
        if min_sum < 0:
            result = 1 - min_sum
        return result
