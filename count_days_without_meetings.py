from typing import List
from heapq import heappop, heapify


class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        n = days
        result = 0
        current = 1
        heapify(meetings)
        while meetings:
            start, end = heappop(meetings)
            if start == current:
                current = end + 1
            elif start > current:
                result += start - current
                current = end + 1
            elif end >= current:
                current = end + 1

        if current <= n:
            result += n - current + 1

        return result
