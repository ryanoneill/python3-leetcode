from heapq import heappush, heappop
from typing import List

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        n = len(events)
        max_end = max(event[1] for event in events)

        heap = []
        result = 0

        index = 0

        for day in range(1, max_end + 1):
            while index < n and events[index][0] <= day:
                heappush(heap, events[index][1])
                index += 1

            while heap:
                end = heappop(heap)
                if end >= day:
                    result += 1
                    break

        return result
