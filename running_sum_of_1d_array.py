from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        sum = 0
        for num in nums:
            sum += num
            result.append(sum)
        return result
