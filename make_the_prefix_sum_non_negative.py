from typing import List
from heapq import heappush, heappop

class Solution:
    def makePrefSumNonNegative(self, nums: List[int]) -> int:
        sum = 0
        result = 0
        negs = []

        for num in nums:
            if num < 0:
                heappush(negs, num)
            sum += num
            if sum < 0:
                result += 1
                sum -= heappop(negs)
        
        return result
