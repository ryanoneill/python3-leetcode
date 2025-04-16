from typing import List
from heapq import heappush, heappop

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = []
        for i, num in enumerate(nums):
            heappush(heap, (num, i))

        for i in range(k):
            _, index = heappop(heap)
            nums[index] *= multiplier
            heappush(heap, (nums[index], index))

        return nums
