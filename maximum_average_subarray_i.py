from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        sum = 0
        i = 0
        while i < k:
            sum += nums[i]
            i += 1
        result = float(sum) / k
        while i < n:
            sum += nums[i]
            sum -= nums[i-k]
            current = float(sum) / k
            result = max(current, result)
            i += 1
        return result

