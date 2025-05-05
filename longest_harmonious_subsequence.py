from collections import Counter
from typing import List

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        result = 0
        counts = Counter(nums)
        for key in counts.keys():
            if key + 1 in counts:
                current = counts[key] + counts[key+1]
                result = max(result, current)

        return result

