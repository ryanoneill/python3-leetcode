from typing import List

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        increasing = None
        
        result = 1
        current = 1

        last = nums[0]
        n = len(nums)

        for i in range(1, n):
            num = nums[i]
            if num > last:
                if increasing:
                    current += 1
                else:
                    current = 2
                    increasing = True
            elif num < last:
                if not increasing:
                    current += 1
                else:
                    current = 2
                    increasing = False
            else:
                current = 1
                increasing = None

            last = num
            result = max(result, current)

        return result
