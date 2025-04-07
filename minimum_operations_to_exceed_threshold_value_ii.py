from typing import List
from heapq import heapify, heappush, heappop


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        result = 0
        heapify(nums)
        while len(nums) >= 2 and nums[0] < k:
            x = heappop(nums)
            y = heappop(nums)
            item = min(x, y) * 2 + max(x, y)
            heappush(nums, item)
            result += 1
        return result
