from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        right = 0
        n = len(nums)
        while right < n and nums[right] < 0:
            right += 1
        left = right - 1
        result = []
        while left > -1 or right < n:
            if left == -1:
                value = nums[right]
                value = value * value
                result.append(value)
                right += 1
            elif right == n:
                value = nums[left]
                value = value * value
                result.append(value)
                left -= 1
            else:
                left_value = nums[left]
                left_value = left_value * left_value
                right_value = nums[right]
                right_value = right_value * right_value
                if left_value < right_value:
                    result.append(left_value)
                    left -= 1
                else:
                    result.append(right_value)
                    right += 1
        return result
