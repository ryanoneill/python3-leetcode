from typing import List

class Solution:
    def sumDigits(self, num: int) -> int:
        result = 0
        working = num
        while working > 0:
            result += working % 10
            working //= 10
        return result

    def maximumSum(self, nums: List[int]) -> int:
        result = -1
        prevs = {}
        for num in nums:
            digits = self.sumDigits(num)
            if digits not in prevs:
                prevs[digits] = num
            else:
                current = prevs[digits] + num
                result = max(result, current)
                prevs[digits] = max(prevs[digits], num)
        return result
