from collections import Counter
from typing import List

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        counts = Counter(nums)
        maximum = max(counts.values())

        maxes = set()
        for num, count in counts.items():
            if count == maximum:
                maxes.add(num)

        indexes = {}
        for i, num in enumerate(nums):
            if num in maxes:
                if num in indexes:
                    indexes[num].append(i)
                else:
                    indexes[num] = [i]

        result = len(nums)
        for values in indexes.values():
            current = values[-1] - values[0] + 1
            result = min(result, current)

        return result
