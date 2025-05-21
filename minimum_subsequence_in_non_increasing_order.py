from typing import List

class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        results = []
        nums.sort(reverse=True)
        total = sum(nums)
        current = 0
        goal = total // 2
        for num in nums:
            results.append(num)
            current += num
            if current > goal:
                break

        return results
