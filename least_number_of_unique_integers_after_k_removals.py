from collections import Counter
from heapq import heappush, heappop
from typing import List

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counts = Counter(arr)
        result = len(counts.keys())

        heap = []
        for value in counts.values():
            heappush(heap, value)

        while k > 0 and heap:
            value = heappop(heap)
            value -= 1
            if value == 0:
                result -= 1
            else:
                heappush(heap, value)
            k -= 1

        return result

