from typing import List
from heapq import heappush, heappop


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        first = {}
        last = {}

        for index, letter in enumerate(s):
            if letter not in first:
                first[letter] = index
            last[letter] = index

        results = []
        heap = []
        for key in first.keys():
            i = first[key]
            j = last[key]
            heappush(heap, (i, j))

        start = 0
        end = 0
        while heap:
            i, j = heappop(heap)
            if i > end:
                results.append(end - start + 1)
                start = i
                end = j
            elif j > end:
                end = j

        results.append(end - start + 1)
        return results
