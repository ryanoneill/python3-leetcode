from typing import List
from heapq import heappop, heappush

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        heap = []

        result = 1
        current = 0
        for interval in intervals:
            start, end = interval

            if current < start:
                current = start
            heappush(heap, end)

            while heap:
                next_end = heap[0]
                if next_end <= current:
                    heappop(heap)
                else:
                    break
            result = max(result, len(heap))

        return result








