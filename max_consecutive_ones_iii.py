from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        remaining = k
        result = 0
        right = 0
        n = len(nums)
        left = 0
        current = 0
        while right < n:
            value = nums[right]
            if value == 1 or remaining > 0:
                current += 1
                result = max(result, current)
                if value == 0:
                    remaining -= 1
                right += 1
            else:
                value = nums[left]
                while value != 0:
                    left += 1
                    current -= 1
                    value = nums[left]
                current -= 1
                left += 1
                remaining += 1

        return result
