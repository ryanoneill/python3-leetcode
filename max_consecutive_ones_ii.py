from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)

        left = 0
        flips = 0
        result = 0

        for right in range(n):
            num = nums[right]
            if num == 1:
                current = right - left + 1
                result = max(result, current)
            elif flips == 0:
                flips = 1
                current = right - left + 1
                result = max(result, current)
            else:
                while nums[left] != 0:
                    left += 1
                left += 1

        return result


