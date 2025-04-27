from typing import List

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        result = 0

        intervals.sort(key=lambda x: (x[0],-x[1]))

        ending = 0
        for _, end in intervals:
            if end > ending:
                result += 1
                ending = end

        return result
