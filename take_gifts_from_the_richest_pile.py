import math
from heapq import heapify, heappop, heappush
from typing import List

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        n = len(gifts)
        result = 0
        for i in range(n):
            gifts[i] = -gifts[i]
        
        heapify(gifts)
        for i in range(k):
            count = -heappop(gifts)
            modified = int(math.floor(math.sqrt(count)))
            heappush(gifts, -modified)

        for num in gifts:
            result += -num

        return result
