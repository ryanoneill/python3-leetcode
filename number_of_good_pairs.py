from collections import Counter
from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        result = 0
        counter = Counter(nums)

        for value in counter.values():
            if value >= 2:
                component = (value) * (value - 1) // 2
                result += component

        return result
