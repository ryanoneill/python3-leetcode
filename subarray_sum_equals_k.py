from collections import defaultdict
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0

        counts = defaultdict(int)
        counts[0] = 1

        current = 0
        for num in nums:
            current += num
            diff = current - k
            result += counts[diff]
            counts[current] += 1

        return result
