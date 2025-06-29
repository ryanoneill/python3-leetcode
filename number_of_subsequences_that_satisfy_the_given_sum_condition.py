from typing import List

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10**9 + 7
        result = 0

        nums = sorted(nums)
        n = len(nums)

        left = 0
        right = n-1
        while left <= right:
            sum = nums[left] + nums[right]
            if sum <= target:
                part = pow(2, right - left, MOD) 
                result = (result + part) % MOD
                left += 1
            else:
                right -= 1

        return result
