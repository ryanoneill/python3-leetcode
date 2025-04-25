from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        result = 0

        left = 0
        right = n - 1
        left_max = 0
        right_max = 0

        while left < right:
            left_height = height[left]
            right_height = height[right]

            if left_height < right_height:
                left_max = max(left_max, left_height)
                result += left_max - left_height
                left += 1
            else:
                right_max = max(right_max, right_height)
                result += right_max - right_height
                right -= 1

        return result
