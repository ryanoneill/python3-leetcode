from typing import List

class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        results = []
        rem_start, rem_end = toBeRemoved

        for start, end in intervals:
            if start > rem_end or end < rem_start:
                results.append([start, end])
            else:
                if start < rem_start:
                    results.append([start, rem_start])
                if end > rem_end:
                    results.append([rem_end, end])

        return results

