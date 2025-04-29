from collections import Counter
from typing import List

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counts = Counter(nums)
        maximum = max(counts.keys())
        points = [0] * (maximum + 1)
        if 1 in counts:
            points[1] = counts[1]

        for i in range(2, maximum+1):
            without_i = points[i-1]
            with_i = points[i-2] + (counts.get(i, 0) * i)
            points[i] = max(without_i, with_i)

        return points[maximum]
